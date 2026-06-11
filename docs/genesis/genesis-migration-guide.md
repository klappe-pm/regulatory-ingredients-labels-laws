# Genesis Foods Master Study Guide

### Internal Training Materials — Prepared for DIANE Tran, Compliance Analyst, Beverage Manufacturing

*Last updated: June 2026*

-----

## How to Use This Guide

Welcome, DIANE Tran. This guide is your complete onboarding resource for **Genesis Foods** (Trustwell’s web-based formulation and labeling platform, formerly ESHA’s Genesis R&D). It is organized so DIANE Tran can work through it in order — from history and platform context, through every functional module, into beverage-specific labeling, GMP/HACCP alignment, and finally the day-to-day compliance analyst workflow. Each section ends with “Check Yourself” questions for self-study.

-----

## Section 1: Program History & Company Background

| Era         | Product / Event                                                                                                                                                                                        |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ~1990s–2023 | **ESHA Research** builds Genesis R&D (“Genesis Classic”), the industry’s first nutrition labeling software, a Windows desktop application backed by SQL Server and a gold-standard nutrition database. |
| 2023        | ESHA Research and **FoodLogiQ** (supply chain/traceability software) merge under a new brand: **Trustwell**. The combined offering is the “Trustwell Connect” platform.                                |
| April 2023  | Trustwell launches the **next generation of Genesis Foods** — a cloud/web-based rebuild of Genesis R&D with a modern UI, built-in data checks, and allergen alerts.                                    |
| 2024–2026   | Quarterly release cadence adds international authorities, AI features (AskReg), versioning/approvals, and migration tooling to move Classic customers to the web platform.                             |

**Key takeaway for DIANE Tran:** When colleagues say “Genesis,” they may mean either **Genesis Classic / Genesis R&D** (the legacy desktop app, version 11.x) or **Genesis Foods** (the current web platform). Always clarify which one. Our company’s future state is the web platform.

**Check Yourself**

1. What two companies merged to form Trustwell?
2. What is the difference between Genesis R&D/Classic and Genesis Foods?

-----

## Section 2: The Migration to the Web Platform (Classic → Genesis Foods)

This is the single most important organizational change to understand.

### 2.1 Why Trustwell migrated to the web

- **Single cloud platform:** real-time updates, no local SQL Server administration, no version patching by IT.
- **Modern UX:** streamlined formulation and data entry, dashboard-driven navigation.
- **Built-in compliance:** automated nutrition data checks and allergen alerts at the point of entry.
- **AI assistance:** AskReg and AI data extraction are only available on the web platform.
- **Connected ecosystem:** Genesis Foods pushes approved formulations into FoodLogiQ Product Management for living specifications shared with suppliers and FSQA teams.

### 2.2 The migration process (what actually happens)

1. **Database handoff.** For cloud-hosted Classic customers, Trustwell Support pulls the database directly. For locally installed customers, the company provides a database backup to a secured drop location.
2. **Preview Environment.** Trustwell migrates a *copy* of the data into a Genesis Foods **Preview environment**. This is the validation sandbox.
3. **Data validation.** The customer’s team reviews migrated ingredients, recipes, and labels in Preview to confirm everything still meets regulatory compliance standards — this is the compliance analyst’s job and a perfect rehearsal for DIANE Tran.
4. **Scheduling final migration.** The customer books a Production migration date (via a Calendly link; reschedules go through [migration@trustwell.com](mailto:migration@trustwell.com)).
5. **Cutover.** After moving to Production, **work must stop in Genesis Classic**. Anything created in Classic afterward is the user’s responsibility to manually re-create in Genesis Foods.
6. **30-day Classic access.** Users retain read access to Classic data for up to 30 days after the Production move.

### 2.3 Security & trust

- Trustwell provides a **SOC 2 Type 2** report on request — useful for our vendor-qualification and audit files.

### 2.4 Migration validation checklist for DIANE Tran

- [ ] Spot-check custom (user-added) ingredients: nutrient values, allergens, ingredient statements.
- [ ] Verify recipe yields, serving sizes, and moisture/fat loss adjustments survived migration.
- [ ] Re-generate key beverage labels and compare against approved Classic label artwork.
- [ ] Confirm audit trail expectations and document the validation as a controlled record (supports GMP documentation requirements).
- [ ] Confirm all team members have correct roles before cutover.

**Check Yourself**

