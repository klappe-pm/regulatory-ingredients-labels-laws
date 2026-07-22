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
use-case: monthly-usage-retro
visibility: private
aliases:
  - copilot usage retro
  - end of month reflection
  - is copilot worth it review
  - keep stop start review
  - monthly retro
  - monthly review of copilot
  - retro on my ai use
  - what worked this month
tags:
  - reflection
  - regulatory-labeling
  - self-improvement
---

# copilot-usage-retro

## prompt-summary

A short monthly retrospective the specialist runs with Copilot: what worked, what wasted time, which prompts earned their keep, which were ignored, and one focused change for next month. It is deliberately lightweight so it actually gets done, and it feeds a running record so month-over-month trends are visible. Reach for it once a month, or at the end of a launch cycle, to keep the library and your habits improving instead of drifting.

## use-cases

- It is month-end (or the end of a launch cycle) and you want a quick keep/stop/start read before habits drift
- You want a dated record that builds a visible trend line so you can compare against last month's retro
- Copilot wasted time on something this month and you want to decide what to change or retire
- A recurring frustration points at a missing reusable asset, and you want to flag it for a [[skill-gap-finder]] run

## expected-outputs

- A dated retro note: what worked, what wasted time, prompts to keep or retire, and one priority for next month
- A short trend line versus last month's retro if one was provided

## prompt

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

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Optionally have last month's retro note ready to attach for comparison.
3. Copy the entire prompt block above and paste it into the chat.
4. Answer the few reflection questions; brief answers are fine.
5. Copilot cannot save files. Copy its full reply into a new note named `copilot-usage-retro-<yyyy-mm-dd>.md` in `projects/regulatory-labeling/`, with H1 equal to the file-name stem, so the series builds a visible trend. Then act on the single next-month priority once you have reviewed it.

## guardrails

Uses only the specialist's answers and any attached prior note; never invents wins, frustrations, or trends. It records a reflection; it changes no saved prompt, record, or installed context. Keep the note short so the habit survives.

Related: [[prompting-style-review]], [[skill-gap-finder]].
