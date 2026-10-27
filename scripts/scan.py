"""Scan a DJ mix and identify tracks with Shazam.

Usage: python scan.py MIX_FILE [STEP_SECONDS] [OFFSET_SECONDS] > hits.jsonl
Cuts a 12 second sample every STEP seconds and prints one JSON line per sample.
"""
import asyncio, json, subprocess, sys, tempfile, os
from shazamio import Shazam

SRC = sys.argv[1]
STEP = int(sys.argv[2]) if len(sys.argv) > 2 else 60
OFFSET = int(sys.argv[3]) if len(sys.argv) > 3 else 0
LEN = 12


def duration(path):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
                                   "format=duration", "-of", "csv=p=0", path])
    return float(out)


async def main():
    shazam = Shazam()
    dur = duration(SRC)
    snip = os.path.join(tempfile.mkdtemp(), "snip.mp3")
    t = OFFSET
    while t < dur - LEN:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-vn", "-ss", str(t),
                        "-t", str(LEN), "-i", SRC, "-ac", "1", "-ar", "44100", snip])
        rec = {"t": t}
        for _ in range(3):
            try:
                r = await asyncio.wait_for(shazam.recognize(snip), 60)
                track = r.get("track")
                if track:
                    rec.update(title=track.get("title"), artist=track.get("subtitle"),
                               url=track.get("url"))
                break
            except Exception as e:
                rec["err"] = str(e)[:80]
                await asyncio.sleep(4)
        print(json.dumps(rec), flush=True)
        await asyncio.sleep(1)
        t += STEP


asyncio.run(main())
