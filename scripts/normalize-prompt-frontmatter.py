#!/usr/bin/env python3
"""Normalize prompt-library frontmatter to the vault linter.yaml schema.

Deterministic pass run after the prose restructure. It:
  - converts a scalar `type: X` into a `types:` list (["X"]),
  - reorders keys to: domain, category, sub-category, types, date-created,
    date-revised, then remaining non-alias/tag keys alphabetically, then
    aliases and tags LAST (per linter.yaml yaml-key-sort priority-keys and the
    "aliases and tags always follow last" rule),
  - alphabetizes and de-dupes list values case-insensitively (aliases, tags,
    types),
  - renders list values as block lists and scalars unquoted.

Usage:
    python3 scripts/normalize-prompt-frontmatter.py            # rewrite in place
    python3 scripts/normalize-prompt-frontmatter.py --check    # nonzero if drift
"""
import glob
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "public" / "prompts"

PRIORITY = ["domain", "category", "sub-category", "types", "date-created", "date-revised"]
LAST = ["aliases", "tags"]
LIST_KEYS = {"types", "aliases", "tags", "links"}


def split_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5:]


def parse(fm):
    """Minimal ordered parser for our flat frontmatter (scalars + block lists)."""
    data = {}
    order = []
    key = None
    for line in fm.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - ") or line.startswith("- "):
            if key is not None:
                data.setdefault(key, [])
                if not isinstance(data[key], list):
                    data[key] = []
                data[key].append(line.split("- ", 1)[1].strip())
            continue
        if ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            k = k.strip()
            v = v.strip()
            order.append(k)
            key = k
            if v == "" or v == "[]":
                data[k] = [] if (v == "[]" or k in LIST_KEYS) else ""
            else:
                data[k] = v
    return data, order


def dedupe_sorted(vals):
    seen = {}
    for v in vals:
        seen.setdefault(v.lower(), v)
    return [seen[k] for k in sorted(seen)]


def render(data):
    # migrate scalar type -> types list
    if "type" in data and "types" not in data:
        t = data.pop("type")
        data["types"] = [t] if t else []
    keys = list(data.keys())
    middle = [k for k in keys if k not in PRIORITY and k not in LAST]
    ordered = [k for k in PRIORITY if k in data] + sorted(middle) + [k for k in LAST if k in data]
    lines = ["---"]
    for k in ordered:
        v = data[k]
        if k in LIST_KEYS or isinstance(v, list):
            v = dedupe_sorted(v if isinstance(v, list) else [v]) if v else []
            if not v:
                lines.append(f"{k}:")
            else:
                lines.append(f"{k}:")
                for item in v:
                    lines.append(f"  - {item}")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def process(path, check):
    text = path.read_text()
    fm, body = split_frontmatter(text)
    if fm is None:
        return False
    data, _ = parse(fm)
    new = render(data) + body.lstrip("\n") if body.startswith("\n") else render(data) + "\n" + body
    # normalize: exactly one blank line after frontmatter
    new = render(data) + "\n" + body.lstrip("\n")
    if new != text:
        if not check:
            path.write_text(new)
        return True
    return False


def main():
    check = "--check" in sys.argv
    changed = []
    for f in sorted(glob.glob(str(PROMPTS / "**" / "*.md"), recursive=True)):
        if process(Path(f), check):
            changed.append(Path(f).relative_to(ROOT))
    if check:
        if changed:
            print("frontmatter drift in:")
            for c in changed:
                print(f"  {c}")
            sys.exit(1)
        print("frontmatter: normalized")
    else:
        for c in changed:
            print(f"normalized {c}")
        print(f"done: {len(changed)} files")


if __name__ == "__main__":
    main()
