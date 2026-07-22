#!/usr/bin/env python3
"""Regenerate public/prompts/<category>/.manifest.json from the category's .md files.

The .md prompt files are the single source of truth. This script parses each
type: prompt or type: skill file, extracts its H2 sections and its verbatim
fenced prompt-text, and writes one manifest entry per prompt so downstream
consumers (the Word export) never drift from the prompts themselves.

Usage:
    python3 scripts/sync-prompt-manifests.py            # write manifests
    python3 scripts/sync-prompt-manifests.py --check    # fail if any manifest is stale
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "public" / "prompts"

CATEGORY_ORDER = [
    "setup",
    "label-intake",
    "content-derivation",
    "claims-compliance",
    "review-and-verification",
    "version-reconciliation",
    "market-and-reporting",
    "communication-email",
    "durable-knowledge",
    "copilot-configuration",
    "copilot-skills",
    "reflection",
]

INCLUDE_TYPES = {"prompt", "skill"}


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    body = text[m.end():]
    fm = {}
    key = None
    for line in m.group(1).splitlines():
        if re.match(r"^[A-Za-z0-9_-]+:", line):
            key, _, val = line.partition(":")
            key = key.strip()
            fm[key] = val.strip()
        elif line.strip().startswith("- ") and key:
            fm.setdefault(key + "__list", []).append(line.strip()[2:].strip())
    return fm, body


def section(body, name):
    """Return the text of an H2 section by kebab heading, minus code fences handled separately."""
    pat = re.compile(r"^## " + re.escape(name) + r"\s*\n(.*?)(?=^## |\Z)", re.S | re.M)
    m = pat.search(body)
    return m.group(1).strip() if m else ""


def first_para(text):
    text = text.strip()
    if not text:
        return ""
    # collapse a leading bullet list into a single sentence-ish string
    if text.startswith("- "):
        items = [ln[2:].strip() for ln in text.splitlines() if ln.strip().startswith("- ")]
        return "; ".join(items)
    return text.split("\n\n")[0].strip()


def extract_fences(body):
    """Return list of verbatim fenced block contents in document order."""
    return re.findall(r"```[a-zA-Z]*\n(.*?)```", body, re.S)


def saves_to(body):
    oh = section(body, "output-handling")
    m = re.search(r"[Ss]aves? (?:to|path)[:\s]*`?([^\s`.,]+/)`?", oh)
    if m:
        return m.group(1)
    m = re.search(r"`(projects/regulatory-labeling/|public/regulatory-labeling/)`", oh)
    return m.group(1) if m else "projects/regulatory-labeling/"


def build_entry(path):
    text = path.read_text()
    fm, body = parse_frontmatter(text)
    if fm.get("type") not in INCLUDE_TYPES:
        return None
    fences = extract_fences(body)
    prompt_text = fences[0].strip() if fences else ""
    if len(fences) > 1:
        # multi-stage prompts (e.g. second-eyes): join stages with a separator
        prompt_text = "\n\n=====\n\n".join(f.strip() for f in fences)
    return {
        "category": fm.get("category", ""),
        "sub_category": fm.get("sub-category", ""),
        "name": path.stem,
        "type": fm.get("type", ""),
        "description": first_para(section(body, "description")),
        "when_to_use": first_para(section(body, "when-to-use")),
        "what_to_use_for": first_para(section(body, "what-to-use-for")),
        "required_inputs": first_para(section(body, "required-inputs")),
        "expected_outputs": first_para(section(body, "expected-outputs")),
        "saves_to": saves_to(body),
        "visibility": fm.get("visibility", "private"),
        "prompt_text": prompt_text,
    }


def category_entries(category):
    cdir = PROMPTS_DIR / category
    entries = []
    for md in sorted(cdir.glob("*.md")):
        entry = build_entry(md)
        if entry:
            entries.append(entry)
    return entries


def main():
    check = "--check" in sys.argv
    stale = []
    written = 0
    for category in CATEGORY_ORDER:
        cdir = PROMPTS_DIR / category
        if not cdir.is_dir():
            print(f"warning: missing category dir {category}", file=sys.stderr)
            continue
        entries = category_entries(category)
        manifest_path = cdir / ".manifest.json"
        new = json.dumps(entries, indent=2, ensure_ascii=False) + "\n"
        old = manifest_path.read_text() if manifest_path.exists() else ""
        if check:
            if new != old:
                stale.append(category)
        else:
            manifest_path.write_text(new)
            written += 1
            print(f"wrote {manifest_path.relative_to(ROOT)} ({len(entries)} entries)")
    if check:
        if stale:
            print("stale manifests: " + ", ".join(stale), file=sys.stderr)
            sys.exit(1)
        print("manifests: up to date")
    else:
        print(f"done: {written} manifests")


if __name__ == "__main__":
    main()
