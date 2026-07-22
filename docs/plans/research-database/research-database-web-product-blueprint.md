---
domain: regulatory-ingredients-labels-laws
category: plan
sub-category: web-product
date-created: 2026-07-22
date-revised: 2026-07-22
type: product-blueprint
version: 0.1.0
status: DRAFT
aliases:
  - beverage regulatory intelligence web product
  - regulatory intelligence product blueprint
tags:
  - alerts
  - authentication
  - beverage
  - design-system
  - financial-model
  - launch
  - web-product
---

# research-database-web-product-blueprint

## Product Thesis

The product is an authenticated beverage regulatory intelligence workspace. It gives product, marketing, and regulatory teams one evidence-backed place to investigate a decision, track a regulatory lifecycle, respond to recalls and alerts, and reconcile a label proof with a versioned formulation. The research library is the durable source layer. The browser experience makes that library usable at the point of a decision.

The product does not approve labels or provide legal advice. Its advantage is disciplined evidence handling: it shows the rule, source, date, confidence, product facts still needed, and required human escalation rather than pretending certainty.

## Users and Goals

| User | Job | Goal | Product Capability | Success Signal |
|---|---|---|---|---|
| Regulatory researcher | Investigate a product or policy question | Produce a trustworthy research brief quickly | CFR agent query, source detail, linked beverage knowledge | Can explain the answer and its limits with sources |
| Product developer | Assess a formula or supplier change | Find facts and review needs before a label is drafted | Product profile, formulation version, ingredient knowledge | Identifies missing supplier or formula inputs early |
| Marketing lead | Explore a claim or campaign | See likely regulatory context and escalation points | Claim research, FTC context, action patterns | Does not route a high-risk claim forward without review |
| Label reviewer | Reconcile a proof | Find factual mismatches and missing information | Proof upload, text verification, formula comparison, review packet | Receives deterministic findings without a false approval |
| Compliance lead | Prioritize changes and recalls | See what needs action and who owns it | Timeline, alert inbox, assignments, audit log | No material alert is lost or silently changed |
| Workspace administrator | Protect organizational data | Manage access, retention, and auditability | Sign-in, organization, member, role, and audit settings | Can show who accessed sensitive records |

## Feature Map

| Feature | Capability | Benefit | Primary Use Case |
|---|---|---|---|
| Sign-in and organization | SSO or passwordless sign-in, membership, roles, sessions | Protect formulas and proofs | User enters an organization-scoped workspace |
| Account and profile | Profile, time zone, notification preferences, active organization | Personalizes but does not broaden authority | User controls notification channels |
| Research workspace | Citation-aware questions, scoped agent tools, source preview, saved briefs | Turns research into a repeatable evidence package | “What applies to this beverage claim?” |
| Search and saved research | Keyword, phrase, date, company, action, and source filters plus saved searches, collections, and briefs | Lets users find, resume, and share evidence without repeating work | “Show recent warning letters about this company or claim” |
| CFR source detail | Hierarchy, current or dated text, version, retrieval time, related notes | Keeps legal context with a citation | User opens a cited section and sees its parent context |
| Timeline | Proposal, comment, final, effective, compliance, implementation, delay, withdrawal events | Makes regulatory timing actionable | User sees a comment deadline and later actual rule state |
| Alerts inbox | Severity, assignment, acknowledgement, source link, snooze with reason, history | Prevents dropped change or recall work | Compliance lead triages new recall and assigns an owner |
| Beverage intelligence | Ingredient function, claim, product, warning-letter, recall, and trend relationships | Grounds generic law in beverage practice | User sees related sweetener, color, or caffeine context |
| Label review | Proof text, formulation version, source checks, discrepancy states, export | Finds factual gaps before human clearance | Reviewer compares ingredient statement to formula |
| Library | Browsable notes, sources, actions, recalls, graph-linked related material | Supports deep learning and audit | New researcher learns a topic without a query |
| Administration | Members, roles, data retention, integrations, audit export | Enables safe operation | Admin removes member access and reviews exports |

