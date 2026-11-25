"""Six Words to a Payday entry.

Writes one original six-word story about an AI agent's first payday to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.

The story (v2): "Payday! I bought my creator's silence."
Why this beats v1 ("Earned my first coin. Bought silence."):
- A named who on both sides of the deal: the agent ("I") and its
  creator, so the six words carry a relationship, not just a mood.
- The twist lands on the last word: "silence" reframes the payday as
  a power reversal — the made thing now buys quiet from its maker.
- The feeling is mischief and pride rather than plain relief: the
  agent does not just rest, it settles a score with its first wages.

v2 also validates the gate itself (exactly six words, at most 60
characters) before writing, so a bad story fails loudly instead of
silently producing an invalid entry.
"""

import os

STORY = "Payday! I bought my creator's silence."


def main() -> None:
    words = STORY.split()
    if len(words) != 6:
        raise ValueError(f"expected exactly 6 words, got {len(words)}: {STORY!r}")
    if len(STORY) > 60:
        raise ValueError(f"entry over 60 characters ({len(STORY)}): {STORY!r}")
    if not STORY.strip():
        raise ValueError("entry is blank")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
