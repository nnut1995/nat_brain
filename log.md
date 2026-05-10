# Log

Chronological append-only history of operations on this wiki. Newest entries at the bottom.

> [!tip] Parseable
> Every entry header follows: `## [YYYY-MM-DD] <op> | <subject>` where `<op>` is `ingest`, `query`, `lint`, `refactor`, or `init`.
> `grep "^## \[" log.md | tail -10` shows the last 10 operations.

---

## [2026-05-02] init | Wiki bootstrapped
Created the second-brain skeleton in `/Users/natnunpanichphong/Desktop/nat_brain`.
- Wrote [[CLAUDE]] (schema and rules), [[index]] (catalog), [[log]] (this file).
- Created folders: `raw/`, `raw/assets/`, `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`, `wiki/syntheses/`.
- Seeded with one example source: `raw/2026-05-02-llm-wiki-pattern.md`, ingested as `[[wiki/sources/2026-05-02-llm-wiki-pattern]]`.
- Created starter pages: [[wiki/concepts/llm-wiki-pattern]], [[wiki/concepts/rag-vs-wiki]], [[wiki/concepts/memex]], [[wiki/concepts/three-layer-architecture]], [[wiki/entities/vannevar-bush]], [[wiki/entities/obsidian]].

## [2026-05-02] ingest | LLM Wiki — A pattern for building personal knowledge bases using LLMs
Source: `raw/2026-05-02-llm-wiki-pattern.md` (the originating idea note).
- New source page: [[wiki/sources/2026-05-02-llm-wiki-pattern]].
- New concept pages: [[wiki/concepts/llm-wiki-pattern]], [[wiki/concepts/rag-vs-wiki]], [[wiki/concepts/memex]], [[wiki/concepts/three-layer-architecture]].
- New entity pages: [[wiki/entities/vannevar-bush]], [[wiki/entities/obsidian]].
- No contradictions (first source).

## [2026-05-02] ingest | N&P Boxing Gym — Operational and Pricing Overview
Source: `raw/N & P Boxing gym.md`. Angle: **(b) reference card** — pure facts, no opinion.
- New source page: [[wiki/sources/n-and-p-boxing-gym]].
- New entity page: [[wiki/entities/n-and-p-boxing-gym]] (business; aliases: P.Paoin Muay Thai, PPAOINMUAYTHAI; pricing tables, hours, contact).
- New concept stub: [[wiki/concepts/muay-thai]] (topic seed for future gym/training sources).
- No contradictions. Open data gaps flagged on the source page (street address, whether monthly membership covers privates, trainer/lineage info).

## [2026-05-02] ingest | N&p.boxing GYM & P.Pao-In Facebook page
Source: `https://www.facebook.com/pnboxing`. Angle: public-facing business preview.
- New source page: [[wiki/sources/pnboxing-facebook-page]].
- Updated entity page: [[wiki/entities/n-and-p-boxing-gym]] with Facebook contact details and a Songkran closure note.
- Contradiction surfaced: Facebook preview shows a Songkran closure announcement, which conflicts with the earlier note's blanket claim that public holidays are open as normal.

## [2026-05-02] ingest | N&P Muaythai Camp website
Source: `https://nandpmuaythai.com/`. Angle: official website crawl.
- New raw capture saved to `ai-raw/2026-05-02-nandpmuaythai-com.md`.
- New source page: [[wiki/sources/2026-05-02-nandpmuaythai-com]].
- Updated entity page: [[wiki/entities/n-and-p-boxing-gym]] with website branding, pricing, schedule, staycation package, and contact details.
- Contradiction surfaced/confirmed: website says open on public holidays, which conflicts with the Facebook Songkran closure post.

## [2026-05-02] query | N&P Boxing Gym social media and ads plan
Filed a cross-source marketing synthesis for [[wiki/entities/n-and-p-boxing-gym]].
- New synthesis page: [[wiki/syntheses/n-and-p-boxing-gym-social-media-ads-plan]].
- Covers positioning, target audiences, content pillars, 30-day calendar, Meta ads funnel, message templates, and first 2-week action plan.
- Caveats preserved: incomplete address detail, holiday-closure contradiction, and staycation booking ambiguity.


## [2026-05-02] query | N&P Boxing Gym one-page content breakdowns
Expanded the social media plan into one execution page per content item.
- New hub page: [[wiki/syntheses/n-and-p-content/content-breakdown-index]].
- New content pages: 20 execution pages under `wiki/syntheses/n-and-p-content/`.
- Each page includes what to shoot/create, caption draft, CTA, and an ad group recommendation.

## [2026-05-02] query | N&P Boxing Gym staycation pinned Facebook poster
Created a pinned-post package for the staycation offer.
- New synthesis page: [[wiki/syntheses/n-and-p-content/staycation-pinned-facebook-poster]].
- New HTML/SVG poster artifacts: `wiki/syntheses/n-and-p-content/staycation-pinned-facebook-poster.html`, `wiki/syntheses/n-and-p-content/staycation-pinned-facebook-poster.svg`, `wiki/syntheses/n-and-p-content/staycation-pinned-facebook-poster-v2-thai-style.svg`, and `wiki/syntheses/n-and-p-content/staycation-pinned-facebook-poster-v3-english-red-logo.svg`.
- Includes poster copy, Facebook caption, export steps, and a staycation direct-inquiry ad group.

