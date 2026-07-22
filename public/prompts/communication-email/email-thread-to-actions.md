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
use-case: convert-thread-to-actions
visibility: private
---

# email-thread-to-actions

## description

Converts an email thread into a summary, decisions made, action items with owners, and open regulatory questions, so nothing discussed in email gets lost.

## when-to-use

A thread has run long enough (or reached a conclusion) that its content needs to become tracked decisions and actions rather than staying buried in email.

## what-to-use-for

Reading a thread end to end and extracting what was decided, what still needs doing, and what regulatory questions remain open.

## required-inputs

- Email thread

## expected-outputs

- Summary
- Decisions
- Action items with owners
- Open questions

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: communication-email`, `sub-category: email-editing`, `date-created`/`date-revised` set to the run date, `type: thread-summary`, `status: DONE`, `aliases: []`, `tags: [communication-email, email-editing]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: email-thread-to-actions`, `visibility: private`.

File name: `thread-summary-<slug>-<yyyy-MM-dd>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: convert an email thread into a summary, decisions, action items, and open questions.

Method:
1. Read the entire thread I provide below, in chronological order.
2. Write a short summary of what the thread was about and how it resolved (or where it stands if unresolved).
3. List every decision actually made in the thread, attributed to whoever made it, exactly as stated; do not infer a decision that was discussed but not actually settled.
4. List every action item mentioned, with an owner (the person named in the thread) and a due date if one was stated; if no owner or date was given, say so rather than assigning one.
5. List every regulatory question raised in the thread that was not resolved by the end of it.

Source of truth: the thread I provide is the only source; do not add a decision, owner, or deadline not stated in it.

This is a summarization pass, not a decision-making one; unresolved items stay listed as open questions, never resolved here.

Do not fabricate a decision, an owner, or a deadline not present in the thread.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste email thread here]
```

## guardrails

Never invents a decision, owner, or deadline the thread did not actually state; unresolved regulatory questions stay open, never silently closed.

Related: [[email-draft-from-brief]], [[weekly-status-report]] (market-and-reporting/, a common downstream consumer of extracted action items).
