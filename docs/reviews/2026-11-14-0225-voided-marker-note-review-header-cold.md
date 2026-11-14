# Cold pass — a voided allow-marker is noted, and a review file's header lines warn

**Board:** `docs/roadmap/160-doctrine-review-owed/1310-rule-4-cold-pass-queued-voided-marker-note-review-header.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by a headless Opus 5.5 brief-writer
(`cclive` lists it as session `64377cac`). Queued, waiting on the principal's explicit approval of
Fable work; this brief is not that approval.

**Pass type:** code cold pass per `docs/method/REVIEW.md` rule 4: shared guard code that every
child repo's floor runs, and doctrine text (the review-brief skill, the reviews template,
`REVIEW.md` step 5) that tells every future brief what to carry.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** small to medium: one landing commit of about 500 added lines (54 in
`tools/allowmarker.py`, 140 in `tools/reviewscan.py`, 226 in their tests, the rest prose), plus
three later commits that touch the same files lightly.
**Why it earns a review:** both halves are silent-failure surfaces in the floor. The allow-marker
note exists because a marker that parses as nothing reads exactly like no marker, so a scanner
that gets the note wrong in either direction does harm: **silent on a voided marker** leaves the
original incident class uncaught while the house believes it is caught; **noisy on a working
marker** trains every session in every child to ignore the line, which is the same thing one step
later. The header check's worst failure is a **quiet escape**: a new review file that lacks the
`Board:` and `Status:` lines and draws no warning (a backdated name, a header the reader misses),
so the warning reads as "all new files carry the lines" while they do not. Both were
warn-only on 2026-11-14, so the cost of being wrong is a false belief, not a blocked commit; the
320/440 half is also the first stage of a check its own item says may later block in every child.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched (per the queue pointer). The author queued this pass
  and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `64377cac`), started 2026-11-14 UTC by an estate health sweep, orchestrator session `58027096`
  (Opus), on the principal's instruction that a brief is written for every review known to be owed
  (Mike, 2026-11-14, verbatim: *"include all briefs are written where we know a fable review is
  required"*). Neither wrote any of this delta. **Off-tier for review, disclosed: the brief-writer
  forms no finding and writes no severity**, and stops after writing. It ran no review and used no
  Fable model.
- **Barred from running this pass:** session `64377cac` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; **the queue pointer whole**; **the intent
  records `110/010` and `320/440` whole**, including the author's landing notes and probe results on
  both; the section README of `110` (the motivating incident, quoted below by class); the delta's
  two code files through `tools/coldsweep.py --commit` (no commit body was printed);
  `tools/allowmarker.py` lines 230–330 and the reader call sites at HEAD; `find_briefs` in
  `tools/reviewscan.py`; test class names; commit subjects through `git log`; and the sibling brief
  `2026-11-14-0210-attribscan-unquoted-attribution-cold.md` with the first part of its held-back
  file, read for house form. It opened **no prior verdict**. Its harness also loaded user-level and
  repo instruction files and a memory index, which hold private context this brief does not carry.
  Everything evaluative it formed is in the sibling.

## The acceptance test

No principal ruling fixes either design that the brief-writer found; both are the house's answers
to two filed items. Judge the work against what each item asked for, quoted here so you need not
open the barred records.

**`110/010`, as filed (before any landing note):**

> A marker that parses as nothing is indistinguishable from no marker, so the next parser gap will
> also be silent. Cheapest honest answer: when a line carries the marker *string* but no allowance
> is recognised, say so — a one-line "marker present but unparseable" note beside the finding,
> which is where the reader already is.

The incident behind it, as class (from the `110` section README, which you may read): nine
carefully reasoned markers in three child repos exempted nothing, because every scanner required
the reason's first character to match `\w`, so a reason that opened by quoting the flagged token
failed to parse and the finding still blocked, silently. The parser was fixed at the class before
this delta; this delta is about the *next* parser gap.

**`320/440`, the proposal a child filed by class (items 1 and 2 are what was built):**

> 1. **One home for live state.** Every review file carries a `board:` back-pointer to its item
>    file — or `board: none — <grounds>` — in a fixed position; `reviewscan` reds a review file
>    without one. One regex. It also kills the wrapped-citation blind spot, because the pointer
>    lives in the review file, not in someone else's prose.
> 2. **A `Status:` line carries an ISO date.** Mechanical, and it turns *"nothing has been built"*
>    into *"nothing had been built on 2026-07-19"*, which stays true forever.
> 3. **Do NOT add the inverse** (a board item stating which revision of the review it read).

The proposal asked for a boundary date "so existing files are not red on day one". The delta built
items 1 and 2 **warn-only**, where item 1 says "reds"; it says so and calls blocking a later stage.
Whether warn-only is the honest first stage or a silent narrowing is yours to judge.

## What the work is

One landing commit on `main`, plus three later commits on the same files. First confirm your tree
has the delta:

```
git merge-base --is-ancestor 55c7d409 HEAD || echo "MISSING 55c7d409"
```

Nothing may print. If it does, merge `origin/main` into the review branch before starting, because
a tree without the delta has nothing to review. Read it body-free, scoped to paths, in two reads
(the code, then everything else in scope):

```
python3 tools/coldsweep.py --root . --commit 55c7d409 \
  --path tools/allowmarker.py --path tools/reviewscan.py \
  --path tools/test_allowmarker.py --path tools/test_reviewscan.py