1. What is the Preview environment for, and what should be validated there?
2. How long do users keep access to Classic data after cutover?
3. Can teams keep working in Classic after moving to Production? What’s the risk?

-----

## Section 3: Product Roadmap, Announcements & Release Timeline

Genesis Foods ships on a roughly quarterly cadence. Knowing this timeline lets DIANE Tran speak to “what the platform can do now” versus “what’s coming.”

### 3.1 Major announcements

- **April 2023 — Next-gen Genesis Foods launch.** Streamlined UI, built-in nutrition data checks, allergen alerts; launch event/webinar introduced versioning and formulation management.
- **Spring 2024.** Canada and Mexico label authorities (bilingual English/French Canada labels, Spanish Mexico labels, Mexico rounding rules), Australia/New Zealand Nutrient Fact Panels with mandatory ingredient-level allergen declarations, pre-selected Authorities in user preferences, and the **three user roles** (Admin/Editor/Viewer).
- **Q4 2024 (announced Jan 2025).** AI-driven **Allergen Identification** powered by AskReg — analyzes custom ingredient data and flags potential allergens even under alternative names or derivatives (e.g., enriched wheat flour in a sub-ingredient triggering a gluten/wheat flag). Enhanced recipe management workflows.
- **Q1 2025.** **Canada front-of-package (FOP) symbols**, **Allergen Origins** tab, bilingual EU support.
- **April 2025.** **AskReg sold as a standalone product** — online purchase, two subscription tiers; natural-language regulatory Q&A with citation-backed answers for U.S., Canadian, and global markets.
- **Q2 2025.** **Preview Labels** (watermarked draft labels and packaging reports), **AskReg restricted-additive monitoring** (scans the ingredient database and flags additives restricted by the selected authority, with dashboard alerts and deep links to documentation), expanded collaboration tools.
- **July 2025.** FDA allergen guidance (Edition 5) implemented: revised tree-nut list (coconut and 11 others removed as designations), animal-source naming for non-cow milk (Cow, Goat, Sheep, Buffalo, Camel added) and non-chicken egg; Trustwell database vs. user-ingredient search toggle; Item Codes shown across search, formulation tables, and ingredient records.
- **Q4 2025.** **Food Comparison Report** — born from Classic’s menu-label reports (FDA menu labeling for chains of 20+ locations) and rebuilt as an R&D comparison/analysis tool. Also an **HFSS calculator** (UK High Fat Salt Sugar scoring) with reports for internal review or partner compliance.
- **January/Q1 2026.** **Trustwell Advisor** (embedded AI: highlight any text in the app → “Ask About This” → real-time explanations and regulatory references), **AI ingredient spec-sheet extraction** (upload a supplier spec sheet, AI populates the ingredient record, attaches the source PDF; human confirms allergens and approves), **Custom Attributes** (beyond the 14 standard attributes like bioengineered/vegan/gluten-free — visible on ingredients, recipes, packaging assets, and Nutrient Spec Sheet reports), improved Label search modal (multi-criteria filtering, multi-recipe add for dual/aggregate labels), and the **U.S. Dual Column Tabular** label format for small packages.

### 3.2 Trustwell’s “best of 2025” themes (their own retrospective)

Streamlined compliance, ingredient management, labeling accuracy, AskReg expansion (allergen suggestions + restricted-substance scanning), Find and Replace across recipes, and Canada FOP support.

### 3.3 Roadmap direction to watch

- Deeper **Genesis Foods ↔ FoodLogiQ** integration: pushing approved formulations into FoodLogiQ Product Management as living specifications; FoodLogiQ Q3 2025 added synchronized nutrition data and scoped API tokens.
- Continued AI investment (AskReg, Advisor, extraction) with **human-in-the-loop approval retained** — final ingredient approval always stays with the user.

**Check Yourself**

1. Name three AI capabilities in Genesis Foods and what each does.
2. Which release added Canada FOP symbols? Why does that matter for a beverage sold in Canada?
3. What is the Food Comparison Report and what two use cases does it serve?

-----

## Section 4: Core Modules & Features (Deep Dive)

Genesis Foods is organized around six functional areas: **Ingredients, Recipes, Labels, Reports, AI Features, and Administration/Access**.

### 4.1 Ingredients — the foundation

