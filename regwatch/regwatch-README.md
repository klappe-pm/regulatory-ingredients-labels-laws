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
| `regwatch-talking-rain.json` | Talking Rain product portfolio model that impact analysis maps obligations onto. |
| `regwatch-obligation-detail.json` | Human-readable detail per obligation: context, implications, action, CFR, and backlinks. |
| `regwatch-changelog.json` | Dated regulatory developments feeding the briefing's "what happened" section. |
| `regwatch-warning-letters.json` | FDA warning-letter enforcement themes for beverages, with governing CFR. |
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
python3 scripts/regwatch.py report --out r.md --json r.json  # change-and-due alert
python3 scripts/regwatch.py portfolio                      # list the Talking Rain portfolio
python3 scripts/regwatch.py impact --severity act-now      # CPG impact analysis on the portfolio
python3 scripts/regwatch.py beverage                       # beverage-category lens over the impacts
python3 scripts/regwatch.py brief --cadence weekly --out-dir out   # synthesized brief in every format
python3 scripts/regwatch.py brief --cadence daily --out-dir out    # short daily change brief
python3 scripts/regwatch.py ingest --live --since 365              # pull recent FDA Federal Register docs
python3 scripts/regwatch.py briefing --out briefing.md             # human-readable FDA beverage briefing
```

## Live Ingestion

`ingest` pulls recent FDA documents from the Federal Register API, filters to
the ones relevant to beverages (by CFR part and keyword), and writes candidate
change-log events to `state/regwatch-ingest-candidates.json`, each flagged
`unconfirmed` with the document type, source backlink, and the CFR references the
API itself reports. Candidates are surfaced in the briefing under a "Newly
Detected — Unconfirmed" section; a human confirms and promotes them into
`regwatch-changelog.json` before any compliance use. Offline, `ingest` degrades
gracefully (no network, no candidates); `--from-file` parses a saved response.
The daily and weekly loops run `ingest --live` before rendering.

## The Briefing

`briefing` renders a clean, marked-up report focused on FDA food safety
impacting US beverages, with Canada and Mexico as the other markets. Every item
is written as What Happened / What It Means (with the governing CFR and the
context for what the rule is) / What We Need To Do, with backlinks to primary
sources. It draws on `regwatch-obligation-detail.json` for the prose and CFR,
`regwatch-changelog.json` for dated recent developments, and
`regwatch-warning-letters.json` for FDA enforcement themes. The committed sample
is `docs/reports/regwatch-samples/regwatch-fda-beverage-briefing.md`.

The briefing renders at three complexity tiers for a phased team rollout, set by
`--tier v1|v2|v3` (v1 is the simplest headlines, v3 the full detail), and the
recent section can be windowed with `--since-days N`. The committed rollout set
(three reports plus a per-version changelog) lives in
`docs/reports/regwatch-rollout/`.

```bash
python3 scripts/regwatch.py briefing --tier v1 --since-days 90 --out report.md
```

`make regwatch-validate` runs validation in CI and in `make test`;
`make regwatch-brief` regenerates the weekly sample outputs.

## Feedback And Update Loops

Two scheduled workflows close the loop. `.github/workflows/regwatch-daily.yml`
scans for change and renders the daily brief; `.github/workflows/regwatch.yml`
runs the weekly scan plus the full synthesized brief. Both persist last-seen
state through the Actions cache and upload their outputs as artifacts.

## Outputs

`brief` renders one synthesized document model into every requested format:
`.docx` (built directly as a WordprocessingML zip), an email newsletter
(`-newsletter.html` plus a `-newsletter.txt` alternative), a web posting
(`-webpost.md` with front matter), and plain markdown. Committed samples live in
`docs/reports/regwatch-samples/`.

## Impact And Synthesis

`impact` joins each obligation to the Talking Rain portfolio on three gates —
jurisdiction or channel reach, school/SNAP scope, and an attribute match on
ingredient function, named ingredient, or claim — and scores severity (act-now,
high, watch, info). `beverage` adds a category lens. `brief` synthesizes the
register, scan deltas, impacts, and the beverage lens into the daily and weekly
documents.

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
