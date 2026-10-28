# djmix-tracklist

Build a timestamped track list from a long DJ mix or live set.

The tool cuts short samples from the recording, identifies each one with Shazam,
and merges the results into a list you can paste into a web page or a post.
It was built by The Fertile Soil to add track lists to our community DJ recordings.

## Requirements

- Python 3.10 or newer
- ffmpeg and ffprobe
- `pip install -r requirements.txt`

## Use

```
python scripts/scan.py mix.mp3 60 0  > hits_a.jsonl
python scripts/scan.py mix.mp3 60 30 > hits_b.jsonl
python scripts/merge.py hits_a.jsonl hits_b.jsonl
```

The first number is the step in seconds. The second is the starting offset.
Running two passes offset by half the step catches short blends.
Use a smaller step (20 to 30 seconds) to zoom in on a section.

## Second pass for vocals, acapellas and layered samples

The first pass finds full tracks. DJs also lay acapellas, vocal snippets and
samples over other tracks. These show up as matches that appear only once, so
they need a second pass of their own.

1. Run both offset scans from the section above and merge them. Tracks matched
   in two or more samples are your main track list.
2. Entries marked "unconfirmed, heard once" go in a separate second section,
   for example "Vocals, acapellas and layered samples". Keep them out of the
   main list.
3. Zoom in on each one. Scan again with a small step (10 to 15 seconds) and an
   offset that lands just before that time, then read only the rows near it.
   This shows how long the layer lasts and whether the match repeats.
   ```
   python scripts/scan.py mix.mp3 15 <seconds-before-the-time> > zoom.jsonl
   ```
4. Listen to the section. A title that names an acapella, a vocal or a remix
   usually means a layer. A match from an unrelated track is probably a sample
   or a mistake. Keep only what you can hear.
5. Give each entry the same three parts as the main list: the jump point, the
   artist page and the YouTube link. Tag clear vocal-only entries "vocal".
6. Say at the top of the section that these were heard once. Readers should
   know they are short layers and not full tracks.

## Check the results

- Shazam can return a wrong match from a single sample. Tracks heard once are
  marked unconfirmed. Listen before you publish them.
- Blends, edits, acapellas and remixes are often missed. Fill gaps by ear.
- Mixes with live vocals over a track can confuse matching.

## The skill

`SKILL.md` describes the workflow in the Agent Skills format, so an AI
coding assistant can run it for you.

## Share and improve

This project is MIT licensed. Fork it, change it, and share your version.
Ideas: other recognition services, vocal-only detection, a web interface.
