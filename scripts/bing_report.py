#!/usr/bin/env python
"""Pull Bing Webmaster Tools data for the site — complements gsc_report.py.

Runs via uv (deps declared inline):

    uv run patchnotes/scripts/bing_report.py            # markdown to stdout
    uv run patchnotes/scripts/bing_report.py -o out.md  # also save to file

Requires a Bing WMT API key (one-time, ~2 min):

  1. bing.com/webmasters -> sign in -> select the site property.
  2. Settings (gear) -> API Access -> API Key -> Generate -> copy.
  3. Save at  personnal/secrets/bing-api-key.txt  or set BING_API_KEY.

The WMT JSON API is older and quirkier than GSC: stats endpoints return
whatever range Bing holds (~3 months typically); "QueryStats" counts
impressions where the query is known — anonymous traffic isn't included.
"""

# /// script
# requires-python = ">=3.9"
# dependencies = ["requests"]
# ///

import argparse
import datetime
import os
import sys

import requests

SITE_URL = os.environ.get("BING_SITE_URL", "https://zagd3m.github.io/patchnotes/")
API = "https://ssl.bing.com/webmaster/api.svc/json"

KEY_URLS = [
    "",
    "full-notes/",
    "blog/",
    "builds/",
    "blog/s14-dev-stream-1/",
    "blog/top-10-changes/",
    "builds/guide-frost-kick/",
    "calculators/dragontalon/",
]

SETUP_HINT = """\
No usable Bing API key. Setup (~2 min):

  1. bing.com/webmasters -> select property -> Settings -> API Access
     -> API Key -> Generate.
  2. Save at personnal/secrets/bing-api-key.txt
     or set BING_API_KEY=<key> and re-run.
"""


def find_key() -> str | None:
    env = os.environ.get("BING_API_KEY")
    if env:
        return env.strip()
    here = os.path.dirname(os.path.abspath(__file__))
    candidate = os.path.join(here, "..", "..", "personnal", "secrets", "bing-api-key.txt")
    candidate = os.path.normpath(candidate)
    if os.path.isfile(candidate):
        with open(candidate, encoding="utf-8") as f:
            return f.read().strip()
    return None


def call(key: str, method: str, **params) -> dict | list | None:
    qs = {"apikey": key, "siteUrl": SITE_URL, **params}
    r = requests.get(f"{API}/{method}", params=qs, timeout=30)
    if r.status_code in (401, 403):
        sys.exit(f"Bing API refused access ({r.status_code}) — check the key.")
    r.raise_for_status()
    return r.json().get("d")


def traffic_table(rows: list | None) -> str:
    """WMT returns one row per query per day — aggregate across the window."""
    if not rows:
        return "_No traffic data yet — Bing reports ~3 months of history._\n"
    totals: dict[str, list[int]] = {}
    for row in rows:
        name = (row.get("Query") or "?").replace(SITE_URL, "/")
        t = totals.setdefault(name, [0, 0])
        t[0] += row.get("Impressions", 0)
        t[1] += row.get("Clicks", 0)
    ordered = sorted(totals.items(), key=lambda kv: -kv[1][0])[:25]
    lines = ["| query/page | impressions | clicks |", "|---|---:|---:|"]
    for name, (imp, clk) in ordered:
        lines.append(f"| {name} | {imp} | {clk} |")
    return "\n".join(lines) + "\n"


def _ms_date(v: str | None) -> str:
    """Bing serializes dates as '/Date(1774396800000)/'."""
    if not v:
        return "?"
    try:
        ms = int(v.strip("/Date()"))
        return datetime.date.fromtimestamp(ms / 1000).isoformat()
    except (ValueError, OSError):
        return v


def crawl_table(stats: list | None) -> str:
    """GetCrawlStats returns daily snapshots; show the latest."""
    if not stats:
        return "_No crawl stats._\n"
    latest = stats[-1]
    fields = [
        ("InIndex", "pages in index"),
        ("CrawledPages", "pages crawled that day"),
        ("CrawlErrors", "crawl errors"),
        ("Code4xx", "4xx seen"),
        ("Code5xx", "5xx seen"),
        ("BlockedByRobotsTxt", "blocked by robots.txt"),
    ]
    lines = [f"_as of {_ms_date(latest.get('Date'))}_\n", "| metric | value |", "|---|---:|"]
    for key, label in fields:
        lines.append(f"| {label} | {latest.get(key, '?')} |")
    return "\n".join(lines) + "\n"


def url_info(key: str) -> str:
    lines = ["| URL | last crawled | size |", "|---|---|---:|"]
    for path in KEY_URLS:
        target = SITE_URL + path
        try:
            info = call(key, "GetUrlInfo", url=target)
        except requests.HTTPError as e:
            lines.append(f"| {path or '/'} | _error {e.response.status_code}_ | |")
            continue
        if not info or not info.get("LastCrawledDate"):
            lines.append(f"| {path or '/'} | _unknown to Bing_ | |")
            continue
        lines.append(
            f"| {path or '/'} | {_ms_date(info.get('LastCrawledDate'))} "
            f"| {info.get('DocumentSize', '?')} B |"
        )
    return "\n".join(lines) + "\n"


def quota_line(key: str) -> str:
    try:
        q = call(key, "GetUrlSubmissionQuota")
    except requests.HTTPError:
        return "_quota check failed_\n"
    if not q:
        return "_quota check returned nothing_\n"
    return f"daily quota: {q.get('DailyQuota', '?')}, monthly: {q.get('MonthlyQuota', '?')}\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", help="also write the report to this file")
    args = ap.parse_args()

    key = find_key()
    if not key:
        sys.exit(SETUP_HINT)

    parts = [
        f"# Bing WMT report — {datetime.date.today().isoformat()}\n",
        f"Property: `{SITE_URL}`\n",
        "## Crawl/index snapshot\n",
        crawl_table(call(key, "GetCrawlStats")),
        "## Top queries\n",
        traffic_table(call(key, "GetQueryStats")),
        "## Top pages\n",
        traffic_table(call(key, "GetPageStats")),
        "## URL index status\n",
        url_info(key),
        "## IndexNow submission quota\n",
        quota_line(key),
    ]
    report = "\n".join(parts)
    print(report)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\n(saved -> {args.output})", file=sys.stderr)


if __name__ == "__main__":
    main()
