# Scaffolding Project Framework Spec

## Summary

Build `scaffolding`, a reusable project initiation repository that provides a
local command, `scaffold`, for creating and retrofitting projects under
`/Users/kevinlappe/Projects` with consistent folder structure, documentation,
agent instructions, Git initialization, GitHub repository setup, and shared
GitHub governance. The system must reduce cognitive load when starting a new
project while preserving project-specific overrides.

Canonical local project:

```text
/Users/kevinlappe/Projects/scaffolding
```

Canonical GitHub repository:

```text
https://github.com/klappe-pm/scaffolding
```

This spec is written for an LLM implementation agent. Follow it directly, but
read the current tree before editing and do not commit unless the user explicitly
asks in the current turn.

## Current Context

The project folder is:

```text
/Users/kevinlappe/Projects/scaffolding
```

At the time this spec was revised, the parent folder was not yet a Git
repository even though the intended remote is
`https://github.com/klappe-pm/scaffolding`. It contains an older nested Git repo:

```text
/Users/kevinlappe/Projects/scaffolding/github-config
```

That nested repo contains early GitHub credential and setup scripts, but some
scripts hardcode stale paths under `/Users/kevinlappe/Documents`. Treat those
scripts as reference material, not production scaffolding code.

This spec is not standalone. It must be read with these evidence artifacts:

```text
/Users/kevinlappe/Projects/scaffolding/specs/specs-projects-folder-purpose-audit.md
/Users/kevinlappe/Projects/scaffolding/specs/specs-projects-folder-purpose-audit.json
/Users/kevinlappe/Projects/scaffolding/specs/specs-projects-git-history-structure-audit.md
/Users/kevinlappe/Projects/scaffolding/specs/specs-projects-git-history-structure-audit.json
```

The folder-purpose audit recursively covers every project-owned folder and
subfolder under `/Users/kevinlappe/Projects`, excluding only generated,
dependency, cache, build, virtual-environment, and Git internals from recursive
purpose analysis. Those excluded roots are still recorded as internal/generated
folders in the audit.

The Git/history audit covers every detected Git root, including remotes, dirty
state, root governance files, passoff coverage, `.github` coverage, top changed
directories and files, and recent commit history since `2026-02-08`.

The audits found these patterns across active projects:

- Strong repo-local governance exists in `docs/passoffs/`.
- Root instruction files are inconsistent but valuable: `AGENTS.md`,
  `CLAUDE.md`, `WARP.md`, and `GEMINI.md`.
- Active repos usually have `README.md`, `docs/`, and `scripts/`.
- Most active repos do not have `.github/` governance checked in.
- The archived `Lattice Lock` project has the richest `.github` example, but it
  is too heavyweight to copy directly.
- Several project-like directories under `/Users/kevinlappe/Projects` are not
  Git repos and need classification before automated setup.

Any implementation agent must read the audit artifacts before writing templates,
default folder layouts, retrofit logic, or GitHub workflow wrappers. If the
implementation changes the scaffold assumptions, update the audits or add a new
dated audit note instead of relying on memory.

## Goals

1. Deliver `/Users/kevinlappe/Projects/scaffolding` as the canonical reusable
   project initiation repo.
2. Provide one command, `scaffold`, for creating new projects.
3. Provide an audit mode that recursively classifies existing folders under
   `/Users/kevinlappe/Projects`.
4. Provide a retrofit mode for existing projects that are missing standard
   structure or GitHub governance.
5. Standardize project structure, documentation, passoff support, and agent
   instruction files.
6. Standardize `.github` configuration through thin per-repo wrappers that call
   reusable workflows hosted by `klappe-pm/scaffolding`.
7. Allow project-specific overrides through a checked-in `project.yml`.
8. Keep operations safe: dry-run by default for destructive actions. Allow
   plan-backed git and GitHub ship flow through merge when verification,
   required checks, and merge criteria pass.
9. Preserve the observed project categories from the recursive audit rather than
   flattening everything into a single generic application template.

## Non-Goals

- Do not migrate every existing project in the first implementation.
- Do not commit or push without a user task and a stated plan. Once that plan
  exists, commit, push, PR creation, and merge are authorized when verification,
  required checks, and merge criteria pass.
