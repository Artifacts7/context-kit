#!/usr/bin/env python3
"""
Substack corpus fetcher (Context Kit, step 3 — acquire-corpus).

Zero-friction acquisition for a free Substack: given a publication URL, enumerate
the FULL archive via the archive API, fetch each free post's full body, normalize
HTML -> text, and segment body vs. appendices (Save for Later / Bookshelf / etc).

Usage:
    python3 substack_fetch.py https://artifactstech.substack.com OUTDIR [--limit N]

Outputs:
    OUTDIR/<slug>.md         one cleaned, segmented issue per file
    OUTDIR/manifest.json     coverage, dates, fidelity, what was excluded

Limits (honest): free posts only (paid -> preview); recurring-section markers are
newsletter-specific (tune APPENDIX_MARKERS per publication).
"""
import sys, json, re, html, urllib.request, argparse, time

# White-label: NO publication-specific defaults. Appendix markers (recurring
# trailing sections like "save for later", "further reading") are passed in per
# newsletter via --appendix-markers; with none given, segmentation no-ops and the
# whole essay stays in BODY. The skill detects a publication's markers and supplies them.
DEFAULT_APPENDIX_MARKERS = []

# Substack UI boilerplate that leaks into body_html as button/widget text.
BOILERPLATE_RE = re.compile(
    r"^\s*(subscribe now|subscribe|share this post|share|leave a comment|comment|"
    r"give a gift subscription|pledge your support|thanks for reading[!.]?|"
    r"let'?s grab a virtual coffee.*|get \d+% off.*|upgrade to paid.*)\s*$",
    re.I)

def strip_boilerplate(text):
    return "\n".join(ln for ln in text.split("\n") if not BOILERPLATE_RE.match(ln.strip()))

def get(url, retries=5):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    delay = 2.0
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                time.sleep(delay); delay *= 2  # exponential backoff on rate limit
                continue
            raise

def enumerate_archive(base):
    posts, offset = [], 0
    while True:
        batch = json.loads(get(f"{base}/api/v1/archive?sort=new&search=&offset={offset}&limit=12"))
        if not batch:
            break
        posts.extend(batch)
        offset += len(batch)
        if len(batch) < 12:
            break
        time.sleep(0.3)
    return posts

def html_to_text(h):
    h = re.sub(r"(?is)<(script|style).*?</\1>", " ", h)
    h = re.sub(r"(?i)<(/?)(h[1-6]|p|br|div|li|blockquote)[^>]*>", "\n", h)
    h = re.sub(r"<[^>]+>", "", h)
    h = html.unescape(h)
    h = re.sub(r"[ \t]+", " ", h)
    h = re.sub(r"\n\s*\n\s*\n+", "\n\n", h)
    return strip_boilerplate(h.strip())

def segment(text, markers):
    """Split essay body from recurring appendices at the first appendix marker.
    With no markers, the whole text stays in body (graceful no-op)."""
    if not markers:
        return text, ""
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        low = ln.strip().lower()
        if low and any(low.startswith(m) or low == m for m in markers):
            return "\n".join(lines[:i]).strip(), "\n".join(lines[i:]).strip()
    return text, ""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("base"); ap.add_argument("outdir")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--appendix-markers", default="",
                    help="comma-separated trailing-section headers to split off the body")
    a = ap.parse_args()
    base = a.base.rstrip("/")
    markers = [m.strip().lower() for m in a.appendix_markers.split(",") if m.strip()] or DEFAULT_APPENDIX_MARKERS
    import os; os.makedirs(a.outdir, exist_ok=True)

    try:
        meta = enumerate_archive(base)
    except (urllib.error.HTTPError, urllib.error.URLError, json.JSONDecodeError) as e:
        sys.exit(f"Not a reachable Substack publication ({base}): {e}. "
                 f"v1 supports free Substack newsletters only.")
    if not meta:
        sys.exit(f"No posts found at {base}. Is this a Substack publication?")
    archive_total = len(meta)
    if a.limit:
        meta = meta[:a.limit]
    manifest = {"publication": base, "total_in_archive": archive_total,
                "sampled": len(meta), "issues": []}
    for p in meta:
        slug, audience = p["slug"], p.get("audience")
        rec = {"slug": slug, "title": p.get("title"), "subtitle": p.get("subtitle"),
               "date": (p.get("post_date") or "")[:10], "audience": audience}
        if audience != "everyone":
            rec["fidelity"] = "preview-only (paid)"; manifest["issues"].append(rec); continue
        try:
            full = json.loads(get(f"{base}/api/v1/posts/{slug}"))
            body_html = full.get("body_html") or ""
            text = html_to_text(body_html)
            body, appendix = segment(text, markers)
            rec["fidelity"] = "full-prose" if len(body.split()) > 250 else "short/excerpt"
            rec["body_words"] = len(body.split())
            with open(f"{a.outdir}/{slug}.md", "w") as f:
                f.write(f"# {p.get('title')}\n**Subtitle:** {p.get('subtitle')}\n"
                        f"**Date:** {rec['date']}\n**URL:** {p.get('canonical_url')}\n\n"
                        f"---\n\n## BODY\n\n{body}\n\n## APPENDICES\n\n{appendix}\n")
        except Exception as e:
            rec["fidelity"] = f"error: {e}"
        manifest["issues"].append(rec)
        time.sleep(0.3)
    with open(f"{a.outdir}/manifest.json", "w") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    full_n = sum(1 for i in manifest["issues"] if i.get("fidelity") == "full-prose")
    print(f"Fetched {len(meta)} posts -> {full_n} full-prose. Manifest: {a.outdir}/manifest.json")

if __name__ == "__main__":
    main()
