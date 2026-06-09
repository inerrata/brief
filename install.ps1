# Installs the marketing skill into ~\.claude\skills\marketing for Claude Code.
# Usage: irm https://raw.githubusercontent.com/inerrata/brief/main/install.ps1 | iex
$ErrorActionPreference = 'Stop'

$repo = 'inerrata/brief'
$dest = if ($env:CLAUDE_SKILLS_DIR) { Join-Path $env:CLAUDE_SKILLS_DIR 'marketing' } else { Join-Path $HOME '.claude\skills\marketing' }
$tmp  = Join-Path ([System.IO.Path]::GetTempPath()) ("brief-install-" + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Force -Path $tmp | Out-Null

try {
    Write-Host "Downloading $repo ..."
    $zip = Join-Path $tmp 'brief.zip'
    Invoke-WebRequest -Uri "https://codeload.github.com/$repo/zip/refs/heads/main" -OutFile $zip -UseBasicParsing
    Expand-Archive -Path $zip -DestinationPath $tmp

    $src = Get-ChildItem -Directory $tmp | Where-Object { Test-Path (Join-Path $_.FullName '_unpacked\marketing\SKILL.md') } | Select-Object -First 1
    if (-not $src) { throw "Could not find _unpacked/marketing in the downloaded archive." }

    New-Item -ItemType Directory -Force -Path $dest | Out-Null
    Copy-Item -Recurse -Force (Join-Path $src.FullName '_unpacked\marketing\*') $dest
    Write-Host "Installed marketing skill to $dest"
    Write-Host "Restart Claude Code (or start a new session) to pick it up."
}
finally {
    Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
}
