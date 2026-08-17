# The board split, from atelier's end — the generator was written for the repo it lives in (2026-08-17, 0530 UTC)

**The ask.** Mike, opening the session: *"Now there are no other active sessions
do the 'board split' of the roadmap. Atelier repo details whats expected and
why."* Sent to an atelier session at the same minute sessions appeared in `ros`,
`shed` and five other children — a fleet-wide launch, one repo each.

**What that means here, and it is not what it first looks like.** atelier's own
board split landed 2026-08-15 and is done; there is no split left to run in this
repo. atelier's job in a fleet rollout is different — it is the worked example
and the source of the spec, so the useful work is making the spec **true and
reachable** for the children splitting their boards right now. That reading was
not assumed: `ListAgents` showed `ros-c2` and `shed-a4` started four and five
minutes earlier, and `faves` had already migrated the day before. The two repos
item `030` names were being migrated as this session ran.

**One premise in the ask was false, and it changed how the work was done.**
"No other active sessions" — there were nineteen peers listed, two of them
atelier sessions and one a `faves` session that messaged this one mid-flight.
So: claim on `main` before the worktree, explicit staged paths, and every
measurement re-read at head. The claim commit's push was rejected on the first
attempt because a peer had landed in between; the index conflict that followed
was resolved the way the board's own doctrine says to resolve it — rebuild, not
hand-merge.

---

## What landed

**Three figures on item `030` were wrong, all in the same direction.** The
fleet-rollout item was written before any child had moved and priced the work
from stale numbers: `ros` 5,213, `shed` 3,125, `faves` 1,853. Measured at HEAD:
**5,513**, **3,465**, and `faves` was **6,274** — out by 4,421 lines. The item
now records `faves` as done (2026-08-17, 6,274 lines → 48 sections / 271-line
index, the `board` floor check live in a child for the first time), carries the
playbook `faves` proved so `ros` and `shed` need not rediscover it, and states
plainly that the rollout shipped with this item's own review gate still shut —
so both of BS1's probed slips now ride in a child too.

**The defect the first child paid for, fixed.** `board.py` hard-coded
`tools/board.py` into three strings a *child* reads: the index banner, the index
preamble, and the stale-index remedy the check prints. Children call the floor's
tools and never vendor them (ADR 0008), so all three named a file that is not
there — including the single instruction printed at the top of the one file
readers are told never to hand-edit, and the remedy line, which fires at the
exact moment a reader is least able to guess. `faves` had made the banner true
the only way a child could: a delegating shim whose own docstring says it exists
to stop the banner lying.

`rebuild_cmd()` now decides per root — repo-relative where the tool sits inside
the tree it rebuilds, the hook's own `python3 "$ATELIER_TOOLS"/board.py rebuild`
where it does not, and **never an absolute path**, which would trade a wrong
string for a machine-local fact in a file that may be public. The banner names
no path at all (115 → 69 columns). The marker is matched as a prefix against
both spellings in `board.py` and `pointerscan.py`, so no repo needs a flag day.

🔑 **The selftest's root is a tempdir, which is exactly a child's geometry** —
the tool is outside the tree it is rebuilding. So the child spelling is what the
offline test already exercises, and two assertions were added to read it,
including one that no home directory reaches the index.

**The scanner-facing half of the same root, half fixed.** The index rendered
each section's path as its link *text*, and `pathscan` resolves both halves of a
link: 28 false findings per commit here, 49 in `faves`, warn-only, forever.
Sections now render `*[Narrative](roadmap/<dir>/README.md)*` — the `##` heading
directly above already names the section, so a title would restate what the
reader just read. Atelier's index: 28 generator-caused findings → **0**. The one
that remains is real (`F1/GUARDS.md`, a stale path inherited verbatim from an
item's title).

---

## What was measured rather than accepted, twice

**A peer's figure, and then this session's own reasoning.** `faves` filed item
`070` reporting the index also fails `wrapscan`, with *"eight lines were over"*.
Running the new generator against `faves`' board in memory and comparing to
`origin/main`: **127 of 291 lines exceed 85 columns**, not 8. That inverts the
conclusion. 8 reads as a banner problem — and the banner fix would have been
declared a fix. 127 is a shape problem: the delta this session's change removes
is **exactly** the banner plus one line per section (`faves` 127 → 78, atelier
188 → 160), and every line that remains is an item line, a markdown link whose
text is a title and whose target is a path. A wrap inside `[…](…)` stops it
being a link, and any hand-rewrap dies at the next `rebuild`.

🎯 **So two of `070`'s three options are spent and only the third survives** —
the generated file is not hand-written prose, and the prose gates should not
read it. That is a floor-policy change, not a tool fix, and it is left **open
and unruled** on the item rather than taken. Until it is ruled, every child
still writes its own `.wrapscanignore` entry.

🚩 **The near-miss worth recording.** The first instinct was "shorten the banner
to 85 columns" — which would have satisfied the report as written, produced a
green-looking commit, and left 78 findings standing in the next child. The
report's own number was what made the wrong fix look sufficient. *A defect
report priced from a partial measurement will accept a partial fix.*

---

## The class, stated once for all three

**A generator writes text that is read from somewhere it was never written
for.** Four instances now, same root: the two-depth link defect the migration
hit on day one; the banner, read by a human standing in a child; the link text,
read by another scanner in the same floor; and the wrap limit, applied to a file
nobody typed. A peer named the fifth independently in `faves` — a rule for
lifting sub-items derived from how *open* items are written, which
systematically missed a *closed* one. The general form is worth more than any of
them: **a rule inferred from the sample in front of you, applied to a population
that sample structurally excludes.**

---

## Verification

- `board.py --selftest` OK; `tools.test_board` + `tools.test_pointerscan` 46/46.
- Full `unittest discover -s tools` suite run; `board check` clean at every
  commit; the floor's hook plane ran on each.
- `pathscan` against `docs/ROADMAP.md`: 28 → 1, and the survivor was read and
  confirmed real rather than assumed false.
- `faves` figures computed from `origin/main` and from
  `git show 672ad17^:docs/ROADMAP.md`, not from a working copy — the same lesson
  the peer had recorded an hour earlier for the same reason.

## What this session did not do

- **Did not migrate `ros` or `shed`.** Their sessions were live in their own
  repos, which is where that work belongs (`PROPAGATION.md` § The problem — a
  child session runs in the child repo), and it is how `faves` did it.
- **Did not rule the `wrapscan` exemption**, which is Mike's.
- **Did not touch BS1–BS14**, which await his ruling round.
