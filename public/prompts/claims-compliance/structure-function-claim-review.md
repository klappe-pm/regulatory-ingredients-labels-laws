---
domain: regulatory-ingredients-labels-laws
category: claims-compliance
sub-category: claims
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - claims-compliance
  - claims
  - regulatory-labeling
topic: beverage-label-compliance
use-case: review-structure-function-claim
visibility: private
---

# structure-function-claim-review

## description

Assesses structure/function claims (e.g. "supports immune health") for truthful, non-disease framing, checking that substantiation is on file and the required disclaimer is present.

## when-to-use

A claim has been scoped as structure/function in [[claims-target-scoping]], or any structure/function claim needs review before label finalization.

## what-to-use-for

Reviewing claim text and substantiation on file to confirm the claim describes a structure or function of the body rather than a disease, and that the FDA-required disclaimer accompanies it.

## required-inputs

- Claim text (exact wording)
- Substantiation on file (summary of evidence backing the claim)

## expected-outputs

- Per-claim verdict (pass/fail/na)
- Disease-claim risk assessment
- Disclaimer need (present/missing)
- Citation

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: claims-compliance`, `sub-category: claims`, `date-created`/`date-revised` set to the run date, `type: claim-review`, `status: REVIEW`, `aliases: []`, `tags: [claims-compliance, claims, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: structure-function-claim-review`, `visibility: private`.

File name: `structure-function-claim-review-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: assess structure/function claims for truthful, non-disease framing.

Source of truth: the claim text under test is the artifact being checked; the substantiation-on-file summary I provide is what the claim must be backed by. Structure/function claims are not pre-approved or reviewed by FDA before use; the specialist company bears responsibility for their truthfulness and substantiation.

Method:
1. Read each claim and the substantiation-on-file summary I provide below.
2. Determine whether the claim describes a structure or function of the body (permitted) or crosses into treating, curing, mitigating, or preventing a disease (an unauthorized disease claim, not permitted without going through the drug approval process or an authorized health claim pathway).
3. Assess whether the substantiation on file is described as reasonably supporting the specific claim as worded; flag if the substantiation summary does not clearly support the claim as stated.
4. Confirm whether the required structure/function disclaimer ("This statement has not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.") is present or noted as planned; flag if missing.
5. Produce a findings table: id, field (claim text), expected (permitted structure/function framing plus disclaimer), observed (actual wording and disclaimer status), verdict (pass/fail/na), severity (critical/major/minor), citation, required-action.
6. Produce an aggregate disposition (pass/conditional-pass/fail) with a blocking-issues list.

Cite the structure/function claim framework under 21 CFR 101.93 and the boundary with 21 CFR 101.14/Subpart E authorized health claims. If you cannot confirm current regulatory text, flag it explicitly.

This is an independent second set of eyes; it never marks a claim approved and never confirms the substantiation is scientifically adequate, only that it appears topically responsive to the claim as worded, a human with subject-matter expertise must judge scientific sufficiency.

Do not fabricate a disease-claim risk, a substantiation gap, or a disclaimer requirement not grounded in the provided materials or in 21 CFR 101.93/101.14. Flag anything you cannot confirm.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste claim text(s) here]

[Paste substantiation-on-file summary here]

SKU identifier: [SKU]
```

## guardrails

Human-in-the-loop: this prompt flags disease-claim risk and disclaimer gaps for a human decision; it never judges scientific adequacy of substantiation. Escalate any claim with disease-claim risk to [[prohibited-and-misleading-claim-screen]].

Related: [[nutrient-content-claim-review]], [[prohibited-and-misleading-claim-screen]].
