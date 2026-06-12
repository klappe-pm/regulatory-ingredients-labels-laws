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

## Deliverable 1 — Conference Summary (Done)

- Output: `../reports/food-label-conference-2026-summary.md`.
- Method: nine parallel extraction agents, one per PDF (177 pages total),
  each returning a structured digest; synthesised into one themed summary.
- Shape: the one-sentence takeaway (2026 is a convergence year), the five
  forces reshaping the label, the MAHA driver, the state patchwork (California
  as template), the legal mechanics (preemption carve-out, Prop 65), claims
  defensibility, beverage-specific flags, and an eight-step analyst playbook.

## Deliverable 2 — Presentation (Done)

- Source: `../reports/food-label-conference-2026-deck.md` (Marp markdown).
- Built artifacts: `food-label-conference-2026-deck.pdf` and
  `food-label-conference-2026-deck.pptx` (editable), rendered via
  `@marp-team/marp-cli`.
- Design: ~22 slides for a 20-minute slot, Duarte Sparkline arc (current
  reality vs. better future), one idea per slide, titles state the takeaway,
  speaker notes in HTML comments. Big Idea: "readiness, not prediction."
- Re-render command:
  `npx @marp-team/marp-cli docs/reports/food-label-conference-2026-deck.md --pdf --pptx --allow-local-files`.

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

1. End goal: a reference knowledge base, a live change-monitoring automation,
   or both? This sets the depth of Deliverable 3.
2. Audience and product scope: internal compliance-analyst tool, or a broader
   product? Single company (beverage) or multi-category?
3. Jurisdiction priority: U.S. federal plus California first, or full
   multi-state plus Canada from the start?
4. Presentation home: keep the deck in `docs/reports/`, or add a
   `docs/presentations/` route (not yet in the canonical scaffold)?
5. Automation runtime: where does it run (local, scheduled cloud agent), and
   what is the alert cadence and delivery channel?

## Verification

- `make audit-strict` passes (audits `docs/plans/` and the reference READMEs).
- `make doctor` passes.
- Marp deck re-renders to PDF and PPTX without error.

## Sequencing and Status

- Deliverables 1 and 2: complete this session, pending commit in Phase 0.
- Phase 0: ready to execute; mechanical and low-risk.
- Deliverable 3: blocked on the Open Questions above — to discuss before build.
