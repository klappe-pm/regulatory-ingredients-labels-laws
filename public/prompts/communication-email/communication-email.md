---
domain: regulatory-ingredients-labels-laws
category: communication-email
sub-category: communication-email
date-created: 2026-07-22
date-revised: 2026-07-22
type: index
status: DONE
aliases: []
tags:
  - communication-email
  - regulatory-labeling
topic: beverage-label-compliance
use-case: browse-communication-email-prompts
visibility: private
---

# communication-email

Drafting, revising, and replying to email in the specialist's voice, and converting threads into decisions and actions: the four-prompt email workflow family (draft, revise, reply, convert-to-actions). All four are drafting aids the specialist reviews before sending or saving; nothing here sends an email, and outputs are unverified drafts until a person signs off.

## surfaces-and-style-profile

- [[email-draft-from-brief]], [[email-tone-and-clarity-revision]], and [[email-reply-with-regulatory-position]] run in Copilot Chat to produce the saveable file output; run in Copilot in Outlook they return subject and body only, into the compose window.
- [[email-thread-to-actions]] runs in Copilot Chat only.
- Only [[email-draft-from-brief]] and [[email-tone-and-clarity-revision]] apply the style profile from [[communication-style-profile]] (durable-knowledge/), falling back to a plain, direct, professional voice when none is installed; [[email-reply-with-regulatory-position]] and [[email-thread-to-actions]] do not use the style profile.

## prompts

- [[email-draft-from-brief]]
- [[email-tone-and-clarity-revision]]
- [[email-reply-with-regulatory-position]]
- [[email-thread-to-actions]]

## workflow

1. [[email-draft-from-brief]] turns a brief into a draft email; its output feeds step 2.
2. [[email-tone-and-clarity-revision]] revises any draft (from step 1 or written directly) and flags overcommitment and compliance risk before the specialist sends.
3. [[email-reply-with-regulatory-position]] drafts citation-backed position replies; the underlying position usually comes from the claims-compliance reviews, every citation stays UNVERIFIED until the specialist confirms it against the current eCFR, and external or novel positions clear a named review gate (regulatory counsel or manager) before sending.
4. [[email-thread-to-actions]] converts a finished thread into decisions, actions, and open questions; extracted action items feed [[weekly-status-report]] (market-and-reporting/).

Up: [[regulatory-labeling]]

![[bases/communication-email.base]]
