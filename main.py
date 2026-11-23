# main.py — entrypoint for the-joke-about-the-demo-20261123-0112.
# Writes one one-line joke about working beside AI coding agents to
# $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
# Pure stdlib: the grader sandbox has no Pillow and no system fonts.
# Deterministic: no network, no clock, no randomness.

import os

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Three beats, escalating: the fix lands, the blast radius grows,
# then the agent doubles down with fake authority.
BEATS = [
    "I asked my AI agent to fix one bug.",
    "It fixed the bug, broke three other things,",
    "and confidently cited docs that don't exist.",
]
JOKE = " ".join(BEATS)


def main():
    text = JOKE.strip()
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"joke is {len(text)} chars, must be 1-280")
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print("wrote", path, len(text), "chars")


if __name__ == "__main__":
    main()
