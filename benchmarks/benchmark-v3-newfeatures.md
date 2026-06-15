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
  repo files, writing release notes). So the with-vs-baseline delta here is mostly
  driven by the two gate behaviors; on the rest, baseline ties.
- **Small N (12).** Single failed assertions move a per-eval score a lot.

## Headline

| Arm | Assertions | Micro pass-rate | Macro mean eval score |
|---|:--:|:--:|:--:|
| **With skill** | **53 / 54** | **98.1%** | **98.3%** |
| Baseline | 50 / 54 | 92.6% | 92.8% |
| **Delta** | **+3** | **+5.6 pp** | **+5.6 pp** |

**Triggering: 12/12 correct.** All 11 marketing prompts triggered the skill; the
commit-message negative control (eval 12) correctly did not.

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
| 9 | brand-md-offer | happy_path | 0.80 | 0.80 | ✓ |
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

## The one real miss — actionable

**eval 9 (brand-md-offer) scored 0.80 in *both* arms** because the skill **did not offer
to save the standing brand facts as a `brand.md`**. The user handed over durable facts
(voice rules, a sourced stat) and got a great hero back — but no offer to persist them.
Step 0's wording ("you *may* suggest starting one") is too soft to fire reliably. This is
the one behavior this pass shows the skill is *not* delivering, and it's a cheap fix:
strengthen Step 0 from "may suggest" to an explicit "offer to save these as a brand.md"
when a user volunteers durable brand facts. Recommended before the next release.

## Reproduce

```
python evals/harness/scaffold_v3.py          # lay out runs + plant project files
# execute each results/v3/eval-*/<arm>/run-1/prompt.txt, writing outputs/
python evals/harness/write_gradings_v3.py    # grading.json per run
python evals/harness/aggregate_v3.py         # this table + benchmark-v3-newfeatures.json
```
