---
domain: regulatory-ingredients-labels-laws
category: communication-email
sub-category: email-editing
types:
  - prompt
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: draft-email-from-brief
visibility: private
aliases:
  - compose email from a brief
  - draft an email
  - draft email in my voice
  - email drafting helper
  - email from bullet points
  - quick email draft
  - turn key points into an email
  - write an email from notes
tags:
  - communication-email
  - email-editing
  - regulatory-labeling
---

# email-draft-from-brief

## prompt-summary

Drafts an email from a short brief in the specialist's own voice, producing a subject line, body, and alternate subject options. Reach for it when you have a purpose, recipient, and key points but no drafted email yet, and you want a ready-to-review first draft. It applies your installed communication style profile from [[communication-style-profile]] if one exists, or a plain, direct, professional voice when none is installed. The draft is yours to review and send; Copilot never sends.

## use-cases

- You have a purpose, recipient, and key points but no drafted email yet.
- You want to turn purpose, recipient, key points, and target tone into a ready-to-review draft.
- You want the email written in your own first-person voice using your style profile from [[communication-style-profile]].
- You want two alternate subject line options to choose from.
- You need a fast first draft that a person reviews before it is sent.

## expected-outputs

- Subject plus body draft
- Alternate subject line options
- Note on which style profile was applied, if any

## prompt

```
Run this in Microsoft 365 Copilot Chat to produce the file output specified at the end. If you are running in Copilot in Outlook instead, return only the subject line and body into the compose window and skip the file output contract.

You should have these inputs: (1) purpose, (2) recipient and whether they are internal or external, (3) key points, (4) target tone. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Your single task: draft an email from a short brief.

Method:
1. Read the purpose, recipient, key points, and target tone I provide below, and my installed communication style profile if one is available to you in Custom Instructions or Memory; if none is available, use a plain, direct, professional voice and note that no style profile was applied.
2. Draft a subject line and body that accomplishes the stated purpose, covers every key point, and matches the target tone and my style profile.
3. Propose two alternate subject lines.
4. State which style profile, if any, you applied.
5. Do not add a commitment, deadline, or promise not present in the key points I gave you.

Write the email in my first-person voice; it is my email, not Copilot's, and the body never references AI assistance.

Source of truth: the purpose, recipient, key points, and tone I provide are the only sources for content; do not invent facts, dates, or commitments.

This is a draft for my review before sending, not a sent email. Do not represent it as final or already sent. Do not fabricate a fact, name, or commitment not present in the inputs I provide.

Purpose: [purpose]

Recipient: [recipient]

Recipient type: [internal or external]

Key points: [key points]

Target tone: [tone]

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: communication-email
sub-category: email-editing
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: email-draft
status: REVIEW
aliases: []
tags:
  - communication-email
  - email-editing
topic: beverage-label-compliance
use-case: email-draft-from-brief
visibility: private
---
2. An H1 equal to the output file name without .md: email-draft-<slug>-<yyyy-MM-dd>
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist before sending.
```

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile; to draft directly into an email instead, open Copilot in Outlook and expect subject and body only, no file output.
2. Have your four inputs ready as text: purpose, recipient (and whether they are internal or external), key points, and target tone; you paste them into the bracketed placeholders, no file attachment needed.
3. Copy the prompt block above, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `email-draft-<slug>-<yyyy-MM-dd>.md` (kebab-case, H1 equal to the file-name stem), saved in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. Review the output yourself, then send the email from your own mailbox. Nothing is final until a person signs off; Copilot never sends.

## guardrails

This is a draft for human review before sending; it never sends an email itself and never adds a commitment beyond the stated key points. The draft is written in the specialist's first-person voice and never references AI assistance in the body.

Related: [[email-tone-and-clarity-revision]], [[email-reply-with-regulatory-position]], [[email-thread-to-actions]], [[communication-style-profile]] (durable-knowledge/, for the style profile referenced above).
