# Devlog

_Dated progress. Raw material for build-in-public posts. Newest first._

## 2026-06-30 — Day 4: packaged as a plug-and-play Claude Code plugin (D25)

- Made it installable: `.claude-plugin/plugin.json` + `marketplace.json` (repo root = the plugin) → `/plugin marketplace add <repo>` then `/plugin install context-kit@context-kit`.
- Fixed the real install-blockers (confirmed against current Claude Code docs): bundled each python tool **inside its skill** and referenced via `${CLAUDE_SKILL_DIR}` (plain relative paths don't resolve in skill content); made every SKILL.md self-contained (dropped runtime `method/` deps — methods are now dev reference); defined the **`./newsletter-context/`** convention for where a user's context lives; added a **Stop hook** to nudge `compound`.
- Added a **`pull-identity`** skill so step 2 is a proper unit → **12 skills**.
- **Removed the Artifacts dogfood** from the repo (per decision); a user's context is generated fresh, never shipped. Wrote a user-facing README; kept `docs/` + `method/` as the build-in-public trail (plugin loader ignores them).
- Honest remaining gaps: not yet pushed to a public GitHub repo; not yet tested running inside Cowork; the cold-run on a non-Artifacts newsletter still stands.

## 2026-06-30 — Day 3: Milestone 2 — voice distilled, calibration pending

- Ran step 7 (distill voice) on the raw English prose via subagent → voice-profile: operational, binary-checkable rules + verbatim examples + an anti-slop list + a runnable VOICE CHECKLIST. Actionable by downstream skills, as required.
- Best catch: the **em-dash trap** — Lorenzo publicly rails against AI's unspaced "—" tells, but his own *spaced-hyphen* asides are core voice. A naive polish skill would "fix" his voice into the tell he hates. Profile encodes the distinction + "preserve idiosyncrasy, fix only true typos."
- Pulled Lorenzo's own stated anti-slop list (no "delve", no "this-not-that", no empty epigrams) from his issues into the DO-NOT section.
- Generated a step-8 calibration sample (opening + 3 titles). **Pending: Lorenzo's reaction + the blind test — the actual Q1 answer.**

## 2026-06-30 — Day 3g: compound & prune — context that improves with use (D24)

- Built the last two steps: **`compound`** (11) and **`prune`** (12), with methods.
- Key design call (D24): compounded learnings land **IN PLACE** in the canonical Brief / Voice Profile (routed by section) — not a side note — because the skills read those files, so that's where a learning takes effect. Added a **Changelog footer** to both canonical files (modeled in the Artifacts dogfood).
- `compound` = session-end ritual proposing the **3–5 key essential, generalizing** items (writer approves); `prune` = counterweight keeping files lean (anti-bloat: sharpen over add, skip one-offs).
- **All 12 steps now have a method + skill (11 skills, 8 methods).** Remaining is productization, not design: cold-run on a stranger's newsletter, Cowork packaging, a session-end hook to auto-fire compound, write-loop wiring.

## 2026-06-30 — Day 3f: added the missing middle — editorial-review (D23)

- Lorenzo's question: are two skills enough to help writing? No — `brainstorm` (ideate) + `polish` (language) skipped the highest-value middle: does the piece *work* and *serve the intention*.
- Added **`editorial-review`** — a substance/intention pass grounded in the **Brief** (interface-moment sharpness, who-decided clarity, the "So, what?", objective-fit, structure, substance-overlap). Kept **`polish` language-only** (it now hands substance off to editorial-review).
- Writing help is now a **three-pass loop (D23):** ideate (brainstorm) → substance (editorial-review, reads Brief) → language (polish, reads Voice Profile). Mirrors structural-edit vs. line-edit. All assist, none rewrite (D21).
- 9 skills total now.

## 2026-06-30 — Day 3e: dogfooded the pre-set skills on Artifacts

- Showed both pre-sets adapting to Artifacts purely via its generated context:
  - example-brainstorm — 3 angles, each grounded in the Brief's lenses + objectives (notably advancing G1 civic-tech), with overlap flags vs. real past issues. Newsletter-specific with zero authoring.
  - example-polish — ran the voice guardrail on the earlier AI-cosplay sample. It **independently caught the AI texture (6/6 naturalness fails)** and correctly flagged the unspaced em-dash while preserving the spaced-hyphen asides + caption-fragment. The guardrail works.
- Updated README with the full dogfood index. The Artifacts worked example is now end-to-end (3 views → Brief → Voice Profile → both skills in action).

## 2026-06-30 — Day 3d: Phase C step 9 — pre-set skills (D22)

- Product decision: don't ask the writer to author skills (too much load — recreates the cold-start one level up). The kit **ships pre-set, context-bound skills** that auto-read the Brief + Voice Profile.
- Built the two v1 pre-sets: **`brainstorm`** (context-aware ideation partner, grounded in Brief + archive, flags overlap) and **`polish`** (the generalized, white-label `artifacts-polish` — runs the voice checklist, preserves idiosyncrasy, never sanitizes). Both assist/defend (D21).
- Now **8 skills** total (0–9 covered). Remaining: write-loop wiring (10), compound (11), prune (12), Cowork packaging, and the cold-run-on-a-new-newsletter test.

## 2026-06-30 — Day 3c: productized steps 4–7 as skills

- Packaged the model-driven steps as invokable skills (same shape as extract-corpus/onboard), each wrapping its method doc: `distill-subject` (4), `reconcile` (5), `brief` (6), `distill-voice` (7–8).
- Now **6 skills total** cover steps 0–8. Remaining: the front half is no longer "method-only" — it's skill-packaged. Steps 9–12 still todo; nothing runs in Cowork yet.
- Honest gap that remains: "validated as method on Artifacts" ≠ "tested as a skill by a stranger." The skills encode the procedure; they haven't been run cold by a new user/newsletter.

## 2026-06-30 — Day 3b: the AI-cosplay problem → defend, don't generate (D21)

- Calibration verdict from Lorenzo: "sounds like me but reads AI-generated — I don't want users facing that." The crucial finding of the project.
- Diagnosis: the sample ticked ~7 signatures in 8 lines — the **density itself is the AI tell**. It even committed the escalating-triplet faux-aphorism the profile forbids. Manufactured simile, no real specifics, too smooth.
- **Reframe (D21):** the kit **defends/assists** writing — it does not generate publish-ready prose. Voice Profile = guardrail (polish, flag AI texture, preserve idiosyncrasy), prose stays the writer's. Matches Lorenzo's own "writing remains mine."
- Added a **Naturalness / anti-AI-texture layer** (voice-profile §9) targeting texture not vocabulary, with a read-aloud test and 6 naturalness checks.
- Q1 nuance: voice is *externalizable as a guardrail* (catching/preserving), not as a *generator*. That's the honest, and more valuable, answer.

## 2026-06-30 — Day 2c: Brief v2 — richer, identity-mode (D20)

- Lorenzo's critique: the v1 Brief was thin vs. his hand-written CLAUDE.md given the depth of analysis behind it. Correct — v1 over-compressed its own source.
- Rewrote the Brief in **declarative identity-mode**, no length limit: explicit topics + *how each is treated* + named patterns (built-for-vs-now, commission/omission, the "So what?" pivot…) + the signature vocabulary (meta-writing, "screens don't lie," the architecture metaphor). Pulled the texture from subject-observed back IN.
- Set the project's **quality bar = a strong hand-written CLAUDE.md** (D20). Proposed eval: blind compare generated Brief vs. Lorenzo's CLAUDE.md.
- Updated the brief method spec accordingly.

## 2026-06-30 — Day 2b: MILESTONE 1 COMPLETE ✅

- Lorenzo answered the reconcile gate (G1–G5): G1 grow civic/democratic tech · G2 AI/cognition is a side vein not a pillar · G3 meta-thesis rejected (over-read) · G4 preserve neutrality · G5 tagline = "Stories & Ideas on the Design of Technology."
- Finalized the Newsletter Brief into a **confirmed source of truth**. Recorded resolutions in reconcile.
- **The reconcile engine proved its worth:** G1 turned a thinning topic into a forward objective (direction the corpus alone couldn't give), and the gate caught G3 (agent over-reach). Exactly the said/stated/shown→aspiration loop the design bet on (D10).
- **Q1 status:** subject + voice-character extraction lands as true-to-writer. The harder half — operational *voice* (M2) — is next.

## 2026-06-28 — Day 2: Milestone 1 run on the real Artifacts corpus

- Designed M1's three methods ([distill-subject](../method/distill-subject.md), [reconcile](../method/reconcile.md), [brief](../method/brief.md)) and defined the Brief as the source-of-truth doc (D19: about + how-written-so-far + objectives/vision).
- Ran step 4 for real via a distillation subagent on 15 recent + 6 older English issues. **Strong Q1 signal:** the read is specific and true — found the "built-for-vs-now" lens, the "So, what?" pivot, the recursive *process-over-output* unity across writing/code/platforms, and the quiet Anthropic partisanship. Not slop.
- Produced subject-observed, reconcile (5 gaps as open questions), and a draft Newsletter Brief.
- **Gate pending:** Lorenzo's answers to G1–G5 turn the provisional Brief into a confirmed source of truth. His reaction is the real test of M1.

## 2026-06-28 — Day 1g: fixed sequencing — onboard ≠ fetch (D18)

- Lorenzo caught a design error: I'd bundled the heavy corpus fetch into the `onboard` skill. Onboard should be "where work lives," not extraction.
- Corrected: onboard = **step 0 only** (tools / knowledge homes / how I work today), explicitly **no corpus fetch**. The read (`extract-corpus`) is now a **gated last step**, run only after describe (1) + stated identity (2).
- Order is now clean: **said → stated → shown/read → Milestone 1.** Added the gate to the journey and a precondition to the extract-corpus skill.

## 2026-06-28 — Day 1f: Phase A complete (setup → ingest) ✅

- Built the rest of Phase A so the front-to-ingest milestone is fully runnable (D17):
  - **Step 2** `substack_identity.py` — pulls name/tagline/about/recent-subjects. Validated on Artifacts: the about page handed over the full thesis, the 4-section structure, even the Langdon Winner name origin. Premium high-signal context, as D8 predicted.
  - **Step 1** `method/intake.md` — the non-derivable question set + seed-context template.
  - **Step 0 + orchestration** `onboard` skill — runs 0→3 in light→heavy order, composing extract-corpus.
- Dogfood now has all **three views** for Artifacts: said (seed-context), stated (identity-stated), shown (corpus). Ready for the reconcile step.
- Live validation of the reconcile premise: RSS tagline ("Tech, Information & Interfaces") ≠ about-page thesis ("the Design of Technology") — a real said/stated gap step 5 will surface.
- Minor polish debt: about-page cleaner still lets some nav/footer text through.

## 2026-06-28 — Day 1e: baked into a white-labeled skill + roadmap

- Packaged extraction as the [`extract-corpus`](../skills/extract-corpus/SKILL.md) skill (D16). **White-labeled:** removed the Artifacts-specific appendix markers from the tool; they're now passed per-newsletter (`--appendix-markers`) and the skill detects them at runtime. No-marker default keeps the whole essay in body (no false splits) — verified.
- Wrote the [roadmap](roadmap.md): step 3 ✅ done; Milestone 1 (subject→reconcile→brief) is NOW; voice (Q1, the make-or-break) is NEXT.
- Net: the load-bearing hurdle (corpus) is closed and reusable. Critical-path risk remains unchanged and untouched — **is voice externalizable?**

## 2026-06-28 — Day 1d: extraction VALIDATED for Substack v1 ✅

- Scoped v1 to **Substack only** (D15) — validation on one platform is now sufficient.
- Closed the gaps the audit found: **CTA-leak bug fixed** (47 files → 0), **backoff confirmed** (33 errors → 0; 78/80 full-prose), **graceful non-Substack handling** added (Platformer 404 → clean exit, no crash).
- **Generalization proven** beyond Artifacts: Astral Codex Ten (custom domain, paid-post detection ✅), Gary Marcus (vanilla ✅). 4 publications total.
- Verdict: extraction capability is **ready to bake into the skill.** Documented v1 limits: paid posts → preview only; appendix segmentation tuned per-newsletter.
- Process note: the audit caught me claiming "done" before inspecting outputs. Lesson logged — validate by looking at the artifact, not the exit code.

## 2026-06-28 — Day 1c: acquisition works — and the corpus is bigger & bilingual

- Built a real fetcher ([`tools/substack_fetch.py`](../tools/substack_fetch.py)) and ran it on Artifacts. **The hurdle is cleared:** for a free Substack, the **URL alone** yields the full archive at full fidelity (archive API → per-post `body_html` → normalize → segment → manifest). Zero user action.
- **Two surprises the tool found on its own:** the archive is **80 posts** (not 23 — single API calls cap; you must paginate), back to Sept 2023; and it's **bilingual** — Italian 2023→mid-2024, then English. The tool surfaced Lorenzo's language pivot without being told.
- **Real constraints logged:** rate-limiting (429 after ~46 posts → added exponential backoff); paid posts need export.
- Strategic shift: flipped **D13** — API scrape is the zero-friction *default* (fixes the step-3 adoption worry), export is the upgrade. Sharpened **Q4** to include era/language weighting: voice cannot be averaged across phases/languages.
- 46 full-prose issues banked; `dogfood/artifacts/corpus-manifest.json` committed as evidence. Clean corpus now exists to re-run distillation honestly.
- **LinkedIn angle:** "I pointed the tool at my own newsletter and it told me something I knew but never wrote down: I used to write in Italian. The archive remembers what you were."

## 2026-06-28 — Day 1b: the corpus problem is real

- Lorenzo's catch: I'd dogfooded distillation on a corpus that was already clean/summarized — users don't have that. Went to the live Artifacts feed to face reality.
- **Findings:** RSS `/feed` returns only ~3 recent posts (full prose); the archive page is JS-truncated (~15 of ~30+); newest post is June 2026 (my local corpus was stale); real issues have recurring sections (*Bookshelf*, *Nerding*, *☕*) my summaries stripped.
- Wrote [`method/acquire-corpus.md`](../method/acquire-corpus.md): acquire (export-first) → normalize → **segment into zones** → fidelity-tag → manifest.
- Logged **D13** (acquisition strategy) and **D14** (zone segmentation). Marked the subject read **provisional** — built on a bad corpus; it tested the method, not Artifacts.
- Lesson: ingestion isn't plumbing; corpus quality caps everything downstream. Even *subject* degraded (missed format signature), not just voice.

## 2026-06-28 — Day 1: first real distillation (dogfood)

- Ran **step 4 (distill subject)** for real on the 14-issue Artifacts corpus. Output: `dogfood/artifacts/subject-observed.md`. First test of the core bet.
- Extracted the **method** into [`method/distill-subject.md`](../method/distill-subject.md) — the reusable IP, with anti-slop tests (substitution / citation / surprise / disagreement-surface).
- Finding → **D12 (corpus fidelity):** subject distills fine from summaries; voice needs raw prose. Several local files are condensed, so voice work must pull raw issue text from the feed first.
- Distinguished **topic vs. lens** as a method principle — the lens ("reads interfaces as political texts," the "what vs. how" gap) is what makes a read feel true-to-writer vs. generic.
- **Pending:** Lorenzo's verdict on whether the read is sharp or slop (Q1). That's the gate.

## 2026-06-28 — Day 0e: Milestone 1 internals

- Detailed M1 (steps 4–6): distill subject → reconcile → Newsletter Brief.
- **Reconcile mechanism:** three-way diff (said/stated/shown) → 4 gap types → user's answer classifies each gap as aspiration / drift / latent-strength / noise. That classification is what makes the context *directional*.
- Logged **D11** (distillation claims must cite corpus evidence — falsifiable, not vibes) and **Q7** (anchoring risk: agent's read may bias the user's answers).
- Rejected splitting the Brief into fixed is/becoming sections (proposed D12) — keep the Brief's shape flexible.

## 2026-06-28 — Day 0d: milestones + the reconcile engine

- Restructured the journey around **two value milestones** (D9): **M1 Newsletter Brief** ("what it's about") then **M2 Voice Profile** ("how it's written"). Substance before style; value delivered after M1 (user can brainstorm before any voice work is done).
- Added the **reconcile beat** (D10): distillation compares what the user *said* vs. what the page *states* vs. what the corpus *shows*, surfaces gaps, and asks about them.
- Sharpest idea of the day: the **corpus is descriptive** (what you *were*); the **discrepancy dialogue is aspirational** (what you *want to be*). A pure-corpus distill can only mirror the past — direction only enters through the conversation. Strong LinkedIn angle.
- Two explicit trust gates now: M1 confirm (step 6), M2 calibrate (step 8).

## 2026-06-28 — Day 0c: progressive loading

- Refined the journey to **10 steps** (0–9). Split install into multi-source connect (0) and split old "ingest" into three layers: **describe (1) → stated identity (2) → corpus (3)**.
- New design principle logged as **D8 — progressive context loading**: build context light → heavy, high-signal first (user's punchline + the newsletter's own Substack about/tiers), bulk corpus last, to avoid cluttering context from the start.
- Nice property: the newsletter's *self-description* is premium context the author already wrote — free, true, cheap.

## 2026-06-28 — Day 0b: user journey

- Sketched the end-to-end user journey ([user-journey.md](user-journey.md)): 9 granular steps from Install → Reiterate, one artifact per step, mapped onto the lifecycle.
- Two friction hotspots named: steps 0–1 (install + intake = where adoption dies) and step 4 (calibrate = where trust is won/lost). Both must stay ruthlessly short.
- Confirms the build order: the journey's spine is step 3 (distill) → step 4 (calibrate). Validates building the distillation method next.

## 2026-06-28 — Day 0: framing + scaffold

- Reframed the cold-start problem from "people don't bother generating context" to an **attribution problem**: they run AI raw, get slop, blame the tool, churn. Context is the unrecognized lever.
- Landed the core insight: a writer's **archive is the context**; the job is to *distill*, not author.
- Recognized the pattern is **already proven by hand in Artifacts** (distilled `CLAUDE.md` + retained corpus + polish/curation skills).
- Chose scope (newsletter/voice), surface (Cowork), and the lifecycle (Bootstrap → Calibrate → Encode → Write → Compound → Prune).
- Set up build-in-public scaffold: README, concept, decisions, devlog, open-questions.

**Next:** draft the distillation method — the prompt/process that takes a corpus and outputs a sharp, Artifacts-quality voice profile. Test on the Artifacts archive (`https://artifactstech.substack.com/feed`) as control.

**LinkedIn angle (D7):** the reframe itself — "Most people who bounce off AI agents blame the tool. The real problem is the cold start: they run it raw, get slop, and never learn that context is the lever." Pair with the insight that your archive *is* the context. Open the repo and invite the first follow-along readers.
