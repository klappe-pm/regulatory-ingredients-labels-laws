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
use-case: revise-email-tone-clarity
visibility: private
---

# email-tone-and-clarity-revision

## description

Revises an existing email draft for tone, clarity, and commitment risk, flagging any wording that could read as overcommitment or an inadvertent compliance claim.

## when-to-use

A draft email exists (from [[email-draft-from-brief]] or written directly) and needs a tone/clarity pass before sending.

## what-to-use-for

Revising a draft for tone and clarity against a target tone, applying the specialist's style profile from [[communication-style-profile]] if one has been installed (or a plain, direct, professional voice when none is installed), listing every change made, and flagging any phrase that overcommits the company or makes an inadvertent regulatory or health claim.

## required-inputs

- Draft email
- Target tone

## expected-outputs

- Revised email
- Change list
- Flags for overcommitment or compliance risk
- Note on which style profile was applied, if any

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile; to revise directly inside an email instead, open Copilot in Outlook and expect subject and body only, no file output.
2. Have your two inputs ready as text: the draft email (copy its full text) and the target tone; you paste them into the bracketed placeholders, no file attachment needed.
3. Copy the entire prompt-text block below, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named per output-handling, in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. Review the revision and every flag yourself, then send the email from your own mailbox. Nothing is final until a person signs off; Copilot never sends.

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: communication-email`, `sub-category: email-editing`, `date-created`/`date-revised` set to the run date, `type: email-revision`, `status: REVIEW`, `aliases: []`, `tags: [communication-email, email-editing]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: email-tone-clarity-revision`, `visibility: private`.

File name: `email-revision-<slug>-<yyyy-MM-dd>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `projects/regulatory-labeling/`.

## prompt-text

```
Run this in Microsoft 365 Copilot Chat to produce the file output specified at the end. If you are running in Copilot in Outlook instead, return only the revised subject line and body into the compose window and skip the file output contract.

You should have these inputs: (1) the draft email, (2) the target tone. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Your single task: revise a draft email for tone, clarity, and commitment risk.

Method:
1. Read the draft email and target tone I provide below, and my installed communication style profile if one is available to you in Custom Instructions or Memory; if none is available, use a plain, direct, professional voice and note that no style profile was applied.
2. Revise for tone (matching the target tone and my style profile) and clarity (shorter sentences, one point per sentence, no ambiguity about who is doing what by when).
3. Produce a change list: what changed and why, line by line for any substantive edit.
4. Flag any phrase in the original or revised draft that: overcommits the company to a deadline, outcome, or regulatory position it cannot back; makes an inadvertent nutrient content, health, or "healthy" implied claim; or states a regulatory conclusion as settled when it is not.
5. Do not change the factual content of the email beyond tone and clarity; if a flagged phrase needs a factual rewrite, note that as a recommendation rather than silently rewriting the underlying fact.

Keep the email in my first-person voice; it is my email, not Copilot's, and the body never references AI assistance.

Source of truth: the draft email and target tone I provide are the only sources.

This is a draft revision for my review before sending, not a sent email. Do not fabricate a fact or commitment not present in the original draft.

[Paste draft email here]

Target tone: [tone]

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: communication-email
sub-category: email-editing
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: email-revision
status: REVIEW
aliases: []
tags:
  - communication-email
  - email-editing
topic: beverage-label-compliance
use-case: email-tone-clarity-revision
visibility: private
---
2. An H1 equal to the output file name without .md: email-revision-<slug>-<yyyy-MM-dd>
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist before sending.
```

## guardrails

This is a draft revision for human review before sending; it flags overcommitment and compliance risk rather than silently resolving it, and never changes the underlying factual content without saying so. The revision stays in the specialist's first-person voice and never references AI assistance in the body.

Related: [[email-draft-from-brief]], [[email-reply-with-regulatory-position]], [[communication-style-profile]] (durable-knowledge/, for the style profile referenced above).
