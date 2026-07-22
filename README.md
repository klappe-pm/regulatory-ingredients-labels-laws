# regulatory-ingredients-labels-laws

Automate regulatory updates for product ingredients, labels, and labeling laws.

`Regulatory Ingredients Labels Laws` is scaffolded from the shared
`/Users/kevinlappe/.claude` project template.

## Quick Start

```bash
make doctor
make audit-strict
make test          # also runs regwatch-validate and regwatch-smoke
```

## regwatch — Regulatory Monitoring

`regwatch` is the regulatory monitoring engine: a validated obligation register,
a change-detection scanner, a live Federal Register ingest, a CPG impact suite
over a Talking Rain portfolio model, and rendered outputs (a human-readable FDA
beverage briefing, a Word document, an email newsletter, and a web post). It is
standard library only.

```bash
python3 scripts/regwatch.py --help        # all commands
python3 scripts/regwatch.py validate      # data model
python3 scripts/regwatch.py briefing      # human-readable FDA beverage briefing
python3 scripts/regwatch.py ingest --live # pull the Federal Register feed
```

- Engine and data: `public/regwatch/regwatch-README.md`.
- Design: `docs/plans/deliverable-3-regulatory-monitoring-design.md`.
- Troubleshooting runbook for agents: `public/regwatch/regwatch-troubleshooting.md`.

Nothing the engine emits is legal advice; confirm against primary source text.

## Copilot Prompt Library

`public/prompts/` is an Obsidian-navigable library of Microsoft 365 Copilot prompts for the regulatory labeling specialist workflow (US FDA / CFR 21). It spans onboarding setup, label intake, content derivation, claims compliance, review and verification, version reconciliation, market and reporting, email, durable knowledge, Copilot configuration, app-specific skills, and reflection.

- Start here: `public/prompts/prompt-library-user-guide.md`, then the master index `public/prompts/regulatory-labeling.md`.
- Every compliance prompt is human-sign-off gated, marks its citations unverified until confirmed against the current eCFR, and never approves a label. Nothing in the library is legal advice.
- The `.md` prompt files are the single source of truth. The per-category `.manifest.json` sidecars and the Word export are generated from them:

```bash
make prompts-sync   # regenerate .manifest.json from the .md prompts
make prompts-check  # fail if any manifest is stale (part of make test)
make prompts-docx   # rebuild the hyperlinked Word export
```

## Project Structure

```text
.
├── .claude/          Project-local commands, agents, and hooks
├── .github/          CI workflow templates
├── agents/           Shared and generated agent definitions
├── docs/             Plans, passoffs, and reference material
├── regwatch/         Regulatory watch-list register, source catalog, and state
├── scripts/          Project maintenance scripts and the regwatch engine
├── CLAUDE.md         Claude Code project instructions
├── Makefile          Validation and strip targets
└── project.yml       Project identity manifest
```

Session handoffs belong in `docs/passoffs/`. Local secrets and machine state
belong outside the repo or in ignored files.
