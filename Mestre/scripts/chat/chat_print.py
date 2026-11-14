#!/usr/bin/env python3
"""Gera o "print do celular" (SVG) de uma conversa de celular, lendo a nota de Chat.

Uso:
  python chat_print.py "Chat/<nota>.md" saida.svg --eu Lena [--titulo "nome do grupo"] [--hora 23:40] [--dia hoje]

Lê as linhas `**Nome** (HH:MM): texto` da seção "## Mensagens". Marcadores especiais no texto:
  [foto: descrição]             foto (desenhada como foto borrada com a descrição)
  [figurinha: 😎 descrição]     figurinha (emoji opcional no começo)
  [áudio 0:42: o que diz]       áudio com duração (transcrição opcional)
  [mensagem apagada]
  [digitando]                   bolha de "digitando…" (normalmente a última)
As mensagens de --eu ficam à direita. Grupo mostra o nome de quem fala; privado não.

Fotos de perfil: lidas de `Visual/Chat/avatares.json` na raiz do vault (nome na mensagem -> imagem),
ou passadas com --avatar "Nome=caminho" (pode repetir). No privado, a foto do contato vai no topo;
no grupo, a foto do grupo (se houver, pela chave do título) vai no topo e a de cada pessoa vai ao lado
da primeira bolha de cada sequência dela. Quem não tem foto aparece com a inicial, como antes.
"""
import argparse, base64, html, json, os, re, unicodedata, zlib

FONT = "'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Segoe UI Emoji', 'Apple Color Emoji', sans-serif"
CORES = ['#f2a65a', '#7cc6fe', '#e57fae', '#9be38b', '#c9a7ff', '#ffd166', '#6fd6c9']


def esc(s):
    return html.escape(s, quote=True)


def ler_nota(path):
    txt = open(path, encoding='utf-8').read().replace('\r\n', '\n')
    fm = {}
    m = re.match(r'^---\n(.*?)\n---\n', txt, re.S)
    if m:
        for line in m.group(1).split('\n'):
            if ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip()
    tit = re.search(r'^# (.+)$', txt, re.M)
    sec = re.search(r'^## Mensagens\n(.*?)(?=^## |\Z)', txt, re.S | re.M)
    msgs = []
    for line in (sec.group(1) if sec else '').split('\n'):
        s = line.strip()
        mm = re.match(r'^\*\*(.+?)\*\* \((\d{1,2}:\d{2})\): (.*)$', s)
        if mm:
            msgs.append(dict(nome=mm.group(1), hora=mm.group(2), texto=mm.group(3)))
        elif msgs and s and not s.startswith(('>', '<!--')):
            msgs[-1]['texto'] += '\n' + s
    parts = [p.strip() for p in fm.get('participantes', '').strip('[]').split(',') if p.strip()]
    return fm, (tit.group(1) if tit else ''), msgs, parts


def is_emoji(ch):
    o = ord(ch)
    return o >= 0x1F000 or (0x2600 <= o <= 0x27BF) or unicodedata.category(ch) == 'So'


def cw(ch, size):
    o = ord(ch)
    if o in (0xFE0F, 0x200D) or 0x1F3FB <= o <= 0x1F3FF:
        return 0
    if is_emoji(ch):
        return size * 1.2
    if ch in "il.,;:'!|ı":
        return size * 0.26
    if ch in 'fjtrI()[] -':
        return size * 0.34
    if ch in 'mwMW':
        return size * 0.82
    if ch.isupper() or ch.isdigit():
        return size * 0.6
    return size * 0.52


def tw(s, size):
    return sum(cw(c, size) for c in s)


def wrap(text, maxw, size):
    out = []
    for para in text.split('\n'):
        cur = ''
        for w in para.split(' '):
            t = (cur + ' ' + w) if cur else w
            if tw(t, size) <= maxw or not cur:
                cur = t
            else:
                out.append(cur)
                cur = w
        out.append(cur)
    return out


