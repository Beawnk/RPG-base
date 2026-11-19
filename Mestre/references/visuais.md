# Peças visuais

Leia quando a cena pedir uma planta, um documento com parte oculta ou a ficha visual, ou quando quem joga pedir uma peça. São ferramentas, não obrigação: use quando a campanha combinar (as regras de cada campanha ficam em `Regras visuais.md`, uma das "Notas à parte" do `_campanha.md`) ou quando quem joga pedir.

- **Plantas** (`Mestre/scripts/mapas/`): quatro geradores de exemplo, do mais simples ao mais trabalhado (`planta_v1_limpa.py`, `planta_v2_ilustrada.py`, `planta_v3_arquivo.py`, `planta_v4_foto.py`), todos com o mesmo cenário. São moldes: copie o do estilo combinado, troque o cenário pelo lugar da cena e gere o SVG em `Visual/Mapas/`. A planta mostra só o que a personagem já viu. `grade.py` dá coordenadas tipo batalha naval e mede distâncias; as faixas de alcance, se o sistema tem, entram pelo `--faixas` (`Sistemas/<sistema>.md`, "Combate").
- **Documentos** (`Mestre/scripts/documentos/documento_exemplo.py`): um papel de arquivo com as cinco formas de esconder um trecho (tarja, dano de água e fogo, tinta invisível, símbolo, impressão corrompida). Molde pra documento com parte oculta; o SVG vai em `Visual/Documentos/`. O texto que a personagem leu vai também pra nota, por extenso.
- **Peça gerada:** embuta na nota do lugar ou do item e, se quem joga usa o celular, mande o arquivo na mesma resposta (`AGENTS.md`, "Registro").
- **Ficha visual:** só existe se a campanha tem um script de ficha pro sistema dela (linha "Ficha visual" do `_campanha.md`). Sem script, a ficha é a nota da personagem e basta.
