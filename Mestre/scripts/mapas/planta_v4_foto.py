"""Planta de exemplo v4: folha de arquivo (papel, datilografia, carimbo, anotações) com o mapa
como FOTO AÉREA colada no papel (fita adesiva, borda de foto, cor envelhecida), anotada por cima.
Mesmo cenário da v1-v3. Molde: copie, troque o cenário e gere.
Uso: python planta_v4_foto.py saida.svg [--grade [metros por casa]]
--grade: coordenadas tipo batalha naval (ver grade.py); sem número, 1 m por casa."""
import math, random, sys
from grade import Grade
sys.stdout.reconfigure(encoding="utf-8")
random.seed(7)
GRADE_M = None
if "--grade" in sys.argv:
    k = sys.argv.index("--grade")
    GRADE_M = float(sys.argv[k + 1]) if k + 1 < len(sys.argv) and sys.argv[k + 1].replace(".", "", 1).isdigit() else 1.0

S = 40
OX, OY = 150, 190 + (16 if GRADE_M else 0)   # com grade, desce um pouco pra caber as letras
W, H = 16, 11
CW, CH = 1140, 810

def X(m): return OX + S * m
def Y(m): return OY + S * m
def rm(x, y, w, h): return f'x="{X(x)}" y="{Y(y)}" width="{S*w}" height="{S*h}"'

# papel / anotação
PAPER = "#d8c7a0"; PAPER_L = "#ecdfbf"; INK = "#2a1c12"; INK_S = "#5a4430"
RED = "#8e1b13"; REDP = "#a3261b"; YEL = "#e2b22c"; ALLY = "#3f8577"
TYPE = "Courier New, Courier, monospace"
HAND = "Segoe Print, Bradley Hand, Comic Sans MS, cursive"
# foto
WALL_D = "#24180f"; WALL_L = "#8a6446"; POST = "#5e412b"; GLASS = "#a9cbe0"; DOOR = "#7a5636"

# recorte da foto (em metros)
PX0, PY0, PX1, PY1 = -1.5, -1.0, 17.0, 11.9
PCX, PCY = (X(PX0) + X(PX1)) / 2, (Y(PY0) + Y(PY1)) / 2
ROT = -0.7
G = Grade(PX0, PY0, PX1, PY1, GRADE_M) if GRADE_M else None
def cc(x, y): return f" ({G.coord(x, y)})" if G else ""
def letra_ult():
    from grade import letra
    return f"A–{letra(G.ncol - 1)}"

