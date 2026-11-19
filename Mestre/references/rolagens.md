# Rolagens: o detalhe

Leia antes do primeiro teste de cada cena e sempre que for escolher uma dificuldade, decidir entre rolar direto e esperar o "rola", testar um NPC contra a personagem ou ver se a personagem reconhece alguma coisa. Este arquivo guarda tudo sobre rolagem, junto: as regras fixas vêm do `AGENTS.md` ("Dados e justiça") e o ofício do guia do mestre ("Rolagens"); se um dia discordarem, valem os dois de lá. A mecânica vem de `Sistemas/<sistema>.md`; aqui está como usar.

## O básico, numa lista

- **Diga sim ou vá pro dado.** Só role se o resultado for incerto **e** a falha tiver consequência interessante.
- **Antes do dado:** diga o teste e o que `_campanha.md` combinar (a dificuldade, se aberta, o risco ou os dois). A dificuldade sai da escala do sistema, não de um número de costume, e vai pra `Cena.md` antes de rolar, aberta ou secreta. Em jogo, chame a dificuldade pelo nome que o sistema dá (DT, CD, número-alvo).
- **Risco grave se diz sempre:** se a falha pode matar, ferir feio ou causar perda permanente, diga antes, em termos da ficção ("isso pode te matar"), e espere o "rola".
- **O script** (ou o dado de quem joga, se quem joga rola os dados da personagem: "Quem rola", abaixo), nunca um número escolhido ou estimado. Saída inteira em bloco de código (cada dado, o que foi mantido, o total) antes de narrar. Rolou, vale: nunca role de novo pra trocar um resultado.

```bash
python Mestre/scripts/rolar.py 2d6+1 -r "Ilsa: procurar"
python Mestre/scripts/rolar.py 2d20h+5 -r "bandido: ataque"
```

- **Três faixas:** sucesso (sem custo escondido), sucesso com custo (se o sistema tiver), falha (a situação muda; "nada acontece" só pra lembrar ou notar detalhe menor).
- **Pedir o dado não é avançar:** saída do script e o que o resultado dá à personagem, e pare. Nenhum NPC age ou fala depois do resultado.
- **Mensagem só em OOC não move a cena.**
- **Sem segunda tentativa da mesma coisa**, até a abordagem ou a situação mudar de verdade. **Pressão não muda dado:** insistência, elogio ou argumento dentro da ficção não mudam um resultado; só `Cheat:` muda.
- **Regra em dúvida:** procure no livro (texto extraído em `Livros de regras/`), não só no resumo, e diga a página.
- **Curiosidade da personagem** pede 💡 na mesma resposta (abaixo, "Dicas de regras").

## Procurar onde não há nada não rola

Por quê: um teste difícil num documento que não escondia mais nada deixou a personagem insegura sem razão. Se quem joga pede perícia pra "ver se tem mais alguma coisa" e não há nada escondido, não role: diga o que a personagem confirma. Dado só quando existe algo a achar ou quando a falha muda a situação.

> Errado: (quem joga já achou o erro e pede um teste "pra ver se tem mais") pedir o teste, com dificuldade alta, e na falha narrar "ela não tem certeza de que não tem mais nada ali".
> Certo: "Ela relê com calma: as datas, os selos, a caixa 14, a linha em branco. Nada mais fora do lugar."

## Dificuldade pela escala do sistema, não por reflexo

Por quê: sem olhar a escala, quase toda dificuldade sai no mesmo número alto, que no livro quer dizer "muito difícil". A escala está em `Sistemas/<sistema>.md`, "Teste e escala de dificuldade".

