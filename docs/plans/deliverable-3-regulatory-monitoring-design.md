---
domain: regulatory-ingredients-labels-laws
category: plan
sub-category: design
date-created: 2026-06-17
date-revised: 2026-06-17
type: design
version: 0.1.0
status: DRAFT
aliases:
  - deliverable 3 design
  - regulatory monitoring design
tags:
  - automation
  - change-detection
  - data-model
  - monitoring
  - register
  - regwatch
---

# deliverable-3-regulatory-monitoring-design

## Spec Citation

This design implements Deliverable 3 of `docs/plans/delivery-plan.md` under the
canonical scaffold spec at
`/Users/kevinlappe/Projects/harness/scaffolding/project-routing-spec.md`
(Records and Source-Corpus Overlay). Operational tooling data lives in a new
top-level `regwatch/` corpus; the engine lives in `scripts/`; derived analyst
output lives under `docs/`.

## Decisions That Shaped This

The five open questions in the delivery plan were answered on 2026-06-17:

- Build the reference register first, then layer monitoring on top of it.
- Cover all 50 US states, Canada, and Mexico in the data model.
- Audience is internal research; do not build a polished front end. Get the
  mechanics, the automations, and the data model right.

So this phase delivers a validated data model, a seed register, a source
catalog, and a working change-detection engine. It deliberately does not ship a
UI, and it does not auto-edit the register.

## What This Delivers

- A structured obligation register, one row per legal obligation per
  jurisdiction, at `regwatch/regwatch-obligations.csv`.
- A source catalog of authoritative feeds at `regwatch/regwatch-sources.json`.
- An ingredient-function map at `regwatch/regwatch-ingredient-functions.json`,
  so a ban on a function resolves to every affected product.
- A validation schema at `regwatch/regwatch-schema.json`.
- A standard-library engine at `scripts/regwatch.py` with `validate`, `list`,
  `scan`, and `digest` commands.

## The Data Model

The register is a flat CSV so it diffs cleanly in git and opens in any
spreadsheet. Each row is one obligation. List-valued fields use a semicolon
delimiter. The schema file is the authority for fields, required-ness, and
enumerations; the engine validates against it.

Key fields: `obligation_id` (stable slug), `country` (US, CA, MX),
`jurisdiction_level`, `jurisdiction`, `instrument`, `citation`, `title`,
`ingredient_functions`, `ingredients`, `claims_affected`, `product_scope`,
`status`, `effective_date`, `source_id`, `source_url`, `last_reviewed`,
`confidence`, and `notes`.

Two modeling choices carry weight. Obligations are tagged by ingredient
function, not only by name, because statutes name ingredients individually but a
business needs to find every product exposed to a function in one query. And the
50-state patchwork starts as aggregate `monitoring` rows
(`us-multistate-*`) that are promoted into per-state rows as individual bills are
confirmed, so the register is honest about what is verified versus what is
merely tracked.

## Source Catalog

Each source records `method` (poll versus subscribe), `mechanism` (api, rss,
html, email-list, manual), and a cadence. The seed catalog covers the Federal
Register API and FDA newsroom, USDA SNAP, California leginfo and OEHHA
Proposition 65, a multistate tracker for the 50-state surface, Health Canada and
the Canada Gazette, and Mexico DOF and COFEPRIS. Per-state US feeds are reached
through the multistate tracker until a confirmed bill warrants its own row.

## Change-Detection Mechanics

The `scan` command obtains content for each source, computes a SHA-256 hash, and
compares it to the last-seen hash in `regwatch/state/regwatch-seen.json`. Each
source is classified NEW, CHANGED, UNCHANGED, or MISSING. Content is read from an
analyst-captured snapshot under `regwatch/state/snapshots/` by default, so the
engine runs and diffs deterministically offline; `--live` fetches the source URL
when no snapshot exists. The last-seen state is only written when the analyst
passes `--update`, which is the explicit act of accepting the new baseline.

## Human in the Loop

Detection flags; it never edits the register. A CHANGED source is a prompt for
an analyst to read the source, decide whether an obligation changed, and edit
the register by hand. This matches the AI-in-food-safety session: automation
drafts and flags, a human confirms before anything is treated as a compliance
fact. Every seed row is marked `secondary-digest` confidence because it derives
from a conference digest, not primary legal text, and must be confirmed against
source text before any label use.

## Running It

```bash
python3 scripts/regwatch.py validate
python3 scripts/regwatch.py list --upcoming 365
python3 scripts/regwatch.py list --function color
python3 scripts/regwatch.py scan --update
python3 scripts/regwatch.py digest --out docs/reports/regwatch-digest.md
```

## Phasing and Next Steps

- Phase A, done here: data model, seed register, source catalog, engine.
- Phase B: capture snapshots or wire `--live` per source, and confirm the
  secondary-digest rows against primary source text.
- Phase C: promote aggregate multistate rows into per-state obligations as bills
  are confirmed, and schedule `scan` on a cadence.
- Phase D: route the digest to a delivery channel once cadence is decided.

## Verification

- `make regwatch-validate` passes (also runs in CI and in `make test`).
- `make audit-strict` and `make doctor` pass.
- `scan` correctly reports NEW, then UNCHANGED, then CHANGED across snapshot
  edits.

## Open Items

- Live fetch for html sources will need per-source parsing to reduce noise from
  unrelated page changes; hashing the whole page is a deliberately blunt first
  cut.
- Per-state coverage for all 50 states is modeled but not yet populated row by
  row.
