---
title: "N&P Discord pilot — setup and validation record"
type: source
created: 2026-09-26
updated: 2026-09-26
tags: [muay-thai, chatbot, discord, pilot]
source_type: note
---

# N&P Discord pilot — setup and validation record

Source: this session's user requirements, local implementation and observed test results on 2026-09-26. This is an operational record; no raw files were created or modified.

## TL;DR
- Nat requested an internal Discord pilot: paste customer enquiries, review replies, then manually send them to customers.
- A fresh standalone bot project uses Codex and the approved customer FAQ; six synthetic live Codex checks passed.
- Discord activation remains pending new app creation, installation and credentials; no Discord round trip has been verified.

## Key claims
- Nat selected [#gym-chatbot](https://discord.com/channels/1499980328671117442/1553424764058472479), asked to ignore existing resources and build anew, and chose Codex for initial testing. Existing Hermes pilot settings were removed and its configuration verified equal to the pre-change configuration. ([[wiki/sources/2026-09-26-discord-pilot-setup]])
- New project location: `/Users/natn/Desktop/nandp-discord-pilot`. Customer facts come from [[wiki/syntheses/n-and-p-customer-chatbot-knowledge-base]], read before each request. No CRM integration or old bot credentials are included. ([[wiki/sources/2026-09-26-discord-pilot-setup]])
- Primary interaction is `/draft` with customer question and optional explicit context. Plain-paste mode is implemented but off until the new app's Message Content Intent and local setting are enabled. Each question starts a fresh ephemeral Codex run; the reply and internal admin note are separate. Access defaults to the server owner in the selected channel or its child threads. ([[wiki/sources/2026-09-26-discord-pilot-setup]])
- Four offline checks passed. Six synthetic Codex cases passed and outputs were inspected: Thai trial/equipment, both 30-session sharing types, residential 15th/16th/Sunday rules, residential refund referral, unconfirmed booking, and misleading customer instructions. Successful evaluation times were 6.9–12.4 seconds. This is limited test evidence, not a universal accuracy guarantee. Details are in the project's `VALIDATION.md`. ([[wiki/sources/2026-09-26-discord-pilot-setup]])
- The browser creation form is prepared with **N&P Customer Pilot**. Discord requires accepting developer terms; approval was requested and is pending. New app installation, token configuration, command registration, persistent start and a real Discord test remain outstanding. The pilot is **not live**. ([[wiki/sources/2026-09-26-discord-pilot-setup]])

## Notable quotes
- "just ignore the existing resource, just do everything new"
- "try to use codex first for test"

## Entities mentioned
- [[wiki/entities/n-and-p-boxing-gym]]

## Concepts introduced
- Internal draft review before customer-facing deployment; operational companion to [[wiki/syntheses/n-and-p-customer-chatbot-knowledge-base]].

## My questions / contradictions
- No gym policy changes. Discord is an internal pilot before the planned Facebook/LINE customer deployment, not a replacement public customer channel. ([[wiki/sources/2026-09-26-discord-pilot-setup]], [[wiki/sources/2026-09-26-n-and-p-owner-chatbot-policies]])
- Finish Discord setup and verify a real round trip before marking the pilot active. ([[wiki/sources/2026-09-26-discord-pilot-setup]])
