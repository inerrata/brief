#!/usr/bin/env python3
"""Generate format adapters from the skill source — do not edit dist/ by hand.

Emits, from _unpacked/marketing/SKILL.md:
  dist/AGENTS.md    — for Codex CLI (AGENTS.md) and Gemini CLI (rename to GEMINI.md)
  dist/.cursorrules — for Cursor

Both adapters are the skill's routing layer with reference paths rewritten to
`marketing/references/...`, so the install is: copy the adapter file to your
project root + copy `_unpacked/marketing/` into your project as `marketing/`.
The agent then lazy-reads the same reference modules Claude Code does —
progressive disclosure preserved, single source of truth preserved.

Output is deterministic (no timestamps/versions) so CI can rebuild and fail on
any drift between SKILL.md and the committed dist/ files.

Usage: python build/build_adapters.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_MD = ROOT / "_unpacked" / "marketing" / "SKILL.md"
DIST = ROOT / "dist"


def parse_skill():
    text = SKILL_MD.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise SystemExit("could not split SKILL.md frontmatter")
    front, body = m.groups()
    dm = re.search(r"^description: >\n(.*)", front, re.S | re.M)
    if not dm:
        raise SystemExit("could not parse description from frontmatter")
    description = " ".join(ln.strip() for ln in dm.group(1).splitlines() if ln.strip())
    # references live at marketing/references/ relative to the user's project root
    body = body.replace("references/", "marketing/references/")
    body = body.replace("`references/`", "`marketing/references/`")
    return description, body.strip()


HEADER = """\
<!-- GENERATED FILE — do not edit. Source: _unpacked/marketing/SKILL.md
     Regenerate with: python build/build_adapters.py
     From: https://github.com/inerrata/brief -->

# Marketing skill ({target})

## Setup

1. Copy this file into your project root as **{filename}**.
2. Copy the `_unpacked/marketing/` folder from https://github.com/inerrata/brief
   into your project as **`marketing/`** (so `marketing/references/*.md` exist).
   The instructions below lazy-load those reference files only when a task needs
   them — the same progressive disclosure the skill uses in Claude Code.

## When these instructions apply

{description}

For any such task, follow the instructions below. For tasks that have nothing to
do with marketing, ignore this file entirely.

---

"""


def main():
    description, body = parse_skill()
    DIST.mkdir(exist_ok=True)

    agents = HEADER.format(
        target="Codex CLI / Gemini CLI adapter",
        filename="AGENTS.md (Codex CLI) or GEMINI.md (Gemini CLI)",
        description=description,
    ) + body + "\n"
    (DIST / "AGENTS.md").write_text(agents, encoding="utf-8", newline="\n")

    cursor = HEADER.format(
        target="Cursor adapter",
        filename=".cursorrules (or .cursor/rules/marketing.mdc)",
        description=description,
    ) + body + "\n"
    (DIST / ".cursorrules").write_text(cursor, encoding="utf-8", newline="\n")

    print(f"wrote dist/AGENTS.md ({len(agents)} chars) and dist/.cursorrules ({len(cursor)} chars)")


if __name__ == "__main__":
    main()
