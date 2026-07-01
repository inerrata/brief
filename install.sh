#!/usr/bin/env bash
# Installs the marketing skill into ~/.claude/skills/marketing for Claude Code.
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/inerrata/brief/main/install.sh | bash
#     -> installs the LATEST RELEASE (recommended)
#   curl -fsSL .../install.sh | bash -s -- --ref v1.7.0
#     -> installs a pinned version
#   curl -fsSL .../install.sh | bash -s -- --ref main
#     -> tracks main (unreleased)
#   BRIEF_REF=v1.7.0 also works instead of --ref.
set -euo pipefail

REPO="inerrata/brief"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}/marketing"
REF="${BRIEF_REF:-}"

while [ $# -gt 0 ]; do
  case "$1" in
    --ref) REF="$2"; shift 2 ;;
    *) echo "unknown option: $1 (supported: --ref <tag|branch>)" >&2; exit 1 ;;
  esac
done

if [ -z "$REF" ]; then
  # Default to the latest release tag; fall back to main if the API is unreachable.
  REF="$(curl -fsSL "https://api.github.com/repos/$REPO/releases/latest" 2>/dev/null \
        | grep -o '"tag_name": *"[^"]*"' | head -n 1 | cut -d'"' -f4 || true)"
  REF="${REF:-main}"
fi

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "Downloading $REPO @ $REF ..."
curl -fsSL "https://codeload.github.com/$REPO/tar.gz/$REF" | tar -xz -C "$TMP"

SRC="$(find "$TMP" -maxdepth 3 -type d -path '*/_unpacked/marketing' | head -n 1)"
if [ -z "$SRC" ]; then
  echo "error: could not find _unpacked/marketing in the downloaded archive" >&2
  exit 1
fi

mkdir -p "$DEST"
cp -R "$SRC"/. "$DEST"/

VERSION="$(cat "$DEST/VERSION" 2>/dev/null || echo "unversioned (pre-1.8.0)")"
echo "Installed marketing skill v$VERSION ($REF) to $DEST"
echo "Restart Claude Code (or start a new session) to pick it up."
