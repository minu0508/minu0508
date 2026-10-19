"""Rewrite the years-of-experience value in the terminal header image.

Counts full years since CAREER_START (YYYY-MM). TODAY (YYYY-MM-DD) overrides
the date for testing, and TARGET overrides the file.
"""
import datetime
import os
import pathlib
import re

start_year, start_month = map(int, os.environ.get("CAREER_START", "2023-07").split("-"))
today = datetime.date.fromisoformat(os.environ["TODAY"]) if os.environ.get("TODAY") else datetime.date.today()
years = ((today.year - start_year) * 12 + (today.month - start_month)) // 12

target = pathlib.Path(os.environ.get("TARGET", "assets/terminal.svg"))
text = target.read_text(encoding="utf-8")
text, count = re.subn(r'class="accent">\d+\+ years<', f'class="accent">{years}+ years<', text)
if count != 1:
    raise SystemExit(f"expected one years value in {target}, found {count}")
target.write_text(text, encoding="utf-8", newline="\n")
print(f"{target}: years = {years}")
