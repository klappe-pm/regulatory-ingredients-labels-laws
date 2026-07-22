---
domain: regulatory-ingredients-labels-laws
category: durable-knowledge
sub-category: relationships
types:
  - prompt
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: record-team-roles-and-responsibilities
visibility: private
aliases:
  - escalation paths
  - raci for labeling
  - responsible accountable consulted informed
  - team ownership map
  - team roles and responsibilities
  - team roster for copilot
  - who approves label changes
  - who owns what
tags:
  - durable-knowledge
  - regulatory-labeling
  - relationships
---

# team-roles-and-responsibilities

## prompt-summary

Records team roles, ownership, and escalation paths as durable context for a private declarative agent's instructions or knowledge. It turns a team roster and ownership information into a RACI-style record (responsible, accountable, consulted, informed, per labeling function) with an escalation path for each function. Reach for it once when setting up durable team context, and again after a team or ownership change.

## use-cases

- First-time setup of durable team context for a private declarative agent.
- A team or ownership change (someone joins, leaves, or picks up a new function) and the record needs refreshing.
- You need a RACI-style map of who is responsible, accountable, consulted, and informed for each labeling function (formulation, regulatory/legal, marketing, QA, prepress/print, market surveillance).
- You need documented escalation paths: who to escalate to first and who the final decision-maker is per function.
- You are routing this artifact to its owning Copilot layer via [[personalization-install-router]].

## expected-outputs

- Roles plus RACI-style ownership (responsible, accountable, consulted, informed, per function)
- Escalation paths
- Install footer naming the owning Copilot layer and load steps

## prompt

```
You are running inside Microsoft 365 Copilot Chat. Your single task: record team roles, ownership, and escalation paths from a team roster and ownership information.

You should have these inputs: (1) team roster, (2) ownership information. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Privacy rule: business role information only; no personal phone numbers or home emails, no performance or personality judgments about colleagues (record who holds a role and its documented escalation route, never an assessment of anyone's capability), and prefer role labels over named individuals where the role suffices.

Method:
1. Read the team roster and ownership information provided below.
2. For each function relevant to labeling (formulation, regulatory/legal, marketing, QA, prepress/print, market surveillance), identify who is Responsible, Accountable, Consulted, and Informed, per the RACI model, using only roles present in the roster.
3. Build an escalation path for each function: who to escalate to first, and who is the final decision-maker, using only relationships stated or clearly implied by the roster and ownership data.
4. Do not invent a role, an ownership assignment, or an escalation path not supported by the inputs; mark a function as "owner not specified" if the roster does not name one.
5. End with an install footer: state this record is best suited to a private declarative agent's instructions or knowledge, built via Agent Builder at m365.cloud.microsoft/chat (Configure tab for instructions, or attached documents/sites for knowledge; verify against your own tenant, since menus and rollout vary), and note that pointing the agent at SharePoint/Graph content is metered and off by default, so a plain-text instructions version is the lower-friction starting point. Warn that anything installed into an agent is visible to every future share recipient, so this record belongs only in an agent that will stay private; note the saved markdown record is the durable source and the agent is a replaceable rendering of it. Include a one-line verification step: ask the agent who owns a specific function and confirm it matches this record.

Source of truth: the team roster and ownership information provided below are the only sources.

This is durable context for the specialist to review and install themselves.

Do not fabricate a role, an ownership assignment, or an escalation path not present in the inputs.

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: durable-knowledge
sub-category: relationships
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: team-roles-record
status: REVIEW
aliases: []
tags:
  - durable-knowledge
  - relationships
topic: beverage-label-compliance
use-case: team-roles-and-responsibilities
visibility: private
---
2. An H1 equal to the output file name without .md: team-roles-and-responsibilities-record-[TODAY as yyyy-MM-dd]
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review by the regulatory labeling specialist before installing into any Copilot layer.

[Paste team roster here]

[Paste ownership information here]
```

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have the inputs ready: team roster and ownership information (who owns what, at least at a summary level). Attach files with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint); paste text directly when a file cannot be attached.
3. Copy the entire prompt block above, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `team-roles-and-responsibilities-record-<yyyy-MM-dd>.md` (kebab-case, H1 equal to the file-name stem; the `-record` suffix keeps outputs from colliding with this prompt file's stem) in `projects/regulatory-labeling/` in this vault, or your team's equivalent OneDrive/SharePoint folder.
5. Review the output yourself, verify escalation paths against an official org source, then install it by hand per its install footer. Nothing installs automatically and nothing is final until a person signs off.

## guardrails

Human-in-the-loop: the specialist reviews and installs this record themselves. Any function with no named owner is marked as such, never filled in with a guess. Privacy: the record describes roles and documented escalation routes only, never capability or performance judgments about colleagues; confirm against Talking Rain's Copilot and data-handling policy before installing. Shared-agent exposure: anything installed into a declarative agent is visible to every future share recipient, so install this only into an agent that stays private. Continuity: agent ownership is non-transferable, so treat the saved markdown record as the durable source and the agent as a replaceable rendering.

Related: [[personalization-install-router]] (copilot-configuration/), [[stakeholder-and-contact-map]], [[workstream-inventory]].