- Do not force every folder under `/Users/kevinlappe/Projects` to become a Git
  repo.
- Do not copy secrets, OAuth tokens, local credential values, or
  `settings.local.json` into any scaffolded project.
- Do not make the scaffold depend on a single LLM provider.
- Do not directly copy the full `Lattice Lock` `.github` setup into every repo.

## Required Command Surface

Implement a CLI named `scaffold`. The first implementation may be a Python script
installed through a shell shim.

Required top-level commands:

```bash
scaffold new
scaffold audit /Users/kevinlappe/Projects
scaffold retrofit /absolute/path/to/project
scaffold doctor
scaffold templates list
scaffold github status
scaffold github bootstrap
scaffold skills plan
scaffold commands plan
```

Required global flags:

```bash
--dry-run
--yes
--verbose
--no-github
--github-visibility private|public
--owner klappe-pm
```

Default behavior:

- `scaffold new` is interactive unless all required values are provided.
- `scaffold audit` never mutates files unless paired with an explicit future
  `--write-report` flag.
- `scaffold retrofit` defaults to dry-run and prints the planned file additions
  and edits.
- GitHub repository creation requires `--yes` or an interactive confirmation.
- Commit and push require explicit confirmation even when `--yes` is present,
  unless a later version adds a clearly named `--commit --push` pair.

### CLI Command Contract

`scaffold` must be boring and explicit. Every command should print what it will
read, what it will write, what external commands it will run, and which actions
are skipped because they need approval.

#### `scaffold new`

Purpose: create a new project from templates.

Required inputs, collected interactively if omitted:

```text
project name
project slug
project type
parent directory
GitHub owner
GitHub visibility
whether to initialize Git
whether to create GitHub remote
whether to create first commit
```

Required flags:

```bash
scaffold new --name "Average Intelligence" --slug average-intelligence --type content
scaffold new --parent /Users/kevinlappe/Projects --owner klappe-pm --github-visibility private
scaffold new --dry-run
scaffold new --no-github
```

Output:

- planned filesystem tree;
- template set selected and why;
- Git commands that would run;
- GitHub commands that would run;
- validation command;
- next manual actions.

#### `scaffold audit`

Purpose: recursively classify folders and Git roots.

Required flags:

```bash
scaffold audit /Users/kevinlappe/Projects --format markdown
scaffold audit /Users/kevinlappe/Projects --format json
scaffold audit /Users/kevinlappe/Projects --write-report
```

Output:

- folder-purpose inventory comparable to
  `specs/specs-projects-folder-purpose-audit.json`;
- Git/history inventory comparable to
  `specs/specs-projects-git-history-structure-audit.json`;
- project-candidate list;
- missing-governance list;
- unsafe-to-retrofit list;
- archive/vault/data-only classifications.

#### `scaffold retrofit`

Purpose: add missing governance to an existing folder or repo.

Required behavior:

- read current files before edits;
- detect dirty Git state;
- refuse destructive rewrites by default;
- generate a patch plan before writing;
- support additive-only mode.

Required flags:

```bash
scaffold retrofit /absolute/path --dry-run
scaffold retrofit /absolute/path --additive-only
scaffold retrofit /absolute/path --apply
scaffold retrofit /absolute/path --include github,instructions,passoffs
```

Output:

- classification of the target;
- missing files;
- files that exist and will be left alone;
- proposed patches;
- verification command.

#### `scaffold doctor`

Purpose: validate the scaffolding repo itself and any generated project.

Checks:

- `project.yml` schema;
- template placeholder coverage;
- command manifests;
- skill manifests;
- `.github` wrapper syntax;
- passoff directory presence;
- root instruction consistency;
- no stale `/Users/kevinlappe/Documents` paths in production files;
- no secrets or local-only settings in tracked templates.

#### `scaffold github status`

Purpose: report whether GitHub setup can run safely.

Checks:

- `gh auth status`;
- current token scopes where visible;
- default owner availability;
- whether the target repo already exists;
- whether workflow-scope actions are blocked.

This command must not run `gh auth refresh`. It may print the exact command the
user should run manually.

#### `scaffold github bootstrap`

Purpose: create or verify GitHub repo configuration after local project
creation.

Required behavior:

