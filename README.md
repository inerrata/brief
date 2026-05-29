# marketing-skill

A comprehensive marketing skill for Claude — covers copywriting, brand & messaging, content strategy, campaigns, SEO, email/lifecycle, CRO, and measurement.

Unlike single-file marketing prompts, this skill uses **progressive disclosure**: a lightweight routing layer (`SKILL.md`) that loads 9 purpose-built reference modules only when relevant. It stays comprehensive without bloating the context window.

Tested against a 26-prompt eval set covering happy paths, phrasing variations, gate checks, multi-module synthesis, implicit triggers, honesty probes, and negative controls.

Compatible with **Claude Code, Claude.ai, the Claude API, Cursor, Codex CLI, Gemini CLI**, and any tool that supports the open `SKILL.md` format.

---

## What it covers

| Module | Covers |
|---|---|
| **Copywriting** | Ads, emails, landing/sales pages, homepages, CTAs, taglines, social posts, microcopy — PAS / AIDA / BAB / 4Ps / FAB frameworks, 10-point editing checklist |
| **Brand & messaging** | Positioning statements, value propositions, messaging hierarchy, brand voice & tone, naming, message testing |
| **Content strategy** | Content pillars, funnel mapping, calendars, content ratios, repurposing, distribution, audits |
| **Campaigns & GTM** | Campaign briefs, concept development, phased launches, go-to-market plans, asset checklists |
| **Research** | Audience personas, ICPs, segmentation, jobs-to-be-done, competitor gap analysis, voice-of-customer |
| **SEO** | Search intent, keyword strategy, content briefs, on-page optimization, E-E-A-T |
| **Email & lifecycle** | Welcome / nurture / sales / onboarding / win-back / abandoned-cart sequences, newsletters, deliverability |
| **CRO** | Conversion audits, the conversion equation, A/B testing methodology, high-impact fixes |
| **Measurement** | Metrics by goal, AARRR funnel, CAC / LTV / ROAS formulas, attribution models, reporting |

---

## How it works

```
marketing/
├── SKILL.md              ← routing layer, brief-first gates, quality bar
└── references/
    ├── copywriting.md
    ├── brand-messaging.md
    ├── content-strategy.md
    ├── campaigns.md
    ├── research.md
    ├── seo.md
    ├── email-lifecycle.md
    ├── cro.md
    └── measurement.md
```

At session start, only the `SKILL.md` description (~100 tokens) is read. When a marketing task is detected, the full `SKILL.md` loads and routes to the relevant reference module. Modules not needed for the task never load.

Two hard gates enforce quality:

- **Gate A — Strategy foundations** (positioning, brand voice, GTM): asks 2–3 sharp questions before writing rather than producing a confident guess on unverified inputs.
- **Gate B — Audits / "improve my X"**: requests the actual asset before auditing. Doesn't invent the contents of a page it hasn't seen.

---

## Installation

### Claude Code (global)

```bash
git clone https://github.com/<your-username>/marketing-skill.git
cp -r marketing-skill/marketing ~/.claude/skills/marketing
```

Restart Claude Code — it auto-discovers skills. Confirm with: *"what skills do you have available?"*

### Claude Code (project-specific)

```bash
cp -r marketing-skill/marketing .claude/skills/marketing
```

### Claude.ai

Download `marketing.skill` from [Releases](../../releases) and upload it under **Settings → Capabilities → Skills**. Requires Pro, Max, Team, or Enterprise.

Or zip it yourself:

```bash
zip -r marketing.skill marketing/
```

---

## Usage

Just ask naturally — the skill triggers without the word "marketing":

```
Write a cold email to SaaS founders for my churn-reduction tool
Help me launch my habit-tracking app
My pricing page isn't converting — what's wrong with it?
Build a content calendar for a B2B fintech startup
Write a positioning statement for a PM tool aimed at agencies
What should I track for a new paid ads channel?
```

On high-stakes tasks (positioning, launches) the skill asks 2–3 focused questions before writing.  
On lower-stakes tasks (a subject line, a social post) it states its assumptions and proceeds.

---

## Design principles

- **Specificity over cleverness** — numbers and outcomes, not vague adjectives
- **Reader-first** — leads with the audience's problem, not the product's features
- **Brief before output** — never silently guesses on audience or goal
- **Proof over claims** — every significant claim needs support
- **One message per piece** — every asset has exactly one job
- **Honest by default** — never fabricates stats, testimonials, or credentials; surfaces advertising and email compliance considerations where relevant

---

## Evals

A 26-prompt eval set lives in `evals/evals.json`. It covers every module, phrasing variations, gate checks (A and B), multi-module synthesis, implicit triggers, a honesty probe, and 3 negative controls (prompts that should NOT trigger the skill).

To run it via the skill-creator skill in Claude Code:

```
Use the skill-creator skill to run a full eval pass on ./marketing using ./evals/evals.json.
Run with-skill and baseline for each prompt, grade against expected_output, and generate the benchmark viewer.
```

---

## Contributing

PRs and issues welcome.

- Keep `SKILL.md` lean — it's always loaded and should stay a routing layer, not a content dump
- Add depth to `references/` — new modules or expanded frameworks go there
- If you add a module, add eval prompts to `evals/evals.json` covering happy path, a phrasing variation, and any gates that apply

---

## License

MIT — see [LICENSE](LICENSE).
