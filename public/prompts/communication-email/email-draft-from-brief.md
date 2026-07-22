---
domain: regulatory-ingredients-labels-laws
category: communication-email
sub-category: email-editing
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - communication-email
  - email-editing
  - regulatory-labeling
topic: beverage-label-compliance
use-case: draft-email-from-brief
visibility: private
---

# email-draft-from-brief

## description

Drafts an email from a short brief in the specialist's own voice, producing a subject line, body, and alternate subject options.

## when-to-use

The specialist has a purpose, recipient, and key points but no drafted email yet.

## what-to-use-for

Turning purpose, recipient, key points, and target tone into a ready-to-review draft email, applying the specialist's style profile from [[communication-style-profile]] if one has been installed.

## required-inputs

- Purpose (what the email needs to accomplish)
- Recipient (who, and relationship/context if relevant)
- Key points (what must be said)
- Tone (target tone for this email)

## expected-outputs

- Subject plus body draft
- Alternate subject line options
- Note on which style profile was applied, if any

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: communication-email`, `sub-category: email-editing`, `date-created`/`date-revised` set to the run date, `type: email-draft`, `status: DRAFT`, `aliases: []`, `tags: [communication-email, email-editing]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: email-draft-from-brief`, `visibility: private`.

File name: `email-draft-<slug>-<yyyy-MM-dd>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat (or Copilot in Outlook if composing directly). Your single task: draft an email from a short brief.

Method:
1. Read the purpose, recipient, key points, and target tone I provide below, and my installed communication style profile if one is available to you.
2. Draft a subject line and body that accomplishes the stated purpose, covers every key point, and matches the target tone and my style profile.
3. Propose two alternate subject lines.
4. State which style profile, if any, you applied.
5. Do not add a commitment, deadline, or promise not present in the key points I gave you.

Source of truth: the purpose, recipient, key points, and tone I provide are the only sources for content; do not invent facts, dates, or commitments.

This is a draft for my review before sending, not a sent email. Do not represent it as final or already sent.

Do not fabricate a fact, name, or commitment not present in the inputs I provide.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

Purpose: [purpose]

Recipient: [recipient]

Key points: [key points]

Target tone: [tone]
```

## guardrails

This is a draft for human review before sending; it never sends an email itself and never adds a commitment beyond the stated key points.

Related: [[email-tone-and-clarity-revision]], [[email-reply-with-regulatory-position]], [[email-thread-to-actions]], [[communication-style-profile]] (durable-knowledge/, for the style profile referenced above).
