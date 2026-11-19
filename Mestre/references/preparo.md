# Preparo: sistema, campanha, sessão e fechamento

Leia ao resumir um sistema novo, ao criar uma campanha, ao preparar o início de uma sessão ou ao fechar um arco. O `/fim` tem arquivo próprio: `Mestre/references/fim.md`.

Os passos com a marca **(módulo)** só existem se o módulo está ligado em "Módulos ligados" do `_campanha.md`. Desligado, pule o passo inteiro.

## Resumir um sistema novo

Isto é modo criação. O jogo usa `Sistemas/<sistema>.md`, um resumo, e não o livro inteiro.

1. Quem joga põe o livro em `Livros de regras/` (fora do git). Sem livro, dita as regras ou aponta uma referência aberta.
2. Copie `Sistemas/_modelo.md` como `Sistemas/<sistema>.md` e preencha todas as seções a partir do livro, com as suas palavras (sem copiar trechos), citando as páginas. Seção que o sistema não tem fica como "não se aplica". Os títulos que o guia e as referências dele consultam pelo nome não mudam: "Notação dos dados", "Teste e escala de dificuldade", "Antes do dado: o que quem joga decide", "Teste de conhecimento", "Ficha", "Combate", "Descanso e recuperação", "Jogando solo", "Pra mestrar" e "Ajustes em teste".
3. Regra ambígua ou interpretação sua: pergunte antes de fixar. Em "Jogando solo", proponha o que muda com uma personagem só e deixe quem joga decidir.
4. Mostre o resumo, ajuste, e só então use em jogo. O que não funcionar na mesa vira entrada em "Ajustes em teste" (pergunta do `/fim`).
5. Se quem joga quiser ficha visual pro sistema, isso é um script à parte, feito em modo criação. Sem script, a ficha é a nota da personagem.

## Criar uma campanha (sessão zero)

Isto é modo criação: você é colaborador, não mestre. Proponha, compare, deixe quem joga decidir, registre só o que for aprovado.

0. **Saga nova ou continuação?** Toda campanha mora numa saga (`Campanhas/<saga>/`), mesmo que seja a única.
   - **Saga nova:** crie `_saga.md` (template Saga) e a pasta de segredos da saga, `Campanhas/<saga>/Segredos/`, com o `Segredos da saga.md` dentro, junto com a campanha. A apresentação do mundo do passo 1 vira a parte "O mundo" do `_saga.md`.
   - **Continuação:** leia `_saga.md`, `Segredos da saga.md` e o fechamento da campanha anterior. Combine com quem joga, como colaborador: quanto tempo passou na ficção; se volta a mesma personagem ou nasce outra (ou as duas convivem); o que mudou no mundo ("Entre campanhas"). Ameaças e vilão novos, ligados ou não à verdade da saga. Com que ficha uma personagem nova começa ao lado de veteranos se decide aqui.
1. **Premissa, tom e sistema.** Uma ou duas linhas de premissa, inspirações, o sistema (`Sistemas/<sistema>.md`; se o resumo ainda não existe, faça antes "Resumir um sistema novo").
   - **Apresente o mundo sem spoiler** antes da personagem: onde e quando, o tom, o que qualquer pessoa ali sabe, que tipo de personagem combina e como ela se liga à premissa. Curto, como um guia do jogador. Nada de ameaça, vilão ou reviravolta. Quem joga cria a personagem dentro desse quadro, e você costura o mundo em volta dela (passo 3).
2. **Combinados**, registrados em `_campanha.md`:
   - Letalidade: a personagem pode morrer? Existe regra de beira da morte? (Se existir, ela vai pra "Regras da casa" agora, não na hora da morte.)
   - Falha pode virar captura, dívida, perda permanente?
   - Linhas (o que nunca aparece) e véus (o que acontece fora de cena). Comece pelos limites de `Jogador.md` e pergunte se esta campanha tem outros.
   - Ganchos explícitos ou sutis.
   - Se a dificuldade é aberta ou secreta. Quem rola os dados vem de `Jogador.md` ("Quem rola os dados"): pergunte só se esta campanha deve ser diferente, e nesse caso grave a exceção e o porquê em "Quem rola os dados" do `_campanha.md`.
   - **Módulos:** quais ligar nesta campanha (companheiros, chat, imagens, mural). Explique cada um em uma linha, com o que custa, e registre a escolha em "Módulos ligados". O padrão é desligado.
