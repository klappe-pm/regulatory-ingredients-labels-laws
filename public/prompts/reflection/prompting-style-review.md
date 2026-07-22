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
use-case: review-prompting-style
visibility: private
aliases:
  - am i prompting well
  - better prompting tips
  - coach my prompts
  - how can i prompt better
  - improve my copilot prompts
  - prompting feedback
  - prompting style review
  - review my prompting
tags:
  - reflection
  - regulatory-labeling
  - self-improvement
---

# prompting-style-review

## prompt-summary

Has Copilot review a sample of the specialist's own recent chats and return concrete, prioritized coaching on how to prompt more effectively: where instructions were vague, where context was missing, where a task should have been split, and which habits are already working. Reach for it after a week or two of real use, when technique feels hit-or-miss, or before deciding which tasks to turn into saved prompts. Written for a beginner LLM user, so the feedback is specific and actionable rather than abstract.

## use-cases

- Your Copilot technique feels hit-or-miss after a week or two of real use and you want a ranked list of what to fix first
- You have three to ten recent chats you can paste and want before-and-after rewrites drawn from your own words
- You are about to decide which recurring tasks to turn into saved prompts and want a read on your habits first (often paired with a [[skill-gap-finder]] run)
- You suspect specific habits are hurting results (vague instructions, missing context, several unrelated asks in one prompt, no stated output format) but cannot name them

## expected-outputs

- A ranked list of prompting improvements, each with a before-and-after example drawn from your own chats
- A short list of what you are already doing well, so you keep it
- One suggested next step (often a saved prompt or a skill-gap-finder run)

## prompt

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

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Gather three to ten recent chats and have them ready: select the conversation text to paste where marked, or attach an export. Remove anything company policy says should not be reused.
3. Copy the entire prompt block above, paste it into the chat, and paste your chats where marked before sending. Fill any bracketed blanks.
4. Copilot cannot save files. Copy its full reply into a new note named `prompting-style-review-<yyyy-mm-dd>.md` in `projects/regulatory-labeling/`, with H1 equal to the file-name stem. The date stamp keeps each review as its own dated record so you can see progress over time.
5. Review the output and pick the top one or two improvements to try in your next real task. Nothing is final until you decide to act on it.

## guardrails

The review uses only the chats the specialist pastes and never invents examples or habits. It coaches; it does not change saved prompts, records, or installed context. Redact anything company policy restricts before pasting, since chat samples may contain SKU, formula, or colleague details.

Related: [[skill-gap-finder]], [[copilot-usage-retro]], [[personalization-install-router]].
