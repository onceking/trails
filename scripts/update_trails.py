#!/usr/bin/env python3
"""
Automated scraper and updater for the New York Ramblers Hiking Schedule.
Source & Attribution: © The New York Ramblers, Inc. (https://www.nyramblers.org/schedule/)
"""
import json
import os
import re
import urllib.request
from datetime import datetime, timezone
from bs4 import BeautifulSoup

SCHEDULE_URL = "https://www.nyramblers.org/schedule/"
META_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "last_checked.json")


def fetch_schedule_html(url: str = SCHEDULE_URL) -> str:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "NYRamblersTrailArchive/1.0 (Personal Archive with Attribution; +https://www.nyramblers.org/schedule/)"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse_schedule_entries(html_text: str) -> list:
    soup = BeautifulSoup(html_text, "html.parser")
    text_blocks = [p.get_text(" ", strip=True) for p in soup.find_all(["p", "li", "h3", "h4"])]
    date_pattern = re.compile(r"^(Sun\.|Sat\.)\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.?\s+\d+", re.I)
    extracted = []
    for idx, line in enumerate(text_blocks):
        if date_pattern.match(line):
            extracted.append({
                "raw_date_header": line,
                "context": " | ".join(text_blocks[idx:idx + 5])
            })
    return extracted


def main():
    print(f"Fetching {SCHEDULE_URL} ...")
    html_text = fetch_schedule_html()
    entries = parse_schedule_entries(html_text)
    meta = {
        "attribution": "Source: The New York Ramblers, Inc. (https://www.nyramblers.org/schedule/)",
        "last_checked_utc": datetime.now(timezone.utc).isoformat(),
        "source_url": SCHEDULE_URL,
        "detected_date_entries_count": len(entries),
        "entries_preview": entries
    }
    os.makedirs(os.path.dirname(META_FILE), exist_ok=True)
    with open(META_FILE, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)
    print(f"Saved schedule check metadata ({len(entries)} entries) to {META_FILE}.")


if __name__ == "__main__":
    main()
