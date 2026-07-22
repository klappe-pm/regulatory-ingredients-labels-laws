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

Assesses structure/function claims (e.g. "supports immune health") on a conventional beverage for truthful, non-disease framing and a nutritive-value basis, checking that substantiation is on file. The DSHEA disclaimer regime (21 CFR 101.93) applies to dietary supplements only, not to conventional beverages.

## when-to-use

A claim has been scoped as structure/function in [[claims-target-scoping]], or any structure/function claim needs review before label finalization.

## what-to-use-for

Reviewing claim text and substantiation on file to confirm the claim describes a structure or function of the body rather than a disease, derives from the beverage's nutritive value, and is correctly routed if it crosses into health-claim or drug-claim territory.

## required-inputs

- Claim text (exact wording)
- Substantiation on file (summary of evidence backing the claim)

## expected-outputs

- Per-claim verdict (pass/fail/na/unable-to-verify)
- Disease-claim routing (risk-reduction framing vs per-se drug claim)
- Nutritive-value basis flag
- Citation, marked UNVERIFIED until confirmed against the current eCFR

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Attach the claim text and substantiation summary with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint); paste text directly when a file cannot be attached.
3. Copy the entire prompt-text block below, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `structure-function-claim-review-<sku-slug>.md` in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. Review the output yourself. Nothing is final until a person signs off.

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: claims-compliance`, `sub-category: claims`, `date-created`/`date-revised` set to the run date, `type: claim-review`, `status: REVIEW`, `aliases: []`, `tags: [claims-compliance, claims, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: structure-function-claim-review`, `visibility: private`.

File name: `structure-function-claim-review-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `projects/regulatory-labeling/`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: assess structure/function claims on a conventional beverage for truthful, non-disease framing and a nutritive-value basis.

You should have these inputs: (1) claim text exact wording, (2) substantiation-on-file summary, (3) SKU identifier. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Source of truth: the claim text under test is the artifact being checked; the substantiation-on-file summary I provide is what the claim must be backed by. FDA does not pre-approve structure/function claims; the company bears responsibility for their truthfulness and substantiation. This prompt assumes a conventional food (beverage), not a dietary supplement.

Method:
1. Read each claim and the substantiation-on-file summary I provide below.
2. Classify each claim's framing into exactly one of: (a) a structure/function effect on the body, permitted for a conventional beverage when truthful, substantiated, and derived from nutritive value; (b) disease risk-reduction framing (for example "may reduce the risk of..."), which is a health claim requiring prior FDA authorization under 21 CFR 101.14/Subpart E (UNVERIFIED); route it to the health-claim pathway for specialist review, this prompt does not grant it; (c) treatment, cure, mitigation, or diagnosis framing, which is a per-se drug claim under FDCA 201(g) (UNVERIFIED), prohibited for a conventional beverage, with no authorization path and no disclaimer that can cure it.
3. Confirm the claimed effect derives from the nutritive value of the beverage or a nutrient it contains (FDCA 201(g)(1)(C), UNVERIFIED); flag any claim resting on a non-nutritive ingredient as elevated drug-classification risk requiring specialist review.
4. Assess whether the substantiation on file is described as reasonably supporting the specific claim as worded (working standard: competent and reliable scientific evidence); flag if the substantiation summary does not clearly support the claim as stated.
5. Do not require or recommend the DSHEA disclaimer ("This statement has not been evaluated by the Food and Drug Administration..."): the disclaimer and notification regime under 21 CFR 101.93 (UNVERIFIED) applies to dietary supplements only and cannot cure a defective conventional-food claim. If the product is actually marketed as a dietary supplement, stop and flag that this prompt does not cover the supplement regime.
6. Produce a findings table: id, field (claim text), expected (permitted structure/function framing with nutritive-value basis), observed (actual wording, framing classification, and substantiation status), verdict, severity, citation (marked UNVERIFIED), required-action. One row per claim, including passing claims. Close with the attestation line: "Claims reviewed: N of N; skipped: none."
7. Produce an aggregate disposition with a blocking-issues list.

Citation discipline: use only the provisions listed in this prompt. Never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current eCFR before relying on it.

Verdict vocabulary: pass (permitted structure/function framing, nutritive-value basis, substantiation topically responsive), fail (framing, basis, or substantiation defect), na (phrase is not a structure/function claim), unable-to-verify (input unreadable or uncheckable; never guess and never silently omit). Aggregate disposition: no-findings-pending-human-review, findings-require-action, or blocked.

Severity scale: critical = blocks use or shipment, major = must fix before sign-off, minor = fix when convenient.

This is an independent second set of eyes; it never marks a claim approved and never confirms the substantiation is scientifically adequate, only that it appears topically responsive to the claim as worded. A human with subject-matter expertise must judge scientific sufficiency.

Do not fabricate a disease-claim risk, a substantiation gap, or a requirement not grounded in the provided materials or in the provisions above. Flag anything you cannot confirm.

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: claims-compliance
sub-category: claims
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: claim-review
status: REVIEW
aliases: []
tags:
  - claims-compliance
  - claims
  - [SKU-SLUG]
topic: beverage-label-compliance
use-case: structure-function-claim-review
visibility: private
---
2. An H1 equal to the output file name without .md: structure-function-claim-review-[SKU-SLUG]
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.

[Paste claim text(s) here]

[Paste substantiation-on-file summary here]

SKU identifier: [SKU]
```

## guardrails

Human-in-the-loop: this prompt flags framing, routing, and substantiation gaps for a human decision; it never judges scientific adequacy of substantiation. Risk-reduction framing routes to the health-claim pathway for specialist review; treatment, cure, mitigation, or diagnosis framing is reported as a prohibited drug claim with no authorization path. Escalate any claim with disease-claim risk to [[prohibited-and-misleading-claim-screen]].

Related: [[nutrient-content-claim-review]], [[prohibited-and-misleading-claim-screen]].
