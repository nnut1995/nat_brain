---
title: RAG vs. LLM Wiki
type: concept
created: 2026-05-02
updated: 2026-05-02
tags: [rag, pattern, comparison]
sources: ["[[wiki/sources/2026-05-02-llm-wiki-pattern]]"]
---

# RAG vs. LLM Wiki

## Definition
A contrast between two strategies for using LLMs over a corpus: **RAG** (Retrieval-Augmented Generation) retrieves chunks from raw sources at query time and synthesizes an answer; the **LLM Wiki Pattern** synthesizes at ingest time and queries a pre-compiled, interlinked wiki ([[wiki/sources/2026-05-02-llm-wiki-pattern]]).

## Why it matters
The choice determines whether knowledge **accumulates** or is **re-derived** on every question. RAG starts from zero each query; the wiki compounds.

## Comparison

| Dimension | RAG | LLM Wiki |
|---|---|---|
| When work is done | Query time | Ingest time |
| Persistence | None — answers vanish | Wiki pages persist, link, evolve |
| Cross-references | Per-query, ad hoc | Maintained continuously |
| Contradiction tracking | None | Flagged on ingest |
| Failure mode | Lossy synthesis under tight context | Stale or inconsistent pages |
| Best for | Ad hoc Q&A over fresh corpora | Long-term deep dives, personal KBs |

## Variants / related concepts
- [[wiki/concepts/llm-wiki-pattern]] — the pattern this contrasts with.
- Tools like NotebookLM and ChatGPT file uploads are canonical RAG-style systems ([[wiki/sources/2026-05-02-llm-wiki-pattern]]).

## Open questions
- Hybrid systems: a wiki *plus* a fallback RAG over `raw/` for queries that miss the index — worth building?

## Sources
- [[wiki/sources/2026-05-02-llm-wiki-pattern]]
