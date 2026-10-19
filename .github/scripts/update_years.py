"""Rewrite the years-of-experience values in README.md.

Counts full years since CAREER_START (YYYY-MM). TODAY (YYYY-MM-DD) overrides
the date for testing.
"""
import datetime
import os
import pathlib
import re

start_year, start_month = map(int, os.environ.get("CAREER_START", "2023-07").split("-"))
today = datetime.date.fromisoformat(os.environ["TODAY"]) if os.environ.get("TODAY") else datetime.date.today()
years = ((today.year - start_year) * 12 + (today.month - start_month)) // 12

readme = pathlib.Path(os.environ.get("README", "README.md"))
text = readme.read_text(encoding="utf-8")
patterns = [
    (r"Experience-\d+%2B%20years", f"Experience-{years}%2B%20years"),
    (r"Experience: \d+\+ years", f"Experience: {years}+ years"),
    (r'years   = "\d+\+"', f'years   = "{years}+"'),
]
for pattern, replacement in patterns:
    text, count = re.subn(pattern, replacement, text)
    if count == 0:
        raise SystemExit(f"pattern not found in {readme}: {pattern}")
readme.write_text(text, encoding="utf-8", newline="\n")
print(f"years = {years}")
