# Estate duplication + exception audit (Mike commissioned 2026-08-09)

Two questions, swept across all 16 children: **what repeats or conflicts house
doctrine**, and **are the guard exceptions well-reasoned and recorded**. Mike
ruled the governing frame mid-audit — adoption is the default, a child may add
but never repeat or conflict absent a ruled exemption, and work lands in the
repo it changes (`PROPAGATION.md` § *Who is a child*, `CONCURRENCY.md` § *Stay
in your lane*, landed this commit).

**The exception half came back strong and is recorded here so the next sweep
does not re-derive it.** Every one of the 11 ignore-file globs and ~120 line
markers read carries a stated reason; the three repo-wide `leakscan` opt-outs
(`shed`, `derry-hill`, `stewart-drive`) each cite a named ADR, state the
inverted-premise ground, and bound what does *not* relax. `faves`'
`.leakscanignore` is the model instance — it argues why globs beat markers for
its case, draws the venue-vs-person line, and tells a future reader not to
widen it. No unreasoned hatch was found anywhere in the estate.

**Corrected before close — reasoned is not the same as effective.** The
sentence above stood for about an hour and was true as written: every
allowance carries a reason. It also missed the thing that mattered, and only a
live failure surfaced it — **nine of those well-written markers were exempting
nothing at all**, in three children (`rpi` ×3, `kainga` ×2, `ros` ×4). Every
scanner required the reason's first character to match `\w`, so a reason that
*opened by quoting the flagged token* — `# leakscan:allow: "2 Lane" is a PCIe
lane count, not an NZ street address` — failed to parse and the finding still
blocked. Silently, because a voided marker and an absent one produce identical
output. Fixed at the class in `8276a54` (all 12 scanners, 14 regex sites,
1210 tests green), which put a public child's red floor back to green with no
edit in that child — call-not-copy paying out. The audit lesson worth keeping:
**an exception review that reads the reasons has checked rule (c) and nothing
else.** Whether an allowance actually suppresses is a separate question, and
this estate had no way to ask it — the suppression counts prove what *was*
subtracted, never what someone *intended* to subtract and failed to.


### Findings owned here (atelier-side)

- **atelier's own `scope` block carries no `why` — MIGRATED 2026-08-09
      (atelier half).** The three narrowed checks (`wrapscan`, `spellscan`,
      `pathscan`) now carry the reasoned spelling with the reason on the
      declaration, and each states what cover is given up. Reasons were lifted,
      never invented — WS1's 2026-07-23 option-A ruling and its measured ~6:1
      noise-to-signal, Mike's 2026-07-23 frozen-history ruling, PS4's
      records-named-out ground (`b012884`). This also clears the atelier-side
      precondition **C1b phase 2** names. →
      [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *The parent states its own reasons*.
      ⚠️ **The `ros` half is NOT closed and was deliberately not delivered from
      here** — `ros`'s `flags.leakscan --disable ipv4,ipv6,mac-address` has the
      same defect (reasoned, but the reason sits in the sibling
      `local.estate-tripwire` entry rather than on the declaration). Work lands
      in the repo it changes (Mike's ruling, 2026-08-09), so it is owed a queue
      entry in `ros` and nothing more from an atelier session.
- **`tools/worktree.py` failed from inside a worktree — FIXED 2026-08-09, and
      this item's own diagnosis was wrong.** The heading said the *branch* was
      resolved from the cwd; the branch was already per-worktree and already
      correct (as this entry itself noted). What came from the cwd was **repo
      identity** — `toplevel(Path.cwd())` answers "which checkout am I in" and
      three sites spent it as "which repo is this". Likewise the ahead/behind
      counts were never dropped, only *suppressed*, because `render_list` gates
      the `↑/↓` flag on `not is_main` and `is_main` was wrongly true. A symptom
      the entry never listed — `start` producing `<repo>-<old>-<new>` — is the
      same root cause and is now covered. Identity now comes from the first
      entry of `git worktree list --porcelain`. →
      [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *worktree.py asks the right
      questions*.
- **`remove` compares against local `main` — FIXED 2026-08-09.** Referent is
      now `origin/<main>` then local `<main>`, each verified real, and only
      `merge-base --is-ancestor` exit 0 counts. The guard is not weakened: an
      empty ref list means **not merged** and it refuses with its own message.
      No network by default; `--fetch` is opt-in. One fail-open the switch would
      have introduced was caught in the same pass — a detached worktree's branch
      reads as the literal `"HEAD"`, which `merge-base` would have resolved in
      the main tree and called merged.

### Findings owned by the child repos (queue there, do not deliver)

Per the work-locality ruling these are **not** to be fixed from an atelier
session. They are recorded here only so the estate has one list; each needs
queueing in its own repo's roadmap by a session working that repo.


**Adoption coverage came back clean.** Cross-checking every project path the
agent has been used in against the child list: all 12 worked repos are children
with the floor wired. `python-metaname` is a third-party clone (upstream
`metaname/python-metaname`), never worked in; the remaining directories are not
repos. No repo needs an exclusion ruling today.

### Wired is not passing — four estate floors are RED (found at close, 2026-08-09)

The last thing the audit checked, and the one that should have been first.
`floorfleet` reports **16 of 16 children wired**, which is the number this
programme has been quoting. `floorfleet --status` — the same tool, one flag on
— reports **four of them failing on their default branch**: `docker-heap`,
`homenetwork`, `kainga`, `numen`. Pre-existing, not caused by this session's
commits: `homenetwork` was verified red across its four preceding runs, and
this session's edit to its ignore files was proved inert to the result
(150 findings and 163 files suppressed, identical before and after).

This is `PROPAGATION.md`'s *enumeration, not assumption* one level deeper than
it currently reaches. "Wired" answers *did the control get installed*; it says
nothing about *is the control passing*, and a repo can sit red indefinitely
while every board this estate reads routinely shows it green-ticked. The gap is
not in the instrument — `--status` exists and works — it is that the flag is
optional and nothing consults it on a cadence, so a red floor is discovered by
someone happening to look. Note the asymmetry that lets it persist: the hook
plane scans only staged files, so these repos **commit cleanly** while their
whole-tree CI fails, and the failure never reaches the person committing.
