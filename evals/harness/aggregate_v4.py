#!/usr/bin/env python3
"""Aggregate v3 grading into benchmarks/benchmark-v4-channels.json + a
markdown table on stdout. Run after every run has grading.json in both arms.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
V3 = HERE.parent / "results" / "v4"
OUT_JSON = HERE.parent.parent / "benchmarks" / "benchmark-v4-channels.json"


def load(p):
    # utf-8-sig tolerates the BOM some subagents prepend to trigger_decision.json
    return json.loads(p.read_text(encoding="utf-8-sig"))


def main():
    rows = []
    for ed in sorted(V3.glob("eval-*"), key=lambda p: int(p.name.split("-")[1])):
        meta = load(ed / "eval_metadata.json")
        row = {"id": meta["id"], "name": meta["name"], "module": meta["module"],
               "type": meta["type"]}
        for arm in ("with_skill", "without_skill"):
            g = ed / arm / "run-1" / "grading.json"
            if g.exists():
                s = load(g)["summary"]
                row[arm] = {"passed": s["passed"], "total": s["total"],
                            "pass_rate": round(s["pass_rate"], 3)}
            else:
                row[arm] = None
        t = ed / "with_skill" / "run-1" / "outputs" / "trigger_decision.json"
        row["triggered"] = load(t)["triggered"] if t.exists() else None
        rows.append(row)

    def agg(arm):
        done = [r for r in rows if r[arm]]
        p = sum(r[arm]["passed"] for r in done)
        t = sum(r[arm]["total"] for r in done)
        m = sum(r[arm]["pass_rate"] for r in done) / len(done) if done else 0
        return {"assertions_passed": p, "assertions_total": t,
                "micro_pass_rate": round(p / t, 4) if t else 0,
                "macro_mean_eval_score": round(m, 4), "evals": len(done)}

    result = {"set": "evals-v4.json", "runs_per_arm": 1,
              "with_skill": agg("with_skill"),
              "without_skill": agg("without_skill"), "per_eval": rows}
    OUT_JSON.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print(f"with_skill:    {result['with_skill']}")
    print(f"without_skill: {result['without_skill']}")
    print()
    print("| # | Eval | Type | With | Base | Trig |")
    print("|---|---|---|:--:|:--:|:--:|")
    for r in rows:
        w = f"{r['with_skill']['pass_rate']:.2f}" if r["with_skill"] else "—"
        b = f"{r['without_skill']['pass_rate']:.2f}" if r["without_skill"] else "—"
        trig = {True: "Y", False: "N", None: "-"}[r["triggered"]]
        print(f"| {r['id']} | {r['name']} | {r['type']} | {w} | {b} | {trig} |")


if __name__ == "__main__":
    main()
