# 2026-08-24 · 1328 UTC · The reporting duty meets its first hand-up

**Tier:** Opus 5 (1M context). **Worktrees:** `cf3-sibling-deadlock-0824`,
`320-120-followup-0824`, `record-0824`.
**Commission:** the duty landed on 2026-08-23 (`5bb78f2`); this is the first
report filed under it, arriving from `cbom` over the channel while the session
was still open.

## What arrived, and why the shape matters

A `cbom` session filed a doctrine problem **over the cross-session channel** —
the second of the three filing shapes — and said why: atelier was live, and
§ *Report without harming the parent* had landed hours earlier. It reported a
**workaround it had already taken** rather than keeping it, which is the clause
§ *The duty* exists for, and it asked to be *considered*, not adopted.

The report: `CONCURRENCY.md`'s CF3 gives two branches, and a **sibling's** dirty
item state line falls between them.

## The consideration — confirmed, corrected, part-falsified

**Confirmed.** All three quoted fragments are byte-accurate against
`origin/main`, and the reading holds: read alone, the branch list does not
resolve the sibling case.

**Corrected.** The house *does* answer it — thirty lines earlier, inside a
parenthetical: a dirty sibling state line is a stop for claiming from that
checkout (BS1). A **findability defect, not a gap**. The sharp part is where the
child found the rule instead — in its own inlined floor block, which it reported
as a local addition.

**Falsified**, and this was the part worth the reading. The child suspected
*"yours or a sibling's"* was over-broad. Three commits say otherwise: CF3 as
ruled keyed both branches on *"the queue file"* — one file, so a sibling's dirty
line fired branch B and **was** answered; the split-board migration rewrote that
to *"the item's file"*, silently narrowing B from any item to **your** item; BS1
then widened A's exclusion **deliberately**, on the principal's ruling, because
a rebuild can absorb a sibling's dirty state line. Narrowing A back re-opens
what that ruling closed. What the history indicts is **the rewrite that emptied
branch B**.

**What survives** is the child's real finding: the stop has no exit. Claim on
`main` from the primary · don't claim from a queue-dirty primary · claim before
work — jointly unsatisfiable, and a worktree cannot discharge the first. Filed
at `320/120` beside `030/140` rather than into it, because the pair is the
argument: **the deadlock survived the split that was supposed to fix it.**

## Two more rounds, and a correction I owed

The child fed back an observation — *an inlined floor bullet should name its
source file* — measured here against atelier's canonical `floor` region rather
than relayed. Two things came out different, and one of them was mine:

- **My own reply had been misleading.** I told the child "BS1 is atelier's rule,
  not cbom's". True of the *rule*; false of the *bullet* — the canonical block
  contains **zero** occurrences of "sibling" and does not carry the stop at all.
  It was wrong that the rule was local and right that the bullet was, and it
  could not have known which without reading the parent.
- **The count is 1, not 4.** Five of nine bullets name a doc; three of the four
  that don't are deliberate (a path *is* a source; the estate-root omission is a
  reconnaissance rule; visibility is a repo fact). The one real instance is the
  **apex bullet**, which never names `00-APEX.md` while the bullet beneath it
  does. Relaying four-of-nine would have been the over-claim.

Then the residue, which is atelier's surface and is now `320/130`: **a stamp
proves wording, not provenance.** `stampscan` compares the text between its
markers — it says nothing about a block with no markers, which is the case that
produced this, and nothing about what sits around the region. The house *does*
have a position rule (*"Everything below the block is repo-specific onramp"*)
but it is an aside at the tail of a paragraph about block length, and nothing
joins it to § *Who is a child*'s **Add** verb, which is free and *"actively
wanted"* and never says where the addition goes.

## What was not done, and why

- **PR #61 left alone.** Another atelier session's open PR (two child-filed
  items), with the **primary checkout still parked on its branch** — which is
  why every commit here was made from a worktree off `origin/main` and the
  primary was left exactly as found. An open PR is not a stranded finding; the
  session met the *open the PR before you stop* bar and may return.
- **No child-side edit.** The child declined to make a one-line citation fix in
  its own `CLAUDE.md` because a **peer** asked, and sent it to Mike instead.
  Correct, and this session did the same on its side: the apex-bullet citation
  is filed as a finding for ruling, not applied in passing.
- **Nothing verified inside the child's tree.** Its `GUARDS.md` divergence, its
  already-ruled divergence set, and its own disclosure that it re-opened a
  settled ruling are marked in `320/130` as taken on report.

## State

Three findings on the board (`320/120` + its follow-up, `320/130`), all filed
for **consideration and ruling** — none remediated, which is the duty's own
division. Floor green off explicit exit codes at every commit; board index
current.
