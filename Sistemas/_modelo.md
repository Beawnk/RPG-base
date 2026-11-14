---
tipo: sistema
sistema: <Nome do sistema>
edicao: <edição, versão do livro, editora e ano>
livro: Livros de regras/<arquivo>
---
# <Nome do sistema>

<!-- Modelo do resumo de um sistema. Copie como Sistemas/<Nome do sistema>.md e preencha a partir do livro em "Livros de regras/". Os títulos com a marca (guia) são consultados pelo guia do mestre pelo nome: não renomeie. Seção que o sistema não tem: escreva "não se aplica" em vez de apagar. Apague estes comentários e as linhas de instrução ao preencher. -->

> Resumo de jogo, escrito com as palavras do mestre a partir do livro. Serve pra mestrar sem o PDF aberto. Pra detalhe de um poder, item ou criatura, o livro está em `Livros de regras/` (fora do git); as páginas citadas são as impressas no livro.

Premissa em duas ou três linhas: quem são as personagens, o que fazem, o tom do jogo.

## Notação dos dados
<!-- (guia) -->
- Como o livro escreve as rolagens e como isso vira expressão do script `rolar.py` (ex.: "vantagem" = `2d20h`; "soma de dois dados mais o bônus" = `2d6+3`).
- Abreviações que o resumo usa (DT, vida, recursos) e o que cada uma quer dizer.

## Teste e escala de dificuldade
<!-- (guia) -->
- O passo a passo de um teste: o que se rola, o que se soma, contra o quê.
- **Escala de dificuldade**, do degrau mais baixo ao mais alto, com o nome e o número de cada um, e o que cada degrau representa na ficção (o que alguém treinado faz normalmente, o que é difícil, o que é excepcional).
- Graus de resultado, se houver: sucesso, sucesso com custo, falha, crítico.
- Circunstância favorável e desfavorável, ajuda, teste oposto, teste estendido.
- Nova tentativa: quando pode e quando não pode.

## Antes do dado: o que quem joga decide
<!-- (guia) -->
- Tudo o que a personagem pode gastar ou acionar **antes** de rolar e que muda o dado: recursos (pontos, fichas, cargas), poderes, itens, ajuda.
- Pra cada um: custo, efeito e limite. É a lista que o mestre oferece numa linha antes de esperar o "rola".

## Teste de conhecimento
<!-- (guia) -->
- Como o sistema resolve "a personagem reconhece isto?": qual teste, com que dificuldade pra pergunta simples, complexa e de mistério.
- Se o sistema prevê conclusão errada numa falha feia, descreva aqui.

## Personagem
- Criação: atributos, origem, classe ou equivalente, o que cada escolha dá.
- Evolução: como e quando a personagem sobe de nível ou ganha habilidades.

## Ficha
<!-- (guia) -->
- **Campos que mudam em jogo:** vida, recursos, condições, munição, dinheiro e qualquer contador que o sistema acumule durante a sessão (experiência, estresse, corrupção).
- **O que conferir no `/fim`:** a lista, campo por campo, do que o mestre confere na nota da personagem ao encerrar a sessão.
- **Dados pra rolar:** o formato da linha que vai na ficha pra cada teste comum (a expressão do script já pronta).
- Ficha visual: só existe se a campanha tem um script de ficha pra este sistema. Se tiver, o caminho e o comando ficam na linha "Ficha visual" do `_campanha.md`.

## Combate
<!-- (guia) -->
- Iniciativa, o que cabe num turno, ataque e defesa, dano, crítico, manobras.
- Distância e movimento: as faixas de alcance do sistema, se houver (são as que entram no `--faixas` do `grade.py` das plantas).
- Ferimentos e morte: o que acontece com a vida no fim, como se estabiliza alguém, quando a personagem morre.

## Medo, estresse e outros estados
- Só se o sistema tem: como se perde, o que acontece no limite, como se recupera. A referência de gênero do guia (`Mestre/references/generos/`) aponta pra cá.

## Subsistemas do gênero
- Investigação, perseguição, furtividade, magia, viagem: o que o sistema tiver de procedimento próprio, um bloco curto pra cada.

## Descanso e recuperação
<!-- (guia) -->
- Quando a personagem pode descansar, o que cada tipo de descanso devolve e o que dá pra fazer no intervalo.

## Equipamento e recursos
- Dinheiro, carga, categorias de item, o que a facção ou o mundo fornece.

## Aliados e NPCs de apoio
- Como o sistema trata quem acompanha a personagem. Se a campanha liga o módulo de companheiros, é aqui que se anota como a ficha deles funciona.

## Regras opcionais e suplementos
- **Adotadas:** as que valem, com a página. O que uma campanha adota fica também nas "Regras da casa" do `_campanha.md` dela.
- **Não adotadas:** catálogo curto, pra saber que existem.

## Jogando solo
<!-- (guia) -->
- O livro costuma supor um grupo. O que muda com uma personagem só: quem estabiliza, como não travar numa pista perdida, o que substitui os outros jogadores.
- Como as peças do sistema encaixam no guia do mestre: o que é arco, o que vira relógio, o que vira pista planejada.

## Pra mestrar
<!-- (guia) -->
- O que o livro ensina sobre criar aventuras, cenas e inimigos, em poucas linhas.
- Tabelas e geradores úteis, com a página.

## Ajustes em teste
<!-- (guia) -->
> O que mudou em relação ao livro, ou está sendo experimentado. Uma entrada por ajuste. O mestre acrescenta aqui a resposta de quem joga à pergunta sobre o sistema, em todo `/fim`. Ajuste aprovado vira regra da casa; reprovado fica registrado como "descartado", com o motivo.

### <Nome curto do ajuste>
- O que mudou na regra:
- Por quê:
- Testado em: (campanha e sessão)
- Resultado: (funcionou, não funcionou, o que quem joga disse; manter, mudar ou descartar)
