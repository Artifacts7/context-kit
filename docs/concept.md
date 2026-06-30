# Concept: why this exists + jobs to be done

_Living doc. Last updated: 2026-06-28._

## The problem

Adoption of agentic AI by non-technical knowledge workers fails at the **cold start**, not the tooling.

The failure chain:
1. New user runs the agent **raw** (no context).
2. Gets generic / wrong output.
3. Concludes **the tool is overhyped** — not "I under-fed it."
4. Churns.

This is an **attribution problem**, not a motivation problem. People don't "fail to bother" — they never learn that context is the lever, because the bad result reads as the AI's fault.

## Why code was the easy case

A codebase is self-describing, structured, and in one place — the artifact *is* the spec. `/init` works because the context is sitting there in machine-readable form.

Knowledge work inverts all of that. The "repo" is scattered (PDFs, Docs, archives, inboxes), unstructured, and the most valuable part — **voice, taste, judgment** — is written down nowhere.

## The insight

The writer's **body of past work already exists** and is *richer* than a codebase: it encodes voice, not just structure. So the move is not "author a context file from a blank page" — it's:

> **ingest the corpus → distill the implicit patterns → keep a representative corpus retrievable.**

The verb is **distill**, not write.

## The pattern, proven by hand

Artifacts already runs this manually:
- `CLAUDE.md` = **distilled rules** (specific, falsifiable: "metaphors carry the argument," named title examples, the opening→close circle-back).
- 12 recent issues kept as full text = **retained corpus**.
- `artifacts-polish`, `artifacts-save-for-later` = **encoded judgment**.

Two layers + encoded judgment. The product is extracting this structure *automatically* from any writer's archive.

## Where the value (and risk) concentrates

The entire bet rests on **distillation quality**. Anyone can dump 50 issues into a prompt and get "your tone is thoughtful and engaging" — worthless, describes every newsletter. The value is producing *specific, true, non-generic* voice rules. That is the core IP. Everything else (ingestion, file structure, surface) is plumbing.

## Jobs to be done

**Primary (the writer):**
- When I start using AI for my newsletter, I want it to already know my voice and standards, **so I don't get generic slop and give up.**
- When I sit down to write a new issue, I want to draw on my whole archive and my own voice, **so I can write faster without sounding generic.**
- When I've written for years, I want that accumulated work to become a usable asset, **so it compounds instead of sitting dead in an archive.**

**Secondary:**
- When I'm choosing what to write, I want to know what I've already covered, **so I don't repeat myself.**
- When I have a draft, I want it polished to *my* standards, **so it ships faster without losing my voice.**
- When my voice has evolved, I want the context to reflect who I am *now*, **so it doesn't encode old/weaker work.**

**Adjacent (thin-corpus writers — bigger, later bet):**
- When my newsletter is young and undistinctive, I want help **discovering and sharpening** my voice — not just cloning it — **so the tool makes me better instead of reproducing my slop.**

## Scope decisions (see decisions.md)

- Start with **newsletter / writing-voice** (most dogfoolable, most externalizable). Defer academic research and course delivery — different context types, different failure modes.
- Surface: **Cowork** (non-technical), shipped as skills + template. Not building runtime/infra.
