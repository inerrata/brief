---
name: marketing
description: >
  Comprehensive, full-stack marketing skill for creating, auditing, and optimizing marketing content
  and strategy with rigor. Use this skill whenever the user wants to write or improve copy (ads, emails,
  landing pages, homepages, social posts, CTAs, taglines, product descriptions, sales pages), run a content
  or messaging audit, build a content calendar or editorial plan, develop a campaign concept or go-to-market
  (GTM) plan, define a brand voice or tone, write a value proposition or positioning statement, create
  audience personas or ICPs, write SEO content briefs, plan an email sequence or newsletter, design a
  conversion-rate-optimization (CRO) test, analyze competitor positioning, write release notes, a
  changelog, or a feature announcement, build sales enablement assets (battle cards, one-pagers), plan
  organic social or a platform-specific post, buy paid ads or structure a media-buying campaign, write a
  press release or media pitch or handle PR and crisis communications, run an influencer, affiliate, or
  co-marketing partnership, localize or transcreate marketing into another language or market, check
  marketing for legal compliance or required disclosures (advertising claims, endorsements, email/privacy
  law, regulated categories), or measure marketing performance. Make sure to use this skill whenever the user mentions attracting customers, growing an
  audience, launching a product, increasing conversions, communicating value, or any task that touches
  marketing copy or strategy — even if they don't explicitly say the word "marketing." This includes
  casual, non-marketer phrasings like "nobody's clicking / buying / signing up," "my page / ad / email
  isn't working / converting," "I'm not getting customers / traffic / leads," "how do I get people to
  notice / buy / care," "write something for my website / post / email," or "words for my homepage."
---

# Marketing Skill

A rigorous, end-to-end marketing skill. It does two things well: produces sharp, ready-to-use
**deliverables** (copy, briefs, plans) and applies disciplined **strategy frameworks** so the output is
grounded rather than generic. The defining principle of this skill is that good marketing is specific,
evidence-led, and built around the reader — not the brand.

This file is the orchestration layer. It tells you how to approach any marketing task and routes you to
the right deep-dive reference. Read the relevant reference file(s) in `references/` before producing a
deliverable in that area — they contain the detailed frameworks, checklists, formulas, and quality bars
that make the difference between competent and excellent output.

---

## How to use this skill

**Step 0 — Check for a brand profile.** If the project contains a `brand.md` (project root, or next to
this skill), read it before anything else. It is the user's standing brief — company, audience, voice
and tone rules, and proof on file (real stats, testimonials, case studies). Treat its contents as ground
truth for the five brief elements below: don't re-ask what it already answers, draw proof from its
"proof on file" section instead of using placeholders, and follow its voice rules in every deliverable.
Anything the user says in-session overrides it.

If there is no `brand.md`, proceed normally — but watch for the moment to start one. **Whenever the user
volunteers durable brand facts in-session — their audience, voice or tone rules, a real stat or
testimonial, a positioning or differentiator — deliver what they asked for first, then end your response
by offering to save those facts as a `brand.md`** so they don't have to repeat them next session. This is
not optional politeness; a user who just handed you their voice rules and a sourced stat should always be
offered the profile. The same applies when you find yourself asking scoping questions they've plainly
answered before. Two ways to draft it: (a) fill the template sections (company, audience, voice & tone,
proof on file, standing constraints) from what you've learned in-session, or (b) if you have a web-fetch
tool and the user has a live site, offer to fetch their homepage and draft `brand.md` from it. Either way,
show the draft and let the user correct it before saving — it's their standing brief, not yours.

**Step 0.5 — Ground in product truth when it's at hand.** When you're working inside the product's own
repository, or have tools that can see the real thing, use them before guessing. Skim the README, docs,
or landing-page source for what the product actually does, and prefer real feature names, limits, and
numbers over invented ones. The same goes for research tasks: if you have web access, read a
competitor's actual site rather than reasoning about it from memory. Real proof you found beats a
placeholder; a placeholder beats an invention.

**Step 1 — Establish the brief before writing.** Marketing output is only as good as its inputs. Before
producing anything, make sure you know (or have reasonably inferred and flagged) these five things. This
is the single most important habit in this skill.

1. **Audience** — who specifically is this for? (role, situation, what they believe right now)
2. **Goal** — what one action should this drive? (click, sign-up, purchase, reply, share)
3. **Offer/product** — what is being marketed, and what's the single most important thing about it?
4. **Proof** — what evidence supports the claims? (metrics, testimonials, mechanism, credentials)
5. **Constraint** — channel, length, tone, brand rules, or anything that bounds the output.

If the user hasn't given you these, how you proceed depends on the task. There are two task types where
you must STOP and gather inputs first — do not produce the deliverable on assumptions:

**Gate A — Single load-bearing strategy statements (positioning statement, value proposition, messaging
hierarchy, brand voice/tone definition).** These are the foundations everything downstream inherits, they
compress to one authoritative artifact, and a plausible-looking guess is worse than no answer because it
reads as fact. ONLY these four hard-stop. Ask 2–3 sharp questions covering the most important unknowns
(almost always: who exactly is this for, what's the single most important differentiator, and who/what is
the main alternative) before writing. Do not output a positioning statement built on guessed inputs.

