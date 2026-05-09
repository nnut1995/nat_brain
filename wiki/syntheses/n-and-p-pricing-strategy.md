---
title: N&P Pricing Strategy — Yield, Peak, and the Unlimited Leak
type: synthesis
created: 2026-05-09
updated: 2026-05-09
tags: [pricing, yield-management, gym-strategy, n-and-p]
sources: ["[[wiki/sources/n-and-p-boxing-gym]]", "[[wiki/sources/2026-05-02-nandpmuaythai-com]]"]
related: ["[[wiki/entities/n-and-p-boxing-gym]]"]
---

# N&P Pricing Strategy — Yield, Peak, and the Unlimited Leak

## Context

[[wiki/entities/n-and-p-boxing-gym]] runs group classes 14:00–20:00 with **3 trainers × 2 students = 6 seats per hourly slot**. The 18:00 and 19:00 slots are reported by the owner as **always full, almost entirely with monthly-unlimited members**. This synthesis answers two linked questions:

1. How should pricing change to maximize profit given the peak-hour bottleneck?
2. Should capacity be expanded by adding freelance trainers at 18:00–20:00, or by extending hours to 22:00?

## TL;DR

- The gym's **scarcest resource (peak seats) is being consumed by its lowest-yield customers (unlimited members)**. Marginal revenue per peak booking is effectively zero.
- The 1-month unlimited plan is **cheaper than the 10-pack** for anyone training ≥12×/month. The 12-month plan collapses to **~156 THB/session** for a 4×/week trainer, less than half the 10-pack effective rate.
- Fix pricing **before** spending on capacity. Expanding peak supply today subsidizes zero-marginal users.
- Recommended sequence: (1) split unlimited into Off-Peak vs All-Access, (2) re-anchor long-duration unlimited tiers, (3) cap unlimited peak bookings, (4) lift private prices, (5) only then evaluate freelance vs hour extension.

## The yield leak — math

Effective per-session rate (THB) under the current published menu ([[wiki/entities/n-and-p-boxing-gym]]):

| Plan | Sticker | Effective per session |
|---|---|---|
| Single | 400 | 400 |
| 10-pack | 3,500 | 350 |
| 30-pack | 9,000 | 300 |
| 1-mo unlimited | 3,990 | 333 at 12×/mo · **200 at 20×/mo** |
| 3-mo unlimited | 9,990 | 3,330/mo |
| 6-mo unlimited | 17,990 | 2,998/mo |
| 12-mo unlimited | 29,990 | 2,499/mo · **156 at 16×/mo** |

Two structural problems:

1. **The 1-month unlimited undercuts the 10-pack** for anyone training ≥12×/month. There is no rational reason for a frequent trainer to buy a session pack — they all funnel into unlimited.
2. **Long-duration tiers compound the discount**. 12-month at 2,499/mo is a ~37% discount vs the 1-month rate, on top of the per-session collapse. Heavy committed trainers — exactly the population most likely to take peak slots — pay the lowest yield.

Combined effect: the customers with the **highest demand for the scarcest inventory** pay the **lowest marginal price**. This is the inverse of what yield management requires.

## Move 1 — Split unlimited into Off-Peak vs All-Access

Introduce two unlimited tracks gated by class time:

- **Off-Peak Unlimited** — valid 14:00–17:00 only. Keep current pricing.
- **All-Access Unlimited** — valid 14:00–20:00. Price at +30–40% over Off-Peak.

Indicative ladder:

| Duration | Off-Peak | All-Access |
|---|---|---|
| 1 month | 3,990 | ~5,500 |
| 3 months | 9,990 | ~13,990 |
| 6 months | 17,990 | ~24,990 |
| 12 months | 29,990 | ~39,990 |

Effects:
- Price-sensitive frequent trainers self-sort into Off-Peak, freeing 18:00–19:00 seats.
- Daytime slots (14:00–17:00) — currently underutilized — get filled by demand that already exists.
- Customers who *need* peak pay for it; the headline "unlimited" price doesn't go up, which protects acquisition.

## Move 2 — Re-anchor the long unlimited plans

The current 6-mo and 12-mo plans embed too-steep loyalty discounts. Suggested ladder (applies to All-Access; scale Off-Peak proportionally):

| Duration | Current | Proposed | Implied per-month |
|---|---|---|---|
| 1 mo | 3,990 | 3,990 | 3,990 |
| 3 mo | 9,990 | 10,990 | 3,663 |
| 6 mo | 17,990 | 19,990 | 3,332 |
| 12 mo | 29,990 | 35,990 | 2,999 |

The 12-month commitment is still rewarded, but a 4×/week trainer no longer trains for 156 THB/session. Migrate existing members at renewal, not retroactively.

## Move 3 — Soft cap on peak bookings for unlimited

Even after Moves 1 and 2, add a soft cap on the All-Access plan:

- Included: **12 peak bookings (18:00 or 19:00) per month**.
- Beyond the cap: **+200 THB top-up** per peak booking, or shift to a non-peak slot for free.

