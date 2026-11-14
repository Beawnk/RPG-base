"""Documento de exemplo: relatório datilografado de arquivo com as cinco formas de parte oculta
(tarja, dano de água e fogo, tinta UV, símbolo, impressão corrompida).
Molde: copie, troque o texto e gere. Uso: python documento_exemplo.py saida.svg [uv]"""
import random, sys
sys.stdout.reconfigure(encoding="utf-8")
random.seed(3)
UV = len(sys.argv) > 2 and sys.argv[2] == "uv"

CW, CH = 860, 1130
PAPER = "#dccba5"; PAPER_L = "#ecdfbf"; INK = "#241810"; INK_S = "#4e3a28"; REDP = "#a3261b"
TYPE = "Courier New, Courier, monospace"
HAND = "Segoe Print, Bradley Hand, Comic Sans MS, cursive"
CHW = 9.0   # largura de um caractere em Courier 15px

o = []; a = o.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CW} {CH}" width="{CW}" height="{CH}">')
a(f'''<defs>
  <filter id="paper" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
    <feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="3" seed="3" result="fib"/>
    <feColorMatrix in="fib" type="saturate" values="0" result="fg"/>
    <feComponentTransfer in="fg" result="fl"><feFuncR type="linear" slope="0.22" intercept="0.86"/><feFuncG type="linear" slope="0.22" intercept="0.86"/><feFuncB type="linear" slope="0.22" intercept="0.86"/></feComponentTransfer>
    <feTurbulence type="fractalNoise" baseFrequency="0.007" numOctaves="3" seed="8" result="mot"/>
    <feColorMatrix in="mot" type="saturate" values="0" result="mg"/>
    <feComponentTransfer in="mg" result="ml"><feFuncR type="linear" slope="0.45" intercept="0.7"/><feFuncG type="linear" slope="0.45" intercept="0.68"/><feFuncB type="linear" slope="0.45" intercept="0.62"/></feComponentTransfer>
    <feBlend in="SourceGraphic" in2="fl" mode="multiply" result="p1"/><feBlend in="p1" in2="ml" mode="multiply" result="p2"/>
    <feComposite in="p2" in2="SourceGraphic" operator="in"/>
  </filter>
  <filter id="typed" x="-2%" y="-20%" width="104%" height="140%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="1" seed="5" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.55" result="holes"/>
    <feComposite in="SourceGraphic" in2="holes" operator="in"/>
  </filter>
  <filter id="ink" x="-5%" y="-5%" width="110%" height="110%">
    <feTurbulence type="fractalNoise" baseFrequency="0.06" numOctaves="2" seed="12" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="2.5" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <filter id="paint" x="-10%" y="-10%" width="120%" height="120%">
    <feTurbulence type="fractalNoise" baseFrequency="0.08" numOctaves="2" seed="19" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="6" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <filter id="stamp" x="-10%" y="-10%" width="120%" height="120%" color-interpolation-filters="sRGB">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="21" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.2 1.5" result="holes"/>
    <feComposite in="SourceGraphic" in2="holes" operator="in" result="s"/>
    <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="1" seed="4" result="d"/>
    <feDisplacementMap in="s" in2="d" scale="2" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <filter id="stain" x="-20%" y="-20%" width="140%" height="140%">
    <feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="3" seed="27" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="40" xChannelSelector="R" yChannelSelector="G" result="d"/>
    <feGaussianBlur in="d" stdDeviation="3"/>
  </filter>
  <filter id="char" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="4"/></filter>
  <filter id="blur6" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="6"/></filter>
  <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%"><feDropShadow dx="4" dy="6" stdDeviation="6" flood-color="#000" flood-opacity="0.6"/></filter>
  <filter id="uvtint" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
    <feColorMatrix type="matrix" values="0.07 0.14 0.03 0 0.02  0.03 0.07 0.01 0 0.0  0.16 0.3 0.06 0 0.05  0 0 0 1 0"/>
  </filter>
  <filter id="glow" x="-20%" y="-60%" width="140%" height="220%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="3.5" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <radialGradient id="burn" cx="0.5" cy="0.45" r="0.8">
    <stop offset="0.6" stop-color="#3a2210" stop-opacity="0"/><stop offset="1" stop-color="#3a2210" stop-opacity="0.5"/>
  </radialGradient>
  <radialGradient id="uvspot" cx="0.42" cy="0.78" r="0.55">
    <stop offset="0" stop-color="#7b4dff" stop-opacity="0.35"/><stop offset="0.6" stop-color="#3a1f8a" stop-opacity="0.12"/><stop offset="1" stop-color="#000" stop-opacity="0.55"/>
  </radialGradient>
  <clipPath id="sheet"><polygon points="{{sheet_pts}}"/></clipPath>
</defs>''')