- **Trustwell database:** 90,000+ ingredients sourced from FDA, Health Canada, UK FSA, and vetted manufacturers/suppliers. Database items are always in an approved state and carry a unique **Item Code**.
- **User-added (custom) ingredients:** built from supplier spec sheets or lab analyses. Required: nutrient data, allergens, ingredient statement. As of 2026, AI extraction can populate these from an uploaded spec sheet; the sheet is stored in Attachments, and the user must still confirm allergens and approve.
- **Search:** toggle between *your* ingredients and the Trustwell database; Advanced Search with filters (Draft/Approved/Archived for user items).
- **Copy vs. Version:** *Copy* creates a brand-new record at Version 1 Draft with a **blank audit trail** (used to take a database ingredient and make an editable company copy). *Versioning* preserves history on the same record.
- **Aliases, Tags, User Codes:** tags are free-form company conventions (e.g., “TN” for tree nuts) for search/sorting.
- **Attributes:** 14 standard attributes (bioengineered, vegan, gluten-free, etc.) plus **Custom Attributes** for anything else the business tracks (e.g., Non-GMO, kosher status, organic certification) — these flow to recipes, packaging assets, and spec-sheet reports.
- **AskReg additive monitoring:** flags banned/restricted additives by authority directly on the dashboard and ingredient pages. For beverages, think of color additives, preservatives (e.g., benzoates), and sweeteners that differ by market.

### 4.2 Recipes — formulation & analysis

- Virtual formulation: add/adjust ingredients and yields; nutrition recalculates instantly — no lab round-trips for iteration.
- Smart prompts ensure required fields are completed as you work.
- **Allergens section** with two tabs: **Allergen Statement** (what prints) and **Allergen Origins** (which ingredient contributes which allergen — a traceability view for root-causing allergen declarations).
- **Versioning & Approvals:** Draft → review → **Approved**. Approval assigns a version number, stamps date/time, and **locks the record**. Editing later prompts a new review/approval and saves a new version alongside the old, so historical formulas remain comparable.
- **Find and Replace:** swap one ingredient for another across the current version of every recipe that contains it, with side-by-side comparison and allergen flagging — critical during sourcing disruptions or allergen-driven reformulation, and it maintains the audit trail.
- **Food Comparison Report:** compare nutrition across multiple recipes/versions (e.g., DIANE Tran comparing three sweetener systems for a tea line, or building menu-board data).

### 4.3 Labels — the compliance output

- **Authorities supported:** U.S. (FDA), Canada (bilingual, FOP symbols, Supplemented Foods), Mexico (Spanish, custom rounding), EU (bilingual support), Australia/New Zealand. Pre-select your organization’s Authorities in preferences to declutter nutrient lists.
- **Formats:** Standard, Simplified (when 7+ mandatory nutrients are insignificant — common for waters and some zero-cal beverages), Dual Column (package 200–300% of RACC), **Dual Column Tabular** (small packages), Tabular/Linear, dual/aggregate labels built from multiple recipes, Infant/Child/Pregnant-Lactating DV profiles.
- **Built-in checks:** government-compliant rounding and %DV math, allergen declaration checks, alerts (e.g., Canada caffeine thresholds for confectionery; Health Canada cautionary statements).
- **Preview Labels:** watermarked “draft” labels and packaging reports for circulating pre-approval versions to marketing/regulatory without risk of a draft being mistaken for final.
- **Label search modal (2026):** filter recipes by multiple criteria; add multiple recipes at once to dual/aggregate formats.

### 4.4 Reports

- Nutrient Spec Sheets (now including Custom Attributes), packaging asset reports, Food Comparison Reports, HFSS reports, and change-tracking outputs. Viewers can generate and download all reports.

### 4.5 AI Features (summary table)

|Feature                       |What it does                                                                                               |Human control point                                |
|------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------|
|AskReg (chatbot)              |Natural-language regulatory Q&A with citations; U.S., Canada, global                                       |User judges applicability                          |
|AskReg Allergen Identification|Flags potential allergens in custom ingredients, including alternative names/derivatives in sub-ingredients|User confirms/edits allergen declarations          |
|AskReg Restricted Additives   |Scans ingredient DB for additives restricted by the selected authority                                     |User reviews flags with linked documentation       |
|AI Spec-Sheet Extraction      |Populates ingredient records from uploaded supplier spec sheets                                            |User confirms allergens, completes fields, approves|
|Trustwell Advisor             |Highlight text anywhere → “Ask About This” → contextual explanations, validation, reference links          |Advisory only                                      |

### 4.6 Administration & Access

