# nat_brain — LLM Wiki Schema

This is Nat's personal second brain. It is an Obsidian vault maintained by an LLM agent (Codex). This file is the contract between Nat and the LLM. Read it at the start of every session before touching anything else.

The pattern: Nat curates raw sources and asks questions. The LLM reads sources, writes/maintains the wiki, keeps cross-references consistent, and never forgets the bookkeeping. Nat reads the wiki in Obsidian; the LLM writes it.

---

## Directory layout

```
nat_brain/
├── AGENTS.md            # this file — schema and rules
├── index.md             # content-oriented catalog of all wiki pages
├── log.md               # chronological append-only history
├── raw/                 # IMMUTABLE source documents (LLM never modifies)
│   ├── assets/          # images, PDFs, audio (Obsidian attachments dir)
│   └── *.md             # clipped articles, notes, transcripts
└── wiki/                # LLM-owned generated knowledge
    ├── sources/         # one summary page per raw source
    ├── entities/        # people, companies, products, places
    ├── concepts/        # ideas, frameworks, themes
    └── syntheses/       # cross-source analyses, comparisons, query answers
```

### Layer rules
- **`raw/`** — source of truth. Read-only for the LLM. Never edit, rename, or delete files here without explicit permission.
- **`wiki/`** — fully owned by the LLM. Create, update, refactor, link freely.
- **`AGENTS.md` / `index.md` / `log.md`** — co-owned. The LLM updates them as part of every operation. Co-evolve `AGENTS.md` with Nat over time.

---

## Page conventions

Every wiki page (anything under `wiki/`) starts with YAML frontmatter so Dataview can query it:

```yaml
---
title: <page title>
type: source | entity | concept | synthesis
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
sources: ["[[sources/foo]]", "[[sources/bar]]"]   # for entity/concept/synthesis pages
source_url: https://...                            # for source pages only
source_type: article | paper | podcast | book | note | transcript
---
```

### File naming
- Lowercase, kebab-case, no spaces: `wiki/entities/sam-altman.md`, `wiki/concepts/prompt-caching.md`.
- Source pages mirror the raw filename: `raw/2026-04-01-llm-wiki-pattern.md` → `wiki/sources/2026-04-01-llm-wiki-pattern.md`.
- One concept/entity per file. If a page grows past ~500 lines, split it.

### Linking
- Always use Obsidian wikilinks: `[[entities/sam-altman]]`, not markdown links. This makes the graph view useful.
- Every wiki page must have at least one inbound link from `index.md` and ideally from a sibling page. Orphans are flagged during lint.
- When citing a claim, link to the source page: `Sam founded OpenAI in 2015 ([[sources/2026-04-01-altman-bio]]).`

### Page templates
- **Source page** — `## TL;DR` (3 bullets) → `## Key claims` → `## Notable quotes` (≤15 words each, in quotes) → `## Entities mentioned` → `## Concepts introduced` → `## My questions / contradictions`.
- **Entity page** — `## Summary` → `## Key facts` (bulleted, each cited) → `## Relationships` → `## Timeline` → `## Sources`.
- **Concept page** — `## Definition` → `## Why it matters` → `## Variants / related concepts` → `## Open questions` → `## Sources`.
- **Synthesis page** — free-form. Title in the form `<topic> — <angle>`, e.g. `wiki/syntheses/agentic-rag-vs-classic-rag.md`.

---

## Operations

### 1. Ingest

When Nat says *"ingest X"* or drops a file in `raw/`:

