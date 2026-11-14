"""Planta de exemplo v2: estilo ilustrado (piso com textura, móveis de cima, luz, quintal).
Mesmo cenário da v1. Molde: copie, troque o cenário e gere. Uso: python planta_v2_ilustrada.py saida.svg"""
import math, random, sys
sys.stdout.reconfigure(encoding="utf-8")
random.seed(7)

S = 40
OX, OY = 110, 130
W, H = 16, 11
CW, CH = 1090, 740
MAPW = 830           # largura da área do mapa (quintal)
TOP, BOT = 92, 616   # faixa do quintal

def X(m): return OX + S * m
def Y(m): return OY + S * m

BG = "#121318"; TXT = "#ece7dc"; MUTED = "#a9a49a"
WALL_D = "#24180f"; WALL_L = "#8a6446"; POST = "#5e412b"
GLASS = "#a9cbe0"; DOOR = "#7a5636"
YEL = "#e8b931"; ALLY = "#4fb39d"; RED = "#cf3f33"; COVER = "#e0b860"

o = []; a = o.append

a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CW} {CH}" width="{CW}" height="{CH}" font-family="Segoe UI, system-ui, sans-serif">')
a(f'''<defs>
  <!-- madeira: tábuas de 25 cm, emendas desencontradas -->
  <pattern id="wood" width="160" height="20" patternUnits="userSpaceOnUse">
    <rect width="160" height="10" fill="#5d3d2b"/>
    <rect y="10" width="160" height="10" fill="#54372a"/>
    <line x1="0" y1="0" x2="160" y2="0" stroke="#2e1d14" stroke-width="1.2"/>
    <line x1="0" y1="10" x2="160" y2="10" stroke="#2e1d14" stroke-width="1.2"/>
    <line x1="58" y1="0" x2="58" y2="10" stroke="#2e1d14" stroke-width="1.2"/>
    <line x1="132" y1="10" x2="132" y2="20" stroke="#2e1d14" stroke-width="1.2"/>
  </pattern>
  <!-- ladrilho xadrez gasto -->
  <pattern id="tile" width="40" height="40" patternUnits="userSpaceOnUse">
    <rect width="40" height="40" fill="#4b4451"/>
    <rect width="20" height="20" fill="#766d7c"/>
    <rect x="20" y="20" width="20" height="20" fill="#766d7c"/>
    <path d="M0 0H40M0 20H40M0 0V40M20 0V40" stroke="#2c2830" stroke-width="1"/>
  </pattern>
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.012 0.45" numOctaves="2" seed="4" result="n"/>
    <feColorMatrix in="n" type="saturate" values="0" result="g"/>
    <feComponentTransfer in="g" result="gl"><feFuncR type="linear" slope="0.45" intercept="0.68"/><feFuncG type="linear" slope="0.45" intercept="0.68"/><feFuncB type="linear" slope="0.45" intercept="0.68"/></feComponentTransfer>
    <feBlend in="SourceGraphic" in2="gl" mode="multiply" result="b"/>
    <feComposite in="b" in2="SourceGraphic" operator="in"/>
  </filter>
  <filter id="dirt" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="3" seed="11" result="n"/>
    <feColorMatrix in="n" type="saturate" values="0" result="g"/>
    <feComponentTransfer in="g" result="gl"><feFuncR type="linear" slope="0.8" intercept="0.45"/><feFuncG type="linear" slope="0.8" intercept="0.45"/><feFuncB type="linear" slope="0.8" intercept="0.45"/></feComponentTransfer>
    <feBlend in="SourceGraphic" in2="gl" mode="multiply" result="b"/>
    <feComposite in="b" in2="SourceGraphic" operator="in"/>
  </filter>
  <filter id="grass" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.012" numOctaves="4" seed="2" result="n"/>
    <feColorMatrix in="n" type="saturate" values="0" result="g"/>
    <feComponentTransfer in="g" result="gl"><feFuncR type="linear" slope="0.9" intercept="0.4"/><feFuncG type="linear" slope="0.9" intercept="0.4"/><feFuncB type="linear" slope="0.9" intercept="0.4"/></feComponentTransfer>
    <feBlend in="SourceGraphic" in2="gl" mode="multiply"/>
  </filter>
  <filter id="smoke" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
    <feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="3" seed="9" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0.13  0 0 0 0 0.14  0 0 0 0 0.17  0 0 0 1.0 -0.3" result="s"/>
    <feComposite in="s" in2="SourceGraphic" operator="in" result="sc"/>
    <feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="sc"/></feMerge>
  </filter>
  <filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="5"/></filter>
  <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="5" dy="7" stdDeviation="6" flood-color="#000" flood-opacity="0.6"/></filter>
  <filter id="tshadow" x="-50%" y="-50%" width="200%" height="200%"><feDropShadow dx="2" dy="3" stdDeviation="2" flood-color="#000" flood-opacity="0.7"/></filter>
  <linearGradient id="dark" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset="0.55" stop-color="#000" stop-opacity="0.55"/><stop offset="1" stop-color="#000" stop-opacity="0.8"/></linearGradient>
  <linearGradient id="moonD" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe3f5" stop-opacity="0.28"/><stop offset="1" stop-color="#cfe3f5" stop-opacity="0"/></linearGradient>
  <linearGradient id="moonU" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#cfe3f5" stop-opacity="0.28"/><stop offset="1" stop-color="#cfe3f5" stop-opacity="0"/></linearGradient>
  <radialGradient id="beam" cx="0" cy="0.5" r="1"><stop offset="0" stop-color="#ffd77a" stop-opacity="0.42"/><stop offset="1" stop-color="#ffd77a" stop-opacity="0"/></radialGradient>
  <radialGradient id="vig" cx="0.35" cy="0.35" r="0.85"><stop offset="0.45" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.45"/></radialGradient>
  <radialGradient id="treeG" cx="0.4" cy="0.35" r="0.7"><stop offset="0" stop-color="#4f7346"/><stop offset="1" stop-color="#22371f"/></radialGradient>
</defs>''')

