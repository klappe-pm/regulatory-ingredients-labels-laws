---
domain: regulatory-ingredients-labels-laws
category: copilot-skills
sub-category: excel
date-created: 2026-07-22
date-revised: 2026-07-22
type: skill
status: DONE
aliases: []
tags:
  - copilot-skills
  - excel
  - m365-copilot
  - regulatory-labeling
topic: beverage-label-compliance
use-case: copilot-in-excel
visibility: private
---

# copilot-in-excel

## description

How to use Copilot inside Excel for the number-heavy parts of labeling: organizing formula and ingredient tables, scaffolding Nutrition Facts math, and cleaning up messy data from R&D or a co-packer. The theme throughout: Copilot is fast at structure and slow to be trusted on arithmetic, so it drafts the table and you verify every number.

## when-to-use

You have formula quantities, nutrient data, or a supplier spreadsheet in Excel and want help structuring, checking, or summarizing it, especially before a Nutrition Facts Panel buildout.

## what-copilot-can-do-here

- Explain what a formula or column does in plain language.
- Suggest a formula for a described calculation (percent of RACC, servings per container) that you then check.
- Reorganize, label, and summarize a table, and flag blank or inconsistent cells.
- Draft a formula column across rows once you confirm the logic on one row.

## what-copilot-cannot-do-here

- Be trusted to compute a nutrient value or rounding correctly on its own. It can state a wrong number confidently. Every value it produces is a draft you verify.
- Know your RACC, Daily Values, or rounding rules reliably from memory. Supply them; do not let it recall them.
- Replace the [[nutrition-facts-panel-buildout]] and [[nutrition-facts-panel-rounding-check]] prompts, which force show-your-work math. Use those for the actual panel.

## setup

1. Open the workbook in Excel for the web or desktop with your work account.
2. Turn on Copilot from the ribbon (the Copilot button). Data should be in a proper table (Insert, Table) so Copilot can reference columns by name.
3. Keep one sheet per source (formula, nutrient data) so references stay clear.

## recipes

### understand an inherited spreadsheet

- Prompt: "Explain in plain language what each column in this table represents and what this formula in cell [CELL] calculates. List any columns that look inconsistent or have blanks."
- Use it to orient before you trust an R&D or supplier sheet you did not build.

### scaffold servings-per-container and percent-of-racc

- Prompt: "I will give you the fill volume and the RACC. Show me the arithmetic to compute servings per container and fill as a percent of RACC. Show the division step by step. Do not round yet. RACC = [VALUE], fill = [VALUE]."
- Then confirm the numbers yourself. These two values drive whether the panel is single-serving or dual-column, so a wrong one is expensive.

### clean up supplier data

- Prompt: "Standardize this ingredient table: one ingredient per row, consistent units, flag any row missing a quantity or unit. Do not invent a missing value; mark it as missing."
- Copilot restructures; you fill the gaps from the source document.

### hand off to the panel prompts

- Once the data is clean, do the actual Nutrition Facts work with [[nutrition-facts-panel-buildout]] and the rounding with [[nutrition-facts-panel-rounding-check]], which require supplied RACC and DV values and force shown arithmetic. Do not let in-sheet Copilot be the final word on any declared number.

## guardrails

Copilot in Excel is a drafting and organizing aid, never the source of truth for a declared nutrient value. Verify every number it produces, supply RACC/DV/rounding rules rather than letting it recall them, and run the dedicated panel prompts for anything that goes on a label. A number that reaches a Nutrition Facts Panel must be traceable to your inputs and checked by a person.

Related: [[nutrition-facts-panel-buildout]], [[nutrition-facts-panel-rounding-check]], [[copilot-chat-basics]].
