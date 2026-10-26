# Cold pass — the index projects each item's logical first paragraph, with a dated grace

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes the pass. The principal's current standing ruling is that no Fable work runs
without his explicit permission, so this pass waits for that permission as well.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-26 UTC by an Opus 5.5
brief-writer subagent of session 5070f22b; the pass waits for a cold Fable session that neither
the delta's authors nor session 5070f22b (nor any of its subagents) started or instructed.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/970-rule-4-cold-pass-queued-paragraph-projection-and-grace.md`.
**Why it earns a review:** `board --check` blocks in every adopting child's CI and has no
advisory form. This change alters what every child's committed index must contain, and adds a
dated acceptance of the old form that switches itself off on a calendar date with no commit in
the child. The worst failures are a check that reds children who changed nothing, a grace that
accepts an index it should not (a silent pass on a gate whose green is read as "current"), or
an end date that behaves differently from what the notice to children says.

## Spawn provenance

- **Author of the delta:** a Mike-opened Opus 5.5 queue run, session `8e498ef1`, 2026-10-18,
  worktree `atelier-qr-010-170` by the pointer's account, and the Opus worker it dispatched,
  which the pointer says wrote the code. Neither is opened here beyond the pointer.
- **Who wrote this brief:** an Opus 5.5 subagent (`claude-opus-5-5`) dispatched on 2026-10-26
  by session `5070f22b`, a headless Opus 5.5 brief-writing session started on the principal's
  instruction of that day to have every queued brief ready for a reviewer. Session `5070f22b`
  authored none of this delta, and neither did this subagent. It is **off-tier for review,
  disclosed: it forms no finding and writes no severity**, and stops after this brief and its
  sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that passes rule 4's
  criterion. If it runs as reviewer-plus-orchestrator, rule 4's off-tier orchestrator conditions
  apply and are disclosed in the claim, the pointer and the verdict. The reviewer repeats its
  own provenance in its verdict.
- **Barred from taking the pass:** session `8e498ef1` and every worker it dispatched; session
  `5070f22b` and every subagent it dispatched, this brief-writer included.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material met before writing). It read:
  - its dispatch prompt and the dispatcher's common instruction file for this batch;
  - `skills/review-brief/SKILL.md` whole; `docs/method/REVIEW.md` lines 20–230 and 320–450;
  - for shape, the brief `docs/reviews/2026-10-18-0511-template-history-privacy-cold.md` and
    its sibling, both whole (another pass, other surfaces), and the brief section of
    `docs/reviews/2026-10-18-0508-body-free-commit-read-cold.md` above its first divider,
    whose header line states that pass's verdict and finding counts (another pass, on
    `coldsweep`); no verdict text below any divider was opened;
  - the queue pointer whole, claim line included;
  - **the intent record whole** (`010/170`), including the author's closing account below
    the principal's words; that account is held in the sibling;
  - board items `010/180` and `010/190` whole, the hand-up `320/730` whole, the first three
    lines of `320/450`, and, through a listing command, the first two lines of `180/170`;
  - the delta through `python3 tools/coldsweep.py --root . --commit 28ef94a`: subject, stat
    and the diffs of `CHANGELOG.md`, `tools/board.py` and `tools/test_board.py`; the
    `docs/ROADMAP.md` hunks were not read line by line. **No commit message body was read**;
  - `tools/board.py` lines 729–830 at HEAD and its `--help`; commit subjects, dates and stats
    from `git log` / `git show --stat --format` for the commits named below.

  It did **not** open `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` or any
  prior verdict on these surfaces. Its harness also loaded user-level and repo instruction files
  and a memory index, which hold private context this brief does not carry. Everything
  evaluative it formed is in the sibling, which holds one intent-record pointer, three
  locations of the author's account and one of other held-back framing, ten hypotheses and
  twelve re-run results.

## The acceptance test: the principal's own words

The intent record quotes the recommendation the principal answered and his answer. Read **only**
those lines, before phase 1:

```
sed -n '11,14p' docs/roadmap/010-board-store-migration-per-item-files-mik/170-the-index-projects-the-logical-first-paragraph-with-a-grace.md
```