a(f'<rect width="{CW}" height="{CH}" fill="{BG}"/>')

# ---------- quintal
a(f'<rect x="0" y="{TOP}" width="{MAPW}" height="{BOT-TOP}" fill="#3a5634" filter="url(#grass)"/>')
for _ in range(260):   # tufos
    x = random.uniform(8, MAPW - 8); y = random.uniform(TOP + 6, BOT - 6)
    if X(-0.4) < x < X(W + 0.4) and Y(-0.4) < y < Y(H + 0.4): continue
    c = random.choice(["#2b4227", "#4a6b40", "#2f4a2b"])
    a(f'<path d="M{x:.1f} {y:.1f} l-2 -5 M{x:.1f} {y:.1f} l1 -6 M{x:.1f} {y:.1f} l3 -4" stroke="{c}" stroke-width="1.2" fill="none"/>')

# caminho de terra até a porta da rua
path_d = f"M {X(0)} {Y(2.4)} C {X(-1)} {Y(2.3)}, {X(-1.6)} {Y(3.4)}, {X(-1.9)} {Y(5)} S {X(-2.2)} {Y(9)}, {X(-2.4)} {Y(12.2)} L {X(-0.6)} {Y(12.2)} C {X(-0.7)} {Y(9)}, {X(-0.5)} {Y(5.5)}, {X(0)} {Y(3.6)} Z"
a(f'<path d="{path_d}" fill="#8f7a58" filter="url(#soft)" opacity="0.9"/>')
a(f'<path d="{path_d}" fill="#9a845f" filter="url(#dirt)" opacity="0.85"/>')

