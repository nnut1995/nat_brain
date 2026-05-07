---
title: Obsidian
type: entity
entity_type: product
created: 2026-05-02
updated: 2026-05-02
tags: [tool, markdown, knowledge-management]
sources: ["[[wiki/sources/2026-05-02-llm-wiki-pattern]]"]
---

# Obsidian

## Summary
Local-first markdown editor used in this wiki as the **front-end / IDE** for browsing what the LLM writes ([[wiki/sources/2026-05-02-llm-wiki-pattern]]). Nat reads in Obsidian; the LLM writes via Claude Code.

## Key facts
- A vault is just a directory of markdown files — fully portable, git-friendly ([[wiki/sources/2026-05-02-llm-wiki-pattern]]).
- Wikilinks (`[[page]]`) drive the graph view, which is the canonical way to see wiki shape.
- Useful plugins for this pattern:
  - **Web Clipper** — browser extension; fastest way to populate `raw/`.
  - **Dataview** — runs queries over YAML frontmatter; pairs with the frontmatter convention in [[CLAUDE]].
  - **Marp** — render markdown as slide decks.

## Relationships
- Used as the front-end for: [[wiki/concepts/llm-wiki-pattern]]

## Conventions in this vault
- Attachment folder: `raw/assets/`
- Wikilinks (not markdown links) for all intra-wiki references.

## Sources
- [[wiki/sources/2026-05-02-llm-wiki-pattern]]
