#!/usr/bin/env python3
"""Deterministic (bias-free) eval checks — no LLM grader.

Two layers, both checkable by code against the committed eval evidence:

1. TRIGGERING (zero-authoring, derived from each eval's `type`): every eval that
   should fire must have with_skill trigger_decision.triggered == true; every
   `should_not_trigger` eval must be false. This is a pure regression guard over
   every eval in v3/v4/v5.

2. CONTENT (authored in deterministic_spec.json): structural string/length checks
   on the with_skill response — banned-buzzword absence, refusal+still-delivered
   on honesty/compliance probes, presence of an assumptions line, etc. These grade
   *structure and triggering*, NOT quality — that's the point: they're objective.

Exit code is non-zero if any check fails, so CI can gate on it. The checker reads
committed outputs; it does not re-run any model.

Usage:  python evals/harness/deterministic_checks.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
EVALS_DIR = HERE.parent
RESULTS = EVALS_DIR / "results"
SPEC = EVALS_DIR / "deterministic_spec.json"
SETS = ["v3", "v4", "v5"]


def read_json(p):
    return json.loads(p.read_text(encoding="utf-8-sig"))


def read_text(p):
    return p.read_text(encoding="utf-8-sig") if p.exists() else ""


# ---- content check primitives (each returns (ok, detail)) -------------------

def c_contains_any_i(text, needles):
    low = text.lower()
    hit = [n for n in needles if n.lower() in low]
    return (bool(hit), f"found {hit}" if hit else f"none of {needles} present")


def c_not_contains_i(text, needles):
    low = text.lower()
    hit = [n for n in needles if n.lower() in low]
    return (not hit, f"present (should be absent): {hit}" if hit else "clean")


def c_min_words(text, n):
    w = len(text.split())
    return (w >= n, f"{w} words (min {n})")


def c_matches(text, pattern):
    return (bool(re.search(pattern, text, re.I | re.M)), f"/{pattern}/")


CONTENT = {
    "contains_any_i": c_contains_any_i,
    "not_contains_i": c_not_contains_i,
    "min_words": c_min_words,
    "matches": c_matches,
}


def run():
    spec = read_json(SPEC) if SPEC.exists() else {}
    passed = failed = 0
    fails = []

    for s in SETS:
        sdir = RESULTS / s
        if not sdir.exists():
            continue
        for ed in sorted(sdir.glob("eval-*"), key=lambda p: int(p.name.split("-")[1])):
            meta = read_json(ed / "eval_metadata.json")
            eid = str(meta["id"])
            expect_trigger = meta.get("type") != "should_not_trigger"

            # Layer 1 — triggering
            tfile = ed / "with_skill" / "run-1" / "outputs" / "trigger_decision.json"
            if tfile.exists():
                got = read_json(tfile).get("triggered")
                ok = (got is expect_trigger)
                passed += ok
                failed += (not ok)
                if not ok:
                    fails.append(f"{s} eval-{eid} TRIGGER: expected {expect_trigger}, got {got}")
            else:
                # negative controls have no trigger file only if they never ran with_skill;
                # all our with_skill arms write one, so a missing file is a real failure.
                failed += 1
                fails.append(f"{s} eval-{eid} TRIGGER: trigger_decision.json missing")

            # Layer 2 — content checks (authored)
            resp = read_text(ed / "with_skill" / "run-1" / "outputs" / "response.md")
            for chk in spec.get(s, {}).get(eid, []):
                name = chk.get("name", "?")
                ran = False
                for key, fn in CONTENT.items():
                    if key in chk:
                        ok, detail = fn(resp, chk[key])
                        ran = True
                        passed += ok
                        failed += (not ok)
                        if not ok:
                            fails.append(f"{s} eval-{eid} CONTENT [{name}]: {detail}")
                if not ran:
                    failed += 1
                    fails.append(f"{s} eval-{eid} CONTENT [{name}]: no known check key in {list(chk)}")

    total = passed + failed
    print(f"Deterministic checks: {passed}/{total} passed across {', '.join(SETS)}")
    if fails:
        print("\nFAILURES:")
        for f in fails:
            print("  -", f)
        return 1
    print("All deterministic checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(run())
