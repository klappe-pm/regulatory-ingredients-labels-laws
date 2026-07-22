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
use-case: review-prompting-style
visibility: private
---

# prompting-style-review

## description

Has Copilot review a sample of the specialist's own recent chats and return concrete, prioritized coaching on how to prompt more effectively: where instructions were vague, where context was missing, where a task should have been split, and which habits are already working. Written for a beginner LLM user, so the feedback is specific and actionable rather than abstract.

## when-to-use

After a week or two of real use, when technique feels hit-or-miss, or before deciding which tasks to turn into saved prompts.

## what-to-use-for

Turning a batch of real Copilot conversations into a short, ranked list of prompting improvements the specialist can apply immediately.

## required-inputs

- A sample of recent Copilot chats (copy the text of three to ten conversations, or export them); redact anything you should not paste per company policy

## expected-outputs

- A ranked list of prompting improvements, each with a before-and-after example drawn from your own chats
- A short list of what you are already doing well, so you keep it
- One suggested next step (often a saved prompt or a skill-gap-finder run)

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Gather three to ten recent chats: select the conversation text and paste it into the prompt where marked, or attach an export. Remove anything company policy says should not be reused.
3. Copy the entire prompt-text block below, paste it into the chat, and paste your chats where marked before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `prompting-style-review-<yyyy-mm-dd>.md` in `projects/regulatory-labeling/`.
5. Pick the top one or two improvements and try them in your next real task.

## output-handling

File name: `prompting-style-review-<yyyy-mm-dd>.md`, H1 equal to the file-name stem. Saves to: `projects/regulatory-labeling/`. Copilot cannot save files; copy the full reply into a new note at that path. The date stamp keeps each review as its own dated record so you can see progress over time.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat, coaching a regulatory labeling specialist at a US beverage manufacturer who is a beginner at using AI assistants. Your single task: review the sample of their own recent Copilot chats below and give concrete, prioritized advice on how to prompt better.

You should have this input: (1) a sample of my recent chats, pasted at the end. If none is pasted, stop and ask me to paste some; do not invent examples.

Method:
1. Read the chats as evidence of my prompting habits, not as tasks to redo.
2. Identify recurring patterns in how I prompt: vague instructions, missing context or inputs, no stated output format, several unrelated asks in one prompt, no success criteria, or not saying which app or file to use.
3. Produce a ranked list of at most five improvements. Rank by how much each would improve my results. For each: name the habit, quote a short real example from my chats, show a concrete rewrite of that exact prompt, and say in one line why the rewrite is better.
4. Produce a short "keep doing this" list of two to three things I already do well, with an example each.
5. End with one suggested next step. If you notice the same task type recurring across chats, suggest turning it into a saved prompt or running a skill-gap review.

Rules: use only my pasted chats as evidence; never fabricate an example or attribute a habit you cannot point to. Keep advice specific and actionable for a non-technical user; avoid jargon. This is coaching for me to act on, not a change to any of my saved work.

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
use-case: review-prompting-style
visibility: private
---
2. An H1 equal to: prompting-style-review-[TODAY as yyyy-mm-dd]
3. The ranked improvements, the keep-doing list, and the next step, as specified above.
4. This exact final line:
COACHING NOTES - based only on the chats I pasted; my judgment, not Copilot's, decides what to change.

[Paste your recent Copilot chats here]
```

## guardrails

The review uses only the chats the specialist pastes and never invents examples or habits. It coaches; it does not change saved prompts, records, or installed context. Redact anything company policy restricts before pasting, since chat samples may contain SKU, formula, or colleague details.

Related: [[skill-gap-finder]], [[copilot-usage-retro]], [[copilot-configuration]].
