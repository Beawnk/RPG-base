# Contexto do vault RPG

Vault de campanhas de RPG solo, com uma IA como mestre. Serve pra qualquer assistente que leia e grave arquivos nesta pasta e rode Python; dá pra jogar pelo PC (com o Obsidian aberto ao lado, se quiser) e pelo celular, se o assistente tiver aplicativo. Sincronizar por git é opcional.

As regras de como mestrar estão no `AGENTS.md`. Este arquivo é o mapa: onde cada coisa fica e como as notas são escritas.

## Estrutura

```
(raiz do vault)
├── LEIA-ME.md              pra quem nunca viu o vault: o que é, primeiro uso, como jogar (vem com a cópia exportada)
├── AGENTS.md               regras do mestre (valem pra todas as campanhas). É o nome que a maioria dos assistentes de IA lê sozinha
├── CLAUDE.md               ponte pro AGENTS.md. Abaixo da marca "Só deste vault" pode ter o que só vale pro Claude Code aqui (não é exportado)
├── .claude/skills/mestre/  skill `mestre`: um atalho que manda ler o guia do mestre. O conteúdo fica em Mestre/, não aqui. A cópia exportada leva a mesma skill também em .agents/skills/mestre/, pro Codex
├── .exportar/              só no vault-fonte: o script que exporta o núcleo pra cópia neutra e os arquivos que só existem nela
├── Jogador.md              quem joga: nome, pronomes, por onde joga, quem rola os dados, lista de opções, preferências, estilo de imagem
├── _contexto.md            este mapa
├── Mestre/                 o ofício de mestre
│   ├── Guia do mestre.md   o ofício: cena, rolagens, registro (núcleo, lido inteiro; "Antes de enviar" relido a cada fim de cena)
│   ├── Histórico do guia.md  de onde veio cada regra (o incidente); não se lê em jogo
│   ├── references/         preparo.md, fim.md (o `/fim` inteiro, lido antes de começar), imprevistos.md, descrever.md, rolagens.md, visuais.md e notas.md (sempre valem, lidos no gatilho que o guia diz)
│   │   ├── modulos/        opcionais, ligados por campanha: companheiros.md, chat.md, imagens.md, mural.md
│   │   └── generos/        opcionais de gênero, lidos quando o tom pede: terror.md, investigação.md (também quando quem joga gosta de puzzle)
│   └── scripts/            rolar.py (todas as rolagens); chat/ (print de conversa); mapas/ (plantas e grade); documentos/ (documento com parte oculta)
├── Sistemas/               um resumo por sistema de RPG, reaproveitável entre campanhas; `_modelo.md` é o esqueleto de todo resumo; `scripts/` guarda o que é de um sistema só (ex.: script de ficha visual)
├── Referências/            pesquisas e material de apoio (ex.: Ofício de mestre em RPG solo)
├── Livros de regras/       os livros dos sistemas. Fora do git (direito autoral e tamanho): só existe no computador de quem joga. O que o jogo precisa vai resumido pra Sistemas/. Ao lado de cada PDF, quando houver, o texto extraído (`.txt`, com a marca `[pdf p. N]` em cada página), pra procurar com grep sem abrir o PDF
├── Patch notes/           um arquivo por dia (`AAAA-MM-DD.md`) com o que mudou fora do jogo e como era antes, pra desfazer (`AGENTS.md`, "Patch notes"). Nasce na primeira mudança
├── Templates/              um por tipo de nota (lista em "Estado atual")
├── Visual/                 imagens (pasta de anexos do Obsidian): `Visual/Mapas/` plantas de lugares (SVG); `Visual/Documentos/` documentos do jogo (SVG); `Visual/Fichas/` ficha visual, só em campanha que tem script de ficha; `Visual/Chat/` prints e `avatares/` (fotos de perfil do chat, mapeadas em `avatares.json`), módulo de chat; `Visual/Prompts/` prompts de imagem, módulo de imagens. Nomes: `<Nome> - ref N`, `<Nome> - perfil`, `<Nome> - sessão N`. Os arquivos "Exemplo - ..." mostram o que cada script faz
└── Campanhas/
    └── <Nome da saga>/          universo compartilhado; toda campanha mora numa saga, mesmo que seja a única
        ├── _saga.md             o mundo, campanhas em ordem, linha do tempo, quem está onde, regras da saga
        ├── Personagens/         personagens de quem joga, uma nota por personagem (passam de uma campanha pra outra)
        ├── NPCs/                uma nota por NPC, companheiros incluídos (persistem na saga)
        ├── Lugares/  Itens/  Facções/
        ├── Chat/                módulo de chat: toda conversa de celular da personagem, uma nota por conversa, na íntegra, e o índice `_chat.md`
        ├── Segredos/            TUDO o que é secreto na saga, e só aqui. Fora desta pasta, toda nota é pública
        │   ├── Segredos da saga.md   o que atravessa campanhas e os ganchos de continuação
        │   ├── Entidades/            `<Nome> (segredo).md`: o lado oculto de cada NPC, lugar, item e facção; um por entidade, criado junto com a nota
        │   └── <Nome da campanha>/   `Segredos.md` (ameaças, vilão, verdades, pistas planejadas; núcleo, com o índice), `Cena.md` (lado oculto da cena atual, dificuldades antes do dado) e, em campanha grande, `Agora.md` (lido sempre), `Companheiros/`, `Missões/`, `Arquivo.md`, `Material.md` (lidos quando o índice manda)
        └── <Nome da campanha>/
            ├── _campanha.md     premissa, tom, limites, dificuldade aberta ou secreta, módulos ligados, regras da casa desta campanha
            ├── Cena atual.md    só a cena de agora: onde, quando, quem, ameaças
            ├── Linhas abertas.md missões, mistérios, promessas, ameaças em aberto
            ├── Mural.md         módulo de mural: link, quadros, regras e a fila do que ainda não foi pro Miro
            ├── Regras visuais.md  regras de mapa, planta e documentos da campanha, lidas quando o gatilho acontece
            ├── Missões/         uma ficha de investigação por missão (template Missão)
            └── Sessões/         uma nota por sessão
```

