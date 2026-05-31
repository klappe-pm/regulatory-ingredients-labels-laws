#!/usr/bin/env python3
"""Markdown audit with runtime carve-out support.

Stage A1 keeps this intentionally conservative: strict checks apply only to
files the current rules can judge safely. Harness surfaces are skipped before
frontmatter, H1, or wikilink checks run.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys
from collections.abc import Iterable

DEFAULT_IGNORE_DIRS = {
    ".git",
    ".obsidian",
    ".venv",
    "__pycache__",
    "_archive",
    "backups",
    "build",
    "cache",
    "dist",
    "file-history",
    "node_modules",
    "plugins",
    "projects",
    "sessions",
    "test-fixtures",
    "venv",
    "z-archive",
}

DEFAULT_CARVEOUT_PREFIXES = {
    ".claude",
    "agents",
    "commands",
    "hooks",
    "skills",
}

DEFAULT_CARVEOUT_FILES = {
    "AGENTS.md",
    "CLAUDE.md",
    "CODEX.md",
    "GEMINI.md",
    "GIT-STRATEGY.md",
    "PASSOFF.md",
    "PR-STANDARDS.md",
    "README.md",
    "SKILL.md",
    "WARP.md",
}

WIKILINK = re.compile(r"\[\[([^\]\|#]+)(?:[#\|][^\]]*)?\]\]")
H1 = re.compile(r"^#\s+(.+)$", re.MULTILINE)
HEADING = re.compile(r"^(#{2,6})\s+(.+)$", re.MULTILINE)
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]*`")
FENCED_CODE = re.compile(r"```.*?```", re.DOTALL)
TABLE_PATTERN = re.compile(r"^\|\s*`?([^`|]+)`?\s*\|", re.MULTILINE)
CANONICAL_STATUS = {"NEW", "DRAFT", "INPRG", "REVIEW", "DONE", "ARCHIVED"}
STATUS_RE = re.compile(r"^status:\s*(.*?)\s*$", re.MULTILINE)
LOWER_WORDS = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "but",
    "by",
    "for",
    "in",
    "nor",
    "of",
    "on",
    "or",
    "per",
    "the",
    "to",
    "vs",
    "with",
}
ACRONYMS = {"API", "CI", "JSON", "LLM", "MCP", "PR", "YAML"}


def strip_code(text: str) -> str:
    return INLINE_CODE.sub("", FENCED_CODE.sub("", text))


def repo_root_for(path: pathlib.Path) -> pathlib.Path:
    if path.is_file():
        return path.parent
    return path


def load_carveout_prefixes(root: pathlib.Path) -> set[str]:
    prefixes = set(DEFAULT_CARVEOUT_PREFIXES)
    candidates = [
        root / "rules" / "runtime-format-carveouts.md",
        pathlib.Path.home() / ".claude" / "rules" / "runtime-format-carveouts.md",
    ]
    for candidate in candidates:
        if not candidate.exists() or candidate.name == "settings.local.json":
            continue
        text = candidate.read_text(encoding="utf-8", errors="replace")
        for raw in TABLE_PATTERN.findall(text):
            item = raw.strip()
            if not item or item.lower() == "subtree":
                continue
            item = item.replace("~/.claude/", "")
            item = item.replace("<project>/", "")
            item = item.rstrip("/")
            first = item.split("/", 1)[0]
            if first and not first.startswith("<"):
                prefixes.add(first)
    return prefixes


def is_safe_markdown_in_claude(root: pathlib.Path, path: pathlib.Path) -> bool:
    rel = path.relative_to(root)
    parts = rel.parts
    if parts[0] == "rules":
        return path.suffix == ".md"
    if parts[0] == "specs":
        return True
    if rel == pathlib.Path("tests/README.md"):
        return True
    return False


def is_claude_config_root(root: pathlib.Path) -> bool:
    return (root / "PASSOFF.md").exists() and (root / "settings.json").exists() and (root / "commands").is_dir()


def should_skip(root: pathlib.Path, path: pathlib.Path, carveouts: set[str]) -> bool:
    if path.name == "settings.local.json":
        return True
    try:
        rel = path.relative_to(root)
    except ValueError:
        rel = pathlib.Path(path.name)
    if any(part in DEFAULT_IGNORE_DIRS or part.startswith("_") for part in rel.parts):
        return True
    if path.name in DEFAULT_CARVEOUT_FILES:
        return True
    if rel.parts and rel.parts[0] in carveouts:
        return True
    if is_claude_config_root(root):
        return not is_safe_markdown_in_claude(root, path)
    return False


def iter_md(targets: Iterable[pathlib.Path], root: pathlib.Path) -> list[pathlib.Path]:
    carveouts = load_carveout_prefixes(root)
    files: list[pathlib.Path] = []
    for target in targets:
        target = target.resolve()
        if target.is_file():
            if target.suffix == ".md" and not should_skip(root, target, carveouts):
                files.append(target)
            continue
        for path in target.rglob("*.md"):
            if not should_skip(root, path, carveouts):
                files.append(path)
    return sorted(set(files))


def parse_frontmatter(text: str) -> tuple[bool, str]:
    match = FRONTMATTER.match(text)
    if not match:
        return False, ""
    return True, match.group(1)


def expected_h1(path: pathlib.Path) -> str:
    return path.stem.lower()


def normalized_h1(value: str) -> str:
    return value.strip().lower().replace(" ", "-")


def check_h1(path: pathlib.Path, text: str) -> list[str]:
    match = H1.search(text)
    if not match:
        return []
    actual = normalized_h1(match.group(1))
    expected = expected_h1(path)
    if actual != expected:
        return [f"{path}: H1 '{match.group(1).strip()}' does not match filename stem '{expected}'"]
    return []


def check_frontmatter(path: pathlib.Path, text: str) -> list[str]:
    found, body = parse_frontmatter(text)
    if not found:
        return []
    errors: list[str] = []
    for line_number, line in enumerate(body.splitlines(), start=2):
        if not line.strip():
            continue
        if line[:1].isspace():
            continue
        stripped = line.strip()
        if stripped.startswith("-") or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            errors.append(f"{path}:{line_number}: frontmatter line lacks ':' -> {line!r}")
    return errors


def check_wikilinks(path: pathlib.Path, text: str, stems: set[str]) -> list[str]:
    errors: list[str] = []
    scannable = strip_code(text)
    for match in WIKILINK.finditer(scannable):
        target = match.group(1).strip().lower()
        if target not in stems:
            errors.append(f"{path}: wikilink [[{match.group(1).strip()}]] has no matching markdown stem")
    return errors


def split_words(value: str) -> list[str]:
    return [word for word in re.split(r"[\s]+", value.strip()) if word]


def is_title_word(word: str, index: int) -> bool:
    cleaned = word.strip("()[]{}.,:;!?")
    if not cleaned:
        return True
    if cleaned in {"-", "—"}:
        return True
    if re.match(r"^\d+[a-z]?$", cleaned, re.IGNORECASE):
        return True
    if word.startswith("(") or word.endswith(")"):
        return True
    if cleaned.startswith("`") and cleaned.endswith("`"):
        return True
    if "/" in cleaned or "." in cleaned:
        return True
    if re.match(r"^v?\d+(?:\.\d+)*(?:-[a-z0-9]+)?$", cleaned):
        return True
    if cleaned in ACRONYMS:
        return True
    if cleaned.isupper() and len(cleaned) > 1:
        return True
    if index > 0 and cleaned.lower() in LOWER_WORDS:
        return cleaned.islower()
    return cleaned[:1].isupper()


def check_headers(path: pathlib.Path, text: str) -> list[str]:
    errors: list[str] = []
    scannable = FENCED_CODE.sub("", text)
    for match in HEADING.finditer(scannable):
        heading = match.group(2).strip()
        if heading.startswith("Header Case Exceptions"):
            continue
        if re.match(r"^v?\d+(?:\.\d+)*(?:-[a-z0-9]+)?(?:\s+\(.+\))?$", heading):
            continue
        words = split_words(INLINE_CODE.sub("`code`", heading))
        bad = [word for index, word in enumerate(words) if not is_title_word(word, index)]
        if bad:
            errors.append(f"{path}: heading '{heading}' is not Title Case")
    return errors


def project_status_mode(root: pathlib.Path) -> str:
    project = root / "project.yml"
    if not project.exists():
        return "canonical" if is_claude_config_root(root) else "off"
    text = project.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"^status-vocabulary:\s*(\S+)\s*$", text, re.MULTILINE)
    return match.group(1) if match else "off"


def check_status(path: pathlib.Path, text: str, mode: str) -> list[str]:
    if mode != "canonical":
        return []
    found, body = parse_frontmatter(text)
    if not found:
        return []
    match = STATUS_RE.search(body)
    if not match:
        return []
    value = match.group(1).strip().strip("'\"")
    if value and value not in CANONICAL_STATUS and value.lower() not in {"active", "draft", "archived", "deprecated"}:
        return [f"{path}: status '{value}' is outside canonical vocabulary"]
    return []


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="files or directories to audit")
    parser.add_argument("--root", default="", help="audit root; defaults to cwd or first path root")
    parser.add_argument("--strict-frontmatter", action="store_true")
    parser.add_argument("--strict-h1", action="store_true")
    parser.add_argument("--strict-links", action="store_true")
    parser.add_argument("--strict-headers", action="store_true", help="accepted for Stage A2 compatibility")
    parser.add_argument("--strict-status", action="store_true", help="accepted for Stage A2 compatibility")
    args = parser.parse_args(argv)

    raw_targets = [pathlib.Path(p).expanduser() for p in args.paths]
    if args.root:
        root = pathlib.Path(args.root).expanduser().resolve()
    elif raw_targets:
        root = repo_root_for(raw_targets[0].resolve())
    else:
        root = pathlib.Path.cwd().resolve()
    targets = raw_targets or [root]

    md_files = iter_md(targets, root)
    stems = {path.stem.lower() for path in md_files}
    if args.strict_links:
        stems.update(path.stem.lower() for path in iter_md([root], root))
        try:
            listed = subprocess.run(
                ["git", "-C", str(root), "ls-files", "*.md"],
                check=False,
                capture_output=True,
                text=True,
            )
        except OSError:
            listed = None
        if listed and listed.returncode == 0:
            stems.update(pathlib.Path(line).stem.lower() for line in listed.stdout.splitlines() if line)
    status_mode = project_status_mode(root)

    errors: list[str] = []
    warnings: list[str] = []
    for path in md_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        frontmatter = check_frontmatter(path, text)
        (errors if args.strict_frontmatter else warnings).extend(frontmatter)
        h1 = check_h1(path, text)
        (errors if args.strict_h1 else warnings).extend(h1)
        links = check_wikilinks(path, text, stems)
        (errors if args.strict_links else warnings).extend(links)
        headers = check_headers(path, text)
        (errors if args.strict_headers else warnings).extend(headers)
        status = check_status(path, text, status_mode)
        (errors if args.strict_status else warnings).extend(status)

    if args.strict_status and status_mode == "custom":
        warnings.append(f"{root}: status-vocabulary custom; skipping canonical status check")

    for warning in warnings:
        print(f"WARN  {warning}")
    for error in errors:
        print(f"ERROR {error}")
    print(f"audit: {len(md_files)} files; errors={len(errors)}; warnings={len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
