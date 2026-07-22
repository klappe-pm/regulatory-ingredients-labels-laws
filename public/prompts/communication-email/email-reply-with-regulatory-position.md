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
use-case: draft-reply-with-regulatory-position
visibility: private
---

# email-reply-with-regulatory-position

## description

Drafts a reply that states a regulatory position with citations, holding or escalating rather than committing the company to a position it cannot fully substantiate.

## when-to-use

An incoming email or thread asks the specialist to state or confirm a regulatory position (e.g. whether a claim is allowed, whether a label change is compliant).

## what-to-use-for

Turning the incoming email/thread and the specialist's position and citations into a reply that states the position clearly, cites its basis, and includes a hold or escalation note if the position cannot be fully substantiated.

## required-inputs

- Incoming email or thread
- Position and citations (the specialist's intended regulatory position and its basis)

## expected-outputs

- Reply stating the position
- Citations
- Hold or escalation note

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: communication-email`, `sub-category: email-editing`, `date-created`/`date-revised` set to the run date, `type: email-draft`, `status: DRAFT`, `aliases: []`, `tags: [communication-email, email-editing, regulatory-position]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: email-reply-regulatory-position`, `visibility: private`.

File name: `email-reply-regulatory-position-<slug>-<yyyy-MM-dd>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat (or Copilot in Outlook if replying directly). Your single task: draft a reply that states a regulatory position with citations.

Source of truth: the position and citations I provide are what this reply states; the incoming email/thread is what it responds to. Do not state a position stronger than what my supplied position and citations actually support.

Method:
1. Read the incoming email/thread and my stated position and citations below.
2. Draft a reply that states the position clearly, in plain language a non-specialist recipient can follow, while citing the exact regulatory provision(s) my position rests on.
3. If my supplied position and citations do not fully resolve the question being asked, do not fill the gap yourself; draft the reply to state what is confirmed, and add an explicit hold or escalation note (e.g. "confirming with [role] before finalizing" or "this needs legal review before we commit to this position externally").
4. Do not overstate certainty; if a citation's current status cannot be confirmed, say so in the reply rather than presenting it as settled.

This is a draft for my review before sending, not a sent reply.

Do not fabricate a citation, a regulatory conclusion, or a commitment beyond what I supplied as my position.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste incoming email/thread here]

[Paste my position and citations here]
```

## guardrails

Never commit the company to a regulatory position stronger than the supplied citations support; when in doubt, the reply holds or escalates rather than asserts.

Related: [[email-draft-from-brief]], [[email-tone-and-clarity-revision]], [[nutrient-content-claim-review]], [[healthy-claim-eligibility-check]] (claims-compliance/, common sources for the underlying position).