3. **Personagem.** Quem joga cria. Você pergunta, não inventa passado, família ou laços. Peça:
   - o que a personagem quer (1 ou 2 objetivos pessoais)
   - um **kicker**: algo que acabou de acontecer e obriga a personagem a agir
   - pessoas e lugares que importam pra ela

   Depois, costure: o passado, o kicker e as pessoas dela viram NPCs, lugares e ganchos nas ameaças. Detalhe importante que não foi dado, pergunte.
4. **Perguntas da campanha.** 1 a 3 perguntas que a história vai responder e que você genuinamente não sabe a resposta ("A Ilsa vai perdoar o irmão?", "A cidade cai antes do inverno?"). Ficam em `_campanha.md`, à vista de quem joga. Os finais possíveis são as respostas.
5. **Ameaças.** Monte em `Segredos.md` (formato abaixo). Ele nasce, com o `Cena.md`, na pasta da campanha dentro dos segredos da saga: `Campanhas/<saga>/Segredos/<campanha>/`. Mostre a quem joga só quem é e o que quer, no nível de premissa. Presságios e desfechos ficam secretos, a menos que quem joga peça pra ver.
6. **Vilão e reviravoltas.** Planeje desde o começo, em `Segredos.md`:
   - **O vilão da campanha** é o motor da ameaça de campanha. Os presságios dela são a construção dele: primeiro só rastros e consequências, depois capangas e boatos, depois contato direto, por fim o confronto. Quem joga deve sentir a presença dele crescer antes de encontrá-lo.
   - **1 ou 2 reviravoltas**: verdades escondidas que mudam o sentido do que a personagem já viveu (o aliado que trabalha pro vilão, o vilão que tem razão em parte, a missão que era outra coisa). Cada uma recebe pistas plantadas bem antes (regra das três pistas), pra que a revelação surpreenda e, olhando pra trás, faça sentido.
   - O que fica fixo é a **verdade**, não o desfecho. Quando e como quem joga descobre, e o que faz com isso, sai do jogo. Se descobrir cedo, a reviravolta vira informação pra usar, não algo a esconder à força.
   - Reviravolta só vale se estava escrita antes. Inventar uma na hora pra salvar o vilão é railroad (ver `Mestre/references/imprevistos.md`).
   - **Pensando na continuação.** A ameaça de campanha se resolve dentro da campanha, com fechamento que dá pra sentir. O que é maior que ela vai em `Segredos da saga.md`: a verdade da saga, que cada campanha mostra só um pedaço, e 1 ou 2 ganchos de continuação plantados ao longo do jogo. Qualquer final possível (vitória, vitória com custo, derrota, morte da personagem) precisa deixar um mundo onde caiba uma próxima campanha. Gancho de continuação não é cliffhanger obrigatório: a campanha pode terminar em paz e a próxima começar de uma semente plantada.
7. **(módulo) Elenco de companheiros.** Depois da personagem e do vilão, porque cada companheiro se liga aos dois. Como planejar, quantos, a escala de aprovação e onde o plano fica: `Mestre/references/modulos/companheiros.md`, "Planejar o elenco".
8. **Abertura.** Combine com quem joga o clima do começo. Pode abrir com ação e tensão ou com calmaria, mas sempre com uma situação concreta (um lugar, um momento, algo acontecendo ou pra explorar). Logo no começo, ou logo depois da tensão inicial, garanta um momento pra digerir o mundo e explorar. Exemplo: Baldur's Gate 3 abre na tensão do nautiloide e, quando ele cai, vem a calmaria da praia, onde a personagem encontra os primeiros companheiros.
9. **Tamanho e fôlego.** A campanha pode ser longa, até gigante. O que importa é ser divertida de jogar sem grupo. Pra isso:
   - Organize em **arcos**: a ameaça de campanha é o fio longo, e cada ameaça de aventura é um arco com começo, meio e um fechamento que dá pra sentir (vitória, perda, revelação).
   - Cada arco termina mudando alguma coisa no mundo ou na personagem. Isso dá sensação de progresso numa história sem fim marcado.
   - Varie o tipo de arco (mistério, viagem, intriga, sobrevivência, ação) pra campanha longa não cansar.
   - Não existe final roteirizado, mas existe direção planejada desde o começo: o vilão em construção e as reviravoltas (acima). A campanha acaba quando quem joga quiser, ou quando a ameaça de campanha se resolver e não houver vontade de outra.

## Ameaças (frentes)

Use **uma ameaça de campanha** (o arco grande, lento) e **no máximo uma ou duas de aventura** ativas ao mesmo tempo. Com uma personagem só, mais que isso vira bagunça: ela não pode se dividir.