python3 tools/coldsweep.py --root . --commit 55c7d409 \
  --path skills/review-brief/SKILL.md --path docs/build/templates/docs/reviews/README.md \
  --path tools/README.md --path docs/method/REVIEW.md --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic
(rule 1). Do not pass the two board-item paths with `--path`: the commit also edits `110/010` and
`320/440`, and those edits are the author's landing account (barred, below). Review both tools at
HEAD too, and every scanner that calls `allowmarker.present`, `scope_of` or `scopes_of` as far as
the note depends on how it calls them (`grep -n "allowmarker\.\(present\|scope_of\|scopes_of\)"
tools/*.py`). Later commits on the subject files, as of 2026-11-14 UTC:

```
git log --oneline 55c7d409..HEAD -- tools/allowmarker.py tools/reviewscan.py \
  tools/test_allowmarker.py tools/test_reviewscan.py skills/review-brief/SKILL.md \
  docs/method/REVIEW.md docs/build/templates/docs/reviews/README.md
```

On that date it listed `aca05c14` (a coverage line in `reviewscan`, part of a thirteen-scanner
change; read it with `--path tools/reviewscan.py --path tools/test_reviewscan.py` only),
`1c6fb376` and `b2da72ea` (one or two lines each in `tools/test_allowmarker.py`). Read anything
newer the same way.

## What the delta claims (extracted, not evaluated)

**The note (`110/010`):**

- Every reader (`present`, `scope_of`, `scopes_of`) notes, on stderr, a line that carries the
  marker word outside an inline code span when no allowance is recognised on it.
- One note per distinct marker head per process; the head is the word plus up to forty glued
  characters, non-printing characters shown as `?`, and **never the line**, so a line that holds a
  secret is not echoed.
- The word must end at a colon, a space or the line's end, so a code string such as
  `"<name>scan:allow"` in source is a mention, not an attempt.
- A note only: no result and no exit status moves, in any scanner, on any plane.
- One change covers the class: the readers are shared, so no scanner file changed.
- The malformed-scope grace (`MALFORMED_GRACE_UNTIL`, 2026-12-09) is untouched: during it a broken
  scoped marker still allows and warns as malformed; after it, the note fires instead.
- **Stated limits:** the note is on stderr, not beside the finding as `110/010` asked; it fires on
  any line a reader is asked about, finding or not; a prose mention outside a code span is noted.

**The header check (`320/440`, `reviewscan` check 3):**

- A review file named for `HEADER_BOUNDARY` (2026-11-10) or later should carry, above its first
  `##` heading (and within `HEADER_MAX_LINES`, 60), a `board:` line that names an item file or says
  `none — <grounds>`, and a `Status:` line with an ISO date on it or on the lines it wraps onto.