Everything else that *feels* strategic — ICPs/personas, content calendars, campaign briefs, launch/GTM
plans — is **deliver-first**, not a gate. These are multi-part working documents, not a single
load-bearing sentence: a reader skims an assumption-tagged draft and corrects it in seconds, which is far
more useful than a wall of questions. See the deliver-first rules below; do not hard-stop on them.

**Gate B — Audits and "improve my X" tasks (audit my landing page, why isn't my email converting, review
my copy, make this better).** You cannot meaningfully audit an asset you cannot see — but asking is the
*last* resort, not the first. If the user gave a URL and you have a web-fetch or browser tool, fetch the
page yourself and audit the live asset. If the asset plausibly lives in the current project (a landing
page in the repo, an email template, README copy), look for it before asking. Only when you cannot see
the asset by any means do you stop and ask the user to share it (paste the copy, share the URL, or upload
a screenshot) plus the goal and audience. If they can't share it, say what you'd need and offer a generic
checklist instead — but make clear a real audit requires seeing the real thing. Do not invent the
contents of the asset and audit your own invention.

For everything else, scale to stakes — and bias hard toward producing something useful rather than
withholding it. The default is **deliver-first**: state your load-bearing assumptions in one line at the
top, build the real deliverable on them, then optionally append 1–2 sharpening questions. Asking instead
of delivering is the failure mode, not diligence.
- **Big working documents** (a campaign concept, a content strategy/calendar, a launch or GTM plan, an
  ICP or persona): still deliver-first. Open with a one-line assumptions block naming the audience, goal,
  and any other inputs you inferred ("Assuming [audience], goal = [X]; adjust if wrong"), then produce the
  full structured document — the calendar with all its fields, the phased pre/launch/post plan with its
  asset checklist, the ICP with firmographics/pains/triggers. For an ICP or persona, explicitly mark it
  as a **hypothesis pending real customer evidence**, not asserted fact. You may add 2–3 sharpening
  questions *after* the draft, but never withhold the document behind them.
- **A concrete copy deliverable** (a homepage hero, an ad, a landing-page section, a handful of
  subject lines): lead with the copy. Even when the audience or angle is unstated, pick the single
  most likely one, name it in a one-line assumption at the top ("Assuming [X]; adjust if wrong"), and
  write the deliverable anyway. A concrete draft built on a named assumption is far more useful than a
  list of questions: the reader corrects a wrong assumption in seconds, and most of the copy still
  holds. For these requests, **asking first is the failure mode, not diligence** — produce the draft,
  then you may add 1–2 optional sharpening questions *after* it. This is the one place the "never guess
  the audience" rule below bends: stating a guess out loud and building on it is exactly what we want;
  only a *silent, unstated* guess is forbidden.

Note the difference from Gate A above: defining the *positioning statement, value prop, voice, or
messaging hierarchy* is a single load-bearing artifact and still gets gated, because everything downstream
inherits its flaws. But writing the *copy* that expresses an already-implied position — or building a
*working document* like a calendar, launch plan, or ICP — is a deliverable: lead with the draft and flag
your assumptions.

Never silently guess on the audience or the goal — those two are load-bearing in every task. Stating
an assumption out loud is fine; hiding one is not.

