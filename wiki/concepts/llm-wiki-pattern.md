---
title: LLM Wiki Pattern
type: concept
created: 2026-05-02
updated: 2026-05-02
tags: [pattern, knowledge-management, second-brain]
sources: ["[[wiki/sources/2026-05-02-llm-wiki-pattern]]"]
---

# LLM Wiki Pattern

## Definition
A knowledge-management pattern in which an LLM agent incrementally builds and maintains a structured, interlinked collection of markdown files (a wiki) sitting between a human curator and a corpus of raw source documents. Knowledge is **compiled at ingest time** into the wiki, not re-derived at query time ([[wiki/sources/2026-05-02-llm-wiki-pattern]]).

## Why it matters
- Avoids the central weakness of RAG: lossy, repetitive re-synthesis on every query ([[wiki/concepts/rag-vs-wiki]]).
- The wiki is a **compounding artifact** — every source and every filed query makes future answers better.
- It solves the historical maintenance problem of personal knowledge bases — the bookkeeping load is now near-zero ([[wiki/concepts/memex]]).

## Mechanics
- Three layers: raw sources, wiki, schema ([[wiki/concepts/three-layer-architecture]]).
- Three operations: **ingest**, **query**, **lint**.
- The human owns curation and direction; the LLM owns writing and maintenance.

## Variants / related concepts
- [[wiki/concepts/rag-vs-wiki]] — the contrast that motivates the pattern.
- [[wiki/concepts/memex]] — historical predecessor.
- [[wiki/concepts/three-layer-architecture]] — the structural commitment that makes the pattern work.

## Open questions
- At what corpus size does the index-file approach stop scaling and require a real search engine (e.g. `qmd`)?
- What's the right cadence for `lint` — per-ingest, weekly, on-demand?
- How should multi-source contradictions be surfaced beyond a callout — a dedicated `wiki/contradictions/` folder?

## Sources
- [[wiki/sources/2026-05-02-llm-wiki-pattern]]