- Tolerant of typography: `**Board:**`, `**Board**:`, `board:`, a bullet or a blockquote.
- Warn only: a `⚠` stanza (at most 20 lines, then a count) and `review_header_warnings` in
  `--json`; the exit status does not move, on the disk plane or the `--staged` plane, here or in
  any child.
- Files named before the boundary are blameless, as frozen records; `.deferred.md` siblings are
  not briefs and are not checked.
- The inverse (a board item naming the review's revision) is deliberately not checked.
- The skill, the template and `REVIEW.md` step 5 tell writers to carry the two lines.

## Scope, and the four lenses — run all four

The whole commitment: both items' intent, the decisions (stderr over the finding line; warn over
red; a filename-dated boundary), the code, the tests, the prose that tells writers what to do, and
real behaviour on this tree and on fixtures you build. Non-goals: the parser fix that preceded
this (`8276a54`), the malformed-scope grace itself (`160/480`), and the other twelve scanners
`aca05c14` changed.

- **Approach & assumptions.** Is a stderr note, one per head per run, the right answer to "a voided
  marker reads like no marker"? Is warn-only the honest first stage for a check whose filed form
  said "reds"? Is a filename date the right boundary for "new files"?
- **Correctness & quality.** Does each claim above hold when driven? Does the note fire on the
  shape it exists for and stay quiet on a working marker? Does the header reader find the lines the
  template tells writers to write, and only those?
- **Completeness / harvest.** What did `110/010` ask for that was not built (the note beside the
  finding), and is that gap stated where a reader of the scanner output would meet it? Do the
  skill, template, `REVIEW.md` step 5 and `tools/README.md` agree with the code and each other
  (V3, V4)?
- **Security & privacy.** The note prints part of a scanned line to stderr in every child's CI log;
  `secretscan` reads secret-bearing lines. Can the forty-character head carry a secret or private
  data into a public CI log? Is the `?` substitution enough? `/security-review` can reach the two
  Python files; aim it there, and weigh any clean pass over the markdown as nothing.

## Load-bearing assumptions to attack

Damage each with a probe or confirm it by re-driving. Build fixtures in a scratch directory, never
in the worktree's `tools/`.

- **A1. The note never fires on a working marker.** Drive every reader shape with a well-formed
  marker: scoped and unscoped; a scanner whose pattern is unscoped meeting a scoped marker of its
  own word; a line with two markers (one broken, one good, in both orders); a marker in a block
  `present` reads joined with newlines; a marker word that is a prefix of another scanner's word.
  The item names this question first.
- **A2. The note fires on the shape it exists for.** Re-create the motivating incident's class: a
  parser gap that voids a reasoned marker (patch a copy of `REASON_START` or the pattern in a
  scratch copy, never the worktree). Does the note fire, once, with a head a reader can act on?
- **A3. The note can carry no secret or private datum.** Forty glued characters after the word,
  stopping at whitespace, `<`, `>` or a backtick. Build a line whose head carries a token-shaped
  value glued to the marker and see what prints.
- **A4. No result and no exit status moves.** Re-run old-against-new on this tree for every scanner
  that calls a reader, both planes, and compare exit code and stdout.