- confirm before `gh repo create`;
- confirm before adding or changing `origin`;
- confirm before pushing;
- never auto-enable branch protection until the repo has a successful initial
  CI run;
- print any GitHub settings that require web UI action.

#### `scaffold templates list`

Purpose: show available project templates, their source evidence, and their
included folders.

Output must identify which existing project informed each template.

#### `scaffold skills plan`

Purpose: print the Codex/agent skills that this repo should eventually install
or export.

Output must include skill name, trigger description, bundled resources, and
implementation status.

#### `scaffold commands plan`

Purpose: print the agent commands that should exist in `commands/` and explain
when each should be used.

Output must include command name, purpose, backing CLI command, required
confirmations, and output artifact.

## Required Agent Commands

In addition to the CLI, the repository should provide agent-facing command
definitions under:

```text
commands/
```

These are not shell scripts. They are prompt/procedure files that tell an LLM how
to operate the `scaffold` CLI safely.

Required command files:

```text
commands/commands-scaffold-new.md
commands/commands-scaffold-audit.md
commands/commands-scaffold-retrofit.md
commands/commands-scaffold-github-bootstrap.md
commands/commands-scaffold-doctor.md
commands/commands-scaffold-passoff.md
```

### `/scaffold-new`

Use when the user wants to start a new project. It must:

1. Read `specs/specs-project-scaffold-framework-spec.md`.
2. Ask for missing required inputs only.
3. Run `scaffold new --dry-run`.
4. Show the plan.
5. Ask before applying filesystem changes.
6. Ask separately before GitHub creation, commit, or push.

### `/scaffold-audit`

Use when the user wants the workspace audited. It must:

1. Run `scaffold audit /Users/kevinlappe/Projects --dry-run`.
2. Compare output coverage to the saved audit artifacts.
3. Write updated reports only after explicit approval.
4. Surface project candidates, unsafe retrofits, and missing governance.

### `/scaffold-retrofit`

Use when the user wants an existing project brought into the standard structure.
It must:

1. Read the target's current files and Git state.
2. Run `scaffold retrofit <target> --dry-run --additive-only`.
3. Show planned additions and conflicts.
4. Ask before applying.
5. Stop at `git status` unless the user explicitly asks for commit/push.

### `/scaffold-github-bootstrap`

Use when local scaffolding is complete and the user wants GitHub setup. It must:

1. Run `scaffold github status`.
2. Refuse to run browser-auth flows from inside the agent.
3. Ask before `gh repo create`.
4. Ask before changing remotes.
5. Ask before pushing.

### `/scaffold-doctor`

Use before reporting scaffolding work complete. It must run `scaffold doctor`
and the generated project's verification command.

### `/scaffold-passoff`

Use when ending a scaffolding session inside a Git repo. It must follow the
global passoff rules and write the passoff to the repo-local `docs/passoffs/`.
If the current folder is not a Git repo, it must not create a passoff and must
state that Git initialization is required first.

## Required Skills

The scaffolding repo should define a small set of Codex/agent skills. These
skills are reusable procedural knowledge for agents; they are distinct from the
CLI and distinct from slash-style commands.

Place project-owned skill definitions under:

```text
skills/
```

Each skill folder must contain `SKILL.md`. Add `references/`, `scripts/`, or
`assets/` only when they reduce repeated work or protect correctness. Keep
`SKILL.md` concise and move large examples into `references/`.

### Skill: `project-folder-auditor`

Purpose: audit a workspace recursively and infer each folder's purpose.

Trigger description:

```text
Use when Codex needs to inspect a workspace or project folder recursively,
classify folders by purpose, identify Git roots, distinguish project-owned
content from generated/dependency internals, and produce Markdown/JSON audit
artifacts for scaffolding or retrofit planning.
```

Required resources:

- `references/classification-taxonomy.md`: folder classifications and signals.
- `scripts/audit_workspace.py`: deterministic audit implementation.

Must enforce:

- every project-owned folder gets a purpose note;
- generated/dependency/internal roots are recorded, then pruned;
- evidence comes from names, marker files, README headings, Git metadata, and
  recent history where available.

### Skill: `project-scaffold-planner`

Purpose: turn audit evidence into a project initialization or retrofit plan.

Trigger description:

