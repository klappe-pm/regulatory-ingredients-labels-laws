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
- Recipient type (internal or external)

## expected-outputs

- Reply stating the position, in the specialist's first-person voice
- Citations list, each marked UNVERIFIED pending the specialist's confirmation against the current eCFR
- Hold or escalation note, including a named review gate (regulatory counsel or manager) when the recipient is external or the position is novel or contested

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile; to reply directly inside an email instead, open Copilot in Outlook and expect subject and body only, no file output.
2. Have your inputs ready: the incoming email or thread (copy its full text, or attach it with the paperclip or a `/` file reference if it is saved in OneDrive or SharePoint), your position and its citations, and whether the recipient is internal or external.
3. Copy the entire prompt-text block below, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named per output-handling, in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. Before sending the reply: confirm every citation against the current eCFR yourself, and clear the named review gate (regulatory counsel or your manager) for any external recipient or novel or contested position. Copilot's output is never verification and Copilot never sends.

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: communication-email`, `sub-category: email-editing`, `date-created`/`date-revised` set to the run date, `type: email-draft`, `status: REVIEW`, `aliases: []`, `tags: [communication-email, email-editing, regulatory-position]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: email-reply-regulatory-position`, `visibility: private`.

File name: `email-reply-regulatory-position-<slug>-<yyyy-MM-dd>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `projects/regulatory-labeling/`.

## prompt-text

```
Run this in Microsoft 365 Copilot Chat to produce the file output specified at the end. If you are running in Copilot in Outlook instead, return only the subject line and reply body into the compose window and skip the file output contract.

You should have these inputs: (1) the incoming email or thread, (2) my regulatory position and the citations it rests on, (3) the recipient type (internal or external). If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Your single task: draft a reply that states a regulatory position with citations.

Source of truth: the position and citations I provide are what this reply states; the incoming email/thread is what it responds to. Do not state a position stronger than what my supplied position and citations actually support.

Citation discipline: use only the citations I supply. Never invent a provision, subsection, or threshold. Check each supplied citation for form (title, part, section, paragraph, e.g. 21 CFR 101.22(k)) and for apparent fit to the stated position; flag any citation that looks malformed, misdirected, or insufficient in the hold or escalation note. Mark every citation UNVERIFIED in the citations list: I must confirm each one against the current eCFR before sending. Your own knowledge of the CFR is not verification.

Method:
1. Read the incoming email/thread and my stated position and citations below, and identify exactly what regulatory question is being asked.
2. Draft a reply that states the position clearly, in plain language a non-specialist recipient can follow, while citing the exact regulatory provision(s) my position rests on.
3. If my supplied position and citations do not fully resolve the question being asked, do not fill the gap yourself; draft the reply to state what is confirmed, and add an explicit hold or escalation note naming what is still needed (e.g. "confirming with [role] before finalizing").
4. Do not overstate certainty; if a citation's current status cannot be confirmed, say so in the hold or escalation note rather than presenting it as settled.
5. If the recipient is external, or the position is novel or contested, the hold or escalation note must name a review gate: regulatory counsel or my manager signs off before this reply is sent.

Write the reply in my first-person voice: the position is mine as the regulatory labeling specialist, never Copilot's, and the body never references AI assistance. The reply never characterizes itself as legal advice.

This is a draft for my review before sending, not a sent reply. Do not fabricate a citation, a regulatory conclusion, or a commitment beyond what I supplied as my position.

[Paste incoming email/thread here]

[Paste my position and citations here]

Recipient type: [internal or external]

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
  - regulatory-position
topic: beverage-label-compliance
use-case: email-reply-regulatory-position
visibility: private
---
2. An H1 equal to the output file name without .md: email-reply-regulatory-position-<slug>-<yyyy-MM-dd>
3. The body specified in the method above: the reply, the citations list with each citation marked UNVERIFIED, and the hold or escalation note.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.
```

## guardrails

Never commit the company to a regulatory position stronger than the supplied citations support; when in doubt, the reply holds or escalates rather than asserts. Every citation is checked for form and apparent fit and marked UNVERIFIED; the specialist confirms each provision's text against the current eCFR before sending, because Copilot's own CFR knowledge is not verification. An external recipient or a novel or contested position requires a named review gate (regulatory counsel or manager) before sending. The position is the specialist's, never Copilot's; the body never references AI assistance and never characterizes itself as legal advice.

Related: [[email-draft-from-brief]], [[email-tone-and-clarity-revision]], [[nutrient-content-claim-review]], [[healthy-claim-eligibility-check]] (claims-compliance/, common sources for the underlying position).
