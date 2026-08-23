# 2026-08-23 · 1314 UTC · A recovery, then five defects closed in the instruments

**Tier:** Opus 5 (1M context). **Worktrees:** `report-lies-0823` (adopted,
not created), `board-worktree-spelling`, `mixed-root-eleven-0823`,
`linkscan-refstyle-0823`, `board-dup-numbers-0823`.
**Commission:** Mike — *"Just keep working until you cant safely or
realistically"*.

## The recovery, before any new work

The onramp found exactly what `CONCURRENCY.md` § *Surviving an interrupted
session* describes: a last commit, then silence. `worktree-report-lies-0823`
held two pushed commits, no PR, no closing entry, last commit 53 minutes old.
The sweep ran before anything was touched, and the decisive evidence was not a
timer but a process check — of nine live `claude` processes on this machine,
exactly one had a working directory inside atelier and it was this session's
own. Dead, not live, so the recovery was in lane rather than someone else's to
run.

It was also unfinished in a way its own subject names. The `370` narrative
counted **five** instances while six items sat beneath it, its table stopped at
the guard, and a heading still claimed the rule "would have caught all three" —
an index undercounting its own contents, which is `370`'s thesis applied to
`370`. Finished and merged (PR #54): the sixth row added, the sentence family
stated as three nouns, and the heading no longer overclaiming, because the
artefact-corroboration rule reaches five of the six and stops at the guard —
corroboration needs a reader, and a guard fires when nobody is looking.

Two orphan worktrees were then put away on the evidence rather than on a timer;
the second, from 2026-08-17, was fully merged and a week idle.

## Five defects, five landings

**`board` called a current index stale from every worktree of atelier**
(PR #55, board `010/150`). Found live *during* the recovery: the same tree
reported `BLOCKED by: board` under atelier's copy of the tool and
`✓ index current` under the worktree's own, seconds apart. `rebuild_cmd` chose
between the repo-relative rebuild command and the portable child spelling by
asking whether the **executing file** sat inside `--root` — which parts from the
question the banner poses in exactly one geometry: a worktree driven by
atelier's canonical tools path, the invocation this estate's own cross-tree
guidance prescribes. Worse than cosmetic: the remedy printed beneath the false
failure expands to `python3 /board.py rebuild` in atelier, so following the only
instruction offered writes the wrong banner into atelier's own index. Fixed by
asking the tree, not the tool, with identity read from **content** — the
generated marker, a pinned format constant — so a child vendoring an unrelated
`tools/board.py` still gets the portable form and a worktree on an older commit
still gets the right one. The selftest had a case for atelier's checkout and one
for a child; the third geometry had none, which is how this survived three
revisions of that one function.

**A relative target resolved against cwd, in eleven scanners** (PR #56, board
`010/110`, 🔥). Built as specified — the item was READY TO TAKE and stayed that
way: `pointerscan`'s line copied into the eleven, and **one** parametrised test
over twelve mains (the eleven plus `pointerscan`, so the source of the fix
cannot drift out of the family). The absolute-path judgement the item left open
was **taken and pinned**, not deferred. One real break is stated rather than
smuggled: `--root repo repo` now means `repo/repo` and exits 2; two existing
tests used that spelling and were updated, and no machine caller is affected
because `floor.py` pre-resolves — which is precisely why neither CI nor the hook
had ever exercised the defect.

**`linkscan` was blind to the whole CommonMark reference family** (PR #57,
board `020/320`, 🔥). Not silence — an affirmative *"every internal link
resolves"* at exit 0 over five broken links, reproduced before anything was
touched. Fixed at the **definitions**, per the reporting child's own shape, with
the end-of-line anchor written down as the safety argument it is rather than
left as a regex detail. Fleet exposure **measured, not estimated**: both
versions run over every repo under the estate root, and exactly one changes —
`faves`, 0 → 5, all real 404s of one shape. Queued, not delivered.

**The board generator could not see a duplicate number** (PR #58, board
`010/120`, 🔥). Now asserted at both grains, redding `check` and `rebuild`
alike — papering over a collision with a well-formed index is how the last one
survived six days. The scope was widened past the item's letter for a reason
recorded in the commit rather than assumed: checking its premise turned up a
**live** item-level duplicate (`160/190`, two files, unnoticed since
2026-08-17), and shipping the section half alone would have landed a guard
running clean over a collision in its own tree. That instance is repaired
(`195`), the tie-break free because neither file had an inbound reference.

**`index_title`'s fallback swallowed the claim into the generated title**
(board `010/140`, on `main`). The child's one-line fix taken as proposed, with
the reason written into the docstring because the naive fallback is the obvious
thing to write and this is the second time it has been reasoned about. Landed
trunk-based: one small commit, and its own claim would have been moot in the
same breath as the work. `130` — the claim fragment pushing a long title past
wrapscan's exemption — is untouched and still open.

## What was verified, and how

Every landing ran the full hook floor at commit and the ci plane by hand, read
off **explicit exit codes** rather than a pipe. Final state: 1,376 Python `OK`,
235 node 0-fail, floor ci plane exit 0, board index current.

Four of the five were **proven against a known-bad input before being
believed** — `370/030`'s rule, filed that same morning by the very session
recovered above. The new tests were re-run with `PYTHONPATH` pointed at the
unfixed tools and had to fail: 12 failures for the mixed-root test, 5 for
linkscan, 4+1 for the duplicate-number check, 1 for the claim-in-title fix.
**That step earned its keep twice.** Two of the duplicate-number tests passed
against the unfixed tool — a new file makes the index stale, so `check` reds
whether or not the collision is seen — and were rewritten to rebuild first. A
test that passes either way proves nothing, and only the negative run says so.

## The rule-4 judgement, stated so it can be overturned

None of the five queued a `⏳` pointer, and the grounds are the same in each:
they change no rule about what is permitted or required, they make existing
checks stop reporting states that were not there, and every correction is
pinned mechanically — rule 4's own escape for ordinary code, which is sound
exactly where a wrong rejection is caught by a machine. The one design choice
that was *this session's* rather than an item's — widening the duplicate-number
check to item numbers — is argued in its own commit rather than assumed. If any
of it reads as doctrine by function, the pointers are cheap to add after the
fact.

## Left for Mike

- ✅ `010/110`'s unruled wording question from 2026-08-17 was **put to Mike in
  this session and ruled**: correct the lead sentence rather than annotate it,
  on the reason that carries — a skim reader only ever reads the first line.
  The severity half was already moot. Both ends of the item now say the same
  thing, and the ruling is recorded inside it (`c766658`).
- 🚩 A **peer atelier session appeared mid-sitting**, after this one's own
  recovery had closed: `worktree-report-lies-0823` was re-created at
  `8648622` (filing a `380` item, 13 minutes before close) with its worktree at
  `~/worktrees/at-report-lies-0823b`. Left entirely untouched — it appeared
  *during* this session, which is positive evidence of company rather than the
  residue the earlier sweep dealt with. It is one commit ahead of `main` on a
  branch, and its index will want a rebuild rather than a hand-merge.
- 🚩 `faves` will red on its next CI run: five genuine broken pointers, each
  with its fix named by linkscan's own suggester. The repair belongs to a
  `faves` session, not this one.
- 🤔 `010/130` (a claim on a long title fails wrapscan on both surfaces) stayed
  open deliberately. `140` was the half with a chosen fix; `130`'s three
  candidate shapes include one that is a rule change, and that is a ruling.