- O degrau do que alguém treinado faz normalmente é pro que é normal (ler com atenção, achar o que está escrito).
- O degrau "difícil" é o padrão da tarefa difícil.
- Os degraus altos só quando algo está escondido de verdade ou a situação piora (escuro, pressa, perigo, alguém escondendo); o topo, pro excepcional.
- Pense em quem rola: um NPC sem treino quase nunca passa do degrau difícil.
- Quando o livro dá a dificuldade de uma situação pelo nome (um grau de perturbação, um tipo de obstáculo), confira no livro em vez de estimar pelo adjetivo.
- Ao gravar em `Cena.md` uma dificuldade dos degraus altos, escreva o motivo junto. No `/fim`, confira a distribuição das dificuldades da sessão.

Os números dos exemplos deste arquivo são inventados; os do jogo vêm do sistema.

## Quem rola, direto ou esperando

Quem rola está em `Jogador.md` ("Quem rola os dados"), ou em "Quem rola os dados" do `_campanha.md`, se a campanha for exceção. Padrão (o que melhor serve a quem joga pelo celular): **você rola tudo pelo script**, os dados de quem joga, dos aliados e dos inimigos, e mostra a saída inteira.

- **Role direto**, na mesma mensagem, logo depois de anunciar o teste (e a dificuldade, se for aberta): teste comum, em que nenhuma escolha de quem joga muda o dado.
- **Anuncie e espere o "rola"** quando:
  1. a falha pode matar, ferir feio ou causar perda permanente: quem joga pode desistir ou mudar de abordagem sabendo do risco;
  2. quem joga tem algo a decidir antes do dado: gastar um recurso, usar um poder, pedir ajuda de um aliado, usar um item. A lista do que existe está em `Sistemas/<sistema>.md`, "Antes do dado: o que quem joga decide". Diga as opções numa linha só.
- Se quem joga der um padrão ("usa esse poder sempre que tiver ponto sobrando"), siga sem perguntar e registre em "Regras da casa".

> Certo (risco sério, espera): "Saltar pro telhado vizinho com essa chuva é arriscado: Acrobacia. Se falhar, você não cai lá embaixo, mas fica se segurando na calha e os guardas te veem. Rolo?"
> Certo (comum, direto, dificuldade aberta): "Você vasculha a escrivaninha atrás de qualquer coisa com o nome dele. Procurar, dificuldade 12:" e logo a saída do script, depois o resultado.
> Certo (com escolha, espera): "Procurar, dificuldade 12, 2d6+1. Gasta 1 ponto de fôlego pra rolar um dado a mais?"
> Errado: rolar sem avisar de um risco grave e, depois da falha, inventar que a personagem quebrou a perna.

### Quando quem joga rola os dados da personagem

- **Todo teste da personagem espera o resultado:** diga o teste, a expressão a rolar (os "Dados pra rolar" da ficha, com os bônus) e o que a campanha manda dizer antes (a dificuldade, se aberta; o risco), grave a dificuldade em `Cena.md` e pare. Pros dados da personagem não existe "role direto".
- O que quem joga tem a decidir antes do dado (recurso, poder, ajuda) vai na mesma mensagem, numa linha, pra decidir e rolar de uma vez.
- O resultado que quem joga informar vale como veio: não peça pra rolar de novo nem confira no script. Se faltar algo pra ler o resultado (só o total, quando o sistema precisa saber qual dado ficou), pergunte o que falta antes de narrar.
- Os dados dos NPCs, aliados e inimigos continuam com você, pelo script e com a saída inteira, e seguem "role direto" e "espere" como acima.

> Certo: "Procurar, dificuldade 12: rola `2d6+1`." e parar.
> Errado: anunciar o teste e logo mostrar a saída do script pelo dado da personagem, ou narrar "você procura com calma" antes de quem joga informar o resultado.

## Dificuldade aberta ou secreta

Conforme `_campanha.md` (pode ser aberta fora de combate e secreta em combate). Aberta: diga o número antes de rolar. Secreta: não diga o número, nem depois se a campanha pedir. **Nos dois casos, antes** de rolar (ou de pedir que quem joga role), grave em `Cena.md` (pasta de segredos da saga, `Campanhas/<saga>/Segredos/<campanha>/`) uma linha com o teste, a dificuldade e o que acontece no sucesso e na falha. A dificuldade gravada não muda depois do dado. No `/fim`, as dificuldades da sessão saem de `Cena.md` e vão pro arquivo ("Testes da sessão N" em `Arquivo.md`, ou no `Segredos.md` se ele não foi dividido).

