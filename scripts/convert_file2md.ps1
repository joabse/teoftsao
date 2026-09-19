<#
.SYNOPSIS
    Script de conversão automatizada do agente file2md no projeto teoftsao.
.DESCRIPTION
    Converte documentos (PDF nativo, DOCX, PPTX, XLSX, EPUB, CSV, etc.) para Markdown
    usando a ferramenta anydoc, salva no destino de 01_markdown, replica para ftsabrain/file2md
    e registra a operação no índice central ftsabrain/file2md/00-indice.md.
.PARAMETER FilePath
    Caminho absoluto ou relativo do arquivo original a ser convertido.
.PARAMETER Materia
    Nome da matéria (ex: biblia2, biblia3, etc.).
.PARAMETER SubFolder
    Subpasta opcional em 01_markdown (ex: adicionais, transcricoes).
.EXAMPLE
    .\scripts\convert_file2md.ps1 -FilePath "materias\biblia2\00_originais\documento.docx" -Materia "biblia2"
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$FilePath,

    [Parameter(Mandatory = $true)]
    [string]$Materia,

    [Parameter(Mandatory = $false)]
    [string]$SubFolder = "",

    [Parameter(Mandatory = $false)]
    [string]$Notes = ""
)

$ErrorActionPreference = "Stop"

# Raiz do projeto
$ProjectRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$ResolvedFile = Resolve-Path $FilePath -ErrorAction SilentlyContinue

if (-not $ResolvedFile -or -not (Test-Path $ResolvedFile)) {
    Write-Error "Arquivo original não encontrado: $FilePath"
    exit 1
}

$FileItem = Get-Item $ResolvedFile
$BaseName = $FileItem.BaseName
$Extension = $FileItem.Extension.ToLower()

# Definir pastas de saída
$MarkdownDir = Join-Path $ProjectRoot "materias\$Materia\01_markdown"
if ($SubFolder -ne "") {
    $MarkdownDir = Join-Path $MarkdownDir $SubFolder
}
if (-not (Test-Path $MarkdownDir)) {
    New-Item -ItemType Directory -Path $MarkdownDir -Force | Out-Null
}

$TargetMarkdownPath = Join-Path $MarkdownDir "$BaseName.md"

# Pasta no ftsabrain
$BrainFile2mdDir = Join-Path $ProjectRoot "ftsabrain\file2md\$Materia"
if ($SubFolder -ne "") {
    $BrainFile2mdDir = Join-Path $BrainFile2mdDir $SubFolder
}
if (-not (Test-Path $BrainFile2mdDir)) {
    New-Item -ItemType Directory -Path $BrainFile2mdDir -Force | Out-Null
}
$BrainMarkdownPath = Join-Path $BrainFile2mdDir "$BaseName.md"

$IndicePath = Join-Path $ProjectRoot "ftsabrain\file2md\00-indice.md"

Write-Host "Iniciando conversão file2md..." -ForegroundColor Cyan
Write-Host "Origem: $($FileItem.FullName)"
Write-Host "Destino: $TargetMarkdownPath"

# Testar se anydoc existe
$anydocCmd = Get-Command anydoc -ErrorAction SilentlyContinue
if (-not $anydocCmd) {
    Write-Error "CLI anydoc não encontrada no sistema. Certifique-se de que @firecrawl/anydoc está instalado."
    exit 1
}

# Executar anydoc
$ProcessStart = Get-Date -Format "yyyy-MM-dd HH:mm"
$ToolName = "anydoc 0.2.4"
$Status = "Pendente"
$Obs = $Notes

try {
    $output = & anydoc "$($FileItem.FullName)" -o "$TargetMarkdownPath" 2>&1
    $exitCode = $LASTEXITCODE

    if ($exitCode -eq 0 -and (Test-Path $TargetMarkdownPath)) {
        $Status = "✅ Convertido"
        if ([string]::IsNullOrWhiteSpace($Obs)) {
            $Obs = "Sucesso ($((Get-Item $TargetMarkdownPath).Length) bytes)"
        }
        Write-Host "Conversão bem-sucedida!" -ForegroundColor Green

        # Copiar para ftsabrain/file2md/<materia>/
        Copy-Item -Path $TargetMarkdownPath -Destination $BrainMarkdownPath -Force
        Write-Host "Cópia sincronizada em ftsabrain: $BrainMarkdownPath" -ForegroundColor Green
    } elseif ($output -like "*need OCR*" -or $exitCode -eq 3) {
        $Status = "⚠️ Necessita OCR"
        $Obs = "Documento escaneado/imagem detectado pelo anydoc"
        Write-Warning "Documento requer OCR. O anydoc não processa imagens escaneadas sem OCR externo."
    } else {
        $Status = "❌ Falha"
        $Obs = ($output -join " ")
        Write-Error "Erro na conversão: $Obs"
    }
} catch {
    $Status = "❌ Erro"
    $Obs = $_.Exception.Message
    Write-Error "Exceção ao converter: $Obs"
}

# Registrar no índice central do ftsabrain
if (Test-Path $IndicePath) {
    $RelTarget = [System.IO.Path]::GetRelativePath($ProjectRoot, $TargetMarkdownPath).Replace("\", "/")
    $FileNameEscaped = $FileItem.Name
    $MdFile = '`' + $FileNameEscaped + '`'
    $MdTarget = '`' + $RelTarget + '`'
    $RegistroLinha = "| $ProcessStart | $Materia | $MdFile | $Extension | $MdTarget | $ToolName | $Status ($Obs) |"
    
    # Adicionar na tabela do índice
    $IndiceContent = Get-Content $IndicePath -Raw -Encoding UTF8
    $TabelaHeaderPattern = "(\| Data / Hora \| Matéria \| Arquivo Original \| Formato \| Destino Markdown \| Ferramenta \| Status \|\r?\n\|[-| ]+\|\r?\n)"
    
    if ($IndiceContent -match $TabelaHeaderPattern) {
        $NovoIndice = $IndiceContent -replace $TabelaHeaderPattern, "`$1$RegistroLinha`r`n"
        Set-Content -Path $IndicePath -Value $NovoIndice -Encoding UTF8
        Write-Host "Registro inserido no índice: $IndicePath" -ForegroundColor Cyan
    } else {
        Add-Content -Path $IndicePath -Value "`r`n$RegistroLinha" -Encoding UTF8
        Write-Host "Registro anexado ao índice: $IndicePath" -ForegroundColor Cyan
    }
} else {
    Write-Warning "Índice $IndicePath não encontrado para registro."
}
