# Open questions & assumptions

_What we're unsure of and what would settle it. Build-in-public gold — share these._

## Make-or-break

### Q1 — Is voice/taste actually externalizable?
Can a distilled profile + retained corpus make Claude sound like *the specific writer*, not "competent newsletter writer about tech"? **The whole product rests on this.**
- **Test:** dogfood on Artifacts. Does output sound like Lorenzo or like generic slop?
- **Settles it:** a blind read where Lorenzo can't tell distilled-context output from his own draft → real. Persistent slop → dead end.
- **Status (2026-06-30): RESOLVED, with a nuance.** Subject + voice-character read true-to-Artifacts (M1). For operational voice (M2): a generated sample "sounded like Lorenzo but read AI-generated" — generation produces **AI cosplay**. So voice is externalizable **as a guardrail** (catch AI texture, preserve idiosyncrasy, polish the writer's own prose) but **not as a generator** of reader-facing prose (D21). That's the answer the product is now built around — more defensible than "the AI can write as you."

## Scaling

### Q2 — The thin-corpus trap
The method works *because* Artifacts has a distinctive, developed voice. Point it at 5 generic posts and it extracts generic context → reproduces slop, making things worse.
- **Open:** do we gate on "enough distinctive corpus," or pivot the tool toward **discovering/sharpening** voice for thin corpora (bigger, better product)?

### Q3 — Commoditization risk
Building on Cowork means betting on Anthropic's roadmap. If they ship a native "learn my writing voice" feature, the plumbing evaporates.
- **Open:** is the defensible moat **newsletter-specific judgment** (curation taste, drift-cleaning, slop-detection, latent-thesis discovery) rather than the bootstrapping itself?

## Mechanics

### Q4 — Drift, era, and language weighting
Three readings, escalating: (a) tidy a messy corpus (mechanical); (b) **voice drift over time** — weight recent/best so distillation doesn't average toward early work; (c) **era/language splits** — proven real on Artifacts (Italian 2023→mid-2024, then English; 80 posts over ~3 years). You cannot average voice across languages or writer-phases.
- **Open:** how to weight recency vs. "best" vs. "most representative"; how to detect era boundaries automatically; whether older eras are discarded, archived, or offered as an optional "earlier voice."

### Q5 — Form factor for real (non-technical) writers
Skills + template validates the method on technical early adopters / Lorenzo. Reaching actual writers needs a guided, zero-terminal flow. Different product, later bet.
- **Open:** is Cowork's skill-distribution good enough, or does this need its own surface eventually?

### Q7 — Anchoring bias in the reconcile dialogue
If the agent presents its own read *first*, the user may just agree rather than think — biasing the very aspiration/direction signal we're trying to capture. The reconcile questions must be genuinely open, not leading.
- **Open:** how to surface the agent's read without anchoring the answer. (Ask before revealing? Present competing reads? Force a disagreement?)

### Q6 — Unit of adoption
Individual writer (clear, our focus) vs. team/publication (multiple contributors, shared voice). Defer, but note it.
