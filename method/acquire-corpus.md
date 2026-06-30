# Method: Acquire & Prepare Corpus (step 3)

_The foundation everything stands on. If this is lossy, distillation is lossy — proven on the Artifacts dogfood, where a summarized/partial corpus hid recurring sections and skewed the read. Drafted 2026-06-28._

## Goal
Turn a writer's published archive into **clean, full-fidelity, segmented** text — full coverage and full prose, with each part routed to the right downstream use.

## Stage A — Acquire (the coverage problem)
RSS and a plain archive fetch do **not** give you the archive. Source priority:

1. **Platform export (PRIMARY).** Substack: Settings → Export → ZIP (HTML posts + CSV). Full coverage + full fidelity. Cost: one user action — ask for it first.
2. **RSS `/feed` (freshness).** Full prose but only the most recent few (3 for Artifacts). Use for incremental updates (the Compound step) and as a zero-setup quick start for new/small newsletters.
3. **Archive API + per-post fetch.** The archive *page* is JS-truncated (~15 posts); the archive API paginates **all** slugs (`/api/v1/archive?sort=new&offset=N&limit=12`), then `/api/v1/posts/{slug}` returns full `body_html`. **Proven on Artifacts: full archive at full fidelity from the URL alone, zero user action.**
   - ⚠️ **Paginate, don't trust one call.** A single `limit=50` returned 23; paginating with `limit=12` revealed **80**. Always loop until a short/empty batch.
   - ⚠️ **Rate limiting (429).** Fetching ~46 posts fast tripped Substack's limit. Use exponential backoff + throttle (see `tools/substack_fetch.py`).
   - Paid posts return preview only → still need the owner's export.

**Rule (revised, D13):** for free newsletters the **API scrape is the zero-friction default** (URL only); export is the upgrade for full archive incl. paid.

## Stage B — Normalize (fidelity)
- HTML → clean markdown: decode entities (`&#8217;`→'), convert tags, **preserve structure** (headers, blockquote, emphasis, links).
- Strip boilerplate: subscribe CTAs, share buttons, "grab a virtual coffee," footers, nav.
- Embeds: YouTube/Spotify → `[media]` markers; handle or drop image captions.

## Stage C — Segment (zones carry different signal)
Split each issue and route each zone — **do not let them contaminate each other**:

| Zone | Examples | Feeds |
|---|---|---|
| `meta` | title, subtitle, date, slug | format/title conventions |
| `body` | the essay | **subject + voice** |
| `appendices` | Save for Later, The Bookshelf, Nerding, ☕ | **curation taste** (save-for-later skill) — NOT voice prose |

The *Save for Later* link blurbs are a different register; letting them into voice distillation is a slop vector.

## Stage D — Fidelity tag
Mark each issue `full-prose | excerpt | summary`. Quarantine anything not full-prose from voice work (D12).

## Stage E — Scope & volume (incl. era/language)
- Dedup drafts/cross-posts; let the user exclude weak early issues.
- **Detect era/language splits.** Artifacts is bilingual: Italian (2023→mid-2024) → English (mid-2024→now). Voice **must not** be averaged across phases or languages. Default to the current-language, recent era for voice/identity; treat older/other-language eras as separate (history, not current voice).
- Large archive (Artifacts: 80 posts): select a representative **retained subset** for context + index the rest for retrieval (don't dump 80 full issues into one window).

## Output
`/corpus/` — normalized, segmented, fidelity-tagged issues + a **manifest** (coverage count, date range, fidelity breakdown, what was excluded and why). The manifest makes the corpus's limits visible to every downstream step.

## Open
- Recurring-section detection is newsletter-specific (Artifacts has Bookshelf/Nerding/☕). Generalize or learn per-writer?
- Retained-subset selection = the same drift/weighting problem as pruning (Q4).
