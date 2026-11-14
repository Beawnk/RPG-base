"""Planta de exemplo v3: estilo "planta antiga de arquivo" (papel envelhecido, nanquim,
datilografia, carimbo), com as anotações de campo por cima. Mesmo cenário da v1/v2.
Molde: copie, troque o cenário e gere. Uso: python planta_v3_arquivo.py saida.svg"""
import math, random, sys
sys.stdout.reconfigure(encoding="utf-8")
random.seed(5)

S = 40
OX, OY = 120, 160
W, H = 16, 11
CW, CH = 1100, 790

def X(m): return OX + S * m
def Y(m): return OY + S * m
def rm(x, y, w, h): return f'x="{X(x)}" y="{Y(y)}" width="{S*w}" height="{S*h}"'

PAPER = "#d8c7a0"; PAPER_L = "#ecdfbf"; INK = "#2a1c12"; INK_S = "#5a4430"
RED = "#8e1b13"; REDP = "#a3261b"; YEL = "#e2b22c"; ALLY = "#3f8577"
TYPE = "Courier New, Courier, monospace"
HAND = "Segoe Print, Bradley Hand, Comic Sans MS, cursive"

o = []; a = o.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CW} {CH}" width="{CW}" height="{CH}">')
a(f'''<defs>
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
  <filter id="ink" x="-5%" y="-5%" width="110%" height="110%">
    <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="12" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="2.6" xChannelSelector="R" yChannelSelector="G"/>
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
  <filter id="blur2"><feGaussianBlur stdDeviation="2"/></filter>
  <filter id="blur6" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="6"/></filter>
  <filter id="tshadow" x="-50%" y="-50%" width="200%" height="200%"><feDropShadow dx="1.5" dy="2.5" stdDeviation="1.5" flood-color="#2a1c12" flood-opacity="0.55"/></filter>
  <pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
    <rect width="6" height="6" fill="{PAPER_L}"/><line x1="0" y1="0" x2="0" y2="6" stroke="{INK}" stroke-width="1.6"/>
  </pattern>
  <radialGradient id="burn" cx="0.5" cy="0.5" r="0.75">
    <stop offset="0.55" stop-color="#3a2210" stop-opacity="0"/>
    <stop offset="0.9" stop-color="#3a2210" stop-opacity="0.45"/>
    <stop offset="1" stop-color="#24140a" stop-opacity="0.85"/>
  </radialGradient>
  <linearGradient id="dark" x1="0" x2="1"><stop offset="0" stop-color="#1b1410" stop-opacity="0"/><stop offset="0.6" stop-color="#1b1410" stop-opacity="0.55"/><stop offset="1" stop-color="#1b1410" stop-opacity="0.8"/></linearGradient>
  <radialGradient id="beam" cx="0" cy="0.5" r="1"><stop offset="0" stop-color="{YEL}" stop-opacity="0.55"/><stop offset="1" stop-color="{YEL}" stop-opacity="0"/></radialGradient>
  <linearGradient id="moonD" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5f86a6" stop-opacity="0.32"/><stop offset="1" stop-color="#5f86a6" stop-opacity="0"/></linearGradient>
  <linearGradient id="moonU" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#5f86a6" stop-opacity="0.32"/><stop offset="1" stop-color="#5f86a6" stop-opacity="0"/></linearGradient>
</defs>''')

# ---------- papel
a(f'<rect width="{CW}" height="{CH}" fill="#0f0d0b"/>')
a(f'<g filter="url(#rough)"><rect x="16" y="16" width="{CW-32}" height="{CH-32}" fill="{PAPER}" filter="url(#paper)"/>'
  f'<rect x="16" y="16" width="{CW-32}" height="{CH-32}" fill="url(#burn)"/></g>')
