# Method: Distill Voice (step 7) + Calibrate (step 8)

_Milestone 2. The operational drafting spec — the executable "how it's written." The
harder half of Q1. Drafted 2026-06-30._

## Goal
An **actionable Voice Profile**: rules a writing skill can *apply and check*, grounded in
the real prose, shaped by the writer's answers. Not description — a contract.

## Three hard requirements (Lorenzo)
1. **Actionable by any writing skill.** The profile is the rule source that polish / draft /
   ideate skills read. Format = named, *binary-checkable* rules + a runnable checklist, not prose.
2. **Grounded in reality.** Every rule backed by a **verbatim** corpus quote (D11). Raw
   full-prose only (D12) — never summaries.
3. **Shaped by the writer's answers.** Era/language scoping (Lorenzo disowns the Italian
   era → distill English, recency-weighted, Q4), the "never" list from intake, and the
   step-8 calibration reactions.

## Inputs
Raw current-era corpus · the [Brief](brief.md) (identity — keeps voice in service of it) ·
seed-context (never-list, disowned eras) · reconcile answers.

## Process (step 7)
1. **Scope** the corpus to the current voice era; exclude disowned/other-language; weight recent.
2. **Close-read at every level**: structure (open/pivot/close) · paragraph & rhythm ·
   sentence patterns · diction/lexicon · rhetorical devices · titles/subtitles.
3. For each pattern: **directive + verbatim example** (+ a DON'T where there's an anti-pattern).
4. **Build the anti-slop / "never" list**: generic AI tells to forbid (Artifacts itself names
   them in `writing-is-thinking`) **+** the writer's own disavowals.
5. **Assemble skill-consumable format**: rules with IDs + examples, then a one-page **VOICE
   CHECKLIST** (8–12 binary items) a skill runs a draft through.

## The actionability contract
The Voice Profile is what downstream skills read. So:
- Rules are **binary-checkable** ("Opens on a concrete moment, not an abstraction" — yes/no).
- The **checklist** is the interface: a polish skill applies it line by line.
- **Preserve idiosyncrasy.** Encode "keep the writer's awkward-but-his phrasing; never sanitize
  into generic fluency" (Lorenzo's standing rule). The profile protects voice, not just imposes it.

## Calibrate (step 8) — the trust gate
1. Generate a **sample in-voice** (an opening + 3 candidate titles, or a short passage).
2. Writer reacts: **dead-on / too generic / "I'd never say X."**
3. Revise the profile from the reactions. Loop until trusted.
4. Optional **blind test** (the Q1 proof): can the writer distinguish profile-generated prose
   from their own? Pass → voice is externalized.
- **Gate:** confirmed Voice Profile before any drafting skill is built on it.

## Naturalness & use-mode (D21) — the lesson from calibration
A descriptive profile + "generate prose" produces **AI cosplay**: it ticks every signature
and that density *is* the AI tell. So:
- The profile carries a **Naturalness layer** (§9) that overrides the rest — targeting *texture*:
  device-density limits, no manufactured similes, ground-in-specifics, ban the escalating-triplet
  crescendo, allow unevenness, restraint over performance. Run the **read-aloud test**.
- **Use-mode is defensive first.** The profile is a **guardrail** — polish, flag AI texture,
  preserve idiosyncrasy, support ideation/structure. The writing stays the writer's. Any
  drafting is rough scaffolding the writer rewrites, never reader-facing prose.

## Boundary
Brief = identity (what / how-character / vision). Voice Profile = executable how. Together
they compose the **CLAUDE.md-equivalent** (the project's quality bar, D20).

## Output
`voice-profile.md` — rules + examples + checklist. The substrate for step 9 (encode skills).
