# active-policy-text-snapshot

This deterministic snapshot contains the root contract and root adapters in alphabetical filename order.

## AGENTS.md

```markdown
# AGENTS.md

## project-contract

This file is the canonical behavioral contract for every AI agent working in this repository.

## project-operating-context

This project provides reference material and tooling for regulatory ingredient and product-label laws. `public/` holds reusable data, reports, and prompt-library content; `projects/` holds private working outputs; `docs/` holds plans, references, and passoffs; and `sources/` holds raw source material.

Primary operational surfaces are `public/regwatch/` for the regulatory monitoring register and `public/prompts/` for the Microsoft 365 Copilot prompt library. The Regwatch engine is `scripts/regwatch.py`.

## operating-rules

- Read a file before editing it and run `make test` before claiming project work complete.
- Regwatch detection and ingestion flag candidates for human review. They never edit the curated register or change log automatically.
- Confirm regulatory claims against primary source text. Nothing the project produces is legal advice or label approval.
- Prompt files are the source of truth for the prompt library. After editing a prompt, run `make prompts-sync`; use `make prompts-docx` when the Word export must be rebuilt.
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
```

## CLAUDE.md

```markdown
@AGENTS.md

# CLAUDE.md

Startup adapter for Claude Code, canonical contract is [AGENTS.md](AGENTS.md).

## contract-pointer

Claude Code imports `AGENTS.md` during session bootstrap through the directive above.

## scope

No local policy is defined here. [AGENTS.md](AGENTS.md) is authoritative on conflict.
```

## CODEX.md

```markdown
# CODEX.md

Startup adapter for Codex, canonical contract is [AGENTS.md](AGENTS.md).

## contract-pointer

Codex reads the root `AGENTS.md` before acting in this repository.

## scope

No local policy is defined here. [AGENTS.md](AGENTS.md) is authoritative on conflict.
```

## CURSOR-AGENT.md

```markdown
# CURSOR-AGENT.md

Startup adapter for Cursor Agent CLI, canonical contract is [AGENTS.md](AGENTS.md).

## contract-pointer

Cursor Agent CLI must read the root `AGENTS.md` before acting in this repository.

## scope

No local policy is defined here. [AGENTS.md](AGENTS.md) is authoritative on conflict.
```

## DEVIN.md

```markdown
# DEVIN.md

Startup adapter for Devin CLI, canonical contract is [AGENTS.md](AGENTS.md).

## contract-pointer

Devin CLI must read the root `AGENTS.md` before acting in this repository.

## scope

No local policy is defined here. [AGENTS.md](AGENTS.md) is authoritative on conflict.
```

## GEMINI.md

```markdown
# GEMINI.md

Startup adapter for Gemini CLI, canonical contract is [AGENTS.md](AGENTS.md).

## contract-pointer

Gemini CLI must read the root `AGENTS.md` before acting in this repository.

## scope

No local policy is defined here. [AGENTS.md](AGENTS.md) is authoritative on conflict.
```

## GROK.md

```markdown
# GROK.md

Startup adapter for Grok CLI, canonical contract is [AGENTS.md](AGENTS.md).

## contract-pointer

Grok CLI must read the root `AGENTS.md` before acting in this repository.

## scope

No local policy is defined here. [AGENTS.md](AGENTS.md) is authoritative on conflict.
```

## KIMI.md

```markdown
# KIMI.md

Startup adapter for Kimi CLI, canonical contract is [AGENTS.md](AGENTS.md).

## contract-pointer

Kimi CLI must read the root `AGENTS.md` before acting in this repository.

## scope

No local policy is defined here. [AGENTS.md](AGENTS.md) is authoritative on conflict.
```

## KIRO.md

```markdown
# KIRO.md

Startup adapter for Kiro CLI, canonical contract is [AGENTS.md](AGENTS.md).

## contract-pointer

Kiro CLI must read the root `AGENTS.md` before acting in this repository.

## scope

No local policy is defined here. [AGENTS.md](AGENTS.md) is authoritative on conflict.
```

## LLAMA.md

```markdown
# LLAMA.md

Startup adapter for Llama CLI, canonical contract is [AGENTS.md](AGENTS.md).

## contract-pointer

Llama CLI must read the root `AGENTS.md` before acting in this repository.

## scope

No local policy is defined here. [AGENTS.md](AGENTS.md) is authoritative on conflict.
```

## OPENCLAW.md

```markdown
# OPENCLAW.md

Startup adapter for OpenClaw CLI, canonical contract is [AGENTS.md](AGENTS.md).

## contract-pointer

OpenClaw CLI must read the root `AGENTS.md` before acting in this repository.

## scope

No local policy is defined here. [AGENTS.md](AGENTS.md) is authoritative on conflict.
```

## WARP.md

```markdown
# WARP.md

Startup adapter for Warp CLI, canonical contract is [AGENTS.md](AGENTS.md).

## contract-pointer

Warp CLI must read the root `AGENTS.md` before acting in this repository.

## scope

No local policy is defined here. [AGENTS.md](AGENTS.md) is authoritative on conflict.
```
