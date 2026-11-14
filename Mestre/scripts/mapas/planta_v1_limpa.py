"""Planta de exemplo v1: estilo limpo (fundo escuro, traço simples, legenda ao lado).
Molde: copie, troque o cenário e gere. Uso: python planta_v1_limpa.py saida.svg"""
import math, sys
sys.stdout.reconfigure(encoding="utf-8")

S = 40          # px por metro
OX, OY = 70, 90 # origem da casa
W, H = 16, 11   # casa em metros

def X(m): return OX + S * m
def Y(m): return OY + S * m

BG = "#14161b"; FLOOR = "#22252d"; WALL = "#d9d3c5"; FURN = "#353a45"
TXT = "#e9e6df"; MUTED = "#8b909c"; WIN = "#8fb3c9"; DOORC = "#a5794a"
YEL = "#e8b931"; ALLY = "#5fb3a1"; RED = "#d24a3c"; COVER = "#c9a66b"

out = []
a = out.append

a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1010 660" width="1010" height="660" font-family="Segoe UI, system-ui, sans-serif">')
a(f'''<defs>
  <pattern id="fog" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
    <rect width="10" height="10" fill="#0c0d10"/>
    <line x1="0" y1="0" x2="0" y2="10" stroke="#1d2027" stroke-width="3"/>
  </pattern>
  <linearGradient id="dark" x1="0" x2="1" y1="0" y2="0">
    <stop offset="0" stop-color="#000" stop-opacity="0"/>
    <stop offset="1" stop-color="#000" stop-opacity="0.6"/>
  </linearGradient>
  <radialGradient id="beam" cx="0" cy="0.5" r="1">
    <stop offset="0" stop-color="{YEL}" stop-opacity="0.22"/>
    <stop offset="1" stop-color="{YEL}" stop-opacity="0"/>
  </radialGradient>
</defs>''')
a(f'<rect width="1010" height="660" fill="{BG}"/>')

# título
a(f'<text x="{OX}" y="42" fill="{TXT}" font-size="20" font-weight="600">Planta de exemplo · casa térrea</text>')
a(f'<text x="{OX}" y="64" fill="{MUTED}" font-size="13">Rodada 2 · só o que a personagem já viu · 1 quadradinho do fundo = 1 m</text>')

# grade leve de 1 m (só referência visual)
for i in range(W + 1):
    a(f'<line x1="{X(i)}" y1="{Y(0)}" x2="{X(i)}" y2="{Y(H)}" stroke="#ffffff" stroke-opacity="0.035"/>')
for j in range(H + 1):
    a(f'<line x1="{X(0)}" y1="{Y(j)}" x2="{X(W)}" y2="{Y(j)}" stroke="#ffffff" stroke-opacity="0.035"/>')

def rect_m(x, y, w, h, **kw):
    attrs = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in kw.items())
    return f'<rect x="{X(x)}" y="{Y(y)}" width="{S*w}" height="{S*h}" {attrs}/>'

# pisos explorados
for r in [(0, 0, 8, 6), (8, 0, 5, 6), (0, 6, 16, 1.5), (0, 7.5, 6, 3.5)]:
    a(rect_m(*r, fill=FLOOR))
# grade por cima do piso
for i in range(W + 1):
    a(f'<line x1="{X(i)}" y1="{Y(0)}" x2="{X(i)}" y2="{Y(H)}" stroke="#ffffff" stroke-opacity="0.04"/>')
for j in range(H + 1):
    a(f'<line x1="{X(0)}" y1="{Y(j)}" x2="{X(W)}" y2="{Y(j)}" stroke="#ffffff" stroke-opacity="0.04"/>')

# escuro no fim do corredor
a(rect_m(7, 6, 9, 1.5, fill="url(#dark)"))

# não explorado
for r in [(13, 0, 3, 6), (6, 7.5, 3, 3.5), (9, 7.5, 7, 3.5)]:
    a(rect_m(*r, fill="url(#fog)"))
    cx, cy = X(r[0] + r[2] / 2), Y(r[1] + r[3] / 2)
    a(f'<text x="{cx}" y="{cy + 8}" fill="#3b404b" font-size="26" font-weight="700" text-anchor="middle">?</text>')

