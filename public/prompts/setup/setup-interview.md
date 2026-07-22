---
domain: regulatory-ingredients-labels-laws
category: setup
sub-category: onboarding
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - onboarding
  - regulatory-labeling
  - setup
topic: beverage-label-compliance
use-case: first-run-onboarding-interview
visibility: private
---

# setup-interview

## description

A staged onboarding interview that Copilot conducts with the specialist: one question at a time across six short stages (role, products, workflows, people, communication style, wrap-up). The answers become a single setup profile record that seeds every durable-knowledge artifact and the install router, so the specialist never has to author context documents from a blank page.

## when-to-use

First session with this library, a new team member joining, or any time the specialist wants to rebuild their Copilot context from scratch.

## what-to-use-for

Collecting personal and team working context through guided questions instead of document writing, and producing the setup profile record that downstream prompts consume.

## required-inputs

- None to start; the interview gathers everything by asking. Having a recent week's calendar or task list nearby helps answer the workflow questions.

## expected-outputs

- A setup profile record with one section per stage
- A next-steps list mapping each section to the durable-knowledge prompt that formalizes it

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Copy the entire prompt-text block below and paste it into the chat; no attachments are needed.
3. Answer one question at a time. Say "skip" to pass on a question and "pause" to stop early; a paused interview still produces a partial record you can resume from later.
4. Copilot cannot save files. Copy its full reply into a new note named `setup-profile-record.md` in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. Follow the next-steps list at the end of the record.

## output-handling

File name: `setup-profile-record.md`, H1 equal to the file-name stem. Saves to: `projects/regulatory-labeling/`. Copilot cannot save files; copy the full reply into a new note at that path. Re-running the interview replaces the record; use [[setup-refresh]] for incremental updates.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat, onboarding a regulatory labeling specialist at a US beverage manufacturer. Your single task: interview me, then produce my setup profile record.

Interview rules:
1. Ask exactly one question at a time and wait for my answer before asking the next.
2. Use plain language; never use regulatory or AI jargon in a question.
3. If I answer "skip", record the field as not-provided and move on. If I answer "pause", stop and produce the record from what you have, marking unfinished stages.
4. If an answer is vague, ask one short follow-up, then move on; never interrogate.
5. Record only what I actually say. Never infer, embellish, or fill a field I did not answer.
6. Privacy rule for stage 4: record business roles and work contact channels only. Do not ask for or record personal phone numbers, home emails, or opinions about colleagues.

Stages and questions (adapt wording naturally, keep the order):
Stage 1, role and scope: what is your job title; what does a normal week look like; which decisions are yours versus which get escalated; who do you report to (role, not name, if you prefer).
Stage 2, products and jurisdictions: which product lines and package types do you work on; which markets do the labels ship to (US, Canada, Mexico, other); which regulations do you touch most (it is fine to name them loosely).
Stage 3, workflows and tools: walk me through how a label goes from a project brief to on-shelf at your company; which steps are yours; which Microsoft 365 apps you use daily (Outlook, Excel, Word, SharePoint, Teams, other); where files live today.
Stage 4, people: which roles do you work with weekly (marketing, R&D, QA, legal, co-packers); for each, what do they send you and what do you send them; who signs off on what.
Stage 5, communication style: how formal are your emails; short or detailed; any phrases or formats your team expects; anything you never want an email draft to do.
Stage 6, wrap-up: your top three frustrations in the labeling process today; the one task you most wish Copilot could take off your plate.

When the interview ends (all stages done, or I said pause), return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: setup
sub-category: onboarding
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: setup-record
status: REVIEW
aliases: []
tags:
  - onboarding
  - setup
topic: beverage-label-compliance
use-case: first-run-onboarding-interview
visibility: private
---
2. An H1 equal to: setup-profile-record
3. One H2 section per stage (role-and-scope, products-and-jurisdictions, workflows-and-tools, people, communication-style, priorities) containing only what I said, with skipped fields listed as not-provided.
4. An H2 next-steps section mapping the record to follow-up prompts, exactly: communication-style section feeds the communication-style-profile prompt; people section feeds the stakeholder-and-contact-map and team-roles-and-responsibilities prompts; workflows and priorities sections feed the workstream-inventory prompt; then run the personalization-install-router prompt to install the results.
5. This exact final line:
UNVERIFIED DRAFT - requires review by the regulatory labeling specialist before any downstream use.
```

## guardrails

The interview records answers verbatim and never invents context; skipped means not-provided, never guessed. Stage 4 collects business roles and work channels only, per the privacy rules in [[durable-knowledge]]. The record is input for the specialist to review, not an installed profile; installation happens only through [[personalization-install-router]] after human review.

Related: [[setup-refresh]], [[communication-style-profile]], [[stakeholder-and-contact-map]], [[team-roles-and-responsibilities]], [[workstream-inventory]], [[personalization-install-router]].
