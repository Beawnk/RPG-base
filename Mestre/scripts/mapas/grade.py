"""Grade de coordenadas pras plantas (pra quem joga poder dizer "vou pra D7").

Colunas em letras, linhas em números, tipo batalha naval. Sem I e O nas colunas (confundem com
1 e 0). A grade só NOMEIA lugares: a distância é medida em linha reta, em metros, nunca contando
casas. Se o sistema tem faixas de alcance, passe-as em --faixas.

Na planta (importar no gerador, que fica na mesma pasta):
    from grade import Grade
    G = Grade(x0, y0, x1, y1, cel=1)      # área coberta, em metros; cel = metros por casa
    o.extend(G.linhas(X, Y))              # traços da grade por cima da foto
    o.extend(G.rotulos(X, Y, afasta=17))  # letras em cima e números à esquerda, fora da foto
    G.coord(7.2, 2.2)  -> "J4"            G.centro("D7") -> (x, y) em metros

Na sessão, medir uma distância (mesma área e casa da planta):
    python grade.py dist D7 J4 --x0 -1.5 --y0 -1 --cel 1
    -> D7 → J4: 6.7 m
    python grade.py dist D7 J4 --x0 -1.5 --y0 -1 --cel 1 --faixas "2=perto,10=curto,30=longo"
    -> D7 → J4: 6.7 m · curto
--faixas: "limite em metros=nome", do menor pro maior; são as faixas de alcance do sistema da
campanha (Sistemas/<sistema>.md, "Combate"). Sem --faixas, sai só a distância.
"""
import argparse, math, re, sys

LETRAS = "ABCDEFGHJKLMNPQRSTUVWXYZ"   # sem I e O


def letra(i):
    s = ""; i += 1
    while i:
        i, r = divmod(i - 1, len(LETRAS)); s = LETRAS[r] + s
    return s


def indice(s):
    n = 0
    for ch in s.upper():
        n = n * len(LETRAS) + LETRAS.index(ch) + 1
    return n - 1


def ler_faixas(txt):
    """"2=perto,10=curto" -> [(2.0, "perto"), (10.0, "curto")]"""
    faixas = []
    for parte in (txt or "").split(","):
        if "=" in parte:
            lim, nome = parte.split("=", 1)
            faixas.append((float(lim), nome.strip()))
    return sorted(faixas)


def alcance(m, faixas):
    """Nome da faixa de alcance em que a distância cai; vazio se o sistema não usa faixas."""
    if not faixas: return ""
    for lim, nome in faixas:
        if m <= lim: return nome
    return f"além de {faixas[-1][1]}"


class Grade:
    def __init__(self, x0, y0, x1, y1, cel=1.0):
        self.x0, self.y0, self.x1, self.y1, self.cel = x0, y0, x1, y1, cel
        self.ncol = math.ceil((x1 - x0) / cel - 1e-9)
        self.nlin = math.ceil((y1 - y0) / cel - 1e-9)

    def coord(self, x, y):
        c = int((x - self.x0) // self.cel); l = int((y - self.y0) // self.cel)
        return f"{letra(c)}{l + 1}"

    def centro(self, cod):
        m = re.fullmatch(r"([A-Za-z]+)(\d+)", cod.strip())
        if not m: raise ValueError(f"coordenada inválida: {cod}")
        c, l = indice(m.group(1)), int(m.group(2)) - 1
        return self.x0 + (c + 0.5) * self.cel, self.y0 + (l + 0.5) * self.cel

    def linhas(self, X, Y, cor="#f3e7c8", op=0.3, larg=1):
        o = []
        for i in range(self.ncol + 1):
            x = min(self.x0 + i * self.cel, self.x1)
            o.append(f'<line x1="{X(x):.1f}" y1="{Y(self.y0):.1f}" x2="{X(x):.1f}" y2="{Y(self.y1):.1f}" stroke="{cor}" stroke-opacity="{op}" stroke-width="{larg}"/>')
        for j in range(self.nlin + 1):
            y = min(self.y0 + j * self.cel, self.y1)
            o.append(f'<line x1="{X(self.x0):.1f}" y1="{Y(y):.1f}" x2="{X(self.x1):.1f}" y2="{Y(y):.1f}" stroke="{cor}" stroke-opacity="{op}" stroke-width="{larg}"/>')
        return o

    def rotulos(self, X, Y, afasta=17, fonte="Courier New, Courier, monospace", cor="#2a1c12", tam=12):
        o = []
        for i in range(self.ncol):
            a = self.x0 + i * self.cel; b = min(a + self.cel, self.x1)
            o.append(f'<text x="{X((a + b) / 2):.1f}" y="{Y(self.y0) - afasta:.1f}" fill="{cor}" font-family="{fonte}" font-size="{tam}" '
                     f'font-weight="700" text-anchor="middle">{letra(i)}</text>')
        for j in range(self.nlin):
            a = self.y0 + j * self.cel; b = min(a + self.cel, self.y1)
            o.append(f'<text x="{X(self.x0) - afasta + 4:.1f}" y="{Y((a + b) / 2) + tam * 0.35:.1f}" fill="{cor}" font-family="{fonte}" '
                     f'font-size="{tam}" font-weight="700" text-anchor="end">{j + 1}</text>')
        return o


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description="Distância entre duas casas da grade")
    p.add_argument("acao", choices=["dist"]); p.add_argument("de"); p.add_argument("para")
    p.add_argument("--x0", type=float, default=0); p.add_argument("--y0", type=float, default=0)
    p.add_argument("--cel", type=float, default=1)
    p.add_argument("--faixas", default="", help='faixas de alcance do sistema: "2=perto,10=curto,30=longo"')
    a = p.parse_args()
    g = Grade(a.x0, a.y0, a.x0 + 1, a.y0 + 1, a.cel)
    d = math.dist(g.centro(a.de), g.centro(a.para))
    nome = alcance(d, ler_faixas(a.faixas))
    print(f"{a.de.upper()} → {a.para.upper()}: {d:.1f} m" + (f" · {nome}" if nome else ""))