def raiz_vault(inicio):
    d = os.path.abspath(inicio)
    while True:
        if os.path.isdir(os.path.join(d, '.obsidian')):
            return d
        pai = os.path.dirname(d)
        if pai == d:
            return os.getcwd()
        d = pai


def carregar_avatares(nota, json_path, extras):
    raiz = raiz_vault(os.path.dirname(os.path.abspath(nota)))
    mapa = {}
    jp = json_path or os.path.join(raiz, 'Visual', 'Chat', 'avatares.json')
    if os.path.isfile(jp):
        for k, v in json.load(open(jp, encoding='utf-8')).items():
            if not k.startswith('_'):
                mapa[k] = v
    for e in extras or []:
        if '=' in e:
            k, v = e.split('=', 1)
            mapa[k.strip()] = v.strip()
    dados = {}
    for nome, cam in mapa.items():
        cam = cam if os.path.isabs(cam) else os.path.join(raiz, cam)
        if not os.path.isfile(cam):
            print(f'aviso: foto de {nome} não encontrada ({cam})')
            continue
        ext = os.path.splitext(cam)[1].lower()
        mime = {'.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp'}.get(ext, 'image/png')
        dados[nome] = f'data:{mime};base64,' + base64.b64encode(open(cam, 'rb').read()).decode()
    return dados


