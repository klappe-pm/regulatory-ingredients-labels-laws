#!/usr/bin/env python3
"""regwatch: regulatory watch-list register and change-detection engine.

Internal-research tooling for the regulatory-ingredients-labels-laws project.
It validates the obligation register against the data model, reports the
register for an analyst, and detects changes in upstream sources by diffing a
content hash against the last-seen state. It never edits the register on its
own: detection flags, a human reviews, and the register is updated by hand.

Standard library only, runnable from the project root:

    python3 scripts/regwatch.py validate
    python3 scripts/regwatch.py list --upcoming 365
    python3 scripts/regwatch.py scan
    python3 scripts/regwatch.py digest
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "regwatch"
SCHEMA_PATH = DATA_DIR / "regwatch-schema.json"
OBLIGATIONS_PATH = DATA_DIR / "regwatch-obligations.csv"
SOURCES_PATH = DATA_DIR / "regwatch-sources.json"
FUNCTIONS_PATH = DATA_DIR / "regwatch-ingredient-functions.json"
STATE_DIR = DATA_DIR / "state"
SEEN_PATH = STATE_DIR / "regwatch-seen.json"
SNAPSHOT_DIR = STATE_DIR / "snapshots"


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


def validate() -> int:
    schema = load_json(SCHEMA_PATH)
    delimiter = schema.get("list_delimiter", ";")
    sources = load_json(SOURCES_PATH)["sources"]
    functions = load_json(FUNCTIONS_PATH)["functions"]
    obligations = load_obligations()

    errors: list[str] = []

    source_ids = {s["source_id"] for s in sources}
    function_ids = {f["function_id"] for f in functions}
    refs = {"sources": source_ids, "functions": function_ids}

    # Cross-file referential integrity is only meaningful if the catalogs
    # themselves have unique keys.
    for name, items, key in (("sources", sources, "source_id"), ("functions", functions, "function_id")):
        seen: set[str] = set()
        for item in items:
            value = item.get(key, "")
            if value in seen:
                errors.append(f"{name}: duplicate {key} '{value}'")
            seen.add(value)

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
        f"regwatch validate: {len(obligations)} obligations, "
        f"{len(sources)} sources, {len(functions)} functions; errors={len(errors)}"
    )
    return 1 if errors else 0


# --- listing ---------------------------------------------------------------


def list_obligations(args: argparse.Namespace) -> int:
    schema = load_json(SCHEMA_PATH)
    delimiter = schema.get("list_delimiter", ";")
    rows = load_obligations()

    if args.country:
        rows = [r for r in rows if r["country"] == args.country]
    if args.function:
        rows = [r for r in rows if args.function in split_list(r["ingredient_functions"], delimiter)]
    if args.status:
        rows = [r for r in rows if r["status"] == args.status]
    if args.upcoming is not None:
        horizon = dt.date.today() + dt.timedelta(days=args.upcoming)
        kept = []
        for r in rows:
            date = r["effective_date"]
            if date and is_iso_date(date) and dt.date.today() <= dt.date.fromisoformat(date) <= horizon:
                kept.append(r)
        rows = sorted(kept, key=lambda r: r["effective_date"])

    for row in rows:
        date = row["effective_date"] or "(no date)"
        print(f"{date}  {row['jurisdiction']:<14}  {row['status']:<11}  {row['title']}")
    print(f"regwatch list: {len(rows)} obligations")
    return 0


# --- change detection ------------------------------------------------------


def fetch_source(source: dict, live: bool) -> tuple[str | None, str]:
    """Return (content, origin). Snapshot first; --live falls back to HTTP.

    Snapshots are analyst-captured fixtures under state/snapshots so the engine
    runs and diffs deterministically offline. --live fetches the source URL.
    """
    snapshot = SNAPSHOT_DIR / f"{source['source_id']}.txt"
    if snapshot.exists():
        return snapshot.read_text(encoding="utf-8", errors="replace"), "snapshot"
    if live:
        try:
            request = urllib.request.Request(source["url"], headers={"User-Agent": "regwatch/0.1"})
            with urllib.request.urlopen(request, timeout=30) as response:  # noqa: S310
                return response.read().decode("utf-8", errors="replace"), "live"
        except Exception as exc:  # network is best-effort in this tool
            print(f"WARN  {source['source_id']}: live fetch failed: {exc}")
            return None, "error"
    return None, "missing"


def scan(args: argparse.Namespace) -> int:
    sources = load_json(SOURCES_PATH)["sources"]
    seen = load_json(SEEN_PATH) if SEEN_PATH.exists() else {}
    new_state = dict(seen)

    counts = {"NEW": 0, "CHANGED": 0, "UNCHANGED": 0, "MISSING": 0}
    for source in sources:
        sid = source["source_id"]
        content, origin = fetch_source(source, args.live)
        if content is None:
            counts["MISSING"] += 1
            print(f"MISSING    {sid:<26}  no snapshot ({origin}); capture one or use --live")
            continue
        digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
        prior = seen.get(sid, {}).get("sha256")
        if prior is None:
            status = "NEW"
        elif prior != digest:
            status = "CHANGED"
        else:
            status = "UNCHANGED"
        counts[status] += 1
        print(f"{status:<10} {sid:<26}  {origin}  {digest[:12]}")
        new_state[sid] = {
            "sha256": digest,
            "origin": origin,
            "checked": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        }

    summary = ", ".join(f"{k.lower()}={v}" for k, v in counts.items())
    print(f"regwatch scan: {len(sources)} sources; {summary}")

    if args.update:
        SEEN_PATH.write_text(json.dumps(new_state, indent=2) + "\n", encoding="utf-8")
        print(f"regwatch scan: updated last-seen state at {SEEN_PATH.relative_to(ROOT)}")
    elif counts["NEW"] or counts["CHANGED"]:
        print("regwatch scan: changes detected; review then re-run with --update to accept")
    return 0


# --- digest ----------------------------------------------------------------


def digest(args: argparse.Namespace) -> int:
    rows = load_obligations()
    today = dt.date.today()
    horizon = today + dt.timedelta(days=args.window)

    lines: list[str] = []
    lines.append("# regwatch-digest")
    lines.append("")
    lines.append(f"Generated {today.isoformat()}. Draft for analyst review; not a compliance determination.")
    lines.append("")

    upcoming = sorted(
        (r for r in rows if r["effective_date"] and is_iso_date(r["effective_date"]) and today <= dt.date.fromisoformat(r["effective_date"]) <= horizon),
        key=lambda r: r["effective_date"],
    )
    lines.append(f"## Effective Within {args.window} Days")
    lines.append("")
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

    output = "\n".join(lines).rstrip() + "\n"
    if args.out:
        pathlib.Path(args.out).write_text(output, encoding="utf-8")
        print(f"regwatch digest: wrote {args.out}")
    else:
        sys.stdout.write(output)
    return 0


# --- cli -------------------------------------------------------------------


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate", help="validate the register against the data model")

    p_list = sub.add_parser("list", help="list obligations with optional filters")
    p_list.add_argument("--country", choices=["US", "CA", "MX"])
    p_list.add_argument("--function")
    p_list.add_argument("--status")
    p_list.add_argument("--upcoming", type=int, help="only obligations effective within N days")

    p_scan = sub.add_parser("scan", help="detect upstream source changes against last-seen state")
    p_scan.add_argument("--live", action="store_true", help="fetch source URLs when no snapshot exists")
    p_scan.add_argument("--update", action="store_true", help="write the new hashes to last-seen state")

    p_digest = sub.add_parser("digest", help="render an analyst-facing markdown digest")
    p_digest.add_argument("--window", type=int, default=365, help="upcoming-effective horizon in days")
    p_digest.add_argument("--out", help="write to this path instead of stdout")

    args = parser.parse_args(argv)
    if args.command == "validate":
        return validate()
    if args.command == "list":
        return list_obligations(args)
    if args.command == "scan":
        return scan(args)
    if args.command == "digest":
        return digest(args)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
