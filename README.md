# RPG-base

Uma base pra jogar RPG solo com uma IA como mestre. É uma pasta de notas em Markdown (dá pra abrir como vault do Obsidian) com as regras e o ofício de um mestre: a IA lê essas instruções, conduz a campanha e grava tudo nas notas, que viram a memória do jogo.

> **Isto não é um programa.** Não tem nada pra instalar nem executar além de uns scripts auxiliares em Python. Você joga conversando com o assistente de IA que preferir (Claude Code, Codex do ChatGPT ou outro), aberto nesta pasta.

## O que vem aqui (e o que não vem)

É uma versão limpa, pronta pra qualquer pessoa clonar:

- **Vem:** as regras do mestre (`AGENTS.md`), o guia de como mestrar (`Mestre/`), templates de nota, o esqueleto pra resumir um sistema (`Sistemas/_modelo.md`), scripts de dados, plantas, documentos e prints de chat, e a pesquisa em que o jeito de mestrar se baseia (`Referências/`).
- **Não vem:** campanhas, sistemas resumidos, livros de regras nem dados de jogador. Você cria os seus depois de clonar.

O mestre não protege a personagem, rola os dados com um script (nunca escolhe o número) e prepara situações, não roteiro.

## O que precisa

- **Um assistente de IA que trabalhe dentro de uma pasta**: que leia e grave arquivos e rode comandos. Ex.: Claude Code, Codex. Um chat comum também serve, com mais trabalho manual (ver `LEIA-ME.md`).
- **Python 3**, pro rolador de dados e os outros scripts. Só usam a biblioteca padrão, nada pra instalar.
- Opcional: **Obsidian**, pra ler as notas com links e imagens; **Git**, pra histórico e pra receber atualizações desta base.

## Como começar

1. Clone o repositório e abra o seu assistente de IA **na raiz da pasta**.
   ```bash
   git clone https://github.com/Beawnk/RPG-base.git
   ```
2. Preencha `Jogador.md` (nome, pronomes, por onde joga, gostos e limites) ou deixe em branco que o mestre pergunta.
3. Ponha o livro do sistema em `Livros de regras/` (fica fora do git) e peça: *"resume o sistema X pra gente jogar"*. Revise o resumo que ele gerar em `Sistemas/`.
4. Faça a sessão zero: *"vamos criar uma campanha"*.
5. Daí em diante, é só abrir o assistente na pasta e dizer *"vamos jogar"*.

Se o assistente não ler as instruções sozinho, comece com: *"Leia o AGENTS.md desta pasta e siga-o. Você é o mestre."*

Durante o jogo há quatro comandos: `Cheat:` (você muda a história com poder de autoria), `(OOC ...)` (fala fora da personagem: dúvida, pedido ou conversa que não é da cena), `Regra:` (correção permanente) e `/fim` (encerra a sessão).

**O passo a passo completo está no [`LEIA-ME.md`](LEIA-ME.md)**: como cada assistente encontra as instruções, os comandos, as pastas, os módulos opcionais (companheiros, chat, imagens, mural) e como testar e ajustar um sistema.

> ⚠️ **Não abra os segredos.** `Segredos.md`, a pasta `Segredos/`, `Segredos da saga.md` e os blocos recolhidos "Só o mestre" das notas são do mestre. Ler estraga a sua própria surpresa.

## Treinar o mestre sem perder as atualizações

O mestre melhora com o uso: cada `Regra:`, cada avaliação no `/fim` e cada ajuste de sistema fica gravado nas notas. Pra continuar puxando as atualizações desta base sem conflito, **cada coisa vai na camada dela**, e o núcleo fica limpo:

| O que você quer guardar | Onde |
|---|---|
| Regra ou combinado de uma história | "Regras da casa" no `_campanha.md` (ou no `_saga.md`, se vale pra saga toda) |
| Regra de um sistema, adaptação pro solo | `Sistemas/<sistema>.md`, em "Ajustes em teste" |
| Você: ritmo, limites, gostos, estilo de imagem | `Jogador.md` |
| Como mestrar, em qualquer sistema e campanha | núcleo: `AGENTS.md` e `Mestre/` |

**Evite pôr no núcleo** (`AGENTS.md`, `Mestre/`, `Templates/`, a skill `mestre`) nome de personagem, de campanha, de pessoa ou mecânica de um sistema específico. Esses arquivos são os que recebem atualização daqui. Se você editar, cada `git pull` vira conflito pra resolver na mão. O mestre já sabe disso e pergunta em que camada gravar quando você usa `Regra:`.

Os arquivos que você cria (campanhas, sistemas) não conflitam com nada. `Jogador.md` e o "Estado atual" do `_contexto.md` vêm em branco e você preenche. Se um dia vier atualização neles, o conflito é pequeno: fique com a sua versão.

### Usar o seu próprio repositório

O mestre faz commit e push sozinho no fim de cada cena. Depois de clonar, aponte o `origin` pro **seu** repositório (de preferência privado, já que as notas guardam os segredos das campanhas) e mantenha esta base como `upstream`:

```bash
git remote rename origin upstream
```

```bash
git remote add origin https://github.com/<seu-usuario>/<seu-repo>.git
```

```bash
git push -u origin main
```

Pra receber as atualizações da base:

```bash
git pull upstream main
```

## Para onde o projeto vai

- **Agora:** melhorar os textos de referência e treinar o mestre jogando, com mais de um sistema, e trazer pra cá o que valer pra qualquer campanha.
- **Segredos só em arquivo de segredo:** hoje o lado oculto de NPCs, lugares, itens e facções fica num callout recolhido dentro da própria nota. No Obsidian ele aparece fechado, mas em qualquer outro editor, no GitHub ou na própria conversa com a IA ele fica à vista. A ideia é mover esses segredos pra `Segredos/` e deixar as notas públicas só com o que a personagem sabe.
- **Depois:** evoluir pra um programa de jogar RPG no estilo de uma mesa virtual (como Foundry VTT ou Roll20), com a IA como opção de mestre. A ideia é de uso pessoal, pra jogar com amigos, não um produto.

Hoje, nada disso existe como programa: as sessões acontecem no seu assistente de IA, e esta pasta é o que ele lê e grava.