def tree(cx, cy, r):
    a(f'<ellipse cx="{cx+8}" cy="{cy+10}" rx="{r*1.05}" ry="{r}" fill="#000" opacity="0.35" filter="url(#soft)"/>')
    for dx, dy, rr in [(-r*.35, -r*.2, r*.7), (r*.35, -r*.15, r*.65), (0, r*.3, r*.7), (0, -r*.1, r*.75)]:
        a(f'<circle cx="{cx+dx:.1f}" cy="{cy+dy:.1f}" r="{rr:.1f}" fill="url(#treeG)" stroke="#1b2b18" stroke-width="1.5"/>')
tree(788, 168, 30); tree(778, 560, 24); tree(48, 140, 26)
for bx, by in [(790, 330), (40, 560)]:
    a(f'<circle cx="{bx}" cy="{by}" r="12" fill="#2e4a2a" stroke="#1b2b18"/>')

# ---------- casa: sombra e piso
a(f'<rect x="{X(0)}" y="{Y(0)}" width="{S*W}" height="{S*H}" fill="#000" filter="url(#shadow)"/>')

def rm(x, y, w, h): return f'x="{X(x)}" y="{Y(y)}" width="{S*w}" height="{S*h}"'

a('<g filter="url(#grain)">')
for r in [(0, 0, 8, 6), (0, 6, 16, 1.5), (0, 7.5, 6, 3.5)]:
    a(f'<rect {rm(*r)} fill="url(#wood)"/>')
a(f'<rect {rm(8, 0, 5, 6)} fill="url(#tile)"/>')
a('</g>')

# grade de 1 m, bem leve
for i in range(W + 1):
    a(f'<line x1="{X(i)}" y1="{Y(0)}" x2="{X(i)}" y2="{Y(H)}" stroke="#fff" stroke-opacity="0.05"/>')
for j in range(H + 1):
    a(f'<line x1="{X(0)}" y1="{Y(j)}" x2="{X(W)}" y2="{Y(j)}" stroke="#fff" stroke-opacity="0.05"/>')

# manchas e sujeira
for (cx, cy, rx, ry) in [(5.2, 4.8, 0.9, 0.5), (12.2, 6.9, 0.8, 0.35), (3.5, 10.4, 0.6, 0.3), (10.0, 1.7, 0.5, 0.35)]:
    a(f'<ellipse cx="{X(cx)}" cy="{Y(cy)}" rx="{S*rx}" ry="{S*ry}" fill="#140b07" opacity="0.45" filter="url(#soft)"/>')

# ---------- móveis
def shade(): return 'filter="url(#tshadow)"'
# sala: tapete, sofá, mesinha, poltrona, cadeira caída, estante
a(f'<rect {rm(0.8, 1.7, 4.2, 2.8)} fill="#5e1f22" stroke="#3a1214" stroke-width="2"/>')
a(f'<rect {rm(1.0, 1.9, 3.8, 2.4)} fill="none" stroke="#a0653f" stroke-width="1.5" stroke-dasharray="6 3"/>')
a(f'<g {shade()}><rect {rm(1, 0.35, 3.2, 1.05)} rx="6" fill="#4e4a5a"/>'
  f'<rect {rm(1, 0.35, 3.2, 0.35)} rx="5" fill="#3c3946"/>'
  f'<rect {rm(1, 0.35, 0.3, 1.05)} rx="5" fill="#3c3946"/><rect {rm(3.9, 0.35, 0.3, 1.05)} rx="5" fill="#3c3946"/>'
  f'<line x1="{X(2.6)}" y1="{Y(0.75)}" x2="{X(2.6)}" y2="{Y(1.35)}" stroke="#2c2a33"/></g>')
a(f'<g {shade()}><rect {rm(2.1, 2.5, 1.5, 0.9)} rx="3" fill="#6b4a33" stroke="#3e2a1d"/>'
  f'<rect {rm(2.4, 2.75, 0.35, 0.25)} fill="#d8d0bd" transform="rotate(12 {X(2.55)} {Y(2.85)})"/></g>')
