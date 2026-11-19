# Módulo: mural

Opcional. Só vale se o `_campanha.md` tem "Mural: sim" em "Módulos ligados" e você, a IA que mestra, consegue ler e escrever no Miro (por uma integração da sua ferramenta). Sem esse acesso o módulo não funciona: avise quem joga e deixe desligado. Com o módulo desligado: não abra o Miro, não mantenha fila, e pule este arquivo no início da sessão e no `/fim`.

Quando ler: guia do mestre, "Módulos opcionais".

O mural é um quadro de investigação no Miro, pra quem joga pensar com as mãos: o mestre põe os fatos, quem joga põe teorias, setas e ligações. **As notas do vault são a verdade absoluta.** O mural sai do vault, nunca o contrário.

## A nota `Mural.md` da campanha

Fica na pasta da campanha e entra em "Notas à parte" do `_campanha.md` (gatilho: início da sessão, `/fim`, pedido de quem joga). Guarda o que é próprio daquele quadro:

```markdown
# Mural
- Quadro: <link do quadro no Miro>
- Regras desta campanha: (cores, o que quem joga combinou a mais)

## Quadros
| Quadro | id | Pra quê | Espaço livre |
|---|---|---|---|
| Teorias | | só de quem joga | |
| To-do | | horários, ideias, a parte "Meus" de quem joga | |

## Notas pretas atuais
- (ids das notas da última sessão, que viram cinza no próximo `/fim`)

## Fila do mural
- quadro · texto da nota (fonte, sN)
- quadro · CORRIGIR: o que a nota diz → o que vale (fonte da correção, sN ou data)
```

## Regras

- **O Miro só se abre em três momentos:** no início da sessão (ler), no `/fim` (colocar a fila e arrumar o To-do) e quando quem joga pedir. **Não abra o Miro durante o jogo** (motivo: cada leitura de quadro gasta muito contexto, e isso faz a sessão ser resumida no meio).
- **A fila vai junto com a gravação da cena.** Todo fato novo que a personagem viu, leu ou ouviu entra na nota certa do vault e ganha uma linha na "Fila do mural" de `Mural.md` (`quadro · texto da nota (fonte, sN)`), na mesma resposta em que a cena é gravada (e no mesmo commit, se o vault usa git). O fim de cena só está completo com a fila em dia. Toda informação minimamente relevante fica no vault: é dele que o mural sai no `/fim`.
- **Fato corrigido também entra na fila.** Quando um fato que já pode estar no mural muda (retcon, `Cheat:`, correção de quem joga, erro achado pelo arquivista), a mesma resposta que corrige a nota põe na fila uma linha `quadro · CORRIGIR: o que a nota diz → o que vale (fonte, sN)`. Se não sabe se o fato chegou ao mural, ponha a linha mesmo assim: no `/fim` se confere.
- **Uma linha da fila = um assunto = uma nota no Miro.** Nada de juntar numa nota o resultado de um teste, uma coisa do passado e uma fala sobre outro tema. Mais notas e quadro maior são melhores que nota misturada.
- **As notas do mestre são fatos:** em **preto** as da última sessão, em **cinza** as anteriores (no `/fim`, as pretas antigas viram cinza e as novas entram em preto, pra quem joga ver o que é novo).
- **As notas de quem joga são de quem joga.** Teorias, setas e o quadro Teorias: nunca mexa, corrija nem comente, nem pra dizer que bate ou que não bate com o vault (motivo: quem joga quer acertar ou errar por conta própria). O que quem joga entendeu certo ou errado vai só pros segredos.
- Seu conhecimento vem do vault, nunca do mural. Se o mural e o vault discordarem, vale o vault, e a diferença não se comenta. Exceção: nota do mestre (preta ou cinza) com erro, que o mestre corrige no mural pela fila ("CORRIGIR").

## No início da sessão

Leia pouco: o quadro Teorias, as notas de quem joga nos outros quadros e o To-do (a parte "Meus" e o que foi marcado). Atualize a seção "O que quem joga suspeita e planeja" (em `Agora.md`, se o `Segredos.md` foi dividido; senão, no próprio `Segredos.md`). O mural diz pra onde quem joga quer ir e o que está pensando; **não é fonte de fatos**.

## `/fim`: colocar a fila

Durante o jogo o Miro fica fechado e os fatos novos se acumulam na fila. Agora:

1. Confira a fila contra a nota da sessão: tudo o que a personagem viu, leu ou ouviu de relevante tem linha?
2. Leia só os quadros que vão receber nota (uma leitura por quadro, pelos ids de `Mural.md`).
3. Troque pra cinza as notas pretas da sessão anterior (ids em "Notas pretas atuais").
4. Crie as notas novas **em preto** nos espaços livres e anote os ids delas em "Notas pretas atuais".
   - Linha "CORRIGIR": ache a nota do mestre que diz o antigo (busca no quadro) e troque o texto, sem mudar cor nem posição. Se não achar em quadro nenhum, o fato não tinha chegado ao mural: apague a linha. Nota de quem joga nunca se corrige.
5. Personagem importante novo (um companheiro, um NPC recorrente) ganha quadro próprio com tudo o que a personagem sabe dele, sem cobrir nota de quem joga.
6. Esvazie a fila e atualize a coluna "Espaço livre".
7. Ao reescrever o preparo da próxima sessão (`Agora.md`, ou o `Segredos.md` se ele não foi dividido), leve junto a seção "O que quem joga suspeita e planeja", com a leitura do mural em dia.

**To-do do mural:** reescreva "Horários" e "Ideias pra hoje" a partir de `Cena atual.md` (relógios e a lista "Esperando") e de `Linhas abertas.md`. Só o que a personagem sabe: nada dos segredos, nenhuma sugestão que aponte pra uma verdade escondida. Leia o quadro antes. **Limpe os riscados:** tudo o que está riscado sai, inclusive na parte "Meus". O que quem joga escreveu e não riscou fica como está, com as marcações que tiver (o que cada cor quer dizer fica em "Regras desta campanha"). Item seu que ficou velho (já feito em jogo ou que perdeu sentido) sai. Depois de limpar, suba os itens pra não sobrar linha vazia no meio.
