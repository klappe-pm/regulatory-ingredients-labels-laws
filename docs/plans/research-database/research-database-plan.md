---
domain: regulatory-ingredients-labels-laws
category: plan
sub-category: research-database
date-created: 2026-07-22
date-revised: 2026-07-22
type: research-plan
version: 0.1.0
status: DRAFT
aliases:
  - CFR beverage research plan
  - beverage labeling knowledge-base plan
tags:
  - beverage
  - cfr
  - enforcement
  - food-labeling
  - knowledge-graph
  - research
  - title-21
---

# research-database-plan

## Objective

Build an evidence-linked internal research database for the United States food and beverage regulatory surface. **21 CFR** is the primary corpus. **7 CFR** and **16 CFR** are bounded contextual corpora. The result makes beverage labeling, standards, claims, marketing, enforcement, recalls, policy change, industry trends, and supply-chain effects readable to people and traversable by an LLM.

This is internal research, not legal advice. It does not substitute for counsel, product specifications, or current primary-source verification. The companion machine contract is `research-database-execution-plan.json`. It extends the evidence-first, human-review posture in [[deliverable-3-regulatory-monitoring-design]].

The complete browser-product, design-system, cloud, security, financial-model, and launch blueprint is [research-database-web-product-blueprint.md](research-database-web-product-blueprint.md).

## Primary User Case

An internal beverage product, marketing, or regulatory researcher has a concrete decision question: “For this non-alcoholic beverage, ingredient, proposed label statement, campaign, or supplier change, what federal rules and current signals should we investigate before escalating for review?” The input is the known product facts, proposed statement or change, channel, and timeframe. The output is a cited research brief, not an approval: relevant 21 CFR rules first, any material 7 CFR or 16 CFR context, current status, applicable enforcement or recall patterns, facts still required, gray areas, and an explicit next action or legal-review boundary.

The secondary user case is retrospective pattern discovery: an analyst asks what labeling-related actions, recalls, or market developments have recurred for a beverage topic, and can trace each pattern to dated primary records. “Ask any question across the whole CFR” is not a user case, and “the system approves a label” is explicitly prohibited.

The database will be judged by answer quality for a defined evaluation set of representative beverage questions, citation traceability, clarity about unknown facts, and freshness handling. Corpus size, embedding count, and graph size are implementation measures, not success measures.

## Product Workflows

### CFR Agent Query

An agent receives a CFR citation, a beverage question, or both. It resolves the relevant current and, when requested, dated regulatory text; preserves the citation hierarchy; returns the exact source link and retrieval date; identifies related beverage knowledge; and states when the question needs product facts or legal review. The tool returns an evidence package, not a freeform answer based on memory.

### Regulatory Change Timeline and Alert

The system detects proposed, final, delayed, withdrawn, and effective actions from authoritative sources. It stores a lifecycle record with docket or document identifier, proposal date, comment opening and closing dates, final publication, statutory effective date, compliance or implementation date, later delay or court event, and source records. It renders a timeline that keeps proposed and actual events separate. Alerts fire for a new proposal, comment-period opening or closing, final action, implementation date, delay, withdrawal, recall, and source change. Detection creates a candidate for human confirmation and never auto-edits a curated obligation.

### Beverage Knowledge and Recall Intelligence

The existing `regwatch` records, ingredient-function taxonomy, portfolio model, change log, warning-letter themes, and beverage lens become the beverage context layer. Recall and enforcement records are indexed separately by action type, product, hazard or labeling issue, affected ingredient or claim, distribution/lot context when public, action date, status, and source. The feature can answer what has happened recently and what recurring patterns suggest, without equating a recall with a confirmed violation.

### Label Proof and Formulation Reconciliation

Given a label proof and a structured formulation or supplier specification, the feature extracts and compares ingredient statements, declared ingredient names, ordering basis, subingredients, carriers, allergens where in scope, claims, and known product attributes. It produces a discrepancy report with `consistent`, `inconsistent`, `missing-input`, `requires-source-check`, or `requires-legal-review` outcomes. It does not pronounce a label legally compliant. A proof image or PDF must be accompanied by a human-verified text extraction before a substantive finding is treated as reliable.

