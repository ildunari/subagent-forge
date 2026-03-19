# Changelog

All notable changes to subagent-forge are documented here.

## [1.0.0] - 2026-03-19

### Created
- Initial hybrid marketplace combining signal-labs and signal-research-rig

### Agents (8)
- product-tool-scout — High-signal product and tool discovery
- forum-sentiment-hunter — Real user signal extraction with astroturfing detection
- github-repo-auditor — Repository health audit with security checks
- academic-literature-scout — Literature discovery with evidence hierarchy
- directory-repo-mapper — Ecosystem mapping and clustering
- freshness-checker — Version and release status verification
- qa-critique-analyst — Adversarial critique with 8 priority checks
- source-verifier — Primary-source claim verification

### Skills (7)
- task-packet-builder — Task packet design for subagents
- research-report-contract — Quick/normal/deep/adversarial report formats
- source-triage — Source credibility and freshness ranking
- rank-and-prune — High-signal option selection
- lessons-ledger — Project-local learning capture
- research-brief — Vague-to-executable brief conversion
- spreadsheet-polish — Decision-grade sheet design

### Output Style
- Signal Research Operator — Research-first orchestration

### Infrastructure
- Bash guard hook for destructive command detection
- Smoke validation script
- MIT license
- Full documentation

### Hybrid Merge Decisions
- Kept Plugin A product-tool-scout (better conciseness, removed underdog bias)
- Enhanced forum-sentiment-hunter with astroturfing detection
- Added security checks to github-repo-auditor
- Merged evidence hierarchy into academic-literature-scout
- Promoted directory-repo-mapper from Plugin B
- Preserved freshness-checker from Plugin A
- Added 8-point critique framework to qa-critique-analyst
- Kept unique source-verifier from Plugin A
- Added research-brief from Plugin B
- Replaced spreadsheet-critic with spreadsheet-polish
- Removed 4 skills with overlaps

### Calibration
- Removed ALL-CAPS emphasis across all prompts
- Applied explained conditionals throughout
- Paired hard rules with alternatives
- Kept instruction count under 150 per agent
- Set default intensity to Level 5

### Removed from Source Repos
- paper-to-podcast
- slides-critique
- spreadsheet-critic
- document-structurer
- Business, SEO, and marketing agents
