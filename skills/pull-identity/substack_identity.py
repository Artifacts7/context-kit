#!/usr/bin/env python3
"""
Substack stated-identity puller (Context Kit, step 2 — pull stated identity).

The high-signal context the writer already wrote about themselves: publication name,
tagline, the about page, and recent subjects. Cheap, true, and loaded BEFORE the bulk
corpus (progressive loading, D8). White-label: works for any Substack from the URL.

Usage:
    python3 substack_identity.py <publication-url> <output-dir>
Output:
    <output-dir>/identity-stated.md
"""
import sys, re, html, json, os, urllib.request, urllib.error
import xml.etree.ElementTree as ET

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")

def html_to_text(h):
    h = re.sub(r"(?is)<(script|style).*?</\1>", " ", h)
    h = re.sub(r"(?i)<(/?)(h[1-6]|p|br|div|li|blockquote)[^>]*>", "\n", h)
    h = re.sub(r"<[^>]+>", "", h)
    h = html.unescape(h)
    h = re.sub(r"[ \t]+", " ", h)
    h = re.sub(r"\n\s*\n\s*\n+", "\n\n", h)
    return h.strip()

def main():
    if len(sys.argv) < 3:
        sys.exit("usage: substack_identity.py <publication-url> <output-dir>")
    base = sys.argv[1].rstrip("/"); outdir = sys.argv[2]
    os.makedirs(outdir, exist_ok=True)

    name = tagline = link = ""
    try:  # RSS channel = publication name + tagline
        ch = ET.fromstring(get(base + "/feed")).find("channel")
        name = (ch.findtext("title") or "").strip()
        tagline = (ch.findtext("description") or "").strip()
        link = (ch.findtext("link") or base).strip()
    except (urllib.error.HTTPError, urllib.error.URLError, ET.ParseError) as e:
        sys.exit(f"Could not read {base}/feed ({e}). Is this a Substack publication?")

    about = ""
    try:  # /about page = the writer's longer self-description
        about = html_to_text(get(base + "/about"))
        words = about.split()
        if len(words) > 500:  # trim page chrome/footers
            about = " ".join(words[:500]) + " …[trimmed]"
    except (urllib.error.HTTPError, urllib.error.URLError):
        pass

    subjects = []
    try:  # a few recent titles, for orientation only (not the corpus)
        arr = json.loads(get(base + "/api/v1/archive?sort=new&limit=6"))
        subjects = [f"{(p.get('post_date') or '')[:10]} — {p.get('title')}" for p in arr[:6]]
    except Exception:
        pass

    out = ["# Stated identity (as the newsletter describes itself)\n",
           f"**Name:** {name}\n", f"**Tagline:** {tagline}\n", f"**URL:** {link}\n"]
    if subjects:
        out.append("**Recent subjects:**\n" + "\n".join(f"- {s}" for s in subjects) + "\n")
    out.append("## About page\n\n" + (about or "_none found_") + "\n")
    open(f"{outdir}/identity-stated.md", "w").write("\n".join(out))
    print(f"Wrote {outdir}/identity-stated.md | name={name!r} tagline_words={len(tagline.split())} about_words={len(about.split())} subjects={len(subjects)}")

if __name__ == "__main__":
    main()