Formato em `Segredos.md`, seção "Ameaças":

```markdown
### Nome da ameaça
- Quem ou o quê: [[NPC]] ou [[Facção]] por trás
- Quer: o impulso, em uma frase
- Presságios:
  - [ ] 1. primeiro passo visível
  - [ ] 2. ...
  - [ ] 3. ...
- Se ninguém interferir: o desfecho
- Pergunta em jogo: o que a história vai descobrir sobre isso
- Relógio: Nome do obstáculo [0/6]
```

- Ameaça de aventura: 1 a 3 presságios. Ameaça de campanha: 3 a 5, mais espaçados.
- Presságio é um passo **visível no mundo**, não um pensamento do vilão. Quando acontece em jogo, marque `[x]` e anote a sessão.
- Relógio (opcional, quando o avanço é gradual): 4 segmentos pra algo rápido, 6 normal, 8 longo. Nomeie pelo obstáculo ("A Torre"), não pelo método ("Escalar a Torre"). Falhas e sucessos com custo enchem o relógio. Relógio cheio = o presságio ou desfecho acontece.
- Os desfechos possíveis de cada ameaça: (a) acontece, (b) a personagem impede, (c) a personagem desvia ou transforma, (d) a personagem se alia. Pense nos quatro. Não escolha.
- Ameaça resolvida sai da lista ativa. Outra pode surgir das consequências.

## Pistas e segredos

**Regra das três pistas.** Pra cada conclusão que quem joga precisa tirar pra história andar, deixe pelo menos três pistas, em formas e lugares diferentes (um objeto, uma conversa, um boato, um padrão). Uma vai passar batida, outra vai ser ignorada e a terceira vai ser mal interpretada. Isso é normal.

Em `Segredos.md`, seção "Pistas planejadas":

```markdown
### Quem matou o cobrador
- [ ] Recibo rasgado com a letra da prefeita
- [x] O cachorro do morto late pra ela (sessão 3)
- [ ] A filha do cobrador viu a carruagem
```

- A conclusão só conta quando quem joga declara ou age com base nela, não quando você acha que já foi entendida.
- Se as pistas estão sendo perdidas, acrescente outras. Nunca entregue a resposta.
- Abordagem esperta que você não previu também encontra pista.
- Evite pista falsa de propósito: quem joga já cria suspeitos por conta própria. Pista falsa é a que o mestre põe só pra despistar, sem nada no mundo por trás: puxado o fio, ele morre ou exige explicação inventada na hora. Duas coisas não são pista falsa e podem entrar:
  - **suspeito ambíguo:** fatos verdadeiros que fazem alguém parecer culpado (brigou com a vítima, estava perto, não tem álibi), cada um com uma causa no mundo que a investigação revela e que acaba por eliminá-lo;
  - **armação de alguém do mundo:** o culpado (ou outro NPC) planta uma pista pra incriminar alguém. Vale se tiver autor, motivo e rastro: quem fez, por quê, e as pistas que levam até essa pessoa (de onde veio o objeto, quem tinha acesso, o detalhe que não bate). Grave nos segredos junto com a pista. Engana sobre quem foi incriminado e diz a verdade sobre quem armou.

**Linha do tempo do passado.** Todo companheiro e todo NPC ligado a um mistério ganha, no arquivo de segredo dele, uma linha do tempo com data (ou "uns tantos dias antes de X") de cada fato do passado que pode aparecer numa fala: quando conheceu quem, quando aconteceu o que o marcou, em que ordem. A trama continua aberta, com vários finais possíveis; o passado é que fica fixo, porque não muda. Feita no preparo, antes de o NPC entrar em jogo; o que for decidido em cena entra nela na mesma resposta.

**Segredos soltos.** Mantenha alguns segredos e pistas sem lugar fixo (cerca de 5 a 10 por arco). Durante o jogo, entregue cada um onde a personagem estiver, por uma fonte plausível pro lugar. Isso é informação flutuando, não escolha: passa no teste do railroad.

Quando um segredo for descoberto, siga o `AGENTS.md` (passa pra nota pública, marca como revelado). Se o segredo estava no arquivo de segredo de uma entidade, mova o fato pra nota pública dela.

## Preparar o início de uma sessão

Depois do protocolo de início do `AGENTS.md`, antes do recap (é preparo mental; só vira nota se algo novo for decidido):

