---
domain: regulatory-ingredients-labels-laws
category: copilot-skills
sub-category: outlook
date-created: 2026-07-22
date-revised: 2026-07-22
type: skill
status: DONE
aliases: []
tags:
  - copilot-skills
  - m365-copilot
  - outlook
  - regulatory-labeling
topic: beverage-label-compliance
use-case: copilot-in-outlook
visibility: private
---

# copilot-in-outlook

## description

How to use Copilot inside Outlook to draft and reply to email in your voice, summarize long threads, and pull action items, without ever letting it send on its own. Email is where a regulatory position becomes externally consequential, so this guide pairs the convenience with the checks that keep a draft from going out wrong.

## when-to-use

Drafting or replying to email, catching up on a long thread, or turning a thread into a task list, especially anything that states a regulatory position.

## what-copilot-can-do-here

- Draft a new email or a reply from a short instruction, in a chosen tone.
- Summarize a long thread and list what was decided and what is open.
- Suggest action items with owners drawn from the thread.
- Coach your own draft for tone and clarity before you send.

## what-copilot-cannot-do-here

- Send email by itself in this workflow. You review and send; that is deliberate.
- Verify a regulation it cites. A position email must have its citations checked against the current eCFR by you.
- Know your house voice unless you give it one. Install a communication style profile (see [[communication-style-profile]]) or the draft will sound generic.

## setup

1. Use Outlook (web or desktop) with your work account; open the message or start a new one.
2. Open Copilot from the ribbon (Draft with Copilot, or the Summary button at the top of a thread).
3. If you have a communication style profile from [[communication-style-profile]], make sure it is installed so drafts match your voice; otherwise expect a plain professional tone.

## recipes

### draft or reply in your voice

- Use the [[email-draft-from-brief]] or [[email-reply-with-regulatory-position]] prompt from this library rather than a bare "write an email"; they carry the voice, citation, and review-gate rules.
- In Outlook's Draft with Copilot box you can paste the prompt, or draft in Copilot Chat and paste the result into the compose window. For a file-based, saved record of the draft, use Copilot Chat; Outlook's inline drafter returns only a subject and body.
- Always read the draft before sending. Copilot drafts; you are the sender and the author of the position.

### summarize a thread

- Click Summary at the top of the thread, or prompt: "Summarize this thread: what was decided, what is still open, and who owns each open item. Do not infer a decision that was not stated."
- Use [[email-thread-to-actions]] when you want a saved action list; it names who made each decision and flags counsel involvement.

### pull action items

- Prompt: "List the action items in this thread with an owner and a due date if stated. Mark items with no owner or date as unassigned; do not invent one."

## guardrails

Copilot in Outlook never sends for you in this workflow: you review every draft and send it yourself, as the author of any position it states. Check every regulation citation against the current eCFR before sending, do not characterize a reply as legal advice, and if a thread includes legal counsel treat the summary as privileged and confirm before saving it anywhere. Positions are yours, never attributed to Copilot, and AI assistance is never mentioned in the message body.

Related: [[email-draft-from-brief]], [[email-reply-with-regulatory-position]], [[email-thread-to-actions]], [[email-tone-and-clarity-revision]], [[communication-style-profile]].
