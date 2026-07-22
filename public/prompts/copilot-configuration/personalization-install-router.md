---
domain: regulatory-ingredients-labels-laws
category: copilot-configuration
sub-category: configuration
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - copilot-configuration
  - configuration
  - regulatory-labeling
topic: beverage-label-compliance
use-case: route-durable-knowledge-artifact
visibility: public
---

# personalization-install-router

## description

Routes a durable-knowledge artifact (see [[durable-knowledge]]) to the correct Microsoft 365 Copilot layer with exact click-path steps, grounded in [[copilot-layering-reference]].

## when-to-use

A durable-knowledge prompt (from [[durable-knowledge]]) has produced an artifact and the specialist needs to know exactly where to install it.

## what-to-use-for

Given an artifact and the list of which Copilot surfaces are enabled in the specialist's tenant, returning the single owning layer, the exact click-path, the cost or admin gate to expect, and a verification step confirming the setting took effect.

## required-inputs

- An artifact (the durable-knowledge output to be installed)
- Which Copilot surfaces are enabled (from the verify-what-is-enabled checklist in [[copilot-layering-reference]])

## expected-outputs

- Owning layer
- Click-path steps
- Caveats
- Verification check

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: copilot-configuration`, `sub-category: configuration`, `date-created`/`date-revised` set to the run date, `type: install-routing`, `status: DONE`, `aliases: []`, `tags: [copilot-configuration, configuration]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: personalization-install-routing`, `visibility: public`.

File name: `install-routing-<artifact-slug>-<yyyy-MM-dd>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `public/regulatory-labeling/` (this is the one public-visibility prompt output in the library).

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: route a durable-knowledge artifact to the correct Copilot layer with exact installation steps.

Source of truth: the layering map in copilot-layering-reference (Custom Instructions, Copilot Memory, Excel personalization/workbook rules, private declarative agent via Agent Builder, Copilot Notebook instructions, Office Scripts via Power Automate) is the grounding for every routing decision. Treat it as a reference to verify against the specialist's own tenant, not as a settled, permanent fact.

Method:
1. Read the artifact I provide and identify what kind of durable knowledge it is: behavioral/style rule, discrete fact, spreadsheet file convention, scoped task/domain context, notebook-scoped context, or executable logic.
2. Read the list of enabled Copilot surfaces I provide.
3. Match the artifact type to its owning layer per the layering map, restricted to what is actually enabled; if the ideal layer is not enabled, recommend the best available alternative and say explicitly that it is a fallback, not the ideal fit.
4. Return the exact click-path to install the artifact in that layer (for example: "Copilot Chat > Settings and more > Chat settings > Personalization > add to Custom Instructions").
5. State the cost or admin gate to expect (free, metered, admin-gated, license-dependent), grounded in the layering reference.
6. Give one verification step: a specific question or action the specialist can take to confirm the installed setting actually took effect.
7. Never assert a capability is enabled without the specialist's confirmation; if the enabled-surfaces list does not cover a needed capability, say so and stop short of assuming it exists.

This recommends where to install the artifact; it never installs it. The specialist performs the click-path themselves.

Do not fabricate a Copilot feature, menu path, or gating rule not grounded in the layering reference provided. Flag anything you cannot confirm against the specialist's own tenant.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste artifact here]

Enabled Copilot surfaces: [list of enabled surfaces]
```

## guardrails

Human-in-the-loop: this prompt recommends a layer and click-path; the specialist performs the installation themselves. Never assert a surface is enabled without confirmation; recommend the best available fallback when the ideal layer is unavailable and say so explicitly.

Related: [[copilot-layering-reference]] (the grounding source), [[communication-style-profile]], [[stakeholder-and-contact-map]], [[team-roles-and-responsibilities]], [[workstream-inventory]] (durable-knowledge/, every one of these routes through this prompt).