Rationale:
- Avoids a hard "no peak" feel that damages the value proposition.
- Recovers yield from the heaviest peak users without changing the headline plan.
- Generates booking-discipline data (who actually consumes peak how often) — input for further tuning.

## Move 4 — Lift private prices

Privates run **07:00–12:00**, a window with **no group-class capacity competition** ([[wiki/entities/n-and-p-boxing-gym]]). Capacity cost is ~zero, so private pricing should be set on willingness-to-pay, not on parity with group rates.

Current private rates:

| Package | Price | Per session |
|---|---|---|
| 1 session | 700 | 700 |
| 10-pack | 5,990 | 599 |
| 30-pack | 14,990 | 500 |

Issues:
- Single private at 700 is only **1.75×** a single group class — for 1-on-1 attention and 50% more time (90 min vs 60 min).
- 30-pack effective rate (500) is barely above the *group* 30-pack (300).

Proposed:

| Package | Proposed | Per session |
|---|---|---|
| 1 session | 900–1,000 | 900–1,000 |
| 10-pack | 7,990 | 799 |
| 30-pack | 17,990 | 600 |

This is pure-margin revenue: privates do not compete with peak.

## Move 5 — Then, and only then, decide on capacity expansion

Two options were on the table:

- **A. Add a 4th (freelance) trainer at 18:00–20:00.** Adds 2 seats per peak slot.
- **B. Extend group class hours to 22:00.** Adds 4 new slots (20:00, 21:00) at full 6-seat capacity = 24 seats/day.

Why pricing has to come first:

- Today, the marginal unlimited booking at peak generates **~0 THB**. A freelance trainer is paid per session.
  → Adding peak supply *before* pricing reform means **paying a freelancer to serve zero-yield demand**.
- Once Moves 1–3 are live, peak seats carry positive marginal revenue. The freelance ROI calculation becomes simple: `(filled peak seats × average peak yield) − freelancer cost`.

After pricing reform, the comparison:

| Factor | A. Freelance at 18:00–20:00 | B. Extend to 22:00 |
|---|---|---|
| Demand risk | **Low** — peak demand is proven and overflowing | **High** — late-evening demand is unproven; gym demand typically drops sharply post-20:00 in Bangkok |
| Cost shape | Variable (per-session freelance fee) | Fixed (rent, utilities, front desk, cleaning) + variable trainer cost |
| Setup cost | Near zero (find a freelancer) | Possible permitting/operational changes; staff schedule overhaul |
| Reversibility | Trivially reversible | Hard to reverse (committed schedule, customer expectations) |
| Cannibalization | Low | Some All-Access users may shift from 19:00 → 21:00 if it's less crowded |

**Recommendation: A first, B only if data demands it.**

After 1–2 months of pricing reform, observe:
- Are 18:00–19:00 *still* full at the new yield? → Freelance trainer at peak is a clear win.
- Is there spillover demand asking for later slots? → Pilot a *single* 20:00 slot for 4–6 weeks before committing to 21:00–22:00.

## Implementation checklist

- [ ] Decide naming for the two unlimited tracks (e.g. "Daytime" vs "All-Day", or "Flex" vs "Prime").
- [ ] Update website + Line OA + Facebook with the new tier table. Mirror to the source pages: [[wiki/sources/2026-05-02-nandpmuaythai-com]], [[wiki/sources/n-and-p-boxing-gym]].
- [ ] Decide migration policy: existing members keep current plan until renewal; new sign-ups on new menu from day one.
- [ ] Configure booking system to enforce time-window restriction on Off-Peak plans and the 12-booking peak cap on All-Access.
- [ ] Communicate to existing peak regulars **before** the change — frame as "we're adding an Off-Peak option that's cheaper" rather than "we're raising prices on peak."
- [ ] Track for 4 weeks: peak fill rate, off-peak fill rate, peak top-up revenue, churn at renewal, pay-per-session bookings at peak.
- [ ] Re-evaluate freelance / hour-extension question with that data in hand.

## Open questions

> [!question] To confirm with the gym owner
> - Does the current monthly membership cover **both** group and private, or group only? ([[wiki/sources/n-and-p-boxing-gym]] flagged this as an open data gap.)
> - What % of peak (18:00–19:00) bookings come from unlimited vs pay-per-session today? Without this, the size of the leak is estimated, not measured.
> - How many active 6-mo and 12-mo members exist? Migration risk scales with this.
> - Is there a booking system that can enforce time-window restrictions, or does this require manual gating?
> - What is the freelance trainer market rate per session in Rama 2? Sets the threshold for Move 5A.

## Cross-links

- Entity: [[wiki/entities/n-and-p-boxing-gym]]
- Source pages: [[wiki/sources/n-and-p-boxing-gym]], [[wiki/sources/2026-05-02-nandpmuaythai-com]]
- Adjacent strategy work: [[wiki/syntheses/n-and-p-two-plans-local-and-staycation]], [[wiki/syntheses/n-and-p-boxing-gym-social-media-ads-plan]]
