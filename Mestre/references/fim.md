# `/fim`: o fim de sessão, passo a passo

Leia este arquivo inteiro antes de começar o `/fim` (o `AGENTS.md` manda) e siga na ordem, sem pular passo. É a única lista do `/fim`: o que cada módulo faz no fim está no arquivo dele, e aqui só aparece a chamada.

Os passos com a marca **(módulo)** só existem se o módulo está ligado em "Módulos ligados" do `_campanha.md`. Desligado, pule o passo inteiro.

## Os passos

0. **Checagem de consistência** (todo `/fim`, sem exceção): rode a lista da seção "Checagem de consistência" abaixo antes de escrever a nota da sessão. O checklist de cena pega o que mudou na cena; só esta passada pega o que ficou velho ou ficou de fora.
1. **Mova o mundo.** Pra cada ameaça em que quem joga não tocou nesta sessão, decida se ela avançou fora de cena (presságio ou relógio). NPCs com objetivo também agem. Registre só na pasta de segredos: em `Segredos.md` ou no arquivo de segredo do NPC ("fazendo agora" e "próximo passo"). Com o `Segredos.md` dividido: reescreva `Agora.md` pra próxima sessão (o mundo depois desta, o que fica preparado) e passe pro `Arquivo.md` o que já foi jogado, com os testes da sessão que estavam em `Cena.md`. A personagem vai ficar sabendo por notícia, boato ou estrago, na próxima sessão.
2. **Pistas e segredos.** Marque o que foi dado. Descarte os que perderam sentido. Reponha.
3. **Nota da sessão** em `Sessões/` (template Sessão): resumo, consequências, ganchos. Só o que a personagem sabe.
4. **Onde paramos.** Primeiro, ao pé da letra: releia as últimas respostas da cena e passe pra seção "Esperando" da `Cena atual.md` o retrato exato do último momento: pra cada um que está ali, o que faz, o que tem na mão e em que estado (comida pela metade, copo quase vazio, caderno fechado), e a última fala ou gesto de cada um, como foi, sem resumir. Por quê: a sessão seguinte abre da nota, não da conversa, e uma nota vaga fez a abertura contradizer o fim da sessão anterior. Depois, o resto da `Cena atual.md`, o `Cena.md` dos segredos (as dificuldades da sessão vão pro arquivo; fica só o que vale pra próxima) e `Linhas abertas.md`.
5. **Ficha**, sempre, mesmo que nada pareça ter mudado. A nota da personagem manda. Confira nela (`Personagens/`), campo por campo, a lista "O que conferir no `/fim`" da seção "Ficha" de `Sistemas/<sistema>.md` (vida, recursos, condições, evolução, inventário, marcas e o que mais o sistema contar) e os contadores que o sistema acumulou na sessão.
   - **Ficha visual, só se a campanha tem script de ficha** (linha "Ficha visual" do `_campanha.md`): o arquivo de dados é o espelho da nota, e a imagem sai dele. Atualize primeiro a nota, depois o arquivo de dados (valores atuais, a data e o momento, ex. "após sessão 3"), regenere com o comando da linha "Ficha visual", abra a imagem e confira antes de gravar. Mande a ficha nova se quem joga usa o celular. Sem script, este item não existe.
6. **Dificuldades.** Confira a distribuição das dificuldades da sessão contra a escala do sistema: se quase todas caíram no mesmo degrau alto, anote o que corrigir.
7. **Módulos ligados**, cada um pelo `/fim` do arquivo dele, em `Mestre/references/modulos/`:
   - **(módulo) Companheiros:** aprovação, quem ficou na base, fichas (`companheiros.md`, "Registro e `/fim`").
   - **(módulo) Chat:** toda conversa salva e indexada; mensagem pendente de quem agiu fora de cena (`chat.md`, "`/fim`").
   - **(módulo) Imagens:** imagens da sessão contra o mínimo de `Jogador.md` (`imagens.md`, "Na cena e no `/fim`").
   - **(módulo) Mural:** colocar a fila inteira (fatos novos e correções) e arrumar o To-do (`mural.md`, "`/fim`: colocar a fila").
