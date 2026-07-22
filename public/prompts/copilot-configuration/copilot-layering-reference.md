---
domain: regulatory-ingredients-labels-laws
category: copilot-configuration
sub-category: configuration
date-created: 2026-07-22
date-revised: 2026-07-22
type: reference
status: DONE
aliases: []
tags:
  - copilot-configuration
  - configuration
  - regulatory-labeling
topic: beverage-label-compliance
use-case: reference-copilot-layers
visibility: public
---

# copilot-layering-reference

Microsoft 365 has no single instructions file. It is a stack of per-surface stores, each settable by a non-admin and each independently gated or disabled by tenant policy. This note is a reference map, not a settled product fact sheet: Copilot capability names, availability, and gating change, and the specialist must verify every row below against their own tenant and build before relying on it.

## layering map

| concern | owning layer | where a non-admin sets it | caveats |
| --- | --- | --- | --- |
| behavioral rules (voice, formatting, no em dashes) | Custom Instructions | Copilot Chat, Settings and more, Chat settings, Personalization (toggle) | controls style not knowledge; propagation into inline Word/Excel/Outlook authoring is partial and rolling, do not assume it governs an inline draft-with-Copilot action in Word |
| auto-learned facts and preferences | Copilot Memory | same Personalization pane; seed and prune entries | |
| spreadsheet file conventions | Excel personalization and workbook rules | Copilot in Excel | added June 2026 per this reference; personalization spans web, Mac, Windows; workbook rules were Insiders preview on Windows and Mac, confirm GA before depending on rules traveling with a file |
| scoped task and domain context plus grounding | private declarative agent (Agent Builder) | m365.cloud.microsoft/chat, New agent (conversational or Configure tab) | instructions-only grounded on public sites is free on plain Copilot Chat; pointing it at SharePoint or Graph content is metered and off by default; the agent is private until shared, sharing is admin-gated, ownership is non-transferable, treat it as personal infrastructure |
| notebook-scoped context | Copilot Notebook instructions | Notebook pane, Copilot instructions | requires a license plus a SharePoint or OneDrive service plan |
| executable logic | Office Scripts (TypeScript) invoked by Power Automate | Excel, Automate tab, browser Code Editor | closest thing to real scripting without a terminal; VBA is usually locked in a managed tenant, do not architect around it |

## recommended layering

One owner per concern: Custom Instructions own behavior; Excel workbook rules own file conventions; a private declarative agent owns scoped context and grounding; Office Scripts own executable logic. Do not restate the same rule across two layers, since it will drift; if a rule needs to move, move it, do not copy it.

## verify what is enabled before building on it

Everything in the table above is author-side; execution is gated by tenant Integrated Apps controls, DLP connector policies, Cloud Policy, add-in blocking, and macro policy. Check these before depending on a layer:

- Personalization pane: are Custom Instructions and Memory on for this account.
- New agent option: is Agent Builder enabled for this tenant.
- Excel Automate tab: is Office Scripts available.
- make.powerautomate.com: are personal flows and the connectors a script needs actually permitted.

Build on whatever is enabled, not on the full list above. A capability documented here that turns out disabled in the specialist's tenant is not a defect in this reference, it is exactly what the verification checklist exists to catch.

## how this is used

[[personalization-install-router]] takes a durable-knowledge artifact (see [[durable-knowledge]]) and the list of enabled surfaces, and returns the single owning layer, the click-path, the cost or admin gate to expect, and a verification step, grounded in this map.

Up: [[configuration]], [[copilot-configuration]]
