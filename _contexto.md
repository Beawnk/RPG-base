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
├── Jogador.md              quem joga: nome, pronomes, por onde joga, preferências, estilo de imagem
├── _contexto.md            este mapa
├── Mestre/                 o ofício de mestre
│   ├── Guia do mestre.md   o ofício: cena, rolagens, registro
│   ├── references/         preparo.md e imprevistos.md (sempre valem)
│   │   ├── modulos/        opcionais, ligados por campanha: companheiros.md, chat.md, imagens.md, mural.md
│   │   └── generos/        opcionais de gênero, lidos quando o tom pede: terror.md
│   └── scripts/            rolar.py (todas as rolagens); chat/ (print de conversa); mapas/ (plantas e grade); documentos/ (documento com parte oculta)
├── Sistemas/               um resumo por sistema de RPG, reaproveitável entre campanhas; `_modelo.md` é o esqueleto de todo resumo; `scripts/` guarda o que é de um sistema só (ex.: script de ficha visual)
├── Referências/            pesquisas e material de apoio (ex.: Ofício de mestre em RPG solo)
├── Livros de regras/       os livros dos sistemas. Fora do git (direito autoral e tamanho): só existe no computador de quem joga. O que o jogo precisa vai resumido pra Sistemas/
├── Templates/              um por tipo de nota (lista em "Estado atual")
├── Visual/                 imagens (pasta de anexos do Obsidian): `Visual/Mapas/` plantas de lugares (SVG); `Visual/Documentos/` documentos do jogo (SVG); `Visual/Fichas/` ficha visual, só em campanha que tem script de ficha; `Visual/Chat/` prints e `avatares/` (fotos de perfil do chat, mapeadas em `avatares.json`), módulo de chat; `Visual/Prompts/` prompts de imagem, módulo de imagens. Nomes: `<Nome> - ref N`, `<Nome> - perfil`, `<Nome> - sessão N`. Os arquivos "Exemplo - ..." mostram o que cada script faz
└── Campanhas/
    └── <Nome da saga>/          universo compartilhado; toda campanha mora numa saga, mesmo que seja a única
        ├── _saga.md             o mundo, campanhas em ordem, linha do tempo, quem está onde, regras da saga
        ├── Segredos da saga.md  o que atravessa campanhas e os ganchos de continuação (o mestre nunca revela)
        ├── Personagens/         personagens de quem joga, uma nota por personagem (passam de uma campanha pra outra)
        ├── NPCs/                uma nota por NPC, companheiros incluídos (persistem na saga)
        ├── Lugares/  Itens/  Facções/
        ├── Chat/                módulo de chat: toda conversa de celular da personagem, uma nota por conversa, na íntegra, e o índice `_chat.md`
        └── <Nome da campanha>/
            ├── _campanha.md     premissa, tom, limites, quem rola, módulos ligados, regras da casa desta campanha
            ├── Cena atual.md    só a cena de agora: onde, quando, quem, ameaças
            ├── Linhas abertas.md missões, mistérios, promessas, ameaças em aberto
            ├── Segredos.md      ameaças, vilão, verdades, pistas planejadas desta campanha (núcleo, com o índice)
            ├── Segredos/        campanha grande: `Agora.md` (lido sempre), `Companheiros/`, `Missões/`, `Arquivo.md`, `Material.md` (lidos quando o índice manda)
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
  NPC e facção também têm `atitude: aliado | amigável | neutro | hostil` (é só um rótulo de como o NPC trata a personagem; não tem nada a ver com a aprovação dos companheiros); companheiro (módulo) usa `aprovacao` (-50 a 100) e `papel: principal | opcional`. Os arquivos fixos usam `tipo: saga | segredos-saga | campanha | cena | linhas | segredos | sessao | chat | chat-indice`, e a personagem de quem joga `tipo: personagem`. Toda nota tem `saga:`; `campanha:` é a campanha da nota (nas entidades, a campanha em que apareceu primeiro).
- Cada nota começa com 1–2 linhas do essencial; detalhes depois.
- O lado oculto de NPC, lugar, item e facção vai num callout recolhido `> [!segredo]- Só o mestre` dentro da própria nota. Fora dele, a nota guarda só o que a personagem sabe ou viu.
- Os arquivos fixos (`_campanha`, `Cena atual`, `Linhas abertas`, `Segredos`) têm o mesmo nome em toda campanha. Pra linkar um deles, use o caminho: `[[Campanhas/<saga>/<campanha>/Cena atual|Cena atual]]`. A personagem de quem joga tem nota com o nome dela em `Personagens/`.
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
- Templates: Saga (vira o `_saga.md`), Segredos da saga, Campanha (vira o `_campanha.md`), Personagem, Cena atual, Linhas abertas, Segredos, Missão (ficha de investigação), NPC, Lugar, Item, Facção, Sessão; dos módulos: Companheiro (NPC com ficha e turno), Chat (uma conversa) e Chat índice (vira o `Chat/_chat.md`). Placeholders `{{title}}`/`{{date:YYYY-MM-DD}}` e `<...>`: o mestre troca pelos valores ao criar notas. No Obsidian, a pasta de templates já está apontada em `.obsidian/templates.json`.
- Guia do mestre em `Mestre/`, baseado em pesquisa sobre ofício de mestre (Alexandrian, Dungeon World, Blades in the Dark, Sly Flourish, estudos sobre LLM como mestre). Decisões de base: ameaças ficam em `Segredos.md`, sem oráculo, segredos de entidade em callout `[!segredo]`. A pesquisa completa está em `Referências/Ofício de mestre em RPG solo.md`.
