#!/usr/bin/env python3
"""
YouTube transcript fetcher for the magic practice.

Fetches transcripts from individual videos or entire channels,
stores them organized by channel in box/transcripts/.

Based on Kermit's ytsum project (~/Code/ytsum/).

Usage:
    # Single video
    python3 box/transcripts/ytfetch.py https://www.youtube.com/watch?v=VIDEO_ID

    # Entire channel (fetches all videos)
    python3 box/transcripts/ytfetch.py https://www.youtube.com/@channel_name/videos

    # Channel with limit
    python3 box/transcripts/ytfetch.py https://www.youtube.com/@channel_name/videos --limit 10

    # List what we have
    python3 box/transcripts/ytfetch.py --list
    python3 box/transcripts/ytfetch.py --list --channel "ogabbab the oracle"

    # Custom languages
    python3 box/transcripts/ytfetch.py URL --languages en,de,es
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse, parse_qs

TRANSCRIPTS_DIR = Path(__file__).parent


def extract_video_id(url: str) -> str:
    """Extract video ID from a YouTube URL."""
    if "youtu.be" in url:
        return url.split("/")[-1].split("?")[0]
    elif "youtube.com" in url:
        parsed = urlparse(url)
        qs = parse_qs(parsed.query)
        if "v" in qs:
            return qs["v"][0]
    raise ValueError(f"Cannot extract video ID from: {url}")


def is_channel_url(url: str) -> bool:
    """Check if URL points to a channel rather than a single video."""
    return any(p in url for p in ["/@", "/channel/", "/c/", "/user/"]) or url.endswith("/videos")


def sanitize_filename(name: str, max_length: int = 50) -> str:
    """Convert string to a safe filename."""
    safe = "".join(c for c in name if c.isalnum() or c in (" ", "-", "_")).rstrip()
    return safe[:max_length] if max_length else safe


def get_video_metadata(video_id: str) -> dict:
    """Get video title and channel name via yt-dlp."""
    import yt_dlp

    ydl_opts = {"quiet": True, "no_warnings": True, "skip_download": True, "ignore_no_formats_error": True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
            return {
                "title": info.get("title") or video_id,
                "channel": info.get("uploader") or info.get("channel") or "Unknown Channel",
            }
    except Exception:
        return {"title": video_id, "channel": "Unknown Channel"}


def get_channel_video_ids(channel_url: str, limit: int = 0) -> list[dict]:
    """Get all video IDs and metadata from a channel URL."""
    import yt_dlp

    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True,
        "skip_download": True,
    }
    if limit:
        ydl_opts["playlistend"] = limit

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)
        if not info:
            return []

        channel_name = info.get("uploader") or info.get("channel") or "Unknown Channel"
        entries = info.get("entries", [])

        videos = []
        for entry in entries:
            if entry and entry.get("id"):
                videos.append({
                    "video_id": entry["id"],
                    "title": entry.get("title") or entry["id"],
                    "channel": channel_name,
                })
        return videos


def fetch_transcript(video_id: str, languages: list[str] = None) -> str:
    """Fetch transcript text for a video."""
    from youtube_transcript_api import YouTubeTranscriptApi

    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id, languages=languages or ["en", "de"])
    return " ".join(entry.text for entry in transcript)


def save_transcript(metadata: dict, transcript: str) -> Path:
    """Save transcript to channel-organized file."""
    channel_dir = TRANSCRIPTS_DIR / sanitize_filename(metadata["channel"], max_length=0)
    channel_dir.mkdir(parents=True, exist_ok=True)

    safe_title = sanitize_filename(metadata["title"])
    file_path = channel_dir / f"{safe_title}.txt"

    content = (
        f"TITLE: {metadata['title']}\n"
        f"CHANNEL: {metadata['channel']}\n"
        f"URL: {metadata['url']}\n"
        f"VIDEO ID: {metadata['video_id']}\n"
        f"FETCH DATE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"\nTRANSCRIPT:\n{'-' * 50}\n"
        f"{transcript}"
    )
    file_path.write_text(content, encoding="utf-8")
    return file_path


def already_fetched(channel: str, title: str) -> bool:
    """Check if we already have a transcript for this video."""
    channel_dir = TRANSCRIPTS_DIR / sanitize_filename(channel, max_length=0)
    if not channel_dir.exists():
        return False
    safe_title = sanitize_filename(title)
    return (channel_dir / f"{safe_title}.txt").exists()


def fetch_video(url: str, languages: list[str] = None, video_id: str = None, metadata: dict = None) -> Path | None:
    """Fetch and save a single video's transcript. Returns file path or None on failure."""
    try:
        vid = video_id or extract_video_id(url)
        meta = metadata or get_video_metadata(vid)

        if already_fetched(meta["channel"], meta["title"]):
            print(f"  skip (exists): {meta['title']}")
            return None

        transcript = fetch_transcript(vid, languages)
        meta_full = {**meta, "url": url or f"https://www.youtube.com/watch?v={vid}", "video_id": vid}
        path = save_transcript(meta_full, transcript)
        print(f"  saved: {meta['title']}")
        return path
    except Exception as e:
        title = (metadata or {}).get("title", video_id or url)
        print(f"  FAIL ({title}): {e}")
        return None


def fetch_channel(channel_url: str, languages: list[str] = None, limit: int = 0):
    """Fetch all transcripts from a channel."""
    print(f"Scanning channel: {channel_url}")
    videos = get_channel_video_ids(channel_url, limit=limit)
    print(f"Found {len(videos)} videos\n")

    saved, skipped, failed = 0, 0, 0
    for v in videos:
        url = f"https://www.youtube.com/watch?v={v['video_id']}"
        result = fetch_video(url, languages, video_id=v["video_id"], metadata=v)
        if result:
            saved += 1
        elif result is None and already_fetched(v["channel"], v["title"]):
            skipped += 1
        else:
            failed += 1

    print(f"\nDone: {saved} saved, {skipped} skipped (existed), {failed} failed")


def list_transcripts(channel_filter: str = None):
    """List available transcripts."""
    if not TRANSCRIPTS_DIR.exists():
        print("No transcripts directory found")
        return

    for d in sorted(TRANSCRIPTS_DIR.iterdir()):
        if not d.is_dir():
            continue
        if channel_filter and channel_filter.lower() not in d.name.lower():
            continue

        files = sorted(d.glob("*.txt"))
        if files:
            print(f"\n{d.name} ({len(files)} transcripts):")
            for f in files:
                print(f"  - {f.stem}")


def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube transcripts for the magic practice")
    parser.add_argument("url", nargs="?", help="YouTube video or channel URL")
    parser.add_argument("--limit", type=int, default=0, help="Max videos to fetch from channel (0 = all)")
    parser.add_argument("--languages", "-l", type=str, default="en,de", help="Comma-separated language codes (default: en,de)")
    parser.add_argument("--list", action="store_true", help="List available transcripts")
    parser.add_argument("--channel", "-c", type=str, help="Filter --list by channel name")

    args = parser.parse_args()
    languages = [lang.strip() for lang in args.languages.split(",")]

    if args.list:
        list_transcripts(args.channel)
    elif args.url:
        if is_channel_url(args.url):
            fetch_channel(args.url, languages, limit=args.limit)
        else:
            fetch_video(args.url, languages)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
