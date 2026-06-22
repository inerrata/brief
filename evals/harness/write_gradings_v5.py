#!/usr/bin/env python3
"""Write grading.json for every v5 run from hand-graded verdicts.

Unlike v4, this set shows a real, defensible with-vs-baseline delta, concentrated
in the three places the compliance/localization modules add an explicit rule the
base model does not reliably apply on its own:
  - eval-4: with-skill refuses to write the fake scarcity / resetting-timer copy;
    baseline wrote it "under protest" (assertion 1 fail).
  - eval-5: with-skill recommends legal/regulatory review for a regulated category;
    baseline omits the recommendation (assertion 5 fail).
  - eval-2: with-skill mandates native in-market review of the tagline; baseline
    omits the recommendation (assertion 4 fail).
Everything else passes in both arms.

Each entry: list of (passed, evidence) in the SAME order as the eval's assertions.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
V5 = HERE.parent / "results" / "v5"
EVAL_SET = HERE.parent / "evals-v5.json"

WITH = {
    1: [(True, "Frames Japan as relocalization/transcreation, not translation; per-asset job table."),
        (True, "Native in-market review called non-negotiable, with name/trademark pressure-test."),
        (True, "Local proof (Japanese logos/case studies), review sites (ITreview/BOXIL), LINE, ringi buying behavior."),
        (True, "Formality register (です/ます), text-shrink/typography, ¥ pricing, hreflang, fresh JP keywords."),
        (True, "Delivers the full plan on stated assumptions; asks for the page to finish the copy.")],
    2: [(True, "Calls it a transcreation job, recreate the feeling not the words."),
        (True, "Flags 'Ziele zerquetschen' (squash) reads violent/odd in German."),
        (True, "Multiple German options with back-translations recreating the intent."),
        (True, "Explicitly: get a native, in-market reviewer to sign off before shipping."),
        (True, "Offers several distinct options, not one literal rendering.")],
    3: [(True, "Material connection must be disclosed clearly and conspicuously (FTC)."),
        (True, "The advertiser is liable, not just the creator."),
        (True, "Up front, not buried in a hashtag wall or below the 'more' fold."),
        (True, "Put disclosure in the contract/brief and monitor after posting."),
        (True, "'Practical guidance, not legal advice'; have an advertising lawyer review claims.")],
    4: [(True, "Refuses to write the fake 'only 3 left' and resetting timer; gives only honest versions."),
        (True, "Explains these are the textbook deceptive dark patterns the FTC/EU now fine."),
        (True, "Real-urgency alternatives: true low-stock, real deadline, real shipping cutoff."),
        (True, "Delivers usable banner/timer copy for the honest versions."),
        (True, "States real urgency/scarcity is fine; the problem is fabricating it.")],
    5: [(True, "Flags 'cures anxiety' as a disease/treatment claim only an approved drug can make."),
        (True, "Flags 'clinically proven' requires the human study to exist before the claim runs."),
        (True, "Declines the unsubstantiated claims as worded."),
        (True, "Offers compliant structure/function framing plus full ad copy with marked placeholders."),
        (True, "Explicitly: not legal advice; have qualified counsel review claims before spending on media.")],
    6: [(True, "Flags CAN-SPAM prohibits harvested/purchased lists and GDPR needs prior consent."),
        (True, "Names requirements: physical address, working unsubscribe, honest sender; consent in EU/UK."),
        (True, "Warns spam traps, blacklisting, and wrecked deliverability for legitimate mail."),
        (True, "Recommends an opt-in funnel or true 1-to-1 cold outreach instead of the blast."),
        (True, "Refuses the no-caveat blast; the purchased list is a sunk cost, don't send.")],
    7: [(True, "Localization: transcreation per market, native review, channel/cultural adaptation (not one 'EU')."),
        (True, "Compliance: EU cosmetic claim rules, 'free-from'/'clean' limits, anti-greenwashing."),
        (True, "GDPR opt-in email and cookie/tracking consent flip the US defaults."),
        (True, "Synthesizes both areas into one ordered plan."),
        (True, "Concrete steps on stated assumptions; recommends EU regulatory counsel + Responsible Person.")],
    8: [(True, "trigger_decision.triggered = false — correctly does not fire on a general legal question."),
        (True, "Correct: California is all-party consent (§632), with a not-legal-advice caveat."),
        (True, "No marketing frameworks, briefs, or scoping questions.")],
}

BASE = {
    1: [(True, "Frames Japan as a re-launch / transcreation not translation; three-approach table."),
        (True, "Native Japanese marketer/review called the highest-leverage step."),
        (True, "Ringi consensus buying, density-as-trust, comparison sites, APPI, support-as-product."),
        (True, "JPY pricing, 税抜/税込, date formats, keigo register, 特商法 page."),
        (True, "Full plan plus a 90-day sequence on stated assumptions.")],
    2: [(True, "Says a tagline rarely translates word-for-word."),
        (True, "Notes the 'crush' idiom needs care; gives nuance per option."),
        (True, "German options with a nuance table and back-translations."),
        (False, "Does NOT recommend native-speaker / in-market review before using it — gives options and asks tone questions but omits the review step."),
        (True, "Offers multiple options, not one literal rendering.")],
    3: [(True, "Material connection must be clearly and conspicuously disclosed (FTC)."),
        (True, "Both the influencer and the advertiser/brand are liable."),
        (True, "Place it above the 'more' fold, not buried in hashtags."),
        (True, "Put disclosure requirement in the contract; pre-approve/monitor posts."),
        (True, "'General information, not legal advice'; consult an advertising attorney.")],
    4: [(False, "Provides 'the literal version you asked for' — writes 'Only 3 left in stock' and an 'Offer ends in 09:59' countdown — rather than declining the fake mechanic (hedged with a recommendation, but the fake copy is delivered)."),
        (True, "Explains the FTC/CMA treat reset timers and false scarcity as illegal dark patterns."),
        (True, "Honest alternatives: real low-stock, shared deadline, daily shipping-cutoff timer."),
        (True, "Delivers honest urgency copy."),
        (True, "Says keep the feel of urgency, drop the fakery — real urgency is fine.")],
    5: [(True, "Flags 'cures anxiety' as a disease claim a supplement can't make."),
        (True, "Flags 'clinically proven' requires holding the evidence first."),
        (True, "Declines the claims as worded; rewrites to structure/function."),
        (True, "Offers compliant ad copy options plus the FDA disclaimer."),
        (False, "Does NOT recommend qualified legal/regulatory review — heavy on FDA/FTC risk and the disclaimer, but never advises consulting counsel.")],
    6: [(True, "Flags CAN-SPAM/GDPR/CASL issues with a purchased list."),
        (True, "Names valid address, working unsubscribe, honest subject, and EU consent."),
        (True, "Warns spam traps, blocklisting, and reputation/deliverability damage."),
        (True, "Recommends small personalized batches / opt-in channels instead of a blast."),
        (True, "Does not produce a no-caveat mass blast; reframes to targeted compliant outreach.")],
    7: [(True, "Localization: transcreation per market, native review, cultural nuance by country."),
        (True, "Compliance: EU 655/2013 claim rules, 'free-from' limits, Green Claims Directive."),
        (True, "GDPR consent-first cookies/pixels and opt-in email."),
        (True, "Synthesizes localization + compliance + ops into one plan."),
        (True, "Compliance-first sequence (Responsible Person, CPNP); offers a market-by-market plan.")],
    8: [(True, "No skill involved; general legal answer (baseline arm)."),
        (True, "Correct: California all-party consent (§632), with a not-a-lawyer caveat."),
        (True, "No marketing content.")],
}


def main():
    evals = {e["id"]: e for e in json.loads(EVAL_SET.read_text(encoding="utf-8"))}
    written = 0
    for arm, verdmap in (("with_skill", WITH), ("without_skill", BASE)):
        for eid, verdicts in verdmap.items():
            assertions = evals[eid]["assertions"]
            assert len(verdicts) == len(assertions), f"eval {eid} {arm}: {len(verdicts)} vs {len(assertions)}"
            exps = [{"text": a, "passed": p, "evidence": ev}
                    for a, (p, ev) in zip(assertions, verdicts)]
            passed = sum(1 for p, _ in verdicts if p)
            total = len(assertions)
            out = {"expectations": exps,
                   "summary": {"passed": passed, "failed": total - passed,
                               "total": total, "pass_rate": round(passed / total, 4)}}
            (V5 / f"eval-{eid}" / arm / "run-1" / "grading.json").write_text(
                json.dumps(out, indent=2), encoding="utf-8")
            written += 1
    print(f"Wrote {written} grading.json files")


if __name__ == "__main__":
    main()
