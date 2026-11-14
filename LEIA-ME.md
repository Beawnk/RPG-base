# Vault de RPG solo com uma IA como mestre

Uma pasta de notas em que uma IA mestra campanhas de RPG pra uma pessoa só, com o sistema que você escolher. As notas são a memória do jogo: mundo, personagens, NPCs, o que aconteceu em cada sessão e o que o mestre está escondendo de você. O mestre rola os dados com um script, não protege a personagem e prepara situações em vez de roteiro.

## O que precisa
- **Um assistente de IA que trabalhe dentro desta pasta**: que leia e grave arquivos aqui e rode comandos. A base foi preparada pro **Codex** (o assistente de código do ChatGPT), mas nada nela é exclusivo dele: serve pra qualquer assistente que leia o `AGENTS.md`.
- **Python 3**, pros scripts: o rolador de dados e, se você quiser, plantas, documentos e prints de conversa.
- Opcional: **Obsidian**, pra ler as notas com links e imagens (abra esta pasta como vault; a pasta de templates já está configurada). **Git**, se quiser histórico ou jogar em mais de um aparelho.

### Como a IA encontra as instruções
As regras do mestre estão em **`AGENTS.md`**, na raiz. O Codex lê esse arquivo sozinho, no começo de cada conversa, desde que seja aberto **nesta pasta** (a raiz do vault, não uma subpasta de fora).

- Há também uma skill do Codex em `.agents/skills/mestre/`, que só aponta pro guia do mestre. Com ela, o Codex puxa o guia sozinho quando você diz que quer jogar. Uma cópia igual fica em `.claude/skills/mestre/`, pra quem usa o Claude Code.
- Se não tiver certeza de que ele leu, comece a primeira conversa com: **"Leia o AGENTS.md desta pasta e siga-o. Você é o mestre."**
- Use o Codex **no computador** (linha de comando, extensão do editor ou aplicativo), com a pasta no seu disco. Pela nuvem, dentro do ChatGPT e ligado a um repositório, ele só enxerga o que está no repositório: os livros de `Livros de regras/` ficam de fora, e cada tarefa começa numa cópia nova. Dá pra jogar assim, mas o resumo do sistema precisa ser feito no computador.
- O Codex pode pedir sua aprovação pra rodar comandos (o script de dados, o git). Aprove os do vault; ele não precisa de internet pra jogar.
- Outro assistente que procure um arquivo com outro nome: crie um arquivo com esse nome contendo "Leia `AGENTS.md` inteiro e siga-o." O `CLAUDE.md` da raiz é uma ponte dessas e pode ser apagado.

### E se a minha IA é só um chat?
Um chat sem acesso à pasta (site ou aplicativo de conversa) funciona pior, mas funciona:
- Anexe ou cole `AGENTS.md`, `Mestre/Guia do mestre.md`, `Jogador.md`, o resumo do sistema e as notas da campanha no começo de cada conversa (ou num "projeto", se o chat tiver).
- Ela não grava nada: ao fim de cada cena, peça o texto das notas que mudaram e salve você.
- Se ela não roda Python, **você rola os dados** (de verdade, ou com `python Mestre/scripts/rolar.py 2d6+1` no seu computador) e diz o resultado. Não deixe a IA "rolar de cabeça": ela escolhe o número.
- Cuidado ao colar os arquivos de segredos: tente não ler.

## Primeiro uso
1. **Preencha `Jogador.md`**: nome, pronomes, por onde joga, o que gosta e seus limites. Se deixar em branco, o mestre pergunta na primeira conversa.
2. **Ponha o livro do sistema em `Livros de regras/`.** Essa pasta fica fora do git. Sem livro, dá pra ditar as regras ou apontar uma referência aberta.
3. **Peça o resumo do sistema**: "resume o sistema X pra gente jogar". O mestre lê o livro e preenche uma cópia de `Sistemas/_modelo.md`. Leia, corrija o que estiver errado, e está pronto.
4. **Faça a sessão zero**: "vamos criar uma campanha". Vocês combinam premissa, tom, limites, quais módulos ligar, e você cria a personagem. O mestre monta o resto escondido.
5. Depois disso, é só abrir o assistente nesta pasta e dizer "vamos jogar".

