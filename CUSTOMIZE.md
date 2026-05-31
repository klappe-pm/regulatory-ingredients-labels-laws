# CUSTOMIZE

## Mental Model

This scaffold is a working baseline, not a framework. Keep the project-local
parts that help the repository and remove the parts that create maintenance
noise.

## Directory Tour

- `.claude/` holds project-local commands, agents, and disabled hook templates.
- `.github/` holds CI workflow templates.
- `agents/shared/` is the source for generated tool-specific agents.
- `docs/passoffs/` is the required session handoff location.
- `rules/` configures strict Markdown audit carve-outs for scaffold surfaces.
- `scripts/` holds local validation and generation scripts.
- `specs/` contains imported starter references; replace them with project
  specs when useful.

## Recipes

- Slash command: add a Markdown command under `.claude/commands/` or the
  user-scope command library, then validate its behavior with a real run.
- Skill: add `skills/<name>/SKILL.md` only when repeated workflow knowledge is
  stable enough to reuse.
- Agent: edit `agents/shared/<role>.md`, then run `make rebuild-agents`.
- Hook: copy `.claude/hooks/pre-commit-audit.sh.disabled`, remove `.disabled`,
  and keep the hook fast enough for local use.
- MCP server: document the server contract in `specs/` before adding runtime
  configuration.
- Project policy: update `AGENTS.md` first, then mirror only tool-specific
  pointers into `CLAUDE.md`, `WARP.md`, and `GEMINI.md`.

## Edit Freely

Change `README.md`, `project.yml`, `docs/`, `specs/`, `.github/`, and
project-local instructions to fit the repository.

## Leave Alone

Avoid weakening passoff rules, secret-handling rules, and CI checks unless the
project has a replacement with equal or better coverage.

## Settings Split

Checked-in project policy belongs in source control. Personal settings,
tokens, credentials, and machine-local overrides belong in ignored files or
external secret stores.

## Agent Pipeline

The shared agent prompts in `agents/shared/` generate Claude Code, Codex,
Cursor, and Gemini agent definitions through `scripts/build-agents.py`.
Generated files are deterministic; rerunning `make rebuild-agents` should not
produce drift unless a shared prompt changed.

## Strip Targets

Use `make strip-agents`, `make strip-hooks`, `make strip-specs`,
`make strip-warp`, and `make strip-gemini` to remove scaffold features that do
not belong in the project.

## Validation Tiers

- `make doctor` checks required scaffold files.
- `make audit-strict` runs the Markdown policy audit.
- `make test` runs the local project smoke gate.

## Troubleshooting

- If agent output changes unexpectedly, rerun `make rebuild-agents` twice and
  compare `git diff`.
- If audit fails on imported docs, either fix the docs or add a narrow
  carve-out in `rules/runtime-format-carveouts.md`.
- If the first commit fails, configure Git author identity and rerun the
  scaffold command in a new target directory.

## Lessons-Learned Anti-Patterns

- Do not copy user-scope secrets into project templates.
- Do not make every project carry every tool if it will not use them.
- Do not let generated files hide the shared source that produced them.
- Do not create passoffs outside the repository they describe.