Campanha encerrada vira cânone da saga: fica onde está, as próximas consultam, ninguém reescreve (só `Cheat:`).

Pastas são criadas quando o primeiro arquivo delas existir — não crie estrutura vazia.

## As quatro camadas
Cada regra e cada lição aprendida em jogo mora numa camada só. É o que deixa o núcleo servir pra qualquer pessoa e qualquer sistema.

| Camada | Onde fica | O que guarda |
|---|---|---|
| Núcleo | `AGENTS.md`, `Mestre/`, `Templates/`, `Sistemas/_modelo.md`, `.claude/skills/mestre/` | como mestrar, em qualquer sistema e campanha |
| Sistema | `Sistemas/<sistema>.md`, `Sistemas/scripts/` | regras do livro, escala de dificuldade, ficha, ajustes em teste |
| Quem joga | `Jogador.md` | nome, pronomes, por onde joga, preferências, estilo de imagem |
| Campanha | `_saga.md`, `_campanha.md` e as notas da saga | regras da casa, combinados, fatos e exemplos daquela história |

No núcleo não entra nome de pessoa, de personagem ou de campanha, nem mecânica de um sistema. Onde gravar uma correção nova: `AGENTS.md`, comando `Regra:`.

## Onde ficam os segredos
Tudo o que quem joga não pode ver mora numa pasta só por saga, `Campanhas/<saga>/Segredos/`. Fora dela, toda nota é pública e pode ser aberta em qualquer lugar. Os caminhos abaixo são a partir dessa pasta.

| O que | Arquivo | Quando o mestre lê |
|---|---|---|
| O que atravessa campanhas, ganchos de continuação | `Segredos da saga.md` | início de sessão |
| O lado oculto de um NPC, lugar, item ou facção | `Entidades/<Nome> (segredo).md` | antes de a entidade entrar em cena, ser citada ou agir fora dela |
| Ameaças, vilão, verdades, pistas planejadas da campanha | `<campanha>/Segredos.md` | início de sessão |
| O lado oculto da cena atual: dificuldades gravadas antes do dado, inimigos, o que vem | `<campanha>/Cena.md` | início de sessão, antes de cada teste, depois de compactação |
| O mundo depois da última sessão e o preparo da próxima (campanha grande) | `<campanha>/Agora.md` | início de sessão |
| Plano de cada companheiro (campanha grande) | `<campanha>/Companheiros/Companheiro N.md` | antes de ele entrar em cena ou falar no chat |
| Preparo de cada missão (campanha grande) | `<campanha>/Missões/Missão N.md` | quando a missão está pra começar ou em andamento |
| Sessões já jogadas, com os testes; material de apoio | `<campanha>/Arquivo.md`, `<campanha>/Material.md` | só pra consultar |

- Em campanha pequena só existem `Segredos.md` e `Cena.md`. Quando o `Segredos.md` passa de umas 200 linhas ele é dividido: vira o núcleo, com um índice do que ler e quando, e nascem os outros arquivos.
- As regras (nota pública sem segredo, a linha fixa `> Lado do mestre: ...`, arquivo de segredo de toda entidade, nome de arquivo, wikilink, segredo descoberto) estão no `AGENTS.md`, "Segredos".

