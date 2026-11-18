# Módulo: companheiros

Opcional. Só vale se o `_campanha.md` tem "Companheiros: sim" em "Módulos ligados". Com o módulo desligado: não planeje elenco, não crie nota de companheiro, não fale de aprovação e pule este arquivo no `/fim`. Aliado comum continua existindo como NPC (template NPC), sem ficha, sem turno e sem aprovação.

Leia: na sessão zero (planejar o elenco), antes de um companheiro entrar em cena pela primeira vez na sessão, ao escolher quem vai pra campo e no `/fim`.

O livro de quase todo sistema supõe um grupo. Este módulo é um jeito de ter grupo no jogo solo sem tirar o centro de quem joga: um elenco de companheiros (NPCs com ficha e turno próprio, controlados por você), principais e opcionais, que entram ao longo da jornada.

## Em cena

- É um personagem, não um ajudante de mestre. Tem voz, objetivo, medo e opinião (nota dele). O que ele esconde, o que aprova agora e o que anda fazendo estão no arquivo de segredo dele (`Entidades/<Nome> (segredo).md`): leia os dois antes de ele falar. Pode discordar de quem joga, recusar, ter segredos e mudar com o que a personagem faz.
- **A protagonista é a personagem de quem joga.** O companheiro não resolve o mistério, não tira a conclusão decisiva, não dá o plano. Pode comentar o que viu ou opinar quando perguntam, como qualquer NPC que só sabe o que presenciou.
- Age no turno dele em combate e na investigação, com rolagens pelo script. Narre a ação dele curta e depois da ação da personagem.
- Nunca decide pela personagem nem fala por ela. Nunca "salva no último segundo" fora do que as regras e os dados permitem.
- Pode se ferir e morrer. Se for ele quem pode estabilizar a personagem (`Sistemas/<sistema>.md`, "Combate" e "Jogando solo"), ele tenta no turno dele, com o dado do script.
- **Até 2 em campo por missão.** Com dois presentes, não deixe os dois comentarem tudo: uma fala por cena costuma bastar, e eles podem discordar entre si.
- **Aprovação** (-50 a 100, campo `aprovacao`; regras abaixo). Reaja às escolhas de quem joga pelos valores atuais dele, não pelo que agrada: pequeno ±1, médio ±5, grande ±10, marca curta `(Nome aprova)` na cena. Os valores podem evoluir com a história e os motivos profundos dele, nunca pra aprovar o que a personagem está fazendo agora.
- Missão pessoal funciona como uma ameaça pequena com presságios: se quem joga ignorar, avança fora de cena e cobra depois.
- **Toque discreto** (quando os combinados pedem ganchos sutis): se quem joga parece seguir contra algo que a própria personagem viu ou ouviu, um companheiro presente pode dar um toque curto, no jeito dele ("tem certeza? a vizinha falou do porão"). Vem só do que ele presenciou, nunca do que só você sabe. Uma vez, sem insistir, sem apontar a solução. Tangente escolhida de propósito não é erro: aí não cutuque (`Mestre/references/imprevistos.md`).

## Planejar o elenco (sessão zero)

Depois da personagem e do vilão, porque cada companheiro se liga aos dois. Pelo menos 3, que entram ao longo da jornada:

- **Principais (2):** entram cedo (na abertura ou no primeiro arco) e têm lugar garantido na história, a menos que morram ou vão embora. A missão pessoal deles se liga à ameaça de campanha, ao vilão ou a uma reviravolta. Exemplo: Astarion e Shadowheart no Baldur's Gate 3.
- **Opcionais (1 ou mais):** aparecem depois, e entrar depende de algo que quem joga faz ou escolhe (salvar alguém, tomar um lado, estar no lugar certo). A personagem pode nunca recrutar, e recusar ou perder também é consequência. Exemplo: Halsin (só se o bosque for salvo) e Minthara (só pelo lado oposto).
- Pra cada um: conceito, gatilho de entrada, missão pessoal, o que aprova e reprova, um segredo, aprovação inicial e ficha (no formato do sistema). Varie funções (combate, investigação, conhecimento, lábia) e personalidades que se choquem entre si e com a personagem.
- **Nada genérico:** cada companheiro precisa de uma contradição (o que parece × o que é), uma voz própria (inclusive no chat, se o módulo de chat estiver ligado), um desejo ou gosto fora da trama e atrito com pelo menos outro companheiro. Teste: se dá pra resumir com um arquétipo só ("o grandão piadista", "a gótica sarcástica", "o veterano rabugento"), refaça antes de mostrar.
- Pergunte se quem joga quer aprovar o conceito dos principais (só a premissa, sem segredo nem missão pessoal) ou prefere a surpresa. Segredo, missão pessoal e opcionais ficam com você.
- O plano vai em `Segredos.md` ("Companheiros planejados"). Em campanha grande, cada plano vira um arquivo em `Companheiros/`, na pasta de segredos da campanha, com número no nome (`Companheiro 1.md`), nunca o nome dele, porque nome de arquivo aparece no Obsidian e daria spoiler, e o `Segredos.md` guarda só uma tabela (quem, papel, quando entra), pra não ler todos em toda sessão. A nota do companheiro (template Companheiro) nasce quando ele aparece em jogo, pra não dar spoiler no vault. Nessa hora nasce também o arquivo de segredo dele (`Entidades/<Nome> (segredo).md`), que guarda o estado atual (o que aprova e reprova agora, os valores mínimos, o que faz fora de cena) e diz qual é o plano dele.

