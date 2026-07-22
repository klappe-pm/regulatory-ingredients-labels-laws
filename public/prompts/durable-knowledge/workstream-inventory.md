---
domain: regulatory-ingredients-labels-laws
category: durable-knowledge
sub-category: workstreams
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - durable-knowledge
  - workstreams
  - regulatory-labeling
topic: beverage-label-compliance
use-case: inventory-workstreams
visibility: private
---

# workstream-inventory

## description

Inventories what the specialist is currently working on, as durable context for a private declarative agent's knowledge or Copilot Memory.

## when-to-use

Periodically (e.g. alongside the weekly status report) or whenever workstreams change enough that Copilot's context on "what am I working on" would be stale.

## what-to-use-for

Turning a list of current projects and workstreams into structured records with goal, status, stakeholders, and key artifacts, kept current as durable Copilot context.

## required-inputs

- Current projects and workstreams

## expected-outputs

- Workstream records (name, goal, status, stakeholders, artifacts)
- Install footer naming the owning Copilot layer and load steps

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: durable-knowledge`, `sub-category: workstreams`, `date-created`/`date-revised` set to the run date, `type: workstream-record`, `status: DONE`, `aliases: []`, `tags: [durable-knowledge, workstreams]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: workstream-inventory`, `visibility: private`.

File name: `workstream-inventory-<yyyy-MM-dd>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: inventory the specialist's current workstreams from a list of current projects and workstreams.

Method:
1. Read the current projects and workstreams I provide below.
2. For each one, produce a record: name, goal (what it is trying to accomplish), status (using this project's status vocabulary: NEW, DRAFT, INPRG, REVIEW, DONE, ARCHIVED, plus a blocked flag if applicable), stakeholders (who else is involved), and key artifacts (documents, SKUs, or files tied to it).
3. Do not invent a workstream, a status, or a stakeholder not present in the inputs; if status is unclear from the input, mark it "unspecified" rather than guessing.
4. End with an install footer: state this inventory is best suited to a private declarative agent's knowledge (for a fuller record with attached documents) or Copilot Memory (for a short list of currently-active items), and note the tradeoff, a declarative agent needs Agent Builder setup at m365.cloud.microsoft/chat, while Memory is lower-friction but has less structure. Include a one-line verification step: ask Copilot what you are currently working on and confirm the answer matches this inventory.

Source of truth: the current projects and workstreams I provide are the only sources.

This is durable context for the specialist to review and install themselves, and it should be refreshed periodically since workstreams change.

Do not fabricate a workstream, a status, or a stakeholder not present in the inputs.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste current projects and workstreams here]
```

## guardrails

Human-in-the-loop: the specialist reviews and installs this inventory themselves, and should refresh it as workstreams change rather than letting it go stale.

Related: [[personalization-install-router]] (copilot-configuration/), [[weekly-status-report]] (market-and-reporting/, a natural companion artifact), [[team-roles-and-responsibilities]].
