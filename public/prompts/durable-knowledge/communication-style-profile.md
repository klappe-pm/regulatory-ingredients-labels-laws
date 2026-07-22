---
domain: regulatory-ingredients-labels-laws
category: durable-knowledge
sub-category: personalization
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - durable-knowledge
  - personalization
  - regulatory-labeling
topic: beverage-label-compliance
use-case: capture-communication-style-profile
visibility: private
---

# communication-style-profile

## description

Captures the specialist's voice and formatting defaults as durable rules: style rules destined for Custom Instructions, and discrete facts destined for Copilot Memory.

## when-to-use

Once, when first setting up Copilot personalization, and again whenever the specialist's writing style or stated preferences change materially.

## what-to-use-for

Turning writing samples, stated preferences, and role context into two clearly separated outputs: durable style rules for Custom Instructions, and discrete facts for Copilot Memory.

## required-inputs

- Writing samples (a few representative emails or documents)
- Stated preferences (anything the specialist explicitly wants followed, e.g. "no em dashes")
- Role (the specialist's role and context)

## expected-outputs

- Style rules for Custom Instructions (voice, formatting defaults, do/don't list, phrase bank)
- Discrete facts for Copilot Memory
- Install footer naming the owning Copilot layer and load steps

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: durable-knowledge`, `sub-category: personalization`, `date-created`/`date-revised` set to the run date, `type: style-profile`, `status: DONE`, `aliases: []`, `tags: [durable-knowledge, personalization]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: communication-style-profile`, `visibility: private`.

File name: `communication-style-profile-<yyyy-MM-dd>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: capture the specialist's communication style as two separated durable outputs, one for Custom Instructions and one for Copilot Memory.

Method:
1. Read the writing samples, stated preferences, and role I provide below.
2. Derive style rules: voice (formal/informal, first/third person, sentence length tendencies), formatting defaults (bullet vs prose, heading use, no em dashes if that is a stated preference), a do/don't list, and a short phrase bank of wording the specialist tends to reuse. Write these as rules for Custom Instructions.
3. Separately, derive discrete facts worth remembering (role, team, recurring correspondents, standing preferences not about style) as short factual statements for Copilot Memory.
4. Do not invent a preference not evidenced in the writing samples or explicitly stated; if a stylistic pattern is only weakly evidenced, note it as tentative rather than asserting it as a firm rule.
5. End with an install footer: state that style rules go into Custom Instructions (Copilot Chat, Settings and more, Chat settings, Personalization) and discrete facts go into Copilot Memory (same Personalization pane), and note that behavioral-rule propagation into inline Word/Excel/Outlook authoring is partial and rolling, so the specialist should verify the rules actually apply in each surface they use. Include a one-line verification step: ask Copilot a style-revealing question and confirm the response reflects the installed rules.

Source of truth: the writing samples, stated preferences, and role I provide are the only sources.

This is durable context for the specialist to review and install themselves; it never installs itself, and it never asserts a preference the samples do not support.

Do not fabricate a preference, a fact, or a phrase not evidenced in the inputs.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste writing samples here]

[Paste stated preferences here]

Role: [role]
```

## guardrails

Human-in-the-loop: the specialist reviews and installs these rules themselves; this prompt never writes directly into Custom Instructions or Memory. Tentative patterns are flagged as tentative, not asserted as firm rules.

Related: [[personalization-install-router]] (copilot-configuration/, routes this artifact to its layer), [[stakeholder-and-contact-map]], [[team-roles-and-responsibilities]], [[workstream-inventory]].