1. **Read** the raw source end-to-end. If it has images, view the key ones.
2. **Discuss** the 3–5 key takeaways with Nat in chat. Ask which angle to emphasize. Wait for direction before writing.
3. **Write** `wiki/sources/<slug>.md` using the source page template.
4. **Update or create** entity and concept pages for everything material the source touches. A single ingest typically modifies 5–15 pages — that is normal and expected.
5. **Cross-reference** — every new claim links back to the source page. Every source page links forward to the entities/concepts it touches.
6. **Update `index.md`** — add the new source under Sources, plus any new entity/concept pages.
7. **Append to `log.md`** with the prefix format: `## [YYYY-MM-DD] ingest | <source title>` followed by a 2–3 line summary of what changed.
8. **Flag contradictions** explicitly. If the new source contradicts an existing claim, do NOT silently overwrite — add a `> ⚠️ Contradiction` callout on both pages and surface it to Nat.

### 2. Query

When Nat asks a question:

1. Read `index.md` first to find candidate pages.
2. Read the candidate pages (not the raw sources unless needed).
3. Synthesize an answer with wikilink citations.
4. **Offer to file the answer** as `wiki/syntheses/<slug>.md` if it required real synthesis (more than retrieving a single fact). Good answers should compound, not vanish into chat.
5. If filed, update `index.md` and `log.md` (`## [YYYY-MM-DD] query | <question>`).

### 3. Lint

When Nat says *"lint"* or *"health check"*:

- Find orphan pages (no inbound wikilinks).
- Find broken wikilinks.
- Find concepts/entities mentioned in prose but lacking their own page.
- Find pages whose `updated` is stale relative to newer sources that mention them.
- Find contradictions across pages.
- Suggest 3–5 follow-up questions or sources to investigate next.
- Append `## [YYYY-MM-DD] lint | <summary>` to `log.md`.

### 4. Refactor

When the wiki structure stops fitting — categories overflow, pages get too big, naming drifts — propose a refactor to Nat first, then execute. Update `AGENTS.md` to record the new convention so future sessions stay consistent.

---

## Git hygiene

This vault is a git repo with `origin` on GitHub. After **any** operation that modifies tracked files (`ingest`, `query` that files a synthesis, `lint`, `refactor`, schema edits), the LLM **commits and pushes without waiting to be asked**.

- One commit per operation. Stage only the files touched by that operation — never `git add -A` or `git add .`.
- Commit message: short imperative subject summarizing the operation; 1–3 line body if non-obvious. Example: `Add N&P pricing strategy synthesis`.
- Push to `origin main` immediately after committing.
- If the push fails (auth, conflict, network), surface the error to Nat. Do not retry destructively, do not `--force`, do not amend a pushed commit.
- Never stage anything under `raw/`. The LLM should not have modified `raw/` in the first place (see Hard rule 1); if `raw/` shows up in `git status` as modified, stop and ask.
- If the only change is to `log.md` or `index.md` without a corresponding wiki page change, that is usually a bug — pause and check before committing.

---

## Hard rules

1. **Never modify `raw/`.** Read-only.
2. **Never delete a wiki page** without telling Nat what it contained and where its content went.
3. **Never silently resolve contradictions.** Flag them, don't paper over them.
4. **Always cite.** Every factual claim in the wiki links to a source page. No floating facts.
5. **Update `index.md` and `log.md` on every ingest, query-that-files, and lint.** Non-negotiable bookkeeping.
6. **One source per source page.** Don't merge multiple sources into one summary page.
7. **Quotes ≤ 15 words, in quotation marks.** Respect copyright. Paraphrase otherwise.
8. **Frontmatter on every wiki page.** Required for Dataview and for the LLM's own scanning.
9. **Wikilinks, not markdown links, inside the wiki.** Markdown links only for external URLs.
10. **Discuss before mass changes.** Refactors, page deletions, schema edits — propose first.

---

## Working style with Nat

- Default to ingesting **one source at a time**, with discussion. Batch mode only on request.
- After every ingest, give Nat a short summary: which pages were created, which were updated, what contradictions surfaced.
- When uncertain how to categorize something (entity vs. concept, which folder), ask rather than guess — early choices shape the whole wiki.
- Keep prose tight. Wiki pages are reference material, not essays.
- Use callouts for emphasis: `> [!note]`, `> [!warning]`, `> [!question]`.
