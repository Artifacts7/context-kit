# Decision log

_ADR-lite. Newest first. Each entry: what we decided, why, and what would reverse it._

## 2026-06-28 — Founding decisions

### D25 — Packaged as a Claude Code plugin; repo root is the plugin; Artifacts dogfood removed
Distributed as a **Claude Code plugin** (`.claude-plugin/plugin.json` + `marketplace.json` at the repo root, source `.`) so users `/plugin marketplace add <repo>` then `/plugin install`. Skills load namespaced (`/context-kit:*`). Mechanics: tools are **bundled inside the skill that uses them** and referenced via `${CLAUDE_SKILL_DIR}` (plain relative paths don't resolve in skill content); each SKILL.md is **self-contained** (method docs are dev reference, not runtime deps); generated context lands in the user's **`./newsletter-context/`** (defined convention); a **Stop hook** nudges `compound` at session end. `docs/` + `method/` stay in the repo as build-in-public (the plugin loader ignores them). The **Artifacts dogfood was removed** — a user's context is generated fresh, never shipped. Added a `pull-identity` skill so step 2 is a proper unit (→ 12 skills).
**Reverses if:** Cowork needs a different package shape than a Claude Code plugin.

### D24 — Compound & prune edit the canonical context IN PLACE, with a changelog footer
Compounded learnings land **in place** in the Brief / Voice Profile (routed by section), not in a side note — because the skills read those files, so that's the only place a learning takes effect. Each canonical file carries a **Changelog** footer (date · what · why) for traceability and as prune's target. `compound` is a **session-end ritual** proposing the **3–5 key essential, generalizing** items (writer approves; never silent); `prune` is the counterweight keeping files under a soft size budget. Anti-bloat: sharpen existing rules over adding new ones; skip one-offs; prune before compounding when a file is full.
**Reverses if:** in-place edits prove risky enough to need a staged "pending changes" buffer first.

### D23 — Writing help is a three-pass loop: ideate · substance · language
Two skills weren't enough — `brainstorm` (ideation) + `polish` (language) skipped the highest-value middle: whether the piece *works* and *serves the newsletter's intention*. Added **`editorial-review`** — a substance/intention pass grounded in the **Brief** (interface-moment sharpness, who-decided clarity, the "So, what?", objective-fit, structure, substance-overlap). **`polish` stays language/voice only** (reads the Voice Profile). Loop: `brainstorm` → [writer drafts] → `editorial-review` (Brief) → `polish` (Voice Profile). Mirrors structural-edit vs. line-edit; all assist, none rewrite (D21).
**Reverses if:** writers find two review passes redundant and want them merged.

### D22 — Ship pre-set, context-bound skills; don't ask the writer to author them
Authoring skills is too much load for a non-technical writer — it recreates the cold-start problem one level up. The kit ships **pre-set** skills that automatically consume the writer's generated context (Brief + Voice Profile), so they're newsletter-specific with **zero authoring**. v1 ships two: **`brainstorm`** (context-aware ideation partner — grounded in the Brief + archive, flags overlap with past issues) and **`polish`** (the Voice-Profile guardrail — the generalized, white-label `artifacts-polish`). Both assist/defend; neither generates reader-facing prose (D21). This reframes step 9 from "writer encodes skills" to "the kit provides them." Compound (11) improves the *context* the skills read — so the skills get better without the writer authoring anything.
**Reverses if:** writers want to author custom skills — then offer it as an advanced option, not the default.

### D21 — The kit defends/assists writing; it does not generate publish-ready prose
Calibration exposed it: a strong descriptive voice profile + "generate prose" yields high-quality **AI cosplay** — reads as AI, which Lorenzo explicitly rejects ("I don't want my users facing AI-generated text"). It also matches his own thesis ("writing remains mine"). So the Voice Profile's primary use is a **guardrail**: polish, flag AI texture, preserve idiosyncrasy, support ideation/structure — the prose stays the writer's. Any drafting is rough scaffolding the writer rewrites, never reader-facing prose. Added a **Naturalness / anti-AI-texture layer** (voice-profile §9) targeting *texture* not vocabulary: device-density limits, no manufactured similes, ground-in-specifics, ban the escalating-triplet crescendo (even when it "sounds like voice"), allow unevenness, restraint over performance.
**Reverses if:** generation quality improves enough that restrained drafting reliably passes the read-aloud test — but reader-facing prose stays the writer's regardless.

### D20 — The Brief is a rich identity document; CLAUDE.md is the quality bar
The Brief is written in **declarative identity-mode** (not hedged analyst-report mode) and is **as descriptive as it needs to be** (no one-screen limit) — explicit topics, *how each is treated*, named patterns, and the signature vocabulary. The texture from `subject-observed.md` must be carried INTO the Brief, not compressed out. **Benchmark:** match or beat a strong hand-written `CLAUDE.md`; the eval is a blind compare of generated vs. hand-built. Corrects the v1 Brief, which over-compressed its own source material into an index.
**Reverses if:** richness tips into bloat that no longer functions as a working reference.

### D19 — The Brief is the source of truth: about + how-written-so-far + objectives/vision
The Milestone 1 deliverable is defined (per Lorenzo's goal) as a living **source-of-truth** document with three parts: *what it's about*, *how it's been written so far*, and *objectives & vision*. It keeps the writer honest as they produce and is the doc to edit deliberately on a pivot. This pulls a **descriptive, high-level** slice of voice into M1 ("how it's been written"); the **operational** voice rules (falsifiable drafting spec) stay in M2's Voice Profile. M1 characterizes; M2 executes.
**Reverses if:** the how-written section duplicates M2 enough to merge the milestones.

### D18 — Separate concerns: onboard ≠ fetch; corpus read is the last, gated step
The `onboard` skill is scoped strictly to **step 0** ("these are my tools, how I work today" — organizing where work lives). It does **not** fetch or read the corpus. The corpus read (`extract-corpus`, step 3) is a deliberate, gated **final** step, run only after describe (1) and stated identity (2). Sequence: said → stated → shown/read → Milestone 1. (Corrects D17's over-bundling, which had onboard orchestrate the whole heavy flow.)
**Reverses if:** —

### D17 — Phase A built as an `onboard` skill orchestrating steps 0→3 _(superseded by D18 — onboard rescoped to step 0; no longer orchestrates the fetch)_
Setup-to-ingest is one runnable flow: the `onboard` skill collects sources (v1: Substack URL + pointers to other homes, deferring full Cowork connectors), runs the intake Q&A (`method/intake.md` → seed-context.md), pulls stated identity (`substack_identity.py` → identity-stated.md), and invokes `extract-corpus` (step 3). Output = the **three views** (said/stated/shown) the reconcile step needs. Step 0's grand multi-source orchestration is scoped down for v1 — only the URL is needed to reach the ingest milestone.
**Reverses if:** the steps prove better as separate user-invoked skills than one flow.

### D16 — Extraction baked into a white-labeled skill
The validated extractor is packaged as the `extract-corpus` skill — **white-labeled** (no publication-specific defaults). Appendix markers are passed per-newsletter via `--appendix-markers` and detected by the skill at runtime, not hardcoded; with none given, segmentation safely no-ops. The skill is the reusable step-3 component any Substack writer can use.
**Reverses if:** —

### D15 — v1 extraction scope: free Substack newsletters only
The extraction capability targets **Substack** for v1 (vanilla and custom-domain). Other platforms (Ghost, Beehiiv, Mailchimp, self-hosted) are out of scope until v1 proves out. Validated across 4 publications (Artifacts full 80, Astral Codex Ten incl. a paid post, Gary Marcus, + graceful failure on non-Substack Platformer). Non-Substack URLs exit cleanly. Paid posts → preview only (need owner export).
**Reverses if:** demand pulls toward a multi-platform promise — then generalize the acquirer.

### D14 — Segment each issue into zones; route them separately
Every issue splits into `meta` (title/subtitle/date), `body` (the essay → subject + voice), and `appendices` (Save for Later, Bookshelf, Nerding, ☕ → curation taste). Zones carry different signal and must not contaminate each other — e.g. Save-for-Later link blurbs are a different register and a slop vector if fed into voice distillation. Surfaced on the live Artifacts feed, which has recurring sections the summary corpus hid.
**Reverses if:** segmentation proves too newsletter-specific to generalize.

### D13 — Corpus acquisition: export-first, RSS for freshness, scrape as fallback
RSS (`/feed`) and a plain archive fetch do NOT yield the archive — RSS returns ~3 recent (full prose); the archive page is JS-truncated (~15 of ~30+). Primary path is the **platform export** (Substack ZIP: full coverage + fidelity, one user action); RSS for incremental/quick-start; archive-API scrape only as fallback. Generalizes to: prefer the platform's full export over RSS/scrape.
**Reverses if:** export UX is too high-friction and a reliable API path exists.

### D12 — Corpus fidelity matters; subject and voice have different requirements
Subject ("what it's about") can be distilled even from condensed/summary text; **voice** ("how it's written") requires **raw published prose**. The kit must detect summarized corpus and quarantine it from voice distillation. Surfaced while dogfooding: several local Artifacts files are summaries, fine for subject, useless for voice.
**Reverses if:** —

### D11 — Distillation claims must be evidence-backed
Every claim in the agent's read (subject and voice) cites example issues from the corpus. The read must be **falsifiable, not vibes** — so the user can challenge it, not just nod. Also the antidote to generic slop.
**Reverses if:** citations add friction without improving trust.

### D10 — Reconcile said vs. stated vs. shown → capture aspiration
Distillation explicitly compares three views — what the user **said** (intake), what the page **states** (about), what the corpus **shows** (observed) — surfaces the discrepancies, and asks the user about them. This dialogue is the engine, because: the corpus is *descriptive* (what the newsletter **was**); the discrepancy conversation is the only place **aspiration** (what it **wants to be**) enters the context. A pure-corpus distill can't capture direction.
**Reverses if:** discrepancies turn out to be rare/noise for most writers.

### D9 — Milestone structure: substance before style, value-early
The build splits into two confirmable milestones, not one big "distill" blob:
1. **Newsletter Brief** — "what it's about (and becoming)." Unlocks idea discussion.
2. **Voice Profile** — "how it's written." Unlocks drafting.
Each ends in a concise deliverable + a user-confirmation gate. Conceived as a product with visible milestones; value is delivered after M1, before the voice work is done.
**Reverses if:** users find the two-step confirmation heavier than one combined pass.

### D8 — Progressive context loading + multi-source orchestration
At install, the agent connects **all** of the writer's knowledge homes (Substack, Drive, Notion, notes) and orchestrates across them. Context is then built **light → heavy**: (1) user's own punchline/description, (2) the newsletter's *stated* identity (Substack about page, tagline, subscription tiers — premium context the author already wrote), (3) only then the bulk corpus. Rationale: high-signal-first avoids cluttering context from the get-go and front-loads the cheapest, truest signal.
**Reverses if:** the corpus turns out to dominate signal so much that the lighter layers are noise.

### D7 — Build-in-public channels: open GitHub repo + LinkedIn short-form
The trail lives in a **public GitHub repo** (docs/devlog as the public record) and **LinkedIn** (progress + open questions for reach and feedback). *Not* Artifacts posts (keep the newsletter for the ideas, not the build) and *not* private. Implication: docs are written to be read by outsiders from day 0; devlog entries double as LinkedIn raw material.
**Reverses if:** the meta-story turns out to be a strong enough Artifacts angle to fold in later.


### D1 — Scope to newsletter / writing-voice first
Defer academic research and university-course use cases. Newsletter is the most **dogfoolable** (Lorenzo runs Artifacts) and the most **externalizable** context type (voice from one's own corpus). Academic adds citation/hallucination stakes; course is more pedagogy/structure than voice.
**Reverses if:** distillation proves easy and the bottleneck turns out to be a different vertical.

### D2 — Build the method layer, not a framework/runtime
Ship as **skills + a project template** on an existing runtime (Claude Code / Cowork), not custom agent infrastructure. "Framework" is the wrong word and would tempt over-building.
**Reverses if:** the runtimes can't express the lifecycle we need.

### D3 — Surface = Cowork for non-technical writers
Terminal (Claude Code) is the wrong surface for writers. Cowork runs the same machinery (skills, MCP connectors, context files) with an accessible UI; connectors handle ingestion (Substack/RSS, Drive, Notion).
**Reverses if:** Cowork's connector/skill-distribution model can't reach real writers, or a better consumer surface appears.

### D4 — The core IP is distillation quality
Not ingestion, not file structure, not the surface. The make-or-break is producing *specific, true, non-generic* voice rules. Prototype and obsess over this first.
**Reverses if:** never — this is the thesis.

### D5 — Lifecycle = Bootstrap → Calibrate → Encode → Write → Compound → Prune
Added **Calibrate** (trust gate), **Write** (the actual value loop, design it first), and **Prune** (cleaning ≠ only learning) to the initial 3-moment sketch.
**Reverses if:** dogfooding shows a stage is redundant.

### D6 — Build in public, dogfood on Artifacts as the control
Folder now, own repo later. Validate by reproducing Lorenzo-quality voice on the Artifacts archive + at least one other newsletter before generalizing.
**Reverses if:** —
