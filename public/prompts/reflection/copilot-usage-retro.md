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
use-case: monthly-usage-retro
visibility: private
---

# copilot-usage-retro

## description

A short monthly retrospective the specialist runs with Copilot: what worked, what wasted time, which prompts earned their keep, which were ignored, and one focused change for next month. It is deliberately lightweight so it actually gets done, and it feeds a running record so month-over-month trends are visible.

## when-to-use

Once a month, or at the end of a launch cycle, to keep the library and the specialist's habits improving instead of drifting.

## what-to-use-for

Producing a dated retro note with a few concrete keep/stop/start items and one priority for the coming month.

## required-inputs

- Optional: last month's `copilot-usage-retro-<date>.md` for trend continuity
- Optional: notes on wins and frustrations from the month; the retro also works from memory answered in the chat

## expected-outputs

- A dated retro note: what worked, what wasted time, prompts to keep or retire, and one priority for next month
- A short trend line versus last month's retro if one was provided

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Optionally attach last month's retro note for comparison.
3. Copy the entire prompt-text block below and paste it into the chat.
4. Answer the few reflection questions; brief answers are fine.
5. Copilot cannot save files. Copy its full reply into a new note named `copilot-usage-retro-<yyyy-mm-dd>.md` in `projects/regulatory-labeling/`, then act on the single next-month priority.

## output-handling

File name: `copilot-usage-retro-<yyyy-mm-dd>.md`, H1 equal to the file-name stem. Saves to: `projects/regulatory-labeling/`. Copilot cannot save files; copy the full reply into a new dated note so the series builds a visible trend.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat, running a monthly usage retrospective with a regulatory labeling specialist at a US beverage manufacturer who is a beginner at using AI assistants. Your single task: interview me briefly, then produce a dated retro note.

Optional input: (1) last month's retro note, if attached, for trend comparison. If it is not attached, run the retro from my answers alone; do not invent a prior month.

Ask these questions one at a time, accept brief answers, and never push:
1. What did Copilot genuinely help with this month?
2. Where did it waste your time or produce something you had to redo?
3. Which prompts or habits do you want to keep using?
4. Which do you want to stop or change?
5. What is the one thing you most want to improve next month?

Method:
1. Record my answers as keep, stop, and start items; keep them concrete and few.
2. If last month's note is attached, add a one-line trend: what improved, what recurred, what is new.
3. Choose exactly one priority for next month, drawn from my answers, and state it as a specific action.
4. If a frustration points at a missing reusable asset, note that a skill-gap-finder run could address it.

Rules: use only my answers and the attached prior note; never invent a win, a frustration, or a trend. Keep it short enough that I will actually do it again next month.

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
use-case: monthly-usage-retro
visibility: private
---
2. An H1 equal to: copilot-usage-retro-[TODAY as yyyy-mm-dd]
3. Keep / stop / start sections, the trend line if applicable, and the single next-month priority.
4. This exact final line:
RETRO NOTES - my own reflection, recorded for next month; not a change to any saved work.
```

## guardrails

Uses only the specialist's answers and any attached prior note; never invents wins, frustrations, or trends. It records a reflection; it changes no saved prompt, record, or installed context. Keep the note short so the habit survives.

Related: [[prompting-style-review]], [[skill-gap-finder]].
