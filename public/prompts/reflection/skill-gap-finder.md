---
domain: regulatory-ingredients-labels-laws
category: reflection
sub-category: self-improvement
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - reflection
  - regulatory-labeling
  - self-improvement
topic: beverage-label-compliance
use-case: find-skill-gaps
visibility: private
---

# skill-gap-finder

## description

Takes a list of the specialist's recurring tasks (or a batch of recent chats) and identifies which ones are worth turning into a reusable asset: a saved prompt, a fill-in template, or a full Copilot skill. It ranks the candidates by how often the task recurs and how much time each conversion would save, then drafts the single best candidate so the specialist has something concrete to install.

## when-to-use

The same manual task keeps recurring, the library seems to be missing a prompt for something done often, or after a [[prompting-style-review]] flags a repeated task type.

## what-to-use-for

Deciding what to systematize next and getting a first draft of the top candidate, rather than re-solving the same task by hand each time.

## required-inputs

- A list of tasks you do repeatedly, or three to ten recent chats showing them; note roughly how often each recurs

## expected-outputs

- A ranked table of candidate assets: task, recurrence, time saved, best form (saved prompt, template, or skill), and why
- A drafted top candidate ready to refine and install
- A pointer to where each asset should live (a durable-knowledge record, a saved prompt, or a copilot-skills guide)

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Either paste a bulleted list of your recurring tasks with rough frequencies, or attach and reference several recent chats that show them.
3. Copy the entire prompt-text block below, paste it into the chat, and fill the list where marked before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `skill-gap-finder-<yyyy-mm-dd>.md` in `projects/regulatory-labeling/`.
5. Take the drafted top candidate, refine it, and install it via [[personalization-install-router]] or save it as a reusable prompt.

## output-handling

File name: `skill-gap-finder-<yyyy-mm-dd>.md`, H1 equal to the file-name stem. Saves to: `projects/regulatory-labeling/`. Copilot cannot save files; copy the full reply into a new note at that path.

## prompt-text

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

## guardrails

Uses only the tasks the specialist provides; never invents a recurring task or a frequency. Any candidate that would automate a compliance judgment is flagged as assist-only, never auto-approval, consistent with the whole library's human-sign-off posture. Drafted candidates are starting points the specialist refines, not installed assets.

Related: [[prompting-style-review]], [[copilot-usage-retro]], [[copilot-skills]], [[personalization-install-router]].
