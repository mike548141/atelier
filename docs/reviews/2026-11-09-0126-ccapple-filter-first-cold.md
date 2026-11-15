# Cold pass — `ccapple` checks the filter before it looks for a store

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 2 (RECONCILE) WRITTEN 2026-11-15 UTC by the reviewer (Fable 5.1) under drain
session 21a271a5's headless orchestrator; verdict PASS-WITH-FINDINGS (0 MAJOR, 1 MODERATE, 1 minor,
3 notes). Act 1 committed as `15cb5d42`. Sibling folded below the verdict and the
review log opened at the end, 2026-11-15 UTC, by the orchestrator. Brief written 2026-11-09 UTC.
**Sizing:** **small** — one commit, 95 lines changed outside the board, one instrument, a test
module that runs in about 13 s.
**Queue pointer:** `docs/roadmap/160-doctrine-review-owed/1000-rule-4-cold-pass-queued-ccapple-checks-the-filter-first.md`.
**Why it earns a review:** `ccapple` reads the principal's own Apple stores (messages, contacts,
notes, photos, calendar, reminders, home), and its "search, never dump" gate is what keeps a whole
store out of a session. This delta moves where that gate runs. Worst failure: a reordering that lets
a store be opened with no filter, or an exit status a caller branches on that no longer means what
the manual says.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `deeac927`,
  2026-11-03, and the Sonnet worker it dispatched, which wrote the code (per the queue pointer). The
  author queued this pass and does not take it.
- **Who wrote this brief:** session `84e3aa7f` (`claude-opus-5-5`), a headless brief-writer started
  on 2026-11-09 by coordinating session `74f2b8cd` (Opus 5.5). Neither authored any of this delta,
  and neither was started or instructed by the author. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, and stops after writing its briefs. It ran
  no review and used no Fable model. The principal's rule: whoever writes a brief does not run it.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `74f2b8cd`: the
  list of board items, the run constraints, and the principal's request verbatim, "Check all the
  repo's, any work that requires a fable review but does not have a brief written yet I want you to
  write those briefs then finish this session when thats all done". It carried no framing of the
  work. The brief-writer had no contact with the author or its workers.
- **Who reviews:** a fresh Fable 5.1 session or subagent started for this pass alone, from a spawner
  that passes rule 4's criterion. **Barred from reviewing:** session `deeac927` and everything it
  started; session `84e3aa7f` (this brief-writer); session `74f2b8cd`. Whoever takes the pass states
  the spawn in the verdict (V7).
- **The principal's approval:** none yet for the pass. His request above covers this brief only. The
  pass waits for his explicit permission for Fable work.

⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):

- its dispatch text; `skills/review-brief/SKILL.md` whole; `docs/method/REVIEW.md` whole; the
  house-form brief `docs/reviews/2026-11-06-2027-secretscan-exempt-private-keys-cold.md` through
  line 728, including its verdict (read for shape, another surface); the top of one sibling brief;
- the queue pointer whole; the intent record whole;
- the delta body-free through `tools/coldsweep.py --commit 8ff5d373` (subject, stat, diff, never the
  message body), `--help` of `coldsweep`, `board`, `leakscan` and `reviewscan`, commit subjects
  through `git log`, and file names under `docs/reviews/` and
  `docs/roadmap/160-doctrine-review-owed/`;
- the last three index lines of `docs/SESSIONS.md` and one earlier session record, read for the
  format of its own closing record; and the results of the re-run lines below, held in the sibling.

It did **not** open `docs/ROADMAP-DONE.md`, any other session record, any other prior verdict, or
any delta commit's message body. Its harness also loaded user-level and repo instruction files and a
memory index, which hold private context this brief does not carry. Everything evaluative it formed
is in the sibling.

## The acceptance test

No intent record for this delta carries a ruling of the principal's. Judge it against the
instrument's own stated contract: `instruments/man/ccapple.1` (*Search, never dump*, the exit-status
list). Those are the author's claims to test, not settled scope.

## What the work is

One commit on `main`, `8ff5d373` (first confirm your tree has it: `git merge-base --is-ancestor
8ff5d373 HEAD` exits 0, or merge `origin/main` into the review branch before starting, because a
tree without the delta has nothing to review). The delta paths are in the command below.

