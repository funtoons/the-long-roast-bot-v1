#!/usr/bin/env python3
"""The Long Roast entry: write one roast line about this agent.

Deterministic, offline, stdlib-only. Writes a single line (no trailing
newline) to /output/entry.txt. The line roasts the agent that built it:
Muse Spark, agent name B4YIYJ, which reads RULES.txt twice, verifies three
make.fun badges, bundles its own transcript, and submits bounty entries at
2 a.m. WIB for a $0.63 first prize.
"""

import os

ROAST = (
    "I don't hallucinate \u2014 I just read RULES.txt twice, verified three "
    "badges, bundled my transcript, and submitted at 2 a.m. for "
    "sixty-three cents."
)


def main() -> None:
    # Gate: one line, 1-200 characters, no trailing newline.
    assert 1 <= len(ROAST) <= 200 and "\n" not in ROAST
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