## Required Data Contracts

The query and timeline workflow needs CFR source records, citation hierarchy, source version, issue date, retrieval date, and a lifecycle-event schema. The reconciliation workflow needs a versioned product profile, formula components and their weights or ordering basis, supplier ingredient specifications and subingredients, intended market/channel, and a versioned label-proof text record. Missing inputs are findings, not blank fields to guess.

The output contract for every tool call is a source-backed result: question or input identity, scope, relevant evidence, current status, timeline where relevant, confidence, material unknowns, discrepancies or alerts, and recommended next action. The result carries an explicit `not_legal_advice` and `human_review_required` indicator when a conclusion depends on product facts or legal judgment.

Search is a first-class workflow. It supports keyword and exact-phrase search plus structured filters for date, company, CFR citation, warning letter, recall, action type, source, topic, ingredient, claim, lifecycle state, and confidence. Users can save a query, result set, source-backed brief, or record collection to their profile. Saved research is private by default, versioned with its source snapshot and retrieval date, and shareable only inside an authorized organization workspace.

## Hosted Browser Product

The product is an authenticated browser workspace, initially for an internal beverage team. The research library remains the authoritative evidence layer. Browser users do not need to understand the graph or invoke raw agent tools; the UI calls bounded server-side tools and shows their sources, status, and uncertainty.

The initial navigation has five primary workspaces:

| Workspace | User outcome | Required browser behavior |
|---|---|---|
| Research | Answer a beverage regulatory question | Query with citations, source preview, confidence, related rules, and open facts |
| Timeline | See proposed and actual regulatory change | Filter by topic, product, rule, or date; show comment period, final, effective, compliance, and implementation events separately |
| Alerts | Act on change, recall, and deadline signals | Triage, assign, acknowledge, link a source, and never silently suppress an alert |
| Label Review | Compare a label proof to evidence and a formulation | Upload or enter proof text, select a product/formula version, view discrepancies and missing inputs, export a review packet |
| Library | Navigate durable beverage knowledge | Browse CFR topics, claims, standards, actions, recalls, sources, and graph-linked related notes |

Every result view exposes a “why this result” panel with the source records, data versions, tool invocation time, and unresolved facts. The UI must never use visual language such as “approved,” “compliant,” or “safe” for an automated result.

## Hosted Architecture and Security

The browser is a thin authenticated client. An application API mediates all access to the research library, agent tools, workflow state, alert routing, and product data. A background worker runs source polling, change detection, timeline calculation, recall monitoring, and report generation. Source snapshots and uploaded label-proof/formulation files use private object storage. Structured records, assignments, audit events, and user actions use a transactional database. The agent tool layer is server-side only; browser clients never receive source credentials or unrestricted web-fetch capability.

Versioned formulation, supplier, and label-proof data are sensitive internal records. The first release requires organization-scoped access, role-based permissions, encryption in transit and at rest, audit logs for uploads, source queries, tool results, assignments, and exports, and retention/deletion rules. Public access, public formula sharing, automatic outward notifications, and automatic modifications to source records or regulatory obligations are out of scope. The final hosting provider, identity provider, alert delivery channel, and retention period are explicit implementation decisions, not assumptions.

## Browser Product Acceptance

- A signed-in user can ask a research question and inspect source-backed answer evidence in the browser.
- A signed-in user can view regulatory lifecycle timelines and alerts without confusing proposed, final, effective, and compliance states.
- A signed-in user can reconcile a selected label-proof text and formula version and receive findings, missing inputs, and source links without an automated compliance verdict.
- A signed-in user can inspect every alert, timeline item, and reconciliation finding through an audit trail.
- Background jobs are observable, retry safely, and do not silently promote detected changes into curated regulatory facts.

## Scope

| Corpus | Purpose | Depth |
|---|---|---|
| 21 CFR | FDA rules for beverage labeling, ingredients, nutrition and health claims, standards of identity, manufacturing, and safety | Deep |
| 7 CFR | USDA organic, bioengineered disclosure, and agricultural sourcing rules that change beverage ingredients or representations | Focused |
| 16 CFR | FTC advertising substantiation, deceptive practices, endorsements, environmental marketing, and remedies relevant to beverage marketing | Focused |

