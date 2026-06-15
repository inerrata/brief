# Pricing Page Audit — tryloopwork.com/pricing

## First, an honesty flag

I tried to pull up your pricing page to audit it directly, and I couldn't reach it. When I look up **tryloopwork.com**, the domain returns no live web address (only an SOA/registration record — no A record pointing to a server). In plain terms: from where I'm sitting, there's nothing being served at that URL right now.

That could mean a few things:
- The domain is registered but not yet pointed at your hosting (common pre-launch).
- The live site is on a different domain or a subdomain (e.g. `app.tryloopwork.com`, `getloopwork.com`, `loopwork.com`).
- It's behind auth, a staging gate, or a region/IP block I can't pass.
- There's a temporary DNS or hosting outage.

**This is itself worth checking.** If your pricing page genuinely isn't resolving for some visitors, that's not a conversion problem — it's a "the page is invisible" problem, and it would tank conversions to zero regardless of copy or design. Before optimizing anything, confirm the page actually loads from a clean device/network (incognito, mobile data, a different country if you can). Tools like `dnschecker.org` or a quick "is it down" check will tell you fast.

So I can't give you a line-by-line audit of *your specific* page yet. Rather than guess at copy I can't see, here's what I need from you to do the real audit — plus a complete, prioritized framework you can run against the page yourself today.

---

## What I need to audit your actual page

Reply with any of these and I'll do a concrete, specific teardown:

1. **A working URL** (or staging link + access), **or** paste the page copy, **or** drop 2–3 screenshots (desktop + mobile).
2. **The numbers.** What does "isn't converting" mean concretely?
   - Page visits → clicks on a plan CTA → started checkout → completed (your funnel drop-off points).
   - Current conversion rate vs. what you expected or used to get.
   - Did it drop after a change, or has it always been low?
3. **Traffic source.** Who's landing here — cold ads, organic search, existing free users upgrading, sales-assisted? Cold traffic and warm traffic need very different pricing pages.
4. **The product + price points.** What does Loop do, who's it for, and what are the tiers/prices?
5. **What "convert" means for you** — free trial signup, paid checkout, "book a demo," or "contact sales"?

The single most useful thing you could send is a **funnel breakdown**, because it tells us *where* people quit:
- High traffic, low CTA clicks → the **offer/value isn't landing** (messaging, pricing, packaging).
- Lots of CTA clicks, few checkout completions → the **checkout/friction** is the problem (form length, payment options, surprise costs, no trust).
- People reach the page but bounce in seconds → **load speed, clarity, or wrong audience.**

---

## The audit framework — run this against your page today

These are the highest-leverage failure modes for SaaS pricing pages, roughly in the order they kill conversions. Score your page on each.

### 1. Clarity in the first 5 seconds
- Can a stranger tell **what the product does and who it's for** without scrolling? Pricing pages get traffic from people who skipped your homepage. If the page assumes context they don't have, they leave.
- Is there a one-line value reminder at the top ("The fastest way to X for Y"), not just a cold "Pricing" header?

### 2. The plans themselves (packaging > price)
- **Too many tiers** = decision paralysis. Three is the sweet spot for most; four max. If you have 5+, that's likely a culprit.
- **Is the difference between tiers obvious?** People should grasp "I'm a ___, so I pick ___" instantly.
- **Is one plan visibly recommended** ("Most popular")? Anchoring and a default dramatically lift conversion.
- **Feature lists:** are they framed as *outcomes* ("Unlimited projects," "Priority support") or as inside-baseball jargon only you understand?
- **Naming:** plain (Starter / Pro / Business) beats clever (Seedling / Voyager / Cosmos) — clever names force people to decode.

### 3. Price presentation
- **Monthly vs. annual toggle** present, with the annual savings shown explicitly ("Save 20%" / "2 months free")? Missing this is a common, easy win.
- Are you showing the **monthly-equivalent price for annual** rather than a scary lump sum?
- **Anchoring:** is the highest tier shown to make the middle one feel reasonable?
- Any **hidden costs** (per-seat math, add-ons, "contact us") that create a "wait, how much?" moment? Surprise pricing kills trust.

### 4. The CTA (this is often the quiet killer)
- Is the button **specific and low-risk** ("Start free trial," "Try it free — no card") vs. generic/scary ("Buy now," "Submit," "Sign up")?
- Does **every** tier have a visible, clickable CTA above the fold of that card?
- Is there a clear **primary** CTA, or do all buttons compete with equal weight?
- On the recommended plan, does the button **stand out visually** (color/contrast)?

### 5. Risk reversal & trust (the conversion multiplier)
Most under-converting pricing pages are missing these entirely:
- **Free trial or freemium** clearly stated, with "no credit card required" if true.
- **Money-back guarantee** or easy cancellation, stated plainly.
- **Social proof on the page itself** — logos, a testimonial, user/revenue counts, ratings. Don't make people leave to find proof.
- **Security/payment trust** signals near checkout (familiar payment logos, SSL, "cancel anytime").

### 6. Objection handling (FAQ)
- Is there a **pricing FAQ** answering the real hesitations: "What happens when I hit the limit?", "Can I switch plans?", "What if I cancel?", "Do you offer refunds?", "Is there a free plan?" A good FAQ recovers people who were one unanswered question away from leaving.

### 7. Friction & mechanics
- **Mobile.** A large share of traffic is mobile; pricing tables often break or require horizontal scrolling. Check it on a real phone.
- **Load speed.** Slow pages bleed conversions before anyone reads a word.
- **Checkout length.** Every extra field costs you. Ask only for what's essential.
- **Payment options.** Card-only vs. PayPal/Apple Pay/Google Pay can matter a lot for some audiences.
- Any **broken toggles, dead buttons, or layout bugs** (very relevant given the page didn't even resolve for me).

### 8. Match to traffic temperature
- **Cold ad traffic** needs more persuasion *on the page* (value recap, proof, risk reversal) because they don't know you.
- **Warm/existing users** need the upgrade path to be frictionless and the upgrade *reason* obvious.
- A mismatch here (e.g. sending cold ads straight to a bare pricing table) is one of the most common reasons a page "doesn't convert."

---

## My honest read

Given that I literally couldn't load the page, **start by ruling out the boring-but-fatal stuff** — is the page actually live, fast, and rendering correctly on mobile for real visitors? A surprising share of "it's not converting" problems are technical, not persuasive. Confirm the page works, then layer in the framework above (clarity → packaging → CTA → trust are the four I'd attack first).

Send me a working link or the page content + your funnel numbers, and I'll turn this from a general checklist into a specific, prioritized list of exactly what to change on *your* page and why.