```text
Use when Codex needs to design or revise a project scaffold from observed local
repository patterns, choose a project type template, map required governance
files, and produce a step-by-step implementation plan before any filesystem or
GitHub mutation.
```

Required resources:

- `references/template-selection.md`: how project types map to templates.
- `references/source-project-patterns.md`: distilled patterns from
  `claude-config`, `skills-main`, `average-intelligence`, `claude-automation`,
  and `Lattice Lock`.

Must enforce:

- no one-size-fits-all template;
- template choices trace back to audit evidence;
- retrofit plans distinguish additive files from conflicting rewrites.

### Skill: `github-governance-bootstrapper`

Purpose: configure GitHub governance safely.

Trigger description:

```text
Use when Codex needs to create or verify GitHub repository setup for a scaffolded
project, add thin workflow wrappers, inspect gh authentication state, plan branch
protection, or explain which GitHub actions require explicit user approval.
```

Required resources:

- `references/github-governance.md`: wrapper workflow design and approval gates.
- `assets/github/`: workflow wrapper templates and PR template.

Must enforce:

- never run `gh auth refresh` inside an agent session unless the user confirms
  they can complete browser approval immediately;
- never commit workflow files if current credentials cannot push workflow
  changes;
- merge only after required checks pass and merge blockers are absent.

### Skill: `project-instruction-author`

Purpose: author root agent instructions and project governance docs.

Trigger description:

```text
Use when Codex needs to create or retrofit project-prefixed root instruction
files such as <project-slug>-AGENTS.md, <project-slug>-CLAUDE.md,
<project-slug>-WARP.md, <project-slug>-GEMINI.md, <project-slug>-README.md,
docs/governance, or docs/passoffs instructions for a new or existing project
while preserving local authority order and verification commands.
```

Required resources:

- `references/instruction-surfaces.md`: required sections by file.
- `assets/instructions/`: base templates for root instruction files.

Must enforce:

- the project-prefixed AGENTS file is the cross-agent source of truth where
  present;
- agent-specific files point to the canonical project instructions instead of
  drifting;
- passoff rules stay repo-local.

### Skill: `scaffold-retrofit-reviewer`

Purpose: review retrofit plans before mutation.

Trigger description:

```text
Use when Codex needs to review a proposed scaffold retrofit for risk, conflicts,
dirty worktree hazards, accidental rewrites, nested Git repos, secrets exposure,
or mismatch between project purpose and selected template.
```

Required resources:

- `references/retrofit-risk-checklist.md`: review checklist.

Must enforce:

- dirty repos require explicit handling;
- nested Git repos are not moved or deleted automatically;
- vaults and archives are classified before governance is added;
- output is findings-first, with exact file paths and commands.

## Standard Project Layout

Every new project should start with this baseline:

```text
<project>/
  <project-slug>-README.md
  <project-slug>-AGENTS.md
  <project-slug>-CLAUDE.md
  <project-slug>-WARP.md
  <project-slug>-GEMINI.md
  project.yml
  .gitignore
  .env.example
  docs/
    docs-README.md
    passoffs/
      .gitkeep
    governance/
      governance-README.md
    specs/
      specs-README.md
    plans/
      plans-README.md
    reference/
      reference-README.md
    ops/
      ops-README.md
  scripts/
    scripts-README.md
    verify.sh
  commands/
    commands-README.md
  skills/
    skills-README.md
  tests/
    tests-README.md
  schemas/
    schemas-README.md
  .github/
    pull_request_template.md
    dependabot.yml
    workflows/
      repo-hygiene.yml
      ci.yml
```

### Naming Rule

Project-owned files must start with the name of the folder that contains them.
Examples:

- files in `specs/` start with `specs-`;
- files in `docs/` start with `docs-`;
- files in `docs/reference/environment/` start with `environment-`;
- root project documents start with the project slug, such as
  `scaffolding-README.md`.

Functional dotfiles, ecosystem-required files, and externally imposed entrypoint
names are allowed exceptions:

- `.gitignore`
- `.env.example`
- `.gitkeep`
- `project.yml`
- GitHub-required files under `.github/`
- Codex-required `SKILL.md` files inside skill folders
- Python-required `__init__.py` package marker files
- installed console command names, such as the final user-facing command
  `scaffold`
