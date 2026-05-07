---
title: "LLM Wiki — A pattern for building personal knowledge bases using LLMs"
type: source
created: 2026-05-02
updated: 2026-05-02
tags: [pattern, knowledge-management, llm, memex]
source_url: (seed note from Nat)
source_type: article
raw: "[[raw/2026-05-02-llm-wiki-pattern]]"
---

# Source: LLM Wiki Pattern

> Raw file: `raw/2026-05-02-llm-wiki-pattern.md` — the originating idea note for this vault.

## TL;DR
- RAG retrieves at query time and re-derives knowledge every time; the LLM Wiki Pattern compiles knowledge once at ingest time into a persistent, interlinked artifact.
- The wiki has three layers: immutable **raw sources**, LLM-owned **wiki**, and a co-evolved **schema** (this `CLAUDE.md`).
- The LLM does the bookkeeping (cross-references, summaries, contradiction-tracking) that humans abandon — that is why the pattern works.

## Key claims
- The LLM should never modify `raw/` and should fully own `wiki/`. ([[wiki/concepts/three-layer-architecture]])
- A single ingest typically touches 10–15 wiki pages — that is the feature, not a bug.
- Cross-references and contradiction-flags are precomputed at ingest, not at query.
- Good query answers should be filed back as synthesis pages so exploration compounds. ([[wiki/concepts/llm-wiki-pattern]])
- Conceptually descended from Vannevar Bush's Memex (1945); the missing piece Bush couldn't solve — *who maintains it* — is filled by the LLM. ([[wiki/concepts/memex]], [[wiki/entities/vannevar-bush]])

## Notable quotes
- "Obsidian is the IDE; the LLM is the programmer."
- "The wiki is a persistent, compounding artifact."

## Entities mentioned
- [[wiki/entities/vannevar-bush]]
- [[wiki/entities/obsidian]]

## Concepts introduced
- [[wiki/concepts/llm-wiki-pattern]]
- [[wiki/concepts/rag-vs-wiki]]
- [[wiki/concepts/memex]]
- [[wiki/concepts/three-layer-architecture]]

## My questions / contradictions
- *(none yet — this is the seed source. Add follow-ups as new sources arrive.)*