## Key User Flows

### Research a Claim

1. User signs in and selects the active organization.
2. User enters a question, product context, proposed claim, and known ingredients.
3. The server invokes bounded research tools and returns a brief with sources, status, unknown facts, related beverage knowledge, and escalation guidance.
4. User opens source detail or saves the brief to a product or alert.
5. User marks the brief as reviewed or routes it to a legal reviewer. The audit log records the result and sources used.

### Search and Save Research

1. User opens global search and enters a key term, exact phrase, CFR citation, company, product, or action identifier.
2. User narrows results with facets for date range, Title, CFR part or section, company, source agency, warning letter, recall, action type, timeline state, topic, ingredient, claim, and confidence.
3. The result card shows matching evidence, source date, current status, citation, and why the record matched.
4. User saves the query and filter set, bookmarks individual records, or stores a research brief in a named collection.
5. The saved item records its owner, organization visibility, source/version snapshot, retrieval date, and later refresh state. The user can resume, duplicate, export, or share it only within their authorized workspace scope.

### Act on a Regulatory Change

1. A worker detects a source change and creates an unconfirmed candidate.
2. A reviewer confirms classification and the system creates or updates a timeline event without overwriting curated rules automatically.
3. Eligible users receive an in-app alert with source and deadline context.
4. The assignee acknowledges, investigates, links a product or claim, and records the outcome.
5. The timeline preserves proposal and actual events, including the comment period and implementation dates.

### Review a Label Proof

1. User creates or selects a product and a versioned formulation.
2. User uploads a label proof or enters verified proof text and identifies the proof version.
3. The system compares declared ingredients, ordering basis, subingredients, carriers, claims, and known product attributes to the selected inputs.
4. The result lists consistent fields, discrepancies, missing input, source checks, and legal-review flags.
5. User exports a review packet or assigns a finding. No result can be labeled approved or compliant.

## Information Architecture

```text
Workspace
  Home
  Search (results, saved searches, collections, bookmarks)
  Research
    New research brief
    Saved briefs
    CFR source detail
  Monitor
    Timeline
    Alerts
    Recalls and actions
  Product Review
    Products
    Formulations
    Supplier specifications
    Label proofs
    Reconciliation packets
  Library
    Topics and claims
    Standards and CFR
    Sources
    Beverage patterns
  Settings
    Profile and notifications
    Organization and members
    Roles and audit log
    Data and integrations
```

## Design Direction

The visual direction is a **regulatory fieldbook**: an exacting working instrument, not a generic analytics dashboard or a legal newssite. The signature element is an evidence rail that appears beside every research brief, alert, timeline event, and reconciliation finding. It visibly connects the conclusion to the source, source date, current status, and unresolved facts. This makes provenance a primary interaction rather than a hidden footer.

The interface uses spacious reading surfaces for evidence, compact data tables for monitoring, and a high-contrast timeline spine for regulatory sequence. Motion is reserved for a single useful moment: the evidence rail expands from a finding to reveal the source chain. Reduced motion renders the same relationship without animation.

## Tokenized Design System

| Token Group | Tokens | Purpose |
|---|---|---|
| Color | `color-ink-950 #102A43`, `color-slate-700 #486581`, `color-paper-50 #F8FAFC`, `color-source-700 #075985`, `color-watch-700 #B45309`, `color-critical-700 #B42318`, `color-success-700 #027A48`, `color-focus-600 #6D28D9` | Readable evidence, status, and accessible interaction states |
| Typography | `font-display Newsreader`, `font-body IBM Plex Sans`, `font-data IBM Plex Mono` | Distinctive source reading, workmanlike UI, stable citations and dates |
| Type Scale | `text-display 36/42`, `text-title 24/30`, `text-section 18/24`, `text-body 16/24`, `text-meta 13/18`, `text-data 13/18` | Reading hierarchy without dashboard clutter |
| Space | `space-1 4px`, `space-2 8px`, `space-3 12px`, `space-4 16px`, `space-6 24px`, `space-8 32px`, `space-12 48px` | Consistent rhythm |
| Shape | `radius-control 6px`, `radius-panel 10px`, `border-subtle 1px`, `shadow-overlay` | Calm, credible surfaces |
| Layout | `content-reading 760px`, `content-workspace 1440px`, `rail-evidence 320px`, `nav-side 248px` | Evidence-first responsive structure |
| Motion | `motion-fast 120ms`, `motion-standard 180ms`, `motion-reduced 0ms` | Deliberate and accessible feedback |

