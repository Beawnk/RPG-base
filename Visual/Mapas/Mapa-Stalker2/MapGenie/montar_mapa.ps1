<#
.SYNOPSIS
  Junta os tiles baixados por baixar_mapa.py numa imagem JPEG e, opcionalmente,
  desenha as divisórias e os nomes das regiões.

.EXAMPLE
  pwsh -ExecutionPolicy Bypass -File montar_mapa.ps1 -Pasta .\the-zone
  pwsh -ExecutionPolicy Bypass -File montar_mapa.ps1 -Pasta .\the-zone -Regioes
  pwsh -ExecutionPolicy Bypass -File montar_mapa.ps1 -Pasta .\the-zone -Regioes -Cor '#7a7a7a' -Opacidade 1
#>
param(
  [Parameter(Mandatory)] [string] $Pasta,      # pasta gerada pelo baixar_mapa.py (tem o mapa.json)
  [string] $Saida,                             # arquivo final (padrão: <slug>-z<zoom>[-regioes].jpg na pasta)
  [switch] $Regioes,                           # desenha divisórias e nomes
  [string] $Cor = '#FFFFFF',                   # cor das divisórias e dos nomes
  [double] $Opacidade = 0.3,                   # 0 a 1, aplicada a divisórias e nomes juntos
  [string] $CorTexto,                          # opcional: cor só dos nomes (padrão: igual a -Cor)
  [double] $TamanhoFonte = 0,                  # px; 0 = automático (150 px numa imagem de 16384 px)
  [double] $EspessuraLinha = 0,                # px; 0 = automático (16 px numa imagem de 16384 px)
  [string] $Fonte = 'Bahnschrift',
  [switch] $SemMaiusculas,                     # mantém os nomes como vêm do Map Genie
  [int] $Qualidade = 92                        # qualidade do JPEG (1-100)
)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$Pasta = (Resolve-Path $Pasta).Path
$info = Get-Content (Join-Path $Pasta 'mapa.json') -Raw -Encoding utf8 | ConvertFrom-Json
$ts = [int]$info.tile_size
$cols = $info.xmax - $info.xmin + 1; $rows = $info.ymax - $info.ymin + 1
$W = $cols * $ts; $H = $rows * $ts
if (-not $Saida) {
  $sufixo = if ($Regioes) { '-regioes' } else { '' }
  $Saida = Join-Path $Pasta "$($info.slug)-z$($info.zoom)$sufixo.jpg"
}
$escala = $W / 16384.0
if ($TamanhoFonte -le 0) { $TamanhoFonte = [math]::Max(12, 150 * $escala) }
if ($EspessuraLinha -le 0) { $EspessuraLinha = [math]::Max(1, 16 * $escala) }

Write-Host "Montando ${W}x${H} px a partir de $($cols * $rows) tiles..."
$bmp = New-Object System.Drawing.Bitmap $W, $H, ([System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$tilesDir = Join-Path $Pasta $info.tiles_dir
$faltando = 0
for ($y = $info.ymin; $y -le $info.ymax; $y++) {
  for ($x = $info.xmin; $x -le $info.xmax; $x++) {
    $arq = Join-Path $tilesDir "${y}_${x}.$($info.ext)"
    if (-not (Test-Path $arq)) { $faltando++; continue }
    $t = [System.Drawing.Image]::FromFile($arq)
    $g.DrawImage($t, ($x - $info.xmin) * $ts, ($y - $info.ymin) * $ts, $ts, $ts)
    $t.Dispose()
  }
}
if ($faltando) { Write-Warning "$faltando tiles faltando (ficam pretos). Rode o baixar_mapa.py de novo pra completar." }

if ($Regioes) {
  if (-not $info.regions -or $info.regions.Count -eq 0) { Write-Warning 'Esse mapa não tem regiões no mapa.json.' }
  else {
    Write-Host "Desenhando $($info.regions.Count) regiões..."
    # Desenha tudo opaco numa camada própria e aplica a opacidade uma vez só: assim a borda
    # compartilhada por duas regiões (desenhada duas vezes) e o texto que cruza uma linha
    # não ficam mais claros que o resto.
    $layer = New-Object System.Drawing.Bitmap $W, $H, ([System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $lg = [System.Drawing.Graphics]::FromImage($layer)
    $lg.SmoothingMode = 'AntiAlias'; $lg.TextRenderingHint = 'AntiAlias'
    $corLinha = [System.Drawing.ColorTranslator]::FromHtml($Cor)
    $corNome = if ($CorTexto) { [System.Drawing.ColorTranslator]::FromHtml($CorTexto) } else { $corLinha }
    $pen = New-Object System.Drawing.Pen $corLinha, ([single]$EspessuraLinha); $pen.LineJoin = 'Round'
    foreach ($r in $info.regions) {
      foreach ($ring in $r.rings) {
        if ($ring.Count -lt 2) { continue }
        $pts = [System.Drawing.PointF[]]($ring | ForEach-Object { New-Object System.Drawing.PointF ([single]$_[0]), ([single]$_[1]) })
        $lg.DrawPolygon($pen, $pts)
      }
    }
    $font = New-Object System.Drawing.Font $Fonte, ([single]$TamanhoFonte), ([System.Drawing.FontStyle]::Bold), ([System.Drawing.GraphicsUnit]::Pixel)
    $brush = New-Object System.Drawing.SolidBrush $corNome
    $fmt = New-Object System.Drawing.StringFormat; $fmt.Alignment = 'Center'; $fmt.LineAlignment = 'Center'
    foreach ($r in $info.regions) {
      if ($null -eq $r.cx) { continue }
      $nome = if ($SemMaiusculas) { $r.title } else { $r.title.ToUpper() }
      $lg.DrawString($nome, $font, $brush, [single]$r.cx, [single]$r.cy, $fmt)
    }
    $lg.Dispose()
    $cm = New-Object System.Drawing.Imaging.ColorMatrix; $cm.Matrix33 = [single]$Opacidade
    $ia = New-Object System.Drawing.Imaging.ImageAttributes; $ia.SetColorMatrix($cm)
    $g.DrawImage($layer, (New-Object System.Drawing.Rectangle 0, 0, $W, $H), 0, 0, $W, $H, [System.Drawing.GraphicsUnit]::Pixel, $ia)
    $layer.Dispose()
  }
}
$g.Dispose()

$enc = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object MimeType -eq 'image/jpeg'
$p = New-Object System.Drawing.Imaging.EncoderParameters 1
$p.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter ([System.Drawing.Imaging.Encoder]::Quality), ([long]$Qualidade)
$bmp.Save($Saida, $enc, $p)
$bmp.Dispose()
Write-Host ("Salvo: {0} ({1:N1} MB)" -f $Saida, ((Get-Item $Saida).Length / 1MB))
