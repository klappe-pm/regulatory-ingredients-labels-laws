---
type: reference
status: active
tags:
  - access-dashboard
  - environments
env-id: local-dev
---

<!-- GENERATED FILE. Do not hand-edit. Regenerate with scripts/gen/gen-access-dashboard.py from the environments/*.access.json configs. Hand-edits are a bug and are overwritten on the next run; edit the access config instead. -->

# Access dashboard: local-dev

What `local-dev` (project `regulatory-ingredients-labels-laws`) can touch, rendered from its `access-v1` config. GENERATED FILE. Do not hand-edit. Regenerate with scripts/gen/gen-access-dashboard.py from the environments/*.access.json configs. Hand-edits are a bug and are overwritten on the next run; edit the access config instead.

## Workspace mount

| path | mode |
|---|---|
| /workspace/regulatory-ingredients-labels-laws | rw |

## Shared-store mounts

| store | path | mode | why |
|---|---|---|---|
| claude-config | /mnt/claude-config | ro | global rules, skills, and guard hooks load in every Claude session |

## Network
> [!info] Network tier: allowlist
> Egress is restricted to the declared hosts below. Declared only: the posture is documented, not yet mechanically enforced. This is the honest committed default, not an alarm.
>
> - `github.com`
> - `api.github.com`
> - `www.federalregister.gov`
> - `www.ecfr.gov`
> - `www.fda.gov`
> - `www.fns.usda.gov`
> - `leginfo.legislature.ca.gov`
> - `oehha.ca.gov`
> - `www.ncsl.org`
> - `www.canada.ca`
> - `gazette.gc.ca`
> - `www.dof.gob.mx`

## Secrets namespaces

- `github`

## Capabilities

| capability | granted |
|---|---|
| docker-socket | no |
| privileged | no |
| host-git-config-rw | no |

## Widening history

Last reviewed: 2026-07-09

No access widening recorded. Least-privilege default holds.