Stop at the end of his quoted answer on line 14; the rest of line 14 onward, and lines 1–10, are
the author's account and are barred until phase 2. The same words are quoted again in a comment
in `tools/board.py` (the LEGACY block); that comment is the delta and readable, and where the
two differ the intent record governs. Judge the work against those words: the projection
change, a grace in which the check accepts both forms, its end, and telling the children.

## What the work is

- `28ef94a` (2026-10-18 09:00 UTC, on `main`) — board: project each item's logical first
  paragraph, with a grace for children. **Delta paths:** `tools/board.py`, `tools/test_board.py`,
  `CHANGELOG.md` (the `010/170` entry only) and the rebuilt `docs/ROADMAP.md`.

Read it body-free: `python3 tools/coldsweep.py --root . --commit 28ef94a` (add `--path <p>` per
file to narrow). Plain `git show` is barred: it prints the message body before the diff, and
reading is atomic (rule 1). Review the paths at HEAD as well as in the diff. Confirm with
`git log --oneline 28ef94a..HEAD -- tools/board.py tools/test_board.py CHANGELOG.md` which later
commits touched the delta paths; a later commit on `CHANGELOG.md` that is not about `010/170` is
not this delta.

Adjacent commits, **not the delta**: `63720eb` (09:01 UTC) closed the intent record, filed
`010/180` and queued the pointer. Read its subject and stat only, with
`git show --stat --format='%h %cI %s' 63720eb`; its body and its hunks on the intent record,
`010/180` and the pointer are barred until phase 2.

**The grace's removal is out of scope but in view.** It is open board work at
`docs/roadmap/010-board-store-migration-per-item-files-mik/190-remove-the-two-adoption-graces-after-their-date.md`
(filed at `0dad7ca`, 2026-10-18 09:33 UTC). You may read it in phase 1: it names what is to be
removed, and whether that list matches the code's own removal instruction in the LEGACY block
is in scope. Doing the removal, and the second grace it names in another tool (`020/150`,
queued separately at `160/980`), are not. **If `010/190` has landed by the day you run**, the
grace is gone from HEAD: review it at `28ef94a` from an extracted copy
(`git archive 28ef94a tools | tar -x -C <scratch>/at-28ef94a`), and record what HEAD now does.

**Related later evidence: the hand-up `320/730`**,
`docs/roadmap/320-child-filed-findings-via-pointing-up/730-hand-up-the-paragraph-projection-joins-a-claim-into-an-index-line-wrapscan-refuses.md`,
landed as PR #122 at `b0a17f6` (2026-10-18 12:40 UTC), after the delta, handed up by a
child's session that is not the delta's author. **It is not a prior verdict and not part of
the delta.** Its *report* of how the delta behaves in a child is **in scope as evidence of
real-world behaviour**: read lines 1–24 in phase 1, as claims to re-drive, never as findings to
adopt. Lines 25–32 carry its
author's remediation options and review note; that framing is barred until phase 2. Choosing a
remedy for it is atelier's open work under that item and **out of scope** here; whether the
delta or its notice to children should have met the case is in scope.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Probe, at least:

- **The projection.** What `item_state` now takes as the logical first paragraph, against the
  item files that exist: on this board and, read-only, on the adopting child repos on the
  machine. Every way a paragraph can end or fail to end (blank lines, unindented lines, the
  block-start pattern, tabs, CRLF, comments, fences, a state line with an empty head), and what
  each field (title, claim, flags, allow-markers) reads.
- **The grace, on both sides of its boundary.** The CLI has no date flag; `run_check` takes an
  injectable `today=` and the module reads the date through `_today_utc()`. Drive
  `board.run_check(root, fix=False, today=date(...))` from Python (or patch `_today_utc`) on the
  day before `LEGACY_INDEX_ACCEPTED_UNTIL`, on that day and after, on both planes (worktree and
  `source=board.INDEX`), for an old-form index, a new-form index, an index matching neither, and
  an index that matches the old form but where the board also has problems. **Then re-check the
  grace's behaviour on the date you actually run**, with no date injected, and state that date
  in UTC: if you run on or after 2026-11-18 the grace should already refuse the old form, and
  whether it does is a live result, not an inference.
