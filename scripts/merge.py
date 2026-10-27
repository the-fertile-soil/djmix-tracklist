"""Merge scan results into a timestamped track list.

Usage: python merge.py hits1.jsonl [hits2.jsonl ...] [--min-hits 2]
Consecutive samples with the same track become one entry. Tracks heard only
once are marked "unconfirmed" so you can check them by ear.
"""
import json, sys

args = [a for a in sys.argv[1:] if not a.startswith("--")]
min_hits = 2
if "--min-hits" in sys.argv:
    min_hits = int(sys.argv[sys.argv.index("--min-hits") + 1])
    args = [a for a in args if a != str(min_hits)]

rows = []
for path in args:
    rows += [json.loads(l) for l in open(path) if l.strip()]
rows.sort(key=lambda r: r["t"])

runs = []
for r in rows:
    if "title" not in r:
        continue
    key = (r["title"], r["artist"])
    if runs and runs[-1]["key"] == key and r["t"] - runs[-1]["end"] <= 180:
        runs[-1]["end"] = r["t"]
        runs[-1]["hits"] += 1
    else:
        runs.append({"key": key, "start": r["t"], "end": r["t"], "hits": 1})


def stamp(s):
    s = int(s)
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}" if s >= 3600 else f"{s // 60}:{s % 60:02d}"


for run in runs:
    flag = "" if run["hits"] >= min_hits else "  (unconfirmed, heard once)"
    print(f"{stamp(run['start'])}  {run['key'][1]} - {run['key'][0]}{flag}")
