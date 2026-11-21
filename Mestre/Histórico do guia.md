# Histórico do guia

Não se lê durante o jogo. Guarda de onde veio cada regra do guia do mestre e das referências: o incidente que a motivou (quando ficou registrado), quando entrou e o que mudou depois. No guia fica a regra com um "por quê" curto; a história fica aqui.

**Antes de pôr uma regra nova no guia**, procure uma que já diga a mesma coisa ou quase: se existe, reescreva ou funda com ela, e registre aqui. Regra nova só entra como linha nova se não houver nenhuma parecida. Por quê: cada erro virava uma regra a mais, o guia crescia, e um guia maior faz o mestre seguir cada regra com menos firmeza, justamente o que causa os erros (sessão de 2026-11-16, quando um NPC soube o que não viu apesar de o guia já dizer que NPC só sabe o que presenciou).

## 2026-11-21: arquivo de tipo novo entra no mapa na hora
- Um índice de investigação foi criado fora do jogo e ficou fora do `_contexto.md`: o mapa só era atualizado no passo 10 do `/fim`, e só no "Estado atual". Quem joga pediu que todo arquivo importante novo entre no mapa. Ficou no `AGENTS.md` (vale dentro e fora do jogo), com o corte "tipo novo" pra o mapa não inchar com cada nota de template, e uma conferência no passo 10 do `/fim`.

## 2026-11-18 (noite): cada regra num lugar só, `/fim` em arquivo próprio, patch notes
- Uma auditoria pedida por quem joga achou regras ditas duas, três e até seis vezes (ler o Agora antes do NPC, as regras de dado, o `/fim`, os gatilhos dos módulos). Cada cópia envelhecia de um jeito e duas já se contradiziam (o `AGENTS.md` mandava ler a nota inteira, o guia mandava ler o Agora). Cada regra ficou num lugar, e os outros apontam pra ele: regra fixa no `AGENTS.md`, ofício no guia, o detalhe na referência. Exceção pedida por quem joga: `references/rolagens.md` guarda tudo de rolagem junto, inclusive o que repete o `AGENTS.md` e o guia.
- O `/fim` estava metade no `AGENTS.md` e metade no `preparo.md`, intercalados ("antes do passo X do AGENTS"). Foi pra `references/fim.md`, numa lista só, que o `AGENTS.md` manda ler antes de começar (ideia de quem joga).
- Agora de lugar, item e facção: o guia mandava montar antes da cena e o `notas.md` dizia "quando a nota crescer". Quem joga escolheu o primeiro: toda entidade sem Agora ganha um antes de entrar em cena, e os templates de lugar, item e facção nascem com ele.
- Marcar vencido passou pro arquivista (antes só no `/fim`), porque uma promessa cumprida ficava escrita como aberta até o fim da sessão.
- Fila do mural com correção: quatro fatos corrigidos num mesmo dia (um número de quarto, um intervalo de tempo, quem sabia de uma conversa, uma data) já estavam no mural, e a fila só sabia receber fato novo.
- Motivo de aprovação na nota pública só com o que a personagem fez e viu: o Histórico de dois companheiros explicava cada aprovação com palavras do plano secreto deles.
- Patch notes: quem joga quer poder desfazer qualquer mudança feita fora do jogo sem caçar no git. O patch note diz o que mudou e como era; este histórico continua dizendo por que a regra existe.

## 2026-11-18: dieta do guia e releitura por cena
- O guia passou de 40 mil pra uns 26 mil caracteres. O detalhe de descrição, de rolagens e de peças visuais foi pra `references/descrever.md`, `references/rolagens.md` e `references/visuais.md`, lidos no gatilho. As histórias dos incidentes vieram pra cá.
- Entrou "Antes de enviar" (as regras que mais escapam, em uma linha cada) e "Releitura durante a sessão": a cada fim de cena, reler "Antes de enviar" e as notas de quem está na próxima cena, mesmo que já lidas. Por quê: numa sessão longa, o mestre passou a narrar da conversa em vez das notas, e os erros de memória e de "quem sabe o quê" se acumularam no fim. Reler por contagem de mensagens foi descartado: o modelo não vê um contador e estima mal.
- Entraram também três lições da mesma sessão que não estavam escritas como regra: coisa certa no mundo real não precisa de sorteio (um app de entrega com "poucas opções" numa cidade grande); esquecer um detalhe como gente esquece pode, saber o que não viu não (quem joga pediu pra não corrigir a fala de um NPC que esqueceu algo); fato errado numa nota vai corrigido na hora (um objeto que a ficha punha no lugar errado, a ordem dos andares de um prédio).

