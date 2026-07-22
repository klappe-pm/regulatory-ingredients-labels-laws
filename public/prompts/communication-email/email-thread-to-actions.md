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
use-case: convert-thread-to-actions
visibility: private
aliases:
  - action items with owners
  - email thread to tasks
  - extract decisions from email
  - open questions from a thread
  - recap a long email thread
  - summarize an email thread
  - thread summary
  - turn a thread into action items
  - who owns what from this thread
tags:
  - communication-email
  - email-editing
  - regulatory-labeling
---

# email-thread-to-actions

## prompt-summary

Converts an email thread into a summary, decisions made, action items with owners, and open regulatory questions, so nothing discussed in email gets lost. Reach for it when a thread has run long enough (or reached a conclusion) that its content needs to become tracked decisions and actions rather than staying buried in email. It reads the thread end to end and extracts what was decided, what still needs doing, and what regulatory questions remain open, attributing each decision and action to the person named in the thread. When any participant is legal counsel, it marks the output privileged and confidential.

## use-cases

- A thread has run long enough that its content needs to become tracked decisions and actions rather than staying buried in email.
- A thread reached a conclusion and you need the decisions and next steps captured before they are lost.
- You need every action item pulled out with its owner and any stated due date.
- You need the open regulatory questions the thread raised but did not resolve.
- The thread includes legal counsel and the summary must be marked privileged and confidential.

## expected-outputs

- Summary
- Decisions, each attributed to the person who made it
- Action items with owners
- Open questions
- Privileged-and-confidential marking when the thread includes legal counsel

## prompt

```
Run this in Microsoft 365 Copilot Chat. Your single task: convert an email thread into a summary, decisions, action items, and open questions.

You should have this input: (1) the full email thread, in chronological order. If the thread is missing, truncated, or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Method:
1. Read the entire thread I provide below, in chronological order.
2. Write a short summary of what the thread was about and how it resolved (or where it stands if unresolved).
3. List every decision actually made in the thread; every decision names the person who made it, exactly as stated in the thread; do not infer a decision that was discussed but not actually settled.
4. List every action item mentioned, with an owner (the person named in the thread) and a due date if one was stated; if no owner or date was given, say so rather than assigning one.
5. List every regulatory question raised in the thread that was not resolved by the end of it.
6. If any participant in the thread is legal counsel (internal or external), put the line "PRIVILEGED AND CONFIDENTIAL - contains attorney communications" directly under the H1, and end the output by telling me to confirm handling with counsel before saving or sharing this file.

Source of truth: the thread I provide is the only source; do not add a decision, owner, or deadline not stated in it.

This is a summarization pass, not a decision-making one; unresolved items stay listed as open questions, never resolved here.

Do not fabricate a decision, an owner, or a deadline not present in the thread.

[Paste email thread here]

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: communication-email
sub-category: email-editing
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: thread-summary
status: REVIEW
aliases: []
tags:
  - communication-email
  - email-editing
topic: beverage-label-compliance
use-case: email-thread-to-actions
visibility: private
---
2. An H1 equal to the output file name without .md: thread-summary-<slug>-<yyyy-MM-dd>
3. The body specified in the method above, including the privileged-and-confidential marking when step 6 applies.
4. This exact final line:
UNVERIFIED DRAFT - requires review by the regulatory labeling specialist; decisions, owners, and open questions unconfirmed against the source thread.
```

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile. This prompt runs in Copilot Chat only.
2. Have the full email thread ready: copy its complete text in chronological order, or attach it with the paperclip or a `/` file reference if it is saved in OneDrive or SharePoint.
3. Copy the prompt block above, paste it into the chat, and fill the placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `thread-summary-<slug>-<yyyy-MM-dd>.md` (kebab-case, H1 equal to the file-name stem; the date stamp in the file name keeps re-runs from overwriting), saved in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. If the output is marked privileged and confidential (the thread included legal counsel), confirm handling with counsel before saving or sharing it. Review every decision, owner, and open question against the thread yourself; nothing is final until a person signs off.

## guardrails

Never invents a decision, owner, or deadline the thread did not actually state; unresolved regulatory questions stay open, never silently closed. Every decision names the person who made it. When the thread includes legal counsel, the output is marked privileged and confidential and the specialist confirms handling with counsel before saving or sharing it.

Related: [[email-draft-from-brief]], [[weekly-status-report]] (market-and-reporting/, a common downstream consumer of extracted action items).