# folha com o canto de baixo à direita queimado
PX, PY, PW, PH = 50, 40, 740, 1050
burn = [(PX + PW, PY + PH - 210), (PX + PW - 18, PY + PH - 180), (PX + PW - 10, PY + PH - 150), (PX + PW - 40, PY + PH - 128),
        (PX + PW - 34, PY + PH - 96), (PX + PW - 70, PY + PH - 80), (PX + PW - 82, PY + PH - 46), (PX + PW - 120, PY + PH - 38),
        (PX + PW - 140, PY + PH - 12), (PX + PW - 178, PY + PH)]
pts = [(PX, PY), (PX + PW, PY)] + burn + [(PX, PY + PH)]
sheet_pts = " ".join(f"{x},{y}" for x, y in pts)
o[1] = o[1].replace("{sheet_pts}", sheet_pts)

a(f'<rect width="{CW}" height="{CH}" fill="#0f0d0b"/>')
a(f'<g transform="rotate(-0.6 {CW/2} {CH/2})">')
a(f'<polygon points="{sheet_pts}" fill="#000" filter="url(#shadow)"/>')
UVF = 'filter="url(#uvtint)"' if UV else ""
a(f'<g {UVF}>')
a('<g clip-path="url(#sheet)">')
a(f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" fill="{PAPER}" filter="url(#paper)"/>')
a(f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" fill="url(#burn)"/>')
# marca de dobra
a(f'<line x1="{PX}" y1="{PY + PH/2}" x2="{PX + PW}" y2="{PY + PH/2}" stroke="#fff6dc" stroke-opacity="0.3" stroke-width="2.5"/>')
a(f'<line x1="{PX}" y1="{PY + PH/2 + 1.5}" x2="{PX + PW}" y2="{PY + PH/2 + 1.5}" stroke="#3a2210" stroke-opacity="0.2"/>')

# ---------- texto datilografado
X0 = PX + 52
BOLD = 'font-weight="700"'
def typed(x, y, t, size=15, bold=False, color=INK, spacing=0):
    b = BOLD if bold else ""
    a(f'<text x="{x}" y="{y}" fill="{color}" font-family="{TYPE}" font-size="{size}" {b} letter-spacing="{spacing}" xml:space="preserve" filter="url(#typed)">{t}</text>')

def line_with_bars(x, y, t):
    """'#' marca trecho tarjado."""
    typed(x, y, t.replace("#", " "))
    i = 0
    while i < len(t):
        if t[i] == "#":
            j = i
            while j < len(t) and t[j] == "#": j += 1
            a(f'<rect x="{x + i*CHW - 1}" y="{y - 13}" width="{(j - i)*CHW + 2}" height="17" fill="#120c08" filter="url(#ink)"/>')
            i = j
        else:
            i += 1

typed(X0, PY + 58, "ARQUIVO GERAL · OCORRÊNCIAS", 12, True, INK_S, 3)
typed(X0, PY + 92, "RELATÓRIO DE OCORRÊNCIA", 24, True, INK, 2)
typed(X0, PY + 116, "Nº 0000-EX · documento de exemplo", 12.5, False, INK_S)
a(f'<line x1="{X0}" y1="{PY + 132}" x2="{PX + PW - 52}" y2="{PY + 132}" stroke="{INK}" stroke-width="1.5" stroke-opacity="0.7"/>')

y = PY + 170
for t in ["LOCAL......: escola estadual desativada, zona rural",
          "DATA.......: ##/##/19##",
          "EQUIPE.....: ##########, ###########",
          "CLASSIFIC..: RESTRITO"]:
    line_with_bars(X0, y, t); y += 26

y += 22
typed(X0, y, "RESUMO DA OCORRÊNCIA", 14, True, INK, 2); y += 32
for t in ["Equipe chegou ao local às 22h40. O zelador relatou luzes",
          "acesas no ginásio, sem energia desde o fechamento. No",
          "vestiário masculino foram encontrados ###################",
          "#######################. Contenção concluída às 03h15,",
          "sem baixas na equipe. Testemunha encaminhada para ########",
          "###############."]:
    line_with_bars(X0, y, t); y += 24

y += 18
wet_top = y - 16
for t in ["Em depoimento, o zelador afirma que viu alguém no corredor",
          "do ginásio nas três noites anteriores, sempre parado, sempre",
          "de costas, sempre no mesmo lugar perto do bebedouro. Disse",
          "que reconheceria o rosto, mas que nunca chegou perto o",
          "bastante. Recusou-se a voltar ao prédio."]:
    typed(X0, y, t); y += 24
# mancha de água: apaga o meio de três linhas
a(f'<g filter="url(#stain)"><ellipse cx="{X0 + 330}" cy="{wet_top + 62}" rx="150" ry="44" fill="{PAPER}" fill-opacity="0.97"/></g>')
a(f'<g filter="url(#stain)"><ellipse cx="{X0 + 330}" cy="{wet_top + 62}" rx="160" ry="50" fill="none" stroke="#7a5428" stroke-opacity="0.55" stroke-width="5"/></g>')
a(f'<g filter="url(#stain)"><ellipse cx="{X0 + 330}" cy="{wet_top + 62}" rx="130" ry="36" fill="#a07a48" fill-opacity="0.25"/></g>')

# ---------- sigilo
y += 30
typed(X0, y, "SÍMBOLO ENCONTRADO", 14, True, INK, 2); y += 18
bx, by_, bw, bh = X0, y, 250, 200
a(f'<rect x="{bx}" y="{by_}" width="{bw}" height="{bh}" fill="none" stroke="{INK}" stroke-opacity="0.5"/>')
cx, cy = bx + bw/2, by_ + bh/2
a(f'<g filter="url(#paint)" stroke="#5a1a12" stroke-width="5" fill="none" stroke-linecap="round" opacity="0.88">'
  f'<path d="M {cx-58} {cy+30} A 64 64 0 1 1 {cx+52} {cy+38}"/>'
  f'<path d="M {cx} {cy-78} L {cx-6} {cy+70}"/>'
  f'<path d="M {cx-62} {cy-12} L {cx+40} {cy-28} L {cx+60} {cy+12}"/>'
  f'<path d="M {cx+14} {cy+10} q 14 -10 6 -22 q -10 -12 -22 2 q -8 14 8 20"/>'
  f'<circle cx="{cx-34}" cy="{cy+44}" r="3" fill="#5a1a12"/><circle cx="{cx+28}" cy="{cy-52}" r="3" fill="#5a1a12"/>'
  f'<path d="M {cx+44} {cy+46} l 16 14 M {cx+60} {cy+46} l -16 14"/></g>')
for k, t in enumerate(["pintado na parede do", "vestiário, a 1,80 m do", "chão. Tinta ainda úmida.", "", "Não traduzido. Ver", "protocolo de leitura."]):
    typed(bx + bw + 26, by_ + 34 + k*24, t, 14, False, INK_S)
y = by_ + bh + 46

# ---------- observações (tinta UV)
typed(X0, y, "OBSERVAÇÕES DE CAMPO:", 14, True, INK, 2)
obs_y = y + 40
y += 112
# assinatura (parte some no canto queimado)
a(f'<line x1="{X0}" y1="{y}" x2="{X0 + 260}" y2="{y}" stroke="{INK}" stroke-opacity="0.6"/>')
line_with_bars(X0, y + 22, "Resp.: ##########")
typed(PX + PW - 262, y + 22, "Arquivado em 19/0", 15)
a('</g>')   # fim do recorte

# borda queimada
a(f'<polyline points="{" ".join(f"{x},{yy}" for x, yy in burn)}" fill="none" stroke="#1b0f07" stroke-width="16" filter="url(#char)" clip-path="url(#sheet)"/>')
a(f'<polyline points="{" ".join(f"{x},{yy}" for x, yy in burn)}" fill="none" stroke="#2a1608" stroke-width="3"/>')

# carimbo
a(f'<g transform="rotate(-11 640 668)" filter="url(#stamp)" opacity="0.78">'
  f'<rect x="545" y="640" width="190" height="56" rx="4" fill="none" stroke="{REDP}" stroke-width="3.5"/>'
  f'<text x="640" y="678" fill="{REDP}" font-family="{TYPE}" font-size="24" font-weight="700" text-anchor="middle" letter-spacing="3">ARQUIVADO</text></g>')

# impressão de consulta ao sistema, grampeada
sx, sy = 520, 44
a(f'<g transform="rotate(3.5 {sx + 130} {sy + 80})">'
  f'<rect x="{sx}" y="{sy}" width="270" height="152" fill="#e9e6dc" filter="url(#shadow)"/>'
  f'<rect x="{sx}" y="{sy}" width="270" height="152" fill="#d6d0c0" opacity="0.4" filter="url(#paper)"/>')
for k, t in enumerate(["SISTEMA · CONSULTA", "REF......: 0000-EX", "STATUS...: ENCERRADO", "ANEXOS...: [DADOS CORROMPIDOS]", "FOTOS....:", "ACESSO COMPLETO:", "  NÍVEL ▓▓ OU SUPERIOR"]):
    a(f'<text x="{sx + 14}" y="{sy + 24 + k*19}" fill="#1d1d22" font-family="{TYPE}" font-size="12" {BOLD if k == 0 else ""} xml:space="preserve">{t}</text>')
for k in range(14):   # lixo digital nas fotos
    w = random.randint(4, 12)
    a(f'<rect x="{sx + 96 + k*11}" y="{sy + 90 + random.randint(-5, 2)}" width="{w}" height="{random.randint(6, 12)}" fill="#1d1d22" opacity="{random.choice([0.9, 0.5, 0.25])}"/>')
a(f'<line x1="{sx + 110}" y1="{sy + 8}" x2="{sx + 150}" y2="{sy + 8}" stroke="#8a8f96" stroke-width="3"/>'
  f'<line x1="{sx + 110}" y1="{sy + 8}" x2="{sx + 110}" y2="{sy + 13}" stroke="#8a8f96" stroke-width="3"/><line x1="{sx + 150}" y1="{sy + 8}" x2="{sx + 150}" y2="{sy + 13}" stroke="#8a8f96" stroke-width="3"/>')
a('</g>')

# clipe
a(f'<path d="M 66 22 L 66 104 Q 66 118 78 118 Q 90 118 90 104 L 90 36 Q 90 28 82 28 Q 74 28 74 36 L 74 96" fill="none" stroke="#9aa0a8" stroke-width="3.5" stroke-linecap="round"/>')
a('</g>')   # fim do tom UV

# ---------- sob luz UV: o texto escondido aparece
if UV:
    a(f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" fill="url(#uvspot)" clip-path="url(#sheet)"/>')
    a(f'<g filter="url(#glow)" fill="#bff6ff" font-family="{HAND}" font-size="21">'
      f'<text x="{X0 + 20}" y="{obs_y + 12}" transform="rotate(-2 {X0} {obs_y})">entramos em três.</text>'
      f'<text x="{X0 + 20}" y="{obs_y + 52}" transform="rotate(-2 {X0} {obs_y})">contei quatro na saída.</text>'
      f'<text x="{X0 + 300}" y="{obs_y + 88}" font-size="17" transform="rotate(-3 {X0} {obs_y})">ninguém mais lembra.</text></g>')
    # a mancha de água também fluoresce de leve
    a(f'<g filter="url(#stain)"><ellipse cx="{X0 + 330}" cy="{wet_top + 62}" rx="160" ry="50" fill="none" stroke="#6af0c8" stroke-opacity="0.25" stroke-width="4"/></g>')
a('</g>')   # fim da rotação

a('</svg>')
open(sys.argv[1], "w", encoding="utf-8").write("\n".join(o))
print("ok", sys.argv[1], "UV" if UV else "normal")
