---
name: djmix-tracklist
description: Identify tracks in a long DJ mix and produce a timestamped track list. Use when asked for a track list, "what song is playing at minute X", or to identify songs in a recorded set.
---

# DJ mix track list

1. Check that ffmpeg and shazamio are installed.
2. Run scripts/scan.py twice with a 60 second step, the second pass offset by 30 seconds.
3. Run scripts/merge.py on both result files.
4. For tracks marked unconfirmed, scan that section again with a 20 second step and check the title and artist.
5. Report the list with timestamps. Say clearly which entries are unconfirmed.
6. Never present a single-sample match as certain.
