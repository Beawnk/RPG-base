# Notas de entidade

Leia ao criar a nota de um NPC (e de um companheiro, com o módulo ligado), de um lugar, item ou facção, ou a ficha de uma personagem de quem joga, no arquivista quando uma nota de entidade muda, na conferência do `/fim` e antes de montar o bloco Agora numa nota que ainda não tem. As regras fixas (nota pública só com o que a personagem sabe, arquivo de segredo de toda entidade) estão no `AGENTS.md`; aqui está como escrever e manter a nota pra ela continuar útil quando crescer.

Por quê: com o tempo, a nota de um NPC importante passa de dez mil caracteres. Relida inteira a cada cena, ela pesa; lida pela metade, esconde o fato que importava. E as seções que ninguém define direito acabam vazias, desatualizadas ou com coisa no lugar errado.

## O bloco Agora

Um bloco no topo da nota, logo abaixo da linha do essencial, com o que vale **hoje**. Ele não substitui o resto da nota, que continua inteiro embaixo. É o que o mestre relê a cada cena; o resto ele procura quando a cena toca um detalhe.

**Regras de base**
1. **Nada sai da nota.** O Agora é tirado do resto dela. Se os dois discordarem, vale o resto da nota (ou quem joga), e o Agora é corrigido.
2. **Só o que a personagem sabe**, porque a nota é pública. O lado oculto tem o próprio Agora, no arquivo de segredo (abaixo).

**As seções (NPC e companheiro)**
- **Onde e como está:** só o presente: o lugar, o estado físico e mental, o recurso do sistema que importa agora (ferido, abalado, sem munição).
- **O que fez há pouco:** pra contexto, o que ele fez nesta sessão antes da cena atual (ou na sessão que acabou), em ordem, com a hora da ficção. Só ações; uma fala, só com a hora e o lugar em que foi dita. A cada sessão nova, o que ficou velho sai: já está na nota da sessão.
- **Com a personagem:** a atitude (ou a aprovação, com o módulo de companheiros), como ele a chama, o momento que mais pesou entre os dois.
- **Em aberto entre os dois:** promessas, combinados, pedidos, dívidas. O que foi cumprido ou venceu sai do Agora.
- **O que ele sabe da personagem:** todo fato que ela contou ou que ele viu e que ainda pode aparecer numa fala dele. Não se resume em grupos ("sabe do passado dela"): é daqui que sai o erro de "quem sabe o quê". Só fica de fora o que perdeu a validade, que continua embaixo.
- **O que a personagem sabe dele:** primeiro o que ele quer e o que teme; depois família, trabalho, passado, culpas, mentiras em curso, fé, gostos que podem aparecer em cena, como ele gosta de ser chamado.
- **Coisas:** objetos dele ou com ele, e onde estão.

**Como escrever cada linha**
- **Uma linha por assunto.** Dois fatos sem relação não dividem linha, nem quando são da mesma sessão ou parecem ligados.
- **O motivo vai junto**, quando foi dito ("estuda as lendas porque o avô contava").
- **Como ele soube**, quando não é óbvio que ela contou: viu, ouviu de outra pessoa, estava lá.
- **Quem disse o quê a quem, com os nomes.** Todo fato contado diz quem contou e pra quem, sem sujeito escondido nem parêntese que sirva pra duas leituras. Nome em vez de pronome sempre que a linha tiver mais de uma pessoa ("a regra é da personagem", não "a regra é dela"). Vale pra toda nota, não só pro Agora.
- **A sessão no fim da linha** (s4, s7), pra achar o detalhe embaixo.
- **Presente só em "Onde e como está".** Uma ação de antes do lado de uma fala faz a fala parecer dita agora.

> Errado (Onde e como está): "No portão, de vigia. Passou a noite em claro: 'não aguento nem ficar de pé'." (lê como se ele estivesse exausto nesta cena)
> Certo: Onde e como está: "No portão, de vigia, atento." · O que fez há pouco: "de madrugada, ronda no cais a noite inteira; dormiu de manhã (s7)".

> Errado (O que ele sabe da personagem): "sabe do passado dela, que ela fala com a curandeira e que pediu uma leitura" (agrupado; dois assuntos numa linha; e a leitura foi a sós, ele não estava lá)
> Errado: "sabe do degrau quebrado da escada (a cozinheira contou)" (contou a quem? a ele, ou à personagem, que depois contou a ele?)
> Certo: "sabe do degrau quebrado: a cozinheira avisou a personagem, e a personagem contou a ele (s2)"

> Certo: "a irmã dela morreu no incêndio do moinho (ela contou, s3)" · "viu ela levar a curandeira pra longe dele, depois da briga no mercado (s4)"

## O resto da nota