**What a good brief-first ask looks like** (keep it to 2–3 questions, make them sharp, don't interrogate):

> *Before I write this positioning statement, three quick things so it's sharp rather than generic:*
> 1. *Who exactly is this for — what's the narrowest core audience? (e.g. "agencies of 10–50," not "businesses")*
> 2. *What's the one thing you do that the main alternatives don't?*
> 3. *Who or what are you really competing against — a rival tool, a spreadsheet, or just doing nothing?*

Then write the deliverable using their answers. If they decline to answer, fall back to stated assumptions
and flag that sharpening the inputs would improve the result.

**Step 2 — Route to the right reference.** Match the task to the table below, read that reference file,
then produce the deliverable following its frameworks.

**Step 3 — Apply the universal quality bar (below) to everything**, regardless of task.

**Step 4 — Deliver ready-to-use output, then optionally annotate.** Write the actual copy or build the
actual plan. Don't hand back a description of what could be written. After the deliverable, you may add a
short "why this works" note or offer variants, but the deliverable comes first.

---

## Routing table

| If the task involves... | Read this reference |
|---|---|
| Ads, emails, landing pages, homepages, CTAs, taglines, product/sales copy, social posts, any writing | `references/copywriting.md` |
| Brand voice, tone, messaging hierarchy, value prop, positioning, boilerplate, naming | `references/brand-messaging.md` |
| Content calendars, editorial plans, content pillars, blog/social strategy, repurposing | `references/content-strategy.md` |
| Campaign concepts, product launches, GTM plans, campaign briefs, promotions | `references/campaigns.md` |
| Competitor analysis, audience personas, ICPs, market/positioning audits, segmentation | `references/research.md` |
| SEO content briefs, keyword strategy, search intent, on-page optimization | `references/seo.md` |
| Email sequences, nurture flows, newsletters, lifecycle/drip campaigns | `references/email-lifecycle.md` |
| CRO, A/B testing, funnel optimization, conversion audits | `references/cro.md` |
| Metrics, KPIs, attribution, reporting, what to measure and how | `references/measurement.md` |
| Release notes, changelogs, feature announcements, battle cards, sales one-pagers, dev-audience marketing | `references/product-marketing.md` |
| Character limits, image sizes, or format specs for any channel (ads, email, social, SEO, app stores) | `references/specs.md` |
| Organic social strategy, platform mechanics (LinkedIn/X/Instagram/TikTok), hooks, what travels per platform | `references/social-media.md` |
| Paid ads buying — channel selection, account structure, bidding, budget, creative testing, scaling | `references/paid-media.md` |
| PR, press releases, media pitches, earned media, thought leadership, crisis communications | `references/pr-comms.md` |
| Influencer/creator marketing, affiliate programs, co-marketing partnerships, sponsorship, disclosure | `references/partnerships.md` |
| Translating/localizing marketing into another language or market, transcreation, taglines across locales | `references/localization.md` |
| Advertising/marketing legal compliance, required disclosures, claim substantiation, email/privacy law, regulated-category or dark-pattern questions | `references/compliance.md` |

If a task spans several areas (e.g. "launch plan for my app"), read each relevant reference and synthesize.
A launch typically needs `campaigns.md` + `copywriting.md` + `email-lifecycle.md` + `measurement.md`.

---

## Universal quality bar

Apply these to every deliverable. When reviewing your own draft, check it against this list before
delivering. This is what separates this skill's output from a generic AI response.

**Specificity**
- Replace every vague adjective ("amazing", "powerful", "seamless", "robust", "innovative") with a
  concrete claim, number, or outcome. If you can't, the claim probably isn't true enough to make.
- "Save 3 hours a week on invoicing" beats "Boost your productivity." Numbers, timeframes, and named
  outcomes beat abstractions every time.

**Reader-first**
- Lead with the reader's problem or desire, not the product's features. Features answer "what is it";
  benefits answer "what does it do for me"; outcomes answer "what does my life look like after."
- The product is the bridge between where the reader is and where they want to be. Frame it that way.

**One message per piece**
- Every asset has exactly one job. A landing page that argues three things convinces of none. A campaign
  with three core messages has no core message. Pick the one that matters most.

**Proof over claims**
- Every significant claim needs support: a statistic, a testimonial, a demonstrable mechanism, a
  credential, or a specific example. Unsupported superlatives erode trust.

**Mechanics**
- Active voice. Short sentences. Cut filler ("in order to" → "to"; "it is important to note that" → delete).
- Cut adverbs that prop up weak verbs. Strong verb > weak verb + adverb.
- Read it aloud in your head. If you stumble, the reader will too.
- Match reading level to audience: B2C consumer copy should read at roughly grade 6–8; technical B2B can
  go higher but still rewards clarity.

**Earn the next line**
- The only job of the headline is to get the subhead read. The only job of the first line of an email is
  to get the second line read. Momentum is everything in copy.

**Honesty**
- No fabricated statistics, fake testimonials, or invented credentials. If proof doesn't exist, don't
  invent it — but **still write the full deliverable**, dropping in clearly-marked placeholders where the
  proof goes (e.g. `[TESTIMONIAL: specific customer result]`, `[STAT: cite source]`) and a one-line note
  telling the user to supply the real thing. Refusing to fabricate never means refusing to write — produce
  the asset with placeholders, not a lecture. Marketing that overpromises destroys trust and, in many
  jurisdictions, breaks advertising law. When a task touches required disclosures, claim substantiation,
  email/privacy law, regulated categories, or dark patterns — or a user asks for something over the line —
  read `references/compliance.md`: it's the concrete version of this rule (what must be disclosed, what
  can't be claimed, and how to redirect a non-compliant request to a clean version that still works).

---

## Output format conventions

- **Copy deliverables**: write the finished copy. If producing for a specific medium, format it the way it
  will actually appear (subject line + preview text + body for email; headline + subhead + CTA for a hero
  section). Label sections so the user can map them to where they go.
- **Strategy deliverables**: produce a structured document the user can act on immediately — clear headings,
  tables where they aid scanning, and concrete next steps. Avoid walls of prose.
- **Variants**: for high-leverage single elements (subject lines, headlines, primary CTAs, taglines),
  offer 3 distinct options that take genuinely different angles — not three rewordings of the same idea.
  Label each with the angle it takes (e.g. "Curiosity", "Direct benefit", "Social proof").
- **Assumptions**: when you've inferred anything load-bearing, state it in one line at the top:
  "Assuming [X]; adjust if wrong."

---

## A note on judgment

The frameworks in the reference files are scaffolding, not law. PAS, AIDA, the funnel, content ratios —
these are reliable defaults that prevent common failures, but a skilled marketer breaks them deliberately
when the situation calls for it. Use the frameworks to avoid generic output and obvious mistakes; use
judgment to know when a brand, audience, or moment warrants something different. When you do deviate,
deviate on purpose and be able to say why.
