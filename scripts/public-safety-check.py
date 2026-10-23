#!/usr/bin/env python3
"""Reject personal, client-specific, and machine-specific text in tracked files."""

from __future__ import annotations

import pathlib
import re
import subprocess
import sys
import zipfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
PATTERNS = {
    "local path": re.compile(r"/(?:Users|home)/[^/\\\s]+|[A-Za-z]:\\\\Users\\"),
    "personal name": re.compile(r"\b(?:Kevin Lappe|Diane Tran)\b", re.IGNORECASE),
    "client identity": re.compile(r"\b(?:Talking Rain|Sparkling Ice)\b", re.IGNORECASE),
    "client email": re.compile(r"\bdtran@", re.IGNORECASE),
}
TEXT_EXTENSIONS = {".csv", ".html", ".json", ".md", ".py", ".txt", ".yml", ".yaml"}


def tracked_files() -> list[pathlib.Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        check=True,
        cwd=ROOT,
        capture_output=True,
    )
    return [ROOT / item.decode("utf-8") for item in result.stdout.split(b"\0") if item]


def text_for(path: pathlib.Path) -> str:
    if path.suffix.lower() == ".docx":
        with zipfile.ZipFile(path) as archive:
            return "\n".join(
                archive.read(name).decode("utf-8", errors="replace")
                for name in archive.namelist()
                if name.endswith(".xml")
            )
    return path.read_text(encoding="utf-8", errors="replace")


def main() -> int:
    errors: list[str] = []
    for path in tracked_files():
        if path == pathlib.Path(__file__).resolve():
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS | {".docx"}:
            continue
        text = text_for(path)
        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{path.relative_to(ROOT)}: contains {label}")
    if errors:
        print("public safety check failed:", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("public safety check: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