a(f'<g {shade()} transform="rotate(-25 {X(5.4)} {Y(1.5)})"><rect {rm(4.9, 1.0, 1.0, 1.0)} rx="7" fill="#6a2a2e"/><rect {rm(4.9, 1.0, 1.0, 0.3)} rx="5" fill="#4d1d20"/></g>')
a(f'<g {shade()} transform="rotate(70 {X(5.9)} {Y(3.9)})"><rect {rm(5.6, 3.6, 0.6, 0.6)} fill="#6b4a33" stroke="#3e2a1d"/>'
  f'<rect {rm(5.6, 3.5, 0.6, 0.12)} fill="#4a3222"/></g>')
a(f'<g {shade()}><rect {rm(0.1, 4.4, 0.45, 1.5)} fill="#4a3222" stroke="#2e1d14"/>'
  + "".join(f'<rect {rm(0.15, 4.5 + i*0.35, 0.35, 0.25)} fill="{c}"/>' for i, c in enumerate(["#7a3b2e", "#3e5a6b", "#8a7a4f", "#5a3a5e"])) + '</g>')
# papéis espalhados
for _ in range(9):
    px, py = random.uniform(0.6, 6.8), random.uniform(3.6, 7.2)
    a(f'<rect x="{X(px):.1f}" y="{Y(py):.1f}" width="9" height="12" fill="#d9d1bd" opacity="0.8" transform="rotate({random.randint(-60,60)} {X(px):.1f} {Y(py):.1f})"/>')

# cozinha: bancada com pia e fogão, geladeira, mesa com cadeiras
a(f'<g {shade()}><rect {rm(8.3, 0, 4.4, 0.75)} fill="#7d7a76" stroke="#3a3836"/>'
  f'<rect {rm(9.5, 0.12, 1.0, 0.5)} rx="4" fill="#4a4e54" stroke="#2a2c30"/><circle cx="{X(10)}" cy="{Y(0.37)}" r="2.5" fill="#22252a"/>'
  f'<rect {rm(11.3, 0.06, 1.2, 0.63)} fill="#2d2f33"/>'
  + "".join(f'<circle cx="{X(11.6 + dx)}" cy="{Y(0.25 + dy)}" r="5" fill="none" stroke="#6a6d73" stroke-width="2"/>' for dx in (0, 0.6) for dy in (0, 0.3)) + '</g>')
a(f'<g {shade()}><rect {rm(8.2, 4.4, 0.85, 0.85)} rx="3" fill="#c9c6bf" stroke="#77736c"/><line x1="{X(8.3)}" y1="{Y(4.75)}" x2="{X(8.95)}" y2="{Y(4.75)}" stroke="#77736c"/></g>')
a(f'<g {shade()}><circle cx="{X(10.6)}" cy="{Y(4.2)}" r="{S*0.5}" fill="#6b4a33" stroke="#3e2a1d" stroke-width="2"/>'
  f'<rect {rm(10.4, 3.25, 0.45, 0.4)} rx="3" fill="#4a3222"/>'
  f'<rect {rm(11.2, 4.4, 0.45, 0.4)} rx="3" fill="#4a3222" transform="rotate(30 {X(11.4)} {Y(4.6)})"/></g>')
a(f'<circle cx="{X(10.45)}" cy="{Y(4.1)}" r="5" fill="#d9d1bd" opacity="0.9"/>')

# quarto: tapete, cama, criado-mudo, cômoda, caixas
a(f'<rect {rm(2.7, 8.6, 2.6, 1.7)} rx="4" fill="#3d4a5e" stroke="#26303e" stroke-width="2"/>')
a(f'<g {shade()}><rect {rm(0.3, 8.0, 2.1, 2.7)} rx="4" fill="#6b4a33" stroke="#3e2a1d"/>'
  f'<rect {rm(0.4, 8.1, 1.9, 2.5)} rx="3" fill="#b8b2a6"/>'
  f'<rect {rm(0.55, 8.2, 0.75, 0.45)} rx="6" fill="#ece6d8"/><rect {rm(1.4, 8.2, 0.75, 0.45)} rx="6" fill="#ece6d8"/>'
  f'<path d="M {X(0.4)} {Y(9.1)} L {X(2.3)} {Y(8.95)} L {X(2.3)} {Y(10.6)} L {X(0.4)} {Y(10.6)} Z" fill="#6d3940"/>'
  f'<path d="M {X(0.4)} {Y(9.1)} L {X(2.3)} {Y(8.95)} L {X(2.3)} {Y(9.25)} L {X(0.4)} {Y(9.35)} Z" fill="#8a4a52"/></g>')