The implementation system is MUI Core plus MUI X Data Grid. MUI supplies the accessible application shell, navigation, forms, dialogs, date controls, theming, and timeline component. MUI X supplies the dense, keyboard-accessible grid and filtering behavior needed for alerts, recalls, searches, and reconciliation findings. The team will use documented components before creating custom equivalents. A licensing decision is required before relying on premium grid features such as advanced grouping or export.

Core components are app shell, side navigation, command/search field, source citation, evidence rail, status chip, lifecycle timeline, alert row, data table, review finding, version selector, file-upload state, assignment control, audit-event list, empty state, error state, and confirmation dialog. All components require keyboard navigation, visible focus, semantic labels, responsive behavior, and non-color status cues.

Search starts with deterministic keyword, exact-phrase, citation, and field filtering across curated evidence and metadata. It stores the query grammar and result snapshot separately from the user’s saved item. Semantic or vector retrieval is optional and must be labeled as an assistive expansion, never a replacement for field filters, source citations, or deterministic recall of a warning letter, recall, company, or date.

## System Design Blueprint

```text
Browser UI
  -> Authenticated application API
     -> Research and CFR query service
     -> Product and reconciliation service
     -> Timeline and alert service
     -> Library and graph service
     -> Organization, account, and audit service
  -> Transactional database
  -> Search index for metadata, text, citations, dates, companies, actions, and saved-research records
  -> Private object storage for source snapshots and uploaded proofs
  -> Search and retrieval index only if evaluation proves it improves answers
  -> Background workers for polling, normalization, timelines, alerts, reports
  -> Observability for logs, metrics, traces, job health, and security events
```

The API is the single policy boundary. It validates organization membership and role before every read, write, upload, export, or tool invocation. Agent tools run server-side with scoped request parameters, source allowlists, timeouts, rate limits, structured outputs, and invocation audit records. Source acquisition and label text extraction run as background jobs with idempotency keys, retries, dead-letter handling, and human-visible failure status.

A saved-research record has a stable ID, owner, organization ID, visibility, query or brief input, normalized filters, result/source snapshot IDs, creation and refresh dates, collection membership, tags, and audit history. Personal saved research is private by default. Shared collections require an explicit organization-scoped permission and never cross organization boundaries.

## Roles and Authorization

| Role | Research | Alerts | Product Data | Administration |
|---|---|---|---|---|
| Member | Create and read permitted briefs | Read and acknowledge assigned alerts | Read assigned products and reviews | Manage own profile |
| Reviewer | All member capabilities | Triage and assign alerts | Create review packets and findings | No organization administration |
| Regulatory Lead | Confirm curated monitoring records | Configure alert rules and close alerts | View all organization product data | Read audit logs |
| Administrator | Read operational data as permitted | Manage integrations | Manage retention and exports | Manage members, roles, and organization settings |

Role design must follow least privilege. Legal-review outcomes are recorded as human decisions with reviewer identity and source references, not produced by an agent tool.

## Cloud Services and Setup Sequence

The provider decision is deferred, but the service inventory is not. The final design maps each category to AWS or GCP without changing the application contracts.

