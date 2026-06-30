# User journey

_The path from installing the kit to iterating on issues. Granular; one artifact per step._

**Two design principles:**
- **Progressive context loading (D8):** build context light → heavy. Cheap high-signal first, bulk corpus last.
- **Milestones, value-early (D9):** understand *what it's about* before *how it's written*. Each milestone ends in a concise, confirmable deliverable and unlocks real use.

**Build status** (mirrors [roadmap.md](roadmap.md)): ✅ built & validated · 🟡 method drafted / prototyped · 🟦 designed (spec only) · ⬜ not started

---

## Phase A — Setup & ingest (light → heavy)

> **Sequencing gate (D18):** the corpus read (step 3) is the **last** beat — run only after
> the writer has been onboarded (0), described their newsletter (1), and we've pulled the
> stated identity (2). Onboard organizes *where work lives*; it never fetches. Order is
> said → stated → **shown/read**, then Milestone 1.

### 0 — Connect sources ✅ — _[`onboard` skill](../skills/onboard/SKILL.md) (v1: URL + source pointers; full multi-connector deferred to Cowork)_
- **User:** adds Context Kit to Cowork; connects **all** knowledge homes — Substack, Drive, Notion, notes. Agent orchestrates across them.
- **→** connected workspace.

### 1 — Describe (your own words) ✅ — _[intake method](../method/intake.md) + onboard skill_
- **Agent:** asks for a **punchline + a few lines** (what it is, who it's for, the thesis) plus non-derivable bits (cadence, topics you'd never touch, an issue you're proud of vs. one you'd disown).
- **→** `seed-context.md`.

### 2 — Pull the stated identity (light, high-signal) ✅ — _skill: [`pull-identity`](../skills/pull-identity/SKILL.md) (bundles substack_identity.py); validated on Artifacts_
- **Agent:** pulls what the newsletter *already says about itself* — Substack about page, tagline, subscription tiers, recent subjects.
- **→** `identity-stated.md`.

### 3 — Ingest the corpus (heavy, last) ✅ — _built: [`extract-corpus` skill](../skills/extract-corpus/SKILL.md) · [method](../method/acquire-corpus.md)_
- **User:** provides the archive — ideally the **platform export** (Substack ZIP = full coverage + fidelity); RSS only covers the recent few.
- **Agent:** acquires → normalizes (HTML/boilerplate) → **segments into zones** (body vs. Save-for-Later/Bookshelf/etc., D14) → fidelity-tags → reports a manifest (count, date range, what's excluded).
- **User:** scopes out weak early issues.
- **→** `/corpus` + manifest.

---

## ▶ MILESTONE 1 — "What the newsletter is about"
_Unlocks: discussing ideas, testing angles, planning issues — before any voice work._

### 4 — Distill the subject ✅ — _skill: [`distill-subject`](../skills/distill-subject/SKILL.md) · [method](../method/distill-subject.md) · run → subject-observed_
- **Agent:** forms its **own** read of the newsletter from the corpus — themes, angle, audience, positioning, what's central vs. occasional.
- **→** `subject-observed.md`.

### 5 — Reconcile (the discrepancy dialogue) ✅ ⟵ the engine _skill: [`reconcile`](../skills/reconcile/SKILL.md) · [method](../method/reconcile.md) · run + resolved (G1–G5)_
- **Agent:** compares the three views — what you **said** (1), what the page **states** (2), what the corpus **shows** (4) — surfaces the gaps, and asks you about each.
- **User:** answers. This resolves not just what the newsletter **is** but what it **wants to be**.
- _Why it matters: the corpus is descriptive (what you were); this dialogue is the only place **aspiration** (what you want to be) enters the context._
- **→** captured tensions + direction.

### 6 — Consolidate → **Deliverable: Newsletter Brief** ✅ — _skill: [`brief`](../skills/brief/SKILL.md) · [method](../method/brief.md) · confirmed Brief — MILESTONE 1 COMPLETE_
- **Agent:** smart, concise consolidation — "This is what your newsletter is about, and where it's heading." Partial-but-clear; explicitly iterable.
- **Gate:** user confirms.
- **→** `newsletter-brief.md`. ▸ first milestone shipped — user can now brainstorm with the agent.

---

## ▶ MILESTONE 2 — "How the newsletter is written"
_Unlocks: drafting in-voice._

### 7 — Distill voice / style ✅ — _skill: [`distill-voice`](../skills/distill-voice/SKILL.md) · [method](../method/voice.md) · run → voice-profile (rules + checklist + naturalness layer)_
- **Agent:** *specific, falsifiable* rules — register, opening/closing moves, title/subtitle conventions, signature devices, what's avoided — + a representative retained corpus subset.
- **→** `voice-profile.md`.

### 8 — Calibrate / eval 🟡 ⟵ trust gate _(one round done: sample → "sounds like me but reads AI" → fed the naturalness layer + reframe (D21); full gate/blind-test **deferred by Lorenzo**)_
- **Agent:** generates a sample (an opening + 3 candidate titles); **user** reacts (dead-on / too generic / "I'd never say X"); agent revises. Optional blind test (Q1).
- **Gate:** user signs off.
- **→** confirmed `voice-profile.md`. ▸ second milestone shipped — user can now draft.

---

## Phase C — Produce & compound

### 9 — Pre-set skills ✅ — _(D22: kit ships them; zero authoring by the writer)_
- The kit ships **pre-set, context-bound** skills that auto-read the Brief + Voice Profile — no authoring load (D22). They form a **three-pass writing loop** (D23): ideate · substance · language.
  - **[`brainstorm`](../skills/brainstorm/SKILL.md)** — ideation partner: grounds angles in the Brief + objectives, finds the interface moment, flags overlap with past issues.
  - **[`editorial-review`](../skills/editorial-review/SKILL.md)** — the **substance & intention** pass (reads the *Brief*): is the interface moment sharp, is it clear who decided, is there a real "So, what?", does it serve an objective or drift? The highest-value editorial help.
  - **[`polish`](../skills/polish/SKILL.md)** — the **voice/language** guardrail (reads the *Voice Profile*): runs the checklist, flags AI texture, preserves idiosyncrasy, fixes only typos.
- **None generate reader-facing prose (D21).** More pre-sets can follow (e.g. save-for-later).

### 10 — The write loop (assist, not generate) ⬜
- `brainstorm` (angle, vs. past coverage) → **you draft** → **`editorial-review`** (substance/intention, vs. the Brief) → **`polish`** (voice/language, vs. the Voice Profile) → curate Save for Later. The prose stays yours; the agent is sparring partner, structural editor, and guardrail. **→** issue shipped. _(Skills exist; "wiring" = the connective glue, deferred.)_

### 11 — Compound ✅ — _skill: [`compound`](../skills/compound/SKILL.md) · [method](../method/compound.md)_
- **Session-end ritual (D24):** scans the session, proposes the **3–5 key essential** generalizing items, and — on the writer's approval — folds them **in place** into the Brief / Voice Profile (routed by section) + a changelog entry. Context improves with use; zero authoring burden. Anti-bloat: sharpen over add; skip one-offs.

### 12 — Prune / reiterate ✅ — _skill: [`prune`](../skills/prune/SKILL.md) · [method](../method/prune.md)_
- The counterweight: dedupe, resolve drift/era (Q4), drop stale, keep each file under a soft budget. **Pivots edit the Brief first**, deliberately, then the work follows. Each shipped issue can also re-enter the corpus for periodic re-distill (4/7).

---

**Friction watch:** steps 0–2 are where adoption dies. Steps **6** and **8** are the two trust gates — the two moments the user decides whether the agent "gets it." Keep all of them short.