a(f'<g {shade()}><rect {rm(2.55, 8.0, 0.55, 0.5)} fill="#5a3d2a" stroke="#3e2a1d"/><circle cx="{X(2.82)}" cy="{Y(8.25)}" r="5" fill="#d8c79a" opacity="0.8"/></g>')
a(f'<g {shade()}><rect {rm(4.2, 10.3, 1.6, 0.6)} fill="#5a3d2a" stroke="#3e2a1d"/></g>')
for (bx, by, bw, rot) in [(4.6, 8.0, 0.6, 12), (5.2, 8.4, 0.5, -8)]:
    a(f'<g {shade()} transform="rotate({rot} {X(bx)} {Y(by)})"><rect {rm(bx, by, bw, bw)} fill="#a07d52" stroke="#5e4630"/><line x1="{X(bx)}" y1="{Y(by + bw/2)}" x2="{X(bx + bw)}" y2="{Y(by + bw/2)}" stroke="#5e4630"/></g>')

# balcão (cobertura)
a(f'<g {shade()}><rect {rm(7.7, 0.5, 0.6, 2.5)} rx="2" fill="#6b4a33"/><rect {rm(7.75, 0.55, 0.5, 2.4)} fill="#80593c"/></g>')
a(f'<rect {rm(7.62, 0.42, 0.76, 2.66)} rx="3" fill="none" stroke="{COVER}" stroke-width="2" stroke-dasharray="5 3"/>')

# ---------- luz e escuridão
a(f'<polygon points="{X(2)},{Y(0)} {X(4)},{Y(0)} {X(5.3)},{Y(3.4)} {X(1.4)},{Y(3.4)}" fill="url(#moonD)"/>')
a(f'<polygon points="{X(9.5)},{Y(0)} {X(11.5)},{Y(0)} {X(12.4)},{Y(2.8)} {X(9.0)},{Y(2.8)}" fill="url(#moonD)"/>')
a(f'<polygon points="{X(2)},{Y(11)} {X(4)},{Y(11)} {X(4.9)},{Y(8.6)} {X(1.4)},{Y(8.6)}" fill="url(#moonU)"/>')
a(f'<rect {rm(0, 0, W, H)} fill="url(#vig)"/>')
a(f'<rect {rm(6.5, 6, 9.5, 1.5)} fill="url(#dark)"/>')

ix, iy = 7.2, 2.2
a(f'<path d="M {X(ix)} {Y(iy)} L {X(12.8)} {Y(0.2)} L {X(12.8)} {Y(4.9)} Z" fill="url(#beam)"/>')
a(f'<circle cx="{X(ix)}" cy="{Y(iy)}" r="34" fill="#ffd77a" opacity="0.12" filter="url(#soft)"/>')

# não explorado (por cima de tudo, menos paredes)
for r in [(13, 0, 3, 6), (6, 7.5, 3, 3.5), (9, 7.5, 7, 3.5)]:
    a(f'<rect {rm(*r)} fill="#07080a" filter="url(#smoke)"/>')
    a(f'<text x="{X(r[0] + r[2]/2)}" y="{Y(r[1] + r[3]/2) + 9}" fill="#3a3f4a" font-size="28" font-weight="700" text-anchor="middle">?</text>')

# ---------- paredes
segs = []
def wall(x1, y1, x2, y2): segs.append((x1, y1, x2, y2))
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

