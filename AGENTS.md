# AGENTS.md

## project

- project: regulatory-ingredients-labels-laws

This value must match the directory this repository sits in. Generation fails when it does not, because an `AGENTS.md` copied from another repository once carried the wrong project's content for nine days with nothing to catch it.

## project-contract

This file is the canonical behavioral contract for every AI agent working in this repository.

## project-operating-context

This project provides reference material and tooling for regulatory ingredient and product-label laws. `public/` holds reusable data, reports, and prompt-library content; `projects/` holds private working outputs; `docs/` holds plans, references, and passoffs; and `sources/` holds raw source material.

Primary operational surfaces are `public/regwatch/` for the regulatory monitoring register and `public/prompts/` for the Microsoft 365 Copilot prompt library. The Regwatch engine is `scripts/regwatch.py`.

## operating-rules

- Read a file before editing it and run `make test` before claiming project work complete.
- Regwatch detection and ingestion flag candidates for human review. They never edit the curated register or change log automatically.
- Confirm regulatory claims against primary source text. Nothing the project produces is legal advice or label approval.
- Prompt files are the source of truth for the prompt library. Each prompt uses exactly these H2 sections in order: `prompt-summary`, `use-cases`, `expected-outputs`, `prompt`, `how-to-run`, and `guardrails`.
- Prompt frontmatter uses a `types` list, never a scalar `type`, and each prompt has 6 to 10 natural-language aliases. Run `make prompts-normalize` after hand edits, then run `make prompts-sync`; use `make prompts-docx` when the Word export must be rebuilt.
- The fenced block under a prompt's `prompt` section is the paste-into-Copilot artifact. Do not change it without regenerating the manifests and Word export.
- Keep generated state, dependency artifacts, caches, and local secrets out of commits.

## project-navigation

- Resolve `docs/passoffs/LATEST.pointer` before resuming a prior session.
- Resolve `docs/plans/ACTIVE-DELIVERY-PLAN.pointer` before planning or changing active delivery work.
- Read `public/regwatch/regwatch-README.md` and `public/regwatch/regwatch-troubleshooting.md` before changing Regwatch behavior or data.
- Read `public/prompts/prompt-library-user-guide.md` and `public/prompts/regulatory-labeling.md` before changing the prompt library.

## active-surface-adapters

- `CLAUDE.md`
- `CODEX.md`
- `GEMINI.md`
- `WARP.md`
- `KIRO.md`
- `KIMI.md`
- `LLAMA.md`
- `GROK.md`
- `DEVIN.md`
- `OPENCLAW.md`
- `CURSOR-AGENT.md`

Adapters bootstrap their named clients only. They define no local policy, and this file is authoritative if an adapter conflicts with it.

## installed-agent-clients

- Installed: `claude`, `codex`, `gemini`, `kimi`, `llama`, `devin`, `grok`, `openclaw`, `cursor-agent`, `cursor`, `continue`, and `opencode`.
- Not installed: `warp`, `kiro`, `aider`, `goose`, `amp`, and `qwen`.

## agent-hub-scope

Folder-level nested agent hubs are disabled. Do not add nested `AGENTS.md`, `CLAUDE.md`, or equivalent adapter files unless this contract is explicitly amended. Project-specific operating rules belong in this root contract.

## policy-source

Keep behavioral policy in this root contract. Update `docs/policies/active-policies.md` whenever this contract or a root adapter changes.
