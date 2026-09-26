---
title: "N&P Discord pilot — setup and validation record"
type: source
created: 2026-09-26
updated: 2026-09-27
tags: [muay-thai, chatbot, discord, pilot]
source_type: note
---

# N&P Discord pilot — setup and validation record

Source: this session's user requirements, local implementation and observed test results on 2026-09-26. This is an operational record; no raw files were created or modified.

## TL;DR
- Nat requested an internal Discord pilot: paste customer enquiries, review replies, then manually send them to customers.
- A fresh standalone bot project uses Codex and the approved customer FAQ; six synthetic live Codex checks passed.
- Discord pilot is active with a thread per enquiry and separate recent conversation history; customer replies and internal notes remain separate.

## Key claims
- Nat selected [#gym-chatbot](https://discord.com/channels/1499980328671117442/1553424764058472479), asked to ignore existing resources and build anew, and chose Codex for initial testing. Existing Hermes pilot settings were removed and its configuration verified equal to the pre-change configuration. ([[wiki/sources/2026-09-26-discord-pilot-setup]])
- New project location: `/Users/natn/Desktop/nandp-discord-pilot`. Customer facts come from [[wiki/syntheses/n-and-p-customer-chatbot-knowledge-base]], read before each request. No CRM integration or old bot credentials are included. ([[wiki/sources/2026-09-26-discord-pilot-setup]])
- Primary interaction is now plain customer text in `#gym-chatbot`, which creates a new thread. Follow-ups inside that thread use only its own recent exchanges; `/draft` also creates or continues a thread. Nat explicitly approved enabling Message Content Intent. Access remains restricted to authorized users in the selected channel and child threads. ([[wiki/sources/2026-09-26-discord-pilot-setup]])
- Four offline checks passed. Six synthetic Codex cases passed and outputs were inspected: Thai trial/equipment, both 30-session sharing types, residential 15th/16th/Sunday rules, residential refund referral, unconfirmed booking, and misleading customer instructions. Successful evaluation times were 6.9–12.4 seconds. This is limited test evidence, not a universal accuracy guarantee. Details are in the project's `VALIDATION.md`. ([[wiki/sources/2026-09-26-discord-pilot-setup]])
- Nat created and installed **N&P Customer Pilot** (application ID `1553428526592565338`) and saved its new token locally. `/draft` was registered and the bot started as its own macOS login service, `com.natn.nandp-discord-pilot`. The pilot is **live** in the selected channel while this Mac is awake and connected; Codex account availability/limits apply. ([[wiki/sources/2026-09-26-discord-pilot-setup]])

- Sales-style revision: Nat requested a welcoming receptionist voice for new Facebook leads and removal of bureaucratic approval wording from customer replies. Updated the standalone prompt; eight synthetic Codex scenarios passed, including beginner conversion, caring extension/refund handover and unchanged pricing/booking rules. Staff decisions remain internal. A live Discord beginner enquiry verified the welcoming trial offer and next-step question in 7.5 seconds. ([[wiki/sources/2026-09-26-n-and-p-owner-chatbot-policies]], [[wiki/sources/2026-09-26-discord-pilot-setup]])

- Monthly buffet revision: updated the pilot to recommend the 3,990 THB one-month group buffet for regular-training leads, with one session per opening day. Four targeted Codex tests passed, covering regular leads, general prices, daily limits/closures and occasional visitors; the pilot service was restarted with the new prompt. ([[wiki/sources/2026-09-26-n-and-p-owner-chatbot-policies]], [[wiki/sources/2026-09-26-discord-pilot-setup]])

- Thread revision: eight offline checks passed, including separate durable histories, duplicate prevention, bounded recent context and ordered follow-ups. A live Codex follow-up retained the customer name/date/time while changing two people to three, without confirming availability (8.6 seconds). The updated service connected successfully. ([[wiki/sources/2026-09-26-discord-pilot-setup]])
- Conversation memory: local `runtime/conversations` files retain the latest 40 successful exchanges per thread across restarts; approximately 22,000 characters of recent whole exchanges are supplied to each fresh Codex run. Internal notes are excluded. No automatic age-based deletion or offline-message replay is configured. ([[wiki/sources/2026-09-26-discord-pilot-setup]])

## Notable quotes
- "just ignore the existing resource, just do everything new"
- "try to use codex first for test"

## Entities mentioned
- [[wiki/entities/n-and-p-boxing-gym]]

## Concepts introduced
- Internal draft review before customer-facing deployment; operational companion to [[wiki/syntheses/n-and-p-customer-chatbot-knowledge-base]].

## My questions / contradictions
- No gym policy changes. Discord is an internal pilot before the planned Facebook/LINE customer deployment, not a replacement public customer channel. ([[wiki/sources/2026-09-26-discord-pilot-setup]], [[wiki/sources/2026-09-26-n-and-p-owner-chatbot-policies]])
- End-to-end verification completed: Nat’s Discord account submitted a synthetic Thai trial-class enquiry using `/draft`; the new bot returned 400 THB, 60 minutes, sportswear, free gloves/wraps and payment after class, with a separate internal note, in 9 seconds. No customer was contacted. This was the initial slash-command check; plain-message thread mode supersedes the original stateless workflow. ([[wiki/sources/2026-09-26-discord-pilot-setup]])

- Final normal-message Discord UI check was blocked by the locked Mac; Nat was asked to unlock it. Message Content Intent was independently verified enabled through Discord’s API, and the updated service connected with no logged errors. Unit and direct Codex follow-up tests passed; an actual top-level message → thread → follow-up round trip has not yet been observed. ([[wiki/sources/2026-09-26-discord-pilot-setup]])

## Admin handover update — 2026-09-27
- Added persistent per-thread pauses for explicit staff requests, one internal handover notice, and guards against queued/in-flight replies, attachments and slash-command bypass. Ordinary staff-review flags do not trigger takeover. Eleven offline tests passed; the service restarted. ([[wiki/sources/2026-09-26-discord-pilot-setup]])
- Direct testing found the owner-selected `gpt-6-luna` is rejected by the current ChatGPT-authenticated CLI. Normal generation and semantic handover classification therefore remain blocked with that setting; explicit Thai/English handover matching works without the model. Nat was asked whether to restore the previous default. No end-to-end Discord takeover test has been performed. ([[wiki/sources/2026-09-26-discord-pilot-setup]])