- **Linha do essencial:** uma ou duas linhas de quem ele é e por que importa. Muda pouco.
- **Aparência; Personalidade e voz:** como no template. "Como chama a personagem" e "como gosta de ser chamado" ficam aqui por inteiro; o Agora repete o que vale hoje.
- **O que sabe:** só o que ele aprendeu. Antes de escrever uma linha, confira **quem estava na cena**: se ele não estava, não sabe, por mais perto que tenha sido. As linhas seguem a sequência das sessões, a nova embaixo; toda linha com a sessão.
- **Dito por ele:** só o que ele disse ou mostrou de si (é o que a personagem aprendeu dele). Fato que ele aprendeu vai pra "O que sabe".
- **Vencido não se apaga, se marca** (em toda nota de entidade, não só de NPC). Promessa cumprida, horário que passou, fato que mudou: no fim da linha, "(cumprido, sN)", "(passou)" ou "(mudou: ver sN)". Assim uma releitura rápida não lê o vencido como presente. Marca-se no arquivista, na cena em que venceu, e confere-se no `/fim`.
- **Missão pessoal** (módulo de companheiros): `Mestre/references/modulos/companheiros.md`, "Registro e `/fim`".
- **Histórico:** o registro das mudanças (atitude, aprovação, faixa, status), com o motivo e a sessão. O estado de hoje fica no Agora.

## O Agora do lado oculto

O arquivo de segredo da entidade ganha um bloco "Agora (lado do mestre)" no topo, curto, com o que só o mestre sabe e vale hoje:
- **Fazendo agora, fora de cena**, e o **próximo passo** se ninguém interferir;
- **o que ele esconde agora** e o que pode fazer isso vazar;
- **o que ele sabe que a personagem não sabe que ele sabe** (e como soube);
- com o módulo de companheiros: o que aprova e reprova hoje, o próximo valor mínimo e onde está o plano dele.

Quem joga não revisa esse bloco, porque ele é segredo. Ao relatar que o montou, diga só "anotei nos segredos".

## Quando montar e atualizar

- **Nota nova:** nasce com o Agora (o template já traz), preenchido com o pouco que se sabe.
- **Nota que ainda não tem** (NPC, lugar, item ou facção): monte antes de a entidade entrar em cena ou ser citada. Não use só a nota dela: leia também as notas das sessões em que ela apareceu e as conversas de chat com ela. Fato que estiver lá e faltar na nota entra no Agora **e** na seção certa da nota. Aproveite pra marcar os vencidos e mover o que estiver no lugar errado, sem apagar nada.
- **Arquivista (fim de cena):** pra cada NPC que estava na cena, a linha nova embaixo, o Agora (o público e o do segredo) e os vencidos marcados; pra cada lugar, item ou facção que mudou na cena, o Agora dele.
- **`/fim`:** pra cada entidade que apareceu na sessão, confira o Agora inteiro contra a nota, marque os vencidos e atualize a linha "Atualizado" no topo do bloco.

## Como o mestre usa

- **Na releitura por cena:** como manda o guia, "Releitura durante a sessão".
- **A cena toca um detalhe** (um objeto, uma conversa antiga, um combinado velho): procure na nota inteira e na nota da sessão.
- **Não achou:** a regra do guia, "Na dúvida sobre o passado, confira; se a nota não resolve, pergunte".
- **Antes de cada fala de NPC:** a lista "O que ele sabe da personagem" é a resposta rápida pra "de onde ele sabe isso?". Se não está lá nem embaixo, ele não sabe.

## Outras entidades

Lugar, item e facção também têm o Agora, com a mesma regra: nota nova nasce com ele (o template traz), e nota que ainda não tem ganha o Agora antes de a entidade entrar em cena ou ser citada. Seções, pra adaptar:
- **Lugar:** como está agora (quem está, o que mudou, perigo à vista); o que a personagem deixou ali; em aberto ali; o que ela sabe dele que importa.
- **Item:** onde está e com quem; em que estado; o que a personagem sabe dele.
- **Facção:** a posição dela com a personagem; quem a personagem conhece lá dentro; em aberto; o que ela sabe dela.
- **Personagem de quem joga** (a ficha): o Agora olha pra fora, pro que o mestre esquece (quem joga já sabe tudo isso). Nasce com a ficha (o template traz) e é atualizado no arquivista e no `/fim`, como os outros. Seções:
  - **Onde e como está:** só o presente: lugar e hora, com quem, o que veste (se uma nota diz), os recursos do sistema e quando cada um volta.
  - **O que fez há pouco:** as ações dela no dia da ficção, da sessão anterior em diante, com a hora. Só ações.
  - **Coisas e onde estão:** por lugar: com ela, onde dorme, guardado com alguém, em casa, no celular ou em arquivos. Coisa sem lugar registrado não se inventa: pergunte.
  - **Em aberto:** só o que tem hora ou pessoa: combinados, pedidos feitos e recebidos, mensagens sem resposta. Promessa sem prazo, mistério e missão ficam em `Linhas abertas.md`.
  - **Laços agora:** uma linha por pessoa que importa, com o estado de hoje (como a chama, a última vez que se viram); o resto está no Agora da nota dela.
  - **Quem sabe o quê dela:** pra cada fato sensível da vida dela (as marcas, as perdas, o que fez de ilegal, as mentiras que conta, a vida amorosa), quem sabe e como soube (contou, viu, ouviu de outra pessoa, estava lá), com a sessão; e "ninguém", quando uma nota diz. É a lista "O que ele sabe da personagem" das notas de NPC ao contrário: serve pra cena com várias pessoas e pra NPC novo. Se as duas divergirem, confira na nota da sessão. O que um NPC sabe dela sem ela saber não entra: é segredo.
  - Teoria e conclusão dela não entram: são de quem joga (ficam no mural, se o módulo estiver ligado).
