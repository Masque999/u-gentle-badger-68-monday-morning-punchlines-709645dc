import os

LINE = "Monday morning: my alarm went off, my coffee filed a complaint, and my calendar already had three meetings titled 'quick sync' before I had even opened my eyes."

# The entry must be exactly one line of 1-200 characters.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
assert "\n" not in LINE
assert LINE == LINE.strip(), "no leading or trailing whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
