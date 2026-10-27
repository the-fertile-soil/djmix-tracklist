# djmix-tracklist




Build a timestamped track list from a long DJ mix or live set.




The tool cuts short samples from the recording, identifies each one with Shazam,
and merges the results into a list you can paste into a web page or a post.
It was built by The Fertile Soil to add track lists to our community DJ recordings.




## Requirements




- Python 3.10 or newer
- ffmpeg and ffprobe
- pip install -r requirements.txt




## Use




    python scripts/scan.py mix.mp3 60 0  > hits_a.jsonl
    python scripts/scan.py mix.mp3 60 30 > hits_b.jsonl
    python scripts/merge.py hits_a.jsonl hits_b.jsonl




The first number is the step in seconds. The second is the starting offset.
Running two passes offset by half the step catches short blends.
