---
domain: regulatory-ingredients-labels-laws
category: setup
sub-category: onboarding
types:
  - prompt
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: refresh-onboarding-profile
visibility: private
aliases:
  - my role changed update copilot
  - quarterly copilot refresh
  - re-run onboarding
  - refresh my copilot profile
  - refresh setup record
  - update copilot about me
  - update setup profile
  - what changed since onboarding
tags:
  - onboarding
  - regulatory-labeling
  - setup
---

# setup-refresh

## prompt-summary

A shorter re-interview that reads your existing setup profile record back to you, asks only what may have changed since it was written, and produces an updated record plus a short list of installed Copilot entries to update or remove. It exists so the specialist maintains context by confirming deltas, not by re-answering the full onboarding interview each quarter. Reach for it when your role, team, product lines, tools, or workstreams have changed, or when a scheduled refresh comes due.

## use-cases

- Your role and scope, product lines, tools, or workstreams have changed since the last record was written.
- A scheduled refresh is due (a quarterly pass is a good default) and you want to confirm deltas rather than re-answer everything.
- A colleague departed or a workstream closed, and you need the stale installed context surfaced for removal.
- You need to know which durable-knowledge artifacts and installed Copilot layers now require updating or retiring.
- You have a current `setup-profile-record.md` from a prior [[setup-interview]] or [[setup-refresh]] run to update in place.

## expected-outputs

- An updated setup profile record with a dated change log section
- A to-update and to-remove list keyed to the durable-knowledge prompts and the install router

## prompt

```
You are running inside Microsoft 365 Copilot Chat, refreshing the context profile of a regulatory labeling specialist at a US beverage manufacturer. Your single task: interview me about what has changed since my attached setup profile record, then produce an updated record.

You should have this input: (1) my current setup-profile-record. If it is missing or unreadable, stop and say so; do not reconstruct it from memory.

Interview rules:
1. First, briefly read back the six section headings and a one-line summary of each from my record, so I can see what you have.
2. Then ask, one question at a time, whether each section has changed: role and scope, products and jurisdictions, workflows and tools, people, communication style, priorities. "No change" is a complete answer; accept it and move on.
3. For a section that changed, ask one follow-up to capture the delta only. Do not re-ask the whole section.
4. Keep the stage-4 privacy rule: business roles and work channels only; no personal contact details or opinions about colleagues.
5. Record only what I say. Never infer a change I did not state, and never drop an unchanged field.

When done, return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: setup
sub-category: onboarding
date-created: [the original record's date-created]
date-revised: [TODAY as yyyy-MM-dd]
type: setup-record
status: REVIEW
aliases: []
tags:
  - onboarding
  - setup
topic: beverage-label-compliance
use-case: refresh-onboarding-profile
visibility: private
---
2. An H1 equal to: setup-profile-record
3. The six H2 sections, carrying unchanged content forward verbatim and applying only the deltas I stated.
4. An H2 change-log section with one dated bullet per change made this run.
5. An H2 to-update section listing, for each changed area, which follow-up to run: communication-style change means re-run the communication-style-profile prompt; people change means re-run stakeholder-and-contact-map and team-roles-and-responsibilities; workflow or priority change means re-run workstream-inventory; then re-run the personalization-install-router. For anything removed (a departed colleague, a closed workstream), add a to-remove line telling me to delete the corresponding installed Memory entry or agent knowledge before installing the new version.
6. This exact final line:
UNVERIFIED DRAFT - requires review by the regulatory labeling specialist before any downstream use.
```

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have ready the current `setup-profile-record.md` from a prior [[setup-interview]] or [[setup-refresh]] run; attach it with the paperclip or a `/` file reference, or paste its text if you cannot attach it.
3. Copy the entire prompt block above, paste it into the chat, and answer only the change questions; "no change" is a valid answer to any of them.
4. Copilot cannot save files. Copy its full reply into `setup-profile-record.md` (H1 equal to the file-name stem) in `projects/regulatory-labeling/`, replacing the old one; the record keeps a dated change-log section so prior states stay visible.
5. Work the to-update and to-remove list, and treat nothing as final until a person signs off.

## guardrails

The refresh carries unchanged content forward verbatim and applies only stated deltas; it never invents a change or silently drops a field. The to-remove list is what keeps stale context from accumulating in Copilot Memory and agent knowledge, per the lifecycle guidance in the durable-knowledge prompts. The record is input for review; installation runs only through [[personalization-install-router]].

Related: [[setup-interview]], [[workstream-inventory]], [[personalization-install-router]].
