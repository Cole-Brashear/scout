#!/usr/bin/env python3
"""List open roles from company job boards on Greenhouse, Ashby or Lever, newest first.

  jobs.py greenhouse:stripe ashby:ramp lever:palantir [-k KEYWORD]... [-l LOCATION]... [-x EXCLUDE]... [--days N] [--json]
  jobs.py detect URL

-k keeps titles containing any keyword, -l keeps locations containing any location ("remote" also
matches roles flagged remote), -x drops titles containing any term. All matching ignores case.
The board name is the slug in the company's job links. A 404 means the wrong board or the wrong ATS.
Standard library only.
"""
import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

HEADERS = {"User-Agent": "scout-job-search/1.0", "Accept": "application/json"}

ATS_PATTERNS = [
    ("greenhouse", r"greenhouse\.io/(?:embed/job_board\?for=)?([A-Za-z0-9_-]+)"),
    ("ashby", r"jobs\.ashbyhq\.com/([A-Za-z0-9_.-]+)"),
    ("lever", r"jobs\.lever\.co/([A-Za-z0-9_-]+)"),
]
NOT_BOARDS = {"embed", "v1", "boards", "jobs", "api"}


def fetch(url, as_json=True):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        body = r.read()
    return json.loads(body) if as_json else body.decode("utf-8", "replace")


def iso(value):
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value / 1000, tz=timezone.utc)
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def greenhouse(board):
    data = fetch(f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs")
    for j in data.get("jobs", []):
        yield {
            "title": j.get("title", ""),
            "location": (j.get("location") or {}).get("name", ""),
            "posted": iso(j.get("first_published") or j.get("updated_at")),
            "url": j.get("absolute_url", ""),
            "pay": "",
            "remote": None,
        }


def ashby(board):
    data = fetch(f"https://api.ashbyhq.com/posting-api/job-board/{board}?includeCompensation=true")
    for j in data.get("jobs", []):
        if j.get("isListed") is False:
            continue
        locations = [j.get("location") or ""]
        locations += [s.get("location", "") for s in j.get("secondaryLocations") or [] if isinstance(s, dict)]
        comp = j.get("compensation") or {}
        yield {
            "title": j.get("title", ""),
            "location": "; ".join(l for l in locations if l),
            "posted": iso(j.get("publishedAt")),
            "url": j.get("jobUrl", ""),
            "pay": comp.get("compensationTierSummary") or comp.get("scrapeableCompensationSalarySummary") or "",
            "remote": j.get("isRemote"),
            "type": j.get("employmentType", ""),
        }


def lever(board):
    data = fetch(f"https://api.lever.co/v0/postings/{board}?mode=json")
    for j in data:
        cats = j.get("categories") or {}
        locations = cats.get("allLocations") or [cats.get("location") or ""]
        pay = ""
        sr = j.get("salaryRange") or {}
        if sr.get("min") and sr.get("max"):
            pay = f"{sr.get('currency', '')} {sr['min']:,}-{sr['max']:,} {sr.get('interval', '')}".strip()
        yield {
            "title": j.get("text", ""),
            "location": "; ".join(l for l in locations if l),
            "posted": iso(j.get("createdAt")),
            "url": j.get("hostedUrl", ""),
            "pay": pay,
            "remote": (j.get("workplaceType") == "remote") if j.get("workplaceType") else None,
            "type": cats.get("commitment", ""),
        }


SOURCES = {"greenhouse": greenhouse, "ashby": ashby, "lever": lever}


def matches(job, keywords, locations, excludes, since):
    title = job["title"].lower()
    if keywords and not any(k in title for k in keywords):
        return False
    if excludes and any(x in title for x in excludes):
        return False
    if locations:
        loc = job["location"].lower()
        remote_ok = "remote" in locations and job.get("remote")
        if not remote_ok and not any(l in loc for l in locations):
            return False
    if since and job["posted"] and job["posted"] < since:
        return False
    return True


def detect(url):
    for ats, pat in ATS_PATTERNS:
        m = re.search(pat, url)
        if m and m.group(1).lower() not in NOT_BOARDS:
            return f"{ats}:{m.group(1)}"
    try:
        html = fetch(url, as_json=False)
    except (urllib.error.URLError, ValueError) as e:
        return f"could not open the page ({e}); look for an Apply link on greenhouse.io, ashbyhq.com or lever.co"
    found = []
    for ats, pat in ATS_PATTERNS:
        for board in re.findall(pat, html):
            tag = f"{ats}:{board}"
            if board.lower() not in NOT_BOARDS and tag not in found:
                found.append(tag)
    if found:
        return " ".join(found)
    return "no Greenhouse, Ashby or Lever board found; this site may use Workday or its own system, so read the page directly"


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "detect":
        if len(sys.argv) != 3:
            sys.exit("usage: jobs.py detect URL")
        print(detect(sys.argv[2]))
        return

    ap = argparse.ArgumentParser(description="List open roles from Greenhouse, Ashby or Lever boards.")
    ap.add_argument("boards", nargs="+", help="ats:board, e.g. greenhouse:stripe ashby:ramp lever:palantir")
    ap.add_argument("-k", "--keyword", action="append", default=[], help="keep titles containing this (repeatable)")
    ap.add_argument("-l", "--location", action="append", default=[], help="keep locations containing this (repeatable)")
    ap.add_argument("-x", "--exclude", action="append", default=[], help="drop titles containing this (repeatable)")
    ap.add_argument("--days", type=int, help="only roles posted in the last N days")
    ap.add_argument("--json", action="store_true", help="print JSON instead of a table")
    args = ap.parse_args()

    keywords = [k.lower() for k in args.keyword]
    locations = [l.lower() for l in args.location]
    excludes = [x.lower() for x in args.exclude]
    since = datetime.now(timezone.utc) - timedelta(days=args.days) if args.days else None

    results, notes = [], []
    for spec in args.boards:
        ats, _, board = spec.partition(":")
        if ats not in SOURCES or not board:
            notes.append(f"{spec}: use ats:board with ats one of greenhouse, ashby, lever")
            continue
        try:
            jobs = list(SOURCES[ats](board))
        except urllib.error.HTTPError as e:
            hint = " (wrong board name or wrong ATS, not 'no openings')" if e.code == 404 else ""
            notes.append(f"{spec}: HTTP {e.code}{hint}")
            continue
        except (urllib.error.URLError, ValueError) as e:
            notes.append(f"{spec}: {e}")
            continue
        kept = [dict(j, company=board) for j in jobs if matches(j, keywords, locations, excludes, since)]
        notes.append(f"{spec}: {len(kept)} of {len(jobs)} open roles match")
        results += kept

    results.sort(key=lambda j: j["posted"] or datetime.min.replace(tzinfo=timezone.utc), reverse=True)

    if args.json:
        for j in results:
            j["posted"] = j["posted"].date().isoformat() if j["posted"] else None
        print(json.dumps(results, indent=2))
    else:
        for j in results:
            date = j["posted"].date().isoformat() if j["posted"] else "----------"
            pay = f" | {j['pay']}" if j.get("pay") else ""
            print(f"{date} | {j['company']} | {j['title']} | {j['location'] or 'n/a'}{pay}\n           {j['url']}")
    for n in notes:
        print(n, file=sys.stderr)


if __name__ == "__main__":
    main()
