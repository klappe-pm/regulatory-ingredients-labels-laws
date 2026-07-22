---
domain: regulatory-ingredients-labels-laws
category: plan
sub-category: review
date-created: 2026-07-22
date-revised: 2026-07-22
type: plan-evaluation
status: DRAFT
aliases:
  - research database plan adversarial review
tags:
  - adversarial-review
  - research-database
  - web-product
---

# research-database-plan-evaluation

## Verdict

**Verdict:** REVISE

**Dominant Gap:** The browser product is coherent, but its production authority, source contract, private-data policy, and shared API ownership remain unresolved.

**Reviewed Snapshot:** Repository regulatory-ingredients-labels-laws, branch codex/session-20260722-095547, base bdd1967ebbf2bc82f06c4a3a9dc7f8d6c6da2278, reviewed 2026-07-22. Scope: research-database-plan.md, research-database-execution-plan.json, and research-database-web-product-blueprint.md.

## Executive Summary

The intended outcome is sound: a beverage team receives source-backed research, timelines, alerts, and label-review findings rather than an opaque legal answer. The research library and regwatch engine provide a credible starting point, and the plan defines a full authenticated browser product. It cannot yet claim hosted readiness because CFR data sources, identity, cloud, domain, retention, cost inputs, and deployment ownership are decisions rather than facts. The smallest repair is to complete PR-001 contract work and require decision evidence before production lanes. Research-library, design-system, scenario, and contract work may proceed now.

## Scope and Evidence

- Reviewed plan artifacts: the three research-database files listed in the reviewed snapshot.
- Reviewed implementation evidence: regwatch README, scripts/regwatch.py, sibling regwatch modules, Makefile, and the existing regulatory monitoring design.
- Confirmed existing capabilities: source scanning, candidate ingestion, manual promotion, obligation validation, portfolio impact, beverage lens, reports, and warning-letter themes.
- Passed checks: execution JSON validator, strict Markdown audit, and diff whitespace check.
- Unavailable evidence: official CFR source probe, user workflow research, AWS or GCP decision, identity decision, domain ownership, pricing calculator, staging runtime, and private-data recovery drill.

## Readiness Scorecard

| Dimension | Result | Evidence | Required Repair |
|---|---|---|---|
| Authority and Currency | Partial | Active delivery pointer still names delivery-plan.md | Promote this package through an explicit plan decision |
| Problem, Outcome, and Scope | Pass | Workflows, users, non-goals, and browser outcome are named | Validate scenarios with representative users |
| Source Coverage and Lineage | Partial | Regwatch and research library are incorporated | Create source disposition for eCFR, GovInfo, provider, and domain |
| Feature and Requirement Traceability | Partial | Machine plan maps browser product requirements to lanes | Add saved-search and design-system acceptance to PR-005 |
| Dependencies and Contracts | Partial | Produced and consumed contracts are named | Version API, lifecycle, formula, and browser contracts |
| Sequencing and Ownership | Fail | Research, monitoring, reconciliation, and UI touch shared API boundaries | Assign disjoint modules and one schema integration owner |
| Technical Feasibility | Partial | Existing regwatch integration is real | Run source, identity, hosting, and browser proof probes |
| Security and Runtime Boundaries | Partial | Security intent and cloud inventory are defined | Approve retention, recovery, role, and incident policy |
| Verification and Evidence Integrity | Partial | Structural checks pass | Add fixtures, hosted checks, and retained evidence locations |
| Migration, Rollout, and Recovery | Partial | Launch stages and rollback intent exist | Add backup restore, alert replay, and deployment drill |
| Automation and Operations | Partial | Existing scheduled regwatch jobs exist | Define job owner, retry budget, dead-letter, and delivery policy |
| Capacity and Stop Conditions | Fail | Financial framework exists without provider or usage inputs | Populate scenario model after provider decision |
| Agent Usability | Partial | Plan is structurally valid | Pin lane bases and replace planned commands as units land |

## Prioritized Findings

### FIND-001 [High] Production Authority Is Unresolved

- **Confidence:** high
- **Location:** Web Product Blueprint, Hosting, Domain, and DNS Decision Gate
- **Claim:** The product will be deployed on AWS or GCP under a future domain.
- **Evidence:** No provider, identity provider, domain, DNS owner, or environment exists in the repository.
- **Gap:** Production acceptance has no approved external authority.
- **Consequence:** Security, cost, launch, and operational claims cannot be proven.
- **Repair:** PR-001 creates decision records; PR-006 remains blocked until provider, identity, domain, retention, and operator ownership are approved.
- **Acceptance:** A decision record names owner, evidence, selected option, rollback, and environment contract.

### FIND-002 [High] CFR Source Contract Is Unverified

- **Confidence:** high
- **Location:** Research Database Plan, CFR Text Source and Retrieval Decision
- **Claim:** CFR query tools will use bulk snapshots and possibly a current-text API.
- **Evidence:** Existing regwatch has Federal Register ingest but no eCFR or GovInfo adapter.
- **Gap:** Format, hierarchy, version behavior, legal status, rate limits, and fallback are unproven.
- **Consequence:** Query results could be stale, unavailable, or mis-cited.
- **Repair:** Build a source-contract probe with saved response fixtures and dated-snapshot fallback.
- **Acceptance:** Fixtures prove citation hierarchy, source version, retrieval date, and failure behavior for every approved source.