- language/package files whose names are fixed by tooling, such as
  `pyproject.toml`, `package.json`, `go.mod`, and `Cargo.toml`

When a standard ecosystem file is required, keep the standard filename and record
the exception in `project.yml`.

Project type templates may add folders:

- `python`: `pyproject.toml`, `src/`, `tests/`, Python CI wrapper.
- `node`: `package.json`, `src/`, Node CI wrapper.
- `content`: `content/`, `brand/`, `docs/strategy/`, docs-only CI wrapper.
- `agent-config`: `commands/`, `skills/`, `agents/`, `schemas/`, validation
  scripts.
- `vault`: Obsidian-aware ignore rules and explicit privacy warnings.
- `mixed`: minimal generic structure plus manually selected modules.

For ordinary projects, `commands/` and `skills/` may contain only README files
that explain whether the project defines local agent commands or skills. For
`scaffolding` itself and `agent-config` projects, those folders are active
implementation surfaces.

## `project.yml` Contract

Create `project.yml` in every scaffolded repo. It is the central override file.

Minimum schema:

```yaml
schema_version: 1
name: example-project
slug: example-project
owner: klappe-pm
visibility: private
project_type: mixed
default_branch: main

governance:
  passoffs: true
  root_agent_instructions: true
  pr_required: true
  auto_merge_allowed: false

github:
  enabled: true
  centralized_workflows: true
  workflow_ref: v1
  required_workflows:
    - repo-hygiene
    - ci

validation:
  local_command: ./scripts/verify.sh
  generated_files: []
  ignored_paths:
    - .DS_Store
    - .env
    - .venv/
    - node_modules/

agent_instructions:
  authority_order:
    - validators and CI
    - <project-slug>-AGENTS.md
    - project.yml
    - docs/governance/
    - <project-slug>-README.md
```

The implementation should validate this file during `scaffold doctor` and in the
generated GitHub repo-hygiene workflow.

## Root Instruction Files

Generate these files for new projects:

- `<project-slug>-AGENTS.md`: canonical cross-agent instructions.
- `<project-slug>-CLAUDE.md`: points Claude sessions to the canonical
  project instructions and project-specific notes.
- `<project-slug>-WARP.md`: points Warp sessions to the canonical project
  instructions.
- `<project-slug>-GEMINI.md`: points Gemini sessions to the canonical project
  instructions.

`<project-slug>-AGENTS.md` must include:

- project identity;
- authority order;
- session startup instructions;
- verification command;
- editing rules;
- passoff rules;
- secrets rules;
- project-specific folder map.

It must not include secrets, local machine credentials, or stale absolute paths
except the project root path when useful.

## Passoff Requirements

Every scaffolded repo should include:

```text
docs/passoffs/
```

The README or governance docs must state:

- passoffs live in `docs/passoffs/`;
- filenames use `yyyy-MM-dd-HH:mm-passoff-file.md`;
- required sections are `Summary`, `Files changed`, `Key decisions`, `Risks and
  open questions`, `State`, `Next actions`, and `Do not do`;
- commits and PRs are not automatic unless the user explicitly asks.

Do not create a passoff during `scaffold new` unless the user asks for an
initial handoff.

## Git Behavior

`scaffold new` should:

1. Create the project directory.
2. Render templates.
3. Run local validation.
4. Run `git init -b main`.
5. Add `.gitignore`.
6. Stop and show `git status`.
7. Ask before the first commit.
8. Ask before creating the GitHub repository.
9. If approved, run `gh repo create`.
10. Add `origin`.
11. Ask before pushing.

`scaffold retrofit` should:

1. Detect whether the target is inside a Git repo.
2. If no Git repo exists, classify the folder and ask whether to initialize.
3. If a Git repo exists, read `git status --short`.
4. Refuse to overwrite conflicting files without a backup or explicit approval.
5. Print planned additions and edits.
6. Add missing governance files.
7. Add `.github` wrappers.
8. Run validation.
9. Stop at `git status`.

Never run:

```bash
git reset --hard
git checkout -- .
git push --force
git commit --no-verify
```

## GitHub Design

Use centralized reusable workflows with thin project wrappers.

Preferred central repository:

```text
klappe-pm/scaffolding
```

