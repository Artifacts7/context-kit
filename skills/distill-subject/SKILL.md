---
name: distill-subject
description: >
  Distill what a newsletter is ABOUT from its corpus — an evidence-cited read of through-line,
  topic clusters, lenses (ways of seeing), motifs, audience, boundaries, and formats. Step 4 of
  the Context Kit (Milestone 1). Run after the corpus is ingested. Use for "distill the subject",
  "what is this newsletter about", "analyze my archive", "read the corpus".
---

# Distill Subject (step 4)

Produce the agent's own **evidence-backed** read of what the newsletter is about. Sharp and
falsifiable, not generic.

## Precondition
Corpus ingested (`extract-corpus`). Do NOT read the writer's intake/about first (anchoring, Q7).

## Procedure
1. **Scope** the corpus to the current voice era — exclude disowned/other-language issues; recency-weight (Q4). Use the manifest's dates/language.
2. **Read the BODY** of the scoped issues. For a large corpus, dispatch the close-read to a subagent (read `## BODY` only; recency-weight; return structured markdown) rather than loading it all yourself.
3. **Extract along the axes**, filling each with specifics not adjectives: through-line · topic clusters (ranked, ≥2 issue citations each) · lenses (recurring *ways of seeing*, distinct from topics — the highest-value) · motifs/fingerprints (self-coined terms, recurring questions) · audience · boundaries (explicit disavowals) · formats.
4. **Cite or cut** (D11): every claim names the issues that prove it. **Separate topic from lens.** Flag corpus fidelity (D12).
5. **Anti-slop tests** before shipping: substitution (cut anything true of any newsletter) · citation (all claims traceable) · surprise (≥1 latent observation) · disagreement-surface (≥1 gap vs. the stated identity, for step 5).

## Output
`newsletter-context/subject-observed.md` — the structured read + a reconcile preview. → hand to **`reconcile`** (step 5).