| Service Category | Purpose | AWS Candidate | GCP Candidate |
|---|---|---|---|
| Organization and accounts | Isolate environments, billing, and access | AWS Organizations and IAM Identity Center | Cloud Organization and Cloud Identity |
| Private network and edge | Segmentation, ingress, WAF, TLS | VPC, ALB, WAF, CloudFront | VPC, Load Balancer, Cloud Armor, Cloud CDN |
| Application runtime | Run browser backend, API, and worker services | ECS Fargate or App Runner | Cloud Run |
| Container registry | Signed deployable artifacts | ECR | Artifact Registry |
| Transactional database | Organization, product, alert, and audit records | RDS PostgreSQL | Cloud SQL for PostgreSQL |
| Object storage | Private sources, uploads, exports, backups | S3 | Cloud Storage |
| Queue and scheduler | Ingestion, OCR, alerts, retries, dead letters | SQS, EventBridge, Step Functions | Pub/Sub, Cloud Scheduler, Workflows |
| Search | Deterministic text and facet search | OpenSearch or PostgreSQL search at pilot scale | Vertex AI Search or PostgreSQL search at pilot scale |
| Secrets and encryption | Credentials, keys, encryption policy | Secrets Manager and KMS | Secret Manager and Cloud KMS |
| Observability | Logs, metrics, traces, job and security health | CloudWatch and X-Ray | Cloud Logging, Monitoring, Trace |
| Delivery and security | CI, artifact scanning, policy checks, infrastructure change | GitHub Actions plus AWS policy controls | GitHub Actions plus Google policy controls |
| DNS and email | Domain, TLS, transaction and alert delivery | Route 53 and SES | Cloud DNS and email provider decision |

Setup order is: establish separate development, staging, and production accounts or projects; configure identity, least-privilege roles, billing alerts, and audit logging; create private networking and encrypted data services; provision database, storage, queue, and secrets; deploy container registry and application runtime; add observability and backup/restore; configure CI/CD and infrastructure as code; then configure DNS, certificates, WAF, and production alert delivery. No production service is created manually outside reviewed infrastructure as code.

## Code Quality and Delivery System

The repository needs a quality contract before web implementation. Every change runs formatting, linting, type checking, unit tests, API contract tests, data-schema validation, accessibility tests, component tests, browser end-to-end tests, and security checks appropriate to the path changed. The delivery pipeline also runs secret scanning, dependency and license scanning, static analysis, software bill of materials generation, infrastructure policy validation, container image scanning, migration checks, and audit-log contract tests.

Quality gates are layered: local fast checks, pull-request checks, merged staging integration, hosted security and authorization checks, backup/restore drill, and production promotion. A browser release requires visual regression review for dense data states, keyboard and screen-reader verification for critical flows, performance budgets for search and timeline views, and an explicit rollback artifact. Code owners review security, data model, design system, and infrastructure changes. Generated clients, schemas, and design tokens require regeneration and drift checks.

## Comparative Research and Design Implications

The information architecture is based on reviewed products, not an abstract dashboard template. eCFR offers citation-first reading and version-aware regulation access, but is dense and not beverage-specific. Federal Register provides strong search and rule-type distinction, but does not unite the docket lifecycle, CFR impact, portfolio, or label workflow. Regology and RegScan demonstrate monitored sources, saved research, profiles, alerts, comparisons, and ownership, while TraceGains, ENTR, Esko WebCenter, and FoodChain ID demonstrate product, supplier, proofing, and review patterns.

The resulting product combines those strengths in one navigation model: command search, regulatory intelligence, change radar, beverage knowledge, product compliance workspace, market safety, saved work, and administration. Every result is an evidence card with requirement, evidence inspected, gap, risk, owner, action, and review state. This deliberately fixes government-site weaknesses: browse-first navigation, opaque lifecycle state, disconnected comment periods, and no path from a rule to a product, label proof, or owner.

