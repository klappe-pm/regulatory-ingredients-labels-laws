---
domain: regulatory-ingredients-labels-laws
category: claims-compliance
sub-category: claims-compliance
date-created: 2026-07-22
date-revised: 2026-07-22
type: index
status: DONE
aliases: []
tags:
  - claims-compliance
  - regulatory-labeling
topic: beverage-label-compliance
use-case: browse-claims-compliance-prompts
visibility: private
---

# claims-compliance

Reviewing marketing and label claims against their regulatory pathway, one prompt per pathway: nutrient content claims, structure/function claims, prohibited or misleading claims, and "healthy" eligibility. All four prompts are independent second-eyes reviews; none of them clears a claim on its own.

Authorized health claims (21 CFR 101.14/Subpart E) have no prompt in this category; a claim routed to that pathway (disease risk-reduction framing) goes to the specialist for manual review against the authorized claims in Subpart E.

## routing

| claim looks like | run |
|---|---|
| A defining word such as "free," "low," "reduced," "high," "good source," "excellent source" | [[nutrient-content-claim-review]] |
| An effect on a body structure or function ("supports immune health") | [[structure-function-claim-review]] |
| "Healthy" or similar implied nutrient content wording | [[healthy-claim-eligibility-check]] |
| Copy close to shipping, or anything ambiguous, disease-adjacent, or longevity-flavored | [[prohibited-and-misleading-claim-screen]] |

## workflow

1. Route each claim with the table above after [[claims-target-scoping]] triage and run the matching pathway prompt.
2. Run [[healthy-claim-eligibility-check]] before any "healthy" wording is committed to label art.
3. Run [[prohibited-and-misleading-claim-screen]] last, on the full marketing and label art copy plus a written imagery description, as the final pre-ship screen.
4. Save every output to `projects/regulatory-labeling/` with status REVIEW; outputs feed the specialist's sign-off and the escalations named in each prompt's guardrails.

## prompts

- [[nutrient-content-claim-review]]
- [[structure-function-claim-review]]
- [[prohibited-and-misleading-claim-screen]]
- [[healthy-claim-eligibility-check]]

Up: [[regulatory-labeling]]

![[bases/claims-compliance.base]]
