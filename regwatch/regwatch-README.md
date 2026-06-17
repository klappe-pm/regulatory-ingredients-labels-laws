# regwatch

Operational data for the regulatory watch-list register and change-detection
engine (Deliverable 3). The engine is `scripts/regwatch.py`. The design is
`docs/plans/deliverable-3-regulatory-monitoring-design.md`.

## Files

| File | Purpose |
|---|---|
| `regwatch-obligations.csv` | The register. One row per legal obligation per jurisdiction. |
| `regwatch-sources.json` | Authoritative source feeds, one per jurisdiction surface. |
| `regwatch-ingredient-functions.json` | Maps ingredient function to definition and examples. |
| `regwatch-jurisdictions.json` | Every jurisdiction the register accounts for: US federal, all 50 states plus DC, an aggregate marker, Canada, Mexico. |
| `regwatch-schema.json` | Field definitions, required-ness, enums, and patterns the engine validates against. |
| `state/regwatch-seen.json` | Last-seen content hash per source. Written by `scan --update`. |
| `state/snapshots/` | Analyst-captured raw source fixtures (gitignored). |

## Commands

```bash
python3 scripts/regwatch.py validate                       # check register + catalogs against the schema
python3 scripts/regwatch.py coverage                       # per-jurisdiction coverage (confirmed/tracked)
python3 scripts/regwatch.py list --upcoming 365            # obligations effective within a year
python3 scripts/regwatch.py list --jurisdiction US-CA      # filter by jurisdiction, --function, --status
python3 scripts/regwatch.py capture --source us-fda-federal-register  # fetch live into a snapshot
python3 scripts/regwatch.py scan                           # NEW / CHANGED / UNCHANGED / MISSING per source
python3 scripts/regwatch.py scan --live --update           # fetch live, accept the result as baseline
python3 scripts/regwatch.py digest --out digest.md         # analyst-facing register digest
python3 scripts/regwatch.py report --out r.md --json r.json  # change-and-due alert (Phase D output)
```

`make regwatch-validate` runs validation in CI and in `make test`. The
`.github/workflows/regwatch.yml` workflow runs `scan` and `report` on a weekly
cadence and uploads the report as an artifact.

## How Change Detection Works

`scan` reduces each source to a change-relevant signal before hashing, so the
hash does not churn on markup or unrelated page furniture: the Federal Register
API is reduced to a sorted list of document identifiers, and HTML is stripped to
collapsed text. The hash is compared to `state/regwatch-seen.json`; `--update`
accepts the current state as the new baseline.

## Working Rules

- Detection flags; humans edit. `scan` never changes the register.
- Seed rows are `secondary-digest` confidence: they come from a conference
  digest, not primary legal text. Confirm against source text before any label
  use. Nothing here is legal advice.
- Aggregate `us-multistate-*` rows are promoted into per-state rows as
  individual bills are confirmed.
