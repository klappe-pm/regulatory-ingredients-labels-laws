"""regwatch impact analysis.

The CPG feature suite joins regulatory obligations to a product portfolio and
scores the impact of each obligation on each product. The beverage component
adds a category lens over those impacts. Both are pure functions over already
loaded data so they stay testable and decoupled from IO.

Matching has three gates, all of which must pass for an impact to be recorded:
jurisdiction relevance (does the rule reach a channel the product sells in),
scope relevance (school or SNAP gating), and an attribute match on ingredient
function, named ingredient, or claim.
"""

from __future__ import annotations

import datetime as dt

US_RETAIL_CHANNELS = {"national", "US-CA", "school-channel", "snap"}
STATUS_WEIGHT = {"enacted": 2, "finalized": 2, "proposed": 1, "voluntary": 1, "in-progress": 1, "monitoring": 0}
SEVERITY_RANK = {"act-now": 0, "high": 1, "watch": 2, "info": 3}


def _split(value: str, delimiter: str) -> list[str]:
    return [item.strip() for item in (value or "").split(delimiter) if item.strip()]


def _is_state_code(jurisdiction: str) -> bool:
    return jurisdiction.startswith("US-") and jurisdiction not in ("US-Federal", "US-Multistate")


def jurisdiction_applies(jurisdiction: str, channels: set[str]) -> bool:
    if jurisdiction == "US-Federal":
        return bool(channels & US_RETAIL_CHANNELS) or any(c.startswith("US-") for c in channels)
    if jurisdiction == "US-Multistate":
        return "national" in channels or "US-CA" in channels
    if jurisdiction == "US-CA":
        return "US-CA" in channels or "national" in channels
    if _is_state_code(jurisdiction):
        # A nationally distributed product is exposed to every state's law.
        return "national" in channels or jurisdiction in channels
    if jurisdiction == "CA-Federal":
        return "CA-Federal" in channels
    if jurisdiction == "MX-Federal":
        return "MX-Federal" in channels
    return False


def scope_applies(scopes: set[str], product_functions: set[str], channels: set[str]) -> bool:
    if "school-channel" in scopes and "school-channel" not in channels:
        return False
    if "snap" in scopes:
        if "sweetener" not in product_functions:
            return False
        if not ({"national", "snap"} & channels):
            return False
    return True


def _near_term(effective_date: str, status: str, today: dt.date) -> int:
    if not effective_date:
        return 0
    try:
        days = (dt.date.fromisoformat(effective_date) - today).days
    except ValueError:
        return 0
    if days < 0:
        return 2 if status in ("enacted", "finalized") else 0
    if days <= 180:
        return 2
    if days <= 365:
        return 1
    return 0


def assess_impacts(obligations: list[dict], products: list[dict], delimiter: str, today: dt.date | None = None) -> list[dict]:
    today = today or dt.date.today()
    impacts: list[dict] = []
    for product in products:
        pfuncs = set(product.get("ingredient_functions", []))
        pings = {i.lower() for i in product.get("ingredients", [])}
        pclaims = set(product.get("claims", []))
        channels = set(product.get("channels", []))
        for ob in obligations:
            if not jurisdiction_applies(ob["jurisdiction"], channels):
                continue
            scopes = set(_split(ob.get("product_scope", ""), delimiter))
            if not scope_applies(scopes, pfuncs, channels):
                continue
            funcs = set(_split(ob.get("ingredient_functions", ""), delimiter))
            ings = _split(ob.get("ingredients", ""), delimiter)
            claims = set(_split(ob.get("claims_affected", ""), delimiter))

            func_match = funcs & pfuncs
            ing_match = sorted(i for i in ings if i.lower() in pings)
            claim_match = claims & pclaims
            if not (func_match or ing_match or claim_match):
                continue

            reasons = []
            if func_match:
                reasons.append("function: " + ", ".join(sorted(func_match)))
            if ing_match:
                reasons.append("ingredient: " + ", ".join(ing_match))
            if claim_match:
                reasons.append("claim: " + ", ".join(sorted(claim_match)))

            score = STATUS_WEIGHT.get(ob["status"], 0)
            score += _near_term(ob.get("effective_date", ""), ob["status"], today)
            score += 1 if ing_match else 0
            severity = "act-now" if score >= 4 else "high" if score >= 3 else "watch" if score >= 1 else "info"

            impacts.append(
                {
                    "product_id": product["product_id"],
                    "product_name": product["name"],
                    "obligation_id": ob["obligation_id"],
                    "obligation_title": ob["title"],
                    "jurisdiction": ob["jurisdiction"],
                    "status": ob["status"],
                    "effective_date": ob.get("effective_date", ""),
                    "reasons": reasons,
                    "severity": severity,
                }
            )
    impacts.sort(key=lambda i: (SEVERITY_RANK[i["severity"]], i["effective_date"] or "9999", i["product_id"]))
    return impacts