o = []; a = o.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CW} {CH}" width="{CW}" height="{CH}">')
a(f'''<defs>
  <!-- papel -->
  <filter id="paper" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
    <feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="3" seed="3" result="fib"/>
    <feColorMatrix in="fib" type="saturate" values="0" result="fg"/>
    <feComponentTransfer in="fg" result="fl"><feFuncR type="linear" slope="0.22" intercept="0.86"/><feFuncG type="linear" slope="0.22" intercept="0.86"/><feFuncB type="linear" slope="0.22" intercept="0.86"/></feComponentTransfer>
    <feTurbulence type="fractalNoise" baseFrequency="0.006" numOctaves="3" seed="8" result="mot"/>
    <feColorMatrix in="mot" type="saturate" values="0" result="mg"/>
    <feComponentTransfer in="mg" result="ml"><feFuncR type="linear" slope="0.5" intercept="0.68"/><feFuncG type="linear" slope="0.5" intercept="0.66"/><feFuncB type="linear" slope="0.5" intercept="0.6"/></feComponentTransfer>
    <feBlend in="SourceGraphic" in2="fl" mode="multiply" result="p1"/>
    <feBlend in="p1" in2="ml" mode="multiply" result="p2"/>
    <feComposite in="p2" in2="SourceGraphic" operator="in"/>
  </filter>
  <filter id="rough" x="-2%" y="-2%" width="104%" height="104%">
    <feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="2" seed="6" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="9" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <filter id="stamp" x="-10%" y="-10%" width="120%" height="120%" color-interpolation-filters="sRGB">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="21" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.2 1.5" result="holes"/>
    <feComposite in="SourceGraphic" in2="holes" operator="in" result="s"/>
    <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="1" seed="4" result="d"/>
    <feDisplacementMap in="s" in2="d" scale="2" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <filter id="graphite" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
    <feTurbulence type="fractalNoise" baseFrequency="0.5" numOctaves="2" seed="15" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0.1  0 0 0 0 0.085  0 0 0 0 0.07  0 0 0 -1.4 1.25" result="g"/>
    <feComposite in="g" in2="SourceGraphic" operator="in"/>
  </filter>
  <filter id="blot" x="-10%" y="-10%" width="120%" height="120%">
    <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="3" seed="31" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="14" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <filter id="tapeedge" x="-5%" y="-20%" width="110%" height="140%">
    <feTurbulence type="fractalNoise" baseFrequency="0.25" numOctaves="1" seed="40" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="4" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <filter id="blur2"><feGaussianBlur stdDeviation="2"/></filter>
  <filter id="blur6" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="6"/></filter>
  <filter id="printshadow" x="-5%" y="-5%" width="110%" height="115%"><feDropShadow dx="3" dy="5" stdDeviation="5" flood-color="#2a1608" flood-opacity="0.55"/></filter>
  <filter id="tshadow" x="-50%" y="-50%" width="200%" height="200%"><feDropShadow dx="1.5" dy="2.5" stdDeviation="1.5" flood-color="#000" flood-opacity="0.6"/></filter>

  <!-- foto: texturas do lugar -->
  <pattern id="wood" width="160" height="20" patternUnits="userSpaceOnUse">
    <rect width="160" height="10" fill="#5d3d2b"/><rect y="10" width="160" height="10" fill="#54372a"/>
    <line x1="0" y1="0" x2="160" y2="0" stroke="#2e1d14" stroke-width="1.2"/><line x1="0" y1="10" x2="160" y2="10" stroke="#2e1d14" stroke-width="1.2"/>
    <line x1="58" y1="0" x2="58" y2="10" stroke="#2e1d14" stroke-width="1.2"/><line x1="132" y1="10" x2="132" y2="20" stroke="#2e1d14" stroke-width="1.2"/>
  </pattern>
  <pattern id="tile" width="40" height="40" patternUnits="userSpaceOnUse">
    <rect width="40" height="40" fill="#4b4451"/><rect width="20" height="20" fill="#766d7c"/><rect x="20" y="20" width="20" height="20" fill="#766d7c"/>
    <path d="M0 0H40M0 20H40M0 0V40M20 0V40" stroke="#2c2830" stroke-width="1"/>
  </pattern>
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.012 0.45" numOctaves="2" seed="4" result="n"/>
    <feColorMatrix in="n" type="saturate" values="0" result="g"/>
    <feComponentTransfer in="g" result="gl"><feFuncR type="linear" slope="0.45" intercept="0.68"/><feFuncG type="linear" slope="0.45" intercept="0.68"/><feFuncB type="linear" slope="0.45" intercept="0.68"/></feComponentTransfer>
    <feBlend in="SourceGraphic" in2="gl" mode="multiply" result="b"/><feComposite in="b" in2="SourceGraphic" operator="in"/>
  </filter>
  <filter id="dirt" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="3" seed="11" result="n"/>
    <feColorMatrix in="n" type="saturate" values="0" result="g"/>
    <feComponentTransfer in="g" result="gl"><feFuncR type="linear" slope="0.8" intercept="0.45"/><feFuncG type="linear" slope="0.8" intercept="0.45"/><feFuncB type="linear" slope="0.8" intercept="0.45"/></feComponentTransfer>
    <feBlend in="SourceGraphic" in2="gl" mode="multiply" result="b"/><feComposite in="b" in2="SourceGraphic" operator="in"/>
  </filter>
  <filter id="grass" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.012" numOctaves="4" seed="2" result="n"/>
    <feColorMatrix in="n" type="saturate" values="0" result="g"/>
    <feComponentTransfer in="g" result="gl"><feFuncR type="linear" slope="0.9" intercept="0.4"/><feFuncG type="linear" slope="0.9" intercept="0.4"/><feFuncB type="linear" slope="0.9" intercept="0.4"/></feComponentTransfer>
    <feBlend in="SourceGraphic" in2="gl" mode="multiply"/>
  </filter>
  <filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="5"/></filter>
  <filter id="hshadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="5" dy="7" stdDeviation="6" flood-color="#000" flood-opacity="0.6"/></filter>
  <filter id="fshadow" x="-50%" y="-50%" width="200%" height="200%"><feDropShadow dx="2" dy="3" stdDeviation="2" flood-color="#000" flood-opacity="0.7"/></filter>
  <!-- revelação antiga: meio sépia, desbotada, contraste baixo, leve desfoque -->
  <filter id="photo" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
    <feGaussianBlur stdDeviation="0.45" result="b"/>
    <feColorMatrix in="b" type="matrix" values="0.61 0.34 0.08 0 0.07  0.15 0.74 0.07 0 0.06  0.12 0.23 0.5 0 0.05  0 0 0 1 0"/>
  </filter>
  <filter id="noise" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="17"/>
    <feColorMatrix type="matrix" values="0 0 0 0 0.5  0 0 0 0 0.45  0 0 0 0 0.4  0.9 -0.3 -0.3 0 0"/>
  </filter>
  <radialGradient id="pvig" cx="0.5" cy="0.5" r="0.72"><stop offset="0.55" stop-color="#1a0f05" stop-opacity="0"/><stop offset="1" stop-color="#1a0f05" stop-opacity="0.42"/></radialGradient>
  <linearGradient id="gloss" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.35" stop-color="#fff" stop-opacity="0.07"/><stop offset="0.5" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <linearGradient id="darkP" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset="0.55" stop-color="#000" stop-opacity="0.55"/><stop offset="1" stop-color="#000" stop-opacity="0.8"/></linearGradient>
  <radialGradient id="treeG" cx="0.4" cy="0.35" r="0.7"><stop offset="0" stop-color="#4f7346"/><stop offset="1" stop-color="#22371f"/></radialGradient>
  <radialGradient id="beam" cx="0" cy="0.5" r="1"><stop offset="0" stop-color="{YEL}" stop-opacity="0.5"/><stop offset="1" stop-color="{YEL}" stop-opacity="0"/></radialGradient>
  <linearGradient id="moonD" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9fc0de" stop-opacity="0.3"/><stop offset="1" stop-color="#9fc0de" stop-opacity="0"/></linearGradient>
  <linearGradient id="moonU" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#9fc0de" stop-opacity="0.3"/><stop offset="1" stop-color="#9fc0de" stop-opacity="0"/></linearGradient>
  <linearGradient id="dark" x1="0" x2="1"><stop offset="0" stop-color="#1b1410" stop-opacity="0"/><stop offset="0.6" stop-color="#1b1410" stop-opacity="0.55"/><stop offset="1" stop-color="#1b1410" stop-opacity="0.8"/></linearGradient>
  <burn/>
  <radialGradient id="burn" cx="0.5" cy="0.5" r="0.75">
    <stop offset="0.55" stop-color="#3a2210" stop-opacity="0"/><stop offset="0.9" stop-color="#3a2210" stop-opacity="0.45"/><stop offset="1" stop-color="#24140a" stop-opacity="0.85"/>
  </radialGradient>
  <clipPath id="pclip"><rect {rm(PX0, PY0, PX1 - PX0, PY1 - PY0)}/></clipPath>
</defs>'''.replace("<burn/>", ""))

