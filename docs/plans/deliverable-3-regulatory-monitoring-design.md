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
- A jurisdiction catalog at `regwatch/regwatch-jurisdictions.json` enumerating US
  federal, all 50 states plus DC, an aggregate marker, Canada, and Mexico.
- A validation schema at `regwatch/regwatch-schema.json` enforcing required-ness,
  enums, patterns, and cross-file references.
- A standard-library engine at `scripts/regwatch.py` with `validate`,
  `coverage`, `list`, `capture`, `scan`, `digest`, and `report` commands.
- A scheduled automation at `.github/workflows/regwatch.yml`.

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
50-state patchwork is enumerated in the jurisdiction catalog with a `coverage`
status per jurisdiction: `confirmed` jurisdictions have their own obligation
rows, `tracked` jurisdictions are watched only through an aggregate multistate
row, and the `aggregate` marker is that row itself. Confirmed states (California
plus Iowa, Nebraska, Tennessee, New Jersey, New York, West Virginia, and Texas)
were promoted out of the aggregate as evidence warranted; the rest stay tracked.
The register is therefore honest about what is verified versus merely watched,
and the `coverage` command reports the ratio.

## Source Catalog

Each source records `method` (poll versus subscribe), `mechanism` (api, rss,
html, email-list, manual), and a cadence. The seed catalog covers the Federal
Register API and FDA newsroom, USDA SNAP, California leginfo and OEHHA
Proposition 65, a multistate tracker for the 50-state surface, Health Canada and
the Canada Gazette, and Mexico DOF and COFEPRIS. Per-state US feeds are reached
through the multistate tracker until a confirmed bill warrants its own row.

## Change-Detection Mechanics

