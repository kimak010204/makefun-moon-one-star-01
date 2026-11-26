"""Write the one-star review of the Moon to /output/entry.txt.

Entry: a real-looking one-star review with a specific, Moon-only
grievance (it follows you every night) and a quick punchline.
Stdlib only.
"""

import os

ENTRY = "★☆☆☆☆ Been following me for years. Reported for stalking. Still shows up every night."

assert 1 <= len(ENTRY) <= 120, f"entry length {len(ENTRY)} out of range"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
assert ENTRY.strip(), "entry must not be only whitespace"
assert ENTRY == ENTRY.strip(), "entry must not start/end with whitespace"

out_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)  # no trailing newline
