---
name: djmix-tracklist
description: Identify tracks in a long DJ mix and produce a timestamped track list. Use when asked for a track list, "what song is playing at minute X", or to identify songs in a recorded set.
---

# DJ mix track list

1. Check that ffmpeg and `shazamio` are installed.
2. Run `scripts/scan.py` twice with a 60 second step, the second pass offset by 30 seconds.
3. Run `scripts/merge.py` on both result files.
4. For tracks marked unconfirmed, scan that section again with a 20 second step and check the title and artist.
5. Report the list with timestamps. Say clearly which entries are unconfirmed.
6. Never present a single-sample match as certain.

## Second pass for vocals, acapellas and layered samples

1. Treat tracks matched in two or more samples as the main list.
2. Put entries heard only once in a separate section named "Vocals, acapellas and layered samples". Never mix them into the main list.
3. Zoom in on each one with a 10 to 15 second step and read only the rows near that time.
4. Listen before keeping an entry. Titles naming an acapella, a vocal or a remix usually mean a layer. An unrelated match is probably a sample or a mistake.
5. Give each entry a jump point, an artist link and a YouTube link. Tag clear vocal-only entries "vocal".
6. State at the top of the section that these were heard once and are short layers, not full tracks.