BEVERAGE_THEMES = [
    {
        "key": "sweeteners",
        "title": "Sweeteners and added sugar",
        "functions": {"sweetener"},
        "why": "Added sugar is the most likely front-of-package High rating and the clearest SNAP and school target, while non-nutritive sweeteners such as sucralose draw ultra-processed-food definitions and labeling challenges. The win and the risk sit on the same zero-sugar can.",
        "action": "Confirm sweetener disclosures and watch front-of-package, UPF, SNAP, California AB 1264, and Mexico NOM-051.",
    },
    {
        "key": "colors",
        "title": "Synthetic colors",
        "functions": {"color"},
        "why": "Flavored and colored sparkling drinks are squarely in the federal dye phase-out and state school bans, and any color swap is also a claims event, not just a recipe change.",
        "action": "Inventory color sources by SKU and route any swap through claims review.",
    },
    {
        "key": "caffeine",
        "title": "Caffeine and energy positioning",
        "functions": {"stimulant"},
        "why": "Caffeinated lines carry their own track: voluntary federal caffeine labeling guidance and Canada's supplemented-foods caution statements and caffeine limits.",
        "action": "Confirm per-serving caffeine and cautionary-statement requirements per market.",
    },
    {
        "key": "preservatives",
        "title": "Preservatives and the GRAS overhaul",
        "functions": {"preservative", "additive"},
        "why": "Self-affirmed GRAS additives now need an audit-ready safety file, and preservatives such as BHA and BHT are early federal re-review targets.",
        "action": "Assemble safety files for any self-affirmed GRAS ingredient in use.",
    },
    {
        "key": "prop65",
        "title": "Proposition 65 heavy metals",
        "functions": {"contaminant"},
        "why": "Trace heavy metals carried in by botanicals, colors, or concentrates create bounty-driven Proposition 65 exposure where presence, not harm, triggers a notice.",
        "action": "Maintain annual heavy-metal testing and supplier indemnity for California-sold products.",
    },
]


def beverage_findings(obligations: list[dict], impacts: list[dict], products: list[dict], delimiter: str) -> list[dict]:
    ob_functions = {ob["obligation_id"]: set(_split(ob.get("ingredient_functions", ""), delimiter)) for ob in obligations}
    ob_titles = {ob["obligation_id"]: ob["title"] for ob in obligations}
    product_functions = {p["name"]: set(p.get("ingredient_functions", [])) for p in products}

    findings: list[dict] = []
    for theme in BEVERAGE_THEMES:
        theme_obligations = sorted(
            {ob_titles[oid] for oid, funcs in ob_functions.items() if funcs & theme["functions"]}
        )
        # A product is affected by a theme only when it both carries one of the
        # theme's functions and has an impact from a theme-relevant obligation.
        affected = sorted(
            {
                i["product_name"]
                for i in impacts
                if ob_functions.get(i["obligation_id"], set()) & theme["functions"]
                and product_functions.get(i["product_name"], set()) & theme["functions"]
            }
        )
        if not theme_obligations and not affected:
            continue
        findings.append(
            {
                "title": theme["title"],
                "why": theme["why"],
                "action": theme["action"],
                "affected_products": affected,
                "obligations": theme_obligations,
            }
        )
    return findings
