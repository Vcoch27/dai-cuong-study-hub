param(
    [string]$RenderDirectory = (Join-Path $PSScriptRoot '.slide-renders'),
    [int]$Width = 1600
)

$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Path $RenderDirectory -Force | Out-Null
$slideApplication = New-Object -ComObject PowerPoint.Application
$existingPresentations = $slideApplication.Presentations.Count
$slideRecords = @()
try {
    foreach ($deckFile in Get-ChildItem -LiteralPath (Join-Path $PSScriptRoot 'slidegk') -Filter '*.pptx' | Where-Object { $_.Name -notlike '~$*' } | Sort-Object Name) {
        $chapterNumber = [int]([regex]::Match($deckFile.BaseName, '\d+').Value)
        $chapterDirectory = Join-Path $RenderDirectory "chapter-$chapterNumber"
        New-Item -ItemType Directory -Path $chapterDirectory -Force | Out-Null
        # Read-only, no new copy, no presentation window. Never save the source.
        $deckPresentation = $slideApplication.Presentations.Open($deckFile.FullName, -1, 0, 0)
        try {
            $renderHeight = [int][math]::Round($Width * $deckPresentation.PageSetup.SlideHeight / $deckPresentation.PageSetup.SlideWidth)
            for ($slideNumber = 1; $slideNumber -le $deckPresentation.Slides.Count; $slideNumber++) {
                $imageName = 'page-{0:D3}.png' -f $slideNumber
                $deckPresentation.Slides.Item($slideNumber).Export((Join-Path $chapterDirectory $imageName), 'PNG', $Width, $renderHeight)
                $slideRecords += [ordered]@{ file = $deckFile.Name; chapter = $chapterNumber; slide = $slideNumber; width = $Width; height = $renderHeight }
            }
            Write-Output "$($deckFile.Name): $($deckPresentation.Slides.Count) pages exported"
        } finally {
            $deckPresentation.Close()
            [void][Runtime.InteropServices.Marshal]::ReleaseComObject($deckPresentation)
        }
    }
    $slideRecords | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath (Join-Path $RenderDirectory 'index.json') -Encoding UTF8
} finally {
    # Leave an existing user's PowerPoint session running.
    if ($existingPresentations -eq 0 -and $slideApplication.Presentations.Count -eq 0) { $slideApplication.Quit() }
    [void][Runtime.InteropServices.Marshal]::ReleaseComObject($slideApplication)
}