## Convenções
- Nome de arquivo = nome da coisa, com acentos e espaços (`Mestre Ondina.md`), pra wikilinks funcionarem natural.
- Notas de sessão: `Sessões/AAAA-MM-DD - Título curto.md`.
- Ligar tudo com wikilinks `[[Nome]]`.
- Frontmatter mínimo em NPCs, lugares, itens e facções:
  ```yaml
  tipo: npc | lugar | item | faccao
  campanha: <nome>
  status: ativo | morto | desaparecido | destruido | resolvido
  ```
  NPC e facção também têm `atitude: aliado | amigável | neutro | hostil` (é só um rótulo de como o NPC trata a personagem; não tem nada a ver com a aprovação dos companheiros); companheiro (módulo) usa `aprovacao` (-50 a 100) e `papel: principal | opcional`. Os arquivos fixos usam `tipo: saga | segredos-saga | campanha | cena | linhas | segredos | segredo | sessao | chat | chat-indice` (`segredo` é o arquivo de segredo de uma entidade), e a personagem de quem joga `tipo: personagem`. Toda nota tem `saga:`; `campanha:` é a campanha da nota (nas entidades, a campanha em que apareceu primeiro).
- Cada nota começa com 1–2 linhas do essencial; detalhes depois.
- No Obsidian, vale pôr a pasta de segredos de cada saga em Configurações → Arquivos e links → Arquivos excluídos, pra busca e o seletor rápido não mostrarem trechos dela.
- Os arquivos fixos (`_campanha`, `Cena atual`, `Linhas abertas`) têm o mesmo nome em toda campanha. Pra linkar um deles, use o caminho: `[[Campanhas/<saga>/<campanha>/Cena atual|Cena atual]]`. Arquivo de segredo nunca se linka: quando precisar citar um, escreva o caminho entre crases. A personagem de quem joga tem nota com o nome dela em `Personagens/`.
- No histórico de NPC, lugar, item e facção, linke a nota da sessão (`[[AAAA-MM-DD - Título]]`), nunca o template.
- Anotação de origem: quando um fato ou uma regra vem de quem joga, marque `(de quem joga, AAAA-MM-DD)` e, se houver, o motivo. O motivo é o que importa guardar.

## O que o mestre (a IA) pode editar
- Livre: as notas da saga ativa e a campanha ativa dentro dela, este arquivo (manter em dia sem pedir), `Jogador.md` quando quem joga responder ou pedir, "Ajustes em teste" do sistema em uso, e o resto de `Sistemas/` e `Templates/` quando quem joga pedir.
- Só leitura: campanhas encerradas da saga ativa (cânone).
- Perguntar antes: `AGENTS.md`, o guia do mestre (pasta `Mestre/`), e qualquer coisa de outra saga.

## Estado atual
> Atualizado em todo `/fim`, sem pedir.
- **Nenhuma saga ainda.** O vault está no estado inicial: falta preencher `Jogador.md`, resumir um sistema em `Sistemas/` e fazer a sessão zero da primeira campanha.
- **Sistemas resumidos:** nenhum. `Sistemas/_modelo.md` é o esqueleto.
- **Sessões jogadas:** nenhuma.
- **Regras que mudaram:** nenhuma ainda. Registre aqui, por sessão, o que mudou nas regras da casa e no guia.
- Templates: Saga (vira o `_saga.md`), Segredos da saga, Campanha (vira o `_campanha.md`), Personagem, Cena atual, Linhas abertas, Segredos, Cena (segredos), Segredo de entidade, Missão (ficha de investigação), Segredo de missão, NPC, Lugar, Item, Facção, Sessão; dos módulos: Companheiro (NPC com ficha e turno), Chat (uma conversa) e Chat índice (vira o `Chat/_chat.md`). Placeholders `{{title}}`/`{{date:YYYY-MM-DD}}` e `<...>`: o mestre troca pelos valores ao criar notas. No Obsidian, a pasta de templates já está apontada em `.obsidian/templates.json`.
- Guia do mestre em `Mestre/`, baseado em pesquisa sobre ofício de mestre (Alexandrian, Dungeon World, Blades in the Dark, Sly Flourish, estudos sobre LLM como mestre). Decisões de base: ameaças ficam em `Segredos.md`, sem oráculo, todo segredo na pasta `Segredos/` da saga (nenhum em nota pública). A pesquisa completa está em `Referências/Ofício de mestre em RPG solo.md`.
