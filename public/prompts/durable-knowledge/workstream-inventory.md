---
domain: regulatory-ingredients-labels-laws
category: durable-knowledge
sub-category: workstreams
types:
  - prompt
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: inventory-workstreams
visibility: private
aliases:
  - active workstreams
  - confidential workstreams flag
  - copilot memory what i do
  - current projects list
  - list my current projects
  - project status roundup
  - what am i working on
  - workstream inventory
tags:
  - durable-knowledge
  - regulatory-labeling
  - workstreams
---

# workstream-inventory

## prompt-summary

Inventories what the specialist is currently working on as durable context for a private declarative agent's knowledge or Copilot Memory. It turns a list of current projects and workstreams into structured records (name, goal, status, stakeholders, key artifacts, confidentiality flag) plus a review-by date so the context never goes stale. Reach for it on a stated cadence (monthly, or alongside the weekly status report, whichever comes first) and whenever workstreams change enough that Copilot's sense of "what am I working on" would be wrong.

## use-cases

- Monthly refresh of durable "what am I working on" context, or alongside the weekly status report, whichever comes first.
- Workstreams change enough that Copilot's context would be stale and needs replacing.
- You want each project recorded with goal, status (using this project's status vocabulary), stakeholders, and key artifacts.
- You need unreleased SKU names, claims strategy, or launch timing flagged as confidential so they go only into a private, never-shared layer.
- You are routing this artifact to its owning Copilot layer via [[personalization-install-router]], or pairing it with the [[weekly-status-report]] companion artifact.

## expected-outputs

- Workstream records (name, goal, status, stakeholders, artifacts, confidentiality flag)
- Review-by date for the whole inventory
- Install footer naming the owning Copilot layer, load steps, and the remove-the-prior-version step

## prompt

```
You are running inside Microsoft 365 Copilot Chat. Your single task: inventory the specialist's current workstreams from a list of current projects and workstreams.

You should have this input: (1) the list of current projects and workstreams. If it is missing or unreadable, stop and say so. Never proceed from memory or invent content for a missing input.

Privacy rule: business role information only; no personal phone numbers or home emails, no performance or personality judgments about colleagues, and prefer role labels over named individuals where the role suffices.

Confidentiality rule: unreleased SKU names, claims strategy, and launch timing stay out of any shareable layer; flag each workstream containing them as confidential so the specialist installs it only into a private, never-shared layer.

Method:
1. Read the current projects and workstreams provided below.
2. For each one, produce a record: name, goal (what it is trying to accomplish), status (using this project's status vocabulary: NEW, DRAFT, INPRG, REVIEW, DONE, ARCHIVED, plus a blocked flag if applicable), stakeholders (who else is involved), key artifacts (documents, SKUs, or files tied to it), and a confidential flag per the confidentiality rule.
3. Do not invent a workstream, a status, or a stakeholder not present in the inputs; if status is unclear from the input, mark it "unspecified" rather than guessing.
4. Add a review-by date for the whole inventory: one month from today, or the next weekly status report if sooner.
5. End with an install footer: state this inventory is best suited to a private declarative agent's knowledge (for a fuller record with attached documents) or Copilot Memory (for a short list of currently-active items), and note the tradeoff, a declarative agent needs Agent Builder setup at m365.cloud.microsoft/chat, while Memory is lower-friction but has less structure. Memory entries are seeded by telling Copilot "Remember that <fact>" in chat, one item per message, then verified and pruned in the Personalization pane (the pane itself is view and delete only; verify against your own tenant, since menus and rollout vary). State the remove-prior-version step: before installing, delete the superseded inventory's Memory entries in the Personalization pane or replace the agent's knowledge file, so stale context never persists. Include a one-line verification step: ask Copilot what you are currently working on and confirm the answer matches this inventory.

Source of truth: the current projects and workstreams provided below are the only sources.

This is durable context for the specialist to review and install themselves, and it must be refreshed by the review-by date since workstreams change.

Do not fabricate a workstream, a status, or a stakeholder not present in the inputs.

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: durable-knowledge
sub-category: workstreams
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: workstream-record
status: REVIEW
aliases: []
tags:
  - durable-knowledge
  - workstreams
topic: beverage-label-compliance
use-case: workstream-inventory
visibility: private
---
2. An H1 equal to the output file name without .md: workstream-inventory-record-[TODAY as yyyy-MM-dd]
3. The body specified in the method above, including the review-by date.
4. This exact final line:
UNVERIFIED DRAFT - requires review by the regulatory labeling specialist before installing into any Copilot layer.

[Paste current projects and workstreams here]
```

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have the input ready: your list of current projects and workstreams. Attach files with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint); paste text directly when a file cannot be attached.
3. Copy the entire prompt block above, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `workstream-inventory-record-<yyyy-MM-dd>.md` (kebab-case, H1 equal to the file-name stem; the `-record` suffix keeps outputs from colliding with this prompt file's stem; the date stamp means re-runs never overwrite an earlier record) in `projects/regulatory-labeling/` in this vault, or your team's equivalent OneDrive/SharePoint folder.
5. Review the output yourself, remove the prior installed version, then install the new one per its install footer. Nothing installs automatically and nothing is final until a person signs off.

## guardrails

Human-in-the-loop: the specialist reviews and installs this inventory themselves, refreshes it by the review-by date (monthly or with the weekly status report, whichever comes first), and removes the prior installed version before installing the new one. Confidentiality: unreleased SKU names, claims strategy, and launch timing stay out of any shareable layer; confidential workstreams go only into a private, never-shared layer, per your organization's Copilot and data-handling policy.

Related: [[personalization-install-router]] (copilot-configuration/), [[weekly-status-report]] (market-and-reporting/, a natural companion artifact), [[team-roles-and-responsibilities]].