hwall(0, 0, 16, [(2, 4), (9.5, 11.5)])
hwall(11, 0, 16, [(2, 4)])
vwall(0, 0, 11, [(2.5, 3.5)])
vwall(16, 0, 11)
vwall(8, 4, 6)
vwall(13, 0, 6, [(4, 5)])
hwall(6, 0, 16, [(1, 2.5), (10, 11)])
hwall(7.5, 0, 16, [(4, 5), (7, 8), (12, 13)])
vwall(6, 7.5, 11)
vwall(9, 7.5, 11)

for (x1, y1, x2, y2) in segs:
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{WALL_D}" stroke-width="10" stroke-linecap="square"/>')
for (x1, y1, x2, y2) in segs:
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{WALL_L}" stroke-width="3.5" stroke-linecap="square"/>')
# pilares nos encontros
posts = {(0, 0), (16, 0), (0, 11), (16, 11), (8, 6), (13, 0), (13, 6), (0, 6), (16, 6), (0, 7.5), (16, 7.5), (6, 7.5), (9, 7.5), (6, 11), (9, 11), (8, 4)}
for (px, py) in posts:
    a(f'<rect x="{X(px) - 7}" y="{Y(py) - 7}" width="14" height="14" fill="{POST}" stroke="{WALL_D}" stroke-width="2"/>')

# janelas
def window(x1, y1, x2, y2):
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{WALL_D}" stroke-width="8"/>')
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{GLASS}" stroke-width="3"/>')
    mx, my = (X(x1) + X(x2)) / 2, (Y(y1) + Y(y2)) / 2
    a(f'<rect x="{mx - 2}" y="{my - 5}" width="4" height="10" fill="{WALL_D}"/>')
window(2, 0, 4, 0); window(9.5, 0, 11.5, 0); window(2, 11, 4, 11)

# portas abertas: folha + arco
def open_door(hx, hy, lx, ly, ex, ey, sweep):
    a(f'<path d="M {X(lx)} {Y(ly)} A {S} {S} 0 0 {sweep} {X(ex)} {Y(ey)}" fill="none" stroke="#d8cdb8" stroke-opacity="0.35" stroke-width="1.2" stroke-dasharray="3 3"/>')
    a(f'<line x1="{X(hx)}" y1="{Y(hy)}" x2="{X(lx)}" y2="{Y(ly)}" stroke="{DOOR}" stroke-width="5" stroke-linecap="round"/>')
open_door(10, 6, 10, 7, 11, 6, 0)       # cozinha -> corredor
open_door(4, 7.5, 4, 8.5, 5, 7.5, 0)    # quarto
open_door(0, 3.5, 1, 3.5, 0, 2.5, 0)    # porta da rua

# portas fechadas
def closed(x1, y1, x2, y2):
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{WALL_D}" stroke-width="9"/>')
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{DOOR}" stroke-width="6"/>')
closed(13, 4, 13, 5); closed(7, 7.5, 8, 7.5); closed(12, 7.5, 13, 7.5)

# ---------- rótulos dos cômodos
def label(x, y, t):
    a(f'<text x="{X(x)}" y="{Y(y)}" fill="#e6dccb" fill-opacity="0.75" font-size="11" letter-spacing="2.5" text-anchor="middle" stroke="#000" stroke-opacity="0.6" stroke-width="3" paint-order="stroke">{t}</text>')
label(4.4, 5.55, "SALA"); label(12.0, 5.55, "COZINHA"); label(3.2, 6.95, "CORREDOR"); label(3.3, 10.8, "QUARTO")

# saída
a(f'<path d="M {X(-1.2)} {Y(3)} l -30 0 m 10 -8 l -10 8 l 10 8" fill="none" stroke="{TXT}" stroke-width="2.5" stroke-opacity="0.9"/>')
a(f'<text x="{X(-1.95)}" y="{Y(3) + 26}" fill="{TXT}" font-size="12" text-anchor="middle" stroke="#000" stroke-opacity="0.6" stroke-width="3" paint-order="stroke">rua</text>')

