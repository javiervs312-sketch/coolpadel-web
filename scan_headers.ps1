$files = Get-ChildItem -Path "coolpadel-web" -Recurse -Filter "*.html" | Where-Object { $_.FullName -notmatch "\\.git" }
Write-Host "Total HTML files: $($files.Count)"
$patterns = @{}
$noHeaders = @()
$noDropdown = @()

foreach ($f in $files) {
    $content = [System.IO.File]::ReadAllText($f.FullName)
    $headerMatch = [regex]::Match($content, '<header[\s\S]*?</header>')
    if ($headerMatch.Success) {
        $header = $headerMatch.Value
        $m = [regex]::Match($header, '<a[^>]+href=["'']([^"'']+)["''][^>]*>[\s\S]*?llavero[\s\S]*?</a>', [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
        if ($m.Success) {
            $href = $m.Groups[1].Value
            $patterns[$href] = [int]$patterns[$href] + 1
        } else {
            $patterns["NO_LLAVERO"] = [int]$patterns["NO_LLAVERO"] + 1
        }

        if (-not ($header.Contains('id="lang-dropdown-btn"') -or $header.Contains('id="lang-dropdown-container"'))) {
            $noDropdown += $f.FullName
        }
    } else {
        $noHeaders += $f.FullName
    }
}

Write-Host "`nLlaveros link occurrences:"
$patterns.GetEnumerator() | Sort-Object Value -Descending | Format-Table -AutoSize

Write-Host "Files without header: $($noHeaders.Count)"
if ($noHeaders.Count -gt 0) {
    $noHeaders | ForEach-Object { Write-Host " - $_" }
}

Write-Host "Files without dropdown: $($noDropdown.Count)"
if ($noDropdown.Count -gt 0) {
    $noDropdown | ForEach-Object { Write-Host " - $_" }
}
