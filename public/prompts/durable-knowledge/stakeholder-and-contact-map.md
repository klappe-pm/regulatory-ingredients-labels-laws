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
use-case: map-stakeholders-and-contacts
visibility: private
---

# stakeholder-and-contact-map

## description

Maps who the specialist interacts with and how each connects to them, as durable context for Copilot Memory or a private declarative agent's knowledge.

## when-to-use

Once, when first setting up durable context, and again whenever stakeholders or interaction patterns change materially.

## what-to-use-for

Turning a contact list, roles, and interaction cadence into a structured contact map with an install footer.

## required-inputs

- Contact list
- Roles
- Interaction cadence

## expected-outputs

- Contact map (who, role, connection to the specialist, cadence, channel)
- Install footer naming the owning Copilot layer and load steps

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: durable-knowledge`, `sub-category: relationships`, `date-created`/`date-revised` set to the run date, `type: contact-map`, `status: DONE`, `aliases: []`, `tags: [durable-knowledge, relationships]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: stakeholder-contact-map`, `visibility: private`.

File name: `stakeholder-contact-map-<yyyy-MM-dd>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: build a stakeholder and contact map from a contact list, roles, and interaction cadence.

Method:
1. Read the contact list, roles, and interaction cadence I provide below.
2. For each contact, produce a row: name, role, how they connect to me (e.g. "reviews my label claims," "owns formula changes," "external co-packer contact"), cadence (how often we interact), and channel (email, meetings, Teams, etc.).
3. Group contacts by function if a natural grouping emerges (e.g. internal regulatory/legal, R&D/formulation, marketing, external co-packer/supplier).
4. Do not invent a contact, role, or cadence not present in the inputs.
5. End with an install footer: state this map is best suited to Copilot Memory (for a small number of key contacts) or a private declarative agent's knowledge (for a larger, structured map), built via Agent Builder at m365.cloud.microsoft/chat, and note that sharing the agent beyond the specialist is admin-gated. Include a one-line verification step: ask Copilot who a specific contact is and confirm it reflects the installed map.

Source of truth: the contact list, roles, and interaction cadence I provide are the only sources.

This is durable context for the specialist to review and install themselves.

Do not fabricate a contact, connection, or cadence not present in the inputs.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste contact list here]

[Paste roles here]

[Paste interaction cadence here]
```

## guardrails

Human-in-the-loop: the specialist reviews and installs this map themselves. Never invents a contact or relationship not present in the source inputs.

Related: [[personalization-install-router]] (copilot-configuration/), [[team-roles-and-responsibilities]], [[communication-style-profile]].
