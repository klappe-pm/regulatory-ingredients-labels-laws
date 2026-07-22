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

Reading proposed claims and positioning copy, then tagging each distinct claim by claim type (nutrient content including relative claims and "diet" brand-name use, implied nutrient content including "healthy", percent juice, authorized or qualified health claim, structure/function, "natural", or non-regulated marketing language) and the substantiation each pathway requires.

## required-inputs

- Proposed claims (list or extracted from brief/positioning copy)
- Positioning copy (optional; marketing language as drafted, when it exists separately from the claims list)

## expected-outputs

- Claim inventory: each claim, its claim-type tag, the regulatory pathway it falls under with its citation marked UNVERIFIED, and the substantiation required for that pathway
- Flags for any claim that does not cleanly fit a recognized pathway, reads as a disease claim, or uses "natural" (always routed to human review)

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have the proposed claims and any positioning copy open, then paste their text into the bracketed placeholders in the prompt; attach a file with the paperclip or a `/` file reference only if it already lives in OneDrive or SharePoint.
3. Copy the entire prompt-text block below, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named per output-handling, in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. Review the output yourself. Nothing is final until a person signs off; every routing tag still needs adjudication by the claims-compliance prompts.

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: label-intake`, `sub-category: intake`, `date-created` and `date-revised` set to the run date, `type: claim-inventory`, `status: REVIEW`, `aliases: []`, `tags: [label-intake, intake, claims, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: claim-inventory`, `visibility: private`.

File name: `claim-inventory-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `projects/regulatory-labeling/`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: build a claim inventory from proposed claims and positioning copy, classifying each claim by its regulatory pathway.

You should have these inputs: (1) the proposed claims, (2) optional: positioning copy, (3) the SKU identifier. If the proposed claims or the SKU identifier is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Method:
1. Read every proposed claim and any positioning copy I provide below, including claims implied by headline copy, not only bulleted claims.
2. Extract each distinct claim as its own inventory row, verbatim as written.
3. Classify each claim into exactly one primary routing tag from this list, using only these provisions:
   - nutrient content claim (21 CFR 101.13 and Subpart D)
   - relative claim, such as "reduced" or "less sugar than" (21 CFR 101.13(j))
   - "diet" used in a soft drink brand name (21 CFR 101.13(q)(2))
   - implied nutrient content claim (21 CFR 101.65)
   - "healthy" (21 CFR 101.65(d))
   - percent juice declaration (21 CFR 101.30)
   - authorized health claim (21 CFR 101.14 and Subpart E)
   - qualified health claim (permitted by FDA enforcement discretion letter; not codified in the CFR)
   - structure/function claim on a conventional food (no CFR provision; rests on FDCA section 201(g)(1)(C); do not cite 21 CFR 101.93, which applies only to dietary supplements)
   - "natural" (no codified FDA regulation; FDA policy only; always route to human review)
   - non-regulated marketing language (no claim-type pathway)
4. For each classified claim, state the substantiation or disclosure that pathway requires (for example: a nutrient content claim needs the NFP value that supports it; a structure/function claim needs substantiation on file; an authorized health claim needs to match an FDA-authorized model claim; a qualified health claim needs the exact qualified wording from the FDA enforcement discretion letter).
5. Flag any claim that is ambiguous between two pathways, or that reads like an unauthorized disease claim (wording that states or implies preventing, treating, mitigating, or curing a disease; such a claim can make the product an unapproved drug under FDCA section 201(g)), for human review rather than resolving the ambiguity yourself.
6. Do not judge whether any claim will pass; that is the job of the downstream claims-compliance prompts (nutrient-content-claim-review, structure-function-claim-review, prohibited-and-misleading-claim-screen, healthy-claim-eligibility-check). This prompt only scopes and tags.
7. Close the inventory with this attestation line: Claims extracted: N; inventory rows: N (one row per claim); skipped: none.

Source of truth: the proposed claims and positioning copy I provide below are the only sources.

Use only the provisions listed in this prompt. Never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current eCFR before relying on it.

This is a scoping pass, not an approval. Do not mark any claim as compliant or cleared here.

Do not fabricate a claim, a pathway, or a substantiation requirement not grounded in the source text or in the pathway list above. Flag anything you cannot confirm.

[Paste proposed claims here]

[Paste positioning copy here, or write "none provided"]

SKU identifier: [SKU]

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: label-intake
sub-category: intake
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: claim-inventory
status: REVIEW
aliases: []
tags:
  - label-intake
  - intake
  - claims
  - [SKU-SLUG]
topic: beverage-label-compliance
use-case: claim-inventory
visibility: private
---
2. An H1 equal to the output file name without .md: claim-inventory-[SKU-SLUG]
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.
```

## guardrails

Human-in-the-loop: this prompt scopes and tags claims, it never approves them; every downstream compliance verdict belongs to the claims-compliance category prompts. Flag ambiguous or disease-adjacent claims (wording that states or implies preventing, treating, mitigating, or curing a disease) for escalation rather than resolving them here; route every "natural" claim to human review.

Related: [[brief-and-formula-intake]] (upstream), [[nutrient-content-claim-review]], [[structure-function-claim-review]], [[prohibited-and-misleading-claim-screen]], [[healthy-claim-eligibility-check]] (downstream, in a different builder's category, claims-compliance/).
