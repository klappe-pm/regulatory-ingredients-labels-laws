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

Revising a draft for tone and clarity against a target tone, listing every change made, and flagging any phrase that overcommits the company or makes an inadvertent regulatory or health claim.

## required-inputs

- Draft email
- Target tone

## expected-outputs

- Revised email
- Change list
- Flags for overcommitment or compliance risk

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: communication-email`, `sub-category: email-editing`, `date-created`/`date-revised` set to the run date, `type: email-revision`, `status: DRAFT`, `aliases: []`, `tags: [communication-email, email-editing]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: email-tone-clarity-revision`, `visibility: private`.

File name: `email-revision-<slug>-<yyyy-MM-dd>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat (or Copilot in Outlook if revising directly). Your single task: revise a draft email for tone, clarity, and commitment risk.

Method:
1. Read the draft email and target tone I provide below.
2. Revise for tone (matching the target tone) and clarity (shorter sentences, one point per sentence, no ambiguity about who is doing what by when).
3. Produce a change list: what changed and why, line by line for any substantive edit.
4. Flag any phrase in the original or revised draft that: overcommits the company to a deadline, outcome, or regulatory position it cannot back; makes an inadvertent nutrient content, health, or "healthy" implied claim; or states a regulatory conclusion as settled when it is not.
5. Do not change the factual content of the email beyond tone and clarity; if a flagged phrase needs a factual rewrite, note that as a recommendation rather than silently rewriting the underlying fact.

Source of truth: the draft email and target tone I provide are the only sources.

This is a draft revision for my review before sending, not a sent email.

Do not fabricate a fact or commitment not present in the original draft.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste draft email here]

Target tone: [tone]
```

## guardrails

This is a draft revision for human review before sending; it flags overcommitment and compliance risk rather than silently resolving it, and never changes the underlying factual content without saying so.

Related: [[email-draft-from-brief]], [[email-reply-with-regulatory-position]].
