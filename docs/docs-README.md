# Scaffolding Documentation Index

This directory separates active project documents from reference and legacy
material.

## Active Specs

The active specs live in `../specs/`:

- `specs-project-scaffold-framework-spec.md` - canonical implementation spec.
- `specs-projects-folder-purpose-audit.md` - recursive folder-purpose evidence.
- `specs-projects-folder-purpose-audit.json` - machine-readable folder inventory.
- `specs-projects-git-history-structure-audit.md` - Git/history evidence.
- `specs-projects-git-history-structure-audit.json` - machine-readable Git inventory.
- `../project.yml` - local project manifest for identity, naming exceptions, and nested repo status.

## Reference Material

Reference documents live under `reference/`.

- `reference/environment/environment-keychain-env-setup.md` - canonical setup record for
  Keychain-backed environment loading.
- `reference/environment/environment-global-credentials-guide.md` - compatibility guide for
  accessing credentials from projects.
- `reference/environment/environment-ide-credentials-guide.md` - IDE and terminal access
  compatibility guide.
- `reference/environment/environment-macos-machine-specs.md` - local machine profile for
  environment-sensitive recommendations.
- `reference/legacy/legacy-github-configuration.md` - status note for the nested
  legacy GitHub auth repo.

## Plans

`plans/` is reserved for implementation plans derived from the canonical spec.
Plans should be dated or named by workstream and should not override the spec.

## Archive

`archive/` is reserved for retired or superseded documents from the parent
`scaffolding` project. Legacy nested-repo notes belong in `reference/legacy/`
unless the actual content is being retired from this project.

## Passoffs

`passoffs/` is reserved for future session handoffs once the parent
`scaffolding` folder is initialized as a Git repo.

## Deconfliction Rules

- The scaffold implementation spec is canonical for what to build.
- The audit files are evidence, not implementation instructions by themselves.
- Environment docs describe local machine setup and must not be copied into
  generated projects as defaults.
- The nested `github-config/` repo is legacy/reference material until a
  specific migration task promotes selected content.
