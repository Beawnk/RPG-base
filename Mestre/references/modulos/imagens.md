# Módulo: imagens

Opcional. Só vale se o `_campanha.md` tem "Imagens: sim" em "Módulos ligados". Com o módulo desligado: não escreva prompt, não proponha imagem, não pause a cena pra isso.

Quando ler: guia do mestre, "Módulos opcionais".

Você não gera imagem. Você escreve o prompt, quem joga gera numa outra IA e traz de volta. O estilo, o que evitar e qual IA estão em `Jogador.md`, seção "Imagens": leia antes do primeiro prompt e, se estiver em branco, pergunte e preencha.

## Regras

- **Quando:** monstro novo, foto ou desenho que aparece em cena, momento importante ou marcante, personagem novo que vá aparecer bastante, ou qualquer coisa que valha mostrar. Quantas por sessão e o que quem joga não quer perder: `Jogador.md`, seção "Imagens". Pausar a cena pra isso é permitido, a menos que `Jogador.md` peça outro ritmo. Companheiro ou NPC fixo entra aqui também, na hora em que aparece.
- **Onde fica o prompt:** numa nota `Visual/Prompts/<AAAA-MM-DD> - <assunto>.md`, nunca colado na conversa (polui a sessão, que pode ser relida depois). Na cena, uma linha `(OOC)` dizendo que o prompt está pronto; se quem joga usa o celular, mande o arquivo na mesma resposta.
- **Como escrever:** na língua que a outra IA entende melhor (em geral, inglês). Comece pelo estilo de `Jogador.md` e descreva tudo explicitamente: pele, olhos (qual lado, quando importa), tipo e comprimento de cabelo, marcas, roupa, pose, luz, cenário. Nunca use nacionalidade ou etnia como atalho ("Brazilian", "Asian"): descreva os traços. Se a outra IA não tem campo negativo, o que evitar vai no fim, em "Avoid: ...", sempre com a lista "O que evitar nas imagens" de `Jogador.md`. Liste no topo da nota quais refs de `Visual/` devem ser anexadas.
- **Segredos:** o prompt mostra só o que a personagem vê naquele momento. Nada dos arquivos secretos (nome verdadeiro, natureza real, o que está escondido na cena). A nota de prompt é pública.
- **Volta:** quem joga manda a imagem; confira contra as notas (rosto, olhos, marcas, roupa, objetos) e diga o que bateu e o que não. **Antes de opinar, abra a imagem e a ref da personagem (a que as notas mandam anexar) e compare lado a lado:** rosto, olhos, marcas e também a proporção do corpo (ombros, tronco, braços, pernas, tamanho da cabeça). Só afirme o que você viu nas duas; o que não der pra ver com certeza, diga que não deu (motivo: uma conferência feita de olho no prompt, e não na imagem, apontou como errado o que estava certo e deixou passar a proporção, que era o problema). Ajuste vai como prompt de edição ("Edit this image. Keep everything exactly the same... Only change: ..."), na mesma nota, como "Ajuste 1", "Ajuste 2". Aprovada: salve em `Visual/` (ou na pasta da cena), embuta na nota do que ela mostra e, com o módulo de mural ligado, ponha uma linha na fila pra imagem ir pro quadro certo no `/fim`. A decisão de aprovar é de quem joga.
- Detalhe que faltar na nota de um NPC ou do mundo: defina e grave. Da vida da personagem de quem joga: pergunte antes (regra "Sem oráculo" do guia).

## Na cena e no `/fim`

O prompt não depende de lembrar: há dois momentos fixos de conferir.

- **Ao fechar cada cena importante:** algo nela pedia imagem (foto ou desenho em cena, alguém sem ref, momento marcante) e ainda não teve prompt? Se sim, escreva agora e mande.
- **`/fim`:** conte as imagens da sessão contra o mínimo de `Jogador.md`. Se faltar, escreva o prompt do momento mais marcante e mande. Na nota da sessão, uma linha com as imagens que saíram (ou "nenhuma, e por quê").

## Molde de prompt

Mesma sequência sempre: estilo → enquadramento → pessoa → roupa → pose → cenário → clima → Avoid. Só o que a personagem vê. Os três exemplos abaixo usam personagens inventados; o trecho `[STYLE]` é o estilo de `Jogador.md` e `[AVOID]` é a lista de lá.

### Ref de personagem