# dobras
for (x1, y1, x2, y2) in [(CW/2, 20, CW/2, CH-20), (20, CH/2, CW-20, CH/2)]:
    a(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#fff6dc" stroke-opacity="0.35" stroke-width="2.5" filter="url(#blur2)"/>')
    a(f'<line x1="{x1+1.5}" y1="{y1+1.5}" x2="{x2+1.5}" y2="{y2+1.5}" stroke="#3a2210" stroke-opacity="0.22" stroke-width="1.2"/>')
# manchas de café e umidade
a(f'<circle cx="955" cy="640" r="46" fill="none" stroke="#7a4a20" stroke-opacity="0.28" stroke-width="7" stroke-dasharray="230 60" filter="url(#blur2)"/>')
a(f'<circle cx="958" cy="643" r="41" fill="#7a4a20" fill-opacity="0.06"/>')
a(f'<ellipse cx="70" cy="700" rx="70" ry="45" fill="#6b3f1a" fill-opacity="0.16" filter="url(#blur6)"/>')
a(f'<ellipse cx="1040" cy="90" rx="55" ry="35" fill="#6b3f1a" fill-opacity="0.14" filter="url(#blur6)"/>')

# ---------- cabeçalho datilografado
a(f'<text x="48" y="58" fill="{INK}" font-family="{TYPE}" font-size="13" font-weight="700" letter-spacing="3">ARQUIVO GERAL · PLANTAS</text>')
a(f'<text x="48" y="88" fill="{INK}" font-family="{TYPE}" font-size="22" font-weight="700" letter-spacing="1">PLANTA DE EXEMPLO — CASA TÉRREA</text>')
a(f'<text x="48" y="112" fill="{INK_S}" font-family="{TYPE}" font-size="12.5" font-weight="700">Rodada 2 · anotado em campo: só o que a personagem já viu · grade de 1 m</text>')
a(f'<line x1="48" y1="124" x2="{CW-48}" y2="124" stroke="{INK}" stroke-width="1.5" stroke-opacity="0.7"/>')
# carimbo
a(f'<g transform="rotate(-9 905 76)" filter="url(#stamp)" opacity="0.8">'
  f'<rect x="800" y="50" width="210" height="52" rx="4" fill="none" stroke="{REDP}" stroke-width="3.5"/>'
  f'<rect x="806" y="56" width="198" height="40" rx="2" fill="none" stroke="{REDP}" stroke-width="1.5"/>'
  f'<text x="905" y="84" fill="{REDP}" font-family="{TYPE}" font-size="21" font-weight="700" text-anchor="middle" letter-spacing="3">CONFIDENCIAL</text></g>')

# ---------- entorno em nanquim
a('<g filter="url(#ink)">')
def tree(cx, cy, r):
    n = 9; pts = [(cx + r*math.cos(2*math.pi*i/n + 0.3), cy + r*math.sin(2*math.pi*i/n + 0.3)) for i in range(n)]
    sc = r * math.sin(math.pi / n) * 1.15
    d = f"M {pts[0][0]:.1f} {pts[0][1]:.1f} " + " ".join(f"A {sc:.1f} {sc:.1f} 0 0 1 {pts[(i+1)%n][0]:.1f} {pts[(i+1)%n][1]:.1f}" for i in range(n)) + " Z"
    a(f'<path d="{d}" fill="{INK}" fill-opacity="0.08" stroke="{INK}" stroke-width="1.4"/>')
    for k in range(3):
        rr = r * (0.3 + 0.18 * k)
        a(f'<path d="M {cx - rr:.1f} {cy + 2*k:.1f} q {rr*0.5:.1f} {-rr*0.6:.1f} {rr:.1f} 0" fill="none" stroke="{INK}" stroke-width="0.9" stroke-opacity="0.6"/>')
tree(X(16) + 46, Y(1.2), 28); tree(X(16) + 40, Y(10.4), 22); tree(X(0) - 60, Y(-0.4), 22)
# caminho até a rua (tracejado de calçamento)
for side in (2.45, 3.55):
    a(f'<path d="M {X(0)} {Y(side)} C {X(-1)} {Y(side)}, {X(-1.6 + (side-3)*0.6)} {Y(4)}, {X(-1.9 + (side-3)*0.9)} {Y(6)} S {X(-2.2 + (side-3)*0.9)} {Y(9.5)}, {X(-2.3 + (side-3)*0.9)} {Y(11.6)}" fill="none" stroke="{INK}" stroke-width="1.3" stroke-dasharray="7 4"/>')
a('</g>')
a(f'<path d="M {X(-1.2)} {Y(3)} l -30 0 m 10 -8 l -10 8 l 10 8" fill="none" stroke="{INK}" stroke-width="2.2"/>')
a(f'<text x="{X(-2.0)}" y="{Y(3) + 26}" fill="{INK}" font-family="{TYPE}" font-size="13" font-weight="700" text-anchor="middle">RUA</text>')

# ---------- piso (lápis)
a('<g opacity="0.55">')
for (x0, y0, w, h) in [(0, 0, 8, 6), (0, 6, 16, 1.5), (0, 7.5, 6, 3.5)]:
    yy = y0 + 0.25
    while yy < y0 + h:
        a(f'<line x1="{X(x0)}" y1="{Y(yy)}" x2="{X(x0 + w)}" y2="{Y(yy)}" stroke="{INK_S}" stroke-width="0.6" stroke-opacity="0.35"/>')
        yy += 0.25
for i in range(10):
    for j in range(12):
        if (i + j) % 2 == 0:
            a(f'<rect x="{X(8 + i*0.5)}" y="{Y(j*0.5)}" width="{S*0.5}" height="{S*0.5}" fill="{INK}" fill-opacity="0.13"/>')
a('</g>')
# grade de 1 m
for i in range(W + 1):
    a(f'<line x1="{X(i)}" y1="{Y(0)}" x2="{X(i)}" y2="{Y(H)}" stroke="{INK}" stroke-opacity="0.09"/>')
for j in range(H + 1):
    a(f'<line x1="{X(0)}" y1="{Y(j)}" x2="{X(W)}" y2="{Y(j)}" stroke="{INK}" stroke-opacity="0.09"/>')

# manchas no chão (o lugar é abandonado)
for (cx, cy, rx, ry) in [(5.2, 4.8, 0.9, 0.5), (12.2, 6.9, 0.8, 0.35), (3.5, 10.4, 0.6, 0.3)]:
    a(f'<ellipse cx="{X(cx)}" cy="{Y(cy)}" rx="{S*rx}" ry="{S*ry}" fill="#3a2210" fill-opacity="0.25" filter="url(#blur6)"/>')

# ---------- móveis em nanquim
F = f'fill="{PAPER_L}" fill-opacity="0.55" stroke="{INK}" stroke-width="1.5"'
a('<g filter="url(#ink)">')
# sala
a(f'<rect {rm(0.8, 1.7, 4.2, 2.8)} fill="{RED}" fill-opacity="0.12" stroke="{INK}" stroke-width="1.2"/>')
a(f'<rect {rm(1.0, 1.9, 3.8, 2.4)} fill="none" stroke="{INK}" stroke-width="0.8" stroke-dasharray="5 3"/>')
a(f'<rect {rm(1, 0.35, 3.2, 1.05)} rx="5" {F}/><line x1="{X(1)}" y1="{Y(0.7)}" x2="{X(4.2)}" y2="{Y(0.7)}" stroke="{INK}"/>'
  f'<line x1="{X(1.3)}" y1="{Y(0.7)}" x2="{X(1.3)}" y2="{Y(1.4)}" stroke="{INK}"/><line x1="{X(3.9)}" y1="{Y(0.7)}" x2="{X(3.9)}" y2="{Y(1.4)}" stroke="{INK}"/><line x1="{X(2.6)}" y1="{Y(0.7)}" x2="{X(2.6)}" y2="{Y(1.4)}" stroke="{INK}" stroke-width="0.8"/>')
a(f'<rect {rm(2.1, 2.5, 1.5, 0.9)} rx="2" {F}/>')
a(f'<g transform="rotate(-25 {X(5.4)} {Y(1.5)})"><rect {rm(4.9, 1.0, 1.0, 1.0)} rx="6" {F}/><line x1="{X(4.9)}" y1="{Y(1.3)}" x2="{X(5.9)}" y2="{Y(1.3)}" stroke="{INK}"/></g>')
a(f'<g transform="rotate(70 {X(5.9)} {Y(3.9)})"><rect {rm(5.6, 3.6, 0.6, 0.6)} {F}/><rect {rm(5.6, 3.48, 0.6, 0.12)} fill="{INK}"/></g>')
a(f'<rect {rm(0.1, 4.4, 0.45, 1.5)} {F}/>' + "".join(f'<line x1="{X(0.1)}" y1="{Y(4.4 + k*0.3)}" x2="{X(0.55)}" y2="{Y(4.4 + k*0.3)}" stroke="{INK}" stroke-width="0.9"/>' for k in range(1, 5)))
for _ in range(9):
    px, py = random.uniform(0.6, 6.8), random.uniform(3.6, 7.2)
    a(f'<rect x="{X(px):.1f}" y="{Y(py):.1f}" width="9" height="12" fill="{PAPER_L}" stroke="{INK}" stroke-width="0.8" transform="rotate({random.randint(-60,60)} {X(px):.1f} {Y(py):.1f})"/>')
# cozinha
a(f'<rect {rm(8.3, 0, 4.4, 0.75)} {F}/>')
a(f'<rect {rm(9.5, 0.12, 1.0, 0.5)} rx="4" fill="none" stroke="{INK}" stroke-width="1.3"/><circle cx="{X(10)}" cy="{Y(0.37)}" r="2.5" fill="{INK}"/>')
a(f'<rect {rm(11.3, 0.06, 1.2, 0.63)} fill="none" stroke="{INK}" stroke-width="1.3"/>' + "".join(f'<circle cx="{X(11.6 + dx)}" cy="{Y(0.25 + dy)}" r="5" fill="none" stroke="{INK}" stroke-width="1.2"/>' for dx in (0, 0.6) for dy in (0, 0.3)))
a(f'<rect {rm(8.2, 4.4, 0.85, 0.85)} rx="2" {F}/><line x1="{X(8.2)}" y1="{Y(4.75)}" x2="{X(9.05)}" y2="{Y(4.75)}" stroke="{INK}"/>')
a(f'<circle cx="{X(10.6)}" cy="{Y(4.2)}" r="{S*0.5}" {F}/><rect {rm(10.4, 3.25, 0.45, 0.4)} rx="2" {F}/>'
  f'<rect {rm(11.2, 4.4, 0.45, 0.4)} rx="2" {F} transform="rotate(30 {X(11.4)} {Y(4.6)})"/>')
# quarto
a(f'<rect {rm(2.7, 8.6, 2.6, 1.7)} rx="3" fill="none" stroke="{INK}" stroke-width="1.1" stroke-dasharray="5 3"/>')
a(f'<rect {rm(0.3, 8.0, 2.1, 2.7)} rx="3" {F}/><rect {rm(0.55, 8.2, 0.75, 0.45)} rx="6" {F}/><rect {rm(1.4, 8.2, 0.75, 0.45)} rx="6" {F}/>'
  f'<path d="M {X(0.3)} {Y(9.1)} L {X(2.4)} {Y(8.95)}" stroke="{INK}" stroke-width="1.3" fill="none"/>'
  f'<path d="M {X(0.3)} {Y(9.3)} L {X(2.4)} {Y(9.2)}" stroke="{INK}" stroke-width="0.8" fill="none"/>')
a(f'<rect {rm(2.55, 8.0, 0.55, 0.5)} {F}/><rect {rm(4.2, 10.3, 1.6, 0.6)} {F}/>')
for (bx, by, bw, rot) in [(4.6, 8.0, 0.6, 12), (5.2, 8.4, 0.5, -8)]:
    a(f'<g transform="rotate({rot} {X(bx)} {Y(by)})"><rect {rm(bx, by, bw, bw)} {F}/>'
      f'<line x1="{X(bx)}" y1="{Y(by)}" x2="{X(bx + bw)}" y2="{Y(by + bw)}" stroke="{INK}"/><line x1="{X(bx + bw)}" y1="{Y(by)}" x2="{X(bx)}" y2="{Y(by + bw)}" stroke="{INK}"/></g>')
# balcão (cobertura)
a(f'<rect {rm(7.7, 0.5, 0.6, 2.5)} {F}/>')
a('</g>')
a(f'<rect {rm(7.6, 0.4, 0.8, 2.7)} rx="3" fill="{YEL}" fill-opacity="0.18" stroke="#9a6b10" stroke-width="2" stroke-dasharray="5 3"/>')

# ---------- luz e escuro (aquarela)
a(f'<polygon points="{X(2)},{Y(0)} {X(4)},{Y(0)} {X(5.3)},{Y(3.4)} {X(1.4)},{Y(3.4)}" fill="url(#moonD)"/>')
a(f'<polygon points="{X(9.5)},{Y(0)} {X(11.5)},{Y(0)} {X(12.4)},{Y(2.8)} {X(9.0)},{Y(2.8)}" fill="url(#moonD)"/>')
a(f'<polygon points="{X(2)},{Y(11)} {X(4)},{Y(11)} {X(4.9)},{Y(8.6)} {X(1.4)},{Y(8.6)}" fill="url(#moonU)"/>')
a(f'<rect {rm(6.5, 6, 9.5, 1.5)} fill="url(#dark)" filter="url(#graphite)"/>')
a(f'<rect {rm(6.5, 6, 9.5, 1.5)} fill="url(#dark)" opacity="0.6"/>')
ix, iy = 7.2, 2.2
a(f'<path d="M {X(ix)} {Y(iy)} L {X(12.8)} {Y(0.2)} L {X(12.8)} {Y(4.9)} Z" fill="url(#beam)" filter="url(#blur2)"/>')

# não explorado: borrão de carvão, como trecho censurado
for r in [(13, 0, 3, 6), (6, 7.5, 3, 3.5), (9, 7.5, 7, 3.5)]:
    a(f'<g filter="url(#blot)"><rect x="{X(r[0]) + 6}" y="{Y(r[1]) + 6}" width="{S*r[2] - 12}" height="{S*r[3] - 12}" fill="#1c1511"/></g>')
    a(f'<rect {rm(*r)} fill="#1c1511" filter="url(#graphite)" opacity="0.6"/>')
    a(f'<text x="{X(r[0] + r[2]/2)}" y="{Y(r[1] + r[3]/2) + 10}" fill="{REDP}" fill-opacity="0.75" font-family="{TYPE}" font-size="30" font-weight="700" text-anchor="middle">?</text>')

# ---------- paredes em nanquim com hachura
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

a('<g filter="url(#ink)">')
for (x1, y1, x2, y2) in segs:
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{INK}" stroke-width="10" stroke-linecap="square"/>')
for (x1, y1, x2, y2) in segs:
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="url(#hatch)" stroke-width="6" stroke-linecap="square"/>')
# janelas: três linhas finas
for (x1, y1, x2, y2) in [(2, 0, 4, 0), (9.5, 0, 11.5, 0), (2, 11, 4, 11)]:
    for off in (-3.5, 0, 3.5):
        a(f'<line x1="{X(x1)}" y1="{Y(y1) + off}" x2="{X(x2)}" y2="{Y(y2) + off}" stroke="{INK}" stroke-width="1.1"/>')
    for xx in (x1, x2):
        a(f'<line x1="{X(xx)}" y1="{Y(y1) - 5}" x2="{X(xx)}" y2="{Y(y1) + 5}" stroke="{INK}" stroke-width="2"/>')
# portas abertas
def open_door(hx, hy, lx, ly, ex, ey, sweep):
    a(f'<path d="M {X(lx)} {Y(ly)} A {S} {S} 0 0 {sweep} {X(ex)} {Y(ey)}" fill="none" stroke="{INK}" stroke-width="0.9" stroke-dasharray="3 3"/>')
    a(f'<line x1="{X(hx)}" y1="{Y(hy)}" x2="{X(lx)}" y2="{Y(ly)}" stroke="{INK}" stroke-width="2.2"/>')
open_door(10, 6, 10, 7, 11, 6, 0); open_door(4, 7.5, 4, 8.5, 5, 7.5, 0); open_door(0, 3.5, 1, 3.5, 0, 2.5, 0)
# portas fechadas
def closed(x1, y1, x2, y2):
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{INK}" stroke-width="10"/>')
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{PAPER_L}" stroke-width="5"/>')
closed(13, 4, 13, 5); closed(7, 7.5, 8, 7.5); closed(12, 7.5, 13, 7.5)
a('</g>')

# ---------- rótulos em fita datilografada
def label(x, y, t, rot):
    w = 9.2 * len(t) + 16
    a(f'<g transform="rotate({rot} {X(x)} {Y(y)})"><rect x="{X(x) - w/2}" y="{Y(y) - 11}" width="{w}" height="18" fill="{PAPER_L}" fill-opacity="0.92" stroke="{INK}" stroke-opacity="0.35"/>'
      f'<text x="{X(x)}" y="{Y(y) + 3}" fill="{INK}" font-family="{TYPE}" font-size="12" font-weight="700" letter-spacing="2" text-anchor="middle">{t}</text></g>')
label(4.4, 5.5, "SALA", -2); label(11.9, 5.5, "COZINHA", 1.5); label(3.2, 6.85, "CORREDOR", -1); label(3.3, 10.5, "QUARTO", 2)

# ---------- distâncias em lápis vermelho
def dist_line(x1, y1, x2, y2, txt, lx, ly):
    a(f'<line x1="{X(x1)}" y1="{Y(y1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{REDP}" stroke-opacity="0.85" stroke-width="1.6" stroke-dasharray="6 4"/>')
    w = 8 * len(txt) + 14
    a(f'<rect x="{X(lx) - w/2}" y="{Y(ly) - 11}" width="{w}" height="20" fill="{PAPER_L}" stroke="{REDP}" stroke-width="1.2"/>')
    a(f'<text x="{X(lx)}" y="{Y(ly) + 4}" fill="{RED}" font-family="{TYPE}" font-size="12.5" font-weight="700" text-anchor="middle">{txt}</text>')
e1 = (11, 3.1); e2 = (11.3, 6.8)
dist_line(ix, iy, *e1, f"{round(math.dist((ix, iy), e1))} m", 9.1, 3.25)
dist_line(ix, iy, *e2, f"{round(math.dist((ix, iy), e2))} m", 9.3, 5.55)

# ---------- fichas
def token(x, y, fill, t, tc):
    a(f'<g filter="url(#tshadow)"><circle cx="{X(x)}" cy="{Y(y)}" r="15" fill="{fill}" stroke="{INK}" stroke-width="3"/></g>')
    a(f'<text x="{X(x)}" y="{Y(y) + 5}" fill="{tc}" font-family="{TYPE}" font-size="16" font-weight="700" text-anchor="middle">{t}</text>')
token(ix, iy, YEL, "P", INK); token(1.8, 4.6, ALLY, "A", PAPER_L); token(*e1, RED, "1", PAPER_L); token(*e2, RED, "2", PAPER_L)
a(f'<circle cx="{X(13.3)}" cy="{Y(9.3)}" r="16" fill="{PAPER_L}" fill-opacity="0.15" stroke="{REDP}" stroke-width="2.4" stroke-dasharray="4 3"/>')
a(f'<text x="{X(13.3)}" y="{Y(9.3) + 6}" fill="{REDP}" font-family="{TYPE}" font-size="17" font-weight="700" text-anchor="middle">?</text>')
a(f'<text x="{X(13.3) + 24}" y="{Y(9.3) - 18}" fill="{REDP}" font-family="{HAND}" font-size="13" transform="rotate(-6 {X(13.3) + 24} {Y(9.3) - 18})">barulho</text>')

# ---------- régua e posição
by = Y(H) + 52; bx0 = 48
a(f'<line x1="{bx0}" y1="{by}" x2="{bx0 + S*10}" y2="{by}" stroke="{INK}" stroke-width="3"/>')
for k, t in enumerate((0, 2.5, 5, 7.5, 10)):
    a(f'<line x1="{bx0 + S*t}" y1="{by - (7 if t in (0, 5, 10) else 4)}" x2="{bx0 + S*t}" y2="{by + (7 if t in (0, 5, 10) else 4)}" stroke="{INK}" stroke-width="1.8"/>')
a(f'<text x="{bx0 + S*10 + 14}" y="{by + 5}" fill="{INK}" font-family="{TYPE}" font-size="13" font-weight="700">10 m</text>')
py = by + 42
a(f'<text x="{bx0}" y="{py}" fill="{INK}" font-family="{TYPE}" font-size="13"><tspan font-weight="700">POSIÇÃO:</tspan> Você atrás do balcão (cobertura), lanterna na cozinha. Aliado na porta da rua.</text>')
a(f'<text x="{bx0}" y="{py + 20}" fill="{INK}" font-family="{TYPE}" font-size="13">1: na cozinha. 2: no corredor escuro. Barulho atrás da porta do quarto dos fundos.</text>')

# ---------- legenda
lx = X(W) + 110; ly = Y(0) + 4
a(f'<line x1="{lx - 22}" y1="{Y(0) - 14}" x2="{lx - 22}" y2="{Y(H) + 10}" stroke="{INK}" stroke-opacity="0.5"/>')
a(f'<text x="{lx}" y="{ly}" fill="{INK}" font-family="{TYPE}" font-size="15" font-weight="700" letter-spacing="3">LEGENDA</text>')
y = ly + 34; cx = lx + 14
def row(name):
    global y
    a(f'<text x="{lx + 40}" y="{y + 4}" fill="{INK}" font-family="{TYPE}" font-size="13" font-weight="700">{name}</text>'); y += 32
for col, t, name, tc in [(YEL, "P", "personagem", INK), (ALLY, "A", "aliado", PAPER_L), (RED, "1", "ameaça vista", PAPER_L)]:
    a(f'<circle cx="{cx}" cy="{y}" r="12" fill="{col}" stroke="{INK}" stroke-width="2.5"/><text x="{cx}" y="{y + 4}" fill="{tc}" font-family="{TYPE}" font-size="12" font-weight="700" text-anchor="middle">{t}</text>'); row(name)
a(f'<circle cx="{cx}" cy="{y}" r="12" fill="none" stroke="{REDP}" stroke-width="2" stroke-dasharray="4 3"/><text x="{cx}" y="{y + 4}" fill="{REDP}" font-family="{TYPE}" font-size="12" font-weight="700" text-anchor="middle">?</text>'); row("ouvido, não visto")
a(f'<rect x="{cx - 13}" y="{y - 7}" width="26" height="14" rx="2" fill="{YEL}" fill-opacity="0.25" stroke="#9a6b10" stroke-width="2" stroke-dasharray="5 3"/>'); row("cobertura")
a(f'<line x1="{cx - 14}" y1="{y + 8}" x2="{cx - 9}" y2="{y + 8}" stroke="{INK}" stroke-width="6"/><line x1="{cx + 9}" y1="{y + 8}" x2="{cx + 14}" y2="{y + 8}" stroke="{INK}" stroke-width="6"/>'
  f'<line x1="{cx - 9}" y1="{y + 8}" x2="{cx - 9}" y2="{y - 10}" stroke="{INK}" stroke-width="2"/><path d="M {cx - 9} {y - 10} A 18 18 0 0 1 {cx + 9} {y + 8}" fill="none" stroke="{INK}" stroke-dasharray="3 3"/>'); row("porta aberta")
a(f'<line x1="{cx - 14}" y1="{y}" x2="{cx + 14}" y2="{y}" stroke="{INK}" stroke-width="9"/><line x1="{cx - 8}" y1="{y}" x2="{cx + 8}" y2="{y}" stroke="{PAPER_L}" stroke-width="4"/>'); row("porta fechada")
a("".join(f'<line x1="{cx - 13}" y1="{y + off}" x2="{cx + 13}" y2="{y + off}" stroke="{INK}" stroke-width="1.1"/>' for off in (-3.5, 0, 3.5))); row("janela")
a(f'<rect x="{cx - 13}" y="{y - 10}" width="26" height="20" fill="#1c1511"/><text x="{cx}" y="{y + 5}" fill="{REDP}" font-family="{TYPE}" font-size="14" font-weight="700" text-anchor="middle">?</text>'); row("não explorado")
a(f'<rect x="{cx - 13}" y="{y - 10}" width="26" height="20" fill="url(#dark)"/>'); row("escuro")
a(f'<path d="M {cx - 13} {y} L {cx + 13} {y - 10} L {cx + 13} {y + 10} Z" fill="{YEL}" fill-opacity="0.5"/>'); row("lanterna")
a(f'<path d="M {cx - 6} {y - 10} L {cx + 6} {y - 10} L {cx + 12} {y + 10} L {cx - 12} {y + 10} Z" fill="#5f86a6" fill-opacity="0.35"/>'); row("luar pela janela")
a(f'<line x1="{cx - 13}" y1="{y}" x2="{cx + 13}" y2="{y}" stroke="{REDP}" stroke-width="1.6" stroke-dasharray="6 4"/>'); row("distância")

a('</svg>')
open(sys.argv[1], "w", encoding="utf-8").write("\n".join(o))
print("ok", sys.argv[1])
