# Paid Media Reference

Buying attention: channel selection, account structure, bidding, budget, creative testing, and the metrics
that tell you whether it's working. This covers the *media-buying* discipline. For the ad **copy and creative
itself**, read `copywriting.md` (ads section); for exact field limits and image sizes, `specs.md`; for
attribution and unit economics, `measurement.md`.

## Table of contents
- [Before you spend a dollar](#before-you-spend-a-dollar)
- [Channel selection](#channel-selection)
- [Account structure](#account-structure)
- [Bidding & budget](#bidding--budget)
- [Creative testing](#creative-testing)
- [The funnel: cold / warm / hot](#the-funnel-cold--warm--hot)
- [Reading the numbers](#reading-the-numbers)
- [Scaling](#scaling)
- [Common ways to waste money](#common-ways-to-waste-money)
- [Quality bar](#quality-bar)

---

## Before you spend a dollar

Paid media amplifies what you already have — it does not fix a broken offer or a page that doesn't convert.

- **Can you afford to acquire a customer?** You need a rough **target CPA** derived from your economics: if
  LTV is $300 and you want a 3:1 LTV:CAC, your ceiling is ~$100 to acquire. Know this number before launching
  (the math is in `measurement.md`). Paid media without unit economics is how you spend fast and learn nothing.
- **Does the landing page convert?** Sending paid traffic to a weak page burns money. Fix conversion first
  (`cro.md`); a 2% → 4% page change halves your effective CPA before you touch the ad account.
- **Can you measure it?** Conversion tracking / pixel installed and tested, before launch. If you can't
  attribute a sale to a campaign, you're flying blind.
- **Is there tracked intent to capture?** Search captures existing demand; social/display *creates* it. Match
  the channel to whether demand already exists (below).

---

## Channel selection

Match the channel to the buyer's state and where they already are.

- **Search (Google/Microsoft Ads)** — captures **existing demand**. Someone is already looking; you pay to be
  the answer. Best for high-intent, known-category products ("crm for nonprofits"). Highest intent, often
  highest CPC. Start here if people are already searching for what you sell.
- **Paid social (Meta, TikTok, LinkedIn, Pinterest, Reddit)** — **creates demand** by interrupting. Best for
  visual products, impulse/discovery, and audiences defined by who they are, not what they typed. Targeting is
  by interest/behavior/lookalike. LinkedIn for B2B (expensive, precise); TikTok/Meta for B2C reach.
- **YouTube** — demand creation at scale via video; good for storytelling and consideration. Pairs with search
  to catch the demand it creates.
- **Retargeting/display** — cheap re-engagement of people who already visited. High ROAS but limited volume; a
  *closer*, not a *prospector*. Don't confuse retargeting ROAS with true incremental return.
- **Affiliate / partnerships** — pay-for-performance reach via others' audiences (see `partnerships.md`).

**Rule of thumb:** if there's search volume for your category, start with search (warm intent, fastest signal).
If the product needs to be *shown* to be wanted, start with paid social. Don't run four channels at once on a
small budget — you'll under-power all of them and learn nothing. Pick one, get it working, then expand.

---

## Account structure

Structure exists to control *what the algorithm optimizes* and *what you can read*.

- **Campaign = budget + objective.** Separate campaigns by goal (prospecting vs. retargeting, by funnel stage,
  sometimes by geo) so budgets don't bleed across intents.
- **Ad set / ad group = targeting + bid.** One audience or theme per set. On search, group tightly by keyword
  theme so the ad matches the query. On social, one audience per ad set so you can read what's working.
- **Ad = creative.** Multiple creatives per set so the algorithm can optimize.
- **Don't over-segment a small budget.** Modern algorithms (Meta Advantage+, broad match + smart bidding) often
  do better with consolidation and room to learn than with 30 tiny ad sets that never exit the learning phase.
  More structure = more control but slower learning; fewer = faster learning, less control. Match it to budget.
- **Keep enough volume per unit to exit the learning phase.** An ad set starved of conversions never optimizes.

---

## Bidding & budget

- **Let the machine bid, steer it with goals.** Manual CPC is mostly legacy; smart/automated bidding
  (target CPA, target ROAS, max conversions) wins when you feed it a clean conversion signal and enough volume.
- **Pick the bid strategy that matches your constraint:** target CPA when you have a cost ceiling, target ROAS
  when revenue varies per sale, max conversions/value when you want to spend a fixed budget efficiently.
- **Budget enough to learn.** Each ad set needs roughly enough daily budget to generate ~enough conversions
  per week to leave the learning phase (platform-dependent; the principle is: starvation prevents optimization).
- **Don't change everything at once.** Big edits reset learning. Change one lever, give it days of data, read,
  then change the next. Patience beats fiddling — the most common rookie error is strangling campaigns before
  they have signal.
- **Dayparting/geo** are refinements for later, once you have data showing where spend converts.

---

## Creative testing

Creative is the biggest lever in paid social — more than targeting, once the audience is broad.

- **Test one variable at a time** so a result means something: hook, visual, format, angle, offer. Changing
  five things tells you nothing about which moved the needle.
- **Test angles before details.** Find the *message* that resonates (problem-led vs. proof-led vs.
  offer-led — see `copywriting.md`) before optimizing button color. Big swings first, polish later.
- **Give a test enough impressions/conversions for significance.** Calling a winner on 40 clicks is noise, not
  a result (testing methodology in `cro.md`).
- **Refresh before fatigue.** Frequency climbing and CTR dropping on the same creative = fatigue. Have the next
  batch ready; creative is consumable, not permanent.
- **Volume of distinct concepts > endless tweaks.** Most winners come from trying genuinely different ideas, not
  the tenth variation of a loser.

---

## The funnel: cold / warm / hot

Match the ask to the relationship — the single most common paid mistake is asking cold traffic to buy.

- **Cold (prospecting)** — they don't know you. Goal: earn attention and a click. Lead with the problem or a
  scroll-stopping hook; low-commitment offer (learn, watch, get the guide). Expect higher CPA; this is the top
  of the funnel.
- **Warm (engaged, site visitors, video viewers)** — they know you a little. Goal: build the case. Proof,
  comparisons, objection-handling, a stronger offer.
- **Hot (retargeting cart/pricing visitors, past customers)** — high intent. Goal: close. Direct offer,
  urgency *if real*, risk reversal. Cheapest conversions; don't mistake their high ROAS for scalable return.

A healthy account runs all three, with budget weighted to where your bottleneck is.

---

## Reading the numbers

Know which metric is diagnostic vs. which is the goal (full definitions in `measurement.md`).

- **The goal metric is CPA or ROAS**, judged against your target from "before you spend a dollar." Everything
  else is a diagnostic on the path to it.
- **Diagnose down the chain:** impressions → CTR (creative/targeting) → CPC → landing-page conversion rate
  (page/offer) → CPA. A bad CPA has a *location* — find which step is leaking before you change anything.
- **Low CTR** → creative or targeting problem. **Good CTR, bad conversion** → page/offer mismatch, not the ad.
- **Watch frequency** (fatigue) and **impression share / lost-to-budget or rank** on search (headroom).
- **Beware vanity ROAS.** Platform-reported ROAS over-credits retargeting and last-click. For real decisions,
  look at incrementality and blended CAC across the whole account, not per-platform self-reported numbers
  (attribution caveats in `measurement.md`).

---

## Scaling

- **Scale winners two ways:** raise budget gradually (≈20–30% steps so you don't reset learning), or duplicate
  into new audiences/geos. Doubling budget overnight usually spikes CPA.
- **Broaden targeting** as creative proves out — let the algorithm find buyers rather than hand-picking tiny
  audiences.
- **Watch CPA as you scale, not just spend.** Efficient at $50/day can break at $500/day; the cheapest
  audience saturates first. Scaling is finding the spend level where CPA is still acceptable, not maxing volume.
- **Keep the creative pipeline full.** Scale dies on creative fatigue more than on audience size.

---

## Common ways to waste money

- Running paid traffic to a page that doesn't convert (fix `cro.md` first).
- Launching without conversion tracking — spending blind.
- Asking cold audiences to buy with no warm-up.
- Four channels on a budget that can't power one.
- Killing campaigns before they exit the learning phase; or editing them constantly so they never stabilize.
- Optimizing to platform-reported ROAS that over-credits retargeting and ignores incrementality.
- Scaling spend faster than creative and economics can support.
- Chasing CTR or impressions (vanity) instead of CPA/CAC (the goal).

---

## Quality bar

Before launching or advising on a paid campaign, check:

1. Is there a target CPA/ROAS derived from real unit economics, set *before* spending?
2. Does the destination page convert, and is conversion tracking installed and tested?
3. Is the channel matched to the buyer's state (search = capture demand; social = create it)?
4. Does the ask match the temperature (cold → low-commitment; hot → direct)?
5. Is the test designed to isolate one variable, with enough volume to mean something?
6. Are you judging on CPA/CAC and incrementality, not vanity CTR/impressions/retargeting ROAS?
7. Is there a plan to read data before editing, and a creative pipeline ready for fatigue?
8. No fabricated performance claims; any projected number is flagged as an estimate with its assumptions.