# móveis
a(rect_m(1, 0.5, 3, 1, fill=FURN, rx=4))                 # sofá
a(rect_m(2, 2.3, 1.6, 1, fill=FURN, rx=3))               # mesinha
a(rect_m(8.4, 0, 4.2, 0.7, fill=FURN))                    # pia e fogão
a(rect_m(0.3, 8.4, 2, 2.3, fill=FURN, rx=3))             # cama
a(rect_m(4.4, 10.3, 1.4, 0.6, fill=FURN))                 # cômoda

# balcão = cobertura
a(rect_m(7.7, 0.5, 0.6, 2.5, fill="#5a4a36", stroke=COVER, stroke_width=2, stroke_dasharray="4 3", rx=2))

# paredes
def wall(x1, y1, x2, y2):
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{WALL}" stroke-width="6" stroke-linecap="square"/>')

def hwall(y, x1, x2, gaps=()):
    cur = x1
    for g1, g2 in sorted(gaps):
        if g1 > cur: wall(cur, y, g1, y)
        cur = g2
    if cur < x2: wall(cur, y, x2, y)

def vwall(x, y1, y2, gaps=()):
    cur = y1
    for g1, g2 in sorted(gaps):
        if g1 > cur: wall(x, cur, x, g1)
        cur = g2
    if cur < y2: wall(x, cur, x, y2)

hwall(0, 0, 16, [(2, 4), (9.5, 11.5)])            # janelas na parede de cima
hwall(11, 0, 16, [(2, 4)])                         # janela do quarto
vwall(0, 0, 11, [(2.5, 3.5)])                      # porta da rua
vwall(16, 0, 11)
vwall(8, 4, 6)                                     # resto da parede sala/cozinha (americana)
vwall(13, 0, 6, [(4, 5)])                          # cozinha / área de serviço
hwall(6, 0, 16, [(1, 2.5), (10, 11)])              # sala e cozinha -> corredor
hwall(7.5, 0, 16, [(4, 5), (7, 8), (12, 13)])      # corredor -> quartos e banheiro
vwall(6, 7.5, 11)
vwall(9, 7.5, 11)

# janelas
def window(x1, y1, x2, y2):
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{WIN}" stroke-width="6"/>')
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{BG}" stroke-width="2"/>')
window(2, 0, 4, 0); window(9.5, 0, 11.5, 0); window(2, 11, 4, 11)

# portas abertas: arco de abertura
def open_door_h(y, x1, x2, up=True):
    r = S * (x2 - x1); sgn = -1 if up else 1
    a(f'<path d="M {X(x1)} {Y(y)} L {X(x1)} {Y(y) + sgn*r} A {r} {r} 0 0 {1 if up else 0} {X(x2)} {Y(y)}" fill="none" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="3 3"/>')
open_door_h(6, 10, 11, up=False)   # cozinha -> corredor
open_door_h(7.5, 4, 5, up=False)   # quarto 1

# porta da rua (aberta) + saída
a(f'<path d="M {X(0)} {Y(2.5)} L {X(1)} {Y(2.5)} A {S} {S} 0 0 1 {X(0)} {Y(3.5)}" fill="none" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="3 3"/>')
a(f'<path d="M {X(0) - 12} {Y(3)} l -26 0 m 9 -7 l -9 7 l 9 7" fill="none" stroke="{TXT}" stroke-width="2"/>')
a(f'<text x="{X(0) - 40}" y="{Y(3) + 24}" fill="{MUTED}" font-size="12" text-anchor="middle">rua</text>')

# portas fechadas
def closed_door(x1, y1, x2, y2):
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{DOORC}" stroke-width="5"/>')
closed_door(13, 4, 13, 5); closed_door(7, 7.5, 8, 7.5); closed_door(12, 7.5, 13, 7.5)

