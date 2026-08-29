# ==========================================================
# Antigravity / Gemini Skills Installer (Windows PowerShell)
# ==========================================================

param (
    [string]$TargetMode = "global" # Options: "global", "local"
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$SourceSkillsDir = Join-Path $RepoRoot "skills"

if (-not (Test-Path $SourceSkillsDir)) {
    Write-Error "Error: 'skills' directory not found in '$RepoRoot'."
    exit 1
}

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  ⚡ Antigravity AI Skills Installer" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

if ($TargetMode -eq "global") {
    $DestinationDir = Join-Path $env:USERPROFILE ".gemini\config\skills"
    Write-Host "[Mode] Global Installation (Antigravity & Gemini CLI)" -ForegroundColor Yellow
    Write-Host "[Target Directory] $DestinationDir" -ForegroundColor Gray
} elseif ($TargetMode -eq "local") {
    $DestinationDir = Join-Path (Get-Location) ".agents\skills"
    Write-Host "[Mode] Local Project Installation (.agents/skills)" -ForegroundColor Yellow
    Write-Host "[Target Directory] $DestinationDir" -ForegroundColor Gray
} else {
    Write-Error "Invalid TargetMode. Supported modes: 'global' or 'local'."
    exit 1
}

# Ensure destination exists
if (-not (Test-Path $DestinationDir)) {
    New-Item -ItemType Directory -Path $DestinationDir -Force | Out-Null
}

$SkillFolders = Get-ChildItem -Path $SourceSkillsDir -Directory

Write-Host "`nDeploying skills..." -ForegroundColor Green
foreach ($Skill in $SkillFolders) {
    $DestSkillPath = Join-Path $DestinationDir $Skill.Name
    Copy-Item -Path $Skill.FullName -Destination $DestSkillPath -Recurse -Force
    Write-Host "  ✔ Installed: $($Skill.Name)" -ForegroundColor Green
}

Write-Host "`n🎉 Successfully installed $($SkillFolders.Count) skills into:" -ForegroundColor Cyan
Write-Host "   $DestinationDir`n" -ForegroundColor White
