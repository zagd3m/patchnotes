#!/usr/bin/env python
"""Pull Google Search Console data for the site — the only real ranking signal.

Runs via uv (deps declared inline):

    uv run patchnotes/scripts/gsc_report.py            # markdown to stdout
    uv run patchnotes/scripts/gsc_report.py -o out.md  # also save to file

Requires a service-account key (one-time setup, ~15 min):

  1. console.cloud.google.com -> create project -> enable "Google Search
     Console API" (and "Search Console URL Inspection API" if listed
     separately — it is bundled in most projects).
  2. Credentials -> Service account -> create -> Keys -> JSON -> download.
  3. Search Console -> property -> Settings -> Users & permissions -> add the
     service-account email (Restricted access is enough).
  4. Save the key as  personnal/secrets/gsc-sa.json  (workspace-level,
     not committed anywhere) or point GSC_SA_KEY at it.

Data lags ~24-72h. On a niche site, read weekly trends, not daily deltas.
"""

# /// script
# requires-python = ">=3.9"
# dependencies = ["requests", "google-auth"]
# ///

import argparse
import datetime
import os
import sys

import requests
from google.oauth2 import service_account

SITE_URL = os.environ.get("GSC_SITE_URL", "https://zagd3m.github.io/patchnotes/")
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
# searchAnalytics still lives on the webmasters/v3 host — searchconsole.googleapis.com/v1
# is a different surface (URL Inspection) and 404s analytics calls.
API_ANALYTICS = "https://www.googleapis.com/webmasters/v3"
API_INSPECT = "https://searchconsole.googleapis.com/v1"

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
No usable service-account key. One-time setup (~15 min, needs a Google
account that owns the Search Console property):

  1. console.cloud.google.com -> new project -> APIs & Services -> enable
     "Google Search Console API".
  2. Credentials -> Create credentials -> Service account -> create -> open it
     -> Keys -> Add key -> JSON -> download.
  3. Search Console -> this property -> Settings -> Users & permissions ->
     Add user -> paste the service-account's email (Restricted is fine).
  4. Save the key at personnal/secrets/gsc-sa.json
     or set GSC_SA_KEY=/path/to/key.json and re-run.
"""


def find_key() -> str | None:
    env = os.environ.get("GSC_SA_KEY")
    if env and os.path.isfile(env):
        return env
    here = os.path.dirname(os.path.abspath(__file__))
    candidate = os.path.join(here, "..", "..", "personnal", "secrets", "gsc-sa.json")
    candidate = os.path.normpath(candidate)
    return candidate if os.path.isfile(candidate) else None


def token() -> str:
    path = find_key()
    if not path:
        sys.exit(SETUP_HINT)
    creds = service_account.Credentials.from_service_account_file(path, scopes=SCOPES)
    from google.auth.transport.requests import Request

    creds.refresh(Request())
    return creds.token


def analytics(hdrs: dict, dimension: str, days: int = 28, rows: int = 25) -> list[dict]:
    end = datetime.date.today() - datetime.timedelta(days=3)  # data lags ~2-3 days
    start = end - datetime.timedelta(days=days)
    body = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "dimensions": [dimension],
        "rowLimit": rows,
    }
    url = f"{API_ANALYTICS}/sites/{requests.utils.quote(SITE_URL, safe='')}/searchAnalytics/query"
    r = requests.post(url, headers=hdrs, json=body, timeout=30)
    if r.status_code in (401, 403):
        sys.exit(
            f"GSC API refused access ({r.status_code}). The service-account email is\n"
            "probably not added to the property — step 3 of the setup hint.\n"
            f"Response: {r.text[:300]}"
        )
    r.raise_for_status()
    data = r.json()
    print(f"_(window: {start} -> {end})_\n")
    return data.get("rows", [])


def sitemaps(hdrs: dict) -> str:
    url = f"{API_ANALYTICS}/sites/{requests.utils.quote(SITE_URL, safe='')}/sitemaps"
    r = requests.get(url, headers=hdrs, timeout=30)
    if not r.ok:
        return f"_sitemap status unavailable (HTTP {r.status_code})_\n"
    lines = ["| sitemap | submitted | pending | warnings | errors |", "|---|---|---:|---:|---:|"]
    for s in r.json().get("sitemap", []):
        lines.append(
            f"| {s['path'].replace(SITE_URL, '/')} | {s.get('lastSubmitted', '?')[:10]} "
            f"| {s.get('isPending')} | {s.get('warnings')} | {s.get('errors')} |"
        )
    return "\n".join(lines) + "\n"


def trend(rows: list[dict]) -> str:
    if not rows:
        return "_No daily data yet._\n"
    lines = ["| date | clicks | impressions |", "|---|---:|---:|"]
    for r in rows[-14:]:  # last two weeks only — earlier days are usually flat-zero
        lines.append(f"| {r['keys'][0]} | {r['clicks']} | {r['impressions']} |")
    return "\n".join(lines) + "\n"


def table(rows: list[dict], keyname: str) -> str:
    if not rows:
        return "_No data — property too new, or traffic below reporting threshold._\n"
    lines = [
        f"| {keyname} | clicks | impressions | CTR | pos |",
        "|---|---:|---:|---:|---:|",
    ]
    for r in rows:
        keys = "/".join(r["keys"])
        short = keys.replace(SITE_URL, "/").replace("https://zagd3m.github.io", "")
        lines.append(
            f"| {short} | {r['clicks']} | {r['impressions']} | {r['ctr']:.1%} | {r['position']:.1f} |"
        )
    return "\n".join(lines) + "\n"


def inspect_urls(hdrs: dict) -> str:
    lines = ["| URL | verdict | coverage |", "|---|---|---|"]
    for path in KEY_URLS:
        target = SITE_URL + path
        r = requests.post(
            f"{API_INSPECT}/urlInspection/index:inspect",
            headers=hdrs,
            json={"inspectionUrl": target, "siteUrl": SITE_URL},
            timeout=30,
        )
        if r.status_code == 429:
            lines.append("| … | _quota hit — inspect remaining URLs tomorrow_ | |")
            break
        if not r.ok:
            lines.append(f"| {path or '/'} | _API error {r.status_code}_ | |")
            continue
        res = r.json().get("inspectionResult", {}).get("indexStatusResult", {})
        verdict = res.get("verdict", "?")
        state = res.get("coverageState", "?")
        lines.append(f"| {path or '/'} | {verdict} | {state} |")
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", help="also write the report to this file")
    args = ap.parse_args()

    hdrs = {"Authorization": f"Bearer {token()}"}
    parts = [
        f"# GSC report — {datetime.date.today().isoformat()}\n",
        f"Property: `{SITE_URL}`\n",
        "## Top queries (last 28d)\n",
        table(analytics(hdrs, "query"), "query"),
        "## Top pages (last 28d)\n",
        table(analytics(hdrs, "page"), "page"),
        "## Daily trend (last 14d of window)\n",
        trend(analytics(hdrs, "date")),
        "## Sitemap status\n",
        sitemaps(hdrs),
        "## URL inspection\n",
        inspect_urls(hdrs),
    ]
    report = "\n".join(parts)
    print(report)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\n(saved -> {args.output})", file=sys.stderr)


if __name__ == "__main__":
    main()