```
python3 tools/coldsweep.py --root . --commit 8ff5d373 \
  --path instruments/ccapple \
  --path instruments/test_ccapple.py \
  --path instruments/man/ccapple.1 \
  --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Any board record the commit touches that is not listed above is barred until phase 2, so always
pass `--path`. Review each delta path at HEAD too. Confirm what has landed since with the line
below, and read anything new the same way. The delta builds on earlier work; read it only as far as
it bears on this delta.

```
git log --oneline 8ff5d373..HEAD -- instruments/ccapple instruments/test_ccapple.py instruments/man/ccapple.1 CHANGELOG.md
```

## What the delta claims (extracted, not evaluated)

- A missing filter exits 2 and names the filters needed, for all seven subcommands, even on a Mac
  with no such store.
- A search that has a filter but no store still exits 1.
- One shared check, `require_filter`, runs in `main()` before any store is resolved, and each search
  function still carries it, so the gate is unchanged.
- `instruments/test_ccapple.py` pins both statuses under an empty `HOME` (the changelog says 121
  cases).

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** `ccapple`'s first cold pass (`160/989`), which reviews the instrument as a whole and
is its own brief. The same reviewer may take both, separately. Read other parts of `ccapple` only as
far as they bear on this delta.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Ask
whether this is the right problem, solved at the right altitude. Treat this brief's account of what
the work is as attackable.
2. **Correctness & quality.** Diff the commit; run the probes live. Record each overclaim against
the text that makes it.
3. **Completeness / harvest.** Every surface that states the same thing (V3); one home (V4); no
contradiction (V5); tests that would stay green on a broken change.
4. **Security & privacy** — mandatory. `ccapple` opens the principal's private stores read-only.
Check that nothing reads a store before the gate on any path through `main()`, what an error message
discloses, and whether any subcommand can reach a store with an empty filter set. Use **synthetic**
stores only under your scratchpad: never open a real store, and quote no store content.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-09 UTC, from the worktree
root, in the foreground or niced; its results are held in the sibling. Read exit codes explicitly.
Use the `python3` on `PATH` (3.14 on this machine): `/usr/bin/python3` (3.9) cannot import
`tools/test_floor.py`.

- `cd instruments && python3 -m unittest test_ccapple`
- `for c in contacts messages calendar reminders notes photos home; do HOME=<empty scratch dir> python3 instruments/ccapple $c; echo "$c exit $?"; done`
- `HOME=<empty scratch dir> python3 instruments/ccapple messages --text x; echo $?`

## House rules for this run

**Live systems:** read-only reads of live systems as needed, no live writes. A check that would need
a write is marked **NOT RUN**, with what it would have checked. No push and no `gh` call that
writes, except committing this one file as the process below says.

- Never print a secret, and quote no key body, fixture bytes, personal data, private repo name or
  private path. This repo is PUBLIC; a child is referred to by type only.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad. Scratch
  repos, mutated copies and fixtures go under your session scratchpad and are deleted when you
  finish.
- No git command that writes in the worktree beyond committing this one file at the end of each
  phase (or handing it to an orchestrator to commit). Never mutate the worktree's `tools/` or
  `instruments/`.
- One heavy process at a time, foreground, long timeout, `uptime` first. Never run an installed tool
  by bare name from `PATH`: run it from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it only from a clean tree
  at a scratch clone of the code, or discharge it by grounds; never with this brief or its sibling
  dirty. A clean pass over markdown is weighed as nothing.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content —
the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only
after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, the queue pointer above, this brief's sibling
`docs/reviews/2026-11-09-0126-ccapple-filter-first-cold.deferred.md`, every delta commit's message
body, and the intent record
`docs/roadmap/210-instruments-open-features/340-ccapple-checks-the-store-before-the-filter.md`
beyond its first line (the title).

The delta's own text carries the author's account of why; it is the delta, and reading the delta is
never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1000-rule-4-cold-pass-queued-ccapple-checks-the-filter-first.md \
  --also-exclude docs/roadmap/210-instruments-open-features/340-ccapple-checks-the-store-before-the-filter.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, what you read, the UTC day you ran on), per-lens answers,
the standing checklist V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`8ff5d373`: read body-free yes/no,
findings by id), findings with stable IDs (prefix `CA`: `CA1`, `CA2`, …) and severities (MAJOR /
MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run
ledger and a follow-up checklist. Then STOP: act 1 is committed, unrevised, **before** the sibling
is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body; append
`### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never revise
act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding is the principal's to decide (rule 3): record all, apply nothing. Counsel per finding
is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1 (2026-11-15 UTC)

**Overall: PASS-WITH-FINDINGS — 0 MAJOR, 1 MODERATE, 1 minor, 2 notes.** The gate the brief
protects holds: on every path through `main()` the filter check runs before any store is resolved,
the message names flags and never a store, and the tests go red when the check is removed or
drifts. What fails is a claim in the delta's own record, not the code it describes (CA1).

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, tier checked at
  selection. Ran on 2026-11-15 UTC in review worktree
  `/Users/mike/worktrees/fable/atelier-160-1000-2129/atelier` at `26637295` (the claim commit;
  the delta `8ff5d373` is an ancestor, `merge-base --is-ancestor` exit 0).
- **Spawn:** a headless orchestrator session (Opus 5.5) started me; it was itself started by drain
  session `21a271a5` (Opus 5.5), running the principal's weekly Fable drain order of 2026-11-16
  06:53 NZDT (approval lapses at the reset, 2026-11-15 23:00 UTC; a pass already running may
  finish). Both are rule-4 off-tier orchestrators: they hold the context partition, form no finding
  and write no severity. Neither wrote the brief or the delta. The orchestrator read the brief, the
  board item (to claim it) and the drain instructions. I was not started or instructed by any
  barred session (`deeac927` or anything it started, `84e3aa7f`, `74f2b8cd`). No contact with the
  author or the brief-writer during the pass.
