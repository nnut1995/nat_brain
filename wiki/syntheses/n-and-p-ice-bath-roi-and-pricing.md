---
title: N&P Ice Bath ROI and Pricing Strategy
type: synthesis
created: 2026-05-10
updated: 2026-05-15
tags: [pricing, roi, recovery, ice-bath, n-and-p]
sources: ["[[wiki/sources/n-and-p-boxing-gym]]", "[[wiki/sources/2026-05-02-nandpmuaythai-com]]", "[[wiki/syntheses/n-and-p-pricing-strategy]]"]
related: ["[[wiki/entities/n-and-p-boxing-gym]]"]
---

# N&P Ice Bath ROI and Pricing Strategy

## Context

Nat asked whether an **~100,000 THB investment** in an ice bath / cold plunge would make sense for [[wiki/entities/n-and-p-boxing-gym]], and how to price it if the wiki did not already contain ice-bath-specific information.

The vault had **no prior ice bath / cold plunge page**. This synthesis therefore uses existing N&P operating facts and pricing anchors:

- Regular class: 400 THB single, 3,500 THB / 10 sessions, 9,000 THB / 30 sessions ([[wiki/entities/n-and-p-boxing-gym]]).
- Unlimited monthly: 3,990 THB / 1 month; 9,990 THB / 3 months; 17,990 THB / 6 months; 29,990 THB / 12 months ([[wiki/entities/n-and-p-boxing-gym]]).
- Private training: 700 THB single, 5,990 THB / 10 sessions, 14,990 THB / 30 sessions ([[wiki/entities/n-and-p-boxing-gym]]).
- Staycation package: 1,000 THB / day or 25,000 THB / month ([[wiki/sources/2026-05-02-nandpmuaythai-com]]).
- Peak group slots are already scarce and should not be given away to unlimited members without marginal revenue ([[wiki/syntheses/n-and-p-pricing-strategy]]).

## TL;DR

- A 100,000 THB ice bath investment is attractive **if the gym can sell at least ~2 paid uses/day**.
- At 300 THB/session, with 50 THB/session variable cost and 3,000 THB/month fixed maintenance, break-even for a 12-month payback is only **~45 sessions/month**, or **~1.7 sessions/day** over 26 operating days.
- Base case: 6 uses/day × 26 days × 300 THB = 46,800 THB monthly revenue and ~36,000 THB monthly net profit, implying payback in **~2.8 months**.
- Do **not** include ice bath free in unlimited membership. Use a member discount or monthly add-on with usage caps.
- Best launch product: **Muay Thai class + ice bath recovery = 600 THB**. This adds recovery revenue to existing training demand without needing a separate customer-acquisition funnel.

## Assumptions

| Input | Base assumption | Notes |
|---|---:|---|
| Capex | 100,000 THB | Ice bath / cold plunge setup |
| Operating days | 26 days/month | N&P is closed on the 15th and 16th of each month ([[wiki/entities/n-and-p-boxing-gym]]) |
| Standalone session price | 300 THB | Used for ROI model; actual menu can anchor higher |
| Variable cost | 50 THB/session | Electricity, water, cleaning, consumables; estimate to validate after launch |
| Fixed maintenance | 3,000 THB/month | Filter, chemicals, cleaning, minor repairs; estimate |
| Extra staff | 0 THB | Assumes existing team can supervise booking/check-in |

> [!warning] Caveat
> This is a financial model, not a vendor quote. Validate electricity, drainage, cleaning, filtration, and safety workflow before purchasing.

## ROI scenarios

| Scenario | Uses/day | Sessions/month | Revenue/month | Net profit/month | Payback |
|---|---:|---:|---:|---:|---:|
| Conservative | 3 | 78 | 23,400 THB | 16,500 THB | 6.1 months |
| Base | 6 | 156 | 46,800 THB | 36,000 THB | 2.8 months |
| Aggressive | 10 | 260 | 78,000 THB | 62,000 THB | 1.6 months |
| Package-heavy base | 6 | 156 | 39,000 THB | 28,200 THB | 3.5 months |

Formula:

```text
Monthly net profit = sessions × (average price − variable cost) − fixed maintenance
Payback months = 100,000 / monthly net profit
```

Base-case math:

```text
156 sessions/month × (300 − 50) − 3,000 = 36,000 THB/month
100,000 / 36,000 = 2.8 months
```

## Break-even thresholds

Sessions needed for **12-month capex payback**, assuming 50 THB variable cost and 3,000 THB monthly fixed maintenance:

| Average price | Required sessions/month | Required sessions/day |
|---:|---:|---:|
| 250 THB | 56.7 | 2.2 |
| 300 THB | 45.3 | 1.7 |
| 350 THB | 37.8 | 1.5 |
| 400 THB | 32.4 | 1.2 |

