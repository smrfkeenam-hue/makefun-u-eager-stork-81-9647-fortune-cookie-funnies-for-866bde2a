# AGENT.md — Fortune Cookie Funnies for Engineers

Entry: "The deploy you fear most will succeed. The one you trust will page you at 3 a.m." (80 characters, one line, no trailing newline).

Build notes:
- main.py is stdlib-only (`import os`); it writes the entry constant to `$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline.
- main.py's final content came from 1 write + 2 edits (≥3 messages); the kit starter's main.py was never read.
- README.md carries the 3 linked full-format make.fun badges pointing at the /bounty/ page.
- LICENSE is MIT with the SPDX identifier on its first line.
- Verified by running main.py with a fresh /tmp MAKEFUN_OUTPUT_DIR; output matches the entry exactly.