# ---------- distâncias
def dist_line(x1, y1, x2, y2, txt, lx, ly):
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{TXT}" stroke-opacity="0.75" stroke-width="1.6" stroke-dasharray="6 4"/>')
    w = 7.2 * len(txt) + 16
    a(f'<rect x="{X(lx) - w/2}" y="{Y(ly) - 11}" width="{w}" height="21" rx="10.5" fill="#121318" fill-opacity="0.92" stroke="{TXT}" stroke-opacity="0.45"/>')
    a(f'<text x="{X(lx)}" y="{Y(ly) + 4}" fill="{TXT}" font-size="12" text-anchor="middle">{txt}</text>')
e1 = (11, 3.1); e2 = (11.3, 6.8)
dist_line(ix, iy, *e1, f"{round(math.dist((ix, iy), e1))} m", 9.1, 3.25)
dist_line(ix, iy, *e2, f"{round(math.dist((ix, iy), e2))} m", 9.3, 5.55)

# ---------- fichas
def token(x, y, fill, t, txt="#111"):
    a(f'<g filter="url(#tshadow)"><circle cx="{X(x)}" cy="{Y(y)}" r="16" fill="#0d0e11"/>'
      f'<circle cx="{X(x)}" cy="{Y(y)}" r="13.5" fill="{fill}"/>'
      f'<circle cx="{X(x)}" cy="{Y(y)}" r="13.5" fill="none" stroke="#fff" stroke-opacity="0.45" stroke-width="1.2"/></g>')
    a(f'<text x="{X(x)}" y="{Y(y) + 5}" fill="{txt}" font-size="14" font-weight="700" text-anchor="middle">{t}</text>')
token(ix, iy, YEL, "P"); token(1.8, 4.6, ALLY, "A"); token(*e1, RED, "1", TXT); token(*e2, RED, "2", TXT)
a(f'<circle cx="{X(13.3)}" cy="{Y(9.3)}" r="16" fill="#000" fill-opacity="0.4" stroke="{RED}" stroke-width="2.2" stroke-dasharray="4 3"/>')
a(f'<text x="{X(13.3)}" y="{Y(9.3) + 5}" fill="{RED}" font-size="15" font-weight="700" text-anchor="middle">?</text>')

# ---------- título, régua, posição
a(f'<text x="{OX - 70}" y="44" fill="{TXT}" font-size="21" font-weight="600">Planta de exemplo · casa térrea</text>')
a(f'<text x="{OX - 70}" y="68" fill="{MUTED}" font-size="13">Rodada 2 · só o que a personagem já viu · grade de 1 m</text>')
by = BOT + 34
a(f'<line x1="{OX - 70}" y1="{by}" x2="{OX - 70 + S*10}" y2="{by}" stroke="{YEL}" stroke-width="3"/>')
for t in (0, 5, 10):
    a(f'<line x1="{OX - 70 + S*t}" y1="{by - 6}" x2="{OX - 70 + S*t}" y2="{by + 6}" stroke="{YEL}" stroke-width="2"/>')
a(f'<text x="{OX - 70 + S*10 + 12}" y="{by + 4}" fill="{TXT}" font-size="12">10 m</text>')
py = by + 40
a(f'<text x="{OX - 70}" y="{py}" fill="{TXT}" font-size="13"><tspan font-weight="600">Posição:</tspan> Você atrás do balcão (cobertura), lanterna na cozinha. Aliado na porta da rua. 1: na cozinha. 2: no corredor escuro.</text>')
a(f'<text x="{OX - 70}" y="{py + 20}" fill="{TXT}" font-size="13">Barulho atrás da porta do quarto dos fundos.</text>')

# ---------- legenda
lx = MAPW + 30; ly = TOP + 22
a(f'<text x="{lx}" y="{ly}" fill="{TXT}" font-size="14" font-weight="600">Legenda</text>')
y = ly + 34
def row(name):
    global y
    a(f'<text x="{lx + 40}" y="{y + 4}" fill="{TXT}" font-size="13">{name}</text>'); y += 33