Covered in depth in Section 7.

**Check Yourself**

1. What’s the difference between Copying and Versioning an ingredient?
2. What does the Allergen Origins tab show, and how is it different from the Allergen Statement tab?
3. When would DIANE Tran use a Preview (watermarked) label?

-----

## Section 5: Beverage Labeling in Genesis Foods

Beverages have a distinct regulatory profile. Here is how the program’s features map to it.

### 5.1 Serving size / RACC

- The RACC for most non-alcoholic beverages is **240 mL (8 fl oz)**. Genesis applies RACC-driven serving logic and format eligibility.
- **Single-serving rule:** a container under 200% of the RACC reasonably consumed in one sitting (e.g., a 355 mL/12 oz can) may be declared one serving. Containers between **200–300% of RACC require Dual Column** labels (per-serving + per-container) — Genesis selects/supports these formats. A common FDA violation in functional beverages is declaring a 16 oz bottle as one serving when the RACC math requires two; Genesis’s format logic helps DIANE Tran catch this.
- Serving sizes can be displayed in mL; metric declarations matter for export markets.

### 5.2 Juice percentage declaration (21 CFR 101.30)

- Any beverage that *purports* to contain fruit/vegetable juice (name, vignette, flavor/color suggesting juice) must declare total % juice (“Contains __% juice”). Less than 1% is declared as “less than 1% juice.” Track this as a label statement on juice-adjacent products.

### 5.3 Caffeine & energy/functional drinks

- U.S.: caffeine is **not** a Nutrition Facts nutrient, but industry practice (and energy-drink voluntary guidelines) is a separate quantitative declaration (mg per serving and per container) plus advisory statements. Manage these as custom label statements.
- **Canada Supplemented Foods:** Genesis added Canada Supplemented Foods labels, supplemented-ingredient handling, **Health Canada Cautionary Statements**, supplemental vitamins/minerals/amino acids, and **caffeine** support — including threshold alerts (e.g., max caffeine alerts for certain categories). This is the module for caffeinated energy drinks and vitamin waters sold in Canada.
- **Canada FOP:** symbols required when sodium, saturated fat, or sugars exceed 15% DV (10% or 30% in some reference-amount/main-dish cases). For sweetened beverages, **sugars** is the trigger to watch. Genesis lets users set reference amount, orientation (horizontal/vertical), size, and language (EN/FR combinations), and preview/download the symbol.

### 5.4 Sugar, claims, and reformulation

- Added sugars: juice concentrates, honey, agave used as sweeteners count as added sugars — “no sugar added” claims fail if present. Claims math is evaluated against the RACC, not a manipulated serving.
- “Low calorie” (≤40 cal per 240 mL) / “calorie free” (<5 cal) thresholds — Genesis’s nutrient math against the RACC supports claim substantiation.
- The **HFSS calculator** matters if our beverages enter the UK market (promotion/placement restrictions for high-sugar drinks).
- **Simplified format** frequently applies to waters/seltzers with insignificant nutrients.

### 5.5 Beverage allergens

- Less obvious beverage allergen sources: milk derivatives in creamers/protein drinks, soy lecithin, barley malt, tree-nut milks, fish gelatin/isinglass fining agents. AskReg Allergen Identification + the Allergen Origins tab are DIANE Tran’s tools to trace these to the contributing ingredient.

**Check Yourself**

1. A 16 fl oz tea has a 240 mL RACC. How many servings must the label declare, and what format question does that raise?
2. Which Genesis module handles a caffeinated energy drink for the Canadian market?
3. What FOP nutrient is most likely to trigger a Canadian symbol on a sweetened beverage?

-----

## Section 6: How Genesis Fits GMP and HACCP

Genesis Foods is a **formulation/labeling and product-data system**, not a full QMS — but it directly supports several GMP (21 CFR 117 cGMP) and HACCP program elements:

