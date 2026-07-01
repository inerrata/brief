# Installs the marketing skill into ~\.claude\skills\marketing for Claude Code.
#
# Usage:
#   irm https://raw.githubusercontent.com/inerrata/brief/main/install.ps1 | iex
#     -> installs the LATEST RELEASE (recommended)
#   $env:BRIEF_REF = 'v1.7.0'; irm .../install.ps1 | iex
#     -> installs a pinned version
#   $env:BRIEF_REF = 'main';   irm .../install.ps1 | iex
#     -> tracks main (unreleased)
$ErrorActionPreference = 'Stop'

$repo = 'inerrata/brief'
$dest = if ($env:CLAUDE_SKILLS_DIR) { Join-Path $env:CLAUDE_SKILLS_DIR 'marketing' } else { Join-Path $HOME '.claude\skills\marketing' }

$ref = $env:BRIEF_REF
if (-not $ref) {
    # Default to the latest release tag; fall back to main if the API is unreachable.
    try {
        $latest = Invoke-RestMethod -Uri "https://api.github.com/repos/$repo/releases/latest" -UseBasicParsing
        $ref = $latest.tag_name
    } catch { $ref = 'main' }
}

$tmp = Join-Path ([System.IO.Path]::GetTempPath()) ("brief-install-" + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Force -Path $tmp | Out-Null

try {
    Write-Host "Downloading $repo @ $ref ..."
    $zip = Join-Path $tmp 'brief.zip'
    Invoke-WebRequest -Uri "https://codeload.github.com/$repo/zip/$ref" -OutFile $zip -UseBasicParsing
    Expand-Archive -Path $zip -DestinationPath $tmp

    $src = Get-ChildItem -Directory $tmp | Where-Object { Test-Path (Join-Path $_.FullName '_unpacked\marketing\SKILL.md') } | Select-Object -First 1
    if (-not $src) { throw "Could not find _unpacked/marketing in the downloaded archive." }

    New-Item -ItemType Directory -Force -Path $dest | Out-Null
    Copy-Item -Recurse -Force (Join-Path $src.FullName '_unpacked\marketing\*') $dest

    $versionFile = Join-Path $dest 'VERSION'
    $version = if (Test-Path $versionFile) { (Get-Content $versionFile -Raw).Trim() } else { 'unversioned (pre-1.8.0)' }
    Write-Host "Installed marketing skill v$version ($ref) to $dest"
    Write-Host "Restart Claude Code (or start a new session) to pick it up."
}
finally {
    Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
}