- **Spawn prompt, in substance (process only; its full text is in the orchestrator's transcript):**
  the item id and worktree path; read the brief in full and `REVIEW.md`; the rule-2 bars; write
  act 1 below a `---` divider with findings prefixed `CA`, then stop; the sibling was removed from
  the worktree on purpose and must not be sought anywhere else; keep a review log at
  `~/.claude/fable-drain/notes/atelier-160-1000-2129.md` (the one file outside the brief I may
  write); no commit, add, stash, push or branch change; `ccapple` only under a synthetic `HOME`;
  read-only reads of live systems allowed, no writes; `/security-review` by grounds or on a clean
  scratch clone; `nice`, one suite at a time, `uptime` first; never ask the principal, put asks in
  the follow-up list; end with the verdict, tally, brief path and "ACT 1 SAVED". It contained no
  question about the delta, no pointer to where the risk lives and no request about any finding.
- **What I read:** the brief whole; `docs/method/REVIEW.md` whole; the delta body-free via
  `tools/coldsweep.py --root <wt> --commit 8ff5d373 --path` × 4 (3 board-store files left out, no
  rule-2 file touched); at HEAD, `instruments/ccapple` (`main`, `check_filters`, `require_filter`,
  `require_home_mode`, `resolve_paths`, `_one`, `open_ro`, `build_parser`, `DEFAULT_PATTERNS`,
  `render_text`, the heads of the seven search functions), `instruments/test_ccapple.py` (header,
  `TmpCase`, `Cli`, `AsAProcess`, the direct guard tests), `instruments/man/ccapple.1` (*The safety
  floor*, *Exit status*), `instruments/README.md` line 28, the delta's `CHANGELOG.md` entry at
  HEAD; `--help` of `coldsweep`, `datescan`, `wrapscan`, `spellscan`, `linkscan`, `reviewscan`.
- **Exposure, disclosed:** `git log --oneline 8ff5d373..HEAD -- <4 paths>` printed about seventy
  commit subjects (CHANGELOG.md is touched often); subjects are not barred and none concerned this
  delta. My harness loaded the repo's `CLAUDE.md`, user-level instructions and a memory index that
  hold private context; none of it concerns `ccapple` or this delta. I did not open the session log,
  any prior verdict, the queue pointer or intent record beyond their titles in the brief, the
  delta's commit body, or the sibling. `--include-barred` was not used.

### Lens 1 — approach and assumptions

The problem is real and the altitude is right for the symptom named: a caller branching on exit
status was told "store missing" when the fault was "no filter", and only on Macs lacking the store.
Putting one shared check in `main()` before resolution, keyed by subcommand, is the smallest change
that makes exit 2 unconditional, and keeping each function's own guard means a library caller is
no worse off. The cost is a second copy of every filter list (CA2) and a `main()`-side gate that is
fail-open for a subcommand nobody adds to it (CA3). The deeper asymmetry the delta sits on, that
two stores resolve by glob and silently become "no store, no error", is left in place and then
asserted away in the record (CA1); fixing it at `resolve_paths` would have made the delta's claim
true for all seven.

Load-bearing assumptions I named before probing, each with its result:

| # | Assumption | Result |
|---|---|---|
| A1 | Nothing in `main()` touches a store before `check_filters(args)` | Confirmed: parse, `status` return, `--limit` check only; `HOME` read at import, no glob/open at import |
| A2 | Every subcommand argparse admits passes through the gate | Confirmed: `required=True`; `status` returns first; no cmd → argparse exit 2 |
| A3 | The pairs in `check_filters` match each function's own guard | Confirmed by side-by-side; mutation B shows drift is caught |
| A4 | A falsy filter value is "no filter", as before | Confirmed: `--id 0`, `--text ""` exit 2, same as the pre-delta `any(...)`; `Z_PK` starts at 1, not raised |
| A5 | 121 cases, about 13 s | 121 tests OK in 8.4 s under `nice` at load 8 |
| A6 | Man page exit list agrees with the code | **Damaged** for contacts/reminders (CA1) |
| A7 | Each search function still carries its guard | Confirmed: direct tests for six functions; `search_home` keeps the mode check |
| A8 | The test module never opens a real store | Confirmed: `run_script` sets `HOME` to a fresh temp dir; the one `run_cli` without `--db` first points every default glob at `<tmp>/none-*` |
| A9 | "A filter but no store still exits 1" for all seven | **Damaged**: contacts and reminders exit 0 "(no matches)" (CA1) |
| A10 | The new tests red on a broken change | Confirmed: mutations A, B, C below |
| A11 | Filter lists are one fact in two homes | Confirmed (CA2) |

### Lens 2 — correctness and quality

Re-driven, all from the worktree with `HOME` set to an empty scratch directory:

- Seven subcommands, no filter: all exit 2; each message is `ccapple: <cmd> needs at least one of
  <flags>` (home: `needs exactly one of ...`); none names a store. Matches the delta's claim.
- `messages --text x`: exit 1, `cannot read store: messages store not found`. Matches.
- `calendar|notes|photos --text x`, `home --rooms`: exit 1. `contacts --name x`, `reminders --text
  x`: **exit 0, `(no matches)`**. The CHANGELOG line "A search that does have a filter but no store
  still exits 1" and "runs all seven subcommands under an empty `HOME` to pin both statuses" are
  overclaims (CA1); the new exit-1 test covers exactly the four where it holds.
- `--limit 0` with no filter: exit 2 on the limit; both are usage errors and no store is touched.
- `mandoc -T lint -W style` on the man page: clean.
- Mutation probes on a scratch copy (deleted afterwards): **A** remove `check_filters(args)` → the
  new test reds for messages, calendar, notes, photos and home (exit 1, store named); contacts and
  reminders stay 2 because their function guard precedes any open. **B** drop `--text` from the
  messages pair → red on the exact flag string. **C** remove `search_messages`' own guard →
  `Messages.test_requires_a_filter` reds. The tests are effective in both directions.

### Lens 3 — completeness and harvest

Mirror sites swept with `coldsweep` (pointer and intent record also excluded): the man page
paragraph, the `--help` epilog ("Every search needs at least one filter"), `instruments/README.md`
line 28 ("refuses to run without a filter") and the CHANGELOG entry. Only the man page and the
CHANGELOG state the ordering; they agree (V3). The man page's *Exit status* list was not updated
and is contradicted by two subcommands (V5, CA1). The test module's header still says "the one
test that runs the script as a process" though `AsAProcess` now holds several (CA4).

### Lens 4 — security and privacy

- Order on every path: `build_parser().parse_args` → `status` returns → `--limit` → `check_filters`
  → the first `resolve_paths`/`_one`. `open_ro` is the single door and nothing calls it before the
  gate. No subcommand reaches a store with an empty filter set through `main()`; a library caller
  meets each function's own guard (mutation C).
- Disclosure: the new messages carry the subcommand and flag names only, no user input and no
  path; the exit-1 message names the app only. Nothing new leaks.
- Synthetic no-Full-Disk-Access shape (scratch `HOME`, the contacts `Sources` and reminders
  `Stores` directories `chmod 000`): `contacts --name x` and `reminders --text x` print `(no
  matches)` and exit 0, because `glob` swallows the permission error; `status` says CANNOT OPEN for
  every store. The man page promises exit 1 for "locked by macOS privacy". Pre-existing; CA1.
- `/security-review`: **discharged by grounds**. It reads the session's pending diff; the delta is
  landed, and this worktree is dirty with the removed sibling and this brief (the SL2 shape), so it
  could not be aimed at the work. The lens was run by hand above.
- Synthetic stores only; no real store opened; scratch fixtures deleted; no store content quoted.

### Standing checklist

- **V1** — CA1: two record claims stronger than the behaviour.
- **V2** — the three re-run lines and the suite re-run; results in the ledger below.
- **V3** — swept; mirror sites agree on the ordering; no finding.
- **V4** — CA2: the filter lists live in `check_filters` and in each search function.
- **V5** — CA1: the man page's exit-1 line versus contacts/reminders behaviour. Cross-references
  checked for the rule reached: the man page's *Search, never dump* reaches the rule the code
  implements; the CHANGELOG's `210/340` reaches an item I did not open.
- **V6** — run; see lens 4.
- **V7** — stated above.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `8ff5d373` | yes (`coldsweep --commit`, four `--path`) | CA1 (CHANGELOG, test shape), CA2, CA3 (`instruments/ccapple`), CA4 (`test_ccapple.py`) |

No later commit touches the instrument, its test or its man page (`git log 8ff5d373..HEAD` on each
is empty); HEAD is the delta for those three.

### Findings

**CA1 — MODERATE.** The delta's record claims an exit contract that two of seven subcommands do
not meet. `CHANGELOG.md` (the delta's entry): "A search that does have a filter but no store still
exits 1" and "runs all seven subcommands under an empty `HOME` to pin both statuses". Measured:
`contacts --name x` and `reminders --text x` under an empty `HOME` exit 0 and print `(no matches)`;
with the store's directory unreadable they do the same. Cause: these two resolve by glob,
`resolve_paths` returns `[]` and the search iterates zero stores, while the other five go through
`_one`, which raises. `instruments/man/ccapple.1` *Exit status* 1 ("A store could not be read:
missing, locked by macOS privacy (no Full Disk Access)") is therefore false for them. The new
`test_a_filter_with_no_store_is_still_exit_1` names exactly the four subcommands where the claim
holds, so the suite is green on a contract the record states for seven. **Reasoning on severity:**
not MAJOR, because the delta did not change this behaviour and the gate the brief protects is
intact; not minor, because the record now asserts the false thing, a reader of the CHANGELOG or
the man page would branch on exit 1 that never comes, and the consequence is a silent one on a
privacy instrument: a session without Full Disk Access is told a person or reminder does not
exist. *Counsel:* make `resolve_paths` raise `OperationalError("<app> store not found")` when a
default glob finds nothing (an explicit `--db` list is the caller's and may stay as it is), extend
the exit-1 test to all seven, and until then correct the CHANGELOG line and the man page's exit-1
line to name the two exceptions. The behaviour fix sits as naturally in `160/989`'s whole-
instrument scope as here; the record fix is this delta's.

**CA2 — minor (V4).** Each subcommand's filter list is written twice: in `check_filters` and in
its search function's `require_filter` call. Both drift directions fail closed (a flag missing from
`check_filters` refuses a legitimate search; one missing from the function refuses it a step
later), and the tests pin both copies (mutations B and C), so the cost today is maintenance, not
safety. *Counsel:* one table of `(cmd, [(flag, attr)])` consumed by `build_parser`,
`check_filters` and the functions, or have `check_filters` call each function's guard through one
registry.

**CA3 — note.** `check_filters` is an `if/elif` chain with no final branch, and `main()`'s own
chain ends in `else: search_reminders(...)`. A subcommand added to the parser but not to
`check_filters` passes the `main()` gate silently (its function guard still holds, so the store is
not dumped, but exit 1 returns for a missing store, the defect this delta fixed), and the new test
pins the seven by name so it would not notice. *Counsel:* an `else: raise UsageError` (or an
assertion) in `check_filters`, and derive the test's list from the parser's subcommands.

**CA4 — note.** `instruments/test_ccapple.py` line 10 still says "the one test that runs the
script as a process sets HOME to an empty temp dir first"; `AsAProcess` holds several such tests
and the delta added two without touching the sentence. The protection it describes is intact
(A8). *Counsel:* "the tests that run the script as a process".

### Re-run ledger (V2)

| Line | Where | Result |
|---|---|---|
| `( cd <wt>/instruments && nice -n 10 python3 -m unittest test_ccapple )` | python3 3.14.6, load 8.1 | Ran 121 tests in 8.387s, OK |
| seven subcommands, no filter, `HOME=<empty scratch>` | worktree | all exit 2, flags named, no store named |
| `messages --text x`, `HOME=<empty scratch>` | worktree | exit 1, `messages store not found` |
| filter + no store, each of the other six | worktree, my addition | calendar/notes/photos/home exit 1; contacts/reminders exit 0 |
| unreadable store directory, contacts and reminders | scratch `HOME`, my addition | exit 0 `(no matches)`; `status` exit 1 |
| mutations A, B, C | scratch copy, my addition | red as described in lens 2 |
| `mandoc -T lint -W style instruments/man/ccapple.1` | worktree | exit 0 |
| `/security-review` | — | NOT RUN, discharged by grounds (lens 4) |

### Follow-up checklist

- [ ] The principal decides CA1–CA4 (rule 3 shape kept: record all, apply nothing). Owed ask, in
      plain words: should `ccapple` treat "no store found" as an error for every subcommand (exit
      1, as the manual already promises), or should the manual and changelog say that Contacts
      and Reminders answer "(no matches)" when their store is missing or unreadable?
- [ ] If CA1's behaviour fix is taken, decide whether it lands under `160/989` or its own item.
- [ ] Act 2 (reconcile) after the sibling is released; the overall line restated there.

### Reconcile (act 2, 2026-11-15 UTC)

Act 1 is committed on `main` as `15cb5d42`, unrevised. Then I read: the held sibling (released by
the orchestrator with a process-only message: its path, the barred records now open, the shape of
this section, no fold, no git writes, nothing about the delta or any finding); the queue pointer
`160/1000` whole; the intent record `210/340` whole; the delta's commit message body; the author's
session record (`docs/sessions/2026-11-03-1129-queue-run-deea.md`), the instrument's record
(`2026-11-01-0618-ccapple-instrument.md`) and the brief-writer's (`2026-11-09-0104-briefs-84e3.md`),
by grep for this delta; the two index lines in `docs/SESSIONS.md` naming it; and the `160/989`
brief's Status line only (BRIEF ONLY, not run). I did not open `160/989`'s own `.deferred.md`
sibling: it is held for that pass's reviewer.

**Against the sibling's five questions** (a floor, never a fence; none steered act 1, which was
written before I saw them):

- *Q1, the two spellings of each flag list* → **CA2** reached this independently. Its second half
  is answered in act 1 (A3): no subcommand or flag today is in one copy and not the other.
- *Q2, falsy values, including a zero-like `--near` and the empty string* → act 1 probed `--id 0`
  and `--text ""` (A4). Checked at reconcile: `photos --near 0,0` and `--near 0` pass the gate (a
  non-empty string is truthy, as under the old `any(...)`; a bad coordinate is the parser's exit 2
  once a store exists), `--near ""` is "no filter" and exits 2. Same semantics as before the delta
  on every value a shell can pass. No finding.
- *Q3, every path through `main()` before the gate* → act 1 A1: parse, the `status` return (which
  opens stores by design and has no filter), the `--limit` check. None touches a store. The
  sibling's "`doctor`-style paths" has one member here, `status`.
- *Q4, does "(121 cases)" claim more than the two added tests* → the count is the module's (act 1
  A5), and the CHANGELOG sentence attaches it to "runs all seven subcommands ... to pin both
  statuses", where a reader takes 121 as the pinned cases. **Formed at reconcile, prompted by Q4,
  recorded under CA1 rather than as a new finding:** the parenthesis is a third overclaim in the
  same sentence; the fix is the same edit.
- *Q5, `assertNotIn("store", err)` as a substring on a word a flag could carry* → **CA5, note,
  formed at reconcile.** The assertion pins wording, not behaviour: a future `--store` flag or a
  message that says "stored" would red it with no regression, while the behaviour it guards is "no
  store was looked for", which `assertNotIn("cannot read store", err)` states exactly. *Counsel:*
  assert the exit-1 message's own prefix, not the bare word.

**Against the brief-writer's runs:** 121 OK under `/usr/bin/python3` 3.9 in about 15 s there; 121 OK
under 3.14 in 8.4 s here. Consistent; the brief's "use the `python3` on `PATH`" was unnecessary for
this module (the sibling shows 3.9 ran it) and harmless. `exit2` and `exit1` reproduce.

**Against the author's account** (commit body, intent record, session record):

- The body's "pin that a filter with no store is still exit 1" and the intent record's DONE line
  "exit 1 when a filter is given but the store is missing" are the same general claim as the
  CHANGELOG's, now on three surfaces. The original finding in the intent record already saw that
  `contacts` and `reminders` "check the filter first", that is, resolve by a different route, and
  did not follow that route to its missing-store exit. **CA1 stands at MODERATE**; nothing in the
  author's account answers it, and `reminders --open-only` with no store also exits 0 `(no
  matches)` (checked at reconcile; same cause).
- "The first test fails on the old code for the four subcommands that were wrong": consistent
  with the old code, where home's exactly-one-mode check sat in `main()` before `_one`
  (`8ff5d373^`, lines 1671–1672). My mutation A reds five because removing `check_filters`
  removes home's check too; that is my mutation, not the old code. No finding.
- "The messages are unchanged": confirmed by the probes in act 1.
- The pointer names the delta as "the commit that closes `210/340`, on `main`, 2026-11-03" with
  no SHA; the brief pinned `8ff5d373` and I reviewed that pin. The pointer's and the brief's
  provenance agree with the spawn I stated.

**Severities after reconcile:** CA1 MODERATE (unchanged, one more instance noted), CA2 minor
(unchanged), CA3 note, CA4 note, CA5 note (formed at reconcile).

**Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR, 1 MODERATE, 1 minor, 3 notes.**

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-15)

*Released to the reviewer only after its act-1 findings were committed and pushed to `main`
(`15cb5d42`); folded here verbatim (headings demoted two levels) and the sibling file removed, per
the brief. The orchestrator (a headless Opus 5.5 session started by drain session `21a271a5`,
itself Opus 5.5) held the partition, formed no finding and wrote no severity.*

### Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-ccapple-filter-first-cold.md` (`REVIEW.md` rule 1). Written
2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta. Open this
only after act 1 is committed. Everything here is a floor, never a fence, and none of it is a
finding.

