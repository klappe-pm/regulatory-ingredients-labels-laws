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
- Discrete facts for Copilot Memory, each phrased as a "Remember that ..." statement
- Install footer naming the owning Copilot layer and load steps

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have the inputs ready: writing samples, stated preferences, and your role. Attach files with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint); paste text directly when a file cannot be attached.
3. Copy the entire prompt-text block below, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `communication-style-profile-record-<yyyy-MM-dd>.md` in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. Review the output yourself, then install it by hand per its install footer. Nothing installs automatically and nothing is final until a person signs off.

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: durable-knowledge`, `sub-category: personalization`, `date-created`/`date-revised` set to the run date, `type: style-profile`, `status: REVIEW`, `aliases: []`, `tags: [durable-knowledge, personalization]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: communication-style-profile`, `visibility: private`.

File name: `communication-style-profile-record-<yyyy-MM-dd>.md`, kebab-case, H1 equal to the file-name stem. The `-record` suffix keeps outputs from colliding with this prompt file's stem.

Saves to: `projects/regulatory-labeling/`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: capture the specialist's communication style as two separated durable outputs, one for Custom Instructions and one for Copilot Memory.

You should have these inputs: (1) writing samples, (2) stated preferences, (3) the specialist's role. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Privacy rule: business role information only; no personal phone numbers or home emails, no performance or personality judgments about colleagues, and prefer role labels over named individuals where the role suffices.

Method:
1. Read the writing samples, stated preferences, and role provided below.
2. Derive style rules: voice (formal/informal, first/third person, sentence length tendencies), formatting defaults (bullet vs prose, heading use, no em dashes if that is a stated preference), a do/don't list, and a short phrase bank of wording the specialist tends to reuse. Write these as rules for Custom Instructions.
3. Separately, derive discrete facts worth remembering (role, team, recurring correspondents by role, standing preferences not about style) as short factual statements for Copilot Memory, each phrased so it can be pasted into chat as "Remember that <fact>".
4. Do not invent a preference not evidenced in the writing samples or explicitly stated; if a stylistic pattern is only weakly evidenced, note it as tentative rather than asserting it as a firm rule.
5. End with an install footer: style rules go into Custom Instructions (Copilot Chat, Settings and more, Chat settings, Personalization); Memory facts are seeded by telling Copilot "Remember that <fact>" in chat, one fact per message, then verified and pruned in the same Personalization pane (the pane itself is view and delete only; verify against your own tenant, since menus and rollout vary). Note that behavioral-rule propagation into inline Word/Excel/Outlook authoring is partial and rolling, so the specialist should verify the rules actually apply in each surface they use. Include a one-line verification step: ask Copilot a style-revealing question and confirm the response reflects the installed rules.

Source of truth: the writing samples, stated preferences, and role provided below are the only sources.

This is durable context for the specialist to review and install themselves; it never installs itself, and it never asserts a preference the samples do not support.

Do not fabricate a preference, a fact, or a phrase not evidenced in the inputs.

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: durable-knowledge
sub-category: personalization
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: style-profile
status: REVIEW
aliases: []
tags:
  - durable-knowledge
  - personalization
topic: beverage-label-compliance
use-case: communication-style-profile
visibility: private
---
2. An H1 equal to the output file name without .md: communication-style-profile-record-[TODAY as yyyy-MM-dd]
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review by the regulatory labeling specialist before installing into any Copilot layer.

[Paste writing samples here]

[Paste stated preferences here]

Role: [role]
```

## guardrails

Human-in-the-loop: the specialist reviews and installs these rules themselves; this prompt never writes directly into Custom Instructions or Memory. Tentative patterns are flagged as tentative, not asserted as firm rules. Privacy: the output carries business role information only, never personal phone numbers, home emails, or judgments about colleagues; confirm against Talking Rain's Copilot and data-handling policy before installing.

Related: [[personalization-install-router]] (copilot-configuration/, routes this artifact to its layer), [[stakeholder-and-contact-map]], [[team-roles-and-responsibilities]], [[workstream-inventory]].