### FIND-003 [High] Shared API Ownership Is Unsafe

- **Confidence:** high
- **Location:** Execution Plan PR-002 through PR-005
- **Claim:** Research, monitoring, reconciliation, and UI lanes can be independently delivered.
- **Evidence:** Their paths and contracts couple through the API, data schemas, and browser results.
- **Gap:** Module boundaries, contract versioning, and shared-schema integration control are absent.
- **Consequence:** Parallel work can conflict or release incompatible behavior.
- **Repair:** PR-001 assigns module ownership and contract versions. The product integration owner serializes shared schema changes.
- **Acceptance:** Each lane owns disjoint modules and every shared contract change has a merge owner and version.

### FIND-004 [High] Private-Data Recovery Policy Is Missing

- **Confidence:** high
- **Location:** Web Product Blueprint, Hosted Architecture and Security
- **Claim:** Formula, supplier, and label-proof records are private.
- **Evidence:** No retention, deletion, backup, restore, or access-review policy exists.
- **Gap:** Security intent has not become an enforceable operating control.
- **Consequence:** Sensitive data may be retained, exposed, or unrecoverable.
- **Repair:** Approve a data policy and run a staging restore drill before the private-upload pilot.
- **Acceptance:** Policy and drill define classification, retention, deletion, backup, restore, access review, and incident owner.

### FIND-005 [Medium] Financial Model Has No Defensible Amount

- **Confidence:** high
- **Location:** Web Product Blueprint, Financial Model
- **Claim:** The product will have estimated cost and financial modeling.
- **Evidence:** Provider, usage, pricing, staffing, and vendor inputs are TBD.
- **Gap:** A numeric forecast would be fabricated.
- **Consequence:** Budget and launch timing cannot use a cost number yet.
- **Repair:** Populate foundation, pilot, and scaled scenarios from a selected provider calculator and current vendor quotes.
- **Acceptance:** The model records fixed and variable cost, sensitivity, currency date, owner, and approval threshold.

### FIND-006 [Medium] Launch Gates Need Measured Thresholds

- **Confidence:** medium
- **Location:** Web Product Blueprint, Launch Plan
- **Claim:** Alpha, pilot, and production readiness have exit gates.
- **Evidence:** Gates exist but no scenario pass rate, alert latency, source freshness, recovery, or user threshold is set.
- **Gap:** Launch remains subjective.
- **Consequence:** Rollout could outpace reliability and usability.
- **Repair:** PR-001 proposes measurable thresholds after user discovery; PR-007 records results and stop conditions.
- **Acceptance:** Each stage has owner, measurement method, threshold, and abort condition.

## Missing Connections Ledger

| Producer | Artifact | Consumer | Required State | Gap | Repair Owner |
|---|---|---|---|---|---|
| PR-001 | API and result schemas | PR-002 through PR-005 | Versioned and accepted | No version protocol | Product integration owner |
| PR-002 | CFR evidence package | Browser research UI | Source and retrieval metadata | UI contract unpinned | Research platform owner |
| PR-003 | Timeline and alert event | Browser monitor UI | Candidate versus confirmed state | Delivery and retry policy absent | Monitoring platform owner |
| PR-004 | Reconciliation packet | Browser label review | Input version and access scope | Retention policy absent | Product verification owner |
| PR-005 | Browser application | PR-006 hosting | Identity, API, storage contract | Provider and identity unresolved | Platform security owner |
| PR-006 | Staging evidence | PR-007 rollout | Hosted security and job gates | Target environment absent | Platform security owner |

## Decision and Probe Register

| Decision or Unknown | Why It Matters | Owner | Cheapest Decisive Evidence | Due Before |
|---|---|---|---|---|
| CFR source contract | Citation accuracy and freshness | Research platform owner | Official response and hierarchy fixture | PR-002 |
| User scenarios and thresholds | Product value and launch gate | Product integration owner | Representative workflow review | PR-002 |
| API ownership | Safe parallel delivery | Product integration owner | Versioned contract and path map | PR-002 through PR-005 |
| Data policy and recovery | Sensitive upload safety | Platform security owner | Policy and restore drill | PR-004 pilot |
| Cloud and identity | Hosted security and cost | Product and platform leads | Decision matrix and provider calculator | PR-006 |
| Domain and DNS | Production launch | Product owner | Registrar ownership and DNS test | Production readiness |

## Final Readiness Statement

The plan is not agent-ready for production hosting. PR-001 discovery, contracts, design-system setup, and evaluation work may start now. Production hosting, private-upload pilot, and general launch wait for the high findings. The next stronger verdict is READY WITH CONDITIONS when source, API ownership, data policy, and external hosting decision records are accepted. The first safe agent action is the product-contract and scenario package, without cloud infrastructure or sensitive product ingestion.
