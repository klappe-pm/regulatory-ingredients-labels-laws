---
domain: regulatory-ingredients-labels-laws
category: label-intake
sub-category: label-intake
date-created: 2026-07-22
date-revised: 2026-07-22
type: index
status: DONE
aliases: []
tags:
  - label-intake
  - regulatory-labeling
topic: beverage-label-compliance
use-case: browse-label-intake-prompts
visibility: private
---

# label-intake

Prompts that turn a new labeling request into a structured, workable record before any content is drafted. This is the first pass on any new labeling request: normalize the dev brief and formula into a structured record, then classify the intended claims by regulatory pathway before anyone starts drafting content.

## prompts

- [[brief-and-formula-intake]], normalize a dev brief and formula into a structured intake record
- [[claims-target-scoping]], classify proposed claims by regulatory pathway

## workflow

1. Run [[brief-and-formula-intake]] on the dev brief and formula/spec; resolve its open-questions and missing-data lists with R&D and marketing before moving on.
2. Run [[claims-target-scoping]] on the proposed claims and positioning copy; every claim gets a pathway routing tag and an UNVERIFIED citation, never an approval.
3. Feed the intake record into the [[content-derivation]] prompts (ingredient statement, nutrition facts panel, allergen verification) and the claim inventory into the [[claims-compliance]] prompts for adjudication.

Up: [[regulatory-labeling]]

![[bases/label-intake.base]]
