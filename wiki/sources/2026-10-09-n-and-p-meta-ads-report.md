---
title: "N&P Meta Ads — snapshot collected 2026-10-09"
type: source
created: 2026-10-09
updated: 2026-10-09
tags: [n-and-p, marketing-stats, snapshot]
source_url: https://adsmanager.facebook.com/
source_type: note
collected_on: 2026-10-09
report_start: 2026-09-09
report_end: 2026-10-08
connector: facebook
---

# N&P Meta Ads report

## TL;DR

- Reported spend: 6,085.07 THB; 158,090 impressions; 4,528 all clicks and 945 link clicks. ([[wiki/sources/2026-10-09-n-and-p-meta-ads-report]])
- Reported messaging conversations: 251; calculated spend per conversation: 24.24 THB. These are not verified paying students. ([[wiki/sources/2026-10-09-n-and-p-meta-ads-report]])
- Two campaigns delivered ads although their names retain DRAFT; snapshot covers returned rows within September 9–October 8. ([[wiki/sources/2026-10-09-n-and-p-meta-ads-report]])

## Key claims

Account 144777171 matches the earlier N&P campaign record. The other connected Meta account was not queried. Reporting timezone: Asia/Bangkok. Currency: THB. Attribution option `default` means 7-day click and 1-day view per Windsor's option definition; unified ad-set attribution was not enabled.

Messaging conversation started means a conversation started after at least seven days of inactivity. It can include returning contacts. All clicks and link clicks are different metrics. Cost per conversation = total spend / reported conversations; do not label this customer acquisition cost or ROAS.

