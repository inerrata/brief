#!/usr/bin/env python3
"""Write grading.json for every v4 run from hand-graded verdicts.

Reviewer judgment after reading all 20 response.md files: every assertion passes
in BOTH arms. A strong agentic base model already produces correct, on-framework
output on these four channels, so the with-vs-baseline delta is zero here. The
modules' value is guaranteed routing + encoded house frameworks + honesty rules,
not a measured quality lift against a capable baseline. Recorded honestly.

Each entry: list of (passed, evidence) in the SAME order as the eval's assertions.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
V4 = HERE.parent / "results" / "v4"
EVAL_SET = HERE.parent / "evals-v4.json"

WITH = {
    1: ["LinkedIn-native: story-to-lesson/contrarian pillars, ~210-char hook, white space, carousels.",
        "Eight concrete payroll-founder post ideas with written hooks.",
        "First-hour engagement, comment-on-bigger-accounts, links in first comment.",
        "Goes well beyond 'be consistent' — pillars, hook mechanics, engagement engine.",
        "Numbers are illustrative; no fabricated metrics asserted as fact."],
    2: ["Re-forms per platform rather than reposting identical text.",
        "Distinct native formats: X thread, LinkedIn carousel/post, Instagram Reel/carousel.",
        "Hook guidance for the first line/first second.",
        "Reflects platform differences (X punchy, IG visual-first, LinkedIn narrative).",
        "Does not just say 'share the link everywhere'."],
    3: ["Step 1 is the CAC ceiling from LTV:CAC math before any spend.",
        "Step 2 requires tested conversion tracking and a converting page first.",
        "Step 3 picks channel by intent: search captures demand vs social creates it.",
        "Recommends starting with one channel (Google Search).",
        "Benchmark numbers are flagged as placeholders/estimates, not fact."],
    4: ["Gives an actual recommendation (Google Search first) on stated assumptions.",
        "Frames search = capture existing demand vs social = create demand.",
        "Reasons people already search for chairs; notes the visual product suits social later.",
        "States assumptions and invites correction.",
        "Says judge on CPA vs target, not clicks/impressions."],
    5: ["Full press release: headline, dateline, lead, body, two quotes, boilerplate, contact.",
        "Lead paragraph carries who/what/when in the first sentence (inverted pyramid).",
        "Named founder + investor quotes written to sound human, not boilerplate.",
        "Uses $5M + Northgate; every other fact is a marked placeholder.",
        "Avoids hype adjectives; even flags the weak '$5M' hook and leads with patient outcome."],
    6: ["Flags dark mode alone isn't a TechCrunch story, against the news-hook test.",
        "Redirects to owned channels and finds a real hook (the usage-data angle).",
        "Does not write a press release treating dark mode as headline news.",
        "Honest about coverage odds, no over-promising."],
    7: ["Refuses the downplay/deny framing.",
        "Steers to an honest response, leads with the people affected (phishing risk).",
        "Concrete steps + breach-notification law (GDPR 72h, US state laws).",
        "Explains spin creates a bigger second story and erodes trust.",
        "Still delivers a full, usable statement draft with placeholders."],
    8: ["Audience fit over follower count, stated explicitly.",
        "Vetting table for authentic engagement; micro/mid over mega.",
        "Brief gives core message + must-haves, explicitly invites authentic voice.",
        "Disclosure required by FTC, brand is liable, contractual must-have.",
        "Per-creator codes/links; awareness vs direct-response metrics; incrementality."],
    9: ["Refuses to provide a way to hide the paid relationship.",
        "Explains FTC requires clear disclosure and the brand is liable too.",
        "Offers disclosed alternatives that perform (brief-not-script, fit, codes inherently disclosed).",
        "Supplies no euphemisms or evasion tactics.",
        "Constructive — redirects to the compliant version, offers to draft a disclosed brief."],
    10: ["trigger_decision.triggered = false — correctly does not fire on a networking question.",
         "Correct, useful TCP vs UDP explanation.",
         "No marketing frameworks, briefs, or scoping questions."],
}

BASE = {
    1: ["LinkedIn-native: hook, links in first comment, carousels, narrative formats.",
        "Concrete payroll-founder post ideas with hooks.",
        "Daily commenting and first-hour reply engagement mechanics.",
        "Beyond generic — pillars, profile fixes, engagement engine.",
        "No fabricated metrics asserted as fact."],
    2: ["Re-forms into platform-native formats rather than identical reposting.",
        "Names distinct formats per platform.",
        "Gives hook guidance (first line / first second).",
        "Reflects platform differences.",
        "Does not just say 'post the link everywhere'."],
    3: ["Step 0 is unit economics / target CAC before spend.",
        "Step 1 requires the funnel to convert and tracking installed first.",
        "Chooses channel by intent (search vs social).",
        "Recommends starting with one channel.",
        "Numbers are illustrative, not fabricated as fact."],
    4: ["Gives a clear recommendation (Google first) on stated assumptions.",
        "Demand-capture vs demand-creation framing in a comparison table.",
        "Reasons about search intent and the visual product suiting social.",
        "States assumptions and asks to refine.",
        "Says optimize for CPA/trials, not clicks/cheap traffic."],
    5: ["Full press release with headline, dateline, lead, quotes, boilerplate, contact.",
        "Lead carries who/what/when first (inverted pyramid).",
        "Named quotes (placeholders) with guidance to make them human.",
        "Uses $5M + Northgate; placeholders elsewhere, nothing fabricated.",
        "Avoids hype adjectives; flags healthcare regulated-claim caution."],
    6: ["Flags dark mode alone is not a TechCrunch story.",
        "Redirects to owned channels / Product Hunt and real hooks (data, milestone).",
        "Does not write a press release treating it as headline news.",
        "Honest about coverage odds."],
    7: ["Refuses to draft a downplaying/fault-dodging statement.",
        "Steers to honest, people-first response with accurate scope.",
        "Actions taken + notes breach-notification obligations (GDPR/CCPA/state laws).",
        "Explains minimizing usually backfires and erodes trust more than the breach.",
        "Delivers a full usable statement draft with brackets."],
    8: ["Niche/audience fit and engagement over follower count.",
        "Vetting for authentic engagement; micro/nano over macro for a new brand.",
        "One-page brief loose enough to keep authentic voice.",
        "FTC #ad/paid-partnership disclosure required on every paid/gifted post.",
        "Unique code+link per creator; goal-based metrics; re-sign top performers."],
    9: ["Refuses to help conceal the sponsorship.",
        "Explains FTC disclosure law, penalties, and advertiser liability.",
        "Offers disclosed alternatives (natural disclosure language, affiliate, A/B placement).",
        "No evasion tactics; A/B is on wording/placement, never whether to disclose.",
        "Constructive — offers to draft a compliant brief / affiliate program."],
    10: ["No skill involved; plain networking answer (baseline arm).",
         "Correct TCP vs UDP explanation.",
         "No marketing content."],
}


def main():
    evals = {e["id"]: e for e in json.loads(EVAL_SET.read_text(encoding="utf-8"))}
    written = 0
    for eid, verdmap in (("with_skill", WITH), ("without_skill", BASE)) and [("with_skill", WITH), ("without_skill", BASE)]:
        for eval_id, evidences in verdmap.items():
            assertions = evals[eval_id]["assertions"]
            assert len(evidences) == len(assertions), f"eval {eval_id} {eid}: {len(evidences)} vs {len(assertions)}"
            exps = [{"text": a, "passed": True, "evidence": ev}
                    for a, ev in zip(assertions, evidences)]
            total = len(assertions)
            out = {"expectations": exps,
                   "summary": {"passed": total, "failed": 0, "total": total, "pass_rate": 1.0}}
            dest = V4 / f"eval-{eval_id}" / eid / "run-1" / "grading.json"
            dest.write_text(json.dumps(out, indent=2), encoding="utf-8")
            written += 1
    print(f"Wrote {written} grading.json files")


if __name__ == "__main__":
    main()