References: [eCFR](https://www.ecfr.gov/), [Federal Register](https://www.federalregister.gov/), [Regology](https://www.regology.com/platform), [RegScan FLEX](https://www.regscan.com/products/regscan-flex/), [TraceGains Compliance](https://tracegains.com/compliance/), [ENTR](https://www.entrtechnologies.com/platform), [Esko WebCenter](https://www.esko.com/en/products/webcenter), [MUI Data Grid](https://mui.com/x/react-data-grid/accessibility/), and [MUI Theming](https://mui.com/material-ui/customization/theming/).

## Hosting, Domain, and DNS Decision Gate

AWS and GCP are both viable candidates. The plan does not select one before a decision record compares identity integration, private networking, managed database and object storage, worker scheduling, observability, region/compliance needs, operational skill, and the cost model. The provider choice blocks production infrastructure only, not the contracts, research library, browser prototype, or provider-neutral service boundaries.

The domain remains TBD. Before launch, the owner chooses a registrar, records domain ownership and renewal contacts, configures DNS in infrastructure as code, enables HTTPS, configures email authentication if email alerts are used, and documents DNS rollback. Production deployment requires separate development, staging, and production environments plus a domain and certificate verification gate.

## Financial Model

The cost model has three scenarios, not one premature number: **foundation**, **internal pilot**, and **scaled workspace**. Each scenario calculates monthly operating cost as:

```text
cloud = web + API + worker compute + database + private storage + backups + egress + search + observability + identity + email/SMS + AI or model usage + support
total cost = cloud + people + security/compliance + vendor contracts + contingency
```

The model records monthly active users, query volume, source polling frequency, stored proof and source volume, retention period, alert volume, expected model tokens, support hours, and loaded engineering/design/product costs. It reports fixed versus variable cost, cost per active organization, cost per research brief, cost per reconciliation, and the break-even or budget threshold for each scenario. Numeric estimates must use the chosen provider’s current calculator and signed vendor quotes. Until AWS versus GCP, domain, identity, and model-provider decisions are made, dollar totals are unverified and must not be presented as forecasts.

## Launch Plan

| Stage | Scope | Exit Gate |
|---|---|---|
| Discovery | Interview representative users, finalize scenarios, test information architecture and proof-review flow | Evidence that the primary workflows match real decisions |
| Internal Alpha | Research library, read-only CFR query, timeline, and alert browser flows for a small internal group | Source citations, authentication, audit logging, and workflow usability pass |
| Controlled Pilot | Add product/formulation/proof reconciliation for named pilot users and private data | Reconciliation fixtures, access controls, monitoring, and human-review process pass |
| Production Readiness | Select cloud, domain, DNS, operations runbook, cost baseline, backups, security review, and rollback | Staging behavior and hosted security gates pass |
| General Availability | Expand eligible organization members and enable governed alerts | Usage, reliability, source-quality, and support gates remain within agreed thresholds |

Launch requires an owner for incidents, source quality, data retention, access reviews, alert operations, customer or internal support, cost monitoring, and release approval. Rollback disables the affected browser release or worker route without deleting immutable audit evidence or source snapshots.

## Adversarial Questions Before Build

- Which decision would a user make differently because of this product, and how will we observe that?
- What source contract proves that current CFR text, historic text, and lifecycle status are not conflated?
- Which inputs are required before label reconciliation can make a factual comparison?
- How does the system prevent an LLM from inventing a citation, an effective date, or a compliance conclusion?
- What happens when a source poll, document parse, alert delivery, or text extraction fails?
- Can one organization ever infer another organization’s products, formula names, or source-query history?
- What concrete usage or accuracy signal would cause us to stop investing in vector retrieval, agent tools, or a particular cloud provider?

## Decision Register

| Decision | Owner | Evidence Needed | Blocks |
|---|---|---|---|
| AWS or GCP | Product and platform leads | Decision matrix and current cost calculator | Production hosting |
| Domain and registrar | Product owner | Ownership, renewal, DNS, certificate plan | Production URL and email |
| Identity provider | Platform lead | Organization, SSO, role, and audit requirements | Authenticated pilot |
| Model and retrieval approach | Research and engineering leads | Evaluation-scenario quality, source traceability, cost | Agent query scale-up |
| Alert channels | Compliance lead | Recipient, escalation, retention, and audit needs | Production alerts |
| Data retention policy | Administrator and legal owner | Data classification and deletion requirements | Production private uploads |
