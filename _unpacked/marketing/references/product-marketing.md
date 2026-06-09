# Product Marketing Reference

The recurring assets that sit between product and market: release notes, feature announcements, naming,
and the material sales actually uses. For full product *launches* (phased plans, GTM), read
`campaigns.md` — this module covers the steady-state work between launches.

## Table of contents
- [Release notes & changelogs](#release-notes--changelogs)
- [Feature announcements](#feature-announcements)
- [Feature naming](#feature-naming)
- [Battle cards](#battle-cards)
- [Sales one-pagers](#sales-one-pagers)
- [Marketing to developers](#marketing-to-developers)
- [Quality bar](#quality-bar)

---

## Release notes & changelogs

Two documents that get conflated. Decide which one you're writing first:

- **Changelog** — for developers and integrators. Precise, complete, conventional. Every change listed,
  grouped `Added / Changed / Fixed / Deprecated / Removed / Security`, breaking changes flagged loudly at
  the top, version and date on every entry. Dry is correct here.
- **Release notes** — for users. Curated, benefit-led, written in the product's voice. Not every change —
  the changes a user would *care* about, leading with the biggest one.

**Release notes structure:**
1. **Lead with the headline change** — one feature, framed as what it lets the user do, not what was built.
2. **Group the rest**: New / Improved / Fixed, each item one line, outcome first.
3. **Link out** for depth (docs, demo) rather than explaining inline.
4. **Breaking changes and deprecations go first, not last** — burying them is how you burn trust.

**The translation move** — release notes are written by translating engineering reality into user outcome:

| Engineering reality | Release note |
|---|---|
| "Fixed race condition in sync worker" | "Sync no longer drops changes when you edit on two devices at once" |
| "Added pagination to /v2/contacts endpoint" | "Contact lists with 10k+ entries now load in under a second" |
| "Migrated export pipeline to streaming" | "Exports that used to time out now finish — even at 1M rows" |

The pattern: name the situation the user was in, then what's different now. If you can't say what the
user-visible difference is, it belongs in the changelog, not the release notes.

**Voice:** confident, specific, zero hype. "Improved performance" is a non-statement — say what got
faster and by how much, or cut it.

---

## Feature announcements

**First decision: does this feature deserve an announcement at all?** Tier it:

| Tier | What qualifies | Treatment |
|---|---|---|
| **1 — Flagship** | Changes who the product is for or why it wins; competitive headline material | Full launch — read `campaigns.md` and build the phased plan |
| **2 — Notable** | Solves a known pain for a meaningful segment | Blog post + email + social + in-app notice |
| **3 — Routine** | Improvements users will be glad to find | Release notes + in-app changelog, nothing more |

Announcing everything at Tier 2 trains the audience to ignore announcements. Most features are Tier 3;
that's healthy.

**Announcement structure (any channel):**
1. **What changed** — one sentence, concrete, no preamble about your journey.
2. **Why you'd care** — the job it unlocks or the pain it removes, for a named kind of user.
3. **How to try it** — one CTA, lowest possible friction (a link into the feature, not to a docs index).
4. **Availability** — which plans, regions, platforms; rollout timing if staged. Omitting this generates
   support tickets and resentment from users who can't find the feature.

**In-app announcements:** one sentence + one button. The user is mid-task; you're interrupting. Earn it
or don't ship it.

---

## Feature naming

**Default to descriptive, not branded.** "Scheduled exports" beats "FlowSync™" — a descriptive name does
its own marketing every time it's said, and costs nothing to learn. Reserve branded names for genuine
flagship differentiators you intend to invest in (the feature that headlines the homepage).

**Test any candidate name against:**
1. **Self-explanatory** — can a user guess what it does from the name alone?
2. **Say-able** — does it survive being said aloud in a sales call or a tweet?
3. **No collision** — not already a competitor's feature name, a generic category term, or a trademark.
4. **System-consistent** — fits the existing naming pattern (don't mix "Smart X" / "X Pro" / "FlowX"
   conventions in one product).
5. **Survives translation** — no unfortunate meanings or untranslatable puns in your main markets.

Renaming a shipped feature is expensive (docs, support muscle memory, SEO) — name it right once, or keep
it descriptive until it earns a brand.

---

## Battle cards

A one-page internal asset a rep can scan **mid-call**. Density and honesty are the whole game.

**Structure (one page, hard limit):**
1. **Competitor snapshot** — 2–3 lines: what they are, who they sell to, current pricing posture.
2. **Where we win** — 3–5 points, each tied to proof (a benchmark, a case study, a capability they lack).
   Claims a rep can't back up get them embarrassed in the room.
3. **Where they win** — yes, honestly. A card that pretends the competitor has no strengths dies in the
   field: the first time a rep gets blindsided by a real competitor strength the card didn't mention, they
   stop trusting the card. Knowing where you lose also tells reps which deals to qualify out of.
4. **Objections & responses** — the 3–5 things prospects actually say ("they're cheaper", "we already use
   them"), each with a response that reframes rather than argues.
5. **Landmines** — questions to plant that expose the competitor's weaknesses ("Ask them how X handles
   more than 50 seats").
6. **Proof points** — the specific case studies, numbers, and references that back the win column.

**Maintenance:** a battle card has a freshness date on it. Stale cards are worse than no cards —
assign an owner and a review cadence (quarterly, or on any competitor pricing/launch event).

---

## Sales one-pagers

The key insight: the person who reads a one-pager is usually **not the person you gave it to**. It gets
forwarded to the economic buyer who wasn't on the call. Write it for *that* reader — cold, busy, senior,
skimming.

**Structure:**
1. **Header** — product name + one-line value proposition (outcome, audience, differentiator).
2. **The problem** — 2–3 lines naming the pain in the buyer's terms. The forwarded-to exec should think
   "yes, we have that."
3. **The solution** — 3 pillars max, each one line of benefit + one line of how. Not a feature list.
4. **Proof** — one strong customer result with a number, plus logos if available.
5. **CTA + contact** — what happens next and who to reach.

One page means one page. Every addition dilutes the three pillars. If sales wants more depth, that's a
second asset (an FAQ doc, a technical brief), not a longer one-pager.

---

## Marketing to developers

Developers are a distinct audience with an allergy to marketing — these rules override the general
playbook when the audience is technical:

- **Show, don't claim.** A code snippet, a benchmark table, or a terminal recording outperforms any
  adjective. "Fast" is noise; "p99 latency 23ms at 10k req/s, benchmark repo here" is marketing.
- **Docs are the marketing.** Developers evaluate by reading docs and trying the quickstart before ever
  talking to you. Gating docs behind a signup form is a conversion killer, not a lead generator.
- **Precision is trust.** Exact version numbers, real limits ("up to 100 req/min on the free tier"),
  public pricing. Vagueness reads as either ignorance or concealment — both fatal.
- **Write like an engineer explaining to a peer.** The Hacker News / Reddit test: would this post get
  shredded for marketing-speak? Plain claims, acknowledged trade-offs, no superlatives.
- **The changelog is a marketing channel.** A precise, frequent changelog signals a live, honest product
  more credibly than any "we ship fast" banner.
- **Admit limitations before they're discovered.** "Not a fit if you need X" earns more trials than
  pretending to be everything — developers reward candor and punish discovery of hidden gaps.

---

## Quality bar

Before delivering any product-marketing asset, check:

1. Is every change framed as a user outcome, not an implementation detail (release notes) — or precisely
   and completely, with breaking changes first (changelog)?
2. Is the feature tiered honestly — does this actually warrant the announcement treatment chosen?
3. Does the announcement say who gets it, on what plan, when?
4. Could a rep defend every claim on the battle card in the room, with the proof point next to it?
5. Does the card admit where the competitor wins?
6. Would the one-pager survive being forwarded to an exec who's never heard of the product?
7. If the audience is developers: zero hype adjectives, claims backed by something runnable or
   measurable, limitations stated?
