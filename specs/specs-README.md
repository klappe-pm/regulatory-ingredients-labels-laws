# specs-README

## Canonical Spec

- `specs-project-scaffold-framework-spec.md` - canonical implementation spec for the
  `scaffolding` project and future `scaffold` command.

## Evidence Artifacts

- `specs-projects-folder-purpose-audit.md` - human-readable recursive folder-purpose
  audit of `/Users/kevinlappe/Projects`.
- `specs-projects-folder-purpose-audit.json` - machine-readable inventory backing the
  folder-purpose audit.
- `specs-projects-git-history-structure-audit.md` - human-readable Git/history audit
  covering repository structure, passoffs, `.github`, dirty state, and recent
  commits.
- `specs-projects-git-history-structure-audit.json` - machine-readable inventory
  backing the Git/history audit.

## Usage

Implementation agents must read the canonical spec and both human-readable audit
files before creating templates, commands, skills, GitHub workflows, or retrofit
logic.

Do not edit audit artifacts to fit a preferred design. If the workspace changes,
regenerate or append a dated audit note.
