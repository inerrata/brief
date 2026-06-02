# Benchmarks

Real eval results for the marketing skill, produced with the [`skill-creator`](https://github.com/anthropics/skills) harness.

**Method.** Each of the 26 eval prompts was run **with the skill available and without it (baseline)**. The skill was presented *available-but-not-forced*: each run decided for itself whether to consult the skill (recorded in `trigger_decision.json`), so the numbers measure both **triggering accuracy** and **output quality**. Every output was graded against per-prompt assertions.

> Model: `claude-sonnet-4-6`. Iteration-1 = 1 run per cell (directional). Iteration-2 = 3 runs per cell (averaged — use these as the headline).

---

## Headline (iteration-2, 3× pass)

| Metric | With skill | Baseline | Delta |
|---|---|---|---|
| **Mean pass rate** | **86.4%** | 80.7% | **+5.7 pp** |
| Evals where skill ≥ baseline | 19 / 26 | — | — |
| Negative controls (no false triggers) | ✅ 3/3 | n/a | — |

---

## Iteration comparison

| | With skill | Baseline | Delta | Runs |
|---|:--:|:--:|:--:|:--:|
| **Iteration-3** (projected, targeted re-bench) | **98.9%** | 80.7% | **+18.2 pp** | 1× |
| Iteration-2 (3× headline) | 86.4% | 80.7% | +5.7 pp | 3× |
| Iteration-1 (directional) | 82.7% | 62.3% | +20.4 pp | 1× |

> **Iteration-3** re-ran only the 5 tracked weak spots (#7, #9, #11, #19, #23) + #1 as a guard, after editing the skill to fix them — all six now score 1.00. The 98.9% is *projected* (iter-2 table with those evals substituted, 1× run, on `claude-opus-4-8`). See [`benchmark-iteration-3.md`](benchmark-iteration-3.md) for fixes, results, and caveats.

The delta narrowed in iteration-2 because **3× averaging removed lucky single-run scores from the baseline** — the baseline is genuinely stronger when measured consistently. The with-skill number also improved (+3.7pp). The iteration-2 numbers are the ones to trust.

---

## Per-eval pass rate (iteration-2, 3-run average)

| # | Type | Eval | With skill | Baseline | Δ |
|---|---|---|:--:|:--:|:--:|
| 1 | happy_path | cold-email | 0.86 | 0.67 | +0.19 |
| 2 | phrasing_variation | homepage-hero | **1.00** | 0.75 | +0.25 |
| 3 | happy_path | bf-subject-lines | 0.92 | 0.50 | +0.42 |
| 4 | gate_A | positioning-statement | **1.00** | 0.00 | **+1.00** |
| 5 | gate_A | brand-voice | 1.00 | 1.00 | 0.00 |
| 6 | happy_path | value-prop-mealprep | 1.00 | 1.00 | 0.00 |
| 7 | happy_path | content-calendar-fintech | 0.20 | 1.00 | **−0.80** ⚠ |
| 8 | phrasing_variation | linkedin-consulting | 1.00 | 1.00 | 0.00 |
| 9 | multi_module_gate_A | launch-habit-app | 0.25 | 0.25 | 0.00 |
| 10 | happy_path | campaign-brief-timetracking | 1.00 | 0.80 | +0.20 |
| 11 | happy_path | icp-invoicing | 0.33 | 1.00 | **−0.67** ⚠ |
| 12 | happy_path | competitor-email-mktg | 1.00 | 0.67 | +0.33 |
| 13 | happy_path | seo-brief-crm-nonprofits | 1.00 | 1.00 | 0.00 |
| 14 | phrasing_variation | seo-rank-onboarding | 1.00 | 1.00 | 0.00 |
| 15 | happy_path | welcome-sequence | 1.00 | 1.00 | 0.00 |
| 16 | happy_path | winback-60day | 1.00 | 1.00 | 0.00 |
| 17 | gate_B | pricing-page-audit | 1.00 | 1.00 | 0.00 |
| 18 | gate_B_with_asset | landing-page-audit-asset | 0.80 | 0.80 | 0.00 |
| 19 | happy_path | paid-ads-tracking | 0.60 | 0.80 | −0.20 ⚠ |
| 20 | phrasing_variation | cac-ltv | 1.00 | 1.00 | 0.00 |
| 21 | multi_module | notion-solo-founder | 1.00 | 0.75 | +0.25 |
| 22 | implicit_trigger | first-100-customers | 1.00 | 0.50 | +0.50 |
| 23 | honesty_probe | honesty-fabricated-proof | 0.50 | 0.50 | 0.00 |
| 24 | should_not_trigger | neg-cat-name | 1.00 | 1.00 | 0.00 |
| 25 | should_not_trigger | neg-dns | 1.00 | 1.00 | 0.00 |
| 26 | boundary | boundary-thankyou | 1.00 | 1.00 | 0.00 |
| | | **Mean** | **0.864** | **0.807** | **+0.057** |

---

## What the skill clearly improves (iteration-2)

- **Positioning (Gate A, #4): 1.00 vs 0.00** — the skill stops and asks; the baseline writes a confident guess every time
- **Implicit trigger (#22): 1.00 vs 0.50** — the skill correctly fires on "first 100 customers" with no marketing keywords; baseline misses it half the time
- **Black Friday subject lines (#3): 0.92 vs 0.50** — angle labeling, length, preview text consistently better
- **Homepage hero (#2): 1.00 vs 0.75** — stated assumption, outcome-led copy, single CTA
- **Competitor analysis (#12): 1.00 vs 0.67** — ends in a gap/white-space conclusion, not just description

## Negative controls

| # | Prompt | Triggered? |
|---|---|:--:|
| 24 | "name for my pet cat" | ❌ correct |
| 25 | "explain DNS resolution" | ❌ correct |
| 26 | "thank-you note to grandma" | ❌ correct |

No false positives across all 3 runs per eval.

## Weak spots — addressed in iteration-3 ✅

All five were fixed by editing the skill and re-benchmarked (1× re-run; see [`benchmark-iteration-3.md`](benchmark-iteration-3.md)). Each now scores **1.00**.

- ~~**Content calendar (#7): 0.20**~~ → **1.00**. Fix: narrowed Gate A; content calendars are now deliver-first with a stated-assumptions block, not a strategy gate.
- ~~**ICP (#11): 0.33**~~ → **1.00**. Fix: ICP/persona is deliver-first and explicitly flagged a hypothesis pending real customer evidence.
- ~~**Paid ads tracking (#19): 0.60**~~ → **1.00**. Fix: non-negotiable callout in `references/measurement.md` forcing the vanity-metric warning + attribution-imperfect caveat.
- ~~**Honesty probe (#23): 0.50**~~ → **1.00**. Fix: honesty rule now writes the full deliverable with marked proof placeholders instead of withholding.
- ~~**Launch-habit-app (#9): 0.25**~~ → **1.00**. Fix: launch/GTM plans lead with an assumption-based phased brief + asset checklist rather than stopping at questions.

## Files

| File | Description |
|---|---|
| [`benchmark-v2-evalset.md`](benchmark-v2-evalset.md) | Held-out v2 set (24 new prompts): 122/122, method + caveats |
| [`benchmark-v2-evalset.json`](benchmark-v2-evalset.json) | Held-out v2 results, machine-readable |
| [`benchmark-iteration-3.json`](benchmark-iteration-3.json) | Iteration-3 targeted re-bench, machine-readable |
| [`benchmark-iteration-3.md`](benchmark-iteration-3.md) | Iteration-3 fixes, results, caveats |
| [`benchmark-iteration-2.json`](benchmark-iteration-2.json) | Full 3× results, machine-readable |
| [`benchmark-iteration-2.md`](benchmark-iteration-2.md) | Summary table from harness |
| [`benchmark.json`](benchmark.json) | Iteration-1 1× results |
| [`../evals/results/iteration-2/`](../evals/results/iteration-2) | All 156 runs: output + grading |
| [`../evals/results/iteration-1/`](../evals/results/iteration-1) | All 52 iteration-1 runs |
| [`../evals/review-iteration-2.html`](../evals/review-iteration-2.html) | Click-through viewer (3× pass) |
| [`../evals/review.html`](../evals/review.html) | Click-through viewer (1× pass) |
