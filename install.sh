#!/usr/bin/env bash
# Installs the marketing skill into ~/.claude/skills/marketing for Claude Code.
# Usage: curl -fsSL https://raw.githubusercontent.com/inerrata/brief/main/install.sh | bash
set -euo pipefail

REPO="inerrata/brief"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}/marketing"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "Downloading $REPO ..."
curl -fsSL "https://codeload.github.com/$REPO/tar.gz/refs/heads/main" | tar -xz -C "$TMP"

SRC="$(find "$TMP" -maxdepth 2 -type d -path '*/_unpacked/marketing' | head -n 1)"
if [ -z "$SRC" ]; then
  echo "error: could not find _unpacked/marketing in the downloaded archive" >&2
  exit 1
fi

mkdir -p "$DEST"
cp -R "$SRC"/. "$DEST"/
echo "Installed marketing skill to $DEST"
echo "Restart Claude Code (or start a new session) to pick it up."
