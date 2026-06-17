# regulatory-ingredients-labels-laws

Automate regulatory updates for product ingredients, labels, and labeling laws.

`Regulatory Ingredients Labels Laws` is scaffolded from the shared
`/Users/kevinlappe/.claude` project template.

## Quick Start

```bash
make doctor
make audit-strict
make test
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