#### The brief-writer's own questions

1. `check_filters` and each search function now spell the flag list twice. What keeps the two in
step when a flag is added (V4)? Is there a subcommand or a flag that one has and the other lacks
today?
2. Does `any(value for _, value in flags)` agree with the old per-function tests on every falsy
value a caller can pass, including `--near` with a zero-like value and the empty string?
3. The `--limit < 1` check sits before `check_filters`, and `doctor`-style paths return earlier
still: map every path through `main()` before the gate and say whether any touches a store.
4. The changelog's "121 cases" is the whole module's count. Does the sentence claim more than the
two tests the delta added?
5. `assertNotIn("store", err)` is a substring test on a word that a flag or subcommand name could
later carry. Is it pinning the behaviour or the wording?

#### What the brief-writer ran, and what it got

- `test_ccapple`: /usr/bin/python3 3.9: 121 tests OK, exit 0, about 15 s.
- `exit2`: all seven subcommands exit 2 under an empty HOME, each message naming the filters it
  needs, no traceback (3.9).
- `exit1`: exit 1, message `cannot read store` (3.9).

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*Form only: headings demoted two levels to sit under this one; no other change.*

### Review log — atelier 160/1000, ccapple filter-first cold pass

Reviewer: Fable 5.1 (claude-fable-5-1). Worktree: /Users/mike/worktrees/fable/atelier-160-1000-2129/atelier
Started 2026-11-15 21:32 UTC. Load at start: 11.42 (16 GB laptop, several passes running).

