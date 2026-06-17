---
domain: regulatory-ingredients-labels-laws
category: plan
sub-category: delivery
date-created: 2026-06-11
date-revised: 2026-06-11
type: plan
version: 0.1.0
status: DRAFT
aliases:
  - regulatory delivery plan
tags:
  - automation
  - conference
  - delivery
  - presentation
  - scaffolding
  - summary
---

# delivery-plan

Delivery plan for `regulatory-ingredients-labels-laws`. Sequences the three
deliverables the project owner set on 2026-06-11: (1) summarise the recent
conference documents, (2) design and build a presentation, (3) plan the balance
of the work — the regulatory-update automation — for later discussion.

## Spec Citation

Per `docs/plans/plans-README.md`, plans cite the spec they implement. The
canonical authority is the harness scaffold spec at
`/Users/kevinlappe/Projects/harness/scaffolding/project-routing-spec.md`
(sections: Base Scaffold, Records and Source-Corpus Overlay, Project Metadata,
`CLAUDE.md` Pointer Contract, Anti-Patterns). The `plans-README.md` pointer to
`specs/specs-project-scaffold-framework-spec.md` is stale — that `specs/` tree
was intentionally stripped (see `docs/passoffs/2026-05-30-2125-passoff-file.md`);
fixing that dangling citation is folded into Phase 0 below.

## What This Plan Covers

Three deliverables in order, plus a Phase 0 scaffold-reconciliation track that
runs first because the source material arrived untracked and the repo has
drifted from the current canonical scaffold:

1. Conference summary — **done** this session.
2. Presentation — **done** this session.
3. Automate regulatory updates — **scoped here for discussion**, not yet built.

## Current State (Reviewed 2026-06-11)

- Purpose (`project.yml`): "automate regulatory updates for product
  ingredients, labels, and labeling laws." Implementation not yet started.
- New source material landed untracked: nine conference decks under
  `docs/diane-tran-genesis-conf-materials/` and a Genesis Foods platform guide
  under `docs/genesys/`.
- One misfiled artifact: `compass_artifact_...md` in the conference folder is a
  Tin Can children's-phone privacy report — unrelated to this project.
- Scaffold drift vs. recent harness changes: root `agents/` stubs still tracked
  after the harness moved to single-canonical-`CLAUDE.md` and untracked
  project-local `.claude/`; `project.yml` uses the pre-2026-06-09 format (no
  `scaffold-overlays:` / `canonical-scaffold:` keys); root `CLAUDE.md` does not
  point at the canonical spec; `docs/docs-README.md` is deleted but uncommitted
  and still referenced by the `Makefile` audit allowlist.

## Deliverable 1 — Conference Summaries and Briefing (Done)

Audience re-scoped (2026-06-11) to a non-regulatory consumer packaged goods
beverage team (Talking Rain, non-alcoholic), educating rather than briefing a
compliance analyst. The earlier compliance-analyst summary and deck were
removed in favour of the audience-correct set below.

- Per-session summaries: `../reports/conference-source-summaries/` (nine files,
  one per session), each plain-language with jargon defined and a
  beverage-implications section.
- Synthesis briefing: `../reports/food-label-conference-2026-beverage-briefing.md`,
  connecting all nine sessions into one business document — the federal-vs-state
  collision, the five label changes, California first (AB 418, Prop 65), why
  beverages are targeted, the claims/marketing lesson, AI, and a seven-step
  action list. US federal plus California lens.
- Method: nine parallel extraction agents, one per PDF (177 pages total), each
  writing its summary and returning a digest; synthesised into the briefing.

## Deliverable 2 — Presentation (Done)

- Source: `../reports/food-label-conference-2026-beverage-deck.md` (Marp markdown).
- Built artifacts: `food-label-conference-2026-beverage-deck.pdf` and
  `food-label-conference-2026-beverage-deck.pptx`, rendered via
  `@marp-team/marp-cli`.
- Design: clean and minimal by request — Helvetica Neue, default theme, no
  custom colors, no italics, one idea per slide, plain markdown that copies into
  any theme. 18 slides for the non-regulatory beverage audience.
- Re-render (two separate calls; combining `--pdf --pptx` is rejected):
  `npx @marp-team/marp-cli docs/reports/food-label-conference-2026-beverage-deck.md -o docs/reports/food-label-conference-2026-beverage-deck.pdf --allow-local-files`
  then the same with `-o ...beverage-deck.pptx`.

## Deliverable 3 — Automate Regulatory Updates

The balance of the work, scoped for discussion. The conference summary already
defines the monitoring surface: federal actions (GRAS rule, dye phase-out, UPF
definition, FOP rule, post-market chemical reviews) and a fast-moving state
patchwork (140+ bills, 42 states). A candidate phased shape:

