---
domain: LLM
category: rules
sub-category: markdown
date-created: 2026-05-20
date-revised: 2026-05-20
type: rule
version: 1.0.0
status: DRAFT
llm-provider:
llm-model:
llm-session:
llm-session-data:
aliases:
tags:
---

# runtime-format-carveouts

## Scope

The generated scaffold starts with operational templates and migrated
reference material. The strict documentation audit should not apply the
Obsidian-style documentation schema to harness or imported-reference surfaces.

## Carve-Outs

| Subtree | Reason |
|---|---|
| `.claude/` | Project-local harness configuration. |
| `.github/` | GitHub workflow syntax, not documentation. |
| `agents/` | Agent templates follow agent specs. |
| `commands/` | Command templates follow command specs. |
| `docs/` | Imported starter reference and passoff area. |
| `hooks/` | Hook scripts follow hook specs. |
| `rules/` | This scaffold rule file configures the audit itself. |
| `scripts/` | Executable implementation code. |
| `skills/` | Skill templates follow skill specs. |
| `specs/` | Imported starter reference specs. |