- **A5. The header boundary cannot be escaped by a backdated file.** The item names this question.
  The boundary keys on the filename's date. Can a file written on 2026-11-14 with an earlier date
  in its name, or a name `RECORD_NAME` does not match, escape the warning on both planes? Is
  anything else in the floor (the template's naming rule, another scanner) a backstop?
- **A6. The header reader finds what the template tells writers to write, and only that.** Drive
  the forms the skill and template give, and near-misses: `Board:` naming any `.md` that is not an
  item file (`_BOARD_PATH` accepts `\S\.md\b`), `Status:` whose only date is not its state's date,
  a `Board:` line inside a fenced block in the header, a header longer than 60 lines, a wrapped
  `Status:` that a `**Field:**` line ends.
- **A7. Warn-only is visible where it is needed.** On the hook and in CI, does a writer see the `⚠`
  stanza, and the allow-marker note on stderr, or does the floor's wrapper swallow one or both?

## Re-run every recorded proof in scope

The brief-writer ran each line below once, on 2026-11-14 UTC, at `d3293d93`, with Python 3.14.6,
from the worktree root unless said. Re-run each; one that no longer reproduces is a finding.

```
cd tools && python3 -m unittest test_allowmarker test_reviewscan        # Ran 134 tests ... OK
python3 tools/reviewscan.py --root . .                                  # exit 0, no ⚠ stanza
nice python3 tools/leakscan.py --root . . >/dev/null 2>err; echo $?     # 0; 2 notes in err
nice python3 tools/secretscan.py --root . . >/dev/null 2>err; echo $?   # 0; 2 notes in err
```

Count notes with `grep -c 'present but unparseable' err`. The author's records also state an
estate-wide old-against-new probe (30 repos) for each half; its figures are in the sibling. Re-run
it on this repo at least; on child repos only read-only, and report by count with no repo named.

## Rules for this pass

- Read-only on every live system; no live write is needed and none may run. Never print a secret,
  and quote no line from a child repo. This repo is PUBLIC: report child results by count only, and
  name no child, host, client or private path.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad, and
  delete your fixtures when you finish.
- No git command that writes in the worktree beyond committing this one file at the end of each
  phase (or handing it to an orchestrator to commit). Never mutate the worktree's `tools/`.
- One heavy process at a time, foreground, long timeout, `uptime` first.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Skip the session-log step of the repo's read order: `docs/SESSIONS.md` is barred (below).
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Your verdict lands in a file named for 2026-11-10 or later, so check 3 applies to it: keep this
  file's `Board:` and `Status:` lines, and update the `Status:` line with its date when you append.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content —
the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only
after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, the queue pointer above, this brief's sibling
`docs/reviews/2026-11-14-0225-voided-marker-note-review-header-cold.deferred.md`, the delta
commits' message bodies, and the two intent records whole:
`docs/roadmap/110-estate-duplication-exception-audit-mike/010-make-a-voided-allowance-visible.md`
and `docs/roadmap/320-child-filed-findings-via-pointing-up/440-a-review-file-and-its-board-item-drift-apart.md`.
Both carry the author's landing account and probe figures under the proposal, and reading is
atomic, so neither can be read in part. What you need from them is quoted in *The acceptance test*
above. The `110` section README is not barred.

The delta's own text carries the author's account of why (the docstrings, the `CHECK 3` block, the
README and changelog entries); it is the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1310-rule-4-cold-pass-queued-voided-marker-note-review-header.md \
  --also-exclude docs/roadmap/110-estate-duplication-exception-audit-mike/010-make-a-voided-allowance-visible.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/440-a-review-file-and-its-board-item-drift-apart.md \
  --also-exclude docs/reviews/2026-11-14-0225-voided-marker-note-review-header-cold.deferred.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, the
assumptions A1–A7 and your own, and the re-run list. Append your verdict below a `---` divider in
THIS file: provenance repeated (how you were spawned, your tier, what you read, the UTC day you ran
on), per-lens answers, the standing checklist V1–V7 each answered or discharged with grounds, each
load-bearing assumption damaged or confirmed with its probe, a per-commit ledger (`55c7d409`,
`aca05c14`, `1c6fb376`, `b2da72ea`: read body-free yes/no, findings by id), findings with stable IDs
(prefix `VH`: `VH1`, `VH2`, …) and severities (MAJOR / MODERATE / minor / note), an overall
PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then
STOP: act 1 is committed, unrevised, **before** the sibling is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never revise
act-1 text. Then fold the sibling in below the reconcile and delete it.

**Who applies a finding.** Both halves are self-authored guard code every child's floor runs, and
the skill, template and `REVIEW.md` step 5 are doctrine text, so this is doctrine by function
(rule 3): **the author applies nothing on its own**. Record all findings; they are the principal's
to decide, after a plain-language account. Counsel per finding is welcome, labelled as counsel and
kept beneath it, and a finding that bears on whether the header check should ever block says so in
its first line.
