# subagent-forge

A hybrid Claude Code / Claude Desktop marketplace repo combining the best of two research-first plugin ecosystems: **signal-labs** (evidence-backed discovery) and **signal-research-rig** (structured research methodology).

## What is here

- **Marketplace root** at `.claude-plugin/marketplace.json`
- **One installable plugin** at `plugins/subagent-forge/`
- **8 research-first subagents**
- **7 compact helper skills**
- **1 output style** for the main orchestrator
- **1 safety hook** that blocks or escalates risky Bash mutations
- **Audit + rationale docs** explaining what was merged, kept, or cut

## Repo layout

```
subagent-forge/
├── .claude-plugin/marketplace.json
├── plugins/
│   └── subagent-forge/
│       ├── .claude-plugin/plugin.json
│       ├── agents/ (8 files)
│       ├── skills/ (7 directories)
│       ├── hooks/hooks.json
│       ├── scripts/guard_destructive_bash.py
│       ├── styles/research-operator.md
│       └── README.md
├── docs/
│   └── HYBRID-RATIONALE.md
├── scripts/
│   └── smoke_validate.py
├── CHANGELOG.md
├── LICENSE
├── README.md
└── .gitignore
```

## Install locally for testing

```bash
claude plugin validate .
claude plugin marketplace add .
claude plugin install subagent-forge@subagent-forge --scope local
```

## How to use it

After install:
- **Agents** under the `subagent-forge:` namespace in `/agents`
- **Skills** under the `subagent-forge:` namespace when you type `/`
- **Output style**: Enable Subagent Forge from `/config`

## Design choices
- **Research-first**: Focus on evidence gathering and verification
- **Moderate delegation**: Main thread orchestrates; subagents handle search and critique
- **Mostly read-only**: Agents lack Edit/Write access. Safety hook guards Bash
- **Small, opinionated catalog**: Every agent and skill earns its place
- **Explicit downranking**: AI slop, affiliate farms, and abandoned repos are downranked

## Validation

```bash
claude plugin validate .
python scripts/smoke_validate.py
```

## See also

- `docs/HYBRID-RATIONALE.md` — Detailed merge decisions and agent selection rationale
- `CHANGELOG.md` — Version history and changes
