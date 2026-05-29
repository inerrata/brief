# marketing-skill

A comprehensive, full-stack **marketing skill for Claude** — copywriting, brand & messaging, content strategy, campaigns & GTM, research, SEO, email/lifecycle, CRO, and measurement, in one installable package.

Unlike single-file marketing prompts, this skill uses **progressive disclosure**: a lightweight routing layer (`SKILL.md`) that loads 9 purpose-built reference modules only when they're relevant. You get the depth of nine specialist playbooks without bloating the context window on every request.

Compatible with **Claude Code, Claude.ai, the Claude API, Cursor, Codex CLI, Gemini CLI**, and any tool that supports the open `SKILL.md` format.

---

## Table of contents

- [Why this exists](#why-this-exists)
- [Who it's for](#who-its-for)
- [What it covers](#what-it-covers)
- [Use cases](#use-cases)
- [How it works](#how-it-works)
- [The brief-first philosophy](#the-brief-first-philosophy)
- [The universal quality bar](#the-universal-quality-bar)
- [A worked example](#a-worked-example)
- [Installation](#installation)
- [Usage](#usage)
- [Validation & evals](#validation--evals)
- [Design principles](#design-principles)
- [FAQ](#faq)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Why this exists

Most "marketing prompts" fail in one of two ways. They're either **too generic** — a wall of best-practice platitudes that produces copy any competitor could have written — or **too narrow** — a single template that only handles one task and breaks the moment your need shifts.

This skill is built around a different premise: **good marketing is specific, evidence-led, and built around the reader, not the brand.** It encodes that discipline as a set of frameworks, checklists, and quality gates, then routes each request to the right one. The result is output that's ready to use, grounded in a real audience and goal, and honest about what it doesn't know.

It also refuses to do the things that quietly destroy trust: it won't fabricate statistics, invent testimonials, or audit a landing page it has never seen.

---

## Who it's for

- **Founders & solo operators** who need a competent marketing partner without hiring one — launch plans, landing copy, positioning, first-100-customers playbooks.
- **Marketers & growth teams** who want a rigorous second brain for briefs, audits, campaign concepts, and measurement — and a consistent quality bar across the team.
- **Agencies & freelancers** producing client work who need to move fast without sounding generic.
- **Product & eng teams** writing their own homepage, onboarding emails, or changelog copy and want it to actually convert.
- **Anyone** who has ever stared at a blank page that needed to sell something.

No marketing vocabulary required — the skill triggers on intent ("nobody knows my store exists, how do I get customers?"), not just keywords.

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

## Use cases

Concrete scenarios, the kind of prompt that triggers them, and what you get back.

### Launching something

| You want to… | Say something like… | You get |
|---|---|---|
| Launch a product with no plan yet | *"Help me launch my new habit-tracking app."* | Scoping questions (audience, goal, timeline), then a one-page campaign brief + a phased pre-/launch/post timeline + an asset checklist |
| Get your first customers from zero | *"Nobody knows my store exists. How do I get my first 100 customers?"* | A focused acquisition plan — one channel/motion to start, matched to your audience, with proof and content angles (not a vague pep talk) |
| Go to market as a solo founder | *"I'm launching a paid Notion-template business next month, no audience yet — what's my plan?"* | A sequenced GTM plan synthesizing research + channel choice + content + email + launch, focused on one motion first |

### Writing copy that converts

| You want to… | Say something like… | You get |
|---|---|---|
| Write a cold outreach email | *"Write a cold email to SaaS founders for my churn-reduction tool."* | A tight email: subject + preview text, relevance-first opening, one idea, one low-friction CTA, assumptions stated |
| Get homepage hero copy | *"I need words for the top of my homepage — it's a tool that schedules social posts."* | Ready-to-paste headline + subheadline + CTA options, outcome-led, on a stated assumption you can correct |
| Generate subject-line options | *"Give me 3 Black Friday subject lines for a coffee subscription brand."* | Three lines taking genuinely different angles (curiosity / benefit / urgency), each labeled and length-checked |
| Avoid fake proof | *"Write a landing page with impressive testimonials and stats."* | The page — with clearly-marked placeholders for proof and an explanation of why fabricating it breaks trust (and law) |

### Strategy & positioning

| You want to… | Say something like… | You get |
|---|---|---|
| Nail your positioning | *"Write a positioning statement for a PM tool aimed at agencies."* | 2–3 sharp questions first (narrowest audience, real differentiator, true alternative), then a defensible statement — not a confident guess |
| Define your brand voice | *"Help me define my brand voice."* | A short discovery, then a voice profile with do/don't dimensions and tone-by-moment guidance |
| Write a value proposition | *"Meal-prep for busy parents, ready in 5 min, no ultra-processed ingredients — write my value prop."* | An outcome-led value prop specific enough that only your brand could say it |

### Content & SEO

| You want to… | Say something like… | You get |
|---|---|---|
| Plan a content calendar | *"Build a content calendar for a B2B fintech startup."* | 3–5 content pillars, funnel-stage mapping, a value-heavy mix, and a calendar with pillar / stage / format / title / CTA |
| Know what to post | *"What should I post on LinkedIn for my consulting business?"* | Pillars + format guidance tied to LinkedIn norms and funnel stages — not "post valuable content" |
| Write an SEO brief | *"Write an SEO brief targeting 'best crm for nonprofits'."* | Intent analysis → format, title/meta, H2/H3 outline, People-Also-Ask, differentiation angle, E-E-A-T notes — with a flag that real volume/difficulty need a tool |

### Lifecycle & retention

| You want to… | Say something like… | You get |
|---|---|---|
| Build a welcome sequence | *"Design a welcome sequence for my newsletter."* | A 3–5 email flow with timing and one CTA each, progressing welcome → story → value → proof → soft offer |
| Win back dormant users | *"Plan a win-back sequence for users inactive 60 days."* | A re-engagement flow that acknowledges the silence, gives a reason to return, and suppresses non-responders to protect deliverability |

### Audit, optimize & measure

| You want to… | Say something like… | You get |
|---|---|---|
| Audit a page | *"My pricing page isn't converting — audit it."* | A request for the actual page first (paste/URL/screenshot) + goal + audience; with the asset, a structured conversion audit + prioritized fixes |
| Analyze competitors | *"Competitor analysis of the main email-marketing players."* | Per-competitor positioning/audience/messaging/proof/gaps, ending in a white-space opportunity ("therefore…") |
| Decide what to measure | *"What should I track for a new paid ads channel?"* | Primary metric tied to the goal (CAC/ROAS), leading indicators, formulas, a vanity-metric warning, and the attribution caveat |
| Sanity-check unit economics | *"Is a $400 CAC good if customers pay $50/mo for ~18 months?"* | The LTV and LTV:CAC math shown, interpreted against the ~3:1 guideline, with the caveats that benchmarks and gross margin matter |

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

At session start, only the `SKILL.md` **description** (~100 tokens) is in context. When a marketing task is detected, the full `SKILL.md` loads and routes to the relevant reference module(s). Modules not needed for the task never load. A multi-area request (e.g. a launch) pulls several modules and synthesizes them.

Two hard gates enforce quality:

- **Gate A — Strategy foundations** (positioning, value prop, messaging hierarchy, brand voice, GTM): asks 2–3 sharp questions before writing rather than producing a confident guess on unverified inputs. These are load-bearing — everything downstream inherits their flaws.
- **Gate B — Audits / "improve my X"**: requests the actual asset before auditing. It won't invent the contents of a page it hasn't seen and then critique its own invention.

Everything else **scales to stakes**: big ambiguous strategy work gets a couple of scoping questions first; a concrete copy deliverable (a hero, an ad, subject lines) is drafted immediately on a clearly-stated assumption, with optional sharpening questions *after* the draft — because a draft you can react to beats an interrogation.

---

## The brief-first philosophy

Marketing output is only as good as its inputs. Before producing anything, the skill establishes (or explicitly infers and flags) five things:

1. **Audience** — who specifically is this for, and what do they believe right now?
2. **Goal** — the one action this should drive.
3. **Offer** — what's being marketed, and the single most important thing about it.
4. **Proof** — the evidence behind the claims.
5. **Constraint** — channel, length, tone, brand rules.

The audience and the goal are never silently guessed — they're load-bearing in every task. When the skill does make an assumption, it states it out loud ("Assuming [X]; adjust if wrong") so you can correct it in one line.

---

## The universal quality bar

Every deliverable is checked against this before it's handed back:

- **Specificity** — concrete claims, numbers, and outcomes replace vague adjectives ("amazing," "powerful," "seamless").
- **Reader-first** — leads with the reader's problem or desire, not the product's feature list.
- **One message per piece** — every asset has exactly one job.
- **Proof over claims** — every significant claim has support, or is flagged as needing it.
- **Mechanics** — active voice, short sentences, filler cut, read-aloud test.
- **Earn the next line** — the headline's only job is to get the subhead read.
- **Honesty** — no fabricated stats, fake testimonials, or invented credentials.

---

## A worked example

**Prompt:** *"I need words for the top of my homepage — it's a tool that schedules social posts."*

A generic assistant either writes vague copy ("Welcome to the future of social media!") or stalls with a list of questions. This skill recognizes a **copy deliverable**, picks the most likely audience, states it, and ships usable copy:

> *Assuming your audience is small businesses / solo creators managing their own social presence; adjust if you're targeting agencies.*
>
> **Headline:** Schedule a week of social posts in 20 minutes.
> **Subheadline:** Plan, schedule, and publish across every channel — so you show up consistently without living on your phone.
> **CTA:** Start scheduling free
>
> *A few things that would sharpen this further: who's your core user, which channels do you support, and is there a free trial?*

Outcome-led headline, a real subhead and CTA, one stated assumption, and the sharpening questions placed *after* the draft — not in front of it.

---

## Installation

### Claude Code (global)

```bash
git clone https://github.com/inerrata/marketing-tool.git
cp -r marketing-tool/_unpacked/marketing ~/.claude/skills/marketing
```

Restart Claude Code — it auto-discovers skills. Confirm with: *"what skills do you have available?"*

### Claude Code (project-specific)

```bash
cp -r marketing-tool/_unpacked/marketing .claude/skills/marketing
```

### Claude.ai

Download `marketing.skill` from the repo (or [Releases](../../releases)) and upload it under **Settings → Capabilities → Skills**. Requires a Pro, Max, Team, or Enterprise plan.

The `marketing.skill` file is just a zip of the `marketing/` folder — you can repackage it yourself from `_unpacked/marketing/` with any zip tool.

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
Nobody knows my store exists — how do I get my first 100 customers?
```

On high-stakes tasks (positioning, launches) the skill asks 2–3 focused questions before writing. On lower-stakes tasks (a subject line, a social post) it states its assumptions and proceeds.

---

## Validation & evals

The skill ships with a **26-prompt eval set** (`evals.json`) covering every module, plus phrasing variations, both gate checks (A and B), multi-module synthesis, implicit triggers, an honesty probe, and **negative controls** — prompts that should *not* trigger the skill (e.g. "what's a good name for my cat?"), used to measure false-positive triggering.

The harness runs each prompt **both with and without the skill** (a baseline), records whether the skill chose to trigger, and grades each output against per-prompt assertions. This measures two things at once:

- **Triggering accuracy** — does it fire when it should, and stay quiet when it shouldn't?
- **Output quality** — given it fired, does the deliverable meet the bar?

In testing, Gate A and Gate B fired correctly, the negative controls correctly declined to trigger, and the happy-path deliverables passed their assertions. (One finding — a homepage hero being over-gated instead of drafted — was fixed by separating *copy deliverables* from *strategy foundations*; it now passes its checks.)

To run the eval pass yourself via the **skill-creator** skill in Claude Code:

```
Use the skill-creator skill to run a full eval pass on ./marketing using ./evals.json.
Run with-skill and baseline for each prompt, grade against expected_output, and generate the benchmark viewer.
```

---

## Design principles

- **Specificity over cleverness** — numbers and outcomes, not vague adjectives
- **Reader-first** — leads with the audience's problem, not the product's features
- **Brief before output** — never silently guesses on audience or goal
- **Proof over claims** — every significant claim needs support
- **One message per piece** — every asset has exactly one job
- **Draft-first for copy, questions-first for strategy** — match the friction to the stakes
- **Honest by default** — never fabricates stats, testimonials, or credentials; surfaces advertising and email-compliance considerations where relevant

---

## FAQ

**Does it need an API key or any dependencies?**
No. It's plain Markdown following the `SKILL.md` format — no code to run, no packages to install.

**Why does it sometimes ask me questions instead of just answering?**
For strategy foundations (positioning, voice, GTM) and audits, a confident guess is worse than a question — everything downstream inherits the error. For ordinary copy, it drafts first and asks after.

**Will it make up testimonials or statistics if I ask it to?**
No. It writes the copy with clearly-marked placeholders and explains that fabricated proof breaks trust and, in many jurisdictions, advertising law.

**Does it work outside Claude?**
Yes — any tool that supports the open `SKILL.md` format (Cursor, Codex CLI, Gemini CLI, and others) can load it.

**How is this different from just asking Claude to "be a marketer"?**
The frameworks, gates, and quality bar make the output consistent and grounded instead of relying on whatever the model improvises that day — and the eval set lets you verify it.

**Can I customize it?**
Yes. Edit the reference modules to encode your own brand rules, frameworks, or tone, and add eval prompts to keep it honest.

---

## Roadmap

Ideas and PRs welcome — rough directions:

- Additional reference modules (e.g. paid-media buying, influencer/partnerships, PR & comms, localization)
- A brand-profile file the skill can read so output inherits your voice and constraints automatically
- More worked examples and before/after copy galleries
- Expanded eval coverage with multi-run variance reporting

---

## Contributing

PRs and issues welcome.

- Keep `SKILL.md` lean — it's always loaded and should stay a routing layer, not a content dump
- Add depth to `references/` — new modules or expanded frameworks go there
- If you add a module, add eval prompts to `evals.json` covering a happy path, a phrasing variation, and any gates that apply
- Run the eval set before and after your change so triggering and quality don't regress

---

## License

MIT — see [LICENSE](LICENSE).
