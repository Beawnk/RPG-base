# Vault de RPG solo com uma IA como mestre

Uma pasta de notas em que uma IA mestra campanhas de RPG pra uma pessoa só, com o sistema que você escolher. As notas são a memória do jogo: mundo, personagens, NPCs, o que aconteceu em cada sessão e o que o mestre está escondendo de você. O mestre rola os dados com um script, não protege a personagem e prepara situações em vez de roteiro.

## O que precisa
- **Um assistente de IA que trabalhe dentro desta pasta**: que leia e grave arquivos aqui e rode comandos. Nada na base é exclusivo de um assistente: serve qualquer um que leia o `AGENTS.md`. Os passos específicos dos dois mais usados, Claude Code e Codex, estão mais abaixo.
- **Python 3**, pros scripts: o rolador de dados e, se você quiser, plantas, documentos e prints de conversa. Só usam a biblioteca padrão, nada pra instalar.
- Opcional: **Obsidian**, pra ler as notas com links e imagens (abra esta pasta como vault; a pasta de templates já está configurada). **Git**, se quiser histórico ou jogar em mais de um aparelho.

### Como a IA encontra as instruções
As regras do mestre estão em **`AGENTS.md`**, na raiz. Abra o assistente **nesta pasta** (a raiz do vault, não uma subpasta nem uma pasta acima dela).

- Muitos assistentes leem o `AGENTS.md` sozinhos no começo de cada conversa. Se o seu procura um arquivo com outro nome, crie um arquivo com esse nome contendo "Leia `AGENTS.md` inteiro e siga-o." O `CLAUDE.md` da raiz é uma ponte dessas.
- Há uma skill `mestre`, um atalho que manda ler o guia do mestre, em duas cópias iguais: `.claude/skills/mestre/` e `.agents/skills/mestre/`. Um assistente que entende skills puxa o guia sozinho quando você diz que quer jogar.
- Se não tiver certeza de que ele leu, comece a primeira conversa com: **"Leia o AGENTS.md desta pasta e siga-o. Você é o mestre."**
- O assistente vai pedir sua aprovação pra rodar comandos (o script de dados, o git). Aprove os do vault. Ele não precisa de internet pra jogar, só pro `git push`.
- **Use no computador, com a pasta no seu disco.** Versões que rodam na nuvem a partir de um repositório só enxergam o que está nele: os livros de `Livros de regras/` ficam de fora, e cada tarefa começa numa cópia nova. Dá pra jogar assim, mas o resumo do sistema precisa ser feito no computador.

### No Claude Code
- **Abrir:** no terminal, entre na pasta do vault e rode `claude`. No aplicativo (aba Code) ou na extensão do editor, escolha esta pasta como projeto.
- **Instruções:** ele lê o `CLAUDE.md` sozinho, e esse arquivo puxa o `AGENTS.md` inteiro (pela linha `@AGENTS.md`). Se você usa o Claude Code, não apague o `CLAUDE.md`.
- **Skill:** a de `.claude/skills/mestre/` é encontrada sozinha. Também dá pra chamar com `/mestre`.
- **Aprovações:** ele pergunta antes de rodar `python` e `git`. Pra não aprovar toda rolagem, escolha a opção de sempre permitir na primeira vez. Isso fica gravado em `.claude/settings.local.json`, que está fora do git.
- **Pelo celular:** uma sessão nova do Claude Code na web ou no app do Claude roda na nuvem, a partir do repositório (vale o aviso acima). Pra jogar pelo celular com a pasta do seu computador, use o **Remote Control**: abra a sessão no PC com `claude --remote-control` (ou digite `/remote-control` numa sessão já aberta, inclusive no aplicativo e na extensão do VS Code) e continue em claude.ai/code ou no app do Claude. O PC precisa ficar ligado, e o recurso pede login com uma assinatura do Claude (não funciona com chave de API).

### No Codex
- **Abrir:** pela linha de comando (rode `codex` dentro da pasta do vault), pela extensão do editor ou pelo aplicativo, sempre com a pasta no seu disco.
- **Instruções:** ele lê o `AGENTS.md` sozinho, nada a configurar. O `CLAUDE.md` não serve pra ele e pode ser apagado se você só usa o Codex.
- **Skill:** a de `.agents/skills/mestre/`.
- **Aprovações:** dependendo do modo de aprovação, ele pede confirmação pra rodar comandos. Aprove os do vault. Se o sandbox bloquear a rede, o mestre faz o commit, avisa que o push ficou pendente e você faz o push depois.
- **Na nuvem:** pelo ChatGPT, ligado a um repositório, ele só vê o que está no repositório (vale o aviso acima).

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
- `(OOC ...)` — você fala fora da personagem: uma pergunta, um pedido ou uma conversa que não é da cena (nem sempre é sobre o jogo). O mestre responde sem avançar a cena. Serve pra tirar dúvida de regra, pedir um resumo, e pra pular ou velar uma cena (ele atende na hora, sem pedir motivo).
- `Regra:` — correção permanente no jeito de jogar. O mestre pergunta em que camada ela vale: só nesta campanha ou saga, nas regras do sistema, em você (`Jogador.md`) ou no jeito de mestrar.
- `/fim` — encerra a sessão. O mestre move o mundo fora de cena, escreve a nota da sessão, atualiza a ficha, pede sua avaliação (opcional) e pergunta como o sistema se saiu. Em alguns assistentes a barra abre um menu de comandos; se `/fim` não passar, escreva "fim de sessão".

## O que é cada pasta
- `AGENTS.md` — as regras do mestre. `_contexto.md` — o mapa completo do vault.
- `CLAUDE.md` — ponte pro `AGENTS.md`, pro Claude Code.
- `Jogador.md` — você.
- `Mestre/` — o ofício do mestre: o guia (como conduzir cena, rolar, preparar), as referências, os módulos e os scripts.
- `.claude/skills/mestre/` e `.agents/skills/mestre/` — a skill `mestre`, só um atalho pro guia, em duas cópias iguais.
- `Campanhas/` — as sagas (um universo) e, dentro delas, as campanhas, com personagens, NPCs, lugares, sessões. Dentro de cada saga, a pasta `Segredos/` é só do mestre.
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
O mestre guarda a verdade escondida da história numa pasta só. Se você ler, estraga a própria surpresa. É só dele:

- a pasta `Segredos/` de cada saga (`Campanhas/<saga>/Segredos/`), inteira: os segredos da saga, os de cada campanha e o lado oculto de cada NPC, lugar, item e facção.

O resto das notas guarda apenas o que a sua personagem sabe, e é feito pra você ler em qualquer lugar: no Obsidian, em outro editor, no GitHub ou na conversa com a IA. Nenhuma nota pública leva segredo; a de um NPC ou lugar só tem uma linha apontando pro arquivo de segredo dele.

No Obsidian, vale pôr a pasta de segredos em Configurações → Arquivos e links → Arquivos excluídos, pra busca e o seletor rápido não mostrarem trechos dela.