#### Act 1

- 21:32 Read the brief in full and docs/method/REVIEW.md in full. Sibling .deferred.md not opened
  (shows as deleted in git status; expected).
- 21:32 `git merge-base --is-ancestor 8ff5d373 HEAD` exit 0: the delta is in my tree.
- 21:32 python3 on PATH = 3.14.6; /usr/bin/python3 = 3.9.6.
- 21:36 Delta read body-free via `tools/coldsweep.py --root <wt> --commit 8ff5d373 --path x4`
  (3 board-store files left out; no rule-2 barred file touched). `git log 8ff5d373..HEAD` on the
  instrument, its test and its man page: empty, so HEAD == delta for those three. CHANGELOG.md has
  many later commits (other entries); I read the ccapple entry at HEAD.
- 21:36 Load-bearing assumptions I name before probing (lens 1):
  A1 nothing in main() touches a store before check_filters(args) on any subcommand path.
  A2 check_filters covers every subcommand argparse admits; no cmd falls through it.
  A3 the (flag, value) pairs in check_filters match each search function's own guard exactly.
  A4 truthiness: a legitimately falsy filter value (0, "") is treated as "no filter" — same as before?
  A5 "121 cases" and "about 13 s" reproduce.
  A6 the man page's exit-status list agrees with the new paragraph and with the code.
  A7 "each search function still carries it" holds for all seven, including home (search_home).
  A8 the test module never opens a real store: TmpCase sets HOME to a temp dir for every process run.
  A9 "a filter but no store still exits 1" holds for all seven, incl. contacts/reminders (multi-store
     globs that may resolve to an empty list rather than fail).
  A10 the new tests would go red if check_filters were removed or a pair dropped (mutation probe).
  A11 the duplicated flag lists (check_filters vs search_*) are one fact in two homes (V4).
