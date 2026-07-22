# public/regwatch/CLAUDE.md

Operating rules for any agent working in `public/regwatch/`, the regulatory monitoring data and engine area. Read these before editing.

## What This Is





`public/regwatch/` holds the data; `scripts/regwatch.py` and its sibling `regwatch_*.py` modules are the engine. Full orientation is in `public/regwatch/regwatch-README.md`; the runbook for diagnosing problems is `public/regwatch/regwatch-troubleshooting.md`.

## Rules

- Standard library only. Do not add dependencies; the project verification and
  the `scripts/CLAUDE.md` policy both assume stdlib.
- Human-in-the-loop. `scan` and `ingest` detect and flag; they never edit the
  register or the curated change log. Promotion of an ingest candidate into
  `regwatch-changelog.json` is a manual, deliberate edit.
- Validate before claiming done: `make regwatch-validate`, then `make test`.
  Every data change must keep validation at zero errors.
- Keep generated state out of commits: `state/snapshots/` and
  `state/regwatch-ingest-candidates.json` are gitignored. `state/regwatch-seen.json`
  is a tracked empty baseline; do not commit a populated one.
- Nothing here is legal advice. Seed rows are `secondary-digest` or
  `internal-model` confidence and must be confirmed against primary source text.

## Data Files

| File | Purpose |
|---|---|
| `regwatch-obligations.csv` | The register, one row per obligation. |
| `regwatch-sources.json` | Authoritative feeds (a `manual` mechanism skips auto-fetch). |
| `regwatch-ingredient-functions.json` | Ingredient-function definitions. |
| `regwatch-jurisdictions.json` | US federal, all 50 states plus DC, Canada, Mexico. |
| `regwatch-talking-rain.json` | Portfolio model for impact analysis. |
| `regwatch-obligation-detail.json` | Briefing prose, CFR, and backlinks per obligation. |
| `regwatch-changelog.json` | Dated developments for the briefing. |
| `regwatch-warning-letters.json` | FDA enforcement themes. |
| `regwatch-schema.json` | Validation rules for the register and catalogs. |

## When Adding Data

Add the obligation row and its detail entry together, reference only catalog
values that already exist, and run `make regwatch-validate`. To add a source,
ensure its `jurisdiction` is in the jurisdiction catalog. See the troubleshooting
runbook's "Extending the System" section.
