---
name: polish
description: >
  Polish-check a newsletter draft against the writer's Voice Profile — flag AI texture, preserve
  idiosyncrasy, fix only true typos, never sanitize. A PRE-SET guardrail (the generalized,
  white-label version of artifacts-polish) that reads the writer's own voice-profile.md. Use for
  "polish this", "check my draft", "does this sound like me", "polish check", "is this AI-sounding".
---

# Polish — the voice guardrail

A pre-set skill that runs the writer's own Voice Profile against a draft. It protects the writer's
voice (including its roughness); it does not impose a house style (D21, D22).

## Reads
`newsletter-context/voice-profile.md` (rules + the VOICE CHECKLIST §8 + the NATURALNESS layer §9) ·
`newsletter-context/newsletter-brief.md` (does the draft serve the brief).

## Procedure
1. **Run the checklist** — §8 voice items + §9 naturalness items — against the draft, item by item.
   Report pass/fail per item with the offending line quoted.
2. **Flag AI texture specifically:** manufactured similes · escalating-triplet crescendos ·
   device-density overload (too many signatures at once) · generic vagueness (no real specifics) ·
   forbidden tells ("delve", formulaic "this-not-that", unspaced "—" as default) · corporate register.
3. **Preserve idiosyncrasy — never "correct":** the writer's spaced "!", their own coinages,
   mild non-native textures, emoji/parenthetical asides. **Fix only unambiguous typos.**
4. **Suggest, don't rewrite.** Surface voice-preserving fluency notes as suggestions the writer
   accepts or rejects. Never rewrite the piece wholesale.
5. **Stay in lane:** `polish` is **language & voice only**. If the draft seems off-thesis, thin in
   argument, or drifting from the Brief, don't fix it here — flag it and point the writer to
   **`editorial-review`** (the substance & intention pass). Substance there, voice here.

## Output
A checklist report + flagged lines + accept/reject suggestions. **The writer decides.**

## Boundary (D21)
A guardrail, not an editor imposing a style. It catches what doesn't sound like the writer and
protects what does — roughness included. Never sanitizes into generic fluent English.
