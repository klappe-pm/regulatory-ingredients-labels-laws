#!/usr/bin/env python3
"""regwatch: regulatory watch-list register and change-detection engine.

Internal-research tooling for the regulatory-ingredients-labels-laws project.
It validates the obligation register against the data model, reports coverage
and the register for an analyst, captures source snapshots, and detects changes
in upstream sources by diffing a normalized content hash against the last-seen
state. It never edits the register on its own: detection flags, a human
reviews, and the register is updated by hand.

Standard library only, runnable from the project root:

    python3 scripts/regwatch.py validate
    python3 scripts/regwatch.py coverage
    python3 scripts/regwatch.py list --upcoming 365
    python3 scripts/regwatch.py capture --source us-fda-federal-register
    python3 scripts/regwatch.py scan --live --update
    python3 scripts/regwatch.py digest --out regwatch-digest.md
    python3 scripts/regwatch.py report --out regwatch-report.md --json regwatch-report.json
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "regwatch"
SCHEMA_PATH = DATA_DIR / "regwatch-schema.json"
OBLIGATIONS_PATH = DATA_DIR / "regwatch-obligations.csv"
SOURCES_PATH = DATA_DIR / "regwatch-sources.json"
FUNCTIONS_PATH = DATA_DIR / "regwatch-ingredient-functions.json"
JURISDICTIONS_PATH = DATA_DIR / "regwatch-jurisdictions.json"
STATE_DIR = DATA_DIR / "state"
SEEN_PATH = STATE_DIR / "regwatch-seen.json"
SNAPSHOT_DIR = STATE_DIR / "snapshots"

TAG_RE = re.compile(r"(?s)<[^>]+>")
SCRIPT_STYLE_RE = re.compile(r"(?is)<(script|style)\b.*?</\1>")
WHITESPACE_RE = re.compile(r"\s+")


# --- loading ---------------------------------------------------------------


def load_json(path: pathlib.Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_obligations() -> list[dict]:
    with OBLIGATIONS_PATH.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def split_list(value: str, delimiter: str) -> list[str]:
    return [item.strip() for item in (value or "").split(delimiter) if item.strip()]


# --- validation ------------------------------------------------------------


def is_iso_date(value: str) -> bool:
    try:
        dt.date.fromisoformat(value)
        return True
    except ValueError:
        return False


def check_value(field: str, rule: dict, value: str, refs: dict, delimiter: str) -> list[str]:
    errors: list[str] = []
    present = bool(value.strip())
    if rule.get("required") and not present:
        errors.append(f"field '{field}' is required but empty")
        return errors
    if not present:
        return errors
    if "enum" in rule and value not in rule["enum"]:
        errors.append(f"field '{field}' value '{value}' not in {rule['enum']}")
    if "pattern" in rule and not re.fullmatch(rule["pattern"], value):
        errors.append(f"field '{field}' value '{value}' does not match pattern {rule['pattern']}")
    if rule.get("type") == "date" and not is_iso_date(value):
        errors.append(f"field '{field}' value '{value}' is not an ISO date")
    if rule.get("type") == "date-or-empty" and value and not is_iso_date(value):
        errors.append(f"field '{field}' value '{value}' is not an ISO date")
    if rule.get("type") == "url-or-empty" and value and not value.startswith("http"):
        errors.append(f"field '{field}' value '{value}' is not a URL")
    if rule.get("ref"):
        items = split_list(value, delimiter) if rule.get("list") else [value]
        known = refs.get(rule["ref"], set())
        for item in items:
            if item not in known:
                errors.append(f"field '{field}' references unknown {rule['ref']} '{item}'")
    return errors


def check_catalog(name: str, items: list[dict], fields: dict, refs: dict, delimiter: str) -> list[str]:
    errors: list[str] = []
    key = next(field for field, rule in fields.items() if rule.get("unique"))
    seen: set[str] = set()
    for index, item in enumerate(items, start=1):
        prefix = f"{name} entry {index} ({item.get(key, '?')})"
        identifier = item.get(key, "")
        if identifier in seen:
            errors.append(f"{prefix}: duplicate {key}")
        seen.add(identifier)
        for field, rule in fields.items():
            value = item.get(field, "")
            value = "" if value is None else str(value)
            for error in check_value(field, rule, value, refs, delimiter):
                errors.append(f"{prefix}: {error}")
    return errors


def validate() -> int:
    schema = load_json(SCHEMA_PATH)
    delimiter = schema.get("list_delimiter", ";")
    sources = load_json(SOURCES_PATH)["sources"]
    functions = load_json(FUNCTIONS_PATH)["functions"]
    jurisdictions = load_json(JURISDICTIONS_PATH)["jurisdictions"]
    obligations = load_obligations()

    refs = {
        "sources": {s["source_id"] for s in sources},
        "functions": {f["function_id"] for f in functions},
        "jurisdictions": {j["jurisdiction_id"] for j in jurisdictions},
    }

    errors: list[str] = []
    errors += check_catalog("jurisdictions", jurisdictions, schema["jurisdiction_fields"], refs, delimiter)
    errors += check_catalog("sources", sources, schema["source_fields"], refs, delimiter)
    errors += check_catalog("functions", functions, schema["function_fields"], refs, delimiter)

    obligation_fields = schema["obligation_fields"]
    seen_ids: set[str] = set()
    for index, row in enumerate(obligations, start=2):
        prefix = f"obligations row {index} ({row.get('obligation_id', '?')})"
        oid = row.get("obligation_id", "")
        if oid in seen_ids:
            errors.append(f"{prefix}: duplicate obligation_id")
        seen_ids.add(oid)
        for field, rule in obligation_fields.items():
            value = row.get(field, "") or ""
            for error in check_value(field, rule, value, refs, delimiter):
                errors.append(f"{prefix}: {error}")
        extra = set(row) - set(obligation_fields)
        if extra:
            errors.append(f"{prefix}: unexpected columns {sorted(extra)}")

    for error in errors:
        print(f"ERROR {error}")
    print(
        f"regwatch validate: {len(obligations)} obligations, {len(sources)} sources, "
        f"{len(functions)} functions, {len(jurisdictions)} jurisdictions; errors={len(errors)}"
    )
    return 1 if errors else 0


# --- coverage --------------------------------------------------------------


def coverage(args: argparse.Namespace) -> int:
    jurisdictions = load_json(JURISDICTIONS_PATH)["jurisdictions"]
    obligations = load_obligations()
    with_rows: dict[str, int] = {}
    for row in obligations:
        with_rows[row["jurisdiction"]] = with_rows.get(row["jurisdiction"], 0) + 1

    by_coverage: dict[str, int] = {}
    gaps: list[str] = []
    for jur in jurisdictions:
        by_coverage[jur["coverage"]] = by_coverage.get(jur["coverage"], 0) + 1
        rows = with_rows.get(jur["jurisdiction_id"], 0)
        if jur["coverage"] == "confirmed" and rows == 0:
            gaps.append(f"{jur['jurisdiction_id']} marked confirmed but has no obligation rows")
        print(f"{jur['coverage']:<10} {jur['jurisdiction_id']:<14} rows={rows:<3} {jur['name']}")

    us_states = [j for j in jurisdictions if j["country"] == "US" and j["level"] == "state"]
    confirmed_states = [j for j in us_states if j["coverage"] == "confirmed"]
    print(
        f"regwatch coverage: {len(jurisdictions)} jurisdictions; "
        + ", ".join(f"{k}={v}" for k, v in sorted(by_coverage.items()))
    )
    print(f"regwatch coverage: US states confirmed {len(confirmed_states)}/{len(us_states)}")
    for gap in gaps:
        print(f"WARN  {gap}")
    return 0


# --- listing ---------------------------------------------------------------


def list_obligations(args: argparse.Namespace) -> int:
    schema = load_json(SCHEMA_PATH)
    delimiter = schema.get("list_delimiter", ";")
    rows = load_obligations()

    if args.country:
        rows = [r for r in rows if r["country"] == args.country]
    if args.jurisdiction:
        rows = [r for r in rows if r["jurisdiction"] == args.jurisdiction]
    if args.function:
        rows = [r for r in rows if args.function in split_list(r["ingredient_functions"], delimiter)]
    if args.status:
        rows = [r for r in rows if r["status"] == args.status]
    if args.upcoming is not None:
        horizon = dt.date.today() + dt.timedelta(days=args.upcoming)
        kept = [
            r
            for r in rows
            if r["effective_date"]
            and is_iso_date(r["effective_date"])
            and dt.date.today() <= dt.date.fromisoformat(r["effective_date"]) <= horizon
        ]
        rows = sorted(kept, key=lambda r: r["effective_date"])

    for row in rows:
        date = row["effective_date"] or "(no date)"
        print(f"{date}  {row['jurisdiction']:<14}  {row['status']:<11}  {row['title']}")
    print(f"regwatch list: {len(rows)} obligations")
    return 0


# --- source fetch and signal extraction ------------------------------------


def http_get(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "regwatch/0.1"})
    with urllib.request.urlopen(request, timeout=30) as response:  # noqa: S310
        return response.read().decode("utf-8", errors="replace")


def extract_signal(source: dict, content: str) -> str:
    """Reduce raw source content to the change-relevant signal before hashing.

    Per-source normalization keeps a hash from churning on markup or unrelated
    page furniture. The Federal Register API is reduced to a sorted list of
    document identifiers; HTML is stripped to collapsed text.
    """
    if source["mechanism"] == "api" and "federalregister.gov" in source["url"]:
        try:
            data = json.loads(content)
        except ValueError:
            return content
        rows = []
        for item in data.get("results", []):
            rows.append(
                "\t".join(
                    [
                        str(item.get("publication_date", "")),
                        str(item.get("document_number", "")),
                        str(item.get("title", "")),
                    ]
                )
            )
        return "\n".join(sorted(rows))
    if source["mechanism"] == "html":
        text = SCRIPT_STYLE_RE.sub(" ", content)
        text = TAG_RE.sub(" ", text)
        return WHITESPACE_RE.sub(" ", text).strip()
    return content


def fetch_source(source: dict, live: bool) -> tuple[str | None, str]:
    """Return (raw_content, origin). Snapshot first; --live falls back to HTTP.

    Snapshots are analyst-captured raw fixtures under state/snapshots so the
    engine runs and diffs deterministically offline. --live fetches the URL.
    """
    snapshot = SNAPSHOT_DIR / f"{source['source_id']}.txt"
    if snapshot.exists():
        return snapshot.read_text(encoding="utf-8", errors="replace"), "snapshot"
    if live:
        try:
            return http_get(source["url"]), "live"
        except Exception as exc:  # network is best-effort in this tool
            print(f"WARN  {source['source_id']}: live fetch failed: {exc}")
            return None, "error"
    return None, "missing"


def compute_scan(sources: list[dict], seen: dict, live: bool) -> list[dict]:
    results: list[dict] = []
    for source in sources:
        sid = source["source_id"]
        raw, origin = fetch_source(source, live)
        if raw is None:
            results.append({"source_id": sid, "status": "MISSING", "origin": origin, "sha256": None})
            continue
        digest = hashlib.sha256(extract_signal(source, raw).encode("utf-8")).hexdigest()
        prior = seen.get(sid, {}).get("sha256")
        if prior is None:
            status = "NEW"
        elif prior != digest:
            status = "CHANGED"
        else:
            status = "UNCHANGED"
        results.append({"source_id": sid, "status": status, "origin": origin, "sha256": digest})
    return results


def capture(args: argparse.Namespace) -> int:
    sources = load_json(SOURCES_PATH)["sources"]
    if args.source:
        sources = [s for s in sources if s["source_id"] == args.source]
        if not sources:
            print(f"ERROR no source '{args.source}'")
            return 1
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    captured = 0
    for source in sources:
        try:
            content = http_get(source["url"])
        except Exception as exc:
            print(f"WARN  {source['source_id']}: capture failed: {exc}")
            continue
        path = SNAPSHOT_DIR / f"{source['source_id']}.txt"
        path.write_text(content, encoding="utf-8")
        captured += 1
        print(f"captured   {source['source_id']:<26}  {len(content)} bytes")
    print(f"regwatch capture: {captured}/{len(sources)} sources")
    return 0 if captured else 1


def scan(args: argparse.Namespace) -> int:
    sources = load_json(SOURCES_PATH)["sources"]
    seen = load_json(SEEN_PATH) if SEEN_PATH.exists() else {}
    results = compute_scan(sources, seen, args.live)

    counts = {"NEW": 0, "CHANGED": 0, "UNCHANGED": 0, "MISSING": 0}
    new_state = dict(seen)
    now = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    for result in results:
        counts[result["status"]] += 1
        sid, status, origin = result["source_id"], result["status"], result["origin"]
        if status == "MISSING":
            print(f"MISSING    {sid:<26}  no snapshot ({origin}); capture one or use --live")
            continue
        print(f"{status:<10} {sid:<26}  {origin}  {result['sha256'][:12]}")
        new_state[sid] = {"sha256": result["sha256"], "origin": origin, "checked": now}

    summary = ", ".join(f"{k.lower()}={v}" for k, v in counts.items())
    print(f"regwatch scan: {len(sources)} sources; {summary}")

    if args.update:
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        SEEN_PATH.write_text(json.dumps(new_state, indent=2) + "\n", encoding="utf-8")
        print(f"regwatch scan: updated last-seen state at {SEEN_PATH.relative_to(ROOT)}")
    elif counts["NEW"] or counts["CHANGED"]:
        print("regwatch scan: changes detected; review then re-run with --update to accept")
    return 0


# --- digest and report -----------------------------------------------------


def upcoming_rows(rows: list[dict], window: int) -> list[dict]:
    today = dt.date.today()
    horizon = today + dt.timedelta(days=window)
    return sorted(
        (
            r
            for r in rows
            if r["effective_date"]
            and is_iso_date(r["effective_date"])
            and today <= dt.date.fromisoformat(r["effective_date"]) <= horizon
        ),
        key=lambda r: r["effective_date"],
    )


def digest(args: argparse.Namespace) -> int:
    rows = load_obligations()
    today = dt.date.today()

    lines: list[str] = ["# regwatch-digest", ""]
    lines.append(f"Generated {today.isoformat()}. Draft for analyst review; not a compliance determination.")
    lines.append("")

    lines.append(f"## Effective Within {args.window} Days")
    lines.append("")
    upcoming = upcoming_rows(rows, args.window)
    if upcoming:
        for r in upcoming:
            lines.append(f"- {r['effective_date']} — {r['jurisdiction']}: {r['title']} ({r['status']})")
    else:
        lines.append("- None.")
    lines.append("")

    by_jurisdiction: dict[str, list[dict]] = {}
    for r in rows:
        by_jurisdiction.setdefault(r["jurisdiction"], []).append(r)
    lines.append("## Register By Jurisdiction")
    lines.append("")
    for jurisdiction in sorted(by_jurisdiction):
        lines.append(f"### {jurisdiction}")
        lines.append("")
        for r in sorted(by_jurisdiction[jurisdiction], key=lambda r: r["title"]):
            date = r["effective_date"] or "no date"
            lines.append(f"- {r['title']} — {r['status']}, {date}")
        lines.append("")

    write_output("\n".join(lines).rstrip() + "\n", args.out, "digest")
    return 0


def report(args: argparse.Namespace) -> int:
    """Phase D output: combine source change-detection with upcoming obligations.

    This is the analyst-facing alert. It reads the last-seen state (it does not
    re-fetch unless --live) and the register, and surfaces what changed plus
    what is coming due. Nothing here is a compliance determination.
    """
    sources = load_json(SOURCES_PATH)["sources"]
    seen = load_json(SEEN_PATH) if SEEN_PATH.exists() else {}
    rows = load_obligations()
    results = compute_scan(sources, seen, args.live)

    flagged = [r for r in results if r["status"] in ("NEW", "CHANGED")]
    missing = [r for r in results if r["status"] == "MISSING"]
    upcoming = upcoming_rows(rows, args.window)
    today = dt.date.today()

    payload = {
        "generated": today.isoformat(),
        "window_days": args.window,
        "source_changes": flagged,
        "sources_missing_snapshot": [r["source_id"] for r in missing],
        "upcoming": [
            {
                "obligation_id": r["obligation_id"],
                "jurisdiction": r["jurisdiction"],
                "title": r["title"],
                "status": r["status"],
                "effective_date": r["effective_date"],
            }
            for r in upcoming
        ],
        "disclaimer": "Draft for analyst review. Detection flags; a human confirms. Not legal advice.",
    }

    lines = ["# regwatch-report", ""]
    lines.append(f"Generated {today.isoformat()}. Draft for analyst review; not a compliance determination.")
    lines.append("")
    lines.append("## Source Changes To Review")
    lines.append("")
    if flagged:
        for r in flagged:
            lines.append(f"- {r['status']} — {r['source_id']} ({r['origin']})")
    else:
        lines.append("- No source changes since last accepted state.")
    if missing:
        lines.append("")
        lines.append(f"_{len(missing)} sources have no snapshot; capture or run with --live._")
    lines.append("")
    lines.append(f"## Obligations Effective Within {args.window} Days")
    lines.append("")
    if upcoming:
        for r in upcoming:
            lines.append(f"- {r['effective_date']} — {r['jurisdiction']}: {r['title']} ({r['status']})")
    else:
        lines.append("- None.")
    lines.append("")

    write_output("\n".join(lines).rstrip() + "\n", args.out, "report")
    if args.json:
        pathlib.Path(args.json).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"regwatch report: wrote {args.json}")
    if flagged:
        print(f"regwatch report: {len(flagged)} source change(s) flagged for review")
    return 0


def write_output(text: str, out: str | None, label: str) -> None:
    if out:
        pathlib.Path(out).write_text(text, encoding="utf-8")
        print(f"regwatch {label}: wrote {out}")
    else:
        sys.stdout.write(text)


# --- cli -------------------------------------------------------------------


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate", help="validate the register and catalogs against the data model")
    sub.add_parser("coverage", help="report per-jurisdiction coverage")

    p_list = sub.add_parser("list", help="list obligations with optional filters")
    p_list.add_argument("--country", choices=["US", "CA", "MX"])
    p_list.add_argument("--jurisdiction")
    p_list.add_argument("--function")
    p_list.add_argument("--status")
    p_list.add_argument("--upcoming", type=int, help="only obligations effective within N days")

    p_capture = sub.add_parser("capture", help="fetch live source content into a snapshot fixture")
    p_capture.add_argument("--source", help="capture only this source_id")

    p_scan = sub.add_parser("scan", help="detect upstream source changes against last-seen state")
    p_scan.add_argument("--live", action="store_true", help="fetch source URLs when no snapshot exists")
    p_scan.add_argument("--update", action="store_true", help="write the new hashes to last-seen state")

    p_digest = sub.add_parser("digest", help="render an analyst-facing markdown digest of the register")
    p_digest.add_argument("--window", type=int, default=365, help="upcoming-effective horizon in days")
    p_digest.add_argument("--out", help="write to this path instead of stdout")

    p_report = sub.add_parser("report", help="render a change-and-due alert (markdown plus optional json)")
    p_report.add_argument("--window", type=int, default=365, help="upcoming-effective horizon in days")
    p_report.add_argument("--live", action="store_true", help="re-fetch sources for the report")
    p_report.add_argument("--out", help="write markdown to this path instead of stdout")
    p_report.add_argument("--json", help="also write the machine-readable report to this path")

    args = parser.parse_args(argv)
    dispatch = {
        "validate": lambda: validate(),
        "coverage": lambda: coverage(args),
        "list": lambda: list_obligations(args),
        "capture": lambda: capture(args),
        "scan": lambda: scan(args),
        "digest": lambda: digest(args),
        "report": lambda: report(args),
    }
    return dispatch[args.command]()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