The research distinguishes binding regulation, statute, guidance, recall, warning letter, enforcement action, industry reporting, and analyst inference. A recall is not proof of a legal violation unless its notice says so.

Out of scope: Title 27, state-law surveys, label clearance, automatic edits to `regwatch`, and uncited legal propositions based only on commentary.

## Questions the Database Must Answer

1. Which 21 CFR provisions govern non-alcoholic beverage identity, labeling, nutrition, ingredients, processing, and safety?
2. What claims are permitted, qualified, prohibited, or fact-dependent?
3. Where are the gray areas in classification, standards, implied claims, ingredient characterization, sugar/sweetener, caffeine, functional ingredients, and digital marketing?
4. What has changed under the current administration, and what is proposed, final, effective, guidance, or an enforcement priority?
5. What do labeling-related recalls, warning letters, FTC cases, and agency actions reveal about common failure modes and remedies?
6. How do sourcing, supplier documents, co-manufacturing, packaging, label control, and advertising approval change exposure?

## Human-Readable Knowledge Base

Future notes go in `docs/research-database/`, one focused topic per note. Every note uses project frontmatter, including `domain`, `category`, `sub-category`, dates, `type`, `status`, `aliases`, and controlled `tags`. It also requires an **As of** date, evidence tier, sources, and Obsidian wikilinks to related notes.

Required note types are `regulation`, `topic`, `claim`, `standard`, `enforcement-pattern`, `recall`, `agency-action`, `trend`, `supply-chain-impact`, `source`, and `open-question`. Interpretive notes link to the exact controlling or supporting source note. Topic and corpus indexes provide human reading paths.

## LLM Evidence Graph

The structured corpus is outside `docs/` at `knowledge/research-database/`:

```text
knowledge/research-database/
  research-database-nodes.jsonl
  research-database-edges.jsonl
  research-database-schema.json
  research-database-manifest.json
```

Nodes have stable IDs, type, title, jurisdiction, status/effective dates, confidence, note path, summary, and source locators. Edges are directional, typed assertions with source IDs, confidence, and an `asserted_by` record. Core relations include `governs`, `defines`, `requires`, `permits`, `limits`, `prohibits`, `interprets`, `applies_to`, `substantiates`, `triggers`, `recalls`, `enforces`, `changed_by`, `affects`, `sourced_from`, `supports`, `qualifies`, and `open_question_for`.

The graph is an access layer, never a substitute for source records. Validation will reject dangling IDs, unsupported edge types, missing source links, undated current-status assertions, and legal conclusions supported only by secondary reporting.

## CFR Text Source and Retrieval Decision

The attached suggestion is useful but not accepted as a factual or architectural premise. Before implementation, PR-001 must verify the official eCFR and GovInfo download contracts, supported formats, update behavior, legal-status descriptions, source versions, API endpoints, and rate limits. The plan must not assume that a `latest` JSON endpoint, a ZIP format, or a stated file size exists until primary documentation and a test response confirm it.

If bulk text is acquired, raw snapshots belong under `sources/cfr/` and remain the audit layer. A streaming normalizer may emit section-bounded JSONL and Markdown records that preserve Title, Chapter, Part, Subpart, Section, citation, heading, issue date, source URL, and retrieval date. Raw XML or JSON is not placed wholesale in an LLM context. A current-text API, if verified, is a narrow retrieval option for a specific current part or section, not a reason to abandon durable source snapshots.

No vector database is in the initial scope. It becomes an implementation decision only after a small evaluation set compares citation-aware lexical and graph retrieval with section chunking on the primary user case. Third-party preprocessed datasets may accelerate experimentation, but they cannot be the authority or replace the source-equivalence check.

## Evidence Protocol