# nomes dos cômodos
def label(x, y, t):
    a(f'<text x="{X(x)}" y="{Y(y)}" fill="{MUTED}" font-size="11" letter-spacing="2" text-anchor="middle">{t}</text>')
label(4.5, 5.4, "SALA"); label(11.9, 5.4, "COZINHA"); label(3.2, 6.95, "CORREDOR"); label(3.6, 9.6, "QUARTO")

# lanterna da personagem (cone pra cozinha)
ix, iy = 7.2, 2.2
a(f'<path d="M {X(ix)} {Y(iy)} L {X(12.6)} {Y(0.4)} L {X(12.6)} {Y(4.6)} Z" fill="url(#beam)"/>')

# linhas de distância
def dist_line(x1, y1, x2, y2, txt, lx, ly):
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{TXT}" stroke-opacity="0.55" stroke-width="1.5" stroke-dasharray="6 4"/>')
    w = 7.2 * len(txt) + 14
    a(f'<rect x="{X(lx) - w/2}" y="{Y(ly) - 11}" width="{w}" height="20" rx="10" fill="{BG}" stroke="{TXT}" stroke-opacity="0.35"/>')
    a(f'<text x="{X(lx)}" y="{Y(ly) + 4}" fill="{TXT}" font-size="12" text-anchor="middle">{txt}</text>')

e1 = (11, 3.1); e2 = (11.3, 6.8)
d1 = math.dist((ix, iy), e1); d2 = math.dist((ix, iy), e2)
dist_line(ix, iy, *e1, f"{round(d1)} m", 9.1, 3.2)
dist_line(ix, iy, *e2, f"{round(d2)} m", 9.3, 5.55)

# fichas
def token(x, y, fill, t, dark=True):
    a(f'<circle cx="{X(x)}" cy="{Y(y)}" r="14" fill="{fill}" stroke="#0b0c0f" stroke-width="2.5"/>')
    a(f'<text x="{X(x)}" y="{Y(y) + 5}" fill="{"#111" if dark else TXT}" font-size="14" font-weight="700" text-anchor="middle">{t}</text>')

token(ix, iy, YEL, "P")
token(1.8, 4.6, ALLY, "A")
token(*e1, RED, "1", dark=False)
token(*e2, RED, "2", dark=False)

# ouvido, não visto
a(f'<circle cx="{X(13.3)}" cy="{Y(9.3)}" r="15" fill="none" stroke="{RED}" stroke-width="2" stroke-dasharray="4 3"/>')
a(f'<text x="{X(13.3)}" y="{Y(9.3) + 5}" fill="{RED}" font-size="14" font-weight="700" text-anchor="middle">?</text>')

# régua
by = Y(H) + 42
a(f'<line x1="{X(0)}" y1="{by}" x2="{X(10)}" y2="{by}" stroke="{YEL}" stroke-width="3"/>')
for t in (0, 5, 10):
    a(f'<line x1="{X(t)}" y1="{by - 6}" x2="{X(t)}" y2="{by + 6}" stroke="{YEL}" stroke-width="2"/>')
a(f'<text x="{X(10) + 10}" y="{by + 4}" fill="{TXT}" font-size="12">10 m</text>')

# linha de posição
py = by + 40
a(f'<text x="{X(0)}" y="{py}" fill="{TXT}" font-size="13"><tspan font-weight="600">Posição:</tspan> Você atrás do balcão (cobertura), lanterna na cozinha. Aliado na porta da rua. 1: na cozinha. 2: no corredor escuro.</text>')
a(f'<text x="{X(0)}" y="{py + 20}" fill="{TXT}" font-size="13">Barulho atrás da porta do quarto dos fundos.</text>')

