---
domain: regulatory-ingredients-labels-laws
category: copilot-configuration
sub-category: configuration
types:
  - reference
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: reference-copilot-layers
visibility: public
aliases:
  - agent builder grounding
  - copilot layers
  - copilot memory setup
  - copilot pages vs notebook
  - custom instructions vs memory
  - microsoft 365 copilot settings
  - office scripts and power automate
  - where to install copilot instructions
  - which copilot layer owns this
tags:
  - configuration
  - copilot-configuration
  - regulatory-labeling
---

# copilot-layering-reference

Microsoft 365 has no single instructions file. It is a stack of per-surface stores, each settable by a non-admin and each independently gated or disabled by tenant policy. This note is a reference map, not a settled product fact sheet: Copilot capability names, availability, and gating change, and the specialist must verify every row below against their own tenant and build before relying on it.

## layering-map

| concern | owning layer | where a non-admin sets it | caveats |
| --- | --- | --- | --- |
| behavioral rules (voice, formatting, no em dashes) | Custom Instructions | Copilot Chat settings, Personalization pane; the feature name and pane location vary by tenant and build, so look for a personalization or instructions setting inside Copilot Chat settings rather than following a fixed click path | controls style not knowledge; propagation into inline Word/Excel/Outlook authoring is partial and rolling, do not assume it governs an inline draft-with-Copilot action in Word |
| auto-learned facts and preferences | Copilot Memory | seed conversationally by telling Copilot "Remember that ..." in chat; prune entries in the same Personalization pane | the pane is for reviewing and deleting entries, not for typing new ones |
| spreadsheet file conventions | Excel personalization and workbook rules | Copilot in Excel | added June 2026 per this reference; personalization spans web, Mac, Windows; workbook rules were Insiders preview on Windows and Mac, confirm GA before depending on rules traveling with a file |
| scoped task and domain context plus grounding | private declarative agent (Agent Builder) | m365.cloud.microsoft/chat, New agent (conversational or Configure tab) | instructions-only grounded on public sites is free on plain Copilot Chat; pointing it at SharePoint or Graph content is metered and off by default; the agent is private until shared; sharing with named individuals is self-service, publishing org-wide into the shared catalog is admin-gated; ownership is non-transferable, treat it as personal infrastructure; anything in the agent's instructions is exposed to every future share recipient |
| notebook-scoped context | Copilot Notebook instructions | inside the Notebook, look for a Copilot instructions or settings pane; the feature name and pane location vary by tenant and build, verify the field exists in your build before routing here | requires a license plus a SharePoint or OneDrive service plan |
| collaborative working content | Copilot Pages | Copilot Chat, create a page from a response; pages live in your OneDrive and can be shared for co-editing | collaborative persistence, not instruction persistence: content on a page does not steer future Copilot answers unless you re-attach or reference it |
| site-scoped grounding on existing documents | SharePoint agent | on a SharePoint site, create an agent scoped to the site or to selected files (requires edit rights on the site) | grounding without Agent Builder; inherits the site's existing permissions; availability is license- and tenant-gated |
| durable reference content Copilot can be pointed at | a file in OneDrive or SharePoint | save the artifact as a file in OneDrive or SharePoint, then attach it in chat or scope an agent or Notebook to it | the simplest layer with no admin gate; attaching manually grounds one conversation only, nothing persists between chats unless an agent, Notebook, or SharePoint agent points at the file |
| executable logic | Office Scripts (TypeScript) invoked by Power Automate | Excel, Automate tab, browser Code Editor | closest thing to real scripting without a terminal; VBA is usually locked in a managed tenant, do not architect around it |

## recommended-layering

One owner per concern: Custom Instructions own behavior; Excel workbook rules own file conventions; a private declarative agent owns scoped context and grounding; Office Scripts own executable logic. Do not restate the same rule across two layers, since it will drift; if a rule needs to move, move it, do not copy it.

## verify-what-is-enabled-before-building-on-it

Everything in the table above is author-side; execution is gated by tenant Integrated Apps controls, DLP connector policies, Cloud Policy, add-in blocking, and macro policy. Check these before depending on a layer:

- Personalization pane: are Custom Instructions and Memory on for this account.
- New agent option: is Agent Builder enabled for this tenant.
- Excel Automate tab: is Office Scripts available.
- make.powerautomate.com: are personal flows and the connectors a script needs actually permitted.

You cannot check tenant policies yourself: if a surface listed here is missing from your build, ask your IT admin whether it is disabled by policy before concluding it does not exist.

Build on whatever is enabled, not on the full list above. A capability documented here that turns out disabled in the specialist's tenant is not a defect in this reference, it is exactly what the verification checklist exists to catch.

## maintenance

Replace, do not duplicate. When a durable-knowledge artifact is revised, update or remove the entry already installed in its owning layer instead of adding a second copy: edit or delete the text in the Custom Instructions pane; delete the Memory entry in the Personalization pane and re-seed conversationally if needed; edit the private agent's instructions in Agent Builder, or delete the agent; replace the stored file for file-, Notebook-, or SharePoint-agent-grounded content; edit or delete the Office Script in the Automate tab. After any change, rerun the verification step from the install-routing output to confirm the old entry is gone and the new one took effect.

## how-this-is-used

[[personalization-install-router]] takes a durable-knowledge artifact (see the durable-knowledge prompts), the list of enabled surfaces, and this reference attached to the chat, and returns the single owning layer, the click-path or pane description, the cost or admin gate to expect, and a verification step, grounded only in this map.
