# Cold pass — `ccapple` checks the filter before it looks for a store

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 1 WRITTEN 2026-11-15 UTC by the reviewer (Fable 5.1) under drain session
21a271a5's headless orchestrator; the sibling is not yet opened. Brief written 2026-11-09 UTC.
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
