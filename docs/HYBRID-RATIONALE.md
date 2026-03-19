# Hybrid Merge Rationale: signal-labs + signal-research-rig to subagent-forge

## Overview

Two research-first plugin ecosystems were evaluated and merged into **subagent-forge** — a single, opinionated research marketplace for Claude Code and Claude Desktop.

## Source Repositories

### Plugin A: signal-labs
- **Agents:** 7 (product-tool-scout, forum-sentiment-hunter, github-repo-auditor, academic-literature-scout, freshness-checker, qa-critique-analyst, source-verifier)
- **Skills:** 5 (task-packet-builder, research-report-contract, source-triage, rank-and-prune, lessons-ledger)
- **Output Styles:** 1 (Signal Research Operator)
- **Strengths:** Concise agent descriptions, clear evidence hierarchy, strong astroturfing detection
- **Weaknesses:** Minimal ecosystem mapping, no research-brief skill

### Plugin B: signal-research-rig
- **Agents:** 8 (all from Plugin A + directory-repo-mapper)
- **Skills:** 9 (includes Plugin A + spreadsheet-critic, document-structurer, research-brief, paper-to-podcast)
- **Output Styles:** 1 (Research Operator)
- **Strengths:** Ecosystem mapping agent, research-brief skill, document/slide critique tools
- **Weaknesses:** More verbose agent descriptions, skill overlap with user's existing Cowork arsenal

## Merge Decisions

### Agents Kept (8/8)

1. **product-tool-scout** — Plugin A (concise, anti-bullshit framing)
2. **forum-sentiment-hunter** — Plugin A enhanced with astroturfing detection
3. **github-repo-auditor** — Merged both (Plugin A base + Plugin B security checks)
4. **academic-literature-scout** — Plugin A + Plugin B's evidence hierarchy
5. **directory-repo-mapper** — Plugin B (fills critical gap for ecosystem mapping)
6. **freshness-checker** — Plugin A (focused, orchestration-friendly)
7. **qa-critique-analyst** — Merged both (Plugin A base + Plugin B's 8-point framework)
8. **source-verifier** — Plugin A (unique, essential for primary-source verification)

### Skills Kept (7/11)

**Kept:**
1. task-packet-builder — Tight task packets for subagent delegation
2. research-report-contract — Quick/normal/deep/adversarial formats
3. source-triage — Source ranking by credibility and freshness
4. rank-and-prune — High-signal option selection
5. lessons-ledger — Project-local lesson capture
6. research-brief — Vague-to-executable brief conversion (Plugin B, fills gap)
7. spreadsheet-polish — Decision-grade sheet design (Plugin B, replaces spreadsheet-critic)

**Removed:**
- spreadsheet-critic — Overlapped with spreadsheet-polish
- document-structurer — Duplicated orchestrator's synthesis role
- paper-to-podcast — User has document-to-tts-transcript in Cowork
- slides-critique — User has pptx-master in Cowork

## Agent Prompt Calibration

All prompts re-calibrated for Claude 4.5/4.6 with:

1. Removed ALL-CAPS emphasis. Replaced with explained conditionals.
2. Paired hard rules with alternatives. Showed reasoning, not just compliance.
3. Kept instruction count under 150 per agent.
4. Set default intensity to Level 5 (explained conditional).

## What Was NOT Merged

- Business/sales agents (product demand, competitive analysis, SEO)
- Ultra-specialized agents (patent analysis, podcast sponsorship valuation)
- Duplicate output styles (merged into one "Research Operator")

## Directory Structure (Final)

```
subagent-forge/
├── .claude-plugin/marketplace.json
├── plugins/subagent-forge/
│   ├── agents/ (8 agents)
│   ├── skills/ (7 skills)
│   ├── hooks/hooks.json
│   ├── scripts/guard_destructive_bash.py
│   ├── styles/research-operator.md
│   └── README.md
├── docs/HYBRID-RATIONALE.md
├── scripts/smoke_validate.py
├── README.md
├── CHANGELOG.md
├── LICENSE
└── .gitignore
```

## Validation

- smoke_validate.py checks directory structure, JSON validity, required fields
- Spot checks confirmed marketplace.json, plugin.json, agent descriptions
- Installation verified locally
