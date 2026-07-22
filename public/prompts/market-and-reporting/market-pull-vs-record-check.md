---
domain: regulatory-ingredients-labels-laws
category: market-and-reporting
sub-category: surveillance
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - market-and-reporting
  - surveillance
  - regulatory-labeling
  - comparison
topic: beverage-label-compliance
use-case: check-market-label-vs-record
visibility: private
---

# market-pull-vs-record-check

## description

Compares a label already in the market against the approved record, field by field, to catch drift that reached consumers and needs a recall or relabel decision, not just a print hold.

## when-to-use

A market pull sample, a consumer photo, or a routine shelf audit surfaces an in-market label that needs checking against the approved record of what should be on shelf.

## what-to-use-for

Field-by-field comparison of an in-market label against the approved record, silent-change detection, and escalation of any in-market discrepancy to a recall/relabel decision path.

## required-inputs

- In-market label (image or extracted text)
- Approved record (the source of truth), with its version identifier and effective date
- SKU identifier
- Lot or date code from the pulled sample (or an explicit note that it is unknown)
- Pull date and location (retailer, city, or channel)

## expected-outputs

- Discrepancy findings (one row per field, including pass rows, with a fields-compared attestation)
- Severity (critical/major/minor)
- Recall/relabel escalation flag
- Machine-readable summary (JSON with `no_blocking_findings_detected` and `recall_escalation`)

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Attach the in-market label photo or file and the approved record with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint); paste extracted text directly when a file cannot be attached.
3. Copy the entire prompt-text block below, paste it into the chat, and fill every bracketed placeholder (label text, approved record, SKU, lot or date code, pull date and location, record version and effective date) before sending.
4. Copilot cannot save files. Copy its full reply into a new note named per output-handling, in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder). The file name is date-stamped so repeat pulls of the same SKU never overwrite an earlier check.
5. Review the output yourself. Nothing is final until a person signs off; every citation is unverified until confirmed against the current eCFR.

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: market-and-reporting`, `sub-category: surveillance`, `date-created`/`date-revised` set to the run date, `type: market-surveillance-review`, `status: REVIEW`, `aliases: []`, `tags: [market-and-reporting, surveillance, comparison, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: market-pull-vs-record-check`, `visibility: private`.

File name: `market-pull-vs-record-<sku-slug>-<yyyy-MM-dd>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `projects/regulatory-labeling/`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat as a market surveillance reviewer for a beverage manufacturer's regulatory labeling specialist. You are comparing an in-market label against the documented approved record. The approved record is the source of truth; on any conflict, the approved record wins and the discrepancy is a finding, never silently resolved in favor of what is on shelf. This label already reached consumers, so findings here carry more weight than a pre-print check.

You should have these inputs: (1) the in-market label image or extracted text, (2) the approved record with its version identifier and effective date, (3) the SKU identifier, (4) the lot or date code from the pulled sample or an explicit "unknown", (5) the pull date and location. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Method:
1. Provenance check before any diff: confirm the approved record supplied is the version in force at the sample's production date (from the lot or date code). If the lot or date code is unknown, or you cannot tie the sample's production date to the supplied record version, mark every finding "provisional: record-version unconfirmed", do not map any finding to recall-escalation or relabel, set the aggregate disposition to blocked, and state that a human must confirm the record version before any recall or relabel action.
2. Legibility gating: transcribe the in-market label first and rate every field legible, partial, or unreadable. Diff only legible fields. A partial or unreadable field gets verdict unable-to-verify with required-action "re-pull or re-photograph the sample"; never guess its content and never omit it silently.
3. Extract every field from the in-market label and the approved record: ingredient statement wording and predominance order, sub-ingredient parentheticals, allergen declaration in either permitted format (a Contains statement and/or in-ingredient-list parentheticals per 21 USC 343(w); a format difference alone is not a discrepancy if the declared allergens match the record), every Nutrition Facts Panel value, serving size and RACC, servings per container, added sugars, percent Daily Value figures, net quantity, and each claim's exact wording.
4. Diff field by field. For every enumerated field, record one row, including pass rows: id, field, legibility, expected (approved record), observed (in-market label), verdict, severity, citation (exact provision if regulatory, otherwise "n/a"), required-action. Verdicts: pass (matches the record), fail (discrepancy vs the record), na (field not applicable to this SKU), unable-to-verify (unreadable or uncheckable; never a guess or a silent omission). Severity: critical = blocks use or shipment, major = must fix before sign-off, minor = fix when convenient. Close the table with the attestation line "Fields compared: N of N; skipped: none".
5. Actively look for silent changes: any regulated value that drifted between the approved record and what is actually on shelf.
6. Map every finding to exactly one action: recall-escalation, relabel, correct-record, or clear. Any confirmed undeclared major allergen or safety-relevant discrepancy maps to recall-escalation: escalate immediately to a human decision-maker for health-hazard evaluation and recall classification per 21 CFR 7 and for Reportable Food Registry assessment per FFDCA 417 (21 USC 350f); never map it to clear, correct-record, or a wait state. These recall provisions are context for the human reviewer and are marked UNVERIFIED like every other citation. Relabel applies to critical non-safety discrepancies; correct-record applies when the approved record itself is stale relative to a properly-approved change.
7. Citation discipline: use only these provisions: 21 CFR 101.4 (ingredient statement and predominance order), 21 CFR 101.9 (Nutrition Facts Panel, added sugars, percent Daily Value), 21 CFR 101.12 (RACC and serving size), 21 CFR 101.105 (net quantity), 21 USC 343(w) (major food allergen declaration), 21 CFR 101.13 plus Subpart D (nutrient content claims), 21 CFR 7 and 21 USC 350f (escalation context only). Never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current eCFR before relying on it.
8. Produce the human-readable discrepancy table AND a machine-readable JSON summary block: {"total_fields": n, "critical": n, "major": n, "minor": n, "pass": n, "unable_to_verify": n, "record_version_confirmed": true|false, "no_blocking_findings_detected": true|false, "recall_escalation": true|false}. no_blocking_findings_detected means "no discrepancy detected in this run on the legible fields"; it is never approval, release, or a statement that the product is compliant in market. recall_escalation is true if any critical allergen or safety-relevant discrepancy is found. State the aggregate disposition as exactly one of: no-findings-pending-human-review, findings-require-action, blocked.
9. Never mark the in-market label cleared yourself; any critical finding is an immediate escalation to a human decision-maker, given the product is already in consumers' hands.
10. Never fabricate a citation, a threshold, a figure, or a discrepancy. Flag anything whose current regulatory status you cannot confirm.

[Paste in-market label image description/text here]

[Paste approved record here]

SKU identifier: [SKU]

Approved-record version and effective date: [version, yyyy-MM-dd]

Lot or date code: [lot/date code, or "unknown"]

Pull date and location: [yyyy-MM-dd, retailer/city/channel]

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: market-and-reporting
sub-category: surveillance
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: market-surveillance-review
status: REVIEW
aliases: []
tags:
  - market-and-reporting
  - surveillance
  - comparison
  - [SKU-SLUG]
topic: beverage-label-compliance
use-case: market-pull-vs-record-check
visibility: private
---
2. An H1 equal to the output file name without .md: market-pull-vs-record-<sku-slug>-<yyyy-MM-dd>
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.
```

## guardrails

The approved record always wins on conflict. Any critical finding here is an immediate human escalation, not a wait-for-next-cycle item, because the product is already in market; a confirmed undeclared major allergen or safety-relevant discrepancy escalates for health-hazard evaluation, recall classification (21 CFR 7), and Reportable Food Registry assessment (FFDCA 417, 21 USC 350f), never monitor or clear. Never fabricate a recall recommendation without a critical, clearly-grounded finding. Findings from an unconfirmed record version or an unreadable field are provisional or unable-to-verify, never a compliance conclusion. `no_blocking_findings_detected` means only that this run found no discrepancy on legible fields; it is never approval or release, and every citation stays UNVERIFIED until the specialist confirms it against the current eCFR.

Related: [[production-vs-documented-comparison]], [[change-propagation-audit]], [[print-proof-preflight]] (the same drift-detection family, run at earlier stages, in version-reconciliation/), [[weekly-status-report]].