## 2026-11-18: os erros que mais se repetem, sessões 1 a 6

Leitura do feedback e da avaliação de quem joga em todas as sessões jogadas até aqui, pra ver o que volta.

| Erro | Sessões | Onde o guia trata |
|---|---|---|
| Controle da personagem (ação, gesto final, conclusão, deslocamento, cena andando depois do dado ou do OOC) | 2, 3, 4, 5, 6 | "Quem fala pelo quê", "Antes de enviar" |
| Fato antigo trocado (quando algo foi feito, quem entregou o quê, onde está um objeto, ontem × hoje cedo) | 2, 4, 5, 6 | "Antes de enviar", fato antigo; releitura por cena. Entrou agora: quem fez o quê e tempo relativo |
| Registro esquecido (lista lida, resposta no mural, aprovação, laços, o que quem joga contou) | 2, 4, 6 | Arquivista |
| Achar que uma leitura antiga basta (o mural, numa sessão em que o mestre achou que a leitura do `/fim` anterior bastava) | 3, 6 | Releitura. Entrou agora: leitura de sessão anterior também não conta |
| Regra respondida só pelo resumo do sistema, sem conferir no livro nem avisar | 5, 6 | Entrou agora em "Rolagens": procurar no livro e dizer onde procurou |
| Texto de exercício confuso | 4 | Entrou agora em "Ritmo": o difícil fica no achado, não na redação |
| Ambientação repetitiva | 1, 2 | "Sem tique". Resolvido desde a sessão 3 |
| Dificuldade alta por reflexo | 4, 6 | `rolagens.md`, escala |

Ficaram de fora por terem aparecido uma vez só e não terem voltado: NPC respondendo a uma frase retórica que já tinha passado (sessão 1, "observar"); fala de NPC que soou como cobrança (sessão 5). Se voltarem, entram.

Saiu no mesmo dia: "sessão de puzzle pesado pede uma mais leve depois". Quem joga gosta de puzzle; a nota sobre cansaço nas avaliações era só pra observar se incomodaria de novo. Volta só se quem joga pedir.

## Incidentes por regra

