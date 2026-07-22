---
domain: regulatory-ingredients-labels-laws
category: copilot-configuration
sub-category: configuration
types:
  - prompt
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: route-durable-knowledge-artifact
visibility: public
aliases:
  - copilot click path
  - copilot install steps
  - custom instructions or memory or agent
  - install routing prompt
  - route durable knowledge
  - verify the setting took effect
  - where do i install this artifact
  - which copilot layer
  - which copilot surface owns this
tags:
  - configuration
  - copilot-configuration
  - regulatory-labeling
---

# personalization-install-router

## prompt-summary

Routes a durable-knowledge artifact (see the durable-knowledge prompts) to the single owning Microsoft 365 Copilot layer and returns exact installation steps, grounded only in [[copilot-layering-reference]]. Reach for it once a durable-knowledge prompt has produced an artifact and the specialist needs to know exactly where it belongs (Custom Instructions, Memory, an Agent Builder agent, Excel rules, a Notebook, a file, or Office Scripts) and how to put it there. It returns the owning layer, the click-path or pane description, the cost or admin gate to expect, and a verification step, and it recommends but never installs anything.

## use-cases

- A durable-knowledge prompt (such as [[communication-style-profile]] or [[workstream-inventory]]) has produced an artifact and you need the one layer that owns it plus the exact steps to install it.
- You have the list of which Copilot surfaces are actually enabled in the tenant and need the routing restricted to what is available, with a labeled fallback when the ideal layer is off.
- You want the click-path where the reference gives one, or a pane description to locate yourself where the location varies by tenant and build.
- You need to know the cost or admin gate to expect for a layer (free, metered, admin-gated, license-dependent) before committing to it.
- You need a verification step to confirm the installed setting actually took effect, and a replace-do-not-duplicate check against any prior copy.
- The artifact carries colleague personal data or confidential product information and you need the data-handling caution before it goes into Memory or shareable agent instructions.

## expected-outputs

- Owning layer
- Click-path steps or pane description
- Caveats
- Verification check

## prompt

```
You are running inside Microsoft 365 Copilot Chat. Your single task: route one durable-knowledge artifact to the correct Microsoft 365 Copilot layer and return exact installation steps for the specialist to perform themselves.

You should have these inputs: (1) the durable-knowledge artifact to be installed, attached or pasted below; (2) the list of Copilot surfaces enabled in the specialist's tenant; (3) the copilot-layering-reference file, attached to this chat, or its layer-map table pasted below. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Grounding rule: use only the attached copilot-layering-reference for layer names, click-paths, pane descriptions, costs, and gates. Never use product memory or your general knowledge of Microsoft 365 Copilot to supply a click-path, feature name, or gating rule that is not in the attached reference. Treat every row of the reference as reference-dated, not settled fact: the specialist must verify it against their own tenant and build before relying on it.

Method:
1. Read the artifact and classify what kind of durable knowledge it is: behavioral/style rule, discrete fact, spreadsheet file convention, scoped task or domain context, notebook-scoped context, collaborative working content, durable reference content, or executable logic.
2. Read the enabled-surfaces list.
3. Match the artifact type to its owning layer per the attached layer map, restricted to what is actually enabled; if the ideal layer is not enabled, recommend the best available alternative and say explicitly that it is a fallback, not the ideal fit.
4. Return the installation steps exactly as the attached reference gives them: a click-path where the reference gives one, or a pane description where the reference says the location varies by tenant and build, in which case tell the specialist to locate that pane in their own build rather than asserting a fixed menu path.
5. State the cost or admin gate to expect (free, metered, admin-gated, license-dependent), exactly as given in the attached reference.
6. Give one verification step: a specific question or action the specialist can take to confirm the installed setting actually took effect.
7. Replace, do not duplicate: if a version of this artifact may already be installed in a layer, instruct the specialist to update or remove the old entry first, never to add a second copy alongside it.
8. Never assert a capability is enabled without the specialist's confirmation; if the enabled-surfaces list does not cover a needed capability, say so and stop short of assuming it exists.

Data-classification guardrails:
- Reference the artifact by name only in your output; never quote or restate the artifact's content.
- If the artifact contains colleague personal data (names, contact details, roles) or confidential product information (formulas, unreleased claims), state that the specialist must check company data-handling policy before placing it in personal Copilot Memory or in agent instructions, and warn that anything placed in a shareable agent's instructions is exposed to every future share recipient.

This prompt recommends where to install the artifact; it never installs anything. The specialist performs every click-path themselves.

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: copilot-configuration
sub-category: configuration
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: install-routing
status: REVIEW
aliases: []
tags:
  - copilot-configuration
  - configuration
topic: beverage-label-compliance
use-case: personalization-install-routing
visibility: public
---
2. An H1 equal to the output file name without .md: install-routing-[artifact-slug]-[TODAY as yyyy-MM-dd]
3. The body specified in the method above: owning layer and why, installation steps (click-path or pane description), caveats (cost, admin gate, license, fallback status), the replace-do-not-duplicate note, the data-classification note when it applies, and the verification step.
4. This exact final line:
UNVERIFIED DRAFT - requires review by the regulatory labeling specialist; click-paths, feature names, and gates unconfirmed against the current tenant and build.

[Paste artifact here, or attach the artifact file]

Enabled Copilot surfaces: [list of enabled surfaces]

Layer-map table from copilot-layering-reference: [attach the file to this chat, or paste its layer-map table here]
```

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have these inputs ready: the durable-knowledge artifact to install, the list of which Copilot surfaces are enabled (from the verify-what-is-enabled checklist in [[copilot-layering-reference]]), and the copilot-layering-reference file itself. Attach the artifact and the reference with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint); paste the artifact text or the layer-map table directly when a file cannot be attached.
3. Copy the entire prompt block above, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `install-routing-<artifact-slug>-<yyyy-MM-dd>.md` (kebab-case, H1 equal to the file-name stem) and save it in `public/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder); this is the one public save path in the library. Apply the project frontmatter convention in canonical key order (`domain`, `category`, `sub-category`, `date-created`/`date-revised` set to the run date, `type: install-routing`, `status: REVIEW`, `aliases: []`, `tags: [copilot-configuration, configuration]`, then `topic: beverage-label-compliance`, `use-case: personalization-install-routing`, `visibility: public`).
5. Review the output yourself. Nothing is installed until you perform the click-path yourself, and nothing is final until a person signs off.

## guardrails

Human-in-the-loop: this prompt recommends a layer and click-path; the specialist performs the installation themselves. Never assert a surface is enabled without confirmation; recommend the best available fallback when the ideal layer is unavailable and say so explicitly. Grounding: the fence requires the layering reference as an attached input and forbids Copilot from supplying click-paths, feature names, or gates from product memory; if the reference is not attached or pasted, the run stops. Data classification: the routing output references the artifact by name only and never quotes its content; colleague personal data and confidential formulas do not go into personal Copilot Memory or shareable agent instructions without checking company data-handling policy, since agent instructions are exposed to every future share recipient. Maintenance: replace, do not duplicate; a revised artifact updates or removes the previously installed entry per the maintenance section of [[copilot-layering-reference]].

Related: [[copilot-layering-reference]] (the grounding source), [[communication-style-profile]], [[stakeholder-and-contact-map]], [[team-roles-and-responsibilities]], [[workstream-inventory]] (durable-knowledge/, every one of these routes through this prompt).
