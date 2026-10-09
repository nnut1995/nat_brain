---
title: "N&P Google Search Console — snapshot collected 2026-10-09"
type: source
created: 2026-10-09
updated: 2026-10-09
tags: [n-and-p, marketing-stats, snapshot]
source_url: https://search.google.com/search-console
source_type: note
collected_on: 2026-10-09
report_start: 2026-09-09
report_end: 2026-10-08
connector: searchconsole
---

# N&P Google Search Console report

## TL;DR

- Returned daily rows total 24 clicks and 973 impressions; calculated CTR: 2.47%. ([[wiki/sources/2026-10-09-n-and-p-search-console-report]])
- Requested September 9–October 8; returned daily dates run September 12–October 6. Missing dates remain unknown. ([[wiki/sources/2026-10-09-n-and-p-search-console-report]])
- The domain property was queried once; the overlapping URL-prefix property was not added to totals. ([[wiki/sources/2026-10-09-n-and-p-search-console-report]])

## Key claims

Selected property: sc-domain:nandpmuaythai.com. The connector returns site as nandpmuaythai.com. `include_fresh_data` is false. Search type was not explicitly selected, so this snapshot retains the connector's default scope; verify it before cross-report comparison. Reporting timezone was not exposed in this response; do not assume Bangkok for organic search.

Search-query rows are a separate breakdown and do not reconcile to daily totals: use daily rows for the headline totals. Do not sum both datasets or infer missing queries. `position` is an average, not a fixed rank; never sum it or take an unweighted average across days. CTR is calculated as sum(clicks) / sum(impressions).