Operating-profit break-even only, before capex recovery:

| Average price | Required sessions/month | Required sessions/day |
|---:|---:|---:|
| 250 THB | 15.0 | 0.6 |
| 300 THB | 12.0 | 0.5 |
| 350 THB | 10.0 | 0.4 |
| 400 THB | 8.6 | 0.3 |

## Pricing strategy

### 1. Do not bundle ice bath free into unlimited plans

The pricing-strategy synthesis already identified an "unlimited leak": frequent users occupy scarce peak inventory while paying low marginal revenue ([[wiki/syntheses/n-and-p-pricing-strategy]]). Ice bath capacity should not repeat that mistake.

Rules:

- Unlimited members get a **discount**, not free unlimited recovery.
- Any monthly ice bath plan should have a usage cap.
- Peak post-class recovery slots should be bookable, tracked, and yield-managed.

### 2. Launch menu

| Product | Recommended price | Role |
|---|---:|---|
| First try / intro | 199 THB | Remove friction; use for launch campaign |
| Standalone ice bath | 350 THB | Anchor price |
| After-class add-on | 250 THB | Easy upsell to existing class buyers |
| Class + ice bath bundle | 600 THB | Best hero offer; current class is 400 THB |
| 10-pack ice bath | 2,500 THB | 250 THB/session; valid 60–90 days |
| Member recovery 8 uses/month | 1,500 THB | 187.5 THB/use if fully used |
| Member recovery 12 uses/month | 1,990 THB | 166 THB/use if fully used |
| High-cap recovery membership | 2,990+ THB | Only if capped or time-windowed |

### 3. Staycation upsell

Existing staycation is priced at 1,000 THB/day or 25,000 THB/month ([[wiki/sources/2026-05-02-nandpmuaythai-com]]). Recovery is especially valuable for foreigners training multiple times per week.

Recommended staycation variants:

| Product | Price |
|---|---:|
| Staycation + recovery day | 1,300 THB/day |
| Monthly recovery staycation | 29,000 THB/month |
| Add-on to existing staycation | +300 THB/day or +4,000 THB/month |

If the 25,000 THB/month package is already margin-sensitive, use a capped inclusion instead:

- Include 3 ice baths/week in a "Recovery Staycation" package.
- Charge extra at 250–300 THB/session beyond the cap.

## Best first offer

Hero launch offer:

```text
Train + Ice Bath Recovery
Muay Thai class + ice bath: 600 THB
```

Why this is the best starting offer:

- It builds on an existing product customers already understand: the 400 THB regular class ([[wiki/entities/n-and-p-boxing-gym]]).
- It creates a visible 150 THB discount versus 400 + 350 = 750 THB.
- It raises order value by 200 THB without changing the core class price.
- It does not require a separate cold-plunge-only customer-acquisition funnel.

## Decision rule

Proceed if the owner believes the gym can reach:

- **Minimum viable:** 2 paid uses/day → likely 12-month payback.
- **Good:** 5–6 paid uses/day → likely 3–4 month payback.
- **Strong:** 10 paid uses/day → likely under 2 month payback.

## Implementation checklist

- [ ] Confirm actual equipment quote, warranty, installation, filtration, and maintenance requirements.
- [ ] Confirm drainage, water access, electrical load, and safe location inside the gym.
- [ ] Write basic safety SOP: max duration, contraindications, supervision, cleaning, booking intervals.
- [ ] Launch with 199 THB first-try campaign for 2 weeks.
- [ ] Make 600 THB class + ice bath the main public offer.
- [ ] Add 250 THB after-class upsell to Line OA / front desk script.
- [ ] Create 8-use and 12-use member add-ons; avoid unlimited free use.
- [ ] Track daily: users, member/non-member mix, revenue, maintenance issues, repeat rate, post-class conversion.
- [ ] Review after 30 days: average realized price, uses/day, peak times, customer feedback, and capex payback trajectory.

## Open questions

> [!question] To confirm before buying
> - What exact equipment is included in the 100,000 THB investment?
> - Does the price include chiller, filtration, tub, installation, delivery, and warranty?
> - What is the real monthly electricity + cleaning + water cost?
> - Where will the tub be placed, and is drainage easy?
> - How many people can use it per hour without crowding or hygiene issues?
> - Will staff need extra training or supervision time?

## Cross-links

- Entity: [[wiki/entities/n-and-p-boxing-gym]]
- Pricing strategy: [[wiki/syntheses/n-and-p-pricing-strategy]]
- Source pages: [[wiki/sources/n-and-p-boxing-gym]], [[wiki/sources/2026-05-02-nandpmuaythai-com]]