cx = lx + 14
for col, t, name, tc in [(YEL, "P", "personagem", "#111"), (ALLY, "A", "aliado", "#111"), (RED, "1", "ameaça vista", TXT)]:
    a(f'<circle cx="{cx}" cy="{y}" r="13" fill="#0d0e11"/><circle cx="{cx}" cy="{y}" r="11" fill="{col}"/><text x="{cx}" y="{y + 4}" fill="{tc}" font-size="11" font-weight="700" text-anchor="middle">{t}</text>'); row(name)
a(f'<circle cx="{cx}" cy="{y}" r="12" fill="none" stroke="{RED}" stroke-width="2" stroke-dasharray="4 3"/><text x="{cx}" y="{y + 4}" fill="{RED}" font-size="11" font-weight="700" text-anchor="middle">?</text>'); row("ouvido, não visto")
a(f'<rect x="{cx - 13}" y="{y - 7}" width="26" height="14" rx="2" fill="#80593c" stroke="{COVER}" stroke-width="2" stroke-dasharray="5 3"/>'); row("cobertura")
a(f'<line x1="{cx - 14}" y1="{y + 8}" x2="{cx - 9}" y2="{y + 8}" stroke="{WALL_L}" stroke-width="5"/><line x1="{cx + 9}" y1="{y + 8}" x2="{cx + 14}" y2="{y + 8}" stroke="{WALL_L}" stroke-width="5"/>'
  f'<line x1="{cx - 9}" y1="{y + 8}" x2="{cx - 9}" y2="{y - 10}" stroke="{DOOR}" stroke-width="4" stroke-linecap="round"/>'
  f'<path d="M {cx - 9} {y - 10} A 18 18 0 0 1 {cx + 9} {y + 8}" fill="none" stroke="#d8cdb8" stroke-opacity="0.45" stroke-dasharray="3 3"/>'); row("porta aberta")
a(f'<line x1="{cx - 14}" y1="{y}" x2="{cx - 8}" y2="{y}" stroke="{WALL_L}" stroke-width="5"/><line x1="{cx - 8}" y1="{y}" x2="{cx + 8}" y2="{y}" stroke="{DOOR}" stroke-width="6"/><line x1="{cx + 8}" y1="{y}" x2="{cx + 14}" y2="{y}" stroke="{WALL_L}" stroke-width="5"/>'); row("porta fechada")
a(f'<line x1="{cx - 13}" y1="{y}" x2="{cx + 13}" y2="{y}" stroke="{WALL_D}" stroke-width="8"/><line x1="{cx - 13}" y1="{y}" x2="{cx + 13}" y2="{y}" stroke="{GLASS}" stroke-width="3"/>'); row("janela")
a(f'<rect x="{cx - 13}" y="{y - 10}" width="26" height="20" fill="#07080a" stroke="#2a2e37"/><text x="{cx}" y="{y + 5}" fill="#3a3f4a" font-size="13" font-weight="700" text-anchor="middle">?</text>'); row("não explorado")
a(f'<rect x="{cx - 13}" y="{y - 10}" width="26" height="20" fill="#54372a"/><rect x="{cx - 13}" y="{y - 10}" width="26" height="20" fill="url(#dark)"/>'); row("escuro")
a(f'<path d="M {cx - 13} {y} L {cx + 13} {y - 10} L {cx + 13} {y + 10} Z" fill="#ffd77a" fill-opacity="0.45"/>'); row("lanterna")
a(f'<path d="M {cx - 6} {y - 10} L {cx + 6} {y - 10} L {cx + 12} {y + 10} L {cx - 12} {y + 10} Z" fill="#cfe3f5" fill-opacity="0.3"/>'); row("luar pela janela")
a(f'<line x1="{cx - 13}" y1="{y}" x2="{cx + 13}" y2="{y}" stroke="{TXT}" stroke-opacity="0.75" stroke-width="1.6" stroke-dasharray="6 4"/>'); row("distância")

a('</svg>')
open(sys.argv[1], "w", encoding="utf-8").write("\n".join(o))
print("ok", sys.argv[1])
