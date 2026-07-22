# Regulatory Ingredients Labels Laws Claude Code Instructions

#agent-context


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
- Run the project verification command (`make test`) before claiming work is
  complete.
- Plan-backed commit, push, PR creation, and merge are authorized when
  verification, required checks, and merge criteria pass.

## regwatch

The regulatory monitoring engine lives in `public/regwatch/` (data) and `scripts/regwatch*.py` (engine, standard library only). Before working on it, read `public/regwatch/CLAUDE.md` for the operating rules and `public/regwatch/regwatch-troubleshooting.md` for the runbook. Detection and ingestion flag for human review; they never auto-edit the register or change log. Nothing the engine emits is legal advice. Generated rollout reports and samples live under `projects/regwatch-rollout/` and `projects/regwatch-samples/`.

## prompt library

The Microsoft 365 Copilot prompt library lives in `public/prompts/`, an Obsidian vault surface. The `.md` prompt files are the single source of truth: each per-category `.manifest.json` and the Word export (`public/prompts/regulatory-labeling-prompt-library.docx`) are generated from them by `scripts/sync-prompt-manifests.py` and `scripts/build-prompt-library-docx.py`. After editing any prompt, run `make prompts-sync` (or `make prompts-docx` to also rebuild the Word file); `make test` runs `prompts-check` and fails on manifest drift. Every compliance-facing prompt is human-sign-off gated, marks citations unverified until confirmed against the current eCFR, and never approves a label. Prompt outputs save to `projects/regulatory-labeling/` (private); only `copilot-configuration` routing notes save to `public/regulatory-labeling/`.

Prompt files use exactly six H2 sections in this order: prompt-summary, use-cases, expected-outputs, prompt, how-to-run, guardrails. The fenced block under `## prompt` is the paste-into-Copilot artifact; never change its body without regenerating manifests and the docx. Frontmatter follows the vault linter schema: `types` is a list (never a scalar `type`), key order is domain, category, sub-category, types, date-created, date-revised, then remaining keys alphabetically, with `aliases` and `tags` last; `scripts/normalize-prompt-frontmatter.py` enforces this (run `make prompts-normalize` after hand edits). Every prompt carries 6 to 10 natural-language `aliases` for search; keep them current when a prompt's job changes. Navigation is flat: no per-category index notes; the home note `regulatory-labeling.md` (Bases tables), `prompt-explorer.md` (Dataview dashboard, needs the Dataview community plugin), and `prompt-library-user-guide.md` are the only navigation surfaces. Bases (`public/prompts/bases/*.base`) reference hyphenated frontmatter keys with bracket notation (`note["sub-category"]`) and test the `types` list with `.contains()`; keep those forms.

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

Project layout and agent routing follow the canonical scaffold spec: `/Users/kevinlappe/Projects/harness/scaffolding/project-routing-spec.md`. This project applies the Records and Source-Corpus overlay: raw source material lives under `sources/`; derived summaries and reports live under `docs/`.

This overlay description is stale for one deliberate deviation: operational data and generated reports intended for reuse or sharing live under `public/` (for example `public/regwatch/`, `public/prompts/`), and private working outputs live under `projects/` (for example `projects/regwatch-rollout/`, `projects/regwatch-samples/`, `projects/regulatory-labeling/`). This split is not yet reflected in the canonical scaffold spec; treat `public/` and `projects/` as this project's convention, additive to, not a replacement for, the overlay's `sources/`/`docs/` structure.
