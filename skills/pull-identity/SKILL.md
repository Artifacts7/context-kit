---
name: pull-identity
description: >
  Pull a Substack newsletter's STATED identity — name, tagline, about page, recent subjects —
  the high-signal context the writer already wrote about themselves. Step 2 of the Context Kit,
  loaded BEFORE the bulk corpus (progressive loading). Use for "pull my newsletter's about page",
  "get the stated identity", or as part of onboarding.
allowed-tools: Bash(python3 *)
---

# Pull stated identity (step 2)

Cheap, true, high-signal context the author already wrote — loaded before the heavy corpus.

## Run
```
python3 ${CLAUDE_SKILL_DIR}/substack_identity.py <publication-url> ./newsletter-context
```
Writes `newsletter-context/identity-stated.md` (name · tagline · about page · recent subjects).
Works for vanilla and custom-domain Substacks; free newsletters only (v1).

## After
Read it back and note any gap vs. the writer's own description (`newsletter-context/seed-context.md`)
— flag it for the `reconcile` step; don't resolve it now.

## Precondition / sequence
Run after onboard (0) and describe (1), before `extract-corpus` (3). Order: said → stated → shown.
