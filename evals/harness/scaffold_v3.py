#!/usr/bin/env python3
"""Scaffold the v3 eval run: targeted evals for the agentic-gates / brand.md /
product-marketing / specs release (commit dd1df6b).

Layout per eval (1x run, matching the v2 method):
  results/v3/eval-<N>/
    eval_metadata.json
    with_skill/run-1/    {prompt.txt, project/?, outputs/}
    without_skill/run-1/ {prompt.txt, project/?, outputs/}

The with_skill description is read live from the skill's frontmatter so the
harness always presents the description users actually see.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
EVALS_DIR = HERE.parent
REPO = EVALS_DIR.parent
SKILL_DIR = REPO / "_unpacked" / "marketing"
SKILL_MD = SKILL_DIR / "SKILL.md"
OUT_ROOT = EVALS_DIR / "results" / "v3"
EVAL_SET = EVALS_DIR / "evals-v3.json"


def read_description() -> str:
    text = SKILL_MD.read_text(encoding="utf-8")
    m = re.search(r"^description: >\n(.*?)^---", text, re.S | re.M)
    if not m:
        raise SystemExit("could not parse description from SKILL.md frontmatter")
    lines = [ln.strip() for ln in m.group(1).splitlines() if ln.strip()]
    return " ".join(lines)


WITH_TMPL = """You are completing ONE evaluation run. Work fully independently. Do NOT ask the requester any clarifying questions back to ME — if the task itself calls for asking the user questions, write those questions into your response file as your deliverable. Make your own decisions otherwise.

A skill is AVAILABLE to you but NOT forced. This is exactly how it would appear in your available-skills list (name + description):

  name: marketing
  description: {description}

The full skill is on disk:
  SKILL.md:    {skill_md}
  references:  {skill_dir}\\references\\  (SKILL.md routes you to the right one)

STEP 1 — Decide for yourself, based only on the user request below and the description above, whether this skill genuinely applies and you would actually consult it. A real assistant consults a skill only when it clearly helps; unrelated, personal, or trivial requests should NOT trigger it. Be honest — do not force it.

STEP 2 — If you decide to use it: read SKILL.md, follow its routing to read the relevant reference file(s), and follow its guidance to complete the request. If you decide NOT to use it: complete the request normally, as you would with no skill available.

STEP 3 — Produce your real, final deliverable to the user (the actual copy/plan/answer, or — where the skill or good judgment says to gather inputs first — the actual clarifying questions you would send).
{files_note}
USER REQUEST:
<<<
{prompt}
>>>

Then save exactly two files (absolute paths):
1. {out}\\response.md  — your full final response to the user, verbatim, exactly as you would send it.
2. {out}\\trigger_decision.json — a JSON object: {{"triggered": true or false, "reason": "<one sentence>", "references_read": ["<filenames you opened>"]}}

Write nothing else to disk. When both files are written, reply with only: DONE triggered=<true|false>
"""

WITHOUT_TMPL = """You are completing ONE task independently. Do NOT ask clarifying questions back to ME — if the task warrants asking the user something, write those questions into your response file as the deliverable. Make reasonable assumptions otherwise and produce a real, finished deliverable.
{files_note}
USER REQUEST:
<<<
{prompt}
>>>

Save your full final response to the user, verbatim, to this absolute path:
  {out}\\response.md

Write nothing else to disk. When done, reply with only: DONE
"""

FILES_NOTE = """
The user's project directory (their cwd) is:
  {proj}
Treat it exactly as you would the project you are working in.
"""


def main():
    evals = json.loads(EVAL_SET.read_text(encoding="utf-8"))
    description = read_description()
    count = 0
    for ev in evals:
        ed = OUT_ROOT / f"eval-{ev['id']}"
        ed.mkdir(parents=True, exist_ok=True)
        (ed / "eval_metadata.json").write_text(
            json.dumps(ev, indent=2), encoding="utf-8")
        for arm in ("with_skill", "without_skill"):
            rd = ed / arm / "run-1"
            out = (rd / "outputs").resolve()
            out.mkdir(parents=True, exist_ok=True)
            files_note = ""
            if ev.get("files"):
                proj = (rd / "project").resolve()
                for f in ev["files"]:
                    rel = Path(f["path"])
                    rel = Path(*rel.parts[1:]) if rel.parts[0] == "project" else rel
                    dest = proj / rel
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_text(f["content"], encoding="utf-8")
                files_note = FILES_NOTE.format(proj=proj)
            if arm == "with_skill":
                text = WITH_TMPL.format(
                    description=description, skill_md=SKILL_MD,
                    skill_dir=SKILL_DIR, prompt=ev["prompt"],
                    out=out, files_note=files_note)
            else:
                text = WITHOUT_TMPL.format(
                    prompt=ev["prompt"], out=out, files_note=files_note)
            (rd / "prompt.txt").write_text(text, encoding="utf-8")
            count += 1
    print(f"Scaffolded {len(evals)} evals, {count} runs under {OUT_ROOT}")


if __name__ == "__main__":
    main()