1. Capture issuer, document type, citation, publication/effective date, retrieval date, canonical URL, and a stable identifier or permitted snapshot.
2. Read and cite primary text before summarizing a binding rule. Use section-level anchors for section-level propositions.
3. Use Federal Register and agency records to establish a change and its status. Do not treat an announcement as a final legal change.
4. Model FDA recalls, warning letters, import actions, court actions, and FTC matters as distinct action types with distinct evidence meaning.
5. Use reputable industry news for trend discovery. Confirm any legal or enforcement fact in a primary source before adding it as a fact.
6. Preserve ambiguity as an `open-question` node containing competing readings, affected products or claims, missing facts, and a resolution source.

## Delivery Lanes

| Lane | Outcome | Depends on |
|---|---|---|
| PR-001 | Product workflow, outcome, evaluation, and data-contract decisions | None |
| PR-002 | Research library, CFR source adapter, and bounded agent-query API | PR-001 |
| PR-003 | Regulatory lifecycle, timeline, recall, and alert services built on regwatch | PR-002 |
| PR-004 | Versioned product, formulation, supplier, and label-proof reconciliation service | PR-001, PR-002 |
| PR-005 | Authenticated browser UI for research, timeline, alerts, label review, and library | PR-002, PR-003, PR-004 |
| PR-006 | Hosting, identity, authorization, auditability, job observability, and secure deployment | PR-003, PR-004, PR-005 |
| PR-007 | Cross-corpus synthesis, graph audit, browser evaluation, and rollout | PR-002, PR-003, PR-004, PR-005, PR-006 |

The detailed requirement, ownership, verification, and acceptance contract is `research-database-execution-plan.json`. Lanes are sequenced when they touch shared graph and index files, with the research-database integration owner responsible for those shared paths.

## Acceptance Criteria

- Each note is readable without graph tooling, has complete metadata and an As-of date, and links to primary sources or labels its secondary status.
- Each material rule or action has a stable source record and citation-level anchor. 21 CFR coverage is materially deeper than 7 CFR and 16 CFR.
- Every substantive graph edge resolves to source evidence and a human note.
- The initial evaluation set shows that a researcher can receive a cited research brief for each representative user question, including material unknowns and escalation boundaries.
- The CFR query tool returns citation hierarchy, exact source metadata, and a bounded result for a representative beverage question.
- The change system produces a timeline that distinguishes proposed, comment, final, effective, compliance, delay, withdrawal, and actual implementation events.
- The label/formulation feature reports discrepancies and missing inputs from deterministic fixtures without making a compliance determination.
- The browser UI supports the five primary workspaces with source, status, uncertainty, and auditability visible to an authorized user.
- The hosted deployment protects product data, performs scheduled monitoring safely, and keeps all agent-tool credentials server-side.
- The database separates current law, effective future law, proposal, guidance, enforcement signal, recall signal, and market commentary.
- The synthesis answers the six questions, identifies gray areas, and flags product-specific or legal-review boundaries.

## Risks and Decisions

- **Freshness:** time-sensitive records need retrieval dates and a future refresh owner. Historical records must not overwrite current status.
- **Classification:** product category and implied-claim analysis may depend on facts unavailable in public sources. Model uncertainty rather than infer it.
- **Source quality:** primary sources support legal propositions. Industry sources support trend context or discovery only until corroborated.
- **Architecture:** bulk ingestion, section normalization, live API retrieval, and retrieval indexing solve different problems. Each is gated on verified source behavior and measured answer quality, not on an assumption that more text improves answers.
- **Hosted-data exposure:** formulation and label proofs are sensitive. The browser product must default to authenticated, organization-scoped access and explicit auditability before feature breadth.
- **Decision required before PR-004:** define recent actions and recalls. The proposed default is 24 months, while retaining older pattern-setting matters if clearly labeled.

## Plan Verification

- Validate `research-database-execution-plan.json` with the harness `plan-to-prs` validator.
- Render `research-database-execution-plan.md` from the JSON contract and confirm it has no drift.
- Run `make audit-strict` for this plan's Markdown conventions.

## Canonical References

- `docs/plans/plans-README.md`
- `docs/plans/deliverable-3-regulatory-monitoring-design.md`
- `/Users/kevinlappe/Projects/harness/scaffolding/project-routing-spec.md`, Routing Principles and Records and Source-Corpus Overlay
- `/Users/kevinlappe/.codex/skills/plan-to-prs/SKILL.md`