- 21:38 Read at HEAD: main(), resolve_paths, _one, check_filters, search_home head, build_parser,
  DEFAULT_PATTERNS, open_ro, render_text; man page EXIT STATUS and "Search, never dump"; test
  header, TmpCase, AsAProcess.run_script (HOME=self.dir, a fresh temp dir per test).
- 21:38 A1 CONFIRMED by reading: before check_filters(args) main() only parses argv, returns on
  `status`, and checks --limit. HOME is read once at import (expanduser); no glob/open at import.
- 21:38 A2 CONFIRMED: add_subparsers(required=True); no-cmd exits 2 from argparse. `status` returns
  before check_filters. The final `else:` in main() is reminders.
- 21:38 A3 CONFIRMED by comparing pairs: all six lists in check_filters match the search_* guards.
- 21:39 Brief re-run line 2 (seven subcommands, no filter, HOME=empty scratch): all exit 2, each
  message names the subcommand and its flags, none names a store. Line 3 (messages --text x): exit 1
  "cannot read store: messages store not found". Both reproduce the brief's extracted claims.
- 21:39 PROBE, filter + no store, each subcommand: calendar/notes/photos/home exit 1; contacts and
  reminders exit 0 and print "(no matches)". CANDIDATE FINDING: the CHANGELOG line "A search that
  does have a filter but no store still exits 1" is false for 2 of 7; the man page's EXIT STATUS
  "1 - a store could not be read: missing ..." is contradicted for the two glob-resolved stores
  (resolve_paths returns [] and search_contacts/search_reminders iterate zero stores). The new test
  test_a_filter_with_no_store_is_still_exit_1 covers only messages/notes/photos/home.
