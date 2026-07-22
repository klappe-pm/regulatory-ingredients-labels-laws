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

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have the inputs ready: contact list, roles, and interaction cadence. Attach files with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint); paste text directly when a file cannot be attached. Strip personal phone numbers and home emails from the contact list before attaching it.
3. Copy the entire prompt-text block below, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `stakeholder-contact-map-record-<yyyy-MM-dd>.md` in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. Review the output yourself, then install it by hand per its install footer. Nothing installs automatically and nothing is final until a person signs off.

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: durable-knowledge`, `sub-category: relationships`, `date-created`/`date-revised` set to the run date, `type: contact-map`, `status: REVIEW`, `aliases: []`, `tags: [durable-knowledge, relationships]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: stakeholder-contact-map`, `visibility: private`.

File name: `stakeholder-contact-map-record-<yyyy-MM-dd>.md`, kebab-case, H1 equal to the file-name stem. The `-record` suffix keeps outputs from colliding with this prompt file's stem.

Saves to: `projects/regulatory-labeling/`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: build a stakeholder and contact map from a contact list, roles, and interaction cadence.

You should have these inputs: (1) contact list, (2) roles, (3) interaction cadence. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Privacy rule: business role information only; no personal phone numbers or home emails, no performance or personality judgments about colleagues, and prefer role labels over named individuals where the role suffices. If the supplied contact list contains personal phone numbers or home emails, omit them from the output.

Method:
1. Read the contact list, roles, and interaction cadence provided below.
2. For each contact, produce a row: name, role, how they connect to me (e.g. "reviews my label claims," "owns formula changes," "external co-packer contact"), cadence (how often we interact), and channel (email, meetings, Teams, etc.).
3. Group contacts by function if a natural grouping emerges (e.g. internal regulatory/legal, R&D/formulation, marketing, external co-packer/supplier).
4. Do not invent a contact, role, or cadence not present in the inputs.
5. End with an install footer: state this map is best suited to Copilot Memory (for a small number of key contacts) or a private declarative agent's knowledge (for a larger, structured map). Memory entries are seeded by telling Copilot "Remember that <fact>" in chat, one contact fact per message, then verified and pruned in the Personalization pane (the pane itself is view and delete only; verify against your own tenant, since menus and rollout vary). A private declarative agent is built via Agent Builder at m365.cloud.microsoft/chat; sharing the agent beyond the specialist is admin-gated, and anything installed into an agent is visible to every future share recipient, so keep this contact map out of any agent that might be shared. Include a one-line verification step: ask Copilot who a specific contact is and confirm it reflects the installed map.

Source of truth: the contact list, roles, and interaction cadence provided below are the only sources.

This is durable context for the specialist to review and install themselves.

Do not fabricate a contact, connection, or cadence not present in the inputs.

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: durable-knowledge
sub-category: relationships
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: contact-map
status: REVIEW
aliases: []
tags:
  - durable-knowledge
  - relationships
topic: beverage-label-compliance
use-case: stakeholder-contact-map
visibility: private
---
2. An H1 equal to the output file name without .md: stakeholder-contact-map-record-[TODAY as yyyy-MM-dd]
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review by the regulatory labeling specialist before installing into any Copilot layer.

[Paste contact list here]

[Paste roles here]

[Paste interaction cadence here]
```

## guardrails

Human-in-the-loop: the specialist reviews and installs this map themselves. Never invents a contact or relationship not present in the source inputs. Privacy: this map is personal data about colleagues; keep it to business role information (no personal phone numbers, home emails, or performance judgments), confirm against Talking Rain's Copilot and data-handling policy before installing, and remove departed contacts when re-running. Shared-agent exposure: anything installed into a declarative agent is visible to every future share recipient, so keep contact maps out of shareable agents.

Related: [[personalization-install-router]] (copilot-configuration/), [[team-roles-and-responsibilities]], [[communication-style-profile]].