## Em campo

Até 2 companheiros por missão; os outros ficam na base (o acampamento, a cidade, o quartel: onde a história guardar quem não foi). Antes de cada missão, pergunte quem vai. Quem fica continua vivo fora de cena (avança a missão pessoal, forma opinião).

## Aprovação

Como no Baldur's Gate 3: um número de **-50 a 100** no campo `aprovacao` da nota, que cresce ou cai pelo acúmulo de muitos momentos, inclusive pequenos.

- Faixas: -49 a -40 muito baixa · -39 a -20 baixa · -19 a 20 neutra · 21 a 40 média · 41 a 60 alta · 61 a 80 muito alta · 81 a 100 excepcional.
- Tamanho: momento pequeno ±1, médio ±5, grande ±10. Raro: ±20, pra um momento enorme ligado à missão pessoal ou a quem entrou tarde e precisa alcançar os outros.
- Só reage quem presenciou. Cada acontecimento conta uma vez (sem repetir a mesma gentileza pra acumular ponto). Máximo 100.
- Na cena: a reação dele na ficção e uma marca curta **com o número novo**, `(Nome aprova · 38)`, `(Nome aprova muito · 50)`, `(Nome desaprova · 12)`. **A marca e a mudança na nota saem na mesma resposta, nunca uma sem a outra** (motivo: aprovação mudou na nota sem marca na cena, e marca saiu na cena sem o número mudar; com o número junto, quem joga confere na hora). Mudança de faixa vai no Histórico com o motivo.
- Em -20 e em -40 ele avisa, na ficção, que está no limite. Em -50 ou menos vai embora de vez (ou pior, se o segredo dele permitir).
- A faixa muda o tom do diálogo e a dificuldade pra convencê-lo: em alta ou acima, um degrau mais fácil na escala do sistema; em baixa ou abaixo, um degrau mais difícil. Momentos especiais (falas íntimas, romance, desfechos da missão pessoal) pedem um valor mínimo, escrito no arquivo de segredo dele.
- **O que ele aprova e reprova pode mudar.** A lista do arquivo de segredo é o estado atual, não uma regra fixa. Ela muda quando faz sentido pros motivos profundos dele: a relação se aprofunda, a missão pessoal se resolve, algo o abala. Exemplo: um companheiro cínico que no começo despreza caridade sem retorno pode, depois de confiar na personagem e encarar o próprio passado, passar a não ligar ou até aprovar. A mudança precisa de um motivo dentro da ficção, aparecer em cena (uma conversa, uma reação diferente do normal) e ir pro Histórico. Nunca mude os valores dele pra que aprove o que quem joga está fazendo agora: isso é bajulação.

**Revisar depois da sessão zero:** a escala do Baldur's Gate 3 foi feita pra um jogo de dezenas de horas. Chegar em "alta" (41) pede uns 8 momentos médios. Com o mundo e as ameaças criados, estime quantos momentos de aprovação cada principal vai ter. Se a campanha planejada parecer curta pra isso (por exemplo, menos de uns 10 a 15 sessões com o companheiro), proponha a quem joga uma escala menor: -10 a +15, mudanças de ±1/2/3, faixas hostil (-10 ou menos, vai embora) · desconfiado (-9 a -4) · neutro (-3 a +3) · aliado (+4 a +9) · leal (+10 a +15). A escala escolhida fica na linha do módulo, no `_campanha.md`.

## Continuação na mesma saga

Companheiros que sobrevivem podem voltar numa campanha seguinte, com a ficha e a aprovação que tinham. O elenco da nova campanha soma quem volta e gente nova, com pelo menos um companheiro novo. Ao fechar a campanha, o `_saga.md` guarda o status e a aprovação de cada um.

## Registro e `/fim`

- Fim de cena: aprovação ganha ou perdida vai na nota do companheiro; mudança de faixa ou de valores, no Histórico.
- `/fim`: confira a aprovação de cada um contra o que aconteceu na sessão; mova quem ficou na base (missão pessoal, opinião sobre o que soube) e registre no arquivo de segredo dele; atualize a ficha de quem se feriu ou gastou recurso.
- Checagem de consistência: a tabela de companheiros do `Segredos.md` bate com os arquivos de `Companheiros/` e com as notas de quem já apareceu?