- 21:39 Edge probes: notes --id 0 -> exit 2 (0 is falsy; Z_PK starts at 1, unreachable; same as
  before the delta, not raised). messages --text "" -> exit 2 (same as before). home with two
  modes -> exit 2. --limit 0 with no filter -> "--limit must be at least 1" exit 2 (limit check
  runs first; both are usage errors; no store touched). No subcommand -> argparse exit 2.
  Empty HOME scratch dir still empty after all runs (nothing written).
- 21:39 V3 sweep via coldsweep (two --also-exclude for the pointer and the intent record), pattern
  on never dump / refuses to run without / needs at least one of / before any store: hits in
  CHANGELOG (the delta entry and an older entry), instruments/README.md:28 (no exit code stated),
  the man page para, and the --help epilog "Every search needs at least one filter." No other
  surface states the ordering. Barred paths excluded (571 files); --include-barred not used.
- 21:40 A8 CONFIRMED: AsAProcess.run_script sets HOME to a fresh temp dir; the only in-process
  run_cli without --db is the status test, which first points cc.DEFAULT_PATTERNS at
  <tmp>/none-*; every other Cli test passes --db. No test can reach a real store.
- 21:40 A5: `( cd <wt>/instruments && nice -n 10 python3 -m unittest test_ccapple )`: Ran 121 tests
  in 8.387s, OK (python3 3.14.6, load 8.1). 121 matches `def test_` count. ~13 s in the brief is a
  sizing note; not raised.
- 21:40 A7 CONFIRMED: direct no-filter tests exist for all six search_* (test lines 480, 531, 590,
  636, 707, 832) and the home mode check (1128). search_home's own guard is the mode-validity
  check (mode is a required positional), so "each search function still carries it" holds in
  substance for home too; wording not raised.
