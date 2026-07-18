# 2026-07-18 · 1655 UTC · Fleet file-size sweep — ros harvested, shed rotated (Opus)

Continuation of the 2026-07-17 file-size session, which had **released** the ros
harvest on finding a live ros session mid-claim. Mike: "try doing ros repo
again", then "and any other repos that should be done as well".

## Liveness first (the lesson from last time)

ros was checked before claiming: **no worktrees** (the previous `radius-home`
worktree was put away), clean tree, last commit ~1h old, and the previous
session's log entry recorded an explicit close. Claimed on atelier `main` and
pushed before touching ros. ros `main` was re-checked immediately before the
merge and had not moved — no collision this time.

## Scoping the whole fleet

Ran `sizescan` across all 14 repos before starting, so the work was sized up
front rather than discovered piecemeal. Only **two** repos were over budget:
ros (4 files) and shed (1). Everything else — including faves, harvested the
previous session — was already clean.

## ros — the flagship harvest

`docs/ROADMAP.md` was at **7123 lines** (3197 when the item was filed, 4933 the
day before: ~2k/day). Its own header already declared the split it had never
performed.

**116 completed-item blocks** moved verbatim to `ROADMAP-DONE.md` behind
one-line pointers. The harvester was deliberately conservative — a block is
taken only if it is `[x]`, **longer than four lines** (short `[x]` items are
already lean, and several carry *standing rules* that are current truth), and
contains **no nested `[ ]`/`[~]` sub-item** (moving one would silently delete
open work). Two mechanical checks: every block **byte-identical** in DONE, and
the **open-item census unchanged** (`[ ]` 101, `[~]` 24 before and after).

A defect was caught mid-run: the first pointer generator let `textwrap` break a
markdown link across lines (`[ROADMAP-\n DONE](…)`), which would have rendered
broken. Fixed to keep links atomic, re-run from pristine originals — all 116
pointers well-formed, zero split links.

Also: `SESSIONS.md` 269→174 (oldest 100 index lines → `SESSIONS-ARCHIVE.md`;
the session *files* untouched), `CLAUDE.md` 257→135 (the ~124 lines its own text
called *"the legacy system"* → `docs/LEGACY-INIT.md`), and
`tiki/docs/ARCHITECTURE.md` 329→319 (dev-environment guidance → `tiki/README.md`).

## Where it honestly stops — two calls for Mike

**ros ROADMAP stays at 4755 and harvesting cannot close that.** Post-harvest the
`[x]` residue is only 431 lines; the remaining 3733 are *genuinely open* work
(101 `[ ]` + 24 `[~]` with design detail) plus 592 of prose. Reaching the 300
budget needs a structural call: migrate pending-feature detail into ros's
`docs/SPECS.md` (its own declared home, already 2263 lines), or split the
roadmap by subsystem.

**`tiki/docs/ARCHITECTURE.md` declares `sizescan:budget=320`** with the reasoning
in its header rather than sitting quietly red. ~100 of its lines are the
Purpose/outcome doctrine **cold-reviewed and ratified 2026-07-18**; trimming
freshly-ratified doctrine to hit a round number is the wrong trade. The clean
way under the 250 default is to split Purpose into its own doc — deliberately
not taken unilaterally, since the ROADMAP records this file as its canonical
home.

Both are on the atelier ROADMAP as a 🎯 principal's item.

## shed

`docs/SESSIONS.md` 318→204 (+ its own entry = 215): older entries rotated
verbatim into a new `SESSIONS-ARCHIVE.md`, all 14 verified present exactly once.
Content stays in shed — nothing about the vault's contents travels here.

**Worktree hazard found and fixed en route:** shed's `hooks.atelierTools` was the
*relative* path `../atelier/tools`, which resolves only from the main checkout —
from a worktree it points at a non-existent directory, so the fail-closed
pre-commit scanner blocked every worktree commit. Set to an absolute path
(machine-local config, never committed). ros had already fixed the same class of
bug in its leakscan hook; **worth checking on the other children.**

## Close

Fleet is `sizescan`-clean except ros's ROADMAP (the structural call above).
atelier's own ROADMAP kept at 300 by moving its two oldest completed harvest
items into `ROADMAP-DONE.md` — the same dogfood. No review owed: mechanical
relocation throughout, verified verbatim and by census, no doctrine or behaviour
changed.
