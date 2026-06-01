#!/usr/bin/env python3
"""Build deterministic per-tool agent definitions from shared prompts."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from typing import Any

TARGETS = {
    "claude-code": {"ext": "md", "format": "claude-md"},
    "codex": {"ext": "yaml", "format": "codex-yaml"},
    "cursor": {"ext": "md", "format": "cursor-md"},
    "gemini": {"ext": "yaml", "format": "gemini-yaml"},
}

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n(.*)", re.DOTALL)

# Claude Code's agents-spec requires `tools` to be an explicit list of real
# tool names, not a semantic tier. Map the shared `agent-tools` tier to a
# spec-valid Claude tool list. Other targets (codex/gemini/cursor) keep the
# raw tier value, which their own ecosystems accept.
CLAUDE_TOOL_TIERS = {
    "read-only": "Read, Grep, Glob",
    "read-edit": "Read, Edit, Write, Grep, Glob",
    "read-web": "Read, Grep, Glob, WebFetch, WebSearch",
}


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = FRONTMATTER.match(text)
    if not match:
        raise ValueError("missing frontmatter")
    fm_text, body = match.group(1), match.group(2)
    data: dict[str, str] = {}
    current: str | None = None
    for line in fm_text.splitlines():
        if not line.strip():
            continue
        if line[:1].isspace() and current:
            data[current] = f"{data.get(current, '')} {line.strip()}".strip()
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            current = key.strip()
            data[current] = value.strip().strip('"')
    return data, body.strip()


def parse_shared(path: pathlib.Path) -> dict[str, Any]:
    fm, body = parse_frontmatter(path.read_text(encoding="utf-8"))
    return {
        "body": body,
        "name": fm.get("agent-name") or fm.get("name") or path.stem,
        "role": fm.get("agent-role") or fm.get("description") or "",
        "stem": path.stem,
        "tools": fm.get("agent-tools") or fm.get("tools") or "read-only",
    }


def emit_claude_md(agent: dict[str, Any]) -> str:
    tools = CLAUDE_TOOL_TIERS.get(agent["tools"], agent["tools"])
    return (
        "---\n"
        f"name: {agent['name']}\n"
        f"description: {agent['role']}\n"
        f"tools: {tools}\n"
        "---\n\n"
        f"{agent['body']}\n"
    )


def emit_cursor_md(agent: dict[str, Any]) -> str:
    return (
        "---\n"
        f"name: {agent['name']}\n"
        f"description: {agent['role']}\n"
        "mode: agent\n"
        "---\n\n"
        f"{agent['body']}\n"
    )


def block_scalar(value: str) -> str:
    return "\n".join(f"  {line}" if line else "" for line in value.splitlines())


def emit_codex_yaml(agent: dict[str, Any]) -> str:
    return (
        "version: 1\n"
        f"name: {agent['name']}\n"
        f"description: {agent['role']}\n"
        f"tools: {agent['tools']}\n"
        "system_prompt: |\n"
        f"{block_scalar(agent['body'])}\n"
    )


def emit_gemini_yaml(agent: dict[str, Any]) -> str:
    return (
        "version: 1\n"
        f"name: {agent['name']}\n"
        f"role: {agent['role']}\n"
        f"capabilities: {agent['tools']}\n"
        "instructions: |\n"
        f"{block_scalar(agent['body'])}\n"
    )


EMITTERS = {
    "claude-md": emit_claude_md,
    "codex-yaml": emit_codex_yaml,
    "cursor-md": emit_cursor_md,
    "gemini-yaml": emit_gemini_yaml,
}


def selected_tools(value: str) -> list[str]:
    tools = sorted(t.strip() for t in value.split(",") if t.strip())
    unknown = [tool for tool in tools if tool not in TARGETS]
    if unknown:
        raise SystemExit(f"unknown tool(s): {', '.join(unknown)}")
    return tools or sorted(TARGETS)


def build(shared_dir: pathlib.Path, out_dir: pathlib.Path, tools: list[str], name: str, dry_run: bool) -> dict[str, Any]:
    if not shared_dir.exists():
        raise SystemExit(f"missing shared dir: {shared_dir}")
    shared_files = sorted(shared_dir.glob("*.md"))
    if name:
        shared_files = [path for path in shared_files if path.stem == name]
    if not shared_files:
        raise SystemExit("no matching shared agents")

    summary: dict[str, Any] = {"agents": [], "tools": tools}
    for source in shared_files:
        agent = parse_shared(source)
        outputs: list[str] = []
        for tool in tools:
            config = TARGETS[tool]
            target_dir = out_dir / tool
            target_path = target_dir / f"{agent['stem']}.{config['ext']}"
            content = EMITTERS[config["format"]](agent)
            if dry_run:
                print(f"would write {target_path} ({len(content)} bytes)")
            else:
                target_dir.mkdir(parents=True, exist_ok=True)
                target_path.write_text(content, encoding="utf-8")
            outputs.append(str(target_path))
        summary["agents"].append({"name": agent["name"], "outputs": outputs, "stem": agent["stem"]})
    return summary


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shared-dir", default="", help="directory containing shared *.md prompts")
    parser.add_argument("--out-dir", default="", help="directory where per-tool folders are written")
    parser.add_argument("--tools", default=",".join(sorted(TARGETS)), help="comma-separated tool list")
    parser.add_argument("--name", default="", help="build one shared agent stem")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    root = pathlib.Path(__file__).resolve().parents[1]
    shared_dir = pathlib.Path(args.shared_dir).expanduser().resolve() if args.shared_dir else root / "agents" / "shared"
    out_dir = pathlib.Path(args.out_dir).expanduser().resolve() if args.out_dir else root / "agents"
    summary = build(shared_dir, out_dir, selected_tools(args.tools), args.name, args.dry_run)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
