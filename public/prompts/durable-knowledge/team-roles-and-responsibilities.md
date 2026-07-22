---
domain: regulatory-ingredients-labels-laws
category: durable-knowledge
sub-category: relationships
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - durable-knowledge
  - relationships
  - regulatory-labeling
topic: beverage-label-compliance
use-case: record-team-roles-and-responsibilities
visibility: private
---

# team-roles-and-responsibilities

## description

Records team roles, ownership, and escalation paths as durable context for a private declarative agent's instructions or knowledge.

## when-to-use

Once, when setting up durable team context, and again after a team or ownership change.

## what-to-use-for

Turning a team roster and ownership information into a structured roles-and-responsibilities record with RACI-style ownership and escalation paths.

## required-inputs

- Team roster
- Ownership (who owns what, at least at a summary level)

## expected-outputs

- Roles plus RACI-style ownership (responsible, accountable, consulted, informed, per function)
- Escalation paths
- Install footer naming the owning Copilot layer and load steps

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: durable-knowledge`, `sub-category: relationships`, `date-created`/`date-revised` set to the run date, `type: team-roles-record`, `status: DONE`, `aliases: []`, `tags: [durable-knowledge, relationships]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: team-roles-and-responsibilities`, `visibility: private`.

File name: `team-roles-and-responsibilities-<yyyy-MM-dd>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: record team roles, ownership, and escalation paths from a team roster and ownership information.

Method:
1. Read the team roster and ownership information I provide below.
2. For each function relevant to labeling (formulation, regulatory/legal, marketing, QA, prepress/print, market surveillance), identify who is Responsible, Accountable, Consulted, and Informed, per the RACI model, using only roles present in the roster.
3. Build an escalation path for each function: who to escalate to first, and who is the final decision-maker, using only relationships stated or clearly implied by the roster and ownership data.
4. Do not invent a role, an ownership assignment, or an escalation path not supported by the inputs; mark a function as "owner not specified" if the roster does not name one.
5. End with an install footer: state this record is best suited to a private declarative agent's instructions or knowledge, built via Agent Builder at m365.cloud.microsoft/chat (Configure tab for instructions, or attached documents/sites for knowledge), and note that pointing the agent at SharePoint/Graph content is metered and off by default, so a plain-text instructions version is the lower-friction starting point. Include a one-line verification step: ask the agent who owns a specific function and confirm it matches this record.

Source of truth: the team roster and ownership information I provide are the only sources.

This is durable context for the specialist to review and install themselves.

Do not fabricate a role, an ownership assignment, or an escalation path not present in the inputs.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste team roster here]

[Paste ownership information here]
```

## guardrails

Human-in-the-loop: the specialist reviews and installs this record themselves. Any function with no named owner is marked as such, never filled in with a guess.

Related: [[personalization-install-router]] (copilot-configuration/), [[stakeholder-and-contact-map]], [[workstream-inventory]].
