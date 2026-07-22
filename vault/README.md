---
domain: harness
category: containers
sub-category: vault-scaffold
date-created: 2026-07-08
date-revised: 2026-07-08
type: reference
status: active
aliases:
  - environment vault scaffold
tags:
  - containers
  - obsidian
  - vault
---

# Environment Vault

Vault scaffold placeholder baked into the harness base image at `/opt/harness/vault-scaffold` (F2.1.1). `harness env up` (E2.3) copies it into the environment workspace; the host Obsidian app opens it through the existing workspace mount. Obsidian is a host application: the container packages the vault, never the app.

The E2.4 generators write into `generated/`: `gen-access-dashboard.py` renders the fleet `generated/ACCESS-DASHBOARD.md` plus a per-environment note under `generated/access/<env-id>.md`, and `gen-fleet-health.py --vault-dir` renders the `alerts-v1` dashboard-sink log at `generated/ALERTS.md`. Every note under `generated/` is a regenerated read model: deleting all of them loses nothing, and hand edits are bugs.

Single-writer rule: close Obsidian on this vault while its generators run. An open Obsidian buffer flushes its in-memory copy over on-disk edits and silently reverts generator writes.
