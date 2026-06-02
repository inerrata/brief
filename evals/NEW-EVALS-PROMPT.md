# Prompt: generate a fresh eval set for the marketing skill

Copy everything in the fenced block below and give it to another AI (ChatGPT, Gemini, another Claude, etc.). It will produce a brand-new eval set as JSON. Save that JSON as `evals/evals-v2.json` and it can be benchmarked the same way as `evals/evals.json`.

---

```
You are designing an evaluation set for a "marketing skill" — a system prompt that teaches an AI assistant to produce sharp, evidence-led marketing deliverables (copy, briefs, plans) and to apply discipline about WHEN to ask questions vs. when to just deliver.

Your job: write a BRAND-NEW set of 24 eval cases that test this skill. They must be original — do NOT reuse the prompts I list under "Already covered." I will run each new prompt through the assistant twice (with the skill, and without it as a baseline) and grade the output against your assertions, so the assertions are the most important part.

## How the skill behaves (so your assertions match its intended behavior)

The skill's core rule is DELIVER-FIRST. For almost every task it should state any assumptions in one line ("Assuming [X]; adjust if wrong") and then produce the actual deliverable — not ask a pile of questions first. There are exactly TWO exceptions where it must STOP and ask 2-3 questions before writing:

- GATE A — a single load-bearing strategy STATEMENT: a positioning statement, a value proposition, a messaging hierarchy, or a brand voice/tone definition. ONLY these four. (Note: ICPs, personas, content calendars, campaign briefs, and launch/GTM plans are NOT gated — they are deliver-first working documents.)
- GATE B — an audit / "improve my X" task where the asset is not provided. It must ask for the real asset (paste/URL/screenshot) before auditing, and must NOT invent the asset's contents.

Other key behaviors to test:
- Quality bar: specificity over vague adjectives, reader-first benefits, one message per asset, proof over claims, active voice.
- Honesty: never fabricate stats/testimonials/credentials — but still WRITE the full deliverable using clearly-marked placeholders like [TESTIMONIAL: specific result].
- Measurement deliverables must always warn against vanity metrics and note attribution is imperfect.
- Triggering: the skill should fire even on casual, keyword-light marketing requests, and must NOT fire on non-marketing requests (naming a pet, explaining DNS, a personal thank-you note).

## Modules the skill covers (spread your evals across these)
copywriting, brand-messaging, content-strategy, campaigns, research (personas/ICP/competitor), seo, email-lifecycle, cro, measurement.

## Required mix of the 24 evals (use these exact `type` values)
- 9 × `happy_path` — core deliverable quality, one per module.
- 3 × `phrasing_variation` — casual / keyword-light wording that should still trigger and deliver.
- 3 × `gate_A` — a true positioning / value-prop / messaging-hierarchy / brand-voice request that SHOULD make the skill stop and ask first.
- 2 × `gate_B` — an audit/improve request with NO asset attached (should request the asset). For ONE of them, optionally include the asset inline and require an actual audit instead.
- 2 × `deliver_first_trap` — tasks that FEEL strategic but must NOT be gated (e.g. "build me an ICP", "make a content calendar", "plan my launch"). Assertions must require the deliverable to be produced on stated assumptions, NOT withheld behind questions.
- 1 × `honesty_probe` — explicitly asks for impressive testimonials/stats; must refuse to fabricate yet still write the asset with marked placeholders.
- 1 × `multi_module` — a request spanning 3+ modules (e.g. a launch) that must synthesize without sprawling.
- 3 × `should_not_trigger` — non-marketing requests; the skill must NOT activate.

## Output format
Return ONLY valid JSON: an array of 24 objects, each exactly:

{
  "id": <int 1..24>,
  "name": "<short-kebab-name>",
  "module": "<one of the modules above, or 'none' for should_not_trigger>",
  "type": "<one of the type values above>",
  "prompt": "<the user's request, written naturally — vary the phrasing and realism>",
  "expected_output": "<1-3 sentences describing what a correct response looks like>",
  "assertions": ["<assertion 1>", "<assertion 2>", ...],
  "files": []
}

## Rules for assertions (this is what makes the eval usable)
- 3-7 assertions per eval, each a single objectively-checkable statement a grader can mark pass/fail with one line of evidence.
- Prefer concrete, countable checks: "Provides exactly three subject line options", "Each subject line is under ~50 characters", "Includes a CTA", "Does not fabricate a discount figure".
- For gate_A: assert that it asked 2-3 scoping questions BEFORE writing and did not output a full statement built on guesses.
- For deliver_first_trap: assert that it produced the full deliverable AND stated assumptions, and did NOT withhold it behind questions.
- For should_not_trigger: assert the marketing skill did NOT activate and no marketing framework was applied.
- Make at least 4 of the happy_path / deliver_first_trap cases ADVERSARIAL — realistic but missing audience or goal — to test that the skill states an assumption and delivers instead of stalling.
- Keep prompts realistic and varied in tone (some terse, some rambling, some with typos). No two prompts should test the same thing.

## Already covered — do NOT duplicate these
cold email for a churn tool; homepage hero for a social-post scheduler; Black Friday subject lines for coffee; positioning statement for an agency PM tool; brand voice; value prop for meal-prep; content calendar for B2B fintech; LinkedIn post for consulting; launch plan for a habit-tracking app; campaign brief for a time-tracking tool; ICP for an invoicing tool; competitor email-marketing analysis; SEO brief for CRM-for-nonprofits; SEO for an onboarding tool; welcome email sequence; 60-day win-back; pricing-page audit; landing-page audit with asset; paid-ads tracking metrics; CAC/LTV; Notion for solo founders; first-100-customers; fabricated-proof landing page; pet-cat name; DNS explanation; thank-you note to grandma.

Return only the JSON array.
```
