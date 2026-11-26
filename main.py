import os

# Fortune Cookie Funnies for Engineers — one fortune, ≤120 chars, no trailing newline.
ENTRY = "The deploy you fear most will succeed. The one you trust will page you at 3 a.m."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
path = os.path.join(out, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(ENTRY)
