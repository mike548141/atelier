# 2026-08-22 · 0456 UTC · The ask rule reaches the children — and the list it carries gets wider

**Tier:** Opus 5 (1M). **Worktree:** `ask-rule-to-children-0822`.
**Commission:** Mike, ruling on a menu of next work, selecting two of four:
*widen the rule* and *push the ask-rule to children* — alongside *close the
session*, which is read here as the end state rather than a veto on the two he
picked. The fourth option, rebuilding `cctranscript`, is **not** taken.

## What landed

**`00-APEX.md` — the options bullet widened.** It asked for *what it buys, what
it costs, and what it affects*. It now asks for **pros, cons, impacts, risks,
costs and any other consideration that bears on the choice** — the principal's
own list, given 2026-08-22. The reason is stated in place rather than left as a
longer list for its own sake: **risk and cost are not species of impact.** A
cheap option can be the risky one, and an option can be free of impact and
expensive to take.

**The child floor gained an `Asking` bullet** — `PROPAGATION.md` § *Doctrine —
inherited from atelier*, and the same text in `docs/build/templates/CLAUDE.md`,
which the scaffold stamps. It carries the device, the overflow rule, the widened
option list, the owed recommendation, and the verified-or-marked-assumed basis,
and points at both homes for the detail.

## Why the floor and not a pointer

The block is deliberately a **safety floor**: it inlines what must bind even if
atelier is never read, and everything richer is read on demand. Until now the
ask rule was in the second category, which meant a child session met it only if
it opened `COMMUNICATION.md` — and nothing prompts it to. That is the gap the
principal's question exposed: *"Do we have work to direct repos (child and
yourself) to use askuserquestion…"*. Partially, was the honest answer. Now the
answer is yes for any child at a pin bumped past this commit.

**The compression is the known hazard here**, so it was written against the
2026-08-18 finding rather than in ignorance of it: a stamped copy read as the
source manufactures phantom debt. The bullet states the rule and names both
parent sections, so a child reading only its own block knows there is more and
where it is — it does not read as the whole rule.

## Evidence

Both suites green at the landing commit, read off explicit exit codes rather
than a pipe: **1,344 Python tests `OK` (exit 0)** and **235 node tests, 0 fail
(exit 0)** — `tools/test_templates.py` is the one that would catch the two
copies of the child block drifting apart, and it passes with both edited.
Floor `--plane ci` exit 0.

## What is not claimed

- **Children are unchanged until each bumps its own pin.** Ten-plus repos carry
  the old block; the bump is a per-repo act in the child (`PROPAGATION.md` §5),
  and nothing here touched one.
- **Nothing enforces the ask rule.** `plainscan` reads committed prose; an ask
  lives in the reply. That gap is `220/060`, still unfunded.
- The searched question — *"I believe I gave you a longer prompt"* — was
  **answered by measurement, not memory**: all 63 mentions of the device across
  both channels and every repo, back to July. There is no longer prompt. The
  2026-08-19 statement is the fullest, it is captured verbatim, and *risks,
  costs, considerations* are new on 2026-08-22 rather than something dropped.
  Recorded because the opposite conclusion — "I must have lost it" — would have
  sent a session hunting for an artefact that does not exist.

## The measurement error, carried forward

The mid-turn figures published on 2026-08-21 were wrong and were corrected the
same day (`210/100`, `320/070`): **24.3% estate-wide, not 33.5%**, because
system-injected text was counted as the principal's typing on both channels.
The child that filed the finding had written the wrong figure into its own
record on the strength of the parent's number; it was told, and corrected within
the hour. Its `RULINGS.md` hand audit — *about a third* — turns out to agree
with the corrected script figure for that repo (36.1%), so `320/080` now rests
on two independent measurements by different methods rather than one.

Self-authored doctrine, so the rule-4 `⏳` is queued at `160/290` in this
landing commit, and neither taken nor spawned here. A parallel session is
writing and running the other pointers' passes; this one wrote no brief.

**A collision was caught rather than committed.** This pointer was first
numbered `160/280`; the parallel session had taken that number on `main` while
this worktree was open. Found by reading `origin/main` before staging, not by a
merge conflict — the shared-allocator rule working as written
(`CONCURRENCY.md`: a message reserves nothing, only a pushed artefact does, so
check the allocator **after** the push).
