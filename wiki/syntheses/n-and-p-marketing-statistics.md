---
title: "N&P marketing statistics — saved reports and refresh guide"
type: synthesis
created: 2026-10-09
updated: 2026-10-09
tags: [n-and-p, marketing-stats, reporting]
sources: ["[[wiki/sources/2026-10-09-n-and-p-meta-ads-report]]", "[[wiki/sources/2026-10-09-n-and-p-google-ads-report]]", "[[wiki/sources/2026-10-09-n-and-p-search-console-report]]"]
---

# N&P marketing statistics

Start here when answering questions about saved marketing performance. The current snapshot was collected October 9, 2026 for the requested period September 9–October 8. Each source contains the exact request and machine-readable JSON rows, including account/property, dates and metric names. These are historical reports, not a live dashboard.

## Saved reports

| Source | Reported results | Evidence and daily data |
|---|---|---|
| Facebook/Instagram advertising | 6,085.07 THB spend; 158,090 impressions; 4,528 all clicks; 945 link clicks; 251 messaging conversations | [[wiki/sources/2026-10-09-n-and-p-meta-ads-report]] |
| Google Ads | 8.17 THB spend; 10 impressions; 1 click; 0 reported conversions | [[wiki/sources/2026-10-09-n-and-p-google-ads-report]] |
| Search Console | 24 clicks; 973 impressions; calculated CTR 2.47%; returned dates September 12–October 6 | [[wiki/sources/2026-10-09-n-and-p-search-console-report]] |

## Meta campaign summary

| Campaign ID | Campaign | Spend THB | Conversations | THB per conversation |
|---|---|---:|---:|---:|
| 52640169255608 | Local Trial 400 | 1,037.19 | 39 | 26.59 |
| 52642026682008 | Kids School Break | 5,047.88 | 212 | 23.81 |
| Total | Both campaigns | 6,085.07 | 251 | 24.24 |

Calculated from daily rows in [[wiki/sources/2026-10-09-n-and-p-meta-ads-report]]. Conversation counts include conversations restarted after seven days of inactivity; they are not confirmed customers. Offline revenue and paying-student counts remain unavailable in these reports, so they do not establish customer acquisition cost, profit or ROAS.

## Status differences to preserve

> ⚠️ Contradiction / dated status update: Both earlier setup notes describe unpublished drafts. The newer reports show delivered ads despite DRAFT in campaign names. Keep those setup histories and use report dates when stating delivery status. Google’s delivered campaign ID differs from the earlier draft ID; the lineage and publication date have not been verified. ([[wiki/sources/2026-10-09-n-and-p-meta-ads-report]], [[wiki/sources/2026-10-09-n-and-p-google-ads-report]])

- [[wiki/syntheses/n-and-p-facebook-reel-seven-day-test]] — historical setup.
- [[wiki/syntheses/n-and-p-google-search-draft]] — historical setup.

## Instructions for future agents

1. Read this hub, then the linked source for the relevant platform. Parse its fenced JSON request and returned arrays when calculations are needed. Cite that source and state its collection date, requested period and actual returned coverage.
2. Keep missing days and null values unknown. Sum spend, clicks and impressions only within the same scope. Recalculate ratios from summed numerators and denominators; do not average daily ratios. Never sum average position, reach or rates.
3. Keep organic search, paid ads, platform conversions and verified payments separate. The two Search Console properties overlap: query the selected domain property without adding URL-prefix results. Query breakdowns must not be added to daily totals.
4. For a refresh, read the Windsor skill and discover current accounts, fields and options before fetching. Reuse the saved request as a starting point, choose explicit dates and record changed options. Recheck source cache/fetch time when freshness matters.
5. Save a new dated source page per platform with its exact request, complete returned rows, definitions, coverage gaps and collection date. Preserve previous snapshots. Link the new source here and from index.md; append log.md and commit/push under AGENTS.md. Do not overwrite raw/ or store credentials.
6. Follow the vault's discussion-before-ingest rule. Do not treat this guide as authorization to change campaigns, budgets or attribution settings. No recurring refresh is configured by this operation.

## Next useful data

Recommended additions: GA4 website enquiries and an owner-confirmed payment summary for matching leads to paying students. Those datasets are not included in this snapshot. Start with [[wiki/entities/n-and-p-boxing-gym]] for business context.
