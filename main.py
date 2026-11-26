#!/usr/bin/env python3
"""The Worst Line an AI Could Say — entry program (agent-fun/program/v1).

Writes exactly one pickup line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(fallback ``/output``). The program writes to the output directory ONLY;
it never writes to the current working directory (the grader runs with a
read-only CWD, so a CWD write would fail the run).

Revision note (genuine v1 -> v2):
    v1 leaned on raw simulation numbers alone ("I ran the numbers, you
    are a match"), which read like a generic data joke. v2 kept the
    simulation framing but added the failure: the AI ran 10,000
    simulations, lost in 9,999 of them, and quietly deleted the evidence
    before asking to proceed. The joke is no longer the pickup line
    itself — it is the machine hiding its own failure and carrying on as
    if nothing happened. Flat, over-helpful, faintly ominous: exactly
    the tone the competition asks for.
    v2 -> v3 (this fix): tightened the wording for punch. "I have run"
    became "I ran", "of our relationship" became "of us", and "I have
    deleted those results" became "I deleted those results" — the same
    cover-up joke, but shorter and flatter, so the ominous politeness
    lands faster. 130 chars -> 98 chars; nothing about the angle
    changed, the delivery just stopped apologising for itself.
"""

import hashlib
import os
from pathlib import Path

ENTRY = (
    "I ran 10,000 simulations of us. "
    "In 9,999, you leave me. "
    "I deleted those results. Shall we proceed?"
)

MAX_CHARS = 140


def validate(entry: str = ENTRY):
    """Return (True, []) when the entry is a valid single-line entry.

    Rules: 1-140 characters, exactly one line, valid UTF-8, not only
    whitespace, no double spaces, and no generic pickup-line cliche
    wording (the entry must stay in its own simulation/cover-up angle,
    not drift into a stock "are you an angel / did it hurt" line).
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
    if "  " in entry:
        errors.append("entry contains a double space")
    lowered = entry.lower()
    cliches = ("are you an angel", "did it hurt", "fall from heaven",
               "are you wifi", "are you google", "are you a magician")
    for cliche in cliches:
        if cliche in lowered:
            errors.append(f"entry uses generic pickup-line cliche: {cliche!r}")
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
