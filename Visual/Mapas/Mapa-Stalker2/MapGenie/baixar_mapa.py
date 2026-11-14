"""Baixa os tiles de um mapa do Map Genie (sem marcadores) e os limites das regiões.

Uso:
    python baixar_mapa.py <url-do-mapa> [--zoom N] [--saida PASTA] [--threads N]

Gera em PASTA:
    tiles_z<N>/<y>_<x>.<ext>   os tiles daquele zoom
    mapa.json                  grade de tiles + regiões já convertidas pra pixels da imagem final

Depois rode montar_mapa.ps1 apontando pra mesma pasta. Só usa a biblioteca padrão do Python.
"""
import argparse
import json
import math
import os
import re
import struct
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"


def http_get(url, referer=None, accept=None):
    headers = {"User-Agent": UA}
    if referer:
        headers["Referer"] = referer
    if accept:
        headers["Accept"] = accept
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def js_value(html, name):
    """Lê `window.<name> = <valor JSON>;` do HTML da página."""
    m = re.search(r"window\." + re.escape(name) + r"\s*=\s*", html)
    if not m:
        return None
    value, _ = json.JSONDecoder().raw_decode(html, m.end())
    return value


def jpeg_size(data):
    """(largura, altura) de um JPEG, lendo só o cabeçalho."""
    i = 2
    while i < len(data) - 9:
        marker, length = data[i + 1], struct.unpack(">H", data[i + 2:i + 4])[0]
        if marker in (0xC0, 0xC1, 0xC2):
            h, w = struct.unpack(">HH", data[i + 5:i + 9])
            return w, h
        i += 2 + length
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", help="link do mapa, ex.: https://mapgenie.io/stalker-2-heart-of-chornobyl/maps/the-zone")
    ap.add_argument("--zoom", type=int, help="zoom dos tiles (padrão: o máximo disponível)")
    ap.add_argument("--saida", help="pasta de saída (padrão: <slug-do-mapa> ao lado deste script)")
    ap.add_argument("--threads", type=int, default=16, help="downloads simultâneos (padrão: 16)")
    args = ap.parse_args()

    print("Lendo a página do mapa...")
    html = http_get(args.url).decode("utf-8")
    map_data = js_value(html, "mapData")
    if not map_data:
        sys.exit("Não achei window.mapData na página. O link é de um mapa do Map Genie?")
    tiles_cdn = js_value(html, "tilesCdnUrl") or "https://tiles.mapgenie.io/games/"

    tile_set = map_data["mapConfig"]["tile_sets"][0]
    bounds = {int(z): b for z, b in tile_set["bounds"].items()}
    zoom = args.zoom or tile_set.get("tiles_max_zoom") or max(bounds)
    if zoom not in bounds:
        sys.exit(f"Zoom {zoom} não existe. Disponíveis: {sorted(bounds)}")
    b = bounds[zoom]
    xmin, xmax, ymin, ymax = b["x"]["min"], b["x"]["max"], b["y"]["min"], b["y"]["max"]
    ext = tile_set.get("extension", "jpg")
    pattern = tile_set["pattern"]  # ex.: jogo/mapa/v4/{z}/{y}/{x}.jpg

    slug = map_data["map"]["slug"]
    saida = args.saida or os.path.join(os.path.dirname(os.path.abspath(__file__)), slug)
    tiles_dir = os.path.join(saida, f"tiles_z{zoom}")
    os.makedirs(tiles_dir, exist_ok=True)

    cols, rows = xmax - xmin + 1, ymax - ymin + 1
    print(f"Mapa: {map_data['map']['title']} | zoom {zoom} | {cols}x{rows} = {cols * rows} tiles")

    def baixar(yx):
        y, x = yx
        dest = os.path.join(tiles_dir, f"{y}_{x}.{ext}")
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            return None
        url = tiles_cdn + pattern.replace("{z}", str(zoom)).replace("{x}", str(x)).replace("{y}", str(y))
        erro = None
        for _ in range(3):
            try:
                data = http_get(url, referer="https://mapgenie.io/")
                with open(dest, "wb") as f:
                    f.write(data)
                return None
            except Exception as e:  # noqa: BLE001 - tenta de novo e reporta no fim
                erro = e
        return f"{y}/{x}: {erro}"

    jobs = [(y, x) for y in range(ymin, ymax + 1) for x in range(xmin, xmax + 1)]
    with ThreadPoolExecutor(args.threads) as ex:
        falhas = [r for r in ex.map(baixar, jobs) if r]
    print(f"Tiles: {len(jobs) - len(falhas)} ok, {len(falhas)} falharam")
    for f in falhas[:20]:
        print("  falhou:", f)

    with open(os.path.join(tiles_dir, f"{ymin}_{xmin}.{ext}"), "rb") as f:
        tile_size = (jpeg_size(f.read()) or (256, 256))[0] if ext in ("jpg", "jpeg") else 256

    # Regiões: mesma API que o site usa pra desenhar as bordas.
    regions = []
    origin = "{0.scheme}://{0.netloc}".format(urlparse(args.url))
    try:
        api = json.loads(http_get(f"{origin}/api/v1/maps/{map_data['map']['id']}/data",
                                  referer=args.url, accept="application/json"))
        world = tile_size * 2 ** zoom
        ox, oy = xmin * tile_size, ymin * tile_size

        def to_px(lng, lat):  # Web Mercator -> pixel da imagem montada
            s = math.sin(math.radians(lat))
            px = (lng + 180) / 360 * world
            py = (0.5 - math.log((1 + s) / (1 - s)) / (4 * math.pi)) * world
            return [round(px - ox, 1), round(py - oy, 1)]

        for r in api.get("regions") or []:
            rings = []
            for feat in r.get("features") or []:
                geom = feat["geometry"]
                polys = {"Polygon": [geom["coordinates"]], "MultiPolygon": geom["coordinates"]}.get(geom["type"], [])
                for poly in polys:
                    rings += [[to_px(*c[:2]) for c in ring] for ring in poly]
            if r.get("center_x") is not None and r.get("center_y") is not None:
                cx, cy = to_px(float(r["center_x"]), float(r["center_y"]))
            else:
                cx = cy = None
            regions.append({"title": r["title"], "cx": cx, "cy": cy, "rings": rings})
        print(f"Regiões: {len(regions)}")
    except Exception as e:  # noqa: BLE001 - mapa sem regiões não impede a montagem
        print(f"Não consegui baixar as regiões ({e}). A imagem limpa ainda pode ser montada.")

    info = {
        "title": map_data["map"]["title"], "slug": slug, "zoom": zoom,
        "xmin": xmin, "xmax": xmax, "ymin": ymin, "ymax": ymax,
        "tile_size": tile_size, "ext": ext, "tiles_dir": f"tiles_z{zoom}",
        "width": cols * tile_size, "height": rows * tile_size,
        "regions": regions,
    }
    with open(os.path.join(saida, "mapa.json"), "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False)
    print(f"Pronto: {saida}")
    print(f"Imagem final terá {info['width']}x{info['height']} px. Agora rode montar_mapa.ps1 -Pasta \"{saida}\"")


if __name__ == "__main__":
    main()
