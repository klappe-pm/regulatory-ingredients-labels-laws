# Regulatory Ingredients Labels Laws Claude Code Instructions

Follow this file before editing this repository. Project-local instructions
augment, but do not replace, the user-scope policy in
`/Users/kevinlappe/.claude/`.

## Project Identity

- Name: `Regulatory Ingredients Labels Laws`
- Slug: `regulatory-ingredients-labels-laws`
- Root: `/Users/kevinlappe/Projects/regulatory-ingredients-labels-laws`
- GitHub: `https://github.com/klappe-pm/regulatory-ingredients-labels-laws`

## Operating Rules

- Read files before editing them.
- Keep generated, dependency, cache, and local-secret files out of commits.
- Store session passoffs in `docs/passoffs/`. Read
  `docs/passoffs/LATEST.pointer`, resolve the target relative to that
  directory, and read the latest passoff before work.
- Run the project verification command before claiming work is complete.
- Plan-backed commit, push, PR creation, and merge are authorized when
  verification, required checks, and merge criteria pass.

## Active Routing

Current document paths are routed through stable `.pointer` files. Each pointer
is one line containing a path relative to the pointer file's directory. Read the
pointer, then read the resolved target; update the pointer when a current
document is superseded.

| Pointer | Resolves to |
|---|---|
| `docs/passoffs/LATEST.pointer` | Latest passoff |
| `docs/plans/ACTIVE-DELIVERY-PLAN.pointer` | Current delivery plan |
| `docs/reports/BEVERAGE-BRIEFING.pointer` | Current beverage briefing |
| `docs/reports/BEVERAGE-DECK.pointer` | Current beverage deck source |

## Project Layout

Project layout and agent routing follow the canonical scaffold spec:
`/Users/kevinlappe/Projects/harness/scaffolding/project-routing-spec.md`.
This project applies the Records and Source-Corpus overlay: raw source
material lives under `sources/`; derived summaries and reports live under
`docs/`.
