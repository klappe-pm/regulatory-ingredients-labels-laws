---
domain: regulatory-ingredients-labels-laws
category: decision
sub-category: source-intake
date-created: 2026-06-11
date-revised: 2026-06-11
type: decision
status: DONE
aliases:
  - conference materials source intake
tags:
  - conference
  - intake
  - provenance
  - sources
---

# 2026-06-11-source-intake-conference-materials

## Decision

Route the nine 38th Annual Food Label Conference decks into the
Records and Source-Corpus overlay at
`sources/diane-tran-genesis-conference-materials/`, kebab-renamed as the
canonical filename per source. Derived summaries and the presentation remain
under `docs/reports/`.

## Context

The decks arrived untracked inside `docs/diane-tran-genesis-conf-materials/`,
mixing raw source evidence into `docs/`. The canonical scaffold spec routes raw
source material to `sources/`, kebab-renamed, with an intake decision logged
before analysis.

## Rename Map

Original filename to canonical kebab name. Two filenames carried typos
(`Strategis`, `UPdate`); both were normalized in the canonical name.

| Original | Canonical |
|---|---|
| `BP Aligning RD Marketing Legal on Food Claims.pdf` | `bp-aligning-rd-marketing-legal-on-food-claims.pdf` |
| `California Compliance and Labeling Strategis.pdf` | `california-compliance-and-labeling-strategies.pdf` |
| `GenSess AI In food Safety.pdf` | `gensess-ai-in-food-safety.pdf` |
| `GenSess FDA and Food Policy UPdate.pdf` | `gensess-fda-and-food-policy-update.pdf` |
| `GenSess Law Talk.pdf` | `gensess-law-talk.pdf` |
| `GenSess MAHA and the Admin.pdf` | `gensess-maha-and-the-admin.pdf` |
| `GenSess State Initiatives.pdf` | `gensess-state-initiatives.pdf` |
| `PB QA and Regulatory.pdf` | `pb-qa-and-regulatory.pdf` |
| `Regulatory Landscape.pdf` | `regulatory-landscape.pdf` |

## Related

- One misfiled artifact (`compass_artifact_...md`, an unrelated Tin Can
  children's-phone privacy report) was relocated to `_local/inbox/` rather than
  kept in the source corpus.
- The Genesis Foods platform guide was kept under `docs/` with its typo'd folder
  renamed `docs/genesys/` to `docs/genesis/`; it is reference material, not a
  conference source.
