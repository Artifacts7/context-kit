---
name: prune
description: >
  Keep the writer's context lean and current — the counterweight to compound. Dedupe overlapping
  rules, resolve drift/era, drop stale entries, and handle pivots (edit the Brief first). Run
  periodically or when a context file gets bloated. Use for "prune my context", "clean up the
  brief/voice profile", "my context is getting bloated", "we've pivoted — update the source of truth".
---

# Prune / iterate (step 12) — keep it sharp

Context that only grows rots. This trims the canonical files so they stay a trustworthy working
reference.

## Reads / writes
`newsletter-context/newsletter-brief.md` + `newsletter-context/voice-profile.md` (edits in place; trims the changelog).

## Procedure
1. **Dedupe & merge** overlapping rules/entries.
2. **Resolve drift/era** (Q4): retire/down-weight old-era signal; on contradictions, newer practice wins — or ask.
3. **Drop the stale:** rules that no longer fire, objectives met/abandoned, resolved tensions.
4. **Pivot:** edit the **Brief first**, deliberately, then re-confirm with the writer — the source of truth changes on purpose, never by drift.
5. **Trim the changelog** to a useful history.

## Budget
Each file is a working reference, not an archive — keep it under a soft size budget. If `compound`
keeps adding, prune before adding more.

## Boundary
Cleans context only; never touches published work. Pivots are confirmed with the writer, not assumed.