Source evidence: the Windsor.ai read request and returned rows preserved below ([[wiki/sources/2026-10-09-n-and-p-search-console-report]]#Request and returned data). This is a live connector snapshot, not a raw-file ingest; no raw file was created or changed. Collection date is recorded separately from the reporting dates. Source fetch/cache timestamps were not requested, so collection date does not prove a fresh upstream fetch. Missing rows are not zeros; returned zeros are preserved.

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
  "connector": "searchconsole",
  "accounts": [
    "sc-domain:nandpmuaythai.com"
  ],
  "fields": [
    "date",
    "site",
    "clicks",
    "impressions",
    "position"
  ],
  "options": {
    "include_fresh_data": false
  },
  "date_from": "2026-09-09",
  "date_to": "2026-10-08"
}
```

```json
[
{"date":"2026-09-12","site":"nandpmuaythai.com","clicks":0,"impressions":64,"position":6.2656},
{"date":"2026-09-13","site":"nandpmuaythai.com","clicks":2,"impressions":42,"position":4.6429},
{"date":"2026-09-14","site":"nandpmuaythai.com","clicks":1,"impressions":43,"position":3.4651},
{"date":"2026-09-15","site":"nandpmuaythai.com","clicks":0,"impressions":26,"position":4.3077},
{"date":"2026-09-16","site":"nandpmuaythai.com","clicks":1,"impressions":30,"position":6.6333},
{"date":"2026-09-17","site":"nandpmuaythai.com","clicks":0,"impressions":50,"position":3.36},
{"date":"2026-09-18","site":"nandpmuaythai.com","clicks":0,"impressions":44,"position":4.1364},
{"date":"2026-09-19","site":"nandpmuaythai.com","clicks":1,"impressions":37,"position":5.5135},
{"date":"2026-09-20","site":"nandpmuaythai.com","clicks":0,"impressions":54,"position":3.7222},
{"date":"2026-09-21","site":"nandpmuaythai.com","clicks":0,"impressions":67,"position":4.9701},
{"date":"2026-09-22","site":"nandpmuaythai.com","clicks":1,"impressions":55,"position":3.6},
{"date":"2026-09-23","site":"nandpmuaythai.com","clicks":2,"impressions":39,"position":2.6667},
{"date":"2026-09-24","site":"nandpmuaythai.com","clicks":3,"impressions":25,"position":2.8},
{"date":"2026-09-25","site":"nandpmuaythai.com","clicks":0,"impressions":28,"position":2.9286},
{"date":"2026-09-26","site":"nandpmuaythai.com","clicks":2,"impressions":38,"position":8.4474},
{"date":"2026-09-27","site":"nandpmuaythai.com","clicks":1,"impressions":19,"position":5.4737},
{"date":"2026-09-28","site":"nandpmuaythai.com","clicks":3,"impressions":25,"position":4.64},
{"date":"2026-09-29","site":"nandpmuaythai.com","clicks":2,"impressions":36,"position":3.8333},
{"date":"2026-09-30","site":"nandpmuaythai.com","clicks":0,"impressions":30,"position":3.7333},
{"date":"2026-10-01","site":"nandpmuaythai.com","clicks":1,"impressions":42,"position":4.0238},
{"date":"2026-10-02","site":"nandpmuaythai.com","clicks":1,"impressions":29,"position":3.5517},
{"date":"2026-10-03","site":"nandpmuaythai.com","clicks":3,"impressions":43,"position":4.2093},
{"date":"2026-10-04","site":"nandpmuaythai.com","clicks":0,"impressions":33,"position":7.8788},
{"date":"2026-10-05","site":"nandpmuaythai.com","clicks":0,"impressions":30,"position":11.4333},
{"date":"2026-10-06","site":"nandpmuaythai.com","clicks":0,"impressions":44,"position":3.4545}
]
```

## Search query breakdown

Separate request, same property and requested period. This returned breakdown is not a complete accounting of daily totals; the discrepancy's cause was not established.

```json
{
  "connector": "searchconsole",
  "accounts": [
    "sc-domain:nandpmuaythai.com"
  ],
  "date_from": "2026-09-09",
  "date_to": "2026-10-08",
  "fields": [
    "query",
    "clicks",
    "impressions",
    "position"
  ],
  "options": {
    "include_fresh_data": false
  }
}
```

```json
[
{"query":"ค่ายมวยใกล้ฉัน","clicks":1,"impressions":42,"position":12.0714},
{"query":"boxing","clicks":0,"impressions":8,"position":4},
{"query":"boxing gym","clicks":0,"impressions":1,"position":1},
{"query":"camp muay thai bangkok","clicks":0,"impressions":1,"position":79},
{"query":"fitness ใกล้ฉัน","clicks":0,"impressions":1,"position":1},
{"query":"gần đây","clicks":0,"impressions":1,"position":4},
{"query":"kick boxing for kids","clicks":0,"impressions":1,"position":1},
{"query":"kick boxing for kids near me","clicks":0,"impressions":1,"position":1},
{"query":"muay","clicks":0,"impressions":2,"position":5.5},
{"query":"muay thai","clicks":0,"impressions":4,"position":1.75},
{"query":"muay thai camp bangkok","clicks":0,"impressions":2,"position":29.5},
{"query":"muay thai camps thailand","clicks":0,"impressions":2,"position":67},
{"query":"muay thai gym near bangna","clicks":0,"impressions":1,"position":42},
{"query":"muay thai gyms bangkok","clicks":0,"impressions":1,"position":1},
{"query":"muay thai near me","clicks":0,"impressions":2,"position":4},
{"query":"muay thai slp","clicks":0,"impressions":1,"position":13},
{"query":"muaynip","clicks":0,"impressions":4,"position":33},
{"query":"muaythai","clicks":0,"impressions":2,"position":1},
{"query":"near me","clicks":0,"impressions":1,"position":1},
{"query":"paba boxing","clicks":0,"impressions":1,"position":6},
{"query":"sparring boxing","clicks":0,"impressions":1,"position":4},
{"query":"thai boxing camp thailand","clicks":0,"impressions":1,"position":56},
{"query":"thai gym","clicks":0,"impressions":1,"position":1},
{"query":"training camp","clicks":0,"impressions":1,"position":11},
{"query":"คอร์สต่อยมวย","clicks":0,"impressions":1,"position":3},
{"query":"ค่ายมวย","clicks":0,"impressions":1,"position":1},
{"query":"ค่ายมวย ใกล้ฉัน","clicks":0,"impressions":1,"position":17},
{"query":"ค่ายมวย ใกล้ฉัน ราคาถูก","clicks":0,"impressions":1,"position":1},
{"query":"ค่ายมวยจอนนี่มือปราบ","clicks":0,"impressions":1,"position":4},
{"query":"ค่ายมวยปานนิวัฒน์","clicks":0,"impressions":2,"position":1},
{"query":"ค่ายมวยพระราม2","clicks":0,"impressions":4,"position":3.25},
{"query":"ค่ายมวยศิษย์สองพี่น้อง","clicks":0,"impressions":1,"position":1},
{"query":"ชกมวย","clicks":0,"impressions":1,"position":2},
{"query":"ซอมมวย","clicks":0,"impressions":1,"position":3},
{"query":"ซ้อมมวยใกล้ฉัน","clicks":0,"impressions":2,"position":1},
{"query":"ต่อยมวย","clicks":0,"impressions":6,"position":2.1667},
{"query":"ต่อยมวย ใกล้ฉัน","clicks":0,"impressions":3,"position":4.6667},
{"query":"ต่อยมวยใกล้ฉัน","clicks":0,"impressions":3,"position":1},
{"query":"ที่ซ้อมมวย","clicks":0,"impressions":1,"position":1},
{"query":"ที่ต่อยมวย","clicks":0,"impressions":1,"position":1},
{"query":"ป.เปาอินทร์","clicks":0,"impressions":7,"position":3.8571},
{"query":"พญาครุฑ เสือจันถกมวยไทย","clicks":0,"impressions":1,"position":10},
{"query":"มวย","clicks":0,"impressions":32,"position":6.0625},
{"query":"มวยใกล้ฉัน","clicks":0,"impressions":1,"position":1},
{"query":"มวยไทย","clicks":0,"impressions":105,"position":6.4286},
{"query":"มวยไทย ใกล้ฉัน","clicks":0,"impressions":1,"position":7},
{"query":"มวยไทยใกล้ฉัน","clicks":0,"impressions":1,"position":21},
{"query":"ยามิน พีเคแสนชัยมวยไทยยิม","clicks":0,"impressions":1,"position":8},
{"query":"ยิมมวยสากลใกล้ฉัน","clicks":0,"impressions":1,"position":1},
{"query":"ยิมมวยใกล้ฉัน","clicks":0,"impressions":1,"position":1},
{"query":"ยิมมวยไทย ใกล้ฉัน","clicks":0,"impressions":1,"position":99},
{"query":"สนามมวย","clicks":0,"impressions":3,"position":1.6667},
{"query":"สนามมวยใกล้ฉัน","clicks":0,"impressions":5,"position":1},
{"query":"สอนมวย","clicks":0,"impressions":1,"position":1},
{"query":"สอนมวยใกล้ฉัน","clicks":0,"impressions":1,"position":1},
{"query":"สอนมวยไทยใกล้ฉัน","clicks":0,"impressions":1,"position":1},
{"query":"เปาอินทร์","clicks":0,"impressions":8,"position":5.625},
{"query":"เรียน มวยไทย ฟรี ใกล้ฉัน","clicks":0,"impressions":2,"position":1.5},
{"query":"เรียน มวยไทย ใกล้ฉัน","clicks":0,"impressions":4,"position":4},
{"query":"เรียนชกมวย","clicks":0,"impressions":1,"position":1},
{"query":"เรียนต่อยมวย","clicks":0,"impressions":4,"position":3.5},
{"query":"เรียนต่อยมวย ใกล้ฉัน","clicks":0,"impressions":1,"position":1},
{"query":"เรียนมวย","clicks":0,"impressions":1,"position":1},
{"query":"เรียนมวย ใกล้ฉัน","clicks":0,"impressions":2,"position":1},
{"query":"เรียนมวยใกล้ฉัน","clicks":0,"impressions":1,"position":8},
{"query":"เรียนมวยไทย เด็ก","clicks":0,"impressions":1,"position":2},
{"query":"เรียนมวยไทยใกล้ฉัน","clicks":0,"impressions":1,"position":1},
{"query":"โรงเรียนสอนยิมนาสติกเด็ก","clicks":0,"impressions":1,"position":24},
{"query":"ไทยคิวบิค","clicks":0,"impressions":1,"position":4},
{"query":"ムエタイキャンプ","clicks":0,"impressions":2,"position":9},
{"query":"泰國泰拳訓練營","clicks":0,"impressions":1,"position":9}
]
```

