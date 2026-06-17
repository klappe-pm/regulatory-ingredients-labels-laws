---
domain: regulatory-ingredients-labels-laws
category: reference
sub-category: troubleshooting
date-created: 2026-06-17
date-revised: 2026-06-17
type: reference
status: DRAFT
aliases:
  - regwatch troubleshooting
  - regwatch runbook
tags:
  - agent-guide
  - regwatch
  - runbook
  - troubleshooting
---

# regwatch-troubleshooting

A runbook for a future agent (Codex, Claude Code, or otherwise) working on
`regwatch`, the regulatory monitoring engine. It explains how to run and verify
the system and how to diagnose the failures that actually happen here. Start by
reading `regwatch/regwatch-README.md` and `docs/plans/delivery-plan.md`.

## Quick Start

```bash
make test                 # doctor + audit-strict + regwatch-validate + regwatch-smoke
make regwatch-validate    # validate the register and all sidecars
python3 scripts/regwatch.py --help
```

The engine is `scripts/regwatch.py` plus sibling modules (`regwatch_impact.py`,
`regwatch_synthesis.py`, `regwatch_render.py`, `regwatch_briefing.py`,
`regwatch_ingest.py`). Data lives in `regwatch/`. It is standard library only;
do not add dependencies.

## Architecture Map

- Register and catalogs: `regwatch/regwatch-obligations.csv`,
  `regwatch-sources.json`, `regwatch-ingredient-functions.json`,
  `regwatch-jurisdictions.json`, `regwatch-talking-rain.json`.
- Briefing sidecars: `regwatch-obligation-detail.json`, `regwatch-changelog.json`,
  `regwatch-warning-letters.json`.
- Schema and validation: `regwatch-schema.json`; `validate()` and
  `validate_extras()` in `scripts/regwatch.py`.
- State (generated, not all tracked): `regwatch/state/regwatch-seen.json`
  (last-seen hashes), `state/snapshots/` (analyst captures, gitignored),
  `state/regwatch-ingest-candidates.json` (live candidates, gitignored).
- Loops: `.github/workflows/regwatch-daily.yml` and `regwatch.yml`; audit CI in
  `.github/workflows/audit.yml`.

## How Verification Works

`make test` chains `doctor` (files exist), `audit-strict` (markdown audit of
`docs/plans` and the reference docs), `regwatch-validate` (data model), and
`regwatch-smoke` (runs every command so a command-path error fails the build).
CI runs `audit-strict`, `regwatch-validate`, and `regwatch-smoke`.

## Common Issues and Fixes

### Live Fetch Returns 403 or 404

The build sandbox blocks outbound network, so `scan --live`, `ingest --live`,
and `capture` return 403 or time out here. This is expected. Verify the live
path on the GitHub Actions runner instead (see Verifying the Live Path). For
real 404s on the runner, the source URL has moved or the site blocks
non-browser agents; `http_get` already sends a browser user agent, so update the
URL in `regwatch-sources.json` and re-verify.

### Certificate Verification Failed

Some government sites (for example the Mexican DOF) serve an incomplete
certificate chain. `http_get` retries once without verification for these
read-only public documents and prints a warning. If a source is chronically
unreachable, set its `mechanism` to `manual` in `regwatch-sources.json`; `scan`
then reports it `MANUAL` instead of erroring, and an analyst checks it by hand.

### Scan Shows Everything Missing

`scan` with no snapshots and no network reports every source `MISSING`. That is
correct offline. Capture a snapshot (`python3 scripts/regwatch.py capture
--source <id>`) or run with `--live` where the network allows it.

### Validation Errors

`regwatch-validate` prints one `ERROR` line per problem. Causes: a field value
outside its enum, a value failing its `pattern`, a missing required field, a
reference to an unknown source/function/jurisdiction/channel, or a sidecar key
that is not a real `obligation_id`. Fix the data file named in the message.

### The Briefing Has No Candidates

The "Newly Detected — Unconfirmed" section appears only when
`state/regwatch-ingest-candidates.json` holds candidates. Offline, `ingest`
writes zero candidates, so the section is absent. Run `ingest --live` (on the
runner) or `ingest --from-file <saved-api-response.json>` to populate it.

### A Word Document Will Not Open

The `.docx` is built directly as a zip of WordprocessingML. Verify it with
`python3 -c "import zipfile,xml.dom.minidom as m; z=zipfile.ZipFile('f.docx');
m.parseString(z.read('word/document.xml'))"`. If that parses, the file is valid.

### CI Fails on Audit-Strict

The markdown audit requires each audited file's H1 to equal its filename stem
(lowercase, spaces to hyphens) and headings to be Title Case. Function words
(`and`, `the`, `in`, `of`, `to`, `or`, and the rest) must be lowercase when not
the first word; a bare date in a heading is rejected, so wrap it in parentheses.
Fix per the audit message and re-run `make audit-strict`.

## Verifying the Live Path

The sandbox cannot reach the live feeds, so confirm them on the runner:

1. Trigger the weekly loop: run the `regwatch.yml` workflow via
   `workflow_dispatch` on `main`.
2. Read the job logs for the run and find the ingest line, for example
   `regwatch ingest: N candidate events from live (since ...)`.
3. The uploaded `regwatch-weekly` artifact contains the rendered outputs and the
   candidates file.

## Extending the System

- New obligation: add a row to `regwatch-obligations.csv`, then a matching entry
  in `regwatch-obligation-detail.json`; run `make regwatch-validate`.
- New source: add an entry to `regwatch-sources.json` (its `jurisdiction` must
  exist in the jurisdiction catalog).
- New ingredient function or jurisdiction: add it to its catalog before
  referencing it.
- Promote a live candidate: copy a confirmed entry from
  `state/regwatch-ingest-candidates.json` into `regwatch-changelog.json` by hand.

## Guardrails

- Standard library only; no new dependencies.
- Human-in-the-loop: detection and ingestion flag; they never edit the register
  or the curated change log. Promotion is manual.
- Do not commit `state/snapshots/` or `state/regwatch-ingest-candidates.json`.
- Nothing the engine emits is legal advice; confirm against primary source text.
