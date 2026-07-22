---
domain: regulatory-ingredients-labels-laws
category: regulatory-labeling
sub-category: overview
types:
  - guide
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: onboard-to-prompt-library
visibility: private
aliases:
  - how to use the prompt library
  - user guide
tags:
  - prompt-library
  - regulatory-labeling
  - user-guide
---

# prompt-library-user-guide

A start-to-finish guide to using this prompt library with Microsoft 365 Copilot. It assumes no prior experience with AI tools. Read it once, then keep it open for the first few prompts you run.

## what-this-library-is

A collection of ready-made prompts (instructions you paste into Copilot) for the regulatory labeling work at a US beverage manufacturer. Each prompt does one job: check a claim, build a Nutrition Facts Panel, draft an email, compare two labels. You copy a prompt, paste it into Copilot, fill in a few blanks, and Copilot returns a draft you review. Nothing here approves a label. Every prompt keeps a person in charge.

## what-you-need

- The work (licensed) version of Microsoft 365 Copilot, the one allowed to see company files. If you are not sure which one that is, ask your IT contact. Never put SKU, formula, or colleague information into a personal or public AI tool.
- Your files (formula, approved label, brief) saved in OneDrive or SharePoint, so Copilot can read them.
- This vault open in Obsidian to browse and copy prompts.

## the-five-minute-start

1. Read [[copilot-chat-basics]]. It teaches the moves every prompt assumes: attaching a file, referencing with `/`, and reading Copilot's answer critically.
2. Run [[setup-interview]] once. Copilot interviews you and builds a profile of your role, products, team, and style. This is what makes later prompts sound like you and know your context.
3. Skim the [[regulatory-labeling]] home page to see the categories, or search by what you would call the task (the aliases make prompts findable).
4. Pick one real task and find its prompt (see the map below).

## how-to-run-any-prompt

Every prompt file has the same six sections, and you only ever paste one of them.

1. Open the prompt file in this vault (search by name or by what you would call the task; each prompt has plain-language aliases).
2. Read prompt-summary and use-cases to confirm it fits, and expected-outputs to see what you will get.
3. Copy the prompt block (the fenced block under `## prompt`). That block is self-contained; you do not paste any other section.
4. Paste it into Copilot Chat, fill every [BRACKETED] blank, attach the inputs it names, and send.
5. Follow how-to-run for the exact steps (which app, what to attach, what to name the output). Copilot cannot save files, so you copy its reply into a new note, usually in `projects/regulatory-labeling/`.
6. Review the output. Every compliance output ends with an UNVERIFIED DRAFT line; that is your reminder that nothing is final until you check it and a person signs off.

## reading-a-prompt-file

- prompt-summary: what the prompt does and when to reach for it.
- use-cases: concrete situations that call for it, so you know it is the right one.
- expected-outputs: what you will get back.
- prompt: the only part you paste. Fenced, self-contained, with [BRACKETED] blanks to fill.
- how-to-run: the click-by-click steps and where to save the result.
- guardrails: the safety rules and limits for that prompt.

## which-prompt-do-i-need

| your task | category | start with |
|---|---|---|
| a new brief and formula arrived | label-intake | [[brief-and-formula-intake]] |
| decide which claim rules apply | label-intake | [[claims-target-scoping]] |
| write the ingredient statement | content-derivation | [[ingredient-statement-drafting]] |
| check allergens | content-derivation | [[allergen-statement-verification]] |
| build or check the Nutrition Facts Panel | content-derivation | [[nutrition-facts-panel-buildout]] |
| test a nutrient content claim | claims-compliance | [[nutrient-content-claim-review]] |
| test a body-function claim | claims-compliance | [[structure-function-claim-review]] |
| screen copy for prohibited claims | claims-compliance | [[prohibited-and-misleading-claim-screen]] |
| check "healthy" eligibility | claims-compliance | [[healthy-claim-eligibility-check]] |
| run a checklist review | review-and-verification | [[checklist-template-evaluation]] |
| second-eyes review | review-and-verification | [[second-eyes-hitl-review]] |
| compare approved label vs production | version-reconciliation | [[production-vs-documented-comparison]] |
| check an in-market label | market-and-reporting | [[market-pull-vs-record-check]] |
| write the weekly report | market-and-reporting | [[weekly-status-report]] |
| draft or reply to email | communication-email | [[email-draft-from-brief]] |
| teach Copilot your context | durable-knowledge | [[setup-interview]] then [[communication-style-profile]] |
| install context into Copilot | copilot-configuration | [[personalization-install-router]] |
| get better at using Copilot | reflection | [[prompting-style-review]] |
| use Copilot inside an app | copilot-skills | [[copilot-chat-basics]] |

## the-safety-rules-that-never-change

- Nothing here approves a label. Copilot drafts; a person signs off. Outputs are marked UNVERIFIED DRAFT for that reason.
- Every regulation citation Copilot gives is unverified until you confirm it against the current eCFR. Copilot's memory of the law can be out of date.
- If an input is missing or unreadable, the prompt tells Copilot to stop and say so. If you get a confident answer that ignored a missing file, re-attach and re-run.
- Copilot cannot reliably read photos, scans, or artwork where text is a picture. For those, the prompt flags the field as unable-to-verify; trust that, do not override it.
- Only paste company information into the work (licensed) Copilot. Check company policy before putting colleague personal data or confidential formulas into anything that can be shared.

## keeping-yourself-current

- Re-run [[setup-refresh]] when your role, team, or products change.
- Run [[copilot-usage-retro]] monthly to see what is working.
- When the same manual task keeps recurring, run [[skill-gap-finder]] to turn it into a saved prompt or a new skill.

## getting-unstuck

- Copilot ignored my file: confirm the file is in OneDrive or SharePoint, re-attach with the paperclip or `/`, and wait for confirmation before asking.
- The answer looks generic: it may not have read your inputs; re-attach and say "use only the attached files".
- A citation looks wrong: it probably is; verify it in the current eCFR before using it.
- The tables on the [[regulatory-labeling]] home page look empty or broken: open the vault in current Obsidian with the Bases core plugin enabled.
- The [[prompt-explorer]] dashboard shows code instead of dropdowns: install the Dataview community plugin and enable its JavaScript queries, or just use the home-page tables instead.

Related: [[regulatory-labeling]], [[prompt-explorer]], [[copilot-chat-basics]], [[setup-interview]], [[prompting-style-review]].
