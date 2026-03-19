#!/usr/bin/env python3
"""Smoke validation for subagent-forge repository."""

import json
import os
import sys
from pathlib import Path

class ValidationError(Exception):
    pass

def validate_marketplace_json():
    path = Path(".claude-plugin/marketplace.json")
    if not path.exists():
        raise ValidationError(f"Missing {path}")
    try:
        with open(path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValidationError(f"Invalid JSON in {path}: {e}")
    if data.get("name") != "subagent-forge":
        raise ValidationError(f"Marketplace name must be 'subagent-forge'")
    plugins = data.get("plugins", [])
    if not plugins:
        raise ValidationError("No plugins defined")
    for plugin in plugins:
        if plugin.get("name") != "subagent-forge":
            raise ValidationError(f"Plugin name must be 'subagent-forge'")

def validate_plugin_json():
    path = Path("plugins/subagent-forge/.claude-plugin/plugin.json")
    if not path.exists():
        raise ValidationError(f"Missing {path}")
    try:
        with open(path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValidationError(f"Invalid JSON in {path}: {e}")
    if data.get("name") != "subagent-forge":
        raise ValidationError(f"Plugin name must be 'subagent-forge'")

def validate_agents():
    agents_dir = Path("plugins/subagent-forge/agents")
    if not agents_dir.exists():
        raise ValidationError(f"Missing agents directory")
    required_agents = [
        "product-tool-scout.md", "forum-sentiment-hunter.md",
        "github-repo-auditor.md", "academic-literature-scout.md",
        "directory-repo-mapper.md", "freshness-checker.md",
        "qa-critique-analyst.md", "source-verifier.md"
    ]
    for agent_file in required_agents:
        path = agents_dir / agent_file
        if not path.exists():
            raise ValidationError(f"Missing agent: {path}")

def validate_skills():
    skills_dir = Path("plugins/subagent-forge/skills")
    if not skills_dir.exists():
        raise ValidationError(f"Missing skills directory")
    required_skills = [
        "task-packet-builder", "research-report-contract", "source-triage",
        "rank-and-prune", "lessons-ledger", "research-brief", "spreadsheet-polish"
    ]
    for skill_name in required_skills:
        skill_dir = skills_dir / skill_name
        if not skill_dir.exists():
            raise ValidationError(f"Missing skill: {skill_dir}")

def validate_hooks():
    hooks_file = Path("plugins/subagent-forge/hooks/hooks.json")
    if not hooks_file.exists():
        raise ValidationError(f"Missing hooks file")
    script_file = Path("plugins/subagent-forge/scripts/guard_destructive_bash.py")
    if not script_file.exists():
        raise ValidationError(f"Missing bash guard script")

def validate_documentation():
    required_docs = [
        Path("README.md"), Path("CHANGELOG.md"), Path("LICENSE"),
        Path("plugins/subagent-forge/README.md")
    ]
    for doc_file in required_docs:
        if not doc_file.exists():
            raise ValidationError(f"Missing {doc_file}")

def main():
    checks = [
        ("Marketplace JSON", validate_marketplace_json),
        ("Plugin JSON", validate_plugin_json),
        ("Agents", validate_agents),
        ("Skills", validate_skills),
        ("Hooks", validate_hooks),
        ("Documentation", validate_documentation),
    ]
    print("Validating subagent-forge repository...")
    failed = False
    for check_name, check_func in checks:
        try:
            check_func()
            print(f"OK {check_name}")
        except ValidationError as e:
            print(f"FAIL {check_name}: {e}")
            failed = True
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
