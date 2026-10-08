# ==========================================================
# Sync Skills from Global Config into Repository
# ==========================================================

param (
    [string[]]$SkillNames = @()
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$LocalSkillsDir = Join-Path $RepoRoot "skills"
$GlobalSkillsDir = Join-Path $env:USERPROFILE ".gemini\config\skills"

if (-not (Test-Path $GlobalSkillsDir)) {
    Write-Error "Global skills directory not found at '$GlobalSkillsDir'."
    exit 1
}

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  🔄 Antigravity Skills Global Sync" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "[Source] $GlobalSkillsDir" -ForegroundColor Gray
Write-Host "[Target] $LocalSkillsDir`n" -ForegroundColor Gray

# If specific skills requested, sync only those; otherwise sync existing repo skills from global
$Targets = if ($SkillNames.Count -gt 0) {
    $SkillNames
} else {
    Get-ChildItem -Path $LocalSkillsDir -Directory | Select-Object -ExpandProperty Name
}

foreach ($Name in $Targets) {
    $GlobalPath = Join-Path $GlobalSkillsDir $Name
    $LocalPath = Join-Path $LocalSkillsDir $Name

    if (Test-Path $GlobalPath) {
        Copy-Item -Path $GlobalPath -Destination $LocalSkillsDir -Recurse -Force
        Write-Host "  ✔ Synced from global: $Name" -ForegroundColor Green
    } else {
        Write-Host "  ⚠ Not found in global: $Name" -ForegroundColor Yellow
    }
}

Write-Host "`n🎉 Sync complete!`n" -ForegroundColor Cyan
