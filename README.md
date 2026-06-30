# Context Kit

**Turn your newsletter's archive into living AI writing-context — then write with a partner that keeps your voice yours.**

Most people bounce off AI writing tools because of the cold start: they run the AI raw, get generic slop, and blame the tool. Context Kit fixes that. It reads your whole published archive to learn **what your newsletter is about** (a Brief) and **how you write** (a Voice Profile), then gives you pre-set skills that brainstorm, review, and polish — as a **guardrail, never a ghostwriter**. The writing stays yours.

> v1 supports **free Substack** newsletters (vanilla or custom-domain).

## Install (Claude Code)

```
/plugin marketplace add <your-github-repo>
/plugin install context-kit@context-kit
```

Skills then load namespaced, e.g. `/context-kit:onboard`, `/context-kit:brainstorm`.

## Quick start

Run these in your project; everything the kit generates lands in **`./newsletter-context/`**.

| Phase | Skill | What happens |
|---|---|---|
| Setup | `/context-kit:onboard` | tell it your tools + your Substack URL |
| | `/context-kit:pull-identity` | pulls your about-page / stated identity |
| | `/context-kit:extract-corpus` | pulls your full archive (clean, full-text) |
| **Understand** | `/context-kit:distill-subject` → `reconcile` → `brief` | → your **Brief** (source of truth) |
| **Voice** | `/context-kit:distill-voice` | → your **Voice Profile** (+ checklist) |
| **Write** | `brainstorm` → *you draft* → `editorial-review` → `polish` | ideate · substance · language |
| Maintain | `/context-kit:compound` (session end) · `prune` | context improves & stays lean |

A describe step (your own words) happens during onboarding. Order is deliberate: **what you say → what your page states → what your archive shows**, light to heavy.

## What it is — and isn't

- **Is:** a partner that *grounds, sharpens, and guards* your writing — a Brief that keeps you honest, a Voice Profile that flags AI texture and protects your idiosyncrasies.
- **Isn't:** a generator. No skill writes reader-facing prose for you. The thinking and the words stay yours.

## Your context lives in `./newsletter-context/`
`brief.md` · `voice-profile.md` · `seed-context.md` · `identity-stated.md` · `corpus/`. These are *yours*, generated from *your* newsletter — they're what makes the generic skills specific to you.

## For the curious (build-in-public)
This kit was built in the open, dogfooded on the [Artifacts](https://artifactstech.substack.com) newsletter. The reasoning trail lives in [`docs/`](docs/) — [decisions](docs/decisions.md) (D1–D25, each with a "reverses if"), [the journey](docs/user-journey.md), [open questions](docs/open-questions.md), [devlog](docs/devlog.md) — and the method specs behind each skill in [`method/`](method/). *(The author's own Artifacts context isn't shipped — your `newsletter-context/` is generated fresh from your archive.)*
