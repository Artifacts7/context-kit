# Roadmap — what we have to build

_Status against the 12-step journey + cross-cutting work. Updated 2026-06-30._

Legend: ✅ built & validated · 🟡 method drafted / prototyped · 🟦 designed (spec only) · ⬜ not started

## The journey

| Step | Stage | Status | Notes |
|---|---|---|---|
| 0 | Connect sources | ✅ | `onboard` skill (v1: URL + source pointers; full Cowork multi-connector deferred) |
| 1 | Describe (intake) | ✅ | `method/intake.md` + onboard skill |
| 2 | Stated identity | ✅ | `substack_identity.py`; validated on Artifacts |
| **3** | **Ingest corpus** | **✅** | **`extract-corpus` skill + fetcher; validated on 4 Substacks** |
| — | **PHASE A COMPLETE** | **✅** | **setup → ingest milestone done; produces the 3 views (said/stated/shown)** |
| 4 | Distill subject | ✅ | run on real corpus; sharp, evidence-cited read |
| 5 | Reconcile (said/stated/shown) | ✅ | run + resolved on Artifacts (G1–G5) |
| 6 | **Newsletter Brief** (Milestone 1) | ✅ | **confirmed source-of-truth Brief — MILESTONE 1 COMPLETE** |
| 7 | Distill voice | ✅ | run on real prose → voice-profile: rules + examples + checklist + naturalness layer |
| 8 | Calibrate (Milestone 2) | 🟡 | one round done → fed the naturalness layer (D21); full trust-gate / blind-test **deferred by Lorenzo** |
| — | **MILESTONE 2** | **✅\*** | **Voice Profile built as a guardrail (D21); calibration gate deferred** |
| 9 | Pre-set skills | ✅ | **D22/D23: kit ships them (zero authoring). Three-pass loop: `brainstorm` (ideate) · `editorial-review` (substance/intention, reads Brief) · `polish` (voice/language, reads Profile). Assist, not generate (D21)** |
| 10 | Write loop | ⬜ | the value loop — **assist, not generate; prose stays the writer's** |
| 11 | Compound | ✅ | `compound` skill — session-end ritual; folds 3–5 essentials IN PLACE into Brief/Profile + changelog (D24) |
| 12 | Prune / reiterate | ✅ | `prune` skill — dedupe, resolve drift/era, keep under budget; pivots edit the Brief first (D24) |

## Cross-cutting

| Item | Status | Notes |
|---|---|---|
| Build-in-public docs (concept/decisions/devlog/Q) | ✅ ongoing | the trail |
| Method library (`method/`) | ✅ | acquire-corpus, intake, distill-subject, reconcile, brief, voice — all drafted & run on Artifacts |
| Plugin packaging | ✅ | **Claude Code plugin (D25):** `.claude-plugin/plugin.json` + `marketplace.json`, **12 skills** (added `pull-identity`) + 2 bundled tools + a Stop hook. Installable via `/plugin marketplace add`. Tools resolved via `${CLAUDE_SKILL_DIR}`; context → `./newsletter-context/` |
| Repo spin-out (own public GitHub) | 🟡 | structure is plugin-ready + a user README exists; just needs pushing to a public repo. Artifacts dogfood removed (D25) |
| Cowork verification | ⬜ | packaged as a Claude Code plugin; not yet tested running in Cowork |
| Multi-platform extraction (Ghost/Beehiiv/…) | ⬜ | out of scope for v1 (D15) |

## Where we are

**Built and validated on Artifacts: Phase A + Milestone 1 + Milestone 2 (voice profile).**
- **Phase A (0–3):** onboarding, intake, stated identity, corpus extraction — produces the three views (said/stated/shown).
- **Milestone 1 (4–6):** confirmed source-of-truth **Brief**.
- **Milestone 2 (7–8):** an actionable **Voice Profile** with a naturalness layer. Calibration gate deferred by Lorenzo.

**The reframe that defines what's left (D21):** the kit **defends and assists** writing — it does not generate reader-facing prose. So steps 9–12 are guardrail/assist tools (polish, flag AI tells, ideate, structure), not a draft generator. The writing stays the writer's.

## Now → Next → Later

- **DONE:** the full context base — Phase A, the Brief (M1), and the Voice Profile (M2). Together: a generated CLAUDE.md-equivalent (the D20 bar).
- **DONE (this session):** all 12 steps now have a method + skill — including compound (11) & prune (12), the session-end ritual that keeps context improving and lean.
- **NOW (when resumed):** the real productization test — **run the whole kit cold** on a newsletter that isn't Artifacts, end to end. That's what surfaces the gaps dogfooding can't.
- **LATER:** write-loop wiring (10, the connective glue — deferred); **Cowork packaging** (nothing runs there yet); a session-end **hook** to auto-fire `compound`; repo spin-out.

## Critical-path risk — now answered
**Q1 (is voice externalizable?) resolved with a nuance:** yes **as a guardrail** (catch AI texture, preserve idiosyncrasy), no **as a generator** (produces AI cosplay — D21). This is the more defensible and more useful answer, and it sets the design of everything downstream.
