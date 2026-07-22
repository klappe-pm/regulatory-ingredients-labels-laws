---
domain: regulatory-ingredients-labels-laws
category: durable-knowledge
sub-category: durable-knowledge
date-created: 2026-07-22
date-revised: 2026-07-22
type: index
status: DONE
aliases: []
tags:
  - durable-knowledge
  - regulatory-labeling
topic: beverage-label-compliance
use-case: browse-durable-knowledge-prompts
visibility: private
---

# durable-knowledge

Capturing the specialist's durable communication style, stakeholders, team roles, and current workstreams so Copilot can remember them across sessions instead of relearning them each time. Every prompt here ends with an install footer naming the owning Copilot layer and the exact steps to load it; see [[personalization-install-router]] for routing help and [[copilot-layering-reference]] for the underlying layer map.

## before-you-start

Everything in this category is personal or organizational data going into durable Copilot layers, so these rules apply to every prompt and every installed output:

- Business role information only: describe colleagues by role and business channel, never personal phone numbers or home emails.
- No performance or personality judgments about colleagues in any durable record.
- Prefer role labels (e.g. "QA lead") over named individuals where the role suffices.
- Confirm against Talking Rain's Copilot and data-handling policy before installing anything into a durable Copilot layer.
- Shared-agent exposure: anything installed into a declarative agent is visible to every future share recipient; keep contact maps and confidential workstream details (unreleased SKU names, claims strategy, launch timing) out of any agent that might be shared.

## prompts

- [[communication-style-profile]], the specialist's voice and formatting defaults as durable rules for Custom Instructions and Memory
- [[stakeholder-and-contact-map]], who the specialist works with, as durable context for Copilot Memory or a private declarative agent
- [[team-roles-and-responsibilities]], how the team is structured, with RACI-style ownership and escalation paths
- [[workstream-inventory]], what the specialist is currently working on, refreshed on a stated cadence

## workflow

1. Run [[communication-style-profile]] first; its style rules feed Custom Instructions and its facts feed Memory, and every drafting prompt in [[communication-email]] writes better once it is installed.
2. Run [[stakeholder-and-contact-map]] and [[team-roles-and-responsibilities]] next; their outputs ground drafts, summaries, and escalation reasoning from Memory or a private declarative agent.
3. Run [[workstream-inventory]] last, and re-run it monthly or alongside [[weekly-status-report]] (market-and-reporting/), whichever comes first.
4. Route each saved output through [[personalization-install-router]] (copilot-configuration/) to pick the owning layer for your tenant, then install it yourself following the output's install footer; nothing installs automatically.

## keeping-this-current

- Memory: seed facts by telling Copilot "Remember that <fact>" in chat; the Personalization pane is view and delete only, so prune superseded or departed-colleague entries there (verify against your own tenant, menus and rollout vary).
- Custom Instructions: edit the rules text in the Personalization pane whenever your style rules change materially.
- Declarative agent knowledge: replace the agent's instructions text or attached knowledge file with the new dated record; never stack versions.
- Re-run cadence: style, stakeholder, and team records whenever something changes materially; workstream inventory monthly or with the weekly status report. Always remove the prior installed version before installing the new one.

Up: [[regulatory-labeling]]

![[bases/durable-knowledge.base]]