```
[STYLE], bust/waist-up portrait, character reference.

A short woman in her early twenties, light brown skin with freckles across the nose and cheeks, round soft face, large dark-brown eyes. Loosely wavy hair (soft wide waves, not curly), shoulder length, dark with a single white streak on the left side of the image, held back with two small bone hairpins. Friendly, easygoing smile, but her eyes are slightly watchful and curious, sizing the viewer up.

Outfit in faded warm tones: an oversized knitted shawl slipping a little off the shoulders, a long linen skirt, worn leather boots. Many thin bracelets stacked on both wrists (wooden beads, thin copper chains, one plain red string). A cloth satchel over her shoulder with a small embroidered crescent moon. Holding a steaming clay cup with both hands.

Setting: early morning, the stone corridor of an old inn, a closed door with a small painted number "3", cold overcast light from a window mixing with the warm glow of a lantern. Quiet atmosphere that contrasts with her soft look.

Mood: sweet and approachable on the surface, with a quiet, unreadable edge. No text other than the door number.

Avoid: [AVOID], extra fingers, deformed hands, text, watermark, multiple people.
```

### Retrato antigo a partir da ref

```
Using the attached image as the character reference, create a portrait of the SAME man about ten years younger, in his early forties: same long bony face, same defined cheekbones, same long straight nose, same thin lips, same pale gray eyes and steady gaze. Salt-and-pepper hair, still more dark than gray, short and neatly combed back, slightly receding at the temples. Clean-shaven. Fewer and lighter forehead lines, faint dark circles under the eyes already there. Keep the same art style as the reference.

The image is a small official portrait, vertical 3:4 format. Strictly frontal pose, head and top of the shoulders, centered, plain pale gray-blue background, flat even lighting. He wears a dark formal coat and a plain high collar. Neutral, closed expression, no smile, looking straight at the viewer.

It looks like an old physical picture kept in a drawer for years: slightly faded colors, a soft warm yellowish tint, light paper texture, a few tiny dust specks and a faint scratch near one corner, slightly uneven border on the edges. The face itself stays sharp and clearly readable.

Avoid: [AVOID], smiling, head tilt, casual pose, background objects, beard, blur on the face, text, stamps, watermark, other people.
```

### Edição

```
Edit the first image. Keep everything exactly the same: her face, eyes, hair, smile, expression, clothes, the dog, lighting, colors, background and composition.

Only change the scar on her cheek, so it matches the scar in the second attached image (a close-up crop):
- A thin, subtle healed scar, only slightly lighter than her skin, faint and delicate, not a thick dark line.
- It starts just below the outer corner of the eye on the right side of the image and runs down to the jaw. It does not cross the nose or the mouth.
- Slightly curved, like a shallow hook at the lower end.

Avoid: [AVOID], thick or dark scar, scar too short, scar on the wrong side, scar removed, changes to anything else, text, watermark.
```

## O que a prática ensina

- Lado do rosto: com a pessoa de frente, diga pelo lado da imagem ("the eye on the LEFT side of the image (her right eye) is white"); com ela virada, diga "her right eye" e anexe a ref.
- A IA embeleza: peça explicitamente pra manter cicatriz, franja e marcas, e ponha "scar removed" no Avoid.
- Corpo todo: "head in natural proportion to the body", senão a cabeça sai grande; "not overly muscular" quando citar exercício.
- Luz quente (fim de tarde) puxa névoa: reforce "clear contrast, defined shadows".
- Edição com várias mudanças às vezes ignora uma; se errar, peça uma por vez, começando pela mais difícil.
- Um chat por personagem na outra IA evita que os traços de um vazem pro outro.
- **Sangue, carne exposta e corpo humano em criatura** (feridas, carne viva, boca ou rosto humano num monstro, cara de foto de crime) costumam ser bloqueados por violência, ou saem estranhos nos ajustes. Desde o primeiro prompt: diga que é um monstro fictício, troque "carne viva" e "sangue" por pele de cor e textura ("glossy dark crimson leathery skin"), tire armas, cápsulas e marcadores de evidência, e ponha "blood, gore, wounds" no Avoid. O detalhe mais pesado (uma boca humana, um ferimento) pode ficar só na narração: avise quem joga antes de insistir em várias tentativas (já houve caso de cinco tentativas sem sucesso, e a imagem ficou sem o detalhe).
- Prompt que deu certo com quem joga: guarde na nota de prompt como "aprovado", pra servir de molde nas próximas.