def corner_path(x, y, w, h, tl, tr, br, bl):
    return (f'M{x+tl},{y} H{x+w-tr} Q{x+w},{y} {x+w},{y+tr} V{y+h-br} Q{x+w},{y+h} {x+w-br},{y+h} '
            f'H{x+bl} Q{x},{y+h} {x},{y+h-bl} V{y+tl} Q{x},{y} {x+tl},{y} Z')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('nota')
    ap.add_argument('saida')
    ap.add_argument('--eu', required=True, help='nome da personagem de quem joga (fica à direita)')
    ap.add_argument('--titulo', help='nome do grupo ou do contato no topo')
    ap.add_argument('--hora', help='hora no relógio do celular (padrão: hora da última mensagem)')
    ap.add_argument('--dia', default='hoje', help='etiqueta de data no topo da conversa')
    ap.add_argument('--avatar', action='append', help='foto de perfil: "Nome=caminho" (pode repetir)')
    ap.add_argument('--avatares', help='JSON nome -> foto (padrão: Visual/Chat/avatares.json do vault)')
    a = ap.parse_args()

    fm, titulo_nota, msgs, parts = ler_nota(a.nota)
    grupo = fm.get('canal', 'grupo') == 'grupo'
    outros = [p for p in parts if p != a.eu]
    for m in msgs:
        if m['nome'] != a.eu and m['nome'] not in outros:
            outros.append(m['nome'])
    cor = {n: CORES[i % len(CORES)] for i, n in enumerate(outros)}
    titulo = a.titulo or (titulo_nota if grupo else (outros[0] if outros else ''))
    fotos = carregar_avatares(a.nota, a.avatares, a.avatar)
    pid = {n: f'av{i}' for i, n in enumerate(fotos)}
    contato = titulo if grupo else (outros[0] if outros else titulo)
    AV = 34 if grupo else 0      # espaço da foto ao lado das bolhas, no grupo
    hora_tela = a.hora or (msgs[-1]['hora'] if msgs else '00:00')

    # ---- geometria
    PAD = 30
    FW = 400                 # largura do aparelho
    SX, SW = PAD + 12, FW - 24
    TOP_STATUS, TOP_HEAD = 44, 64
    INPUT_H = 72
    MAXW = 248               # largura máx. do texto na bolha
    FS, LH = 15, 20

    # ---- layout das mensagens (primeiro passo: alturas)
    itens = []
    prev = None
    for m in msgs:
        eu = m['nome'] == a.eu
        primeiro = prev != m['nome']
        prev = m['nome']
        t = m['texto'].strip()
        mostra_nome = grupo and not eu and primeiro
        k = dict(m=m, eu=eu, primeiro=primeiro, nome=mostra_nome)
        mt = re.match(r'^\[(foto|figurinha|áudio|audio|mensagem apagada|digitando)\s*(\d+:\d{2})?\s*:?\s*(.*?)\]$', t, re.S)
        tipo = mt.group(1) if mt else 'texto'
        tipo = 'áudio' if tipo == 'audio' else tipo
        k['tipo'] = tipo
        nome_h = 18 if mostra_nome else 0
        if tipo == 'texto':
            linhas = wrap(t, MAXW, FS)
            k['linhas'] = linhas
            hw = tw('00:00', 11) + 10
            larg = max([tw(l, FS) for l in linhas] + [tw(m['nome'], 13) if mostra_nome else 0])
            extra = 0
            if tw(linhas[-1], FS) + hw > MAXW:
                extra = 14
            else:
                larg = max(larg, tw(linhas[-1], FS) + hw)
            k['w'] = larg + 22
            k['h'] = 8 + nome_h + len(linhas) * LH + extra + 8
        elif tipo == 'foto':
            k['desc'] = mt.group(3).strip()
            k['w'] = 244
            k['h'] = 6 + nome_h + 160 + 6
        elif tipo == 'figurinha':
            d = mt.group(3).strip()
            em = ''
            if d and is_emoji(d[0]):
                em, _, d = d.partition(' ')
            k['emoji'], k['desc'] = em or '🙂', d
            k['w'] = 124
            k['h'] = nome_h + 124 + 18
        elif tipo == 'áudio':
            k['dur'] = (mt.group(2) or '').strip() or '0:10'
            tr = mt.group(3).strip()
            k['trans'] = wrap('“' + tr + '”', MAXW - 10, 13) if tr else []
            k['w'] = 262
            k['h'] = 8 + nome_h + 40 + len(k['trans']) * 17 + (6 if k['trans'] else 0) + 8
        elif tipo == 'mensagem apagada':
            k['w'] = tw('🚫 Mensagem apagada', 14) + tw('00:00', 11) + 34
            k['h'] = 8 + nome_h + 20 + 8
        else:  # digitando
            k['w'] = 62
            k['h'] = nome_h + 36
        k['gap'] = 10 if primeiro else 3
        itens.append(k)

    conteudo = 14 + 24 + 10 + sum(k['gap'] + k['h'] for k in itens) + 16
    SH = max(700, TOP_STATUS + TOP_HEAD + conteudo + INPUT_H)
    FH = SH + 24
    W, H = FW + 2 * PAD, FH + 2 * PAD
    SY = PAD + 12
    CHAT_Y = SY + TOP_STATUS + TOP_HEAD

    o = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}">')
    o.append(f'''<defs>
  <clipPath id="tela"><rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" rx="36"/></clipPath>
  <filter id="sombra" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000" flood-opacity="0.45"/></filter>
  <filter id="ruido" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="4"/>
    <feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.035 0"/>
  </filter>
{''.join(f'<pattern id="{pid[n]}" patternContentUnits="objectBoundingBox" width="1" height="1"><image width="1" height="1" preserveAspectRatio="xMidYMid slice" href="{fotos[n]}"/></pattern>' for n in fotos)}
  <filter id="borrao" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
    <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="3" seed="11"/>
    <feColorMatrix values="0.25 0.1 0 0 0.12  0.2 0.15 0 0 0.11  0.15 0.1 0.05 0 0.1  0 0 0 0 1"/>
    <feGaussianBlur stdDeviation="3"/>
  </filter>
</defs>''')
    # aparelho
    o.append(f'<rect x="{PAD}" y="{PAD}" width="{FW}" height="{FH}" rx="48" fill="#060708" stroke="#34383d" stroke-width="2" filter="url(#sombra)"/>')
    o.append(f'<rect x="{PAD+3}" y="{PAD+3}" width="{FW-6}" height="{FH-6}" rx="45" fill="none" stroke="#15181b" stroke-width="3"/>')
    o.append('<g clip-path="url(#tela)">')
    o.append(f'<rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" fill="#0d1115"/>')
    o.append(f'<rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" filter="url(#ruido)"/>')

    # barra de status
    o.append(f'<text x="{SX+30}" y="{SY+29}" fill="#e8eaed" font-size="15" font-weight="600">{esc(hora_tela)}</text>')
    o.append(f'<rect x="{SX+SW/2-52}" y="{SY+10}" width="104" height="27" rx="13.5" fill="#000"/>')
    bx = SX + SW - 30
    o.append(f'<rect x="{bx-25}" y="{SY+18}" width="23" height="12" rx="3.5" fill="none" stroke="#e8eaed" stroke-opacity=".6"/>'
             f'<rect x="{bx-23}" y="{SY+20}" width="13" height="8" rx="2" fill="#e8eaed"/>'
             f'<rect x="{bx-1}" y="{SY+22}" width="2" height="4" rx="1" fill="#e8eaed" fill-opacity=".6"/>')
    for i in range(4):
        hb = 4 + i * 2.6
        o.append(f'<rect x="{bx-58+i*5}" y="{SY+30-hb}" width="3.2" height="{hb}" rx="1" fill="#e8eaed" fill-opacity="{1 if i < 3 else .35}"/>')

    # cabeçalho
    hy = SY + TOP_STATUS
    o.append(f'<rect x="{SX}" y="{hy}" width="{SW}" height="{TOP_HEAD}" fill="#161b20"/>')
    o.append(f'<line x1="{SX}" y1="{hy+TOP_HEAD}" x2="{SX+SW}" y2="{hy+TOP_HEAD}" stroke="#222a31"/>')
    o.append(f'<path d="M{SX+24},{hy+22} l-9,10 l9,10" fill="none" stroke="#7cc6fe" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>')
    ax, ay = SX + 58, hy + 32
    letra = next((c for c in titulo if c.isalpha()), '?').upper()
    av_cor = '#2c3e4a' if grupo else cor.get(titulo, '#2c3e4a')
    letra_cor = '#e8eaed' if grupo else '#0d1115'
    if contato in fotos:
        o.append(f'<circle cx="{ax}" cy="{ay}" r="19" fill="url(#{pid[contato]})"/>')
    else:
        o.append(f'<circle cx="{ax}" cy="{ay}" r="19" fill="{av_cor}"/>')
        o.append(f'<text x="{ax}" y="{ay+6}" text-anchor="middle" fill="{letra_cor}" font-size="17" font-weight="700">{esc(letra)}</text>')
    o.append(f'<text x="{ax+30}" y="{ay-3}" fill="#e8eaed" font-size="16" font-weight="600">{esc(titulo)}</text>')
    if grupo:
        sub = ', '.join('você' if p == a.eu else p for p in (parts or outros))
        sub_cor = '#8b96a0'
    elif itens and itens[-1]['tipo'] == 'digitando':
        sub, sub_cor = 'digitando…', '#5fd38d'
    else:
        ult = [m['hora'] for m in msgs if m['nome'] != a.eu]
        sub, sub_cor = (f'visto por último às {ult[-1]}' if ult else ''), '#8b96a0'
    o.append(f'<text x="{ax+30}" y="{ay+15}" fill="{sub_cor}" font-size="12.5">{esc(sub)}</text>')
    for i in range(3):
        o.append(f'<circle cx="{SX+SW-22}" cy="{ay-7+i*7}" r="1.8" fill="#8b96a0"/>')

    # etiqueta de dia
    y = CHAT_Y + 14
    dw = tw(a.dia, 12) + 22
    o.append(f'<rect x="{SX+SW/2-dw/2}" y="{y}" width="{dw}" height="24" rx="12" fill="#1c2329"/>')
    o.append(f'<text x="{SX+SW/2}" y="{y+16}" text-anchor="middle" fill="#9aa5ae" font-size="12">{esc(a.dia)}</text>')
    y += 24 + 10

    def hora_txt(x, yy, hh, cor_='#8b96a0', fundo=False):
        s = ''
        if fundo:
            ww = tw(hh, 11) + 10
            s += f'<rect x="{x-ww+5}" y="{yy-11}" width="{ww}" height="15" rx="7.5" fill="#000" fill-opacity=".45"/>'
        s += f'<text x="{x}" y="{yy}" text-anchor="end" fill="{cor_}" font-size="11">{esc(hh)}</text>'
        return s

    for k in itens:
        y += k['gap']
        m, eu, tipo = k['m'], k['eu'], k['tipo']
        w, h = k['w'], k['h']
        x = SX + SW - 12 - w if eu else SX + 12 + AV
        if grupo and not eu and k['primeiro']:
            cx, cy = SX + 12 + 14, y + 14
            if m['nome'] in fotos:
                o.append(f'<circle cx="{cx}" cy="{cy}" r="14" fill="url(#{pid[m["nome"]]})"/>')
            else:
                le = next((c for c in m['nome'] if c.isalpha()), '?').upper()
                o.append(f'<circle cx="{cx}" cy="{cy}" r="14" fill="{cor.get(m["nome"], "#2c3e4a")}"/>'
                         f'<text x="{cx}" y="{cy+5}" text-anchor="middle" fill="#0d1115" font-size="13" font-weight="700">{esc(le)}</text>')
        fill = '#1f5a46' if eu else '#1d252c'
        r = 13
        if k['primeiro']:
            tl, tr = (r, 4) if eu else (4, r)
        else:
            tl = tr = r
        nome_h = 18 if k['nome'] else 0
        hcor = '#a9d8c4' if eu else '#8b96a0'
        ncor = cor.get(m['nome'], '#e8eaed')

        if tipo in ('texto', 'mensagem apagada', 'foto', 'áudio'):
            o.append(f'<path d="{corner_path(x, y, w, h, tl, tr, r, r)}" fill="{fill}"/>')
            if k['nome']:
                o.append(f'<text x="{x+11}" y="{y+20}" fill="{ncor}" font-size="13" font-weight="600">{esc(m["nome"])}</text>')

        if tipo == 'texto':
            ty = y + 8 + nome_h + 15
            for ln in k['linhas']:
                o.append(f'<text x="{x+11}" y="{ty}" fill="#e8eaed" font-size="{FS}">{esc(ln)}</text>')
                ty += LH
            o.append(hora_txt(x + w - 9, y + h - 8, m['hora'], cor_=hcor))
        elif tipo == 'mensagem apagada':
            o.append(f'<text x="{x+11}" y="{y+8+nome_h+15}" fill="#8b96a0" font-size="14" font-style="italic">🚫 Mensagem apagada</text>')
            o.append(hora_txt(x + w - 9, y + h - 8, m['hora'], cor_=hcor))
        elif tipo == 'foto':
            px, py, pw, ph = x + 6, y + 6 + nome_h, w - 12, 160
            cid = f'f{zlib.crc32((m["hora"] + k["desc"]).encode()) % 100000}'
            o.append(f'<clipPath id="{cid}"><rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="9"/></clipPath>')
            o.append(f'<g clip-path="url(#{cid})"><rect x="{px}" y="{py}" width="{pw}" height="{ph}" filter="url(#borrao)"/>'
                     f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="#000" fill-opacity=".35"/></g>')
            o.append(f'<text x="{px+pw/2}" y="{py+34}" text-anchor="middle" font-size="22">📷</text>')
            dy = py + 58
            for ln in wrap(k['desc'], pw - 26, 12)[:6]:
                o.append(f'<text x="{px+pw/2}" y="{dy}" text-anchor="middle" fill="#dfe4e8" fill-opacity=".85" font-size="12" font-style="italic">{esc(ln)}</text>')
                dy += 16
            o.append(hora_txt(px + pw - 7, py + ph - 7, m['hora'], cor_='#e8eaed', fundo=True))
        elif tipo == 'figurinha':
            sy = y
            if k['nome']:
                o.append(f'<text x="{x+2}" y="{y+13}" fill="{ncor}" font-size="13" font-weight="600">{esc(m["nome"])}</text>')
                sy += nome_h
            o.append(f'<rect x="{x}" y="{sy}" width="{w}" height="{w}" rx="18" fill="#161c21" stroke="#36414a" stroke-dasharray="5 4"/>')
            o.append(f'<text x="{x+w/2}" y="{sy+62}" text-anchor="middle" font-size="50">{esc(k["emoji"])}</text>')
            dy = sy + 86
            for ln in wrap(k['desc'], w - 16, 10.5)[:3]:
                o.append(f'<text x="{x+w/2}" y="{dy}" text-anchor="middle" fill="#8b96a0" font-size="10.5" font-style="italic">{esc(ln)}</text>')
                dy += 13
            o.append(hora_txt(x + w - 4, sy + w + 14, m['hora']))
        elif tipo == 'áudio':
            cy = y + 8 + nome_h + 20
            bola = '#2c7a5f' if eu else '#2b3640'
            o.append(f'<circle cx="{x+28}" cy="{cy}" r="16" fill="{bola}"/>')
            o.append(f'<path d="M{x+23},{cy-8} L{x+35},{cy} L{x+23},{cy+8} Z" fill="#e8eaed"/>')
            seed = zlib.crc32((m['hora'] + k['dur']).encode())
            for i in range(30):
                seed = (seed * 1103515245 + 12345) & 0x7fffffff
                bh = 4 + (seed % 19)
                op = .9 if i < 3 else .55
                o.append(f'<rect x="{x+54+i*5.6}" y="{cy-bh/2}" width="3" height="{bh}" rx="1.5" fill="#9fb0bd" fill-opacity="{op}"/>')
            o.append(f'<text x="{x+54}" y="{cy+28}" fill="#8b96a0" font-size="11">{esc(k["dur"])}</text>')
            ty = cy + 30 + 14
            for ln in k['trans']:
                o.append(f'<text x="{x+11}" y="{ty}" fill="#c3ccd3" font-size="13" font-style="italic">{esc(ln)}</text>')
                ty += 17
            o.append(hora_txt(x + w - 9, y + h - 8, m['hora'], cor_=hcor))
        else:  # digitando
            by = y + nome_h
            if k['nome']:
                o.append(f'<text x="{x+2}" y="{y+13}" fill="{ncor}" font-size="13" font-weight="600">{esc(m["nome"])}</text>')
            o.append(f'<path d="{corner_path(x, by, w, 36, tl, tr, r, r)}" fill="{fill}"/>')
            for i, op in enumerate((.9, .6, .35)):
                o.append(f'<circle cx="{x+18+i*13}" cy="{by+18}" r="4" fill="#9aa5ae" fill-opacity="{op}"/>')
        y += h

    # barra de digitar
    iy = SY + SH - INPUT_H
    o.append(f'<rect x="{SX}" y="{iy}" width="{SW}" height="{INPUT_H}" fill="#12171b"/>')
    o.append(f'<rect x="{SX+12}" y="{iy+12}" width="{SW-74}" height="42" rx="21" fill="#1f262d"/>')
    o.append(f'<text x="{SX+32}" y="{iy+38}" fill="#6f7b85" font-size="15">Mensagem</text>')
    mx, my = SX + SW - 33, iy + 33
    o.append(f'<circle cx="{mx}" cy="{my}" r="21" fill="#2c7a5f"/>')
    o.append(f'<rect x="{mx-4}" y="{my-11}" width="8" height="14" rx="4" fill="#e8eaed"/>'
             f'<path d="M{mx-8},{my-1} a8,8 0 0 0 16,0 M{mx},{my+7} v5" fill="none" stroke="#e8eaed" stroke-width="2" stroke-linecap="round"/>')
    o.append(f'<rect x="{SX+SW/2-60}" y="{SY+SH-8}" width="120" height="4" rx="2" fill="#e8eaed" fill-opacity=".5"/>')
    o.append('</g></svg>')

    with open(a.saida, 'w', encoding='utf-8') as f:
        f.write('\n'.join(o))
    print(f'ok: {a.saida} ({W}x{H}, {len(msgs)} mensagens)')


if __name__ == '__main__':
    main()
