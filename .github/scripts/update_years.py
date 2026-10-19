"""Rewrite the years-of-experience badge in README.md and README.ko.md.

Counts full years since CAREER_START (YYYY-MM). TODAY (YYYY-MM-DD) overrides
the date for testing, and README (comma-separated) overrides the file list.
"""
import datetime
import os
import pathlib
import re

start_year, start_month = map(int, os.environ.get("CAREER_START", "2023-07").split("-"))
today = datetime.date.fromisoformat(os.environ["TODAY"]) if os.environ.get("TODAY") else datetime.date.today()
years = ((today.year - start_year) * 12 + (today.month - start_month)) // 12

PATTERNS = {
    "en": [
        (r"Experience-\d+%2B%20years", f"Experience-{years}%2B%20years"),
        (r"Experience: \d+\+ years", f"Experience: {years}+ years"),
    ],
    "ko": [
        (r"%EA%B2%BD%EB%A0%A5-\d+%EB%85%84%2B", f"%EA%B2%BD%EB%A0%A5-{years}%EB%85%84%2B"),  # 경력-N년+
        (r"경력: \d+년\+", f"경력: {years}년+"),
    ],
}

files = os.environ.get("README", "README.md,README.ko.md").split(",")
for name in files:
    readme = pathlib.Path(name)
    text = readme.read_text(encoding="utf-8")
    lang = "ko" if readme.name.endswith(".ko.md") else "en"
    for pattern, replacement in PATTERNS[lang]:
        text, count = re.subn(pattern, replacement, text)
        if count == 0:
            raise SystemExit(f"pattern not found in {readme}: {pattern}")
    readme.write_text(text, encoding="utf-8", newline="\n")
    print(f"{readme}: years = {years}")
