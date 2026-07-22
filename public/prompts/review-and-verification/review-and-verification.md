---
domain: regulatory-ingredients-labels-laws
category: review-and-verification
sub-category: review-and-verification
date-created: 2026-07-22
date-revised: 2026-07-22
type: index
status: DONE
aliases: []
tags:
  - review-and-verification
  - regulatory-labeling
topic: beverage-label-compliance
use-case: browse-review-and-verification-prompts
visibility: private
---

# review-and-verification

Prompts that check a labeling artifact against a checklist or against a prior reviewer's own output, without ever auto-approving. These are the human-in-the-loop layer of the library: every output here recommends a human sign-off decision rather than making one, and every citation in an output stays marked UNVERIFIED until the specialist confirms it against the current eCFR.

Capability caveat: a second Copilot pass is not an independent human review. Both prompts run on the same model, driven by the same user, in the same Microsoft 365 tenant, so errors shared by the passes (a common misreading or a shared fabricated citation) are not caught here. These prompts supplement, and never replace, review by a second person.

## prompts

- [[checklist-template-evaluation]]: runs a labeling artifact against a checklist template and writes a finding for every item, one by one.
- [[second-eyes-hitl-review]]: runs a second review pass over an artifact and a prior reviewer's own output in two stages, surfacing agreement, disagreement, and residual risk without ever marking the work approved.

## workflow

1. Run [[checklist-template-evaluation]] against the artifact, its checklist template (or the built-in defaults), and its source records; save the output to `projects/regulatory-labeling/`.
2. Run stage-a of [[second-eyes-hitl-review]] in a fresh Copilot chat with only the artifact and the source of truth attached, so the re-derived findings are not anchored on the first pass.
3. Run stage-b of [[second-eyes-hitl-review]] with the stage-a findings, the prior review's output, and the source of truth; save the output to `projects/regulatory-labeling/`.
4. The specialist reads both outputs, confirms every UNVERIFIED citation against the current eCFR, and makes the sign-off decision; nothing in this category approves anything.

## see also

- [[regulatory-labeling]] (master index)
- [[production-vs-documented-comparison]]

![[bases/review-and-verification.base]]