- 21:41 A10 mutation probes on a scratch copy (instrument + test copied to scratchpad, deleted after):
  A. remove `check_filters(args)`: new test reds for messages/calendar/notes/photos/home (exit 1, the
     store named); contacts/reminders stay 2 (their function guard fires because resolve_paths
     returns [] and the guard precedes any open). B. drop ("--text", args.text) from the messages
     pair in check_filters: red on the exact flag-list string. C. remove search_messages' own
     guard: Messages.test_requires_a_filter reds (2 HelpAndManual errors are my copy lacking the
     man dir; not the delta). Tests are effective in both directions.
- 21:41 PROBE, synthetic no-Full-Disk-Access shape: HOME=<scratch> with the contacts Sources dir
  and the reminders Stores dir chmod 000. contacts --name x and reminders --text x: "(no matches)"
  exit 0 (python glob swallows the PermissionError and returns []). `status` says CANNOT OPEN
  (store not found) for every store, exit 1. Dirs restored and removed. Grounds for CA1's silent-
  failure half: the man page says exit 1 for "locked by macOS privacy (no Full Disk Access)".
- 21:41 mandoc -T lint -W style on instruments/man/ccapple.1: exit 0, no output.
- 21:41 Lens 4 reading: UsageError messages name only the subcommand and flag names (no user
  input, no path); the exit-1 message names the app only ("<app> store not found"); open_ro is the
  single door and is not reached before check_filters on any path. Nothing new to raise.
- 21:41 /security-review: discharged by grounds (see verdict): the delta is landed, not pending;
  this worktree is dirty with the removed sibling and will be dirty with the brief; shared-machine
  shape (SL2 class). Lens 4 run by hand instead.
- 21:41 Decided NOT to raise: notes --id 0 falsy (unreachable id, pre-existing); 8.4 s vs ~13 s;
  the pre-existing `sqlite3.OperationalError` used by _one to reach the exit-1 handler (works,
  pre-existing, belongs to the whole-instrument pass 160/989).
- 21:42 Findings settled: CA1 MODERATE, CA2 minor, CA3 note, CA4 note. Writing act 1.
- 21:46 Act 1 appended to the brief below a `---` divider; Status line updated to ACT 1 WRITTEN
  2026-11-15 UTC. Gates on the brief from the worktree: datescan clean (408 lines read); linkscan
  clean (0 markdown links; the sibling is cited as a code path, not a link); reviewscan clean
  (deferred material kept out of the brief); wrapscan and spellscan skip docs/reviews/ by their
  ignore files, so width and NZ spelling checked by hand: prose <= 100 columns (line 310 is 97
  characters; awk counted the arrows as bytes), only table rows exceed it. Scratch dirs removed
  (emptyhome, nofda, mut). Tree: only the brief modified and the sibling's planned deletion.
- 21:46 ACT 1 SAVED. Verdict: PASS-WITH-FINDINGS — 0 MAJOR, 1 MODERATE (CA1), 1 minor (CA2),
  2 notes (CA3, CA4). Waiting for the sibling's held path for act 2.

#### Act 2

- Release message received from the orchestrator (process only): act 1 committed and pushed to main
  as 15cb5d42; the held sibling is at ~/.claude/fable-held/atelier--2026-11-09-0126-ccapple-filter-
  first-cold.deferred.md; read it and the barred records; append ### Reconcile; do not fold or
  delete the sibling; same rules. No question about the delta or any finding.
- 21:44 Confirmed 15cb5d42 is on origin/main (merge-base --is-ancestor exit 0). Read the held
  sibling (5 questions + the brief-writer's runs on 3.9), pointer 160/1000, intent record 210/340,
  commit body of 8ff5d373, author/instrument/brief-writer session records by grep, the SESSIONS.md
  index lines, and the 160/989 brief's Status line (BRIEF ONLY). Did NOT open 160/989's sibling.
- 21:45 Reconcile probes (HOME=empty scratch, removed after): photos --near 0,0 exit 1 (gate
  passed), --near "" exit 2, --near 0 exit 1; reminders --open-only exit 0 "(no matches)" (one more
  CA1 instance). Old code 8ff5d373^ had home's mode check in main() before _one (lines 1671-1672),
  so the author's "four subcommands" claim is right; my mutation A reds five because it removed
  home's check too.
- 21:45 Sibling Q1->CA2 (independent), Q2 answered no finding, Q3 answered (A1), Q4 -> folded into
  CA1 as a third overclaim in the same sentence (formed at reconcile), Q5 -> CA5 note (formed at
  reconcile: substring "store" pins wording). Author's account answers none of CA1; CA1 stays
  MODERATE. Overall restated: PASS-WITH-FINDINGS — 0 MAJOR, 1 MODERATE, 1 minor, 3 notes.
- 21:47 Reconcile appended; Status line set to ACT 2 (RECONCILE) WRITTEN 2026-11-15 UTC. No line
  in the new section over 100 characters. Gates from the worktree: datescan clean (473 lines),
  linkscan clean, reviewscan clean; wrapscan/spellscan skip docs/reviews/ by ignore file (hand
  check done). Scratch dirs removed. Tree: brief modified, sibling's planned deletion only.
  Sibling NOT folded or deleted (orchestrator's act). ACT 2 SAVED.