Source evidence: the Windsor.ai read request and returned rows preserved below ([[wiki/sources/2026-10-09-n-and-p-meta-ads-report]]#Request and returned data). This is a live connector snapshot, not a raw-file ingest; no raw file was created or changed. Collection date is recorded separately from the reporting dates. Source fetch/cache timestamps were not requested, so collection date does not prove a fresh upstream fetch. Missing rows are not zeros; returned zeros are preserved.

> ⚠️ Contradiction / dated status update: [[wiki/syntheses/n-and-p-facebook-reel-seven-day-test]] records an unpublished draft at setup time. This later report has delivery metrics despite DRAFT in the name. Preserve the historical record; do not use it as current delivery status. The actual publication time and person who published are unknown. ([[wiki/sources/2026-10-09-n-and-p-meta-ads-report]])

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
  "connector": "facebook",
  "accounts": [
    "144777171"
  ],
  "fields": [
    "date",
    "account_id",
    "account_currency",
    "account_timezone",
    "campaign",
    "campaign_id",
    "spend",
    "impressions",
    "clicks",
    "actions_link_click",
    "actions_onsite_conversion_messaging_conversation_started_7d"
  ],
  "options": {
    "attribution_window": "default"
  },
  "date_from": "2026-09-09",
  "date_to": "2026-10-08"
}
```

```json
[
{"date":"2026-09-13","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Local Trial 400 | Reel | 7D 1400 | DRAFT","campaign_id":"52640169255608","spend":72.43,"impressions":1279,"clicks":74,"actions_link_click":16,"actions_onsite_conversion_messaging_conversation_started_7d":4},
{"date":"2026-09-14","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Local Trial 400 | Reel | 7D 1400 | DRAFT","campaign_id":"52640169255608","spend":246.48,"impressions":2903,"clicks":140,"actions_link_click":23,"actions_onsite_conversion_messaging_conversation_started_7d":11},
{"date":"2026-09-15","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Local Trial 400 | Reel | 7D 1400 | DRAFT","campaign_id":"52640169255608","spend":188.03,"impressions":2651,"clicks":122,"actions_link_click":23,"actions_onsite_conversion_messaging_conversation_started_7d":6},
{"date":"2026-09-16","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Local Trial 400 | Reel | 7D 1400 | DRAFT","campaign_id":"52640169255608","spend":233.67,"impressions":4801,"clicks":240,"actions_link_click":28,"actions_onsite_conversion_messaging_conversation_started_7d":8},
{"date":"2026-09-17","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Local Trial 400 | Reel | 7D 1400 | DRAFT","campaign_id":"52640169255608","spend":199.25,"impressions":5532,"clicks":246,"actions_link_click":40,"actions_onsite_conversion_messaging_conversation_started_7d":6},
{"date":"2026-09-18","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Local Trial 400 | Reel | 7D 1400 | DRAFT","campaign_id":"52640169255608","spend":97.33,"impressions":1859,"clicks":86,"actions_link_click":12,"actions_onsite_conversion_messaging_conversation_started_7d":3},
{"date":"2026-09-19","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Local Trial 400 | Reel | 7D 1400 | DRAFT","campaign_id":"52640169255608","spend":0,"impressions":0,"clicks":0,"actions_link_click":0,"actions_onsite_conversion_messaging_conversation_started_7d":0},
{"date":"2026-09-20","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Local Trial 400 | Reel | 7D 1400 | DRAFT","campaign_id":"52640169255608","spend":0,"impressions":0,"clicks":0,"actions_link_click":0,"actions_onsite_conversion_messaging_conversation_started_7d":1},
{"date":"2026-09-21","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":154.2,"impressions":2646,"clicks":148,"actions_link_click":29,"actions_onsite_conversion_messaging_conversation_started_7d":11},
{"date":"2026-09-22","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Local Trial 400 | Reel | 7D 1400 | DRAFT","campaign_id":"52640169255608","spend":0,"impressions":0,"clicks":0,"actions_link_click":0,"actions_onsite_conversion_messaging_conversation_started_7d":0},
{"date":"2026-09-22","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":431.29,"impressions":9044,"clicks":441,"actions_link_click":76,"actions_onsite_conversion_messaging_conversation_started_7d":35},
{"date":"2026-09-23","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":316.18,"impressions":9361,"clicks":346,"actions_link_click":62,"actions_onsite_conversion_messaging_conversation_started_7d":27},
{"date":"2026-09-24","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":341.67,"impressions":8954,"clicks":268,"actions_link_click":52,"actions_onsite_conversion_messaging_conversation_started_7d":14},
{"date":"2026-09-25","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":345.2,"impressions":9212,"clicks":233,"actions_link_click":37,"actions_onsite_conversion_messaging_conversation_started_7d":13},
{"date":"2026-09-26","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":494.49,"impressions":14767,"clicks":346,"actions_link_click":86,"actions_onsite_conversion_messaging_conversation_started_7d":19},
{"date":"2026-09-27","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":190.18,"impressions":5615,"clicks":125,"actions_link_click":31,"actions_onsite_conversion_messaging_conversation_started_7d":10},
{"date":"2026-09-28","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":0,"impressions":0,"clicks":0,"actions_link_click":0,"actions_onsite_conversion_messaging_conversation_started_7d":0},
{"date":"2026-09-29","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":0,"impressions":0,"clicks":0,"actions_link_click":0,"actions_onsite_conversion_messaging_conversation_started_7d":0},
{"date":"2026-09-30","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":254.38,"impressions":7292,"clicks":161,"actions_link_click":28,"actions_onsite_conversion_messaging_conversation_started_7d":9},
{"date":"2026-10-01","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":699.82,"impressions":24506,"clicks":498,"actions_link_click":109,"actions_onsite_conversion_messaging_conversation_started_7d":18},
{"date":"2026-10-02","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":636.85,"impressions":17898,"clicks":403,"actions_link_click":94,"actions_onsite_conversion_messaging_conversation_started_7d":21},
{"date":"2026-10-03","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":691.64,"impressions":19331,"clicks":392,"actions_link_click":109,"actions_onsite_conversion_messaging_conversation_started_7d":21},
{"date":"2026-10-04","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":377.48,"impressions":8383,"clicks":203,"actions_link_click":74,"actions_onsite_conversion_messaging_conversation_started_7d":11},
{"date":"2026-10-05","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":114.5,"impressions":2056,"clicks":56,"actions_link_click":16,"actions_onsite_conversion_messaging_conversation_started_7d":3},
{"date":"2026-10-06","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":0,"impressions":0,"clicks":0,"actions_link_click":0,"actions_onsite_conversion_messaging_conversation_started_7d":0},
{"date":"2026-10-07","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":0,"impressions":0,"clicks":0,"actions_link_click":0,"actions_onsite_conversion_messaging_conversation_started_7d":0},
{"date":"2026-10-08","account_id":"144777171","account_currency":"THB","account_timezone":"Asia/Bangkok","campaign":"N&P | Kids School Break | Messenger | 7D 2800 | DRAFT","campaign_id":"52642026682008","spend":0,"impressions":0,"clicks":0,"actions_link_click":0,"actions_onsite_conversion_messaging_conversation_started_7d":0}
]
```