|GMP/HACCP element                                  |How Genesis supports it                                                                                                                                                                                                                                 |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**Hazard analysis — allergens (a chemical hazard)**|Allergen declarations per ingredient, Allergen Origins traceability, AskReg flagging of hidden/derivative allergens. Undeclared allergens are the #1 U.S. recall cause; label accuracy is an allergen preventive control.                               |
|**Ingredient specifications & supplier controls**  |Custom ingredient records built from supplier spec sheets, with the spec sheet attached to the record; Item Codes/User Codes; restricted-additive monitoring per authority.                                                                             |
|**Formulation control / master records**           |Approved, version-locked recipes act as the controlled master formula; changes force re-review and new versions.                                                                                                                                        |
|**Document control & change management**           |Draft → Approved workflow, version numbers, date/time stamps, locked approved records, audit trail of who changed what and when (with comments). In Classic, the Audit Trail must be manually enabled; once on, every save records date/time/user.      |
|**Recordkeeping for audits**                       |Historical versions retained side-by-side; spec-sheet reports; SOC 2 Type 2 vendor assurance for our own supplier-qualification file on Trustwell.                                                                                                      |
|**Recall/withdrawal readiness**                    |Find and Replace + Allergen Origins speed impact assessment (“every recipe containing ingredient X”) during sourcing disruptions or recalls; FoodLogiQ extends this to supplier traceability and recall management.                                     |
|**What Genesis does NOT do**                       |CCP monitoring (e.g., pasteurization temps, pH for acidified beverages), sanitation records, environmental monitoring, batch records. Those live in our plant QMS/HACCP plan. Genesis feeds the *label and formula truth* that those programs depend on.|

**Framing for DIANE Tran:** think of Genesis as the system of record for *what the product is and what the label must say* — the front half of HACCP (hazard identification for allergens/ingredients) and the documentation backbone of GMP for formulas and labels. Plant-floor controls remain in our HACCP plan and production systems.

**Check Yourself**

1. Which hazard class does Genesis most directly help control, and through which features?
2. Name two GMP documentation requirements satisfied by versioning + audit trail.
3. What HACCP activities does Genesis *not* cover?

-----

## Section 7: Roles, User Scopes & the Compliance Analyst Workflow

### 7.1 The three user roles

|Role      |Can do                                                                                                                                                                                                      |Cannot do            |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
|**Admin** |Everything Editors can, **plus** user management: invite users (name + email, no support ticket needed), deactivate users, change permissions; see last-login dates and invite status (Invite Sent → Active)|—                    |
|**Editor**|Create/edit Ingredients, Recipes, Labels; generate and download reports                                                                                                                                     |Manage users         |
|**Viewer**|View all ingredients, recipes, labels; generate and download reports                                                                                                                                        |Make any data changes|

Notes: each user also has individual user settings (preferences) that don’t affect account-level settings. Deactivation is the offboarding control when staff leave — an access-control point worth auditing periodically.

**Typical mapping at a beverage company:** R&D scientists = Editors; the compliance/regulatory lead and IT owner = Admins; marketing, procurement, plant QA = Viewers. As a compliance analyst, DIANE Tran will likely hold **Editor** (to maintain ingredient/label data) with an Admin partner, or **Admin** if owning the account.

### 7.2 The end-to-end compliance analyst workflow (“recipe to label”)

1. **Ingredient intake.** Receive supplier spec sheet → create custom ingredient (or AI-extract it) → verify nutrients, confirm allergens (mandatory human step), attach the spec sheet, assign User Code/tags/attributes → respond to any AskReg allergen or restricted-additive flags → approve the ingredient.
2. **Formulation support.** R&D builds/iterates the recipe; nutrition recalculates live. Compliance reviews the Allergen Statement and uses **Allergen Origins** to verify every declared allergen traces to a real ingredient (and nothing is missing).
3. **Pre-approval review.** Generate **Preview (watermarked) labels** for cross-functional review with marketing and regulatory; run Food Comparison Reports if choosing among candidate formulas.
4. **Approval & lock.** Route the recipe through the approval step — version number assigned, date/time captured, record locked. This becomes the controlled master formula.
5. **Label generation.** Select Authority(ies), choose the correct format (RACC/dual-column logic, simplified eligibility), add beverage statements (juice %, caffeine declarations, Canadian cautionary statements/FOP as applicable), validate rounding and %DV, export final label data for packaging artwork.
6. **Change management.** Any later edit prompts re-review → new approved version alongside the old; document the reason in the audit-trail comment. Use Find and Replace for cross-portfolio ingredient swaps and review every affected recipe’s allergen flags.
7. **Downstream sync.** Where FoodLogiQ is in use, push approved formulation data into Product Management specs so FSQA and suppliers work from the same truth.
8. **Ongoing monitoring.** Watch dashboard alerts (restricted additives, allergen suggestions), quarterly release notes, and regulatory changes (the July 2025 FDA allergen-guidance update is the model: tree-nut list changed, milk/egg animal-source naming added — labels had to be reviewed).

