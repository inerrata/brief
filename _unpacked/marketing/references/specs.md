# Channel Specs Reference

A cheat sheet of character limits, dimensions, and format constraints per channel. Use it to make
deliverables correct on the first pass — a 45-character Google Ads headline isn't a draft, it's a rejection.

**How to use these numbers.** Platforms change limits without notice. Treat everything here as a *safe
working limit*: a number that fits today and leaves margin. Where display truncation differs from the hard
cap (LinkedIn allows 3,000 characters but cuts the preview at ~210), write to the truncation point — the
hard cap is the platform's problem, the truncation point is the reader's. Before a high-stakes launch,
verify the live limit in the platform's current docs and say so in the deliverable.

## Table of contents
- [Universal rules](#universal-rules)
- [Search ads](#search-ads)
- [Social ads](#social-ads)
- [Organic social](#organic-social)
- [Email](#email)
- [SEO & web](#seo--web)
- [Video](#video)
- [Display ads](#display-ads)
- [App stores](#app-stores)
- [SMS & push](#sms--push)

---

## Universal rules

- **Front-load.** Assume every field gets cut at half its limit on someone's screen. The first 2–3 words
  carry the message.
- **Mobile-first truncation.** Mobile cuts sooner than desktop everywhere. If a limit has a range, write
  to the short end.
- **Count characters, not words** — and count spaces and emoji (emoji often count as 2+).
- **Design video for sound-off** — most feed video plays muted. Captions or on-screen text are not optional.

---

## Search ads

**Google Responsive Search Ads (RSA):**

| Field | Limit |
|---|---|
| Headlines | up to 15, **30 chars** each |
| Descriptions | up to 4, **90 chars** each |
| Display path | 2 fields, **15 chars** each |

- Google mixes and matches headlines/descriptions — every headline must stand alone *and* combine sensibly
  with any other. Don't write three headlines that only work in sequence.
- Pin sparingly (pinning reduces the optimization space); pin only for compliance-required text.
- Include the target keyword in at least 2 headlines; vary the rest by angle (benefit, proof, CTA, offer).

**Microsoft Ads:** same shape (15 × 30, 4 × 90) — write once, reuse.

---

## Social ads

**Meta (Facebook/Instagram):**

| Field | Safe limit |
|---|---|
| Primary text | **~125 chars** before "See more" (hard cap much higher) |
| Headline | **~27 chars** visible |
| Description | **~27 chars** (often not shown) |

- Images: **1:1** (1080×1080) for feed, **4:5** (1080×1350) for mobile feed, **9:16** (1080×1920) for
  Stories/Reels.
- Stories/Reels safe zones: keep text out of roughly the top 14% and bottom 20% — UI overlays live there.
- Less text on the image still outperforms, even though the old 20%-text rule is retired.

**LinkedIn:**

| Field | Safe limit |
|---|---|
| Intro text | **~150 chars** before truncation (cap 600) |
| Headline | **70 chars** before truncation (cap 200) |
| Single image | 1200×627 |

**X/Twitter ads:** body **280 chars**; website-card headline **70 chars**.

---

## Organic social

| Platform | Hard cap | Truncation point (write to this) |
|---|---|---|
| LinkedIn post | 3,000 | **~210 chars** desktop / ~140 mobile before "…see more" |
| X/Twitter | 280 | n/a — the cap is the format |
| Instagram caption | 2,200 | **~125 chars** before "… more" |
| Facebook post | 63,206 | **~477 chars** |
| TikTok caption | 2,200 | first line — the video is the content |
| Threads | 500 | n/a |
| Pinterest | title 100 / description 500 | title **~40 chars** in feed |

- Instagram hashtags: cap 30, use **3–5 relevant** ones; hashtag walls read as spam.
- The truncation point is your hook deadline — the line that earns the "see more" click (see
  `copywriting.md` → Social posts for hook craft).

---

## Email

| Element | Safe limit |
|---|---|
| Subject line | **30–50 chars** (mobile shows ~30–40) |
| Preview text | **40–90 chars** — complement the subject, don't repeat it |
| From name | **~20 chars** visible |
| Body width | **600–640 px** |

- Always set preview text explicitly; otherwise clients scrape the first line of body (often "View in
  browser").
- Alt text on every image; many clients block images by default — the email must make sense without them.
- Keep image-to-text ratio low and include a plain-text version: both affect deliverability (see
  `email-lifecycle.md` for the full deliverability list).

---

## SEO & web

| Element | Safe limit |
|---|---|
| Title tag | **50–60 chars** (~580 px — wide letters cut sooner) |
| Meta description | **120–155 chars** (mobile cuts ~120) |
| URL slug | 3–5 words, hyphenated, no stop-words |
| H1 | one per page; can differ from title tag |
| OG/social-share image | **1200×630** |

- Front-load the target keyword in the title tag; brand name goes at the end ("Primary benefit — Brand").
- Meta description is ad copy for the SERP: one benefit + one reason to click. Google rewrites it about
  half the time anyway — write it for the half it doesn't.

---

## Video

| Format | Length | Notes |
|---|---|---|
| TikTok | up to 10 min | sweet spot **15–60s**; hook in the first **1–2 seconds** |
| Instagram Reels | up to ~3 min | same hook rule; 9:16 |
| YouTube Shorts | up to 3 min | under 60s still the norm |
| YouTube title | 100 cap | **~70 chars** visible |
| YouTube description | 5,000 | first **~100–150 chars** show above "Show more" — put the link and hook there |
| YouTube thumbnail | 1280×720 | the thumbnail+title pair *is* the ad — write them together |
| Bumper ads | 6s exactly | one message, no buildup |
| Skippable pre-roll | 15–30s | brand + message in the first **5s** (the unskippable window) |

---

## Display ads

The IAB sizes that cover most inventory — produce these first:

- **300×250** (medium rectangle — highest volume)
- **728×90** (leaderboard)
- **320×50** (mobile banner)
- **160×600** (skyscraper)
- **300×600** (half page)
- **970×250** (billboard)

Display copy: one short headline (~5 words), optional ~10-word support line, button-style CTA. The image
does the stopping; the words do the pointing.

---

## App stores

| Field | iOS App Store | Google Play |
|---|---|---|
| App name/title | **30 chars** | **30 chars** |
| Subtitle / short description | **30 chars** | **80 chars** |
| Description | 4,000 | 4,000 (first ~80 chars show before "Read more") |
| Keywords field | 100 chars (iOS only) | n/a — Play indexes the description |

- iOS: the keywords field is invisible to users — no spaces after commas, no plurals duplicating singulars.
- Screenshots sell more than the description: first two screenshots carry the message in caption-sized text.

---

## SMS & push

| Channel | Limit |
|---|---|
| SMS | **160 chars** per segment (GSM-7); **70** if any emoji/unicode — emoji literally costs you 90 characters |
| Push title | **~30–50 chars** |
| Push body | **~120–150 chars** before truncation |

- SMS must include opt-out language where required ("Reply STOP to opt out") — count it in your budget.
- Push: lead with the payoff, not the app name (the OS already shows the app name).