- **Phase A — Define the watch list.** Convert the summary's forces and the
  state-law tables into a structured register (jurisdiction, instrument,
  ingredients/claims affected, status, effective date, source URL). One row per
  obligation; map triggers by ingredient *function*, not name.
- **Phase B — Source the feeds.** Identify authoritative sources per
  jurisdiction (FDA dockets/Federal Register, state legislature trackers,
  Health Canada, OEHHA/Prop 65 list). Decide poll vs. subscribe per source.
- **Phase C — Change detection.** Ingest, diff against the last-seen state, and
  flag new or changed obligations against the watch-list register.
- **Phase D — Surface and route.** Produce the analyst-facing output (digest,
  alert, dashboard) and decide cadence and delivery channel.
- **Human-in-the-loop by default**, consistent with the AI-in-food-safety
  session: automation drafts and flags; an analyst confirms before anything is
  treated as a compliance fact.

Open scope questions are listed below; the build does not start until they are
settled in discussion.

### Status Update (2026-06-17)

The scope questions were answered (see below) and Phases A through D are built.
The data model, seed register, source catalog, jurisdiction catalog (all 50
states plus Canada and Mexico), and change-detection engine live in `regwatch/`
and `scripts/regwatch.py`, with the full design in
`deliverable-3-regulatory-monitoring-design.md`. The engine validates, reports
coverage, lists, captures snapshots, scans with per-source signal extraction,
and emits an analyst report. A weekly `regwatch` workflow runs the scan and
routes the report as an artifact. Validation runs in CI via
`make regwatch-validate`. Remaining work is analyst confirmation of rows against
primary source text and the final delivery channel.

A second layer adds daily and weekly update loops, a CPG impact suite that maps
obligations onto a Talking Rain portfolio model, a beverage analytical lens, and
a synthesis engine that renders the result as a Word document, an email
newsletter, and a web posting. Sample outputs live in
`docs/reports/regwatch-samples/`.

## Phase 0 — Scaffold Reconciliation

Bring the repo into conformance before further build. Each item is a discrete,
low-risk change:

- Remove or relocate the misfiled Tin Can artifact out of the conference folder.
- Route raw conference PDFs to a `sources/` corpus per the Records and
  Source-Corpus Overlay; kebab-rename and log an intake decision. Keep derived
  summaries under `docs/`.
- Rename `docs/genesys/` to correct the typo and align the folder with its
  contents.
- Reconcile tracked `agents/` stubs and project-local `.claude/` against the
  current single-canonical-`CLAUDE.md` model; gitignore or untrack as the
  harness PRs (collapse-to-`CLAUDE.md`, untrack-`.claude`, remove-agent-stubs)
  established.
- Update `project.yml` to the current format (`scaffold-overlays:`,
  `canonical-scaffold:`).
- Add the canonical-spec pointer to root `CLAUDE.md`.
- Resolve the deleted `docs/docs-README.md`: restore it or remove its reference
  from the `Makefile` audit allowlist, and fix the stale `plans-README.md`
  spec citation.
- Commit the now-tracked source material and these deliverables.

## Open Questions for Discussion

Answered 2026-06-17 (marked inline):

1. End goal: a reference knowledge base, a live change-monitoring automation,
   or both? **Answer: both, phased — register first, then monitoring on top.**
2. Audience and product scope: internal compliance-analyst tool, or a broader
   product? **Answer: internal research; do not build a polished front end.
   Get the mechanics, automations, and data model right.**
3. Jurisdiction priority: U.S. federal plus California first, or full
   multi-state plus Canada from the start? **Answer: all 50 US states, Canada,
   and Mexico are modeled; the seed register starts with the federal and
   California obligations we have evidence for plus aggregate multistate rows.**
4. Presentation home: keep the deck in `docs/reports/`, or add a
   `docs/presentations/` route (not yet in the canonical scaffold)? **Still
   open; the deck remains in `docs/reports/`.**
5. Automation runtime: where does it run (local, scheduled cloud agent), and
   what is the alert cadence and delivery channel? **Still open; deferred to
   Phase D. The engine runs locally and offline today.**

## Verification

- `make audit-strict` passes (audits `docs/plans/` and the reference READMEs).
- `make doctor` passes.
- Marp deck re-renders to PDF and PPTX without error.

## Sequencing and Status

- Deliverables 1 and 2: complete this session, pending commit in Phase 0.
- Phase 0: ready to execute; mechanical and low-risk.
- Deliverable 3: blocked on the Open Questions above — to discuss before build.
