#!/usr/bin/env bash
# ==========================================================
# Antigravity / Gemini Skills Installer (macOS & Linux)
# ==========================================================

set -e

TARGET_MODE="${1:-global}" # Options: "global", "local"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
SOURCE_SKILLS_DIR="$REPO_ROOT/skills"

if [ ! -d "$SOURCE_SKILLS_DIR" ]; then
    echo "Error: 'skills' directory not found in '$REPO_ROOT'." >&2
    exit 1
fi

echo "=========================================="
echo "  ⚡ Antigravity AI Skills Installer"
echo "=========================================="

if [ "$TARGET_MODE" = "global" ]; then
    DESTINATION_DIR="$HOME/.gemini/config/skills"
    echo "[Mode] Global Installation (Antigravity & Gemini CLI)"
    echo "[Target Directory] $DESTINATION_DIR"
elif [ "$TARGET_MODE" = "local" ]; then
    DESTINATION_DIR="$(pwd)/.agents/skills"
    echo "[Mode] Local Project Installation (.agents/skills)"
    echo "[Target Directory] $DESTINATION_DIR"
else
    echo "Invalid TARGET_MODE. Supported modes: 'global' or 'local'." >&2
    exit 1
fi

mkdir -p "$DESTINATION_DIR"

echo ""
echo "Deploying skills..."
for skill_path in "$SOURCE_SKILLS_DIR"/*; do
    if [ -d "$skill_path" ]; then
        skill_name="$(basename "$skill_path")"
        cp -R "$skill_path" "$DESTINATION_DIR/"
        echo "  ✔ Installed: $skill_name"
    fi
done

echo ""
echo "🎉 Successfully installed skills into:"
echo "   $DESTINATION_DIR"
echo ""
