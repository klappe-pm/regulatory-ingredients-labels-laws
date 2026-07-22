---
domain: regulatory-ingredients-labels-laws
category: label-intake
sub-category: intake
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - label-intake
  - intake
  - claims
  - regulatory-labeling
topic: beverage-label-compliance
use-case: scope-claim-pathways
visibility: private
---

# claims-target-scoping

## description

Captures the claims a brief intends to make and classifies each by the FDA regulatory pathway it would need to clear, so downstream claims-compliance review starts from a scoped inventory instead of raw marketing copy.

## when-to-use

After [[brief-and-formula-intake]] has produced an intake record, or whenever proposed claims and positioning copy exist for a SKU and need to be triaged before drafting or review.

## what-to-use-for

Reading proposed claims and positioning copy, then tagging each distinct claim by claim type (nutrient content, structure/function, authorized health claim, or none of the above/marketing puffery) and the substantiation each pathway requires.

## required-inputs

- Proposed claims (list or extracted from brief/positioning copy)
- Positioning copy (marketing language as drafted)

## expected-outputs

- Claim inventory: each claim, its claim-type tag, the regulatory pathway it falls under, and the substantiation required for that pathway
- Flags for any claim that does not cleanly fit a recognized pathway

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: label-intake`, `sub-category: intake`, `date-created` and `date-revised` set to the run date, `type: claim-inventory`, `status: DRAFT`, `aliases: []`, `tags: [label-intake, intake, claims, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: claim-inventory`, `visibility: private`.

File name: `claim-inventory-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: build a claim inventory from proposed claims and positioning copy, classifying each claim by its regulatory pathway.

Method:
1. Read every proposed claim and the positioning copy I provide below.
2. Extract each distinct claim as its own inventory row, verbatim as written.
3. For each claim, classify it into exactly one of: nutrient content claim (21 CFR 101.13 and Subpart D), implied nutrient content claim including "healthy" (21 CFR 101.65), structure/function claim, authorized health claim (21 CFR 101.14 and Subpart E), or non-regulated marketing language (no claim-type pathway).
4. For each classified claim, state the substantiation or disclosure that pathway requires (for example: a nutrient content claim needs the NFP value that supports it; a structure/function claim needs substantiation on file plus the required disclaimer; a health claim needs to match an FDA-authorized model claim).
5. Flag any claim that is ambiguous between two pathways, or that reads like an unauthorized disease claim, for human review rather than resolving the ambiguity yourself.
6. Do not judge whether any claim will pass; that is the job of the downstream claims-compliance prompts ([[nutrient-content-claim-review]], [[structure-function-claim-review]], [[prohibited-and-misleading-claim-screen]], [[healthy-claim-eligibility-check]]). This prompt only scopes and tags.

Source of truth: the proposed claims and positioning copy I provide are the only sources.

Cite the exact CFR provision or statute for each pathway tag (21 CFR 101.13/Subpart D, 101.65, 101.14/Subpart E). If you cannot confirm the current text or status of a cited provision, say so explicitly rather than asserting it.

This is a scoping pass, not an approval. Do not mark any claim as compliant or cleared here.

Do not fabricate a claim, a pathway, or a substantiation requirement not grounded in the source text or in FDA's actual claim framework. Flag anything you cannot confirm.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste proposed claims here]

[Paste positioning copy here]

SKU identifier: [SKU]
```

## guardrails

Human-in-the-loop: this prompt scopes and tags claims, it never approves them; every downstream compliance verdict belongs to the claims-compliance category prompts. Flag ambiguous or disease-adjacent claims for escalation rather than resolving them here.

Related: [[brief-and-formula-intake]] (upstream), [[nutrient-content-claim-review]], [[structure-function-claim-review]], [[prohibited-and-misleading-claim-screen]], [[healthy-claim-eligibility-check]] (downstream, in a different builder's category, claims-compliance/).