The `scan` command obtains content for each source, reduces it to a
change-relevant signal, computes a SHA-256 hash, and compares it to the
last-seen hash in `regwatch/state/regwatch-seen.json`. Each source is classified
NEW, CHANGED, UNCHANGED, or MISSING. Signal extraction is per-source so the hash
does not churn on markup or unrelated page furniture: the Federal Register API is
reduced to a sorted list of document identifiers, and HTML is stripped to
collapsed text. Content is read from an analyst-captured raw snapshot under
`regwatch/state/snapshots/` by default, so the engine runs and diffs
deterministically offline; `capture` and `--live` fetch the source URL over
HTTP. The last-seen state is only written when the analyst passes `--update`,
which is the explicit act of accepting the new baseline. The `report` command
combines flagged source changes with obligations coming due into one
analyst-facing alert in markdown and JSON; `.github/workflows/regwatch.yml` runs
that on a weekly cadence, persists the last-seen state through the Actions cache,
and uploads the report as an artifact.

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
python3 scripts/regwatch.py coverage
python3 scripts/regwatch.py list --upcoming 365
python3 scripts/regwatch.py list --function color
python3 scripts/regwatch.py capture --source us-fda-federal-register
python3 scripts/regwatch.py scan --live --update
python3 scripts/regwatch.py report --out regwatch-report.md --json regwatch-report.json
```

## Phasing and Next Steps

- Phase A, done: data model, seed register, source catalog, engine.
- Phase B, done: per-source signal extraction, `capture`, and `--live` fetch.
  Confirming the secondary-digest rows against primary source text is the
  remaining analyst task, not an engine task.
- Phase C, done: the jurisdiction catalog enumerates all 50 states plus Canada
  and Mexico, evidenced states are promoted to their own rows, and the weekly
  workflow runs `scan` on a cadence.
- Phase D, done: `report` surfaces changes and due dates, and the workflow
  routes the report as a build artifact. The remaining open choice is the final
  delivery channel and cadence beyond the artifact default.

## Feedback Loops, Impact, and Synthesis

A second build layer turns detection into delivered analysis on a cadence.

- **Update loops.** Two scheduled workflows close the loop. The daily workflow
  (`.github/workflows/regwatch-daily.yml`) scans for change and renders the
  daily brief; the weekly workflow (`.github/workflows/regwatch.yml`) runs the
  weekly scan plus the full synthesized brief. Both persist last-seen state
  through the Actions cache and upload outputs as artifacts.
- **Content abstraction and synthesis.** `scripts/regwatch_synthesis.py`
  abstracts raw register rows, scan deltas, and impact scores into one document
  model. The daily brief is short and change-driven; the weekly synthesis is a
  full executive summary, coming-due list, per-product impact, beverage lens,
  and recommended actions.
- **CPG impact suite.** `scripts/regwatch_impact.py` joins each obligation to
  the product portfolio on three gates — jurisdiction or channel reach,
  school/SNAP scope, and an attribute match on ingredient function, named
  ingredient, or claim — and scores severity (act-now, high, watch, info), with
  a direct named-ingredient match weighted above a function-only match.
- **Beverage component.** The same module applies a category lens over the
  impacts (sweeteners and added sugar, synthetic colors, caffeine, preservatives
  and GRAS, Proposition 65), naming affected products only where a product
  actually carries the theme's function.
- **Talking Rain connection.** `regwatch/regwatch-talking-rain.json` models the
  portfolio (products, ingredient functions, claims, sales channels) that every
  impact maps onto. Product attributes are an internal model flagged for
  confirmation against current specifications.
- **Outputs.** `scripts/regwatch_render.py` renders the synthesized model into
  the requested formats: a Word document (`.docx`, built directly as a
  WordprocessingML zip with no third-party dependency), an email newsletter
  (HTML plus a plain-text alternative), and a web posting (markdown with front
  matter). Committed samples live in `docs/reports/regwatch-samples/`.

## The Human-Readable Briefing

The `briefing` command renders the usable, narrative report the project owner
asked for, focused on FDA food safety impacting US beverages with Canada and
Mexico as the other markets. It is built from three input sidecars so the
content is deep, not just a list of titles:

- `regwatch-obligation-detail.json` carries the context (what the rule is), the
  implications for beverages, the action, the governing CFR with eCFR links, and
  backlinks per obligation.
- `regwatch-changelog.json` holds dated regulatory developments so the briefing
  shows what happened recently, not a single in-window item.
- `regwatch-warning-letters.json` captures the recurring FDA warning-letter
  enforcement themes for beverages with their governing CFR, and the source
  catalog adds the live FDA Warning Letters database.

Each finding is written as What Happened, What It Means, and What We Need To Do,
with CFR and source backlinks. The sidecars are validated by
`make regwatch-validate`.

## Live Ingestion From the Federal Register

`scripts/regwatch_ingest.py` and the `ingest` command pull recent FDA documents
from the Federal Register API, filter to the beverage-relevant ones by CFR part
and keyword, and write candidate change-log events to
`state/regwatch-ingest-candidates.json`. Each candidate carries the document
type, the source backlink, and the CFR references the API itself reports, so CFR
tagging is sourced rather than guessed. Candidates are flagged `unconfirmed` and
surfaced in the briefing under a dedicated section; a human confirms and promotes
them into the curated change log before any compliance use, preserving the
human-in-the-loop posture. The daily and weekly loops run `ingest --live` before
rendering; offline, ingestion degrades to no candidates.

## Verification

- `make regwatch-validate` passes (also runs in CI and in `make test`).
- `make audit-strict` and `make doctor` pass.
- `scan` correctly reports NEW, then UNCHANGED, then CHANGED across snapshot
  edits, and the Federal Register signal is order-independent.
- Schema `pattern` and `enum` rules are enforced on the register and on all
  three catalogs.

## Open Items

- HTML signal extraction is collapsed-text; tightening it to per-source
  selectors would further cut noise once live feeds are wired.
- Confirmed-state coverage is 8 of 51 US jurisdictions; the rest stay tracked
  under the aggregate until evidence promotes them to their own rows.
- The final delivery channel beyond the artifact default is still open.