# ================= PAPEL =================
a(f'<rect width="{CW}" height="{CH}" fill="#0f0d0b"/>')
a(f'<g filter="url(#rough)"><rect x="16" y="16" width="{CW-32}" height="{CH-32}" fill="{PAPER}" filter="url(#paper)"/>'
  f'<rect x="16" y="16" width="{CW-32}" height="{CH-32}" fill="url(#burn)"/></g>')
for (x1, y1, x2, y2) in [(CW/2, 20, CW/2, CH-20), (20, CH/2, CW-20, CH/2)]:
    a(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#fff6dc" stroke-opacity="0.35" stroke-width="2.5" filter="url(#blur2)"/>')
    a(f'<line x1="{x1+1.5}" y1="{y1+1.5}" x2="{x2+1.5}" y2="{y2+1.5}" stroke="#3a2210" stroke-opacity="0.22" stroke-width="1.2"/>')
a(f'<circle cx="995" cy="672" r="46" fill="none" stroke="#7a4a20" stroke-opacity="0.28" stroke-width="7" stroke-dasharray="230 60" filter="url(#blur2)"/>')
a(f'<ellipse cx="70" cy="720" rx="70" ry="45" fill="#6b3f1a" fill-opacity="0.16" filter="url(#blur6)"/>')
a(f'<ellipse cx="1080" cy="90" rx="55" ry="35" fill="#6b3f1a" fill-opacity="0.14" filter="url(#blur6)"/>')

# cabeçalho e carimbo
a(f'<text x="48" y="58" fill="{INK}" font-family="{TYPE}" font-size="13" font-weight="700" letter-spacing="3">ARQUIVO GERAL · PLANTAS</text>')
a(f'<text x="48" y="88" fill="{INK}" font-family="{TYPE}" font-size="22" font-weight="700" letter-spacing="1">PLANTA DE EXEMPLO — CASA TÉRREA</text>')
a(f'<text x="48" y="112" fill="{INK_S}" font-family="{TYPE}" font-size="12.5" font-weight="700">Rodada 2 · anotado em campo: só o que a personagem já viu · {f"grade {letra_ult()} × 1–{G.nlin}, {GRADE_M:g} m por casa" if G else "grade de 1 m"}</text>')
a(f'<line x1="48" y1="124" x2="{CW-48}" y2="124" stroke="{INK}" stroke-width="1.5" stroke-opacity="0.7"/>')
a(f'<g transform="rotate(-9 945 76)" filter="url(#stamp)" opacity="0.8">'
  f'<rect x="840" y="50" width="210" height="52" rx="4" fill="none" stroke="{REDP}" stroke-width="3.5"/>'
  f'<rect x="846" y="56" width="198" height="40" rx="2" fill="none" stroke="{REDP}" stroke-width="1.5"/>'
  f'<text x="945" y="84" fill="{REDP}" font-family="{TYPE}" font-size="21" font-weight="700" text-anchor="middle" letter-spacing="3">CONFIDENCIAL</text></g>')

# seta da rua, no papel
a(f'<path d="M {X(PX0) - 8} {Y(3)} l -30 0 m 10 -8 l -10 8 l 10 8" fill="none" stroke="{INK}" stroke-width="2.2"/>')
rx_, ry_ = (34, Y(3) + 5) if G else (X(PX0) - 26, Y(3) + 26)   # com grade, sai do caminho dos números
a(f'<text x="{rx_}" y="{ry_}" fill="{INK}" font-family="{TYPE}" font-size="13" font-weight="700" text-anchor="middle">RUA</text>')

# ================= FOTO COLADA =================
a(f'<g transform="rotate({ROT} {PCX} {PCY})">')
# borda de foto revelada
B = 11
a(f'<rect x="{X(PX0) - B}" y="{Y(PY0) - B}" width="{S*(PX1-PX0) + 2*B}" height="{S*(PY1-PY0) + 2*B}" fill="#eee7d6" filter="url(#printshadow)"/>')
a(f'<rect x="{X(PX0) - B}" y="{Y(PY0) - B}" width="{S*(PX1-PX0) + 2*B}" height="{S*(PY1-PY0) + 2*B}" fill="#c9b892" opacity="0.25" filter="url(#paper)"/>')

a('<g clip-path="url(#pclip)"><g filter="url(#photo)">')
# --- quintal
a(f'<rect {rm(PX0, PY0, PX1 - PX0, PY1 - PY0)} fill="#3a5634" filter="url(#grass)"/>')
for _ in range(260):
    x = random.uniform(X(PX0), X(PX1)); y = random.uniform(Y(PY0), Y(PY1))
    if X(-0.4) < x < X(W + 0.4) and Y(-0.4) < y < Y(H + 0.4): continue
    c = random.choice(["#2b4227", "#4a6b40", "#2f4a2b"])
    a(f'<path d="M{x:.1f} {y:.1f} l-2 -5 M{x:.1f} {y:.1f} l1 -6 M{x:.1f} {y:.1f} l3 -4" stroke="{c}" stroke-width="1.2" fill="none"/>')
path_d = f"M {X(0)} {Y(2.4)} C {X(-0.6)} {Y(2.3)}, {X(-1.0)} {Y(3.0)}, {X(-1.6)} {Y(3.1)} L {X(-1.6)} {Y(4.1)} C {X(-0.9)} {Y(4.0)}, {X(-0.4)} {Y(3.8)}, {X(0)} {Y(3.6)} Z"
a(f'<path d="{path_d}" fill="#8f7a58" filter="url(#soft)" opacity="0.9"/>')
a(f'<path d="{path_d}" fill="#9a845f" filter="url(#dirt)" opacity="0.85"/>')
def tree(cx, cy, r):
    a(f'<ellipse cx="{cx+8}" cy="{cy+10}" rx="{r*1.05}" ry="{r}" fill="#000" opacity="0.35" filter="url(#soft)"/>')
    for dx, dy, rr in [(-r*.35, -r*.2, r*.7), (r*.35, -r*.15, r*.65), (0, r*.3, r*.7), (0, -r*.1, r*.75)]:
        a(f'<circle cx="{cx+dx:.1f}" cy="{cy+dy:.1f}" r="{rr:.1f}" fill="url(#treeG)" stroke="#1b2b18" stroke-width="1.5"/>')
tree(X(16.55), Y(0.4), 26); tree(X(16.6), Y(10.9), 22); tree(X(-0.9), Y(-0.3), 22); tree(X(-0.8), Y(10.5), 18)

# --- casa
a(f'<rect {rm(0, 0, W, H)} fill="#000" filter="url(#hshadow)"/>')
a('<g filter="url(#grain)">')
for r in [(0, 0, 8, 6), (0, 6, 16, 1.5), (0, 7.5, 6, 3.5), (6, 7.5, 3, 3.5), (9, 7.5, 7, 3.5), (13, 0, 3, 6)]:
    a(f'<rect {rm(*r)} fill="url(#wood)"/>')
a(f'<rect {rm(8, 0, 5, 6)} fill="url(#tile)"/>')
a('</g>')
for (cx, cy, rx, ry) in [(5.2, 4.8, 0.9, 0.5), (12.2, 6.9, 0.8, 0.35), (3.5, 10.4, 0.6, 0.3), (10.0, 1.7, 0.5, 0.35)]:
    a(f'<ellipse cx="{X(cx)}" cy="{Y(cy)}" rx="{S*rx}" ry="{S*ry}" fill="#140b07" opacity="0.45" filter="url(#soft)"/>')

def sh(): return 'filter="url(#fshadow)"'
a(f'<rect {rm(0.8, 1.7, 4.2, 2.8)} fill="#5e1f22" stroke="#3a1214" stroke-width="2"/>')
a(f'<rect {rm(1.0, 1.9, 3.8, 2.4)} fill="none" stroke="#a0653f" stroke-width="1.5" stroke-dasharray="6 3"/>')
a(f'<g {sh()}><rect {rm(1, 0.35, 3.2, 1.05)} rx="6" fill="#4e4a5a"/><rect {rm(1, 0.35, 3.2, 0.35)} rx="5" fill="#3c3946"/>'
  f'<rect {rm(1, 0.35, 0.3, 1.05)} rx="5" fill="#3c3946"/><rect {rm(3.9, 0.35, 0.3, 1.05)} rx="5" fill="#3c3946"/>'
  f'<line x1="{X(2.6)}" y1="{Y(0.75)}" x2="{X(2.6)}" y2="{Y(1.35)}" stroke="#2c2a33"/></g>')
a(f'<g {sh()}><rect {rm(2.1, 2.5, 1.5, 0.9)} rx="3" fill="#6b4a33" stroke="#3e2a1d"/>'
  f'<rect {rm(2.4, 2.75, 0.35, 0.25)} fill="#d8d0bd" transform="rotate(12 {X(2.55)} {Y(2.85)})"/></g>')
a(f'<g {sh()} transform="rotate(-25 {X(5.4)} {Y(1.5)})"><rect {rm(4.9, 1.0, 1.0, 1.0)} rx="7" fill="#6a2a2e"/><rect {rm(4.9, 1.0, 1.0, 0.3)} rx="5" fill="#4d1d20"/></g>')
a(f'<g {sh()} transform="rotate(70 {X(5.9)} {Y(3.9)})"><rect {rm(5.6, 3.6, 0.6, 0.6)} fill="#6b4a33" stroke="#3e2a1d"/><rect {rm(5.6, 3.5, 0.6, 0.12)} fill="#4a3222"/></g>')
a(f'<g {sh()}><rect {rm(0.1, 4.4, 0.45, 1.5)} fill="#4a3222" stroke="#2e1d14"/>'
  + "".join(f'<rect {rm(0.15, 4.5 + i*0.35, 0.35, 0.25)} fill="{c}"/>' for i, c in enumerate(["#7a3b2e", "#3e5a6b", "#8a7a4f", "#5a3a5e"])) + '</g>')
for _ in range(9):
    px, py = random.uniform(0.6, 6.8), random.uniform(3.6, 7.2)
    a(f'<rect x="{X(px):.1f}" y="{Y(py):.1f}" width="9" height="12" fill="#d9d1bd" opacity="0.8" transform="rotate({random.randint(-60,60)} {X(px):.1f} {Y(py):.1f})"/>')
a(f'<g {sh()}><rect {rm(8.3, 0, 4.4, 0.75)} fill="#7d7a76" stroke="#3a3836"/>'
  f'<rect {rm(9.5, 0.12, 1.0, 0.5)} rx="4" fill="#4a4e54" stroke="#2a2c30"/><circle cx="{X(10)}" cy="{Y(0.37)}" r="2.5" fill="#22252a"/>'
  f'<rect {rm(11.3, 0.06, 1.2, 0.63)} fill="#2d2f33"/>'
  + "".join(f'<circle cx="{X(11.6 + dx)}" cy="{Y(0.25 + dy)}" r="5" fill="none" stroke="#6a6d73" stroke-width="2"/>' for dx in (0, 0.6) for dy in (0, 0.3)) + '</g>')
a(f'<g {sh()}><rect {rm(8.2, 4.4, 0.85, 0.85)} rx="3" fill="#c9c6bf" stroke="#77736c"/><line x1="{X(8.3)}" y1="{Y(4.75)}" x2="{X(8.95)}" y2="{Y(4.75)}" stroke="#77736c"/></g>')
a(f'<g {sh()}><circle cx="{X(10.6)}" cy="{Y(4.2)}" r="{S*0.5}" fill="#6b4a33" stroke="#3e2a1d" stroke-width="2"/>'
  f'<rect {rm(10.4, 3.25, 0.45, 0.4)} rx="3" fill="#4a3222"/><rect {rm(11.2, 4.4, 0.45, 0.4)} rx="3" fill="#4a3222" transform="rotate(30 {X(11.4)} {Y(4.6)})"/></g>')
a(f'<circle cx="{X(10.45)}" cy="{Y(4.1)}" r="5" fill="#d9d1bd" opacity="0.9"/>')
a(f'<rect {rm(2.7, 8.6, 2.6, 1.7)} rx="4" fill="#3d4a5e" stroke="#26303e" stroke-width="2"/>')
a(f'<g {sh()}><rect {rm(0.3, 8.0, 2.1, 2.7)} rx="4" fill="#6b4a33" stroke="#3e2a1d"/><rect {rm(0.4, 8.1, 1.9, 2.5)} rx="3" fill="#b8b2a6"/>'
  f'<rect {rm(0.55, 8.2, 0.75, 0.45)} rx="6" fill="#ece6d8"/><rect {rm(1.4, 8.2, 0.75, 0.45)} rx="6" fill="#ece6d8"/>'
  f'<path d="M {X(0.4)} {Y(9.1)} L {X(2.3)} {Y(8.95)} L {X(2.3)} {Y(10.6)} L {X(0.4)} {Y(10.6)} Z" fill="#6d3940"/>'
  f'<path d="M {X(0.4)} {Y(9.1)} L {X(2.3)} {Y(8.95)} L {X(2.3)} {Y(9.25)} L {X(0.4)} {Y(9.35)} Z" fill="#8a4a52"/></g>')
a(f'<g {sh()}><rect {rm(2.55, 8.0, 0.55, 0.5)} fill="#5a3d2a" stroke="#3e2a1d"/></g>')
a(f'<g {sh()}><rect {rm(4.2, 10.3, 1.6, 0.6)} fill="#5a3d2a" stroke="#3e2a1d"/></g>')
for (bx, by, bw, rot) in [(4.6, 8.0, 0.6, 12), (5.2, 8.4, 0.5, -8)]:
    a(f'<g {sh()} transform="rotate({rot} {X(bx)} {Y(by)})"><rect {rm(bx, by, bw, bw)} fill="#a07d52" stroke="#5e4630"/><line x1="{X(bx)}" y1="{Y(by + bw/2)}" x2="{X(bx + bw)}" y2="{Y(by + bw/2)}" stroke="#5e4630"/></g>')
a(f'<g {sh()}><rect {rm(7.7, 0.5, 0.6, 2.5)} rx="2" fill="#6b4a33"/><rect {rm(7.75, 0.55, 0.5, 2.4)} fill="#80593c"/></g>')
# escuro de verdade no corredor (sem luz)
a(f'<rect {rm(6.5, 6, 9.5, 1.5)} fill="url(#darkP)"/>')

# paredes
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
hwall(0, 0, 16, [(2, 4), (9.5, 11.5)]); hwall(11, 0, 16, [(2, 4)])
vwall(0, 0, 11, [(2.5, 3.5)]); vwall(16, 0, 11); vwall(8, 4, 6); vwall(13, 0, 6, [(4, 5)])
hwall(6, 0, 16, [(1, 2.5), (10, 11)]); hwall(7.5, 0, 16, [(4, 5), (7, 8), (12, 13)])
vwall(6, 7.5, 11); vwall(9, 7.5, 11)
for (x1, y1, x2, y2) in segs:
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{WALL_D}" stroke-width="10" stroke-linecap="square"/>')
for (x1, y1, x2, y2) in segs:
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{WALL_L}" stroke-width="3.5" stroke-linecap="square"/>')
for (px, py) in {(0, 0), (16, 0), (0, 11), (16, 11), (8, 6), (13, 0), (13, 6), (0, 6), (16, 6), (0, 7.5), (16, 7.5), (6, 7.5), (9, 7.5), (6, 11), (9, 11), (8, 4)}:
    a(f'<rect x="{X(px) - 7}" y="{Y(py) - 7}" width="14" height="14" fill="{POST}" stroke="{WALL_D}" stroke-width="2"/>')
for (x1, y1, x2, y2) in [(2, 0, 4, 0), (9.5, 0, 11.5, 0), (2, 11, 4, 11)]:
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{WALL_D}" stroke-width="8"/>')
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{GLASS}" stroke-width="3"/>')
def open_door(hx, hy, lx, ly):
    a(f'<line x1="{X(hx)}" y1="{Y(hy)}" x2="{X(lx)}" y2="{Y(ly)}" stroke="{DOOR}" stroke-width="5" stroke-linecap="round"/>')
open_door(10, 6, 10, 7); open_door(4, 7.5, 4, 8.5); open_door(0, 3.5, 1, 3.5)
for (x1, y1, x2, y2) in [(13, 4, 13, 5), (7, 7.5, 8, 7.5), (12, 7.5, 13, 7.5)]:
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{WALL_D}" stroke-width="9"/>')
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{DOOR}" stroke-width="6"/>')
a('</g>')   # fim do filtro de revelação
# granulação, vinheta e brilho da foto
a(f'<rect {rm(PX0, PY0, PX1 - PX0, PY1 - PY0)} filter="url(#noise)" opacity="0.35" style="mix-blend-mode:multiply"/>')
a(f'<rect {rm(PX0, PY0, PX1 - PX0, PY1 - PY0)} fill="url(#pvig)"/>')
a(f'<rect {rm(PX0, PY0, PX1 - PX0, PY1 - PY0)} fill="url(#gloss)"/>')
a('</g>')   # fim do recorte

# ---------- anotações por cima da foto
a('<g>')
if G:
    o.extend(G.linhas(X, Y))
else:
    for i in range(W + 1):
        a(f'<line x1="{X(i)}" y1="{Y(0)}" x2="{X(i)}" y2="{Y(H)}" stroke="#f3e7c8" stroke-opacity="0.13"/>')
    for j in range(H + 1):
        a(f'<line x1="{X(0)}" y1="{Y(j)}" x2="{X(W)}" y2="{Y(j)}" stroke="#f3e7c8" stroke-opacity="0.13"/>')
# arcos das portas abertas (caneta)
for (lx_, ly_, ex, ey) in [(10, 7, 11, 6), (4, 8.5, 5, 7.5), (1, 3.5, 0, 2.5)]:
    a(f'<path d="M {X(lx_)} {Y(ly_)} A {S} {S} 0 0 0 {X(ex)} {Y(ey)}" fill="none" stroke="#f3e7c8" stroke-opacity="0.55" stroke-width="1.2" stroke-dasharray="3 3"/>')
# luz (marca-texto)
a(f'<polygon points="{X(2)},{Y(0)} {X(4)},{Y(0)} {X(5.3)},{Y(3.4)} {X(1.4)},{Y(3.4)}" fill="url(#moonD)"/>')
a(f'<polygon points="{X(9.5)},{Y(0)} {X(11.5)},{Y(0)} {X(12.4)},{Y(2.8)} {X(9.0)},{Y(2.8)}" fill="url(#moonD)"/>')
a(f'<polygon points="{X(2)},{Y(11)} {X(4)},{Y(11)} {X(4.9)},{Y(8.6)} {X(1.4)},{Y(8.6)}" fill="url(#moonU)"/>')
ix, iy = 7.2, 2.2
a(f'<path d="M {X(ix)} {Y(iy)} L {X(12.8)} {Y(0.2)} L {X(12.8)} {Y(4.9)} Z" fill="url(#beam)" filter="url(#blur2)"/>')
# não explorado: caneta preta por cima da foto
for r in [(13, 0, 3, 6), (6, 7.5, 3, 3.5), (9, 7.5, 7, 3.5)]:
    a(f'<g filter="url(#blot)"><rect x="{X(r[0]) + 6}" y="{Y(r[1]) + 6}" width="{S*r[2] - 12}" height="{S*r[3] - 12}" fill="#120d0a"/></g>')
    a(f'<rect {rm(*r)} fill="#120d0a" filter="url(#graphite)" opacity="0.55"/>')
    a(f'<text x="{X(r[0] + r[2]/2)}" y="{Y(r[1] + r[3]/2) + 10}" fill="{REDP}" fill-opacity="0.85" font-family="{TYPE}" font-size="30" font-weight="700" text-anchor="middle">?</text>')
# cobertura
a(f'<rect {rm(7.6, 0.4, 0.8, 2.7)} rx="3" fill="{YEL}" fill-opacity="0.15" stroke="{YEL}" stroke-width="2" stroke-dasharray="5 3"/>')
# rótulos em fita datilografada
def label(x, y, t, rot):
    w = 9.2 * len(t) + 16
    a(f'<g transform="rotate({rot} {X(x)} {Y(y)})"><rect x="{X(x) - w/2}" y="{Y(y) - 11}" width="{w}" height="18" fill="{PAPER_L}" fill-opacity="0.95" stroke="{INK}" stroke-opacity="0.35" filter="url(#fshadow)"/>'
      f'<text x="{X(x)}" y="{Y(y) + 3}" fill="{INK}" font-family="{TYPE}" font-size="12" font-weight="700" letter-spacing="2" text-anchor="middle">{t}</text></g>')
label(4.4, 5.5, "SALA", -2); label(11.9, 5.5, "COZINHA", 1.5); label(3.2, 6.85, "CORREDOR", -1); label(3.3, 10.5, "QUARTO", 2)
# distâncias em lápis vermelho
def dist_line(x1, y1, x2, y2, txt, lx, ly):
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="#d8402f" stroke-opacity="0.95" stroke-width="1.8" stroke-dasharray="6 4"/>')
    w = 8 * len(txt) + 14
    a(f'<rect x="{X(lx) - w/2}" y="{Y(ly) - 11}" width="{w}" height="20" fill="{PAPER_L}" stroke="{REDP}" stroke-width="1.2" filter="url(#fshadow)"/>')
    a(f'<text x="{X(lx)}" y="{Y(ly) + 4}" fill="{RED}" font-family="{TYPE}" font-size="12.5" font-weight="700" text-anchor="middle">{txt}</text>')
e1 = (11, 3.1); e2 = (11.3, 6.8)
dist_line(ix, iy, *e1, f"{round(math.dist((ix, iy), e1))} m", 9.1, 3.25)
dist_line(ix, iy, *e2, f"{round(math.dist((ix, iy), e2))} m", 9.3, 5.55)
# fichas
def token(x, y, fill, t, tc):
    a(f'<g filter="url(#tshadow)"><circle cx="{X(x)}" cy="{Y(y)}" r="15" fill="{fill}" stroke="{INK}" stroke-width="3"/></g>')
    a(f'<text x="{X(x)}" y="{Y(y) + 5}" fill="{tc}" font-family="{TYPE}" font-size="16" font-weight="700" text-anchor="middle">{t}</text>')
token(ix, iy, YEL, "P", INK); token(1.8, 4.6, ALLY, "A", PAPER_L); token(*e1, RED, "1", PAPER_L); token(*e2, RED, "2", PAPER_L)
a(f'<circle cx="{X(13.3)}" cy="{Y(9.3)}" r="16" fill="none" stroke="#d8402f" stroke-width="2.4" stroke-dasharray="4 3"/>')
a(f'<text x="{X(13.3)}" y="{Y(9.3) + 6}" fill="#d8402f" font-family="{TYPE}" font-size="17" font-weight="700" text-anchor="middle">?</text>')
a(f'<text x="{X(13.3) + 24}" y="{Y(9.3) - 18}" fill="#d8402f" font-family="{HAND}" font-size="13" transform="rotate(-6 {X(13.3) + 24} {Y(9.3) - 18})">barulho</text>')
a('</g>')

# fita adesiva nos cantos
def tape(cx, cy, rot):
    a(f'<g transform="rotate({rot} {cx} {cy})" filter="url(#tapeedge)"><rect x="{cx - 38}" y="{cy - 12}" width="76" height="24" fill="#efe3bf" fill-opacity="0.62"/>'
      f'<rect x="{cx - 38}" y="{cy - 12}" width="76" height="24" fill="none" stroke="#b9a77a" stroke-opacity="0.35"/></g>')
tape(X(PX0) - 4, Y(PY0) - 4, -38); tape(X(PX1) + 4, Y(PY0) - 4, 38); tape(X(PX0) - 4, Y(PY1) + 4, 38); tape(X(PX1) + 4, Y(PY1) + 4, -38)
if G:   # datilografado no papel, por cima da fita
    o.extend(G.rotulos(X, Y, afasta=B + 7, fonte=TYPE, cor=INK))
a('</g>')  # fim da rotação

# ================= RÉGUA, POSIÇÃO, LEGENDA =================
by = Y(PY1) + 46; bx0 = 48
a(f'<line x1="{bx0}" y1="{by}" x2="{bx0 + S*10}" y2="{by}" stroke="{INK}" stroke-width="3"/>')
for t in (0, 2.5, 5, 7.5, 10):
    big = t in (0, 5, 10)
    a(f'<line x1="{bx0 + S*t}" y1="{by - (7 if big else 4)}" x2="{bx0 + S*t}" y2="{by + (7 if big else 4)}" stroke="{INK}" stroke-width="1.8"/>')
a(f'<text x="{bx0 + S*10 + 14}" y="{by + 5}" fill="{INK}" font-family="{TYPE}" font-size="13" font-weight="700">10 m</text>')
py = by + 40
a(f'<text x="{bx0}" y="{py}" fill="{INK}" font-family="{TYPE}" font-size="13"><tspan font-weight="700">POSIÇÃO:</tspan> Você atrás do balcão{cc(ix, iy)} (cobertura), lanterna na cozinha. Aliado na porta da rua{cc(1.8, 4.6)}.</text>')
a(f'<text x="{bx0}" y="{py + 20}" fill="{INK}" font-family="{TYPE}" font-size="13">1: na cozinha{cc(*e1)}. 2: no corredor escuro{cc(*e2)}. Barulho atrás da porta do quarto dos fundos.</text>')

lx = X(PX1) + 48; ly = Y(0) - 8
a(f'<line x1="{lx - 20}" y1="{Y(PY0)}" x2="{lx - 20}" y2="{Y(PY1)}" stroke="{INK}" stroke-opacity="0.5"/>')
a(f'<text x="{lx}" y="{ly}" fill="{INK}" font-family="{TYPE}" font-size="15" font-weight="700" letter-spacing="3">LEGENDA</text>')
y = ly + 34; cx = lx + 14
def row(name):
    global y
    a(f'<text x="{lx + 38}" y="{y + 4}" fill="{INK}" font-family="{TYPE}" font-size="13" font-weight="700">{name}</text>'); y += 32
for col, t, name, tc in [(YEL, "P", "personagem", INK), (ALLY, "A", "aliado", PAPER_L), (RED, "1", "ameaça vista", PAPER_L)]:
    a(f'<circle cx="{cx}" cy="{y}" r="12" fill="{col}" stroke="{INK}" stroke-width="2.5"/><text x="{cx}" y="{y + 4}" fill="{tc}" font-family="{TYPE}" font-size="12" font-weight="700" text-anchor="middle">{t}</text>'); row(name)
a(f'<circle cx="{cx}" cy="{y}" r="12" fill="none" stroke="{REDP}" stroke-width="2" stroke-dasharray="4 3"/><text x="{cx}" y="{y + 4}" fill="{REDP}" font-family="{TYPE}" font-size="12" font-weight="700" text-anchor="middle">?</text>'); row("ouvido, não visto")
a(f'<rect x="{cx - 13}" y="{y - 7}" width="26" height="14" rx="2" fill="{YEL}" fill-opacity="0.25" stroke="#9a6b10" stroke-width="2" stroke-dasharray="5 3"/>'); row("cobertura")
a(f'<line x1="{cx - 14}" y1="{y + 8}" x2="{cx - 9}" y2="{y + 8}" stroke="{WALL_L}" stroke-width="5"/><line x1="{cx + 9}" y1="{y + 8}" x2="{cx + 14}" y2="{y + 8}" stroke="{WALL_L}" stroke-width="5"/>'
  f'<line x1="{cx - 9}" y1="{y + 8}" x2="{cx - 9}" y2="{y - 10}" stroke="{DOOR}" stroke-width="4" stroke-linecap="round"/>'
  f'<path d="M {cx - 9} {y - 10} A 18 18 0 0 1 {cx + 9} {y + 8}" fill="none" stroke="{INK}" stroke-opacity="0.6" stroke-dasharray="3 3"/>'); row("porta aberta")
a(f'<line x1="{cx - 14}" y1="{y}" x2="{cx - 8}" y2="{y}" stroke="{WALL_L}" stroke-width="5"/><line x1="{cx - 8}" y1="{y}" x2="{cx + 8}" y2="{y}" stroke="{DOOR}" stroke-width="6"/><line x1="{cx + 8}" y1="{y}" x2="{cx + 14}" y2="{y}" stroke="{WALL_L}" stroke-width="5"/>'); row("porta fechada")
a(f'<line x1="{cx - 13}" y1="{y}" x2="{cx + 13}" y2="{y}" stroke="{WALL_D}" stroke-width="8"/><line x1="{cx - 13}" y1="{y}" x2="{cx + 13}" y2="{y}" stroke="{GLASS}" stroke-width="3"/>'); row("janela")
a(f'<rect x="{cx - 13}" y="{y - 10}" width="26" height="20" fill="#120d0a"/><text x="{cx}" y="{y + 5}" fill="{REDP}" font-family="{TYPE}" font-size="14" font-weight="700" text-anchor="middle">?</text>'); row("não explorado")
a(f'<rect x="{cx - 13}" y="{y - 10}" width="26" height="20" fill="url(#dark)"/>'); row("escuro")
a(f'<path d="M {cx - 13} {y} L {cx + 13} {y - 10} L {cx + 13} {y + 10} Z" fill="{YEL}" fill-opacity="0.5"/>'); row("lanterna")
a(f'<path d="M {cx - 6} {y - 10} L {cx + 6} {y - 10} L {cx + 12} {y + 10} L {cx - 12} {y + 10} Z" fill="#5f86a6" fill-opacity="0.35"/>'); row("luar pela janela")
a(f'<line x1="{cx - 13}" y1="{y}" x2="{cx + 13}" y2="{y}" stroke="{REDP}" stroke-width="1.6" stroke-dasharray="6 4"/>'); row("distância")
if G:
    a(f'<text x="{cx}" y="{y + 5}" fill="{INK}" font-family="{TYPE}" font-size="13" font-weight="700" text-anchor="middle">D7</text>'); row("coluna D, linha 7")

a('</svg>')
open(sys.argv[1], "w", encoding="utf-8").write("\n".join(o))
print("ok", sys.argv[1])