- **The legacy renderer.** It claims to reproduce the pre-delta rendering byte for byte. Extract
  the pre-delta tools (`git archive 28ef94a^ tools | tar -x -C <scratch>/pre`) and compare its
  index against `_index_entry_v1`'s over copies of real boards.
- **The children.** Read-only, over the adopting child repos on the machine, **by count only**:
  how many have a split board, how many pass today, pass only under the grace, or fail, and how
  each count moves on the grace's end date. Establish which `board.py` each child plane runs (CI
  from `floor.yml@main`, the commit hook from the child's pinned copy) and what that means at
  the boundary. Never name a child, quote its content or write to it.
- **The notice.** The `CHANGELOG.md` entry as what reaches the children, against the acceptance
  words and the code's actual behaviour (dates, planes, the remedy command it names).
- **The tests.** Do they fail if the grace or the projection breaks? Mutate the code in a
  scratch copy (an off-by-one on the date, the grace applied under `--rebuild`, the paragraph
  stop removed) and re-run; a suite that stays green on a broken behaviour is a finding.

**Non-goals:** the board store's per-item design (`010`), and the second grace landed the same
day in another tool. The decision to have a grace at all is the principal's and is not under
review; how it was built, sized and announced is.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first, then attack
   the ones below and any you add.
2. **Correctness & quality.** Diff the commit; run the probes above live; record any overclaim
   against the text that makes it (docstrings, comments, the CHANGELOG entry, check output).
3. **Completeness / harvest.** Every surface that states how the index is projected or how
   children adopt a board change (board README, the board item template, the reviews and
   queue-run skills, any child-facing doc). Is a man page, stamp or doc change owed?
4. **Security & privacy** — mandatory. The tool reads item files and shells out to git through
   `harvestscan`; check path and argument handling against the OWASP catalogue (A03 Injection)
   by hand, and that every test fixture is synthetic. Aim `/security-review` at the code diff
   only from a clean tree (see *House rules*), or discharge it in one line with grounds.

## Load-bearing assumptions to attack

Each is a falsifiable claim; damage it with a probe or confirm it by re-driving.

1. A child that changed nothing still passes `board --check` until the grace ends, on both
   planes.
2. On and after the end date the old form reds exactly as any stale index does, and before it
   the grace never accepts an index that is stale for any other reason.
3. The legacy renderer is byte-identical to the pre-delta projection on every real board.
4. The logical-first-paragraph rule matches what a Markdown renderer shows as the item's first
   paragraph, for the item shapes that exist on this board and on the children.
5. Flags read only from the state line, and allow-markers only from the lines the title and
   claim came from, lose nothing an index line needs and carry nothing it should not.
6. The new projection produces index lines every adopting child's own enforced guards accept.
7. The CHANGELOG entry tells a child everything it needs to act before the end date.
8. The end date, as the code computes it, is the date the notice states.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing. Each line below was run once by the
brief-writer from its worktree root, in the foreground; its results are held in the sibling,
not offered here. Read exit codes explicitly; check `uptime` before the heavy ones.

- `python3 tools/coldsweep.py --root . --commit 28ef94a`
- `python3 -m unittest discover -s tools -p test_board.py -v` and
  `python3 tools/board.py --selftest`
- `python3 tools/board.py --check --root .` and `python3 tools/board.py --check --staged --root .`
- `python3 tools/wrapscan.py --root . tools/board.py tools/test_board.py`
- `git log --oneline 28ef94a..HEAD -- tools/board.py tools/test_board.py CHANGELOG.md`
- the legacy byte-identity comparison and the boundary probe described under *Scope*, from a
  script in your scratchpad that imports the worktree's `tools/board.py` by path
- the count-only child probe described under *Scope*, read-only, check mode only
- `nice -n 10 python3 -m unittest discover -s tools` (the full suite, once)
- the floor at HEAD: `nice -n 10 python3 tools/floor.py --plane ci --root .`

## House rules for this run

