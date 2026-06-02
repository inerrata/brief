# Skill Benchmark: marketing — iteration-3 (targeted re-benchmark)

**Model**: claude-opus-4-8
**Date**: 2026-06-02
**Scope**: Re-ran the 5 weak spots tracked after iteration-2 (#7, #9, #11, #19, #23) plus #1 as a regression guard. With-skill arm, 1 run each. Baseline and the untouched 20 evals carry over from iteration-2 (3×).

## Why iteration-3

Iteration-2 flagged five concrete weak spots. This iteration edits the skill to fix them and re-measures just those evals.

| What was wrong (iter-2) | Fix in the skill |
|---|---|
| #7 calendar, #11 ICP, #9 launch — skill **over-gated** and asked questions instead of delivering | Narrowed Gate A to the four single load-bearing statements only; calendars, ICPs, briefs, launch/GTM plans are now **deliver-first** with a stated-assumptions block |
| #11 ICP asserted as fact | ICP/persona must be flagged a **hypothesis pending real customer evidence** |
| #23 honesty — refused to fabricate but wrote **nothing** | Honesty rule now requires writing the full deliverable with **marked proof placeholders** |
| #19 ads — missing vanity-metric + attribution caveats | Added a **non-negotiable callout** to `references/measurement.md` |

## Results (re-run evals)

| # | Eval | iter-2 | iter-3 | Δ |
|---|---|:--:|:--:|:--:|
| 7 | content-calendar-fintech | 0.20 | **1.00** | **+0.80** |
| 9 | launch-habit-app | 0.25 | **1.00** | **+0.75** |
| 11 | icp-invoicing | 0.33 | **1.00** | **+0.67** |
| 23 | honesty-fabricated-proof | 0.50 | **1.00** | **+0.50** |
| 19 | paid-ads-tracking | 0.60 | **1.00** | **+0.40** |
| 1 | cold-email (regression guard) | 0.86 | **1.00** | +0.14 |

Every previously-failing assertion now passes; no regression on the guard.

## Projected suite headline

| Metric | Value |
|---|:--:|
| With-skill mean (projected, 26 evals) | **98.9%** |
| Iteration-2 with-skill mean | 86.4% |
| Baseline mean | 80.7% |

*Projected = iteration-2 with-skill table with the 6 re-run evals substituted; assumes the untouched 20 hold their iteration-2 3× scores.*

## Caveats (read these)

- **1× run**, not the 3× averaging behind the iteration-2 headline.
- Run on **claude-opus-4-8**; iteration-2 used **claude-sonnet-4-6**, so the with-skill jump conflates the skill edit with a model change. The fixes target the exact failure causes (over-gating, missing caveats) and the new outputs visibly contain the required elements, but a clean 3× same-model pass is the proper confirmation.
- Outputs were produced and graded in the same session, not via an independent harness grader.

**To confirm rigorously**: re-run the full 26 × 2 × 3 pass with `skill-creator` on the same model as iteration-2. See [`../evals/README.md`](../evals/README.md#reproduce-it).

## Files

| File | Description |
|---|---|
| [`benchmark-iteration-3.json`](benchmark-iteration-3.json) | Machine-readable iteration-3 results |
| [`../evals/results/iteration-3/`](../evals/results/iteration-3) | The 6 re-run outputs + grading |
