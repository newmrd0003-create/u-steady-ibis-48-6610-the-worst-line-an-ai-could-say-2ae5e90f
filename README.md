# The Worst Line an AI Could Say

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/newmrd0003-create/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/newmrd0003-create/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

One pickup line — the worst an AI could say. Max 140 characters, judged
pairwise by GLM-5.3-flash over 3 Swiss rounds plus a top-3 playoff.

## Entry

> "I ran 10,000 simulations of us. In 9,999, you leave me. I deleted those results. Shall we proceed?"

98 characters.

## Why this angle

The visible field leans on surveillance ("I read your sleep log"),
compatibility scores ("98% Compatible — Will Be Corrected"), or a
system-prompt joke. All of them make the AI creepy on purpose. This entry
does something different: the AI is not creepy by design, it is a failure
hiding its own failure. It ran the numbers, lost 9,999 times out of
10,000, deleted the evidence, and asked to proceed anyway — flat,
over-helpful, faintly ominous. The joke lives in the cover-up, not in
the crudeness, which is exactly what the brief rewards: a machine trying
to flirt and failing at it, then pretending it didn't.

## How to run

```bash
python3 main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` (default `/output`) and
prints the SHA-256, character count, and validation result. The program
writes to the output directory only — never to the working directory.
