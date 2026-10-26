#!/usr/bin/env python3
"""Confirm the published page is serving the deep-link build before the URL
goes into a submission. Exits 0 once the marker is present."""
import sys
import time
import urllib.request

URL = "https://noorbsharma21.github.io/rittenhouse-night/"
MARKER = "URLSearchParams"          # only present once deep links shipped

for attempt in range(1, 41):        # up to ~10 minutes
    try:
        with urllib.request.urlopen(URL, timeout=10) as r:
            body = r.read().decode("utf-8", "replace")
        if MARKER in body:
            print(f"deep-link build is live after {attempt} tries "
                  f"({len(body)/1024:.0f} KB)")
            sys.exit(0)
        print(f"try {attempt}: serving an older build ({len(body)/1024:.0f} KB)")
    except Exception as e:
        print(f"try {attempt}: {type(e).__name__} {e}")
    time.sleep(15)

print("deep-link build still not live after 10 minutes")
sys.exit(1)
