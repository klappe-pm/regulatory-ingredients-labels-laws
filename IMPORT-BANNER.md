---
domain: engineering
category: platform
sub-category: scaffolds
date-created: 2026-05-18
date-revised: 2026-05-18
aliases:
tags:
  - runtime
  - scaffolds
  - source-import
  - stage-2b
---

# import-banner

This directory is the **verbatim import** of `projects-repo/scaffolding/` per `docs/discovery/migration-manifest.md` (Stage 2A) and the Stage 2B copy step.

Per the manifest, this is **Option A**: preserve the source layout under `scaffolds/source-import/` until the four Section 4 sub-scaffolds (`minimal/`, `business-project/`, `pm-note/`, `hook/`) are designed in a follow-up stage. The contents here are reference material, not the canonical scaffolds.

## Origin

- **Source:** `projects-repo/scaffolding/` at `projects-repo` HEAD on 2026-05-17.
- **Destination:** `runtime/scaffolds/source-import/`.
- **Exclusions applied during copy:** `.DS_Store`, `.claude/`, `docs/archive/`, `docs/passoffs/`.

## What lives here vs what is canonical

| Path | Status |
| --- | --- |
| `scaffolds/source-import/` | reference import — do not extend |
| `scaffolds/minimal/` | canonical (Section 4); author in a follow-up stage |
| `scaffolds/business-project/` | canonical (Section 4); author in a follow-up stage |
| `scaffolds/pm-note/` | canonical (Section 4); author in a follow-up stage |
| `scaffolds/hook/` | canonical (Section 4); author in a follow-up stage |

When the four canonical sub-scaffolds are written, decide per file whether the source-import entry promotes, merges, or is dropped. Until then, no code or doc should *link* to paths under `source-import/` from canonical runtime files.