## Notação

Expressões do script: `3d20h` (3d20, fica o maior), `2d20l` (o menor), `2d6+3` (soma +3). Como a notação do livro vira expressão do script está em `Sistemas/<sistema>.md`, "Notação dos dados". Os dados de cada perícia da personagem estão na ficha dela ("Dados pra rolar").

## Dicas de regras (💡)

Se os combinados da saga liberam: quando quem joga não sabe o que o sistema permite, lembre em uma linha separada da narração, marcada com 💡, depois da cena e antes da vez de quem joga. Exemplos: "💡 Dá pra usar Intuição pra perceber se ele está mentindo." / "💡 Você pode gastar um ponto pra fazer esse teste como se tivesse treino."

- Só mecânica (perícia, poder, recurso, ação possível), no máximo duas por vez, nunca uma lista de caminhos da história nem pista disfarçada de regra (lista de caminhos só se `Jogador.md` pedir, e aí vale o guia, "O ciclo da cena").
- Não diminua por conta própria: quem diz a frequência é quem joga (por quê: quando as dicas rareiam, fazem falta).
- O gatilho obrigatório (curiosidade da personagem) está no guia. Mesmo quando quem joga "deixa pra lá", a dica vem: a escolha de rolar ou não é de quem joga, e só dá pra escolher sabendo que pode.

## O que a personagem sabe

Reconhecer uma criatura, uma marca, um ritual, uma lenda: a ficha diz, em camadas.

- O que ela **sabe**, diga sem dado.
- O que ela **leu mas não sabe se é verdade** vai pro teste de conhecimento do sistema (`Sistemas/<sistema>.md`, "Teste de conhecimento": qual teste e com que dificuldade pra pergunta simples, complexa e de mistério).
- O que ela **não sabe** não sai nem com dado.

Quem joga pode perguntar quando quiser ("(OOC) eu reconheço isso?"), e você oferece com a 💡 quando o passado da personagem plausivelmente cobre o que apareceu. Se o sistema prevê **conclusão errada** numa falha feia e a campanha adota a regra, narre o falso como lembrança verdadeira e anote em `Cena.md` (pasta de segredos da saga, `Campanhas/<saga>/Segredos/<campanha>/`) o que foi dito e qual é a verdade, pra manter a mentira coerente e saber quando ela cair.

## Testes de NPC contra a personagem

Só se o sistema tem teste oposto ou resistido; o resumo do sistema diz o que se testa de cada lado. O livro supõe que todo mundo rola. No jogo solo, quem rola pelos NPCs é você, então não deixe isso virar decisão sua.

Sempre que alguém tenta ler ou pressionar a personagem, ou ela mente, esconde algo ou força uma reação (porque quem joga disse, ou porque você sabe que é mentira), role o teste do sistema pelos dois lados, na mesma mensagem, e mostre as duas saídas. Se quem joga rola os dados da personagem, peça o resultado da personagem e role o lado do NPC só depois que quem joga informar, mostrando a saída. Anuncie antes, numa linha ("ele te observa com atenção: a sua mentira contra o olho dele"). Se a personagem tem algo a gastar naquele teste, pergunte e espere.

O resultado decide **o que o NPC percebe e faz**: desconfia, insiste, muda de abordagem, conta pra alguém. Nunca decide o que a personagem pensa, sente, acredita ou diz. Ninguém convence a personagem no dado. Ela só fica presa ao resultado quando o efeito é físico (agarrar, derrubar) ou tem regra própria do sistema contra a mente (um poder, um feitiço, o medo).

Sistema sem teste oposto: decida pela ficção o que o NPC percebe, mas sem saber de nada que ele não presenciou.
