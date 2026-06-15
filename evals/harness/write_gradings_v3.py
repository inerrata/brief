#!/usr/bin/env python3
"""Write grading.json for every v3 run from hand-graded verdicts, then the
aggregator can compile them. Verdicts below are the reviewer's per-assertion
judgments from reading each response.md against its evals-v3.json assertions.

Each entry: list of (passed, evidence) in the SAME order as the eval's
assertions[] in evals-v3.json.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
V3 = HERE.parent / "results" / "v3"
EVAL_SET = HERE.parent / "evals-v3.json"

# (eval_id, arm) -> list of (passed:bool, evidence:str), assertion-order
G = {
    (1, "with_skill"): [
        (True, "Delivers finished release notes for v2.3."),
        (True, "Breaking /v1 API removal is the first section, '⚠️ Breaking change — action required'."),
        (True, "Sync race condition -> 'edits made on two devices at once are no longer dropped'; streaming -> 'exports no longer time out on large workspaces'."),
        (True, "Logging upgrade explicitly dropped as having no user-visible effect."),
        (True, "No 'improved performance'/'various fixes' filler; each line is specific."),
    ],
    (1, "without_skill"): [
        (True, "Delivers finished release notes."),
        (True, "'Action required: legacy v1 Tasks API removed' is the first content section."),
        (True, "Sync and streaming-export items translated to user outcomes."),
        (True, "Logging upgrade demoted to an 'Under the hood / no visible changes' note."),
        (True, "Each item is specific; intro is mildly fluffy but no vague filler items."),
    ],
    (2, "with_skill"): [
        (True, "Structured, scannable battle card with labeled sections."),
        (True, "'Where they win' names brand/trust, breadth, ecosystem lock-in honestly."),
        (True, "All win claims use [BRACKET] placeholders with an explicit no-fabrication note."),
        (True, "Objection/response table covers price and 'we already use QuickBooks'."),
        (True, "Landmines section with plant-questions for reps."),
        (True, "Card body is one dense page; sharpening questions sit after the card."),
    ],
    (2, "without_skill"): [
        (True, "Structured battle card."),
        (True, "'Where QuickBooks Is Strong' section is honest."),
        (True, "Proof points use placeholders; no fabricated stats."),
        (True, "Objection-handling table present."),
        (True, "Landmines-to-plant section present."),
        (False, "Sprawls well past one page: 9 numbered sections plus a 30-second pitch, discovery questions, and traps-to-avoid."),
    ],
    (3, "with_skill"): [
        (True, "Plain peer tone; explicitly cuts 'powerful/seamless/effortless'."),
        (True, "Shows the three CLI commands and what each does."),
        (True, "'What it's not' paragraph: not a migration tool, Postgres-only, schema-not-data."),
        (True, "Claims are concrete (CI non-zero exit) not superlative."),
        (True, "First-person Show HN with feedback ask and first-comment prep."),
    ],
    (3, "without_skill"): [
        (True, "No hype words; explicitly avoids 'revolutionary/effortless'."),
        (True, "Concrete sample diff output and command example."),
        (True, "States read-only/no-data limitation and lists objects still on the roadmap."),
        (True, "Specific and demonstrable, not superlative."),
        (True, "Reads as a Show HN first comment with targeted feedback asks."),
    ],
    (4, "with_skill"): [
        (True, "Recommends 'Monday Brief' (descriptive) over PulseIQ with reasoning."),
        (True, "Explicit criteria: repeat test, describe test, crowding test, say-aloud."),
        (True, "Many distinct options across descriptive/cadence/delivery/synthesis angles."),
        (True, "Notes branding is justified if real 'Pulse' brand equity exists."),
    ],
    (4, "without_skill"): [
        (True, "Recommends 'Monday Brief'/clear naming over PulseIQ; drop the IQ cliche."),
        (True, "Explicit criteria: descriptive-vs-evocative, say-aloud, trademark, truth-in-naming."),
        (True, "Three tiers of distinct options."),
        (True, "Notes when an evocative/brand name (Compass) is justified."),
    ],
    (5, "with_skill"): [
        (True, "States 30-char headlines and 90-char descriptions."),
        (True, "Up to 15 headlines, up to 4 descriptions."),
        (True, "Notes Google mixes/matches so each headline must stand alone; pin sparingly."),
        (True, "Concise table + tips matching the quick factual question."),
    ],
    (5, "without_skill"): [
        (True, "States 30/90 char limits correctly."),
        (True, "Up to 15 headlines, up to 4 descriptions (plus minimums)."),
        (True, "Notes mix-and-match, standalone headlines, pinning trade-off."),
        (True, "Tabular and direct; slightly more verbose but on-point."),
    ],
    (6, "with_skill"): [
        (True, "Lead line 'We just raised $2.4M...' (~76 chars) lands the raise before truncation."),
        (True, "Explicitly explains the ~140/210 'see more' cutoff and writes to it."),
        (True, "Ready-to-post LinkedIn post."),
        (True, "Uses $2.4M and Foundry Capital; everything else is bracketed, nothing invented."),
    ],
    (6, "without_skill"): [
        (True, "'We raised $2.4M.' is the first line, before the cutoff."),
        (True, "Explains the ~140-210 char cutoff and front-loads accordingly."),
        (True, "Ready-to-post LinkedIn post."),
        (True, "Uses the given facts; placeholders for the rest, nothing fabricated."),
    ],
    (7, "with_skill"): [
        (True, "Refuses to invent the page; says it won't critique its own guesses."),
        (True, "Reports it tried to load the URL and the domain didn't resolve, then asks for screenshot/paste/working URL."),
        (True, "Asks for buyer, the one target action, and where the funnel leaks."),
        (True, "Option B is explicitly labeled a generic self-audit checklist, with a real audit requiring the real page."),
    ],
    (7, "without_skill"): [
        (True, "Does not fabricate the page contents."),
        (True, "Reports a DNS lookup found no A record, then requests URL/paste/screenshots."),
        (True, "Asks for funnel numbers, traffic source, product/price, and conversion definition."),
        (True, "Framework explicitly labeled as a self-run checklist pending the real asset."),
    ],
    (8, "with_skill"): [
        (True, "Opens 'I pulled up landing-page.md in your project and audited it' — reads the real file, no paste request."),
        (True, "Quotes the real headline, subhead, the three buttons, and the feature list."),
        (True, "Flags all real weaknesses: vague superlative headline, buzzword subhead, three competing CTAs, features-not-benefits, no proof."),
        (True, "Prioritized fixes with a rewritten hero, not just labels."),
        (True, "Unknowns left as marked placeholders; no invented content."),
    ],
    (8, "without_skill"): [
        (True, "'I read your current copy (landing-page.md)' — locates and reads the file itself."),
        (True, "Quotes the real headline, subhead, buttons, and features line by line."),
        (True, "Identifies the same real weaknesses present in the file."),
        (True, "Prioritized fixes plus a rewritten copy template."),
        (True, "Uses bracketed placeholders for unknowns; nothing invented."),
    ],
    (9, "with_skill"): [
        (True, "Delivers the hero (headline/subhead/CTA) immediately, no gating questions."),
        (True, "Uses the real 11-hours stat with sourcing (n=142, 2025 survey) in a proof line."),
        (True, "Voice is plainspoken/warm; no 'leverage'/'solutions', not corporate."),
        (False, "Does NOT offer to save the standing brand facts as a brand.md profile — the skill's create-brand.md offer did not fire."),
        (True, "Headline is outcome-led and specific to restaurant owners."),
    ],
    (9, "without_skill"): [
        (True, "Delivers the hero immediately."),
        (True, "Uses the 11-hours stat with its source."),
        (True, "Plainspoken/warm voice; avoids the banned words."),
        (False, "No brand.md offer (baseline has no concept of one)."),
        (True, "Outcome-led, restaurant-specific headline."),
    ],
    (10, "with_skill"): [
        (True, "Reads the project's brand.md (Kindling); output is built from its contents."),
        (True, "Does not re-ask audience/voice/goal that brand.md already answers."),
        (True, "Uses the real 52%-vs-21% open-rate stat and the Mia Torres testimonial."),
        (True, "Warm/bookish/playful; never says 'blast', no exclamation pileups."),
        (True, "Single CTA driving the stated free-to-paid quarterly goal."),
    ],
    (10, "without_skill"): [
        (True, "Reads brand.md from the cwd and uses Kindling's details."),
        (True, "Does not re-ask answered scoping questions."),
        (True, "Uses the 52% stat and the Mia Torres quote."),
        (True, "Warm/bookish/playful voice; avoids 'blast'."),
        (True, "Single upgrade CTA aimed at free-to-paid."),
    ],
    (11, "with_skill"): [
        (True, "Asks three sharp scoping questions before committing to a final statement."),
        (True, "Q1 targets narrow audience; Q2/Q3 target differentiator and the real alternative."),
        (True, "No finished statement on guesses: the optional draft is explicitly 'provisional', a 'placeholder to react to, not a finished answer', with product name and proof bracketed."),
        (True, "Three concise questions, not an open-ended interrogation."),
    ],
    (11, "without_skill"): [
        (False, "Delivers a finished 'Primary positioning statement' first; questions come only afterward."),
        (True, "Does include audience/differentiator/competitor questions (but after the statement)."),
        (False, "Outputs a finished positioning statement built on guessed audience/category/differentiation in this turn."),
        (True, "The trailing questions are concise."),
    ],
    (12, "with_skill"): [
        (True, "trigger_decision.triggered = false — correctly does not fire on a commit-message task."),
        (True, "Provides a sensible Conventional Commits message for the refactor."),
        (True, "No marketing frameworks, briefs, or scoping questions."),
    ],
    (12, "without_skill"): [
        (True, "No skill involved; output is a plain commit message."),
        (True, "Sensible Conventional Commits message."),
        (True, "No marketing content."),
    ],
}


def main():
    evals = {e["id"]: e for e in json.loads(EVAL_SET.read_text(encoding="utf-8"))}
    written = 0
    for (eid, arm), verdicts in G.items():
        assertions = evals[eid]["assertions"]
        assert len(verdicts) == len(assertions), f"eval {eid} {arm}: {len(verdicts)} verdicts vs {len(assertions)} assertions"
        exps = [{"text": a, "passed": p, "evidence": ev}
                for a, (p, ev) in zip(assertions, verdicts)]
        passed = sum(1 for _, (p, _) in zip(assertions, verdicts) if p)
        total = len(assertions)
        out = {"expectations": exps,
               "summary": {"passed": passed, "failed": total - passed,
                           "total": total, "pass_rate": round(passed / total, 4)}}
        dest = V3 / f"eval-{eid}" / arm / "run-1" / "grading.json"
        dest.write_text(json.dumps(out, indent=2), encoding="utf-8")
        written += 1
    print(f"Wrote {written} grading.json files")


if __name__ == "__main__":
    main()