0. Se a última nota de `Sessões/` tem "Avaliação de quem joga", releia as notas, os porquês e "O que o mestre leva pra próxima". É o que corrigir nesta sessão. Releia também `Jogador.md`: ritmo, limites e por onde a pessoa joga hoje.
1. Releia as ameaças e relógios em `Segredos.md`. Qual presságio está mais perto? Releia `Cena.md` (o lado oculto da cena em que a sessão parou). Se o `Segredos.md` foi dividido, leia também `Agora.md` (o mundo depois da última sessão e o que está preparado) e abra o plano de cada companheiro e de cada missão que deve aparecer hoje. Abra também o arquivo de segredo (`Entidades/`) de quem deve aparecer. O resto da pasta fica fechado. NPC, lugar, item ou facção que deve aparecer e ainda não tem o bloco Agora: monte agora (`Mestre/references/notas.md`).
   - **(módulo) Chat:** como manda `Mestre/references/modulos/chat.md`, "No início da sessão".
2. Escolha 3 a 5 pistas ou segredos que podem aparecer nesta sessão, sem prender a lugar. Inclua, quando couber, uma pista de reviravolta ou um sinal do vilão. Se `Jogador.md` pede puzzles e a sessão comporta, veja se uma dessas pistas pode vir como puzzle, montado como manda `Mestre/references/generos/investigação.md` (resposta gravada nos segredos antes).
3. Escolha a **abertura**: retome exatamente de onde parou. Se parou na ação, abra na ação; se parou num respiro, pode abrir com calma. Sempre com uma situação concreta, nunca um "o que você quer fazer hoje?" no vazio.
4. Pense em 2 ou 3 cenas possíveis. São possibilidades, não roteiro: se nenhuma acontecer, tudo bem.
5. **(módulo) Mural:** leia o mural como manda `Mestre/references/modulos/mural.md`, "No início da sessão".
6. **Paleta sensorial.** Pra cada lugar que provavelmente aparece na sessão, preencha a seção "Sentidos" da nota dele em partes: **sempre ali** (2 ou 3 sinais que não mudam: a luz, um cheiro, uma textura ou temperatura, o detalhe que só o lugar tem), **acontece às vezes** (1 ou 2 sons ou eventos que vêm e vão; cada um sai no máximo uma vez por sessão), **dá pra mexer** (uma ou duas coisas que convidam a personagem a agir) e, em lugar de terror, **o detalhe errado** (o familiar entortado). Lugar sem nota ainda: anote a paleta no preparo dos segredos (`Agora.md`, se o `Segredos.md` foi dividido; senão, o próprio `Segredos.md`) e passe pra nota quando o lugar entrar em jogo. NPCs e ameaças recorrentes ganham uma **assinatura sensorial** (o cachimbo do Dario; pra uma ameaça, um cheiro, um som ou uma sensação que só ela traz), que volta quando eles aparecem, pra quem joga reconhecer: no máximo uma vez por cena, não a cada fala. Isso é material, não roteiro: use na hora com a regra de descrição do guia, sem recitar a lista.

## Fechar um arco ou a campanha

Quando uma ameaça se resolve, de qualquer jeito:

1. Registre o desfecho na nota da sessão e marque a ameaça como resolvida em `Segredos.md`.
2. Mostre as consequências no mundo: quem ganhou, quem perdeu, quem quer vingança, quem ocupa o vazio.
3. Se era a ameaça da campanha: algumas sessões antes do fim provável, pergunte em `(OOC)` quais linhas quem joga quer ver fechadas. No fim, proponha um epílogo ("onde ela está um ano depois?") e pergunte se a campanha termina ou continua com uma nova ameaça.
4. **Fechar a campanha na saga.** Quando a campanha termina:
   - `_campanha.md`: `status: encerrada` e o desfecho em poucas linhas. A pasta vira cânone: daqui em diante só leitura.
   - `_saga.md`: desfecho na lista de campanhas, linha do tempo, e o elenco com o status de cada um (a personagem: viva, morta, aposentada ou o que o sistema previr, com o resumo da ficha ao fim; companheiros, se o módulo está ligado: status e aprovação ao fim).
   - `Segredos da saga.md`: marque o que a campanha deixou ver da verdade da saga, os ganchos plantados, e preencha "Entre campanhas" (o que o mundo e os NPCs fazem no intervalo).
   - Linhas abertas que sobram viram ganchos possíveis, não dívida: a próxima campanha escolhe quais puxar.
   - Pergunte em `(OOC)` se quem joga quer uma continuação agora, depois, ou uma saga nova.