# legenda
lx = X(W) + 48; ly = Y(0) + 6
a(f'<text x="{lx}" y="{ly}" fill="{TXT}" font-size="14" font-weight="600">Legenda</text>')
rows = [
    ("tok", YEL, "P", "personagem"),
    ("tok", ALLY, "A", "aliado"),
    ("tok", RED, "1", "ameaça vista"),
    ("heard", None, None, "ouvido, não visto"),
    ("cover", None, None, "cobertura"),
    ("open", None, None, "porta aberta"),
    ("closed", None, None, "porta fechada"),
    ("win", None, None, "janela"),
    ("fog", None, None, "não explorado"),
    ("dark", None, None, "escuro"),
    ("beam", None, None, "luz da lanterna"),
    ("dist", None, None, "distância"),
]
y = ly + 32
for kind, col, t, name in rows:
    cx = lx + 14
    if kind == "tok":
        a(f'<circle cx="{cx}" cy="{y}" r="11" fill="{col}" stroke="#0b0c0f" stroke-width="2"/>')
        a(f'<text x="{cx}" y="{y + 4}" fill="{"#111" if col != RED else TXT}" font-size="11" font-weight="700" text-anchor="middle">{t}</text>')
    elif kind == "heard":
        a(f'<circle cx="{cx}" cy="{y}" r="11" fill="none" stroke="{RED}" stroke-width="2" stroke-dasharray="4 3"/>')
        a(f'<text x="{cx}" y="{y + 4}" fill="{RED}" font-size="11" font-weight="700" text-anchor="middle">?</text>')
    elif kind == "cover":
        a(f'<rect x="{cx - 12}" y="{y - 6}" width="24" height="12" rx="2" fill="#5a4a36" stroke="{COVER}" stroke-width="2" stroke-dasharray="4 3"/>')
    elif kind == "open":
        a(f'<path d="M {cx - 10} {y + 8} L {cx - 10} {y - 10} A 18 18 0 0 1 {cx + 8} {y + 8}" fill="none" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="3 3"/>')
        a(f'<line x1="{cx - 14}" y1="{y + 8}" x2="{cx - 10}" y2="{y + 8}" stroke="{WALL}" stroke-width="5"/><line x1="{cx + 8}" y1="{y + 8}" x2="{cx + 14}" y2="{y + 8}" stroke="{WALL}" stroke-width="5"/>')
    elif kind == "closed":
        a(f'<line x1="{cx - 14}" y1="{y}" x2="{cx - 8}" y2="{y}" stroke="{WALL}" stroke-width="5"/><line x1="{cx - 8}" y1="{y}" x2="{cx + 8}" y2="{y}" stroke="{DOORC}" stroke-width="5"/><line x1="{cx + 8}" y1="{y}" x2="{cx + 14}" y2="{y}" stroke="{WALL}" stroke-width="5"/>')
    elif kind == "win":
        a(f'<line x1="{cx - 12}" y1="{y}" x2="{cx + 12}" y2="{y}" stroke="{WIN}" stroke-width="6"/><line x1="{cx - 12}" y1="{y}" x2="{cx + 12}" y2="{y}" stroke="{BG}" stroke-width="2"/>')
    elif kind == "fog":
        a(f'<rect x="{cx - 12}" y="{y - 9}" width="24" height="18" fill="url(#fog)" stroke="#2a2e37"/>')
    elif kind == "dark":
        a(f'<rect x="{cx - 12}" y="{y - 9}" width="24" height="18" fill="{FLOOR}"/><rect x="{cx - 12}" y="{y - 9}" width="24" height="18" fill="url(#dark)"/>')
    elif kind == "beam":
        a(f'<path d="M {cx - 12} {y} L {cx + 12} {y - 9} L {cx + 12} {y + 9} Z" fill="{YEL}" fill-opacity="0.25"/>')
    elif kind == "dist":
        a(f'<line x1="{cx - 12}" y1="{y}" x2="{cx + 12}" y2="{y}" stroke="{TXT}" stroke-opacity="0.55" stroke-width="1.5" stroke-dasharray="6 4"/>')
    a(f'<text x="{lx + 38}" y="{y + 4}" fill="{TXT}" font-size="13">{name}</text>')
    y += 31

a('</svg>')

path = sys.argv[1]
open(path, "w", encoding="utf-8").write("\n".join(out))
print("ok", path, round(d1, 2), round(d2, 2))
