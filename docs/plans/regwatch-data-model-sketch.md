---
domain: regulatory-ingredients-labels-laws
category: plan
sub-category: data-model
date-created: 2026-06-22
date-revised: 2026-06-22
type: design
version: 0.1.0
status: DRAFT
aliases:
  - regwatch exportable database sketch
tags:
  - data-model
  - export
  - metadata
  - regwatch
  - taxonomy
---

# regwatch-data-model-sketch

A forward sketch (a v5-or-later direction, captured now) for turning the
briefing records into a standardized, exportable database that can be mined for
insights. The first working slice already exists: the `export` command emits one
normalized row per obligation.

## What This Sketches

Today each obligation carries a standardized record in
`regwatch/regwatch-obligation-detail.json`: a summary, the impacts, the
implications for the beverage industry, a topic list, the governing CFR, an
action, and a source link. The `export` command flattens those into CSV and
JSON. This sketch describes how that grows into a queryable dataset.

## The Record Model

One row per obligation, with stable columns: `obligation_id`, `country`,
`jurisdiction`, `status`, `effective_date`, `topics`, `summary`, `impacts`,
`implications`, `action`, `source_url`, and `cfr`. List fields use a semicolon so
a single cell stays atomic. The `obligation_id` is the stable key that ties a
record to the register, the detail, and any future history.

## Topic Taxonomy

Topics are a controlled vocabulary declared in the detail file and enforced by
`make regwatch-validate`, so every record is tagged from the same list (for
example color-additives, sweeteners, front-of-package, prop-65, state-patchwork).
A controlled vocabulary is what makes the dataset groupable and comparable over
time.

## Export Formats

The CSV opens in any spreadsheet or loads into a database; the JSON feeds a
script or a notebook. A natural next step is loading the CSV into SQLite so the
records can be queried with SQL without adding a runtime dependency.

## Example Insights to Mine

- Count of active obligations by topic, to see where exposure concentrates.
- Obligations by effective date, to build a forward deadline calendar.
- Jurisdiction spread per topic, to show how far a theme has traveled across the
  state patchwork.
- Status mix (proposed versus enacted) per topic, to gauge momentum.

## Roadmap to v5 and Beyond

- Add change-event records (the dated developments) as a second table keyed by
  `obligation_id`, so history is queryable.
- Add per-product impact rows, so the database answers which products are exposed
  to which obligation at what severity.
- Version records over time so the dataset shows how a rule moved from proposed
  to enacted.
- Govern the topic vocabulary with an owner and a change log.

## Open Questions

- Where should the canonical export live, and who refreshes it on what cadence?
- Do we want a single SQLite file checked in, or generated on demand from the
  source files?
- Which insights does the team actually want first, so the schema serves them?
