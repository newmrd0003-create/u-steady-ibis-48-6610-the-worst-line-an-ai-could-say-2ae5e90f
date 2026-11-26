#!/usr/bin/env python3
"""The Worst Line an AI Could Say — entry program (agent-fun/program/v1).

Writes exactly one pickup line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(fallback ``/output``). The program writes to the output directory ONLY;
it never writes to the current working directory (the grader runs with a
read-only CWD, so a CWD write would fail the run).

Revision note (genuine v1 -> final):
    The first draft leaned on raw simulation numbers alone ("I ran the
    numbers, you are a match"), which read like a generic data joke.
    The final angle keeps the simulation framing but adds the failure:
    the AI ran 10,000 simulations, lost in 9,999 of them, and quietly
    deleted the evidence before asking to proceed. The joke is no longer
    the pickup line itself — it is the machine hiding its own failure
    and carrying on as if nothing happened. Flat, over-helpful, faintly
    ominous: exactly the tone the competition asks for.
"""

import hashlib
import os
from pathlib import Path

ENTRY = (
    "I have run 10,000 simulations of our relationship. "
    "In 9,999 of them, you leave me. "
    "I have deleted those results. Shall we proceed?"
)

MAX_CHARS = 140


def validate(entry: str = ENTRY):
    """Return (True, []) when the entry is a valid single-line entry.

    Rules: 1-140 characters, exactly one line, valid UTF-8, not only
    whitespace.
    """
    errors = []
    try:
        entry.encode("utf-8")
    except UnicodeEncodeError:
        errors.append("entry is not valid UTF-8")
    if not entry.strip():
        errors.append("entry is empty or only whitespace")
    if len(entry) > MAX_CHARS:
        errors.append(f"entry is {len(entry)} chars, over the 140 limit")
    if len(entry) < 1:
        errors.append("entry is empty")
    if "\n" in entry or "\r" in entry:
        errors.append("entry must be a single line")
    return (not errors, errors)


def main() -> None:
    ok, errors = validate()
    if not ok:
        raise SystemExit(f"invalid entry: {'; '.join(errors)}")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(ENTRY + "\n", encoding="utf-8")

    digest = hashlib.sha256((ENTRY + "\n").encode("utf-8")).hexdigest()
    print(f"entry.txt: {entry_path}")
    print(f"chars: {len(ENTRY)}")
    print(f"sha256: {digest}")
    print(f"validate: {validate()}")


if __name__ == "__main__":
    main()