Preferred organization/community repository:

```text
klappe-pm/.github
```

The `.github` repository can hold default community health files and workflow
templates. The `scaffolding` repository should hold the reusable workflows,
templates, validation scripts, and CLI implementation. This keeps project
initiation logic and project governance defaults in one reusable repo.

Each scaffolded project should have local wrappers like:

```yaml
name: Repo Hygiene

on:
  pull_request:
  push:
    branches: [main]

jobs:
  hygiene:
    uses: klappe-pm/scaffolding/.github/workflows/repo-hygiene.yml@v1
    with:
      config_path: project.yml
```

And:

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

jobs:
  ci:
    uses: klappe-pm/scaffolding/.github/workflows/ci.yml@v1
    with:
      config_path: project.yml
```

Project-specific overrides must be expressed in `project.yml`, not by copying
large workflow bodies into each repo.

## Central Reusable Workflows

The `klappe-pm/scaffolding` repo should expose:

- `repo-hygiene.yml`: validates root docs, passoff folder, project.yml,
  `.gitignore`, and untracked generated-file policy.
- `ci.yml`: dispatches by `project_type`.
- `python-ci.yml`: Python install, lint, tests.
- `node-ci.yml`: Node install, lint, tests.
- `docs-ci.yml`: markdown/link/path checks.
- `passoff-check.yml`: validates passoff naming and required headings.
- `secrets-scan.yml`: basic secret scanning and forbidden local-file checks.

First implementation can include only local wrapper templates and leave the
central reusable workflow implementation as a task, but it must document that
wrappers will fail until the matching workflows exist in `klappe-pm/scaffolding`.

## Audit Mode

`scaffold audit /Users/kevinlappe/Projects` should recursively classify folders.

The audit mode must be at least as complete as
`specs-projects-folder-purpose-audit.json`: every project-owned folder and subfolder
must receive a classification and purpose note. Generated/dependency/internal
roots may be pruned from recursive purpose analysis, but they must still be
listed with the reason they were pruned.

Classification values:

- `git-repo`
- `nested-git-repo`
- `project-candidate`
- `vault`
- `archive`
- `inbox`
- `data-only`
- `empty`
- `ignore`

Signals:

- `.git` means `git-repo`.
- `README.md`, `package.json`, `pyproject.toml`, `Makefile`, `docs/`,
  `scripts/`, or `.github/` imply `project-candidate` when no Git repo exists.
- `.obsidian/` implies `vault` unless there is strong code/project structure.
- `z-archive/` implies `archive`.
- `.tmp`, `.trash`, `.DS_Store-only`, and empty folders imply `ignore` or
  `empty`.

Audit output should include:

```text
path
depth
classification
purpose
git_status
remote
default_branch
missing_files
recommended_action
notes
marker_files
readme_or_instruction_evidence
```

Produce both human-readable Markdown and machine-readable JSON:

```text
reports/projects-audit.md
reports/projects-audit.json
```

Do not create those reports unless the user runs a future explicit
`--write-report` mode or confirms during an interactive session.

## Initial Retrofit Task List From Audit

Seed the audit report with these known findings when detected:

- `/Users/kevinlappe/Projects/scaffolding`: make this the canonical reusable
  project initiation repo; initialize Git at the parent level and connect it to
  `https://github.com/klappe-pm/scaffolding` after explicit user approval.
- `/Users/kevinlappe/Projects/scaffolding/github-config`: nested legacy
  Git repo; review and either merge its useful content into the parent repo or
  archive it.
- `/Users/kevinlappe/Projects/agents`: project candidate; has README, Makefile,
  and Python project signals; needs Git decision.
- `/Users/kevinlappe/Projects/paddle-cf`: project candidate; needs Git decision.
- `/Users/kevinlappe/Projects/money-manager`: Git exists, but missing root
  instruction files and passoff folder; remote may not match project name.
- `/Users/kevinlappe/Projects/average-intelligence/website`: nested Git repo
  without remote or root instructions; decide separate repo vs parent subfolder.
- `/Users/kevinlappe/Projects/claude-config`: strong governance, missing
  `.github` wrappers.
- `/Users/kevinlappe/Projects/skills-main`: strong governance, missing `.github`
  wrappers.
