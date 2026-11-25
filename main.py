#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program.

Writes one joke about office life, a single line under 200 characters,
to /output/entry.txt, as the competition requires.

The line was chosen by manual ranking against the kit's published judge
brief (see ../candidates.md): it is unmistakably about office life, the
observation is true to the office (email), the turn is surprising (the
complicity escalation in the last clause), it is tight at 103 characters,
and it is an original angle, not a familiar line with the nouns swapped.
"""

import os

JOKE = "I wrote 'as discussed' in an email about something we never discussed, and three people agreed with me."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    # The text is plain ASCII, so it is valid UTF-8 by construction.
    text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
