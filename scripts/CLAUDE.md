# scripts/CLAUDE.md

#agent-context


Scripts should be deterministic, shell-safe, and runnable from the project
root. Prefer standard-library implementations unless the project already
declares a dependency. The regwatch engine is standard library only — do not
add dependencies.

## Maintenance Scripts

- `audit-markdown.py` — the markdown audit gate (`make audit` / `audit-strict`).
- `build-agents.py` — agent template builder.

## regwatch Engine

`regwatch.py` is the CLI; it imports sibling modules that are pure functions
over loaded data, so they stay testable and free of circular imports:

- `regwatch_impact.py` — CPG impact scoring and the beverage lens.
- `regwatch_synthesis.py` — daily and weekly document-model synthesis.
- `regwatch_render.py` — `.docx`, newsletter, and web-post renderers.
- `regwatch_briefing.py` — the human-readable FDA beverage briefing.
- `regwatch_ingest.py` — Federal Register live ingestion.

Exercised end to end by `make regwatch-smoke`. For diagnosis see
`docs/reference/regwatch-troubleshooting.md`.
