---
title: Three-Layer Architecture
type: concept
created: 2026-05-02
updated: 2026-05-02
tags: [architecture, pattern]
sources: ["[[wiki/sources/2026-05-02-llm-wiki-pattern]]"]
---

# Three-Layer Architecture

## Definition
The structural commitment of the [[wiki/concepts/llm-wiki-pattern]]: a strict separation between three layers ([[wiki/sources/2026-05-02-llm-wiki-pattern]]).

1. **Raw sources** — `raw/`. Immutable. Source of truth. The LLM reads but never writes.
2. **Wiki** — `wiki/`. LLM-owned. Generated, interlinked markdown. Created, updated, refactored freely.
3. **Schema** — `CLAUDE.md` (this vault) or `AGENTS.md` for other agents. Conventions, page templates, workflows. Co-evolved between human and LLM.

## Why it matters
- The immutability of `raw/` means the human can always trace any wiki claim back to original evidence — there is no LLM-corrupted ground truth.
- The LLM's full ownership of `wiki/` means refactors are cheap and there is no shared-edit conflict between human and machine.
- The schema layer is what turns the LLM from a generic chatbot into a disciplined wiki maintainer — the source of all the rules.

## Variants / related concepts
- Maps onto a classic compiler analogy: `raw/` = source code, `wiki/` = compiled artifact, `CLAUDE.md` = the compiler.

## Open questions
- Should `syntheses/` (filed query answers) eventually split into its own fourth layer, given it has different provenance from ingested-from-source pages?

## Sources
- [[wiki/sources/2026-05-02-llm-wiki-pattern]]