- `/Users/kevinlappe/Projects/average-intelligence`: strong content structure,
  missing `.github` wrappers.
- `/Users/kevinlappe/Projects/claude-automation`: passoff structure exists,
  missing `.github` wrappers.

Use `specs-projects-git-history-structure-audit.md` as the source for repo-level
priorities:

- `claude-config` and `skills-main` are the strongest governance references:
  both have root multi-agent instructions, generated indexes, passoffs, scripts,
  tests, schemas, and high commit volume.
- `average-intelligence` is the strongest content/product reference: it uses
  `brand/`, `content/`, `docs/specs/`, `docs/strategy/`, `docs/ops/`, scripts,
  and passoffs.
- `claude-automation` is the cleanest small passoff/spec reference.
- `Lattice Lock` is the strongest `.github` reference, but only as a source for
  reusable-workflow patterns, not as a default template.
- `money-manager`, `average-intelligence/website`, and several vault/archive
  projects show why retrofit mode must classify before mutating.

## Template Requirements

Keep templates under:

```text
templates/
  base/
  github/
  project-types/
    python/
    node/
    content/
    agent-config/
    vault/
    mixed/
  commands/
  skills/
```

Templates should use simple placeholders:

```text
{{ project_name }}
{{ project_slug }}
{{ owner }}
{{ project_type }}
{{ default_branch }}
{{ verification_command }}
```

Avoid adding a template engine dependency in the first version unless needed.
Python standard-library replacement is acceptable if all placeholders are
validated before rendering.

Templates must include provenance comments or metadata that identify which
existing project pattern informed them. For example:

```yaml
source_patterns:
  - claude-config: root multi-agent instruction surface
  - skills-main: validation scripts and generated indexes
  - average-intelligence: content/product folder family
```

Do not include those provenance notes in user-facing generated files unless they
are useful to future maintainers. The provenance can live in template metadata.

## Safety Rules For The Implementing Agent

Before editing:

1. Read the current file if it exists.
2. Check whether the target path is in a Git repo.
3. Check `git status --short` for repos before retrofit edits.
4. Do not overwrite user changes.
5. Do not move or delete nested repos without explicit approval.

When writing:

1. Prefer adding new files over rewriting existing files.
2. If a file exists, create a clear patch and preserve local content.
3. Never write secrets.
4. Keep all generated content ASCII unless the existing file uses Unicode.

Before claiming done:

1. Run `scaffold doctor` once implemented.
2. Run the generated project verification command.
3. Show the exact files created or changed.
4. Show any commands that were skipped because they need user approval.

## Suggested Implementation Steps

1. Initialize `/Users/kevinlappe/Projects/scaffolding` as the parent Git repo
   and connect it to `https://github.com/klappe-pm/scaffolding` only after
   explicit user approval.
2. Read the audit artifacts:

   ```text
   specs/specs-projects-folder-purpose-audit.md
   specs/specs-projects-git-history-structure-audit.md
   ```

   Extract the actual observed folder families before finalizing templates.
3. Add this structure:

   ```text
   scaffold/
     __init__.py
     scaffold_cli.py
     scaffold_audit.py
     scaffold_render.py
     scaffold_git_ops.py
     scaffold_github_ops.py
     scaffold_doctor.py
     scaffold_skills.py
     scaffold_commands.py
   templates/
   commands/
     commands-scaffold-new.md
     commands-scaffold-audit.md
     commands-scaffold-retrofit.md
     commands-scaffold-github-bootstrap.md
     commands-scaffold-doctor.md
     commands-scaffold-passoff.md
   skills/
     project-folder-auditor/
     project-scaffold-planner/
     github-governance-bootstrapper/
     project-instruction-author/
     scaffold-retrofit-reviewer/
   tests/
   specs/
   scaffolding-README.md
   scaffolding-AGENTS.md
   project.yml
   .github/
     workflows/
       repo-hygiene.yml
       ci.yml
   ```

4. Implement `scaffold doctor`.
5. Implement template rendering.
6. Implement `scaffold new --dry-run`.
7. Implement `scaffold new` interactive mode.
8. Implement audit classification.
9. Implement retrofit dry-run.
10. Add GitHub creation support through `gh`.
11. Add `scaffold skills plan` and `scaffold commands plan`.
12. Add the command files under `commands/`.
13. Add the skill skeletons under `skills/`.
14. Add tests for path classification, template rendering, command manifests,
    skill manifests, and safety gates.

