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
├── scripts/          Project maintenance scripts
├── AGENTS.md         Cross-agent project instructions
├── CUSTOMIZE.md      Scaffold tailoring guide
├── Makefile          Validation and strip targets
└── project.yml       Project identity manifest
```

Session handoffs belong in `docs/passoffs/`. Local secrets and machine state
belong outside the repo or in ignored files.