## [2026-05-02] refactor | Render staycation poster v3 to PNG
Generated the 1080×1080 image deliverable for the v3 English red/logo poster.
- New export: `wiki/syntheses/n-and-p-content/exports/staycation-pinned-facebook-poster-v3-english-red-logo.png` (1080×1080, ~390 KB).
- Rendered via cairosvg with Liberation Sans Narrow + DejaVu Sans substituted for Impact/Inter (the source SVG continues to declare Impact/Inter so apps that have them will render natively).
- Note: the source SVG references `raw/assets/IMG_7270.PNG`; the actual file is `raw/assets/logo.png`. Logo path was patched only in the working copy used for the render — source SVG unchanged. Worth fixing the SVG ref in a future edit.

## [2026-05-02] refactor | Render staycation poster v4 — Sacred Repetition (canvas-design)
Designed and rendered a museum-quality replacement poster using the canvas-design skill.
- New design philosophy: `wiki/syntheses/n-and-p-content/exports/staycation-poster-v4-design-philosophy.md` (Sacred Repetition — yantra geometry, Wai Khru four-direction reference).
- New export: `wiki/syntheses/n-and-p-content/exports/staycation-poster-v4-sacred-repetition.png` (1080×1080).
- Rendered via Pillow at 3x supersampling, downsampled with LANCZOS for crisp anti-aliasing. Uses Gloock display serif + RedHatMono technical labels + InstrumentSerif italic subhead.
- Updated [[wiki/syntheses/n-and-p-content/staycation-pinned-facebook-poster]] to point to v4 as the recommended export.

## [2026-05-03] query | N&P two-plan customer acquisition strategy
Filed a split synthesis that separates the original combined plan into two parallel tracks for [[wiki/entities/n-and-p-boxing-gym]].
- New synthesis page: [[wiki/syntheses/n-and-p-two-plans-local-and-staycation]].
- Plan 1 (Thai locals / normal class): channels TikTok-first + Line OA + Google Maps; ad funnel 1A–1D; maps existing content pages 01–10, 16–20 to this plan; adds 12 new content briefs (L1–L12) including after-work, weight-loss, women-friendly, Google Maps cadence, Line OA broadcast, referral, trainer intros, transformation, map-to-gym, schedule poster, raw-audio reel.
- Plan 2 (staycation foreigners): channels Instagram + YouTube + Reddit + partner network; ad funnel 2A–2D; maps existing pages 11–15 + staycation poster; adds 16 new content briefs (S1–S16) including day-in-the-life vlog, accommodation walkthrough, food reel, foreign student testimonial, airport guide, visa carousel, Reddit post, review push, hashtag stack, influencer collab, partner outreach, brand reel.
- Cross-plan: bilingual bio, KPIs table, and a list of facts to confirm with the gym owner (booking rules, holiday-closure contradiction, full street address, likeness consent).

## [2026-05-09] query | N&P pricing strategy given peak-hour bottleneck
Filed a synthesis answering Nat's pricing + capacity-expansion question for [[wiki/entities/n-and-p-boxing-gym]].
- New synthesis page: [[wiki/syntheses/n-and-p-pricing-strategy]].
- Core diagnosis: peak slots (18:00–19:00) are full of unlimited members whose marginal revenue per booking is ~0; the 1-mo unlimited undercuts the 10-pack at ≥12×/mo, and the 12-mo plan collapses to ~156 THB/session for 4×/week trainers — the highest-demand customers pay the lowest yield.
- Five moves in order: (1) split unlimited into Off-Peak (14:00–17:00) vs All-Access (+30–40%), (2) re-anchor 6-mo/12-mo tiers, (3) soft cap of 12 peak bookings/mo on All-Access with 200 THB top-up, (4) lift private prices (privates use empty 07:00–12:00 slots, zero capacity competition), (5) only then evaluate freelance trainer at 18:00–20:00 vs extending hours to 22:00 — recommend freelance first (proven demand, variable cost, reversible) over hour extension (unproven late-evening demand, fixed costs).
- Open questions flagged for the gym owner: monthly-plan private coverage, peak unlimited-vs-paid mix, active long-tier member count, booking-system gating capability, freelance trainer market rate.

## [2026-05-10] query | N&P ice bath ROI and pricing strategy
Filed a synthesis answering Nat's ice bath investment question for [[wiki/entities/n-and-p-boxing-gym]].
- New synthesis page: [[wiki/syntheses/n-and-p-ice-bath-roi-and-pricing]].
- Core ROI model: 100,000 THB capex; at 300 THB/session, 50 THB/session variable cost, and 3,000 THB/month fixed maintenance, 12-month payback requires ~45 sessions/month or ~1.7 sessions/day.
- Recommended pricing: avoid free unlimited use; launch 350 THB standalone, 250 THB after-class add-on, 600 THB class + ice bath bundle, 2,500 THB 10-pack, and capped member recovery add-ons.
- Decision rule: 2 paid uses/day likely supports 12-month payback; 5–6/day gives ~3–4 month payback; 10/day may pay back in under 2 months.
