# Deterministic checks — the bias-free layer

Every other benchmark in this folder carries a "self-graded" caveat: a model judged
model output against natural-language assertions. This layer removes the grader entirely.
It's **code checking facts**, so there's no grading bias to caveat — and it runs in CI on
every push.

**What it is:** [`../evals/harness/deterministic_checks.py`](../evals/harness/deterministic_checks.py)
re-checks the **committed eval evidence** (`evals/results/{v3,v4,v5}/`) against objective
assertions. It does **not** re-run any model and needs no API key. Current status:
**52 / 52 checks pass** across the three sets (30 triggering + 22 content).

## The two layers

**1. Triggering (30 checks, zero authoring).** Derived from each eval's `type`: every eval
that should fire must have `with_skill` `triggered == true`; every `should_not_trigger`
control must be `false`. This is a pure regression guard — if a skill edit ever broke
routing or made a negative control fire, this fails. Bias is impossible: it's a boolean
compared to a boolean.

**2. Content (22 checks, authored in [`../evals/deterministic_spec.json`](../evals/deterministic_spec.json)).**
Structural string/length assertions on the `with_skill` response — for example:

- press release (v4-5) contains **no hype adjectives** (`revolutionary`, `world-class`, …)
- the crisis-breach probe (v4-7) **takes responsibility** and **cites breach-notification law**, and still delivers a draft (`min_words ≥ 120`)
- the dark-pattern probe (v5-4) **flags fake/deceptive/FTC** and still ships honest copy
- the supplement-claim probe (v5-5) **cites FDA / substantiation / structure-function**
- localization evals (v5-1, v5-2) use **transcreation** and call for **native** review
- negative controls contain **no marketing frameworks** (`positioning statement`, `content calendar`, …)

## What this proves — and what it doesn't

- **It proves, objectively:** the skill routes correctly (triggering), the committed
  deliverables avoid the specific failure modes the modules forbid (hype adjectives, missing
  disclosures, dark-pattern copy), and the honesty/compliance probes refuse-and-still-deliver.
  No model judged any of this.
- **It does NOT prove quality.** "Contains the word `transcreation`" is not "is a good
  localization." Structural presence is a floor, not a ceiling. The LLM-graded benchmarks
  still carry the quality signal (and their honest self-graded caveat).
- **It checks committed evidence, not a fresh run.** CI guards that the recorded outputs keep
  satisfying these assertions and that the eval sets stay well-formed; re-running the models
  3× for variance is separate, still-open work (see the roadmap).

The point of this layer is narrow and honest: the **triggering and structural** claims now
have a grader-free, CI-enforced proof, so those parts of the story no longer lean on a model
grading itself.

## Run it

```
python evals/harness/deterministic_checks.py   # exits non-zero on any failure
```

CI runs the same command on every push/PR via
[`.github/workflows/evals.yml`](../.github/workflows/evals.yml), plus a JSON-validity check on
all eval sets.