| Regra | Entrou | O que aconteceu |
|---|---|---|
| Ponto de reação em toda fala de NPC | 2026-11-11 | Pedido de quem joga; o incidente não foi registrado. |
| Como descrever, paleta, primeira vez × de novo | 2026-11-11 e 12 | Pedido de quem joga; o incidente não foi registrado. |
| Sem tique | 2026-11-12 | O mesmo som de fundo voltava em toda cena. |
| Preparar não é fazer | 2026-11-12 | Quem joga disse que a personagem pegava coisas pra ir se lavar, e a narração já a levou até o rio. |
| Texto lido em cena vai pra nota na mesma resposta | 2026-11-12 | Uma lista de nomes lida num quadro de avisos se perdeu na compactação. |
| Releitura depois de compactação | 2026-11-12 | O resumo guardou o enredo e perdeu hábitos e a linha do tempo. |
| Sessão longa: avisar | 2026-11-12; "avisar cedo" em 2026-11-18 | Numa sessão que passou do ponto, os erros se acumularam no fim. |
| Maneirismo não se repete | 2026-11-12 | Sem incidente registrado. |
| 💡 na curiosidade da personagem | 2026-11-13 | Um murmúrio no escuro passou sem quem joga saber que podia rolar. |
| Dicas não diminuem sozinhas | 2026-11-13 | Quando as dicas rarearam, fizeram falta. |
| Fechamento sem gesto da personagem | 2026-11-13 | Pra fechar cena ou pular tempo, o mestre punha um gesto que quem joga não deu; a crítica se repetia de sessão pra sessão. |
| A conclusão é de quem joga | 2026-11-13 | Concluir pela personagem é a mesma perda de controle, em outra forma. Incidente não registrado. |
| Procurar onde não há nada não rola | 2026-11-13 | Um teste difícil num documento sem mais nada escondido deixou a personagem insegura sem razão. |
| Dificuldade pela escala do sistema | 2026-11-13 | Quase toda dificuldade saía no mesmo número alto, "muito difícil" no livro. Em 2026-11-16, uma dificuldade foi estimada pelo adjetivo e o livro dava outra. |
| Como cada NPC chama a personagem | 2026-11-13 | Sem incidente registrado. |
| O que a personagem aprendeu da facção, na íntegra | 2026-11-14 | Quem joga quer reler aulas e relatórios depois. |
| Testes de NPC contra a personagem | 2026-11-14 | O livro supõe que todo mundo rola; no solo, sem a regra, o resultado do NPC virava decisão do mestre. |
| Anunciar não é ir | 2026-11-16 | "Vou pro pátio, quem vem?" levou a personagem ao pátio antes de ela ver a resposta dos outros. |
| Imagens: momentos fixos de ler o módulo | 2026-11-16 | Lido só na hora de escrever o prompt, o módulo nunca lembrava de escrever um, e uma sessão inteira passou sem imagem. |
| Pedir o dado não é avançar | 2026-11-16 | Depois da rolagem pedida, um NPC agia ou falava, e quem joga perdia a vez de reagir ao resultado. Repetiu-se. |
| Mensagem só em OOC não move a cena | 2026-11-17 | Uma mensagem só fora do jogo ganhou narração junto com a resposta, apesar de o `AGENTS.md` já mandar não avançar. |
| Anotar o que quem joga conta da personagem | 2026-11-17 | Fatos do passado da personagem ditos só na conversa não iam pra ficha. |
| Quem sabe o quê, na releitura | 2026-11-18 | Numa sessão longa, NPCs souberam de um treino que a personagem nunca contou, de um horário que ela não disse e de um aviso que não ouviram; uma palavra de uma explicação fora do jogo foi parar na boca de um NPC. |
| Onde paramos, ao pé da letra (`/fim`) | 2026-11-18 | A nota da cena dizia só que um NPC "ia pro copo"; a abertura da sessão seguinte o pôs com o copo cheio, e no fim da anterior ele já tinha comido quase tudo. |
| Na dúvida sobre o passado, perguntar em OOC | 2026-11-18 | Pedido de quem joga: "até mestres humanos fazem isso". Antes, o mestre narrava no chute quando a nota não resolvia. Limite: o que um NPC sabe às escondidas nunca se pergunta, porque a pergunta entrega o segredo. |
| Bloco Agora e regras das notas de entidade (`references/notas.md`) | 2026-11-18 | A nota de um companheiro passou de 18 mil caracteres em seis sessões, com fatos vencidos escritos no presente, uma seção de relação parada na primeira sessão (o template mandava a mudança pro Histórico), "Quer" e "Missão pessoal" vazios, linhas no lugar errado e um fato que o NPC não podia saber (aconteceu numa cena em que ele não estava). Testado num rascunho e revisado por quem joga três vezes antes de entrar. |
| Quem disse o quê a quem, com os nomes (`references/notas.md`, `AGENTS.md`) | 2026-11-18 | A nota de uma NPC dizia que ela sabia de um aviso "(fulana contou)". Lia-se como se fulana tivesse contado a ela; na verdade fulana tinha avisado a personagem, que depois contou à NPC. Pedido de quem joga: as notas estavam ficando confusas. |
| O passado de um NPC tem data (guia, "Sem oráculo"; preparo, "Linha do tempo do passado"; template Segredo de entidade) | 2026-11-18 | O intervalo entre um momento do passado de um NPC e o sumiço de outro foi improvisado em duas falas, em sessões diferentes: "três ou quatro dias" e "duas semanas". O plano do companheiro fixava o que importava pra trama, mas não as datas. Quem joga cobrou que a história seja planejada, com o passado fixo e vários finais possíveis. |
