---
name: spreadsheet-polish
description: Convert messy comparisons or findings into a clean spreadsheet plan, scoring model, and review checklist.
argument-hint: [comparison topic or raw findings]
disable-model-invocation: true
allowed-tools: Read, Grep, Glob
model: sonnet
---

Turn this material into a spreadsheet or table design that is useful for real decisions:

$ARGUMENTS

## What to produce

Return a structured plan with these sections:

1. **Sheet goal**
   - what decision the sheet supports

2. **Recommended tabs or tables**
   - main comparison tab
   - supporting evidence tab
   - notes / risks / sources tabs when useful

3. **Columns**
   - exact column recommendations
   - which columns are required versus optional

4. **Scoring logic**
   - suggested weights or scoring rubric if scoring makes sense
   - what should *not* be reduced to a fake score

5. **Normalization notes**
   - how to handle missing data, stale data, and incomparable fields

6. **Quality-control checks**
   - duplicate detection
   - stale-source detection
   - version/date tracking
   - source-traceability checks

7. **Executive view**
   - what a top summary row or decision view should show

## Rules

- Favor auditability over spreadsheet theater.
- Do not force numeric scoring where qualitative judgment is better.
- Include source/date tracking whenever freshness matters.
