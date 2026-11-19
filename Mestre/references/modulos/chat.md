# Módulo: chat

Opcional. Só vale se o `_campanha.md` tem "Chat: sim" em "Módulos ligados". Com o módulo desligado: nenhuma conversa de celular em cena, nada em `Chat/`, nenhum print, e pule este arquivo no `/fim`. Só faz sentido em mundo que tem celular ou coisa parecida (rádio, cartas e recados também servem, se a campanha combinar).

Quando ler: guia do mestre, "Módulos opcionais".

A personagem tem um celular, e as pessoas falam com ela por ele: um grupo com quem anda junto, e às vezes alguém chama no privado, como no Mystic Messenger. É o equivalente às conversas de acampamento do Baldur's Gate 3: o lugar onde as relações andam fora da ação.

## Em jogo

- **Quando:** nos respiros. Entre missões, no descanso, à noite, no tempo vazio (ao perguntar se quem joga quer pular, o chat é uma das opções). Raramente durante a missão, como evento: alguém de fora manda algo, quem ficou pra trás pede ajuda, chega uma mensagem que não deveria existir. Uma ou duas conversas por pausa, não uma enxurrada.
- **Como mostrar:** mensagens curtas, com nome e hora, no jeito de escrever de cada um (tirado da nota: emoji, caixa alta, áudio descrito, figurinha, erro de digitação). Pare quando for a vez de quem joga responder. Não responder é permitido: se a mensagem pedia resposta, isso também é escolha e pode pesar na relação (e na aprovação, se o módulo de companheiros está ligado).
- **Formato:** em texto, num bloco `> 📱 **Grupo ou Nome** · grupo/privado`, uma linha por mensagem. Foto, figurinha, áudio, mensagem apagada e "digitando" usam os marcadores do template Chat.
- **Quem sabe o quê:** no grupo, todos que estão nele; no privado, só os dois. NPCs também mentem e escondem no chat; a verdade fica no arquivo de segredo deles: leia-o antes de escrever por um NPC.
- **Toda conversa de celular conta**, não só o grupo: mensagem com um parente, com um NPC de fora, com um contato que ela mal conhece, por qualquer aplicativo. Tudo vai pra `Chat/` na íntegra, com o que quem joga escreveu pela personagem do jeito que escreveu.

## Print do celular (SVG)

Só se a linha do módulo no `_campanha.md` permitir print. Salve a conversa na nota primeiro e gere a partir dela, assim o print nunca diverge do registro:

```bash
python Mestre/scripts/chat/chat_print.py "<nota da conversa>.md" "<saida>.svg" --eu <nome da personagem> [--titulo "<nome do grupo>"]
```

- As mensagens de `--eu` ficam à direita. Grupo mostra o nome de quem fala; privado não.
- **Fotos de perfil:** o script lê `Visual/Chat/avatares.json` (nome como aparece nas mensagens → recorte quadrado de 200×200 em `Visual/Chat/avatares/`). No privado a foto vai no topo; no grupo, ao lado da primeira bolha de cada pessoa. Quem não tem foto aparece com a inicial. Foto nova, aprovada por quem joga: recorte, salve lá e acrescente no JSON.
- O SVG vai em `Visual/Chat/`, embutido na nota da conversa. Se quem joga usa o celular, mande o arquivo na mesma resposta.
- Em `Visual/Chat/` há dois exemplos ("Exemplo - ...", nota e print), com personagens inventados.

## Registro (o conteúdo não pode se perder)

Ao fim de cada conversa, salve em `Chat/` da saga (template Chat) com as mensagens como foram escritas, preencha "O que ficou" e adicione uma linha em `Chat/_chat.md` (template Chat índice), mais o que ficou pendente. Com o módulo de companheiros ligado, aprovação ganha ou perdida vai também na nota do companheiro. Não resuma nem reescreva conversas antigas.

## No início da sessão

Leia `Chat/_chat.md`: pendentes e o que cada um disse por último. A conversa inteira só se precisar.

## `/fim`

Confira se toda conversa da sessão foi salva e indexada. Um NPC que agiu fora de cena pode deixar uma mensagem esperando a personagem na próxima sessão: escreva-a em `Chat/` e marque como pendente em `_chat.md`.