8. **Avaliação** (opcional; quem joga pode pular): peça nota de 0 a 10 e o porquê pra sessão, história, interações, ambientação, narração e testes. Grave nas palavras de quem joga em "Avaliação de quem joga" na nota da sessão, sem suavizar, e escreva uma linha do que o mestre leva pra próxima. No início da sessão seguinte, releia essa parte. Crítica que aparece em duas sessões vira proposta de mudança no guia do mestre (ou `Regra:`), que só entra com o sim de quem joga.
9. **Sistema** (uma pergunta; quem joga pode pular): o que funcionou e o que não funcionou nas regras nesta sessão? Grave a resposta em "Ajustes em teste" de `Sistemas/<sistema>.md`: o que mudou na regra, por quê, em que sessão foi testado e o resultado. Se a resposta pede mudança de regra, proponha em modo colaborador; só entra com o sim de quem joga, como `Regra:`.
10. **Mapa do vault:** atualize "Estado atual" no `_contexto.md` (onde a campanha parou, o que mudou nas regras e no guia), sem pedir. Atualize também "Estado geral" no `_campanha.md` e a linha do tempo no `_saga.md`.
11. **Patch notes:** se nesta sessão mudou alguma regra, template ou nota fora do jogo (`Regra:`, `Cheat:` com retcon, correção pedida por quem joga), confira se entrou no patch note do dia (`AGENTS.md`, "Patch notes").
12. **Git**, se o vault usa: commit + push.

## Checagem de consistência

Em todo `/fim` (passo 0) e quando quem joga pedir, revise sem criar canon novo:

- nome ou fato contraditório entre notas
- o que um NPC contou do próprio passado nesta sessão bate com a linha do tempo dele nos segredos? Detalhe novo entrou nela?
- NPC, lugar ou item citado em jogo sem nota (qualquer um com nome e chance de voltar, inclusive família da personagem)
- o que foi narrado e não está em nota nenhuma: fala em que um NPC conta algo de si ou do mundo, texto lido em cena, ambiente novo (um banheiro, uma copa)
- arquivo de segredo de entidade com "fazendo agora" ou "próximo passo" de uma sessão atrás
- **notas de entidade de quem apareceu na sessão** (`Mestre/references/notas.md`): o bloco Agora, o da nota e o do segredo, bate com o resto da nota? A linha "Atualizado" está em dia? Promessa cumprida, horário que passou ou fato que mudou estão marcados como vencidos? Linha de "O que sabe" de cena em que ele não estava? Fato da nota da sessão ou do chat que não chegou à nota dele? Entidade sem Agora que deve aparecer na próxima sessão: monte agora
- pista dada e não marcada na lista dela (reviravoltas, segredos soltos, pistas planejadas)
- `Cena.md` (segredos): dificuldades antigas (vão pro arquivo, "Testes da sessão N") e "se ela fizer X" que já aconteceu
- pasta da campanha nos segredos da saga (`Campanhas/<saga>/Segredos/<campanha>/`): `Agora.md` (se existe) ainda fala de coisa já jogada? o índice do núcleo bate com os arquivos?
- segredo fora do lugar: bloco `[!segredo]` ou fato oculto numa nota pública; entidade com nota e sem arquivo de segredo em `Entidades/` (ou o contrário); wikilink dentro da pasta de segredos
- `Linhas abertas.md`: item na seção errada, perigo que já passou, coisa fechada fora de "Fechadas"
- detalhe sobre a vida da personagem que entrou em cena sem o sim de quem joga: pergunte em `(OOC)` se vale
- segredo que vazou pra narração ou pra nota pública
- presságio que deveria ter avançado e foi esquecido
- ficha que não bate com o que aconteceu
- **(módulo) Companheiros:** a tabela do núcleo bate com os planos e com as notas de quem já apareceu? No Histórico da nota, o motivo de cada aprovação está nos termos do que a personagem fez e viu, sem palavra do plano dele?
- **(módulo) Chat:** conversa de celular sem registro em `Chat/`
- **(módulo) Mural:** fato que a personagem viu, leu ou ouviu e não está no mural nem na fila de `Mural.md`; fato corrigido nas notas (retcon, correção de quem joga) sem linha de correção na fila

Reporte em `(OOC)`. Corrija só erro óbvio de registro. Contradição de história: pergunte qual versão vale.
