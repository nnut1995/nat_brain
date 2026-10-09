---
title: "N&P Google Ads — snapshot collected 2026-10-09"
type: source
created: 2026-10-09
updated: 2026-10-09
tags: [n-and-p, marketing-stats, snapshot]
source_url: https://ads.google.com/
source_type: note
collected_on: 2026-10-09
report_start: 2026-09-09
report_end: 2026-10-08
connector: google_ads
---

# N&P Google Ads report

## TL;DR

- Reported spend: 8.17 THB, 10 impressions, one click, zero reported conversions. ([[wiki/sources/2026-10-09-n-and-p-google-ads-report]])
- Returned delivery dates: October 6 and October 8; no missing date was filled with zero. ([[wiki/sources/2026-10-09-n-and-p-google-ads-report]])
- The delivered campaign is 24275650234, named DRAFT | N&P | Search | Rama 2 | TH | 3000 THB; its ID differs from the September setup record. ([[wiki/sources/2026-10-09-n-and-p-google-ads-report]])

## Key claims

Account: 288-657-8621. Reporting timezone: Asia/Bangkok. Currency: THB. `spend` is returned in account currency, not micros. `conversions` includes conversion actions included in Google's conversions metric; zero reported conversions does not establish zero offline sales. Attribution and conversion tracking were not audited. No revenue or ROAS is inferred.

Source evidence: the Windsor.ai read request and returned rows preserved below ([[wiki/sources/2026-10-09-n-and-p-google-ads-report]]#Request and returned data). This is a live connector snapshot, not a raw-file ingest; no raw file was created or changed. Collection date is recorded separately from the reporting dates. Source fetch/cache timestamps were not requested, so collection date does not prove a fresh upstream fetch. Missing rows are not zeros; returned zeros are preserved.

> ⚠️ Contradiction / dated status update: [[wiki/syntheses/n-and-p-google-search-draft]] records an unpublished draft at setup time. This later report has delivery metrics despite DRAFT in the name. Preserve the historical record; do not use it as current delivery status. The actual publication time and person who published are unknown. ([[wiki/sources/2026-10-09-n-and-p-google-ads-report]])

## Notable quotes

None; metric values and field identifiers are preserved rather than quoted prose.

## Entities mentioned

- [[wiki/entities/n-and-p-boxing-gym]]

## Concepts introduced

- [[wiki/syntheses/n-and-p-marketing-statistics]] — reuse, definitions and refresh instructions.

## My questions / contradictions

- How many enquiries became paying students? Payment attribution is not part of this report.
- Recheck coverage and attribution before comparing with another snapshot.

## Request and returned data

The first JSON block is the reproducible request; the second is the complete returned daily row array. Fields and identifiers retain connector names. These are historical snapshots; save future pulls separately.

```json
{
  "connector": "google_ads",
  "accounts": [
    "288-657-8621"
  ],
  "fields": [
    "date",
    "account_id",
    "account_currency_code",
    "account_time_zone",
    "campaign",
    "campaign_id",
    "spend",
    "impressions",
    "clicks",
    "conversions"
  ],
  "date_from": "2026-09-09",
  "date_to": "2026-10-08"
}
```

```json
[
{"date":"2026-10-06","account_id":"288-657-8621","account_currency_code":"THB","account_time_zone":"Asia/Bangkok","campaign":"DRAFT | N&P | Search | Rama 2 | TH | 3000 THB","campaign_id":"24275650234","spend":0,"impressions":4,"clicks":0,"conversions":0},
{"date":"2026-10-08","account_id":"288-657-8621","account_currency_code":"THB","account_time_zone":"Asia/Bangkok","campaign":"DRAFT | N&P | Search | Rama 2 | TH | 3000 THB","campaign_id":"24275650234","spend":8.17,"impressions":6,"clicks":1,"conversions":0}
]
```