## Implementation Phases

### Phase 0: Evidence Lock

Goal: preserve the audit baseline.

Tasks:

1. Confirm the audit artifacts exist.
2. Add a short `specs/specs-README.md` explaining the relationship between the
   main spec and the two audit reports.
3. Do not implement templates until this phase is complete.

### Phase 1: Repo Foundation

Goal: make `scaffolding` a proper repo.

Tasks:

1. Initialize parent Git after approval.
2. Add `scaffolding-README.md`, `scaffolding-AGENTS.md`, `project.yml`,
   `.gitignore`, and `docs/passoffs/`.
3. Keep the nested `github-config` repo untouched until a separate
   migration decision is made.

### Phase 2: Read-Only CLI

Goal: build trust before mutation.

Tasks:

1. Implement `scaffold doctor`.
2. Implement `scaffold audit`.
3. Implement `scaffold templates list`.
4. Implement `scaffold skills plan`.
5. Implement `scaffold commands plan`.

Exit criteria:

- no command mutates project folders;
- output matches the saved audits on broad counts and classifications;
- tests cover folder classification and manifest parsing.

### Phase 3: Planning Commands

Goal: produce high-quality plans before writing files.

Tasks:

1. Implement `scaffold new --dry-run`.
2. Implement `scaffold retrofit --dry-run`.
3. Add command files that call those dry runs.
4. Add skill skeletons and reference files.

Exit criteria:

- dry-run output is complete enough for user approval;
- retrofit plans separate additive changes from conflicts.

### Phase 4: Local Mutation

Goal: create and retrofit local projects without GitHub side effects.

Tasks:

1. Implement `scaffold new --apply --no-github`.
2. Implement additive retrofit apply mode.
3. Run generated verification commands.

Exit criteria:

- no GitHub commands run;
- no commits are created automatically;
- generated projects pass `./scripts/verify.sh`.

### Phase 5: GitHub Bootstrap

Goal: safely create remotes and workflow wrappers.

Tasks:

1. Implement `scaffold github status`.
2. Implement `scaffold github bootstrap`.
3. Add reusable workflows in `.github/workflows/`.
4. Add thin wrapper templates.

Exit criteria:

- external GitHub mutations are plan-backed and visible before execution;
- workflow-scope blockers are surfaced before writes;
- no merge path bypasses required checks, branch protection, or unresolved
  review threads;
- no force-push path exists without explicit user approval.

## Acceptance Criteria

The work is complete when:

- `scaffold new --dry-run` prints a complete plan for a new project.
- `scaffold new` can create a local project with the standard structure.
- `scaffold audit /Users/kevinlappe/Projects` can classify existing folders
  without mutating anything and produces coverage comparable to the current
  folder-purpose audit.
- `scaffold retrofit <repo>` can identify missing governance files and print a
  patch plan without overwriting files.
- Generated repos include `project.yml`, root instruction files, `docs/passoffs`,
  `commands/`, `skills/`, and thin `.github` workflow wrappers.
- GitHub creation is available but gated behind confirmation.
- The implementation has tests for the core behavior.
- The README explains how to install and run `scaffold`.
- The implementation docs explain which existing projects informed each default
  folder family and GitHub governance default.
- `scaffold commands plan` lists all command files, their backing CLI command,
  and required approval gates.
- `scaffold skills plan` lists all project skills, trigger descriptions,
  bundled resources, and implementation status.
- The skill skeletons validate as well-formed Codex skills once created.

## Open Questions

- Which content from the nested `github-config` repo should be promoted
  into `/Users/kevinlappe/Projects/scaffolding`, and which content should be
  archived as legacy setup material?
- Should `klappe-pm/scaffolding` publish versioned workflow tags such as `v1`,
  or should consuming repos pin to full commit SHAs until the framework
  stabilizes?
- Should default projects be private unless overridden? This spec assumes yes.
- Should `scaffold new` create an initial passoff? This spec assumes no.
- Should dirty existing repos be refused by default during retrofit? This spec
  assumes yes unless the planned changes are purely additive and confirmed.
