# Mapas do Map Genie sem marcadores

Dois scripts pra baixar um mapa do [Map Genie](https://mapgenie.io) limpo, sem ícones, e opcionalmente desenhar por cima as divisórias e os nomes das regiões.

| Arquivo | O que faz |
|---|---|
| `baixar_mapa.py` | Baixa os tiles do mapa e os limites das regiões. Gera uma pasta com os tiles e um `mapa.json`. |
| `montar_mapa.ps1` | Junta os tiles numa imagem JPEG e, se você pedir, desenha as regiões. |

## Como funciona

O Map Genie não guarda o mapa como uma imagem única. Ele divide o mapa em pedaços de 256×256 px (os *tiles*), e o navegador vai carregando só os que aparecem na tela. Os marcadores são outra camada, desenhada por cima. Por isso os tiles já vêm limpos.

- **Tiles:** o endereço segue um padrão como `https://tiles.mapgenie.io/games/<jogo>/<mapa>/v4/{z}/{y}/{x}.jpg`. O script lê esse padrão e quais tiles existem em cada zoom no `window.mapData` do HTML da página.
- **Regiões:** vêm da API `https://mapgenie.io/api/v1/maps/<id>/data`, a mesma que o site usa pra desenhar as bordas. Cada região tem um polígono em latitude e longitude e um ponto central pro nome. O script converte isso pra pixels da imagem final usando a mesma projeção do mapa (Web Mercator). Por isso as linhas caem exatamente sobre o terreno.

## Requisitos

- **Python 3**, só com a biblioteca padrão. Não precisa instalar nada.
- **PowerShell 7** (`pwsh`) no Windows. A montagem usa o `System.Drawing` do .NET, que já vem com o Windows.
- Memória: uma imagem de 16384×16384 com regiões usa uns 2 GB de RAM enquanto está sendo montada.

## Passo a passo

Abra um terminal na pasta `MapGenie` e rode os comandos abaixo.

### 1. Baixar

```bash
python baixar_mapa.py "https://mapgenie.io/stalker-2-heart-of-chornobyl/maps/the-zone"
```

Isso cria a pasta `the-zone/`, com `tiles_z14/` e `mapa.json`. O nome da pasta vem do *slug* do mapa.

Opções:

| Opção | Padrão | Pra que serve |
|---|---|---|
| `--zoom N` | maior disponível | Escolhe o nível de detalhe. Cada zoom a mais dobra a largura da imagem e multiplica por 4 o número de tiles. |
| `--saida PASTA` | `./<slug>` | Onde salvar os tiles e o `mapa.json`. |
| `--threads N` | `16` | Quantos downloads simultâneos. |

Se algum tile falhar, rode o mesmo comando de novo. Ele pula o que já foi baixado e tenta só o que falta.

Tamanhos do mapa The Zone, de STALKER 2:

| Zoom | Tiles | Imagem | Arquivo |
|---|---|---|---|
| 13 | 1.024 | 8192×8192 | ~14 MB |
| 14 | 4.096 | 16384×16384 | ~52 MB |

### 2. Montar

Imagem limpa:

```bash
pwsh -ExecutionPolicy Bypass -File montar_mapa.ps1 -Pasta .\the-zone
```

Com divisórias e nomes. O padrão é branco com 30% de opacidade, a versão que ficou no vault:

```bash
pwsh -ExecutionPolicy Bypass -File montar_mapa.ps1 -Pasta .\the-zone -Regioes
```

O arquivo sai dentro da pasta, como `the-zone-z14.jpg` ou `the-zone-z14-regioes.jpg`.

> [!info] Por que `-ExecutionPolicy Bypass`?
> O Windows bloqueia scripts `.ps1` por padrão. Esse parâmetro libera só esta execução e não muda nenhuma configuração do sistema.

Opções do `montar_mapa.ps1`:

| Opção | Padrão | Pra que serve |
|---|---|---|
| `-Pasta` | (obrigatório) | Pasta gerada no passo 1. |
| `-Saida` | `<slug>-z<zoom>[-regioes].jpg` | Caminho do arquivo final. |
| `-Regioes` | desligado | Desenha as divisórias e os nomes. |
| `-Cor` | `#FFFFFF` | Cor das divisórias e dos nomes. |
| `-CorTexto` | igual a `-Cor` | Cor só dos nomes, se quiser diferente das linhas. |
| `-Opacidade` | `0.3` | De `0` a `1`, aplicada às linhas e aos nomes. |
| `-TamanhoFonte` | automático | Em px. O automático dá 150 px numa imagem de 16k e 75 px numa de 8k. |
| `-EspessuraLinha` | automático | Em px. O automático dá 16 px numa imagem de 16k e 8 px numa de 8k. |
| `-Fonte` | `Bahnschrift` | Qualquer fonte instalada no Windows. |
| `-SemMaiusculas` | desligado | Mantém os nomes como vêm do Map Genie, sem passar pra maiúsculas. |
| `-Qualidade` | `92` | Qualidade do JPEG, de 1 a 100. |

Exemplos:

```bash
pwsh -ExecutionPolicy Bypass -File montar_mapa.ps1 -Pasta .\the-zone -Regioes -Cor '#7a7a7a' -Opacidade 1
```

```bash
pwsh -ExecutionPolicy Bypass -File montar_mapa.ps1 -Pasta .\the-zone -Regioes -Cor '#7a7a7a' -CorTexto '#FFFFFF' -Opacidade 0.6
```

Dá pra rodar o passo 2 quantas vezes quiser, com opções diferentes, sem baixar nada de novo.

## Observações

- **Opacidade uniforme:** quando duas regiões são vizinhas, a borda entre elas é desenhada duas vezes. Pra ela não ficar mais clara que o resto, o script desenha tudo opaco numa camada separada e só aplica a opacidade no final.
- **Outros mapas:** os scripts funcionam em qualquer mapa do Map Genie. Mas nem todo mapa tem regiões cadastradas. Quando não tem, o passo 1 avisa e a imagem limpa continua funcionando.
- **Se o site mudar:** os scripts dependem de como o Map Genie funciona hoje (o `window.mapData` na página e a API `/api/v1/maps/<id>/data`). Se ele mudar isso, os scripts podem parar de funcionar.
- **Uso pessoal:** os mapas são arte do jogo e do Map Genie. Use pra coisa sua, como a mesa de RPG, e não pra redistribuir.
