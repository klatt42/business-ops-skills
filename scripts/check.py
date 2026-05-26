#!/usr/bin/env python3
"""
Lint marketplace.json + every plugin.json + every SKILL.md and verify
cross-file references in klatt42/business-ops-skills.

Checks:
  1. .claude-plugin/marketplace.json parses as valid JSON.
  2. Every plugin entry's `source` path resolves to an existing directory.
  3. Every <plugin>/.claude-plugin/plugin.json parses + has name/version/description.
  4. The `name` in plugin.json matches the marketplace.json entry.
  5. Every SKILL.md under plugins/ and skills/ has valid YAML frontmatter
     with `name` and `description` fields, and a non-empty body.

Exit 0 if clean, 1 otherwise. Requires: pyyaml.

Run from repo root or anywhere — paths resolve from this file's location.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FATAL: pyyaml not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []
warnings: list[str] = []
checked = {"marketplace": 0, "plugin_json": 0, "skill_md": 0}


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def check_marketplace() -> dict:
    """Returns the parsed marketplace.json dict, or {} on fatal error."""
    mp = ROOT / ".claude-plugin" / "marketplace.json"
    if not mp.exists():
        err(f"missing: {mp.relative_to(ROOT)}")
        return {}
    try:
        data = json.loads(mp.read_text())
    except json.JSONDecodeError as e:
        err(f"marketplace.json invalid JSON: {e}")
        return {}
    checked["marketplace"] = 1

    for key in ("name", "owner", "plugins"):
        if key not in data:
            err(f"marketplace.json missing required key: {key}")
    if not isinstance(data.get("plugins"), list):
        err("marketplace.json: 'plugins' must be a list")
        return data

    for i, entry in enumerate(data["plugins"]):
        prefix = f"marketplace.json plugins[{i}] ({entry.get('name', '?')})"
        for k in ("name", "source", "description"):
            if k not in entry:
                err(f"{prefix}: missing '{k}'")
        if not isinstance(entry.get("source"), str):
            continue
        src = entry["source"]
        if not src.startswith("./"):
            warn(f"{prefix}: external source (not in-tree): {src}")
            continue
        plugin_dir = ROOT / src[2:]
        if not plugin_dir.is_dir():
            err(f"{prefix}: source path does not exist: {src}")
            continue
        plugin_json = plugin_dir / ".claude-plugin" / "plugin.json"
        if not plugin_json.exists():
            err(f"{prefix}: missing {plugin_json.relative_to(ROOT)}")
            continue
        check_plugin_json(plugin_json, marketplace_name=entry["name"])
    return data


def check_plugin_json(path: Path, marketplace_name: str) -> None:
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        err(f"{path.relative_to(ROOT)}: invalid JSON: {e}")
        return
    checked["plugin_json"] += 1
    for k in ("name", "version", "description"):
        if k not in data:
            err(f"{path.relative_to(ROOT)}: missing '{k}'")
    if data.get("name") and data["name"] != marketplace_name:
        err(
            f"{path.relative_to(ROOT)}: name '{data['name']}' "
            f"!= marketplace entry name '{marketplace_name}'"
        )


def check_skill_md(path: Path) -> None:
    text = path.read_text(errors="replace")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not m:
        err(f"{path.relative_to(ROOT)}: missing or malformed YAML frontmatter")
        return
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        err(f"{path.relative_to(ROOT)}: frontmatter YAML error: {e}")
        return
    if not isinstance(fm, dict):
        err(f"{path.relative_to(ROOT)}: frontmatter is not a mapping")
        return
    for k in ("name", "description"):
        if not fm.get(k):
            err(f"{path.relative_to(ROOT)}: missing or empty '{k}' in frontmatter")
    if not m.group(2).strip():
        warn(f"{path.relative_to(ROOT)}: SKILL.md body is empty")
    checked["skill_md"] += 1


def main() -> int:
    check_marketplace()

    for skill_md in sorted(ROOT.glob("plugins/**/SKILL.md")):
        check_skill_md(skill_md)
    for skill_md in sorted(ROOT.glob("skills/*/SKILL.md")):
        check_skill_md(skill_md)

    print(
        f"checked: 1 marketplace, {checked['plugin_json']} plugin.json, "
        f"{checked['skill_md']} SKILL.md files"
    )
    if warnings:
        print(f"\n{len(warnings)} warning(s):")
        for w in warnings:
            print(f"  WARN  {w}")
    if errors:
        print(f"\n{len(errors)} error(s):", file=sys.stderr)
        for e in errors:
            print(f"  FAIL  {e}", file=sys.stderr)
        return 1
    print("\nOK — no errors")
    return 0


if __name__ == "__main__":
    sys.exit(main())