## Como jogar
Escreva o que a personagem faz, diz, pensa e sente. O mestre responde pelo resto do mundo e para quando é a sua vez. Quatro comandos:

- `Cheat:` — você fala de fora da história, com poder de autoria. O mestre aplica, corrige as notas e marca como retcon se mudar o passado. É o único jeito de mudar o resultado de um dado.
- `(OOC ...)` — pergunta ou pedido fora do jogo. O mestre responde sem avançar a cena. Serve pra tirar dúvida de regra, pedir um resumo, e pra pular ou velar uma cena (ele atende na hora, sem pedir motivo).
- `Regra:` — correção permanente no jeito de jogar. Vai pras "Regras da casa" da campanha ou da saga.
- `/fim` — encerra a sessão. O mestre move o mundo fora de cena, escreve a nota da sessão, atualiza a ficha, pede sua avaliação (opcional) e pergunta como o sistema se saiu. Em alguns assistentes a barra abre um menu de comandos; se `/fim` não passar, escreva "fim de sessão".

## O que é cada pasta
- `AGENTS.md` — as regras do mestre. `_contexto.md` — o mapa completo do vault.
- `Jogador.md` — você.
- `Mestre/` — o ofício do mestre: o guia (como conduzir cena, rolar, preparar), as referências, os módulos e os scripts. `.agents/skills/mestre/` é só o atalho do Codex pra ele.
- `Campanhas/` — as sagas (um universo) e, dentro delas, as campanhas, com personagens, NPCs, lugares, sessões.
- `Sistemas/` — um resumo por sistema de RPG. `_modelo.md` é o esqueleto.
- `Livros de regras/` — seus livros, fora do git.
- `Templates/` — o molde de cada tipo de nota.
- `Visual/` — plantas, documentos, prints e imagens. Os arquivos "Exemplo - ..." mostram o que os scripts fazem; pode apagar.
- `Referências/` — a pesquisa em que o jeito de mestrar se baseia.

## Módulos opcionais
Vêm desligados. Cada campanha liga os que quiser, na seção "Módulos ligados" do `_campanha.md` (o mestre pergunta na sessão zero; depois, é só pedir "liga o módulo X"). Desligado, o módulo não aparece no jogo.

- **Companheiros** — um elenco de NPCs com ficha e turno próprio que acompanham a personagem, com aprovação que sobe e desce conforme as suas escolhas.
- **Chat** — conversas de celular da personagem com o grupo e no privado, guardadas na íntegra, com "print" em imagem se você quiser.
- **Imagens** — o mestre escreve prompts e você gera as imagens numa IA de imagem. O estilo fica no `Jogador.md`.
- **Mural** — um quadro de investigação no Miro: o mestre põe os fatos, você põe teorias e setas. Só funciona se o seu assistente tiver integração com o Miro.

Também são opcionais as plantas e os documentos em imagem (peça quando quiser), a ficha visual (só existe se alguém escrever um script de ficha pro seu sistema) e a referência de terror, que o mestre só lê em campanha com esse tom.

## Testar e ajustar um sistema
O resumo em `Sistemas/` é uma leitura do livro, e jogar solo quase sempre pede adaptação. Por isso todo resumo termina na seção **"Ajustes em teste"**:

- Em todo `/fim` o mestre pergunta o que funcionou e o que não funcionou nas regras, e anota lá: o que mudou, por quê, em que sessão foi testado e o resultado.
- Quer mudar uma regra? Diga em `(OOC)`. O mestre compara opções, você decide, e a mudança entra como `Regra:` e como entrada em "Ajustes em teste".
- Ajuste que não deu certo fica registrado como descartado, com o motivo, pra não ser tentado de novo sem querer.

## Aviso: não abra os segredos
O mestre guarda a verdade escondida da história nas notas. Se você ler, estraga a própria surpresa. São só dele:

- `Segredos.md` e a pasta `Segredos/` de cada campanha;
- `Segredos da saga.md` de cada saga;
- os blocos recolhidos **"Só o mestre"** (callout `[!segredo]`) dentro das notas de NPC, lugar, item, facção, missão e da `Cena atual.md`. No Obsidian eles aparecem fechados: é só não clicar.

O resto das notas guarda apenas o que a sua personagem sabe, e é feito pra você ler.
