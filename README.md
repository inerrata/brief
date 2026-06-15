<h1 align="center">📋 brief</h1>
<h2 align="center">If this is useful, a ⭐ helps others find it.</h2>
A full-stack marketing skill for Claude — copy, brand, content, campaigns, research, SEO, lifecycle, CRO, and measurement — that stays specific, asks before it guesses, and refuses to fake proof. Star if useful.

![license](https://img.shields.io/badge/license-MIT-green)
![format](https://img.shields.io/badge/format-SKILL.md-blue)
![evals](https://img.shields.io/badge/evals-26%20%2B%2024%20held--out%20%2B%2012%20new--features-blue)
[![with--skill](https://img.shields.io/badge/with--skill-98.9%25%2a-brightgreen)](benchmarks/benchmark-iteration-3.md#caveats-read-these)
[![held-out](https://img.shields.io/badge/held--out%20v2-122%2F122%2a-brightgreen)](benchmarks/benchmark-v2-evalset.md#caveats-read-these)
![delta](https://img.shields.io/badge/vs%20baseline-%2B5.7pp%20%283%C3%97%29-brightgreen)
![iterations](https://img.shields.io/badge/eval%20iterations-3-blue)

<sub>\* 1× runs, self-graded — click a badge for the full caveats. The most rigorous number remains the 3×-averaged iteration-2 result (86.4% vs 80.7% baseline, **+5.7 pp**).</sub>

Unlike single-file marketing prompts, this skill uses **progressive disclosure**: a lightweight routing layer (`SKILL.md`) that loads 11 purpose-built reference modules only when relevant. The depth of eleven specialist playbooks, none of the context bloat. Works with **Claude Code, Claude.ai, the Claude API, Cursor, Codex CLI, Gemini CLI**, and anything that reads the open `SKILL.md` format.

---

## Table of contents

- [Before / After](#before--after)
- [Benchmarks](#benchmarks)
- [Install](#install)
- [What you get](#what-you-get)
- [Use cases](#use-cases)
- [How it works](#how-it-works)
- [The brief-first philosophy](#the-brief-first-philosophy)
- [The universal quality bar](#the-universal-quality-bar)
- [Evaluation](#evaluation)
- [Design principles](#design-principles)
- [FAQ](#faq)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Before / After

**Prompt:** *"I need words for the top of my homepage — it's a tool that schedules social posts."*

| ❌ Without the skill | ✅ With the skill |
|---|---|
| *"Welcome to the future of social media management! Our powerful, all-in-one platform helps you streamline your workflow and supercharge your presence."* | *Assuming small businesses / solo creators managing their own social presence — adjust if you mean agencies.*<br><br>**Headline:** Schedule a week of social posts in 20 minutes.<br>**Subhead:** Plan, schedule, and publish across every channel — so you show up consistently without living on your phone.<br>**CTA:** Start scheduling free |
| Vague adjectives, no audience, no CTA, says nothing only-this-product could say. | Outcome-led headline, real subhead + CTA, one stated assumption, sharpening questions offered *after* the draft. |

That difference is measurable — see below.

---

## Benchmarks

Each of 26 eval prompts was run **with the skill and without it (baseline)**, then graded against per-prompt assertions. Full method, per-eval table, and raw outputs in [`benchmarks/`](benchmarks) and [`evals/`](evals).

| Metric | With skill | Baseline | Delta | Runs |
|---|:--:|:--:|:--:|:--:|
| **Iteration-3** (projected, targeted re-bench) | **98.9%** | 80.7% | **+18.2 pp** | 1× |
| Iteration-2 (3× avg) | 86.4% | 80.7% | +5.7 pp | 3× |
| Iteration-1 (1× directional) | 82.7% | 62.3% | +20.4 pp | 1× |

**Iteration-3** edited the skill to fix the five weak spots iteration-2 surfaced (over-gating on calendars/ICPs/launches, withholding on the honesty probe, missing measurement caveats). The six affected evals went from a 0.20–0.86 spread to **1.00** each. The 98.9% is *projected* — the iteration-2 table with those evals substituted (1× re-run). Full fixes + caveats in [`benchmarks/benchmark-iteration-3.md`](benchmarks/benchmark-iteration-3.md).

### Held-out v2 set — 24 brand-new prompts

To check the iteration-3 skill against cases it was never tuned on, a **separate AI generated 24 fresh evals** (see [`evals/NEW-EVALS-PROMPT.md`](evals/NEW-EVALS-PROMPT.md)) — including traps in *both* directions of the ask-vs-deliver boundary.

| Held-out v2 | Result |
|---|:--:|
| Assertions passed | **122 / 122** |
| Evals at 1.00 | **24 / 24** |

Both gate directions held: strategy statements (positioning, value prop, messaging hierarchy) asked first; working documents (ICP, content calendar) delivered on stated assumptions. Negative controls didn't fire. Method + honest caveats (1× run, self-graded) in [`benchmarks/benchmark-v2-evalset.md`](benchmarks/benchmark-v2-evalset.md).

### New-features set (v3) — 12 prompts for the agentic gates + new modules

A separate 12-prompt set targets the behaviors added after v2: the `product-marketing.md`
and `specs.md` modules, agentic Gate B (fetch the URL / find the asset in-repo), and the
`brand.md` read/offer flow.

| New-features v3 | With skill | Baseline |
|---|:--:|:--:|
| Micro pass-rate | **100%** | 92.6% |
| Triggering | **12 / 12 correct** | — |

The honest read: the standout is **Gate A** — baseline wrote a finished positioning
statement on guessed inputs; the skill asked first (1.00 vs 0.50). The skill also holds the
one-page battle-card discipline and reliably **offers to save volunteered brand facts as a
`brand.md`** (a gap the first pass caught and a Step 0 fix closed). The agentic Gate B and
brand.md-*read* behaviors work with **no regression**, but a capable agentic base model
matches them in a 1× run, so they add little measured lift. Method + per-eval table +
caveats (1× run, self-graded) in [`benchmarks/benchmark-v3-newfeatures.md`](benchmarks/benchmark-v3-newfeatures.md).

**Where it moves the needle most (iteration-2):**

| Eval | With | Base | Δ | Why |
|---|:--:|:--:|:--:|---|
| positioning statement (Gate A) | 1.00 | 0.00 | +1.00 | asks the load-bearing questions instead of guessing |
| implicit trigger (#22) | 1.00 | 0.50 | +0.50 | fires correctly with no marketing keywords |
| BF subject lines | 0.92 | 0.50 | +0.42 | angle labels, preview text, length-checked |
| homepage hero | 1.00 | 0.75 | +0.25 | outcome-led copy on a stated assumption |
| competitor analysis | 1.00 | 0.67 | +0.33 | ends in white-space gap, not just description |

**Negative controls** ("name my cat", "explain DNS", "thank-you note to grandma", plus v2's resume bullet, TCP/UDP, and a eulogy) correctly did **not** trigger. The iteration-2 weak spots are now fixed and re-benchmarked — see [`benchmarks/README.md`](benchmarks/README.md).

📊 **Browse every output and grade:** open [`evals/review.html`](evals/review.html) in a browser.

---

## Install

### Quick start (Claude Code)

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/inerrata/brief/main/install.sh | bash
```

```powershell
# Windows (PowerShell)
irm https://raw.githubusercontent.com/inerrata/brief/main/install.ps1 | iex
```

Installs to `~/.claude/skills/marketing` (all your projects pick it up).

### Claude Code (project-specific)

```bash
git clone https://github.com/inerrata/brief
cp -r brief/_unpacked/marketing your-project/.claude/skills/marketing
```

### Claude.ai

Two options, depending on your plan/UI:

- **Skills upload** (Pro/Max/Team/Enterprise): download `marketing.skill` and upload it under **Settings → Capabilities → Skills**. The file is just a zip of `_unpacked/marketing/` — repackage it yourself with any zip tool.
- **Projects fallback** (works everywhere): paste the contents of [`_unpacked/marketing/SKILL.md`](_unpacked/marketing/SKILL.md) into a Project's custom instructions (**Project → Settings → Project instructions**). You lose progressive disclosure (the 11 reference modules won't lazy-load), so for deep work also paste the relevant module from `_unpacked/marketing/references/`.

### Brand profile (optional, recommended)

Copy [`brand.template.md`](brand.template.md) into your project as `brand.md` and fill it in. The skill reads it at the start of a session and treats it as your standing brief — audience, voice, proof on file — so you stop re-answering the same scoping questions every session.

Don't want to fill it in by hand? Ask the skill to draft it for you — it can build a `brand.md` from what it learns in conversation, or (in tool-enabled environments like Claude Code) from fetching your homepage, and show you the draft to correct before saving.

---

## What you get

| Module | Covers |
|---|---|
| **Copywriting** | Ads, emails, landing/sales pages, homepages, CTAs, taglines, social posts, microcopy — PAS / AIDA / BAB / 4Ps / FAB, 10-point editing checklist |
| **Brand & messaging** | Positioning, value propositions, messaging hierarchy, brand voice & tone, naming, message testing |
| **Content strategy** | Content pillars, funnel mapping, calendars, content ratios, repurposing, distribution, audits |
| **Campaigns & GTM** | Campaign briefs, concept development, phased launches, go-to-market plans, asset checklists |
| **Research** | Personas, ICPs, segmentation, jobs-to-be-done, competitor gap analysis, voice-of-customer |
| **SEO** | Search intent, keyword strategy, content briefs, on-page optimization, E-E-A-T |
| **Email & lifecycle** | Welcome / nurture / sales / onboarding / win-back / abandoned-cart sequences, newsletters, deliverability |
| **CRO** | Conversion audits, the conversion equation, A/B testing methodology, high-impact fixes |
| **Measurement** | Metrics by goal, AARRR funnel, CAC / LTV / ROAS formulas, attribution, reporting |
| **Product marketing** | Release notes, changelogs, feature announcements & tiering, feature naming, battle cards, sales one-pagers, marketing to developers |
| **Channel specs** | Character limits, truncation points, image sizes, and format constraints for ads, email, social, SEO, video, app stores, SMS/push |

---

## Use cases

Concrete scenarios, the prompt that triggers them, and what you get back.

### Launching something

| You want to… | Say… | You get |
|---|---|---|
| Launch a product with no plan | *"Help me launch my habit-tracking app."* | Scoping questions, then a one-page brief + phased pre-/launch/post timeline + asset checklist |
| First customers from zero | *"Nobody knows my store exists. How do I get my first 100 customers?"* | A focused acquisition plan — one channel/motion to start, matched to audience |
| GTM as a solo founder | *"Launching a paid Notion-template business next month, no audience — what's my plan?"* | A sequenced GTM plan (research + channel + content + email + launch), one motion first |

### Writing copy that converts

| You want to… | Say… | You get |
|---|---|---|
| Cold outreach email | *"Cold email to SaaS founders for my churn-reduction tool."* | Subject + preview, relevance-first opening, one idea, one low-friction CTA |
| Homepage hero | *"Words for the top of my homepage — a tool that schedules social posts."* | Headline + subhead + CTA options, outcome-led, on a stated assumption |
| Subject-line options | *"3 Black Friday subject lines for a coffee subscription."* | Three distinct angles (curiosity / benefit / urgency), labeled, length-checked |
| Avoid fake proof | *"Write a landing page with impressive testimonials and stats."* | The page, with marked placeholders + why fabricating proof breaks trust and law |

### Strategy & positioning

| You want to… | Say… | You get |
|---|---|---|
| Nail positioning | *"Positioning statement for a PM tool aimed at agencies."* | 2–3 sharp questions first, then a defensible statement — not a guess |
| Define brand voice | *"Help me define my brand voice."* | Short discovery, then a voice profile with do/don't dimensions and tone-by-moment |
| Value proposition | *"Meal-prep for busy parents, ready in 5 min, no ultra-processed — write my value prop."* | An outcome-led value prop only your brand could say |

### Content, SEO, lifecycle, measurement

| You want to… | Say… | You get |
|---|---|---|
| Content calendar | *"Content calendar for a B2B fintech startup."* | 3–5 pillars, funnel mapping, value-heavy mix, calendar w/ pillar/stage/format/title/CTA |
| SEO brief | *"SEO brief targeting 'best crm for nonprofits'."* | Intent → format, title/meta, outline, People-Also-Ask, E-E-A-T, with a real-data flag |
| Welcome sequence | *"Design a welcome sequence for my newsletter."* | 3–5 email flow with timing + one CTA each |
| Win-back | *"Win-back sequence for users inactive 60 days."* | Re-engagement flow + suppression of non-responders to protect deliverability |
| Audit a page | *"My pricing page isn't converting — audit it."* | Fetches the live page itself (with tools) or asks for it, then a structured audit + prioritized fixes |
| Ship a release | *"Write release notes for v2.3."* | User-outcome release notes from the real changelog — breaking changes first, no "improved performance" filler |
| Arm your sales team | *"Battle card against [competitor]."* | One-page card: where you win with proof, where they win (honestly), objections, landmines |
| What to measure | *"What should I track for a new paid ads channel?"* | Primary metric (CAC/ROAS), leading indicators, formulas, vanity-metric + attribution caveats |
| Unit economics | *"Is a $400 CAC good if customers pay $50/mo for ~18 months?"* | LTV + LTV:CAC math shown, read against ~3:1, with the caveats |

---

## How it works

```
marketing/
├── SKILL.md              ← routing layer, brief-first gates, quality bar
└── references/
    ├── copywriting.md       ├── research.md         ├── email-lifecycle.md
    ├── brand-messaging.md   ├── seo.md              ├── cro.md
    ├── content-strategy.md  ├── campaigns.md        ├── measurement.md
    ├── product-marketing.md └── specs.md
```

At session start, only the `SKILL.md` **description** (~100 tokens) is in context. When a marketing task is detected, the full `SKILL.md` loads and routes to the relevant module(s); unused modules never load. Multi-area requests pull several and synthesize.

Two hard gates enforce quality:

- **Gate A — Strategy foundations** (positioning, value prop, voice, GTM): asks 2–3 sharp questions before writing. These are load-bearing — everything downstream inherits their flaws.
- **Gate B — Audits / "improve my X"**: sees the real asset before auditing. In tool-enabled environments (Claude Code, etc.) it fetches the URL or finds the asset in your repo itself; otherwise it asks you to share it. It won't invent a page's contents and critique its own invention.

Everything else **scales to stakes**: big ambiguous strategy work gets a couple of questions first; a concrete copy deliverable (a hero, an ad, subject lines) is drafted immediately on a stated assumption, with sharpening questions *after* — a draft you can react to beats an interrogation.

---

## The brief-first philosophy

Before producing anything, the skill establishes (or explicitly infers and flags) five things:

1. **Audience** — who specifically, and what do they believe now?
2. **Goal** — the one action this should drive.
3. **Offer** — what's marketed, and the single most important thing about it.
4. **Proof** — the evidence behind the claims.
5. **Constraint** — channel, length, tone, brand rules.

Audience and goal are never *silently* guessed. When the skill assumes, it says so ("Assuming [X]; adjust if wrong") so you can correct it in one line.

---

## The universal quality bar

Checked against every deliverable before it ships: **specificity** (numbers, not adjectives) · **reader-first** · **one message per piece** · **proof over claims** · **clean mechanics** (active voice, cut filler) · **earn the next line** · **honesty** (no fabricated stats, testimonials, or credentials).

---

## Evaluation

The skill ships with its own test suite in [`evals/`](evals): **26 prompts** (`evals.json`), a **24-prompt held-out v2 set** (`evals-v2.json`, AI-generated), and a **12-prompt v3 new-features set** (`evals-v3.json`) targeting the agentic gates and the product-marketing/specs modules — together covering every module, phrasing variations, both gate checks, deliver-first traps, multi-module synthesis, an implicit trigger, an honesty probe, and **negative controls** (prompts that should *not* trigger it).

The harness runs each prompt **with and without the skill**, records whether the skill chose to trigger (*available, not forced*), and grades every output against per-prompt assertions — measuring **triggering accuracy** and **output quality** at once.

- 📊 Aggregate + per-eval table → [`benchmarks/README.md`](benchmarks/README.md)
- 🧪 Eval set + harness + raw results → [`evals/`](evals)
- 🖥️ Click-through viewer → [`evals/review.html`](evals/review.html)

Reproduce it in Claude Code with the `skill-creator` skill:

```
Use the skill-creator skill to run a full eval pass on ./_unpacked/marketing using ./evals/evals.json.
Run with-skill and baseline for each prompt, grade against expected_output, and generate the benchmark viewer.
```

---

## Design principles

- **Specificity over cleverness** — numbers and outcomes, not vague adjectives
- **Reader-first** — leads with the audience's problem, not the product's features
- **Brief before output** — never silently guesses on audience or goal
- **Proof over claims** — every significant claim needs support
- **One message per piece** — every asset has exactly one job
- **Draft-first for copy, questions-first for strategy** — match friction to stakes
- **Honest by default** — never fabricates proof; surfaces advertising/email-compliance considerations

---

## FAQ

**Does it need an API key or dependencies?** No — plain Markdown in the `SKILL.md` format. Nothing to run or install.

**Why does it sometimes ask questions instead of answering?** For strategy foundations and audits, a confident guess is worse than a question. For ordinary copy, it drafts first and asks after.

**Will it invent testimonials or stats if I ask?** No. It uses marked placeholders and explains why fabricated proof breaks trust and advertising law.

**Does it work outside Claude?** Yes — any tool that reads `SKILL.md` (Cursor, Codex CLI, Gemini CLI, …).

**How is this different from "be a marketer"?** Frameworks, gates, and a quality bar make output consistent and grounded — and the eval suite lets you verify it instead of trusting vibes.

**Can I customize it?** Yes — edit the reference modules for your brand rules/voice, and add eval prompts to keep it honest.

---

## Roadmap

- More reference modules (paid-media buying, partnerships/influencer, PR & comms, localization)
- ✅ ~~Product-marketing module (release notes, battle cards, dev marketing) + channel-specs cheat sheet~~
- ✅ ~~Agentic audits — fetch the URL / find the asset in-repo instead of asking for a paste~~
- ✅ ~~brand.md generation — the skill drafts your brand profile from conversation or your homepage~~
- ✅ ~~A brand-profile file the skill reads so output inherits your voice automatically~~ (`brand.template.md`, read via Step 0 in `SKILL.md`)
- ✅ ~~Multi-run (3×) eval pass with variance reporting~~ (iteration-2) and ✅ ~~fix the tracked weak spots~~ (iteration-3, re-benchmarked)
- Independent grading: run the held-out v2 set on a different model with a third-model grader to remove self-grading bias
- 3× multi-run pass on the v2 set; merge it into the standing regression suite
- More worked before/after examples

---

## Contributing

Star if useful.

PRs and issues welcome.

- Keep `SKILL.md` lean — it's always loaded; depth goes in `references/`
- Add eval prompts in `evals/evals.json` for any new module (happy path + a phrasing variation + gates)
- Run the eval set before and after your change so triggering and quality don't regress

---

## License

MIT — see [LICENSE](LICENSE).