- Name the worktree you review from in the verdict; it is read-only to you except for THIS
  file. Other sessions may be live on this machine: touch nothing outside your worktree and your
  scratchpad. Never open another `docs/reviews/2026-10-26-*` file; each is another pass's
  framing.
- No git command that writes in the worktree, beyond committing this one file at the end of
  each phase (or handing it to your orchestrator to commit). Read-only git is fine. Extracted
  trees, board copies, mutated copies and probe scripts go under your session scratchpad, named
  by your prefix, and are deleted when you finish; never mutate the worktree's `tools/`.
- Child repos: read-only, check mode only (never `--rebuild` against a child), no scanner other
  than `board` pointed at them, and results by count. Never write a child's name, path or
  content into this file, a commit message, the pointer or a session log: this repo is PUBLIC.
- One heavy process at a time, under `nice`; the full suite at most once, in the foreground.
  Never run an installed tool by bare name from `PATH`.
- `/security-review` reads the session's pending diff, not this delta: reproduce the diff in a
  scratch clone, or discharge it by grounds — never with this brief or its sibling dirty.
- This pass is pending while you run it: anything you write to the session log, the pointer or
  a commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer, this brief's sibling
`docs/reviews/2026-10-26-0941-paragraph-projection-grace-cold.deferred.md`, the message bodies
of `28ef94a` and `63720eb`, lines 25–32 of the `320/730` hand-up, and these board items (the
intent record beyond lines 11–14, the author's follow-up item, and the upstream hand-up the
work was split from):

- `docs/roadmap/010-board-store-migration-per-item-files-mik/170-the-index-projects-the-logical-first-paragraph-with-a-grace.md`
- `docs/roadmap/010-board-store-migration-per-item-files-mik/180-the-paragraph-projection-loses-two-small-signals.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/450-a-wrapped-claim-does-not-project-and-two-more-from-a-child-s-cold-passes.md`

Code comments and docstrings in `tools/board.py` carry the author's reasons; they are the
delta, and reading the delta is never barred.

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/970-rule-4-cold-pass-queued-paragraph-projection-and-grace.md
--also-exclude docs/reviews/2026-10-26-0941-paragraph-projection-grace-cold.deferred.md
--also-exclude
docs/roadmap/010-board-store-migration-per-item-files-mik/170-the-index-projects-the-logical-first-paragraph-with-a-grace.md
--also-exclude
docs/roadmap/010-board-store-migration-per-item-files-mik/180-the-paragraph-projection-loses-two-small-signals.md
--also-exclude
docs/roadmap/320-child-filed-findings-via-pointing-up/450-a-wrapped-claim-does-not-project-and-two-more-from-a-child-s-cold-passes.md
<pattern>`; `--include-barred` only with disclosure in the verdict. The generated
`docs/ROADMAP.md` projects each barred item's title and claim; a sweep that hits it shows the
same one line the index shows everyone, and is not a breach.

## Process

**Phase 1.** Read the acceptance test; reproduce the floor first; work the lenses, the
assumptions, the probes and the re-run list. Append your verdict below a `---` divider in THIS
file: provenance repeated (how you were spawned, your tier, what you read, the UTC date you
ran), per-lens answers, the standing checklist V1–V7 each answered or discharged with grounds,
the grace's boundary results on each plane and on your run date, the child counts, findings
with stable IDs (prefix `PP`: `PP1`, `PP2`, …) and severities (MAJOR / MODERATE / minor /
note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger (commands
and results) and a follow-up checklist. Then STOP and commit this file unrevised before opening
the sibling. Edit no other file.

**Phase 2.** Open the sibling, the rest of the intent record, `010/180`, `320/450`, lines 25–32
of `320/730`, and the two barred commit bodies. Append `### Reconcile` beneath your verdict:
per-finding notes against the sibling's hypotheses, the author's account and the hand-up's
options, any finding formed at reconcile marked as such, and the overall line restated. Never
revise phase-1 text. Then fold the sibling in below the reconcile and delete it.

`board` is a CI gate that every child inherits, so it is doctrine by function (rule 3): record
all findings and apply nothing; the principal decides. Counsel per finding is welcome, labelled
as counsel and kept beneath it.