### 7.3 Governance habits for DIANE Tran

- Establish tag/User Code conventions before bulk data entry.
- Keep “one approved version = one market-facing label” discipline; never edit around the approval flow.
- Quarterly: read release notes (genesisfoods.zendesk.com), review user list for deactivations, and re-run AskReg additive scans after authority changes.

**Check Yourself**

1. Which role can deactivate a departing employee, and why is that a compliance control?
2. At which workflow step does a record become locked, and what unlocks further change?
3. What should DIANE Tran do in Genesis when the FDA changes an allergen rule?

-----

## Section 8: Glossary

- **AskReg** — Trustwell’s AI regulatory assistant (chatbot + in-app allergen/additive flagging); also sold standalone.
- **Authority** — A regulatory jurisdiction module (U.S., Canada, Mexico, EU, AU/NZ).
- **Audit Trail** — Record of who changed what, when, with optional comments (manual enablement in Classic; integral to Foods workflows).
- **FOP** — Front-of-package nutrition symbol (Canada: sodium/sat fat/sugars thresholds).
- **HFSS** — UK High Fat, Salt, Sugar scoring affecting promotion of products.
- **Item Code** — Unique identifier on Trustwell database ingredients.
- **Preview Environment** — Migration sandbox holding a copy of Classic data for validation.
- **Preview Labels** — Watermarked draft labels/packaging reports.
- **RACC** — Reference Amount Customarily Consumed; 240 mL for most beverages; drives serving size and label format.
- **Supplemented Foods (Canada)** — Health Canada category covering caffeinated energy drinks and vitamin-added beverages; has its own facts panel and cautionary statements.
- **Trustwell Advisor** — Embedded “Ask About This” AI helper (2026).
- **Trustwell Connect** — The combined Genesis Foods + FoodLogiQ platform.

-----

## Section 9: 4-Week Learning Plan for DIANE Tran

|Week|Focus                                                                                                                               |Output                              |
|----|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
|1   |Sections 1–3; create a sandbox ingredient from a real supplier spec sheet; explore search, tags, attributes                         |One fully approved custom ingredient|
|2   |Section 4; build a simple beverage recipe (e.g., sweetened tea); review Allergen Statement vs. Origins; generate a Preview label    |Draft recipe + watermarked label    |
|3   |Section 5; produce U.S. and Canada labels for the same beverage; add juice %/caffeine statements; trigger and resolve a FOP scenario|Two-market label pack               |
|4   |Sections 6–7; run the full approval workflow; perform a Find-and-Replace exercise; write the team’s tag/version SOP draft           |Approved v1 recipe + mini-SOP       |

**Resources:** Genesis Foods Knowledge Base (genesisfoods.zendesk.com — AI Features, Ingredients, Recipes, Labels, Reports, Administration, Release Notes sections), Trustwell blog quarterly release posts, [support@trustwell.com](mailto:support@trustwell.com), [release@trustwell.com](mailto:release@trustwell.com).

-----

## Final Knowledge Check (20 questions)

1. What desktop product preceded Genesis Foods, and who built it?
2. What happens in the migration Preview environment?
3. How long is Classic data accessible after Production cutover?
4. Name the three user roles and one unique capability of each.
5. What does approval do to a recipe record?
6. Copy vs. Version — which one resets the audit trail?
7. What are the two tabs in a recipe’s Allergens section?
8. What does AskReg’s restricted-additive feature scan, and where do alerts appear?
9. What human step is always required after AI spec-sheet extraction?
10. What is the beverage RACC, and what does 200–300% of RACC require?
11. When must a beverage declare a juice percentage?
12. How are caffeine declarations typically handled on a U.S. energy drink label?
13. Which Genesis module supports Canadian energy drinks?
14. Which three nutrients trigger Canadian FOP symbols?
15. Which label format suits a near-zero-nutrient seltzer?
16. What 2025 FDA guidance changed tree-nut and milk allergen designations?
17. Which Genesis features support recall impact assessment?
18. What does Genesis NOT cover in a HACCP plan?
19. Where do approved formulations flow for supplier-facing specifications?
20. Name two 2026 features and their purpose.

-----

*Prepared as internal training material for DIANE Tran. Verify all regulatory interpretations against current FDA/Health Canada source regulations and company SOPs before applying to live labels.*