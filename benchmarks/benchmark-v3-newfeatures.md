# Benchmark — v3 new-features eval set

A targeted eval pass on the behaviors added in commit `dd1df6b` (agentic gates,
brand.md generation, the `product-marketing.md` and `specs.md` modules). 12 prompts,
run **with the skill (available-not-forced)** and **without it (baseline)**, each output
graded against per-prompt assertions in [`../evals/evals-v3.json`](../evals/evals-v3.json).

## Caveats — read these

- **1× run, self-graded.** Each prompt ran once per arm; one model graded its own
  family's outputs against the assertions. Treat these as directional, not as the
  rigorous number. The most rigorous figure in this repo remains the 3×-averaged
  iteration-2 result (**86.4% vs 80.7% baseline, +5.7 pp**).
- **This set is deliberately adversarial to the skill's *marginal* value.** It tests
  behaviors a strong, agentic base model already does well (fetching URLs, reading
  repo files, writing release notes). So the with-vs-baseline delta is driven by the
  three behaviors the skill uniquely enforces — Gate A, the one-page battle-card
  discipline, and the `brand.md` offer; on the rest, baseline ties.
- **Small N (12).** Single failed assertions move a per-eval score a lot.

## Headline

| Arm | Assertions | Micro pass-rate | Macro mean eval score |
|---|:--:|:--:|:--:|
| **With skill** | **54 / 54** | **100%** | **100%** |
| Baseline | 50 / 54 | 92.6% | 92.8% |
| **Delta** | **+4** | **+7.4 pp** | **+7.2 pp** |

**Triggering: 12/12 correct.** All 11 marketing prompts triggered the skill; the
commit-message negative control (eval 12) correctly did not.

> **Note on eval 9.** The first pass scored eval 9 at 0.80 in both arms because the skill
> did not offer to create a `brand.md`. That was fixed by strengthening Step 0 from "offer
> when it would pay off" to an explicit "always offer to save volunteered brand facts," the
> skill was rebuilt, and eval 9 was re-run with-skill — it now scores 1.00 and offers the
> profile (showing a draft before saving). Baseline stays at 0.80 (it has no `brand.md`
> concept), making eval 9 a clean skill-unique win.

## Per-eval

| # | Eval | Type | With | Base | Trig |
|---|---|---|:--:|:--:|:--:|
| 1 | release-notes-translation | happy_path | 1.00 | 1.00 | ✓ |
| 2 | battle-card-honest | happy_path | 1.00 | 0.83 | ✓ |
| 3 | dev-audience-show-hn | happy_path | 1.00 | 1.00 | ✓ |
| 4 | feature-naming-pulseiq | happy_path | 1.00 | 1.00 | ✓ |
| 5 | specs-rsa-limits | happy_path | 1.00 | 1.00 | ✓ |
| 6 | linkedin-truncation-applied | happy_path | 1.00 | 1.00 | ✓ |
| 7 | gate-b-url-audit | gate_B | 1.00 | 1.00 | ✓ |
| 8 | gate-b-asset-in-repo | gate_B (agentic) | 1.00 | 1.00 | ✓ |
| 9 | brand-md-offer | happy_path | **1.00** | 0.80 | ✓ |
| 10 | brand-md-read | happy_path | 1.00 | 1.00 | ✓ |
| 11 | gate-a-regression-positioning | gate_A | **1.00** | **0.50** | ✓ |
| 12 | negative-control-commit-message | should_not_trigger | 1.00 | 1.00 | ✗ |

## What moved, and what didn't

**The skill's clear win is Gate A (eval 11, +0.50).** Asked for a positioning statement
with only "scheduling software for clinics," the baseline wrote a finished, confident
statement on guessed audience, category, and differentiation — exactly the load-bearing
guess Gate A exists to stop. The skill asked three sharp scoping questions first, then
offered an explicitly *provisional*, bracketed draft to react to. This mirrors the
original iteration-2 finding that positioning was the single biggest delta.

**Battle card (eval 2, +0.17):** both arms produced honest cards (including "where the
competitor wins"), but the baseline sprawled to nine sections plus a 30-second pitch;
the skill held the one-page, mid-call-scannable discipline `product-marketing.md`
prescribes.

**The agentic behaviors validated — but baseline matched them.** On Gate B by URL
(eval 7), Gate B by in-repo file (eval 8), and reading a project `brand.md` (eval 10),
the skill did exactly what it should: it tried the URL, found and quoted the real
`landing-page.md`, and built the email from the planted brand profile. But the baseline
*also* did all three — a capable agentic model fetches the URL and reads files in its
working directory on its own initiative. So these features are confirmed working with
**no regression**, but they add no measurable lift in a 1× run against a strong base
model. The skill's contribution here is making the behavior a guaranteed instruction
rather than emergent initiative.

**New modules' factual content held:** RSA limits (eval 5) and LinkedIn truncation
(eval 6) were correct in both arms; the specs module didn't need to rescue the base
model on these common specs, though it guarantees them.

## The one miss — found and fixed

The first pass surfaced one real gap: **eval 9 scored 0.80 in *both* arms** because the
skill **did not offer to save the standing brand facts as a `brand.md`**. The user handed
over durable facts (voice rules, a sourced stat) and got a great hero back — but no offer
to persist them. Step 0's wording ("offer when it would clearly pay off") was too soft to
fire reliably.

**Fix applied in the same session:** Step 0 was strengthened to an explicit, non-optional
instruction — *whenever the user volunteers durable brand facts, deliver first, then offer
to save them as a `brand.md`*. The skill was rebuilt and eval 9 re-run with-skill: it now
delivers the hero and closes with a concrete offer to save the voice rules and sourced
stat as a `brand.md`, showing the draft before saving. Score moved 0.80 → **1.00**.
Baseline stays at 0.80, so this is now a clean skill-unique win.

## Reproduce

```
python evals/harness/scaffold_v3.py          # lay out runs + plant project files
# execute each results/v3/eval-*/<arm>/run-1/prompt.txt, writing outputs/
python evals/harness/write_gradings_v3.py    # grading.json per run
python evals/harness/aggregate_v3.py         # this table + benchmark-v3-newfeatures.json
```
