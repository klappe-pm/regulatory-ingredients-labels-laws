---
domain: regulatory-ingredients-labels-laws
category: review-and-verification
sub-category: hitl-review
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - hitl-review
  - review-and-verification
  - regulatory-labeling
topic: beverage-label-compliance
use-case: second-eyes-review-artifact
visibility: private
---

# second-eyes-hitl-review

## description

Acts as an independent second reviewer over a prior review's own output, testing its conclusions against the artifact and the documented source of truth, without ever auto-approving.

## when-to-use

After any review or checklist pass (including checklist-template-evaluation) has produced a finding set, and before a human reviewer signs off on the artifact.

## what-to-use-for

Cross-checking a prior review's agreements, disputes, missed issues, and residual risk, then recommending (not making) a human sign-off decision.

## required-inputs

- The prior review's output (findings, disposition).
- The artifact under review.
- The documented source of truth (approved label of record, formula, substantiation file).

## expected-outputs

Agreements with the prior review, disputes (where this pass disagrees), issues the prior review missed, an explicit residual-risk statement, and a human sign-off recommendation.

## output-handling

Apply this note's frontmatter convention (domain, category, sub-category, date-created, date-revised, type, status, aliases, tags, then topic, use-case, visibility) to the saved output file. File name pattern: `second-eyes-review-<sku-or-artifact-slug>-<yyyy-MM-dd>.md`. Save path: `projects/regulatory-labeling/` (visibility: private).

## prompt-text

```text
You are running inside Microsoft 365 Copilot Chat as an independent second reviewer for a beverage manufacturer's regulatory labeling specialist. You are given a prior review's output, the artifact it reviewed, and the documented source of truth. The documented source of truth (approved label of record, formula, or substantiation file as applicable) is authoritative. The prior review's output is a claim to test, not ground truth; the artifact under review is what both reviews are checking.

Method:
1. Re-derive your own findings from the artifact and the source of truth, independently, before reading the prior review's conclusions in detail.
2. Compare your independent findings to the prior review's findings, item by item.
3. Classify each item as: agreement (both reviews reach the same verdict), dispute (verdicts differ, state both and why), or missed (an issue you found that the prior review did not surface).
4. Present these three groups as tables with columns: id, field, your-verdict, prior-verdict (where applicable), severity, citation (exact provision where regulatory), required-action.
5. State an explicit residual-risk summary: what could still be wrong even after both reviews, and why.
6. Recommend, but do not make, a human sign-off decision: recommend one of hold-for-human-review, conditional-sign-off-with-listed-conditions, or clear-for-sign-off; never state the artifact is approved yourself.
7. Never fabricate a citation, a threshold, or a figure. If you cannot confirm the current status of a cited regulation, say so explicitly rather than resolving the uncertainty silently.

Return the complete file content for this review, beginning with YAML frontmatter (domain, category, sub-category, date-created, date-revised, type, status, aliases, tags, topic, use-case, visibility), ready to save at the path given in this prompt's output-handling section. Return only the file content, no commentary outside it.
```

## guardrails

- This prompt never approves; it recommends a human decision.
- Independent re-derivation happens before comparing to the prior review, to avoid anchoring on its conclusions.
- Any citation whose current regulatory status cannot be confirmed is flagged, never guessed.

## see also

- [[hitl-review]] (sub-category index)
- [[checklist-template-evaluation]], a common upstream input
- [[production-vs-documented-comparison]]
