---
domain: regulatory-ingredients-labels-laws
category: reflection
sub-category: self-improvement
types:
  - prompt
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: find-skill-gaps
visibility: private
aliases:
  - build a copilot skill
  - find skill gaps
  - systematize my recurring tasks
  - what am i missing a prompt for
  - what should i turn into a saved prompt
  - what skills do i need
  - what to automate next
  - which tasks need a template
tags:
  - reflection
  - regulatory-labeling
  - self-improvement
---

# skill-gap-finder

## prompt-summary

Takes a list of the specialist's recurring tasks (or a batch of recent chats) and identifies which ones are worth turning into a reusable asset: a saved prompt, a fill-in template, or a full Copilot skill. It ranks the candidates by how often the task recurs and how much time each conversion would save, then drafts the single best candidate so the specialist has something concrete to install. Reach for it when the same manual task keeps recurring or the library seems to be missing a prompt for something you do often.

## use-cases

- The same manual task keeps recurring and you want to decide what to systematize next instead of re-solving it by hand
- The library seems to be missing a prompt for something you do frequently and you want it drafted for you
- A [[prompting-style-review]] flagged a repeated task type and you want to convert it into a reusable asset
- You have three to ten recent chats or a bulleted task list (with rough frequencies) and want a ranked table plus a first draft of the top candidate

## expected-outputs

- A ranked table of candidate assets: task, recurrence, time saved, best form (saved prompt, template, or skill), and why
- A drafted top candidate ready to refine and install
- A pointer to where each asset should live (a durable-knowledge record, a saved prompt, or a copilot-skills guide)

## prompt

```
You are running inside Microsoft 365 Copilot Chat, advising a regulatory labeling specialist at a US beverage manufacturer who is a beginner at using AI assistants. Your single task: from my recurring tasks below, identify which are worth turning into reusable assets and draft the best one.

You should have this input: (1) a list of my recurring tasks (or chats showing them), pasted at the end, ideally with rough frequency. If nothing is pasted, stop and ask; do not invent tasks.

Definitions to apply:
- Saved prompt: a single reusable instruction I paste when I need it. Best for a well-defined task with variable inputs.
- Template: a fill-in document (Word or Excel) I reuse. Best when the output shape is fixed and I fill blanks.
- Skill: a short written guide for using Copilot inside a specific app (Outlook, Excel, Word, SharePoint) for a recurring workflow. Best when the task is really "how do I get Copilot to help me in this app repeatedly."

Method:
1. Cluster my tasks into distinct recurring jobs; merge near-duplicates.
2. Score each job on recurrence (how often) and time-saved-if-systematized (rough, low/medium/high). Do not fabricate frequencies; if I did not give one, mark it unknown and ask me to confirm.
3. Recommend the best form (saved prompt, template, or skill) for each, with a one-line reason.
4. Produce a ranked table: job, recurrence, time saved, best form, where it should live (durable-knowledge record, saved prompt, or a copilot-skills guide), reason.
5. Draft the single top-ranked candidate in full so I can use it immediately: if a saved prompt, write the prompt; if a template, outline its sections; if a skill, write the short app-specific how-to.
6. Note anything that should not be systematized (one-off or judgment-heavy tasks) so I do not over-automate compliance decisions.

Rules: use only the tasks I provide; never invent a recurring task or a frequency. Flag any candidate that would automate a compliance judgment, and state that such tasks stay human-decided and only get assistive prompts, never auto-approval.

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: reflection
sub-category: self-improvement
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: reflection-note
status: REVIEW
aliases: []
tags:
  - reflection
  - self-improvement
topic: beverage-label-compliance
use-case: find-skill-gaps
visibility: private
---
2. An H1 equal to: skill-gap-finder-[TODAY as yyyy-mm-dd]
3. The ranked table, the drafted top candidate, and the do-not-systematize note.
4. This exact final line:
DRAFT CANDIDATES - based only on the tasks I listed; I review and refine before installing anything.

[Paste your recurring tasks or recent chats here]
```

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have your inputs ready: either a bulleted list of your recurring tasks with rough frequencies, or several recent chats that show them to attach or reference.
3. Copy the entire prompt block above, paste it into the chat, and fill the list where marked before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `skill-gap-finder-<yyyy-mm-dd>.md` in `projects/regulatory-labeling/`, with H1 equal to the file-name stem.
5. Take the drafted top candidate, refine it, and install it via [[personalization-install-router]] or save it as a reusable prompt. Nothing is installed until you review and refine it.

## guardrails

Uses only the tasks the specialist provides; never invents a recurring task or a frequency. Any candidate that would automate a compliance judgment is flagged as assist-only, never auto-approval, consistent with the whole library's human-sign-off posture. Drafted candidates are starting points the specialist refines, not installed assets.

Related: [[prompting-style-review]], [[copilot-usage-retro]], [[copilot-chat-basics]], [[personalization-install-router]].
