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
| `regwatch-schema.json` | Field definitions, required-ness, and enumerations the engine validates against. |
| `state/regwatch-seen.json` | Last-seen content hash per source. Written by `scan --update`. |
| `state/snapshots/` | Analyst-captured source fixtures (gitignored). |

## Commands

```bash
python3 scripts/regwatch.py validate            # check the register against the schema
python3 scripts/regwatch.py list --upcoming 365 # obligations effective within a year
python3 scripts/regwatch.py scan                # report NEW / CHANGED / UNCHANGED / MISSING sources
python3 scripts/regwatch.py scan --update       # accept the current source state as baseline
python3 scripts/regwatch.py digest              # render an analyst-facing markdown digest
```

`make regwatch-validate` runs validation in CI and in `make test`.

## Working Rules

- Detection flags; humans edit. `scan` never changes the register.
- Seed rows are `secondary-digest` confidence: they come from a conference
  digest, not primary legal text. Confirm against source text before any label
  use. Nothing here is legal advice.
- Aggregate `us-multistate-*` rows are promoted into per-state rows as
  individual bills are confirmed.
