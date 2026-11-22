# Cold pass — a voided allow-marker is noted, and a review file's header lines warn

**Board:** `docs/roadmap/160-doctrine-review-owed/1310-rule-4-cold-pass-queued-voided-marker-note-review-header.md`
**Status:** VERDICT COMPLETE 2026-11-22 UTC, both acts, by a Fable 5.1 cold reviewer (drain
session `eca14b23`, per-pass orchestrator `1cdcd5c7`): PASS-WITH-FINDINGS, 0 MAJOR, 3 MODERATE,
2 minor, 1 note; the reconcile changed no severity. Findings await the principal's decision
(rule 3). Brief written 2026-11-14 UTC by a headless Opus 5.5 brief-writer (`cclive` lists it as
session `64377cac`).

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
`docs/reviews/2026-11-14-0225-voided-marker-note-review-header-cold.deferred.md` (now folded below), the
delta commits' message bodies, and the two intent records whole:
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

---

## Verdict — act 1, Fable 5.1 cold pass, 2026-11-22 UTC

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE (VH1, VH2, VH3) · 2 minor (VH4, VH5) ·
1 note (VH6).** Both halves do what they claim on every shape driven: no working marker is noted,
no result or exit status moves on either plane, and a new review file without the two lines draws
the stanza. The findings are about what the design leaves out: the note can echo a secret that is
glued to the marker, it names no file or line and reaches no machine reader, and the header check's
boundary is a filename a writer chooses. None reverses the work; the third bears on whether check 3
may ever block.

### Provenance (rule 4, V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), tier checked at selection, run as a subagent on
  2026-11-22 UTC (22:48–23:1x). Worktree, read-only to me except this file:
  `/Users/mike/worktrees/fable/atelier-160-1310-2246/atelier`, HEAD `3e581375`.
- **Spawn chain, disclosed:** a headless per-pass orchestrator, session `1cdcd5c7` (Opus 5.5),
  started by drain session `eca14b23` (Opus 5.5) under the principal's weekly drain order of
  2026-11-23 NZDT (verbatim in my spawn prompt: *"Start a fable drain or whatever it is called now.
  Target 100% of weekly budget by 11.30am NZT todat"*). Both are off-tier orchestrators: they hold
  the context partition, form no finding and write no severity. Neither wrote the brief nor any of
  the delta. I was not started or instructed by sessions `64377cac`, `58027096` or `d0ca5d24`.
- **Spawn prompt, as received (process only):** who I am and where; read the brief and `REVIEW.md`;
  the brief's run rules; keep a running work log outside the repo (the drain's reviewer log for this
  pass, `atelier-160-1310-2246.md`); write only that log and this file; act 1 below a divider and
  act 2 as `### Reconcile` only; no git writes, no GUI, `nice`, one suite at a time, `uptime`
  first; read-only on live systems; public-repo wording rules; finish with "ACT 1 SAVED" and wait.
  It said the `.deferred.md` sibling had been removed from the worktree on purpose and barred me
  from recovering it (history, other checkouts, scratch, held-files directories). It carried no
  question about the delta, no pointer to where risk lives and no request about any finding.
- **Barred set honoured:** the sibling, the retired one-file done and session indexes,
  `docs/sessions/`, every prior verdict under `docs/reviews/`, the queue pointer `160/1310`, the
  intent records `110/010` and `320/440`, and every commit message body. The landing commit and
  the fourteen later commits on the subject files were read with `coldsweep --commit`, scoped to
  the subject paths; the board-store files it left out were left out. Sweeps ran through
  `coldsweep` (barred paths excluded, no `--include-barred`). I skipped the onramp's session-log
  step. The `110` section README (not barred) was read whole. **Start-up exposure, disclosed:**
  the worktree's `git status` showed the sibling as a deleted path (its name only) and `git log
  --oneline -5` showed five commit subjects, three of them claim commits of this drain; none reads
  as an account of the delta.
- **Release message:** not yet received; it will be quoted in the reconcile.

### Method and what I read, in order

1. `uptime` (load 25.6 at start, 6.8–23 during; every heavy run alone, under `nice -n 10`),
   `date -u`, `git status --short`, `git log --oneline -1`.
2. The brief whole; `docs/method/REVIEW.md` whole (835 lines); the `110` section README.
3. `git merge-base --is-ancestor 55c7d409 HEAD` (present). `git log --oneline 55c7d409..HEAD --
   <subject files>`: fourteen commits, not the three the brief listed on 2026-11-14 (ledger below).
4. `coldsweep --commit 55c7d409 --path` the four code files (600 lines), then the five prose files
   (116 lines); `coldsweep --commit` for each later commit, scoped to the subject files.
5. `tools/allowmarker.py` whole at HEAD (751 lines); `tools/reviewscan.py` 160–290, 388–508,
   554–662, 725–787; `grep -n "allowmarker\.\(present\|scope_of\|scopes_of\)" tools/*.py` (20
   call sites, 17 scanners) and every `ALLOW_RX`-style definition (all 18 built by `marker_rx`).
6. `tools/floor.py` 700–740, 2850–2925, 3390–3400, 3711; `tools/floorhook.py` 60–140;
   `tools/pre-commit.sample`; `.github/workflows/floor.yml`; `tools/report.py` 270–335;
   `tools/secretscan.py` 1100–1120; `tools/leakscan.py` 995–1012; `tools/conflictscan.py`
   430–440 and 590–600; `.atelier-floor.json` wrapscan block; `.wrapscanignore`.
7. Mirror sites: `skills/review-brief/SKILL.md` 122–124, the reviews template README 89–93,
   `tools/README.md` 1466–1472 and 2401–2406, `REVIEW.md` 503–504 and 809–810, the CHANGELOG
   entry.
8. The unit tests, the probe script (A1–A3, A5, A6, in process), two tool archives (`git archive`
   of `0be93efc` and `55c7d409` into scratch) for old-against-new on both planes, a scratch
   fixture repo for the staged plane, and the brief's re-run list. Fixtures lived in my scratch
   directory only; the worktree's `tools/` was not touched.

Left out, with grounds: the parser fix `8276a54`, the grace itself (`160/480`) and the other twelve
scanners `aca05c14` changed (the brief's non-goals, which fence off nothing this delta carries);
child-repo probes (the estate-wide figures sit in the sibling; a read-only re-run on this repo was
made, and the finding they would inform, VH5, is already grounded here); `/security-review` (lens 4
says why).

### Per-lens answers

**1. Approach and assumptions.** *Is a stderr note, once per head per run, the right answer to "a
voided marker reads like no marker"?* It is the cheapest answer that closes the silence, and it
closes it: driven on the motivating class (a quoted reason under the old `[\w]` grammar, on a
scratch copy), the note fires. But the shape chosen gives up the two things the item asked for.
The item said *"beside the finding, which is where the reader already is"*; the note is on
stderr, carries no file or line, and dedupes by head, so nine voided markers in one repo print one
line that says the word and nothing else (VH2). The stated reason, that the shared readers are not
told where they are, is true of the readers but not of their callers: every scanner calls
`parse_allow(line)` with the line number in hand. *Is warn-only the honest first stage for a check
whose filed form said "reds"?* Yes, as built: the narrowing is stated in the docstring, the
README and the changelog, and the stanza says "warn only, not blocking" on every print. What is not
stated anywhere a reader meets is what would let it block, and VH3 says the present boundary
cannot. *Is a filename date the right boundary for "new files"?* No: it is a date the writer
chooses, and the one escape the brief names (a backdated or non-conforming name) is open on both
planes with nothing behind it (VH3).

**2. Correctness and quality.** Every claim in *What the delta claims* held when driven, with two
qualifications. The note: fires on the no-reason, broken-scope-after-grace and prose-mention
shapes; stays quiet on nineteen working shapes (A1); prints once per distinct head; moves no
result and no exit status on either plane (A4); shows the head and never the line, *except* when a
secret is glued to the marker, where the head is the secret (VH1). The header check: finds the
template's forms and the tolerated typographies; warns on the bare file and not on the complete or
frozen one; same exit either way on disk and staged (fixture); JSON carries
`review_header_warnings`. Its tolerances are uneven in ways the template does not warn about (VH4).
The tests are honest about what they pin; the gaps they leave are exactly the three findings'
shapes (a glued secret, a non-conforming name, a plain-typography wrap).

**3. Completeness and harvest.** What `110/010` asked for and did not get is the location. That gap
is stated in `tools/README.md` and the CHANGELOG, not in the note itself, so a reader of the scanner
output meets the word and no way to act on it (VH2). The readers already export `unparseable_seen()`
for exactly this and nothing calls it. The skill, template, `REVIEW.md` step 5 and micro list,
`tools/README.md` and the CHANGELOG agree with the code and each other on the two lines (V3, V5);
they are six restatements with no canonical home or stamp (V4, VH6). Nothing in the floor was
duplicated or ignored: check 3 reuses `RECORD_NAME`, `_iter_file_lines` and the staged-blob reader.

**4. Security and privacy.** The one new surface is the note: up to forty glued characters of a
scanned line printed to stderr in every child's hook output and CI log. Driven (A3): a GitHub
PAT-shaped token glued to `secretscan:allow:` prints 39 of its 40 characters; an AWS key id prints
whole; a URL with user-info glued to `leakscan:allow:` prints the password once the grace ends.
Realistic path: a writer who means "allow this token" and writes the token as the scope, with no
reason. The exposure is bounded by two facts, which is why VH1 is MODERATE and not MAJOR: the
secret is already on a line the tree holds, and on the hook plane the same marker fails to parse,
so the finding blocks the commit and the note stays on the writer's terminal; in CI the line is
already committed. The `?` substitution is enough against control and escape characters (driven);
a workflow-command injection through the head is not possible because the note never starts a
line with the head. `_warn_malformed`'s unsanitised `shown` is pre-existing (`160/480`), noted,
not a finding here. `reviewscan` reads only `docs/reviews/*.md` and `docs/decisions/*.md` through
bounded windows; the header regexes are anchored and bounded (`{0,40}`, 60 windows), with no
catastrophic-backtracking shape. **`/security-review`: NOT RUN, with grounds.** It reads the
session's pending diff, and this worktree's only pending change is the deletion of the barred
`.deferred.md` sibling, so running it would have fed that file's content back to me before act 1
was written (the SL2 class REVIEW.md names). A manual code-altitude pass over the two Python files
covered injection, log injection, secret handling, unsafe input paths and resource bounds, as above.

### The standing checklist

- **V1 — No claim stronger than its evidence.** One over-claim: the docstring's and README's
  *"shows the head and never the line, so a line that holds a secret is not echoed"* is false for
  a secret glued to the marker (VH1). The warn-only and no-result-moves claims are exactly as
  strong as their evidence.
- **V2 — Re-run every recorded proof.** Re-run ledger below; all four reproduce in substance; the
  counts have moved (134 → 154 tests; the stderr note count on this tree is now 2 for leakscan, 2
  for secretscan and 2 for conflictscan, which the brief did not list).
- **V3 — A changed rule swept to every mirror.** Skill item 6, template, `REVIEW.md` step 5 and
  micro list, `tools/README.md`, CHANGELOG: all carry the two lines. atelier's own reviews
  directory has no README to carry it. Discharged.
- **V4 — One fact, one home.** The two-line grammar is restated in six places with no canonical
  home named and no stamp; the stanza's `<state>, <ISO date>` and the template's `<state, with its
  ISO date>` differ in wording and agree in substance (VH6, note).
- **V5 — No internal contradiction.** Cross-references checked for the rule reached: `REVIEW.md`
  809–810 → the skill's item 6 (present, says what it says); the stanza → `tools/README.md`
  *Allow markers and ignore files* (present, 2401–2406 carries the note's rule); the item's
  "reds" → built "warn only", stated. No contradiction found.
- **V6 — Security and privacy.** Lens 4 above; VH1.
- **V7 — Provenance stated.** The brief states it; this verdict repeats it above.

### Load-bearing assumptions, each attacked

- **A1 — The note never fires on a working marker.** CONFIRMED. Nineteen shapes driven through
  `present`, `scope_of` and `scopes_of`: scoped and unscoped forms of the leakscan (list),
  secretscan (one), wrapscan (unscoped) and blockscan (any-space, unnamed reason) patterns; an
  unscoped pattern meeting a scoped marker of its own word; one broken and one good marker on a
  line in both orders (after the grace); a block whose marker, or whose reason, sits on a later
  line; a well-formed marker inside an HTML comment; a good leakscan marker asked about by the
  secretscan pattern; the prefix word `scan:allow` against `leakscan:allow: why` and the reverse;
  `leakscan:allowed`; `if "leakscan:allow" in line:`. All quiet, all with the right result. The
  stated limit reproduced: `write leakscan:allow on the line` is noted. One pre-existing shape,
  out of scope (`160/480`): `m:allow:ipv4 m:allow:email: ok` reads as malformed during the grace,
  warns and exempts the whole line; after it, `{email}`.
- **A2 — The note fires on the shape it exists for.** CONFIRMED, with a qualification. On a
  scratch copy of `allowmarker.py` with `REASON_START` set to the pre-`8276a54` `[\w]`, loaded by
  file path, two quoted-reason leakscan markers each returned `None` and the readers printed one
  note, head `leakscan:allow:`. Once, as designed; but a head is not something a reader can act
  on without a grep: no file, no line, no count (VH2).
- **A3 — The note can carry no secret or private datum.** DAMAGED. The secretscan word, a colon
  and a fabricated 40-character PAT shape (`ghp_` plus 36) with no reason prints the word, the
  colon and 39 characters of the token; the same with the vendor's documented 20-character example
  access-key id prints the id whole; the leakscan word, a colon and a URL whose user-info carries
  a password prints the password once the grace ends (during it, the malformed warning stops at
  the second colon, after the scheme). An escape sequence and a `::error::` in a head come out as
  `?[31m…` on a line that does not start with the head (VH1). The fixture lines are in the
  reviewer log, not here, so this record stays inert to the scanners it describes.
- **A4 — No result and no exit status moves.** CONFIRMED on both planes. CI plane: the whole floor
  (`floor.py --plane ci`) with the tools at `0be93efc` and at `55c7d409` over this tree, one after
  the other: exit 1 both (pre-existing on this tree with those tools: leakscan 4, board stale,
  pathscan 3; none from the delta), stdout byte-identical, stderr +6 lines, all notes. Hook plane:
  a scratch fixture repo with four staged review files and a staged `notes.py` carrying a bare
  `secretscan:allow:`, a `leakscan:allow:ipv4` and a good conflictscan marker, run from inside
  it: exit 0 both, stdout differs only by the four-line `⚠` stanza, stderr +1 note
  (`secretscan:allow:`). With HEAD's tools the same fixture adds the note `leakscan:allow:ipv4`
  (the no-reason shape `2b8bcd92` made a note later); nothing else moves.
- **A5 — The header boundary cannot be escaped by a backdated file.** DAMAGED. `_header_in_scope`
  returns False for `2026-11-09-2359-x.md`, `cold-pass.md`, `20261110-x.md` and `x-2026-11-10.md`
  while `staged_kind` and `find_briefs` call each a brief and run check 2 on it; in the fixture
  the backdated and the undated file drew no stanza on either plane. No backstop: `grep` of
  `tools/` finds no scanner that enforces `docs/reviews/` names (pathscan only treats the
  directory as a records store), and the template's naming rule is prose (VH3).
- **A6 — The reader finds what the template tells writers to write, and only that.** PARTLY
  DAMAGED. Finds: the canonical form and the tolerated typographies, `none` with a hyphen, an en
  or em dash or a colon. Does not find: a `**Board:**` whose value wraps to the next line (a
  false warning; the line is 115 columns in this very brief, and `docs/reviews/` is
  wrapscan-ignored, so nothing forces the wrap, but nothing says "same line" either). Finds what
  it should not: a `Status:` wrapped onto a plain `Tier: … 2026-11-10` or a bullet (the
  `_NEXT_FIELD` end-marker is bold-only while
  the field regexes accept plain); a `Board:` inside a fenced block in the header (check 1 tracks
  fences, check 3 does not); a `Board:` naming any `.md` (`\S\.md\b`); the date `2026-13-45`.
  Fields past line 60 or under an H2 title warn, as designed (VH4).
- **A7 — Warn-only is visible where it is needed.** CONFIRMED on the hook, QUALIFIED in CI. The
  floor runs each scanner with stdout to its own stdout and stderr inherited, so on the hook both
  the stanza and the note reach the terminal (fixture, above). In CI the same two land inside the
  scanner's `::group::`, collapsed by default on a green step, and the floor emits `::error::` only
  on a non-zero exit; nothing raises a `::warning::` for a stanza or a note, so a green run shows
  neither until a reader opens the group (VH5).

### Per-commit ledger

Every commit below was read body-free with `coldsweep --commit`, scoped to the subject files.

- `55c7d409` — the landing (code read first, then prose). Findings: VH1–VH6.
- `aca05c14` — scoped to `reviewscan.py` and its tests: the coverage line in `_render`, two tests.
  None.
- `1c6fb376` — attribscan pattern pin. None.
- `b2da72ea` — namescan and quotescan pattern pins. None.
- `a78ee8b0` — `Deferment` dataclass → NamedTuple so a child can load the module by file path;
  a test. None: the note's module-level state is per loaded module, which is right for that shape.
- `2b8bcd92` — a scope with no reason exempts nothing and is now noted (`115/230` item 1; its own
  pointer `160/1550`). None here; it widens the note's reach, so VH1 and VH2 apply to its shape.
- `734930ef` — one comment word. None.
- `2522f4fe` — review-by deferments in ignore files; no note or header change. None.
- `a879c93a`, `aa7746e8`, `aa3409b0`, `bc383fb1`, `9e0ac28f`, `2f3aed4b`, `b68cf410` — scoped to
  the three doctrine files and grepped for the header-line text: only `2f3aed4b` touches this
  subject (`REVIEW.md` 809–810, consistent with the delta). None.

### Findings

Each is the principal's to decide (rule 3: self-authored guard code every child's floor runs, and
doctrine text). Counsel is labelled and kept beneath.

**VH1 — MODERATE — The note echoes a secret that is glued to the marker.** `_note_unparseable`'s
head is `\b<word>(?![^\s:])[^\s<>`]{0,40}`: it runs across colons and stops only at whitespace, `<`,
`>` or a backtick, so a token written as the scope with no reason (`secretscan:allow:ghp_…`,
`secretscan:allow:AKIA…`) or a URL with user-info glued to the word is printed, up to forty
characters, to stderr in the hook output and the CI log. The docstring, `tools/README.md` and the
CHANGELOG say the opposite (*"never the line, so a line that holds a secret is not echoed"*). The
malformed warning the note sits beside already cuts at the second colon. Evidence: A3. Not MAJOR
because the secret is already in the tree on that line and, on the hook, the same marker fails to
parse and blocks the commit. *Counsel:* cut the head at the second colon as `_malformed_rx` does,
or show the word plus a bounded, scope-shaped run only (`[A-Za-z0-9_,-]{0,24}`) and elide the
rest with a count; add a glued-token test beside `test_the_note_shows_the_head_and_never_the_line`,
which today covers only a space-separated secret.

**VH2 — MODERATE — The note names no file, no line and no count, and reaches no machine
reader.** One line per distinct head per process, on stderr: for the incident that motivated the
item (nine voided markers of one shape across three repos) each repo's run prints
`leakscan:allow:` once and nothing else. The item asked for the note *beside the finding*; the
stated reason for not doing so (the shared readers are not told where they are) does not reach
the callers, which hold the line
number when they call `parse_allow(line)`. `unparseable_seen()` exists for a scanner to report the
heads and no scanner calls it, so `--json`, the floor's summary and anything built on them see
nothing: the machine half of "the house believes it is caught" is unchanged. Evidence: A2; `grep
unparseable_seen tools/*.py` finds only `allowmarker.py` and its tests; the CI stderr of this tree
carries six notes that cannot be placed without a grep (VH5). *Counsel:* the least change that
closes it is one line per scanner: print `unparseable_seen()`'s count in the existing
`suppressed:` slot beside `marker(s) naming no rule`, and the heads in `--json`; the fuller change
is an optional `where=` on the readers that scanners pass as `path:lineno`, printed in the note.

**VH3 — MODERATE — bears on blocking: the boundary keys on a filename the writer chooses, and
nothing in the floor stands behind it.** A review file named for a day before 2026-11-10, or with
no date at all, is still a brief for check 2 and is exempt from check 3 on both planes; no scanner
enforces the `docs/reviews/<date>-<HHMM>-<slug>.md` name the template prescribes. While the check
warns, the cost is the false belief the brief names: a clean run reads as "every new file carries
the lines". If check 3 ever blocks on this boundary, the escape becomes a bypass. Evidence: A5 and
the fixture on both planes. *Counsel:* on the hook plane, read the staged status (`git diff
--cached --name-status`; `report.staged_paths` keeps only the names today) and treat an added file
as new whatever its name; on both planes, warn on a `docs/reviews/*.md` whose name does not match
`RECORD_NAME` (the name is the template's rule, so a non-conforming one is itself the defect); keep
the filename date only as the frozen-records exemption it was meant to be.

**VH4 — minor — The header reader's tolerances are uneven, in ways the template does not warn
about.** (a) A `**Board:**` whose value wraps onto the next line draws a false `board` warning;
item paths run past 100 columns and the template does not say "same line". (b) A wrapped
`Status:` is ended only by a bold `**Field:**`; a plain `Tier: … <date>` or a bullet beneath it is
read as the status date, while the field regexes themselves accept plain typography. (c) A
`Board:` inside a fenced block in the header counts, where check 1 skips fenced `review:` lines
(RS2). (d) `_BOARD_PATH` accepts any `.md`, and `_ISO_DATE` accepts `2026-13-45`. Evidence: A6.
*Counsel:* let `_NEXT_FIELD` accept the plain form the field regex accepts; either read a bare
`**Board:**` line's value from the next non-blank line or say "one line" in the skill and template;
track fences as `scan_record` does; the `.md` and date checks are fine to leave tolerant if the
tolerance is stated.

**VH5 — minor — In CI the warn-only output is collapsed, and the house's own tree prints six
false notes per run.** The stanza and the note land inside the scanner's `::group::`, which Actions
collapses on a green step; the floor annotates `::error::` on failure only. On this tree the CI
plane prints six notes (`conflictscan` ×2, `leakscan` ×2, `secretscan` ×2), all from `tools/`'s
own test fixtures and two files that quote the regex `leakscan:allow:([a-z0-9,-]+):` as source
(`tools/pdlistscan.py:81`, `tools/test_personal_data.py:43`); none is a voided marker and none can
be placed from the note. Children have no `tools/`, so the noise is atelier's own, but it is the
"trains every session to ignore the line" harm the brief names, on the repo whose sessions write
the doctrine. Evidence: A4, A7, the `coldsweep` location of all six. *Counsel:* a `::warning::`
annotation from the floor when a scanner's stdout carries `⚠` or its stderr `allowmarker: note:`;
VH2's locator makes the six placeable, after which the fixture lines can carry the syntax in a
form the word-end rule excludes, or the rule can treat `:(` and `:[` as source, not an attempt.

**VH6 — note — The two-line grammar lives in six places with no canonical home.** Skill item 6,
the template, `REVIEW.md` step 5, `REVIEW.md`'s micro list, `tools/README.md` and the CHANGELOG
each restate `**Board:** <item file>` (or `none — <grounds>`) and `**Status:** <state, ISO date>`;
the stanza prints a seventh wording. They agree today. *Counsel:* name one home (the skill's item 6,
which the micro list already points at) and stamp or point from the rest, per `PROPAGATION.md`
§ *One statement, stamped copies*.

### Re-run ledger

Recorded by the brief-writer on 2026-11-14 at `d3293d93` with Python 3.14.6; re-run by me on
2026-11-22 at `3e581375` with the Python 3.14.6 on PATH, each alone under `nice -n 10`.

- `python3 -m unittest test_allowmarker test_reviewscan` → recorded 134 OK; mine (`PYTHONPATH=
  tools`, no `cd`) **154 OK** in 21.7 s.
- `reviewscan --root . .` → recorded exit 0, no `⚠`; mine exit 0, no `⚠`, 254 briefs, 262
  checks, 0 stderr lines.
- `leakscan --root . .` → recorded 0, 2 notes; mine exit 0, **2** notes.
- `secretscan --root . .` → recorded 0, 2 notes; mine exit 0, **2** notes.
- `conflictscan --root . .` (not on the brief's list; the CI run showed it) → exit 0, 2 notes.
- Estate-wide old-against-new, 30 repos (figures in the sibling) → this repo only, both planes:
  CI plane stdout identical and exit identical; hook plane on a fixture, stdout differs by the
  stanza only. Child repos not probed: read-only probes would add nothing to VH5's grounding.

All reproduce. Two staleness notes on the brief, not the delta: the later-commit list grew from
three to fourteen (two of them, `a78ee8b0` and `2b8bcd92`, change `allowmarker.py`), and the test
count grew by twenty.

### Follow-up checklist

- [ ] VH1: bound the note's head at the second colon or to a scope-shaped run; glued-token test;
      correct the three "never echoes a secret" statements or make them true.
- [ ] VH2: a count in each scanner's `suppressed:` line and heads in `--json` from
      `unparseable_seen()`; or a `where=` locator through the readers.
- [ ] VH3: a new-file test on the hook plane that does not depend on the name; a name-shape warning
      for `docs/reviews/*.md`; a statement of what blocking would need, where the warn-only
      narrowing is already stated. **Decide before any blocking stage.**
- [ ] VH4: `_NEXT_FIELD` plain form; wrapped `Board:` value or "one line" in the template; fence
      tracking in `header_warnings`.
- [ ] VH5: `::warning::` from the floor for warn-only output; clear or place atelier's six notes.
- [ ] VH6: one home for the two-line grammar, stamped elsewhere.
- [ ] Brief hygiene (not a delta finding): the re-run list and later-commit list of a brief that
      waits more than a week are stale on arrival; the taker re-derives both, as here.

Act 1 ends here. Act 2 follows as `### Reconcile` once the sibling is released.

### Reconcile — act 2, 2026-11-22 UTC

Opened after act 1 was committed (`3dd15f49`, this file only, unrevised), on the orchestrator's
release message, verbatim: *"Act 1 is committed (3dd15f49, brief file only, unrevised). Act 2 may
now begin. You may now read the held sibling, this one file: … plus the records the brief opens at
phase 2 (the barred intent records, queue pointer, the delta commits' message bodies, prior
verdicts as the brief allows). … Do NOT fold the sibling in or delete anything: the orchestrator
does the fold."* Process only; it carried no question about the delta. Read, in this order: the
held sibling (one file, from the orchestrator's holding directory, outside every worktree); the
intent records `110/010` and `320/440` whole; the queue pointer `160/1310`; the message bodies of
`55c7d409`, `aca05c14`, `1c6fb376`, `b2da72ea`, `a78ee8b0` and `2b8bcd92`. The brief names no
prior verdict, so none was opened. Act-1 text above is unchanged.

**What the sibling and the author's account add, in brief.** The author probed leakscan,
secretscan and reviewscan old-against-new across 30 local repositories (exit code and stdout
*length* identical everywhere); after the word-end tightening the note fired in two repos, four
times in this repo's own tooling source and once in one child's secretscan run, every one a
mention. For the header half, with the boundary pushed back for a count only, 736 of 738 review
files across 17 repos lacked a `board:` line and 480 a dated `Status:`, which is why the boundary
is forward-looking. `320/440` is kept open on purpose for blocking, with a probe plan: count the
review files dated on or after the boundary that lack the lines, per child, and read what the
warning has caught; if it catches nothing, close as warn-only. The queue pointer's two questions
(can the note fire on a working marker; can a backdated file escape) were already in the brief as
A1 and A5, so the pointer added no framing I had not met.

**Per finding, against the sibling and the author's account.**

- **VH1 (MODERATE, glued secret) — stands, unchanged.** Neither the sibling nor either landing
  note considers a secret glued to the marker; the commit body repeats the claim ("shows the marker
  head, never the line"). `2b8bcd92`'s body says the note "names" a scope with no reason, which is
  the shape that echoes a token written as the scope; that pass (`160/1550`) should carry VH1
  forward.
- **VH2 (MODERATE, no locator or machine surface) — stands, sharpened by the account.** The author
  states the limit and the reason: printing beside the finding "would mean changing each
  scanner's render path (15 sites), which was not done". The reason is a cost, not a constraint,
  and the author's own probe shows the cost of the omission: the five notes it found could be
  called mentions only because the author went and looked; a child's CI reader cannot. The
  account also measures the mention noise at "a few stderr lines", which on this repo is now six
  per run (VH5) and will rise as fixtures are added. The sibling's question 2 (is stderr passed
  through?) is answered in A7: yes on the hook, inside a collapsed group in CI.
- **VH3 (MODERATE, filename boundary; bears on blocking) — stands, and now bears on the author's
  own probe plan.** `320/440`'s plan for the blocking decision counts "review files dated on or
  after the boundary that lack the lines". That count inherits the blind spot: an undated or
  backdated file is neither counted nor warned, so the probe can read "the warning caught
  nothing" while non-conforming files pass unseen. The sibling's question 5 (a good-faith
  backdated name) is the house's own convention: a file is named for its start time, so a brief
  begun before 2026-11-10 and finished after it is out of scope by design, and nothing catches a
  name that does not match `RECORD_NAME` at all. The close rule "if the warning catches nothing,
  close as warn-only" also conflates two things the fixture separates: a check that catches
  nothing because the template is doing the work (this repo's 254 briefs, all compliant), and a
  check that catches nothing because the miss is out of its scope.
- **VH4 (minor, reader tolerances) — stands; one sub-point sharpened at reconcile.** The sibling's
  question 4 asks whether `Board:` should check that the named item file exists. It is cheap on
  the disk plane (`root / value` exists) and matches the proposal's aim, a pointer a reader can
  follow; on the staged plane the target may be in the same commit, so the index would have to be
  consulted. Added to VH4(d)'s counsel as an option, formed at reconcile, severity unchanged.
- **VH5 (minor, CI visibility and six false notes) — stands.** The author's probe found four
  mention notes in this repo on 2026-11-09 (two scanners); the floor now prints six (conflictscan
  joined), all from `tools/`'s own fixtures and regex sources. The account calls this the
  `160/480` AM3 residual; it is, and it is also the noise the brief warned about, on the repo whose
  sessions write the doctrine.
- **VH6 (note, six homes) — stands.** Not addressed by the sibling or the account.

**The sibling's questions, answered.** (1) No scanner reads one line with two patterns for one
word: all eighteen definitions are one pattern per scanner, and the two scanners with two call
sites (`namescan`, `stampscan`) use one pattern each. The sibling's premise is also wrong on one
point: a `conflictscan:allow:<kind>: <reason>` line read by the unscoped conflictscan pattern is
*accepted*, not noted, because the reason may start with any word character and so begins at
`<kind>` (A1, "unscoped pattern meets scoped marker of own word"). (2) Answered above and in A7.
(3) Both: the check is proven on real misses in fixtures (the bare staged file drew the stanza on
both planes); in this repo the template is doing the work, which is the check working, and the
close rule in `320/440` should not read it as the check being useless. (4) Folded into VH4.
(5) Folded into VH3.

**Corrections to act 1 formed at reconcile:** none to its findings or severities. One count: the
author's "15 reader call sites" is 20 at HEAD across 17 scanners (attribscan, namescan and
quotescan joined the shared readers after the landing); immaterial to any finding.

**Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE (VH1, VH2, VH3) · 2 minor (VH4,
VH5) · 1 note (VH6).** The findings are the principal's to decide (rule 3); the author applies
nothing on its own. The sibling is folded in below by the orchestrator, not by me.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-22)

*Released to the reviewer only after its act-1 findings were committed (locally `3dd15f49`, the hash
the reviewer's text cites; it lands rebased with this fold); folded here verbatim (headings demoted
two levels, 0 line(s) over 100 columns wrapped at word boundaries, no word changed) and the sibling
file removed, per the brief. The orchestrator, headless Opus 5.5 session `1cdcd5c7` started by drain
session `eca14b23`, held the partition, formed no finding and wrote no severity; drain session
`eca14b23` wrote no brief and no delta and started no brief-writer for this pass.*

### Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-14-0225-voided-marker-note-review-header-cold.md` (`REVIEW.md`
rule 1). Written 2026-11-14 UTC by the brief-writer (`cclive` lists it as session `64377cac`),
which authored none of the delta. Open this only after act 1 is committed. Everything here is a
floor, never a fence, and none of it is a finding: the brief-writer read the code once and probed
none of these past what the brief's re-run list records.

#### What the barred intent records say, in brief

- `110/010` carries the author's landing note (2026-11-09, queue run `d0ca5d24`): the note covers
  15 reader call sites with no scanner file changed; an old-against-new probe of `leakscan` and
  `secretscan` in each of 30 local repositories, one at a time under `nice`, found exit code and
  stdout length identical everywhere. After a tightening (the word must end at a colon, a space or
  the line's end) the note fired in 2 repos: twice per scanner in atelier's own tooling source and
  once in one child's `secretscan` run, every one a mention, none a genuinely voided marker. Its
  conclusion: the estate held no voided marker of that shape on that date. It states the same
  limits the brief extracts (stderr, not the finding line; fires on any line a reader is asked
  about; a prose mention outside a code span is noted, the residual `160/480` AM3 names).
- `320/440` carries the author's landing note: proposal items 1 and 2 built warn-only, 3 and 4 not
  built by design; the same 30-repo probe found exit code and stdout length identical (no review
  file was dated on or after the boundary then). With the boundary pushed back for a count only,
  736 of 738 review files across 17 repos had no `board:` line and 480 had no dated `Status:` line.
  The item stays open on purpose for blocking, which "needs its own date and a fleet probe at that
  date"; if the warning is not read or catches nothing by then, it closes as warn-only.
- Earlier on `320/440`, the child's own measurement of the drift ("one in five") was corrected by
  the filer the same day to **unmeasured**; the class survived the correction.

#### The brief-writer's own questions

1. **A scoped marker read by an unscoped pattern.** `conflictscan` and `wrapscan` build their
   pattern with no scope. A line carrying `conflictscan:allow:<kind>: <reason>` allows nothing
   there and is noted, correctly. But is there any scanner that reads the same line with two
   patterns for one word (scoped and unscoped), so that the one that does not match notes a line
   the other honoured?
2. **The note in CI.** The note goes to stderr. Does `tools/floor.py` (and the pre-commit hook)
   pass a scanner's stderr through, or keep only its exit code and stdout? If stderr is dropped,
   the note is invisible exactly where `110/010` said the reader already is.
3. **Today's briefs are the first in scope.** Every brief named for 2026-11-10 or later is under
   check 3. On 2026-11-14 at `d3293d93` the scanner printed no `⚠` stanza over this repo, so every
   such brief carried both lines. Is that the check working, or the template doing the work and
   the check untested on real misses?
4. **Any `.md` passes `Board:`.** `_BOARD_PATH` is `\S\.md\b`, so `**Board:** see README.md`
   passes, as does a path to an item file that does not exist. The docstring says "naming its item
   file". Is existence worth checking, given the proposal's aim is a pointer a reader can follow?
5. **The boundary is a filename.** A brief-writer or reviewer that names a file for the day the
   work was done rather than the day it was written produces a backdated name in good faith. How
   common is that shape in the house's own naming rule (HHMM from `date -u`), and does anything
   catch it?

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*Form fixes only: headings demoted two levels; 1 line(s) over 100 columns wrapped at word
boundaries, no word changed. No public-repo gate blocked a token, so no placeholder was needed.*

### Review log — atelier 160/1310 (voided-marker note + review-header check), Fable 5.1 cold pass

Reviewer: Fable 5.1, spawned by per-pass orchestrator 1cdcd5c7 (Opus 5.5), itself from drain
session eca14b23 (Opus 5.5). Worktree:
/Users/mike/worktrees/fable/atelier-160-1310-2246/atelier (read-only except the brief).
Brief: docs/reviews/2026-11-14-0225-voided-marker-note-review-header-cold.md
Started 2026-11-22T22:48Z. uptime load 25.65 (many passes running); one heavy process at a time.

#### Method (planned)
1. Read brief in full; REVIEW.md (verdict shape); 110 section README (not barred).
2. Confirm delta present (merge-base 55c7d409). List later commits on subject files.
3. Read landing commit body-free via coldsweep, code first then prose. Read later commits on the
   subject files body-free.
4. Read tools/allowmarker.py and tools/reviewscan.py at HEAD whole; reader call sites in scanners.
5. Lenses: approach, correctness, completeness/harvest, security/privacy.
6. Probes A1–A7 in scratch; re-run the recorded proofs.
7. Write act 1 under --- in the brief; run datescan/wrapscan on the brief.
Barred and NOT opened: .deferred.md sibling (anywhere), docs/ROADMAP-DONE.md, docs/SESSIONS.md,
docs/sessions/, prior verdicts in docs/reviews/, queue pointer 160/1310, items 110/010 and 320/440,
commit message bodies.

#### Steps
- 22:48Z `uptime` -> load 25.65; `date -u` -> Sun Nov 22 22:48 UTC 2026. git status: only the
  expected deletion of the .deferred.md sibling. HEAD 3e581375.
- Read brief whole (307 lines).
- `git merge-base --is-ancestor 55c7d409 HEAD` -> present (nothing printed).
- `git log --oneline 55c7d409..HEAD -- <subject files>` -> 14 commits (brief listed 3 as of
  2026-11-14): b68cf410 734930ef a78ee8b0 2f3aed4b 2522f4fe 2b8bcd92 9e0ac28f bc383fb1 aa3409b0
  aa7746e8 a879c93a b2da72ea 1c6fb376 aca05c14. a78ee8b0 and 2b8bcd92 touch allowmarker.py.
- grep reader call sites: 20 call sites across 17 scanner files (attribscan, blockscan, datescan,
  conflictscan, licenscan, linkscan, pointerscan, leakscan, quotescan, reviewscan, pathscan,
  namescan x2, spellscan, sizescan, stampscan x2, secretscan, wrapscan).
- /usr/bin/python3 is 3.9.6 (brief-writer used 3.14.6); will check `python3` on PATH too.
- Read docs/method/REVIEW.md whole (835 lines) for the verdict shape and rules 1-4, V1-V7.
- Read docs/roadmap/110-.../README.md (not barred): the incident class (9 markers, 3 children,
  REASON_START `\w` gap, fixed 8276a54).
- coldsweep --commit 55c7d409 (code paths) -> scratch delta-code.diff, 600 lines; read whole.
  coldsweep --commit 55c7d409 (prose paths) -> delta-prose.diff, 116 lines; read whole. Board-store
  files left out by default (3), as the brief requires. No message body printed.
- coldsweep --commit for the 14 later commits, scoped to the subject files -> scratch later-*.diff.
- Read tools/allowmarker.py at HEAD whole (751 lines); tools/reviewscan.py 160-290, 388-508,
  554-662; grep of def/returns.
- Read tools/floor.py 2850-2925 (scanner subprocess: stdout -> child_stdout, stderr inherited;
  CI wraps each scanner in ::group::), tools/floorhook.py 60-140 (Claude Code pin hook; captures
  both streams but is not the scanner runner), tools/pre-commit.sample (runs floor.py --plane
  hook), .github/workflows/floor.yml (runs floor.py --plane ci, python 3.12).
- grep ALLOW_RX definitions: all 18 scanner patterns are built by allowmarker.marker_rx, so
  _MARKER_OF covers every reader pattern (claim "one change covers the class" holds on this
  axis).

#### Candidate findings (to probe)
- C1 (A3): the note's head regex `[^\s<>`]{0,40}` runs across colons; a token glued to the
  marker (`secretscan:allow:ghp_...` with no reason) would be echoed, up to 40 chars, to stderr
  in CI. _warn_malformed stops at the second colon; the note does not. PROBE.
- C2 (A5): _header_in_scope keys on RECORD_NAME; a review file whose name carries no date (or an
  earlier date) is a "brief" for find_briefs/scan_brief yet exempt from check 3 on both planes.
  Is anything a backstop? PROBE + grep.
- C3 (A6): _NEXT_FIELD requires bold `**Field**`; a plain `Tier: ... 2026-11-10` line after a
  wrapped Status: would be read as the status date. Also Board: in a fenced block; H2 title.
  PROBE.
- C4 (A7): in CI the stanza/note land inside a collapsed ::group:: when the scanner exits 0;
  on the hook they reach the terminal. Confirm by reading floor.py registry/planes.
- C5: blockscan `any(present(rx, t) for t in texts)`: a block whose first text has the word but
  no marker and a later text a good marker is allowed AND noted. Edge; note only.
- 22:54Z `uptime` load 23; `PYTHONPATH=tools nice -n 10 python3 -m unittest test_allowmarker
  test_reviewscan` (python3 = 3.14.6 on PATH) -> Ran 154 tests OK (brief recorded 134 on
  2026-11-14; the suite grew). One malformed-marker warning printed by a test fixture, expected.
- Read later commits body-free: aca05c14 (coverage line in reviewscan _render; two tests),
  1c6fb376 + b2da72ea (test pins only), a78ee8b0 (Deferment dataclass -> NamedTuple so a child can
  load allowmarker by file path; test), 2b8bcd92 (115/230 item 1: a scope with no reason exempts
  nothing and is NOTED; _no_reason_rx, is_scope_without_reason; has its own pointer 160/1550),
  734930ef (comment word change), 2522f4fe (review-by deferments; no note/header change). The seven
  doctrine commits (a879c93a aa7746e8 aa3409b0 bc383fb1 9e0ac28f 2f3aed4b b68cf410): grep for
  Board/Status/header shows only 2f3aed4b adds REVIEW.md micro-list line "The Board: and Status:
  header lines (the skill's item 6; reviewscan warns ... never blocks)". Consistent with the delta.
- Read tools/floor.py 700-740 (reviewscan registry: hook plane --staged, ci whole tree,
  advisory=None), 3390-3400 (cannot be softened), 3711 (ci = plane ci AND GITHUB_ACTIONS), 2919
  (::error:: only on rc != 0; grep finds no ::warning::).
- Read report.py 270-335: staged_paths() = `git diff --cached --name-only --diff-filter=ACMR`;
  no status letter kept (so "new file" is not known to reviewscan's staged plane; it keys on name).
- Read skills/review-brief/SKILL.md 122-124 (item 6), template README 89-93, tools/README.md
  1466-1472 and 2401-2406, CHANGELOG entry (in the diff), REVIEW.md step 5 (503-504) and micro
  list (809-810): the two-line grammar is restated in each; they agree. atelier has no
  docs/reviews/README.md (so no mirror there).
- Read secretscan.py 1100-1120 and leakscan.py 995-1012: both ask the reader on EVERY line that
  contains the marker word (`if ALLOW_MARKER in line`), finding or not. conflictscan.py 430-440:
  asks only on a finding line. So for leakscan/secretscan the note is not tied to a finding.
- Probe script scratch/probe_note.py (imports the worktree modules read-only; A2 patches a COPY of
  allowmarker.py in scratch and loads it by file path). Results:
  A1 (19 shapes): every well-formed marker quiet, incl. scoped/unscoped, unscoped pattern on a
    scoped marker of its own word, broken+good in both orders (AFTER grace), block text with the
    marker or the reason on a later line, cross-scanner, HTML comment, prefix word `scan:allow`
    vs `leakscan:allow` both ways, `leakscan:allowed`, quoted source string. CONFIRMED.
    Stated limit reproduced: a prose mention `write leakscan:allow on the line` is NOTED.
    Pre-existing (160/480 grace, non-goal): `m:allow:ipv4 m:allow:email: ok` DURING grace reads
    as malformed, warns and exempts the whole line; AFTER it reads {email}.
  A2: old grammar REASON_START `[\w]` on a scratch copy: two quoted-reason markers (the incident
    class) -> None, None; ONE note, head `leakscan:allow:`; no file, no line, no count. The note
    fires on the shape but is not locatable and dedupe collapses nine incidents into one line.
  A3: `secretscan:allow:ghp_<36>` (fake PAT, no reason) -> note head echoes 39 chars of the
    token; `secretscan:allow:AKIAIOSFODNN7EXAMPLE` -> full id echoed; `leakscan:allow:https:// <!-- secretscan:allow:aws-access-key-id: AWS's published documentation example key, a probe fixture in the reviewer's log --> <!-- leakscan:allow:aws-access-key-id: same documentation example key, a probe fixture -->
    user:S3cr3tPw@host.example/p` AFTER grace -> password echoed (DURING grace the malformed <!-- leakscan:allow:email: synthetic URL user-info on an RFC-2606 example host, a probe fixture in the reviewer's log -->
    warning stops at the second colon: `leakscan:allow:https:`). ANSI/control chars -> `?`.
    The docstring's "never the line, so a line that holds a secret is not echoed" fails for a
    secret glued to the marker. The test suite covers only a space-separated secret.
  A5: _header_in_scope: `2026-11-09-2359-x.md`, `cold-pass.md`, `20261110-x.md`, `x-2026-11-10.md`
    all False while staged_kind says 'brief' for each. grep of tools/ finds no scanner enforcing
    review-file names (pathscan only treats docs/reviews as a records dir).
  A6 (19 shapes): canonical OK; Board naming a review .md accepted; Board value wrapped onto the
    next line -> FALSE 'board' warning; Status wrapped then a BOLD field with a date -> correct
    'status' warning; Status wrapped then a PLAIN `Tier:` or a bullet with a date -> accepted
    (false pass); Board inside a ``` fence in the header -> accepted; H2 title -> both warn;
    fields at line 61 -> both warn; invalid date 2026-13-45 accepted; `none:` and `NONE —`
    accepted; table rows warn.
- `git archive 0be93efc tools` and `git archive 55c7d409 tools` into scratch (read-only git).
  A4 CI plane: `floor.py --plane ci --root <worktree> --tools <scratch tools>` old then new under
  nice: exit 1 both (pre-existing on this tree with 2026-11-09 tools: leakscan 4, board stale,
  pathscan 3 - unrelated to the delta); stdout diff EMPTY; stderr +6 lines, all notes:
  conflictscan x2, leakscan x2, secretscan x2. CONFIRMED: no result or exit moved.
  Located the six by coldsweep (barred excluded): tools/pdlistscan.py:81 and
  tools/test_personal_data.py:43 quote the regex `leakscan:allow:([a-z0-9,-]+):`; the bare and
  colon-only heads come from tools/test_conflictscan.py, tools/test_secretscan.py,
  tools/test_leakscan.py fixtures. All six are false notes on the house's own clean tree.
- Recorded re-run lines at HEAD: reviewscan --root . . exit 0, no stanza, 254 briefs, 0 stderr;
  leakscan exit 0 notes 2; secretscan exit 0 notes 2; (conflictscan exit 0 notes 2).
- Scratch fixture repo (git init, one commit, then staged: docs/reviews/2026-11-10-0900-new-bare.md,
  2026-11-09-2359-old-bare.md, cold-pass-undated.md, 2026-11-10-0901-good.md, notes.py with
  `leakscan:allow:ipv4`, `secretscan:allow:`, a good conflictscan marker). First run from the
  wrong cwd: staged scanners refuse (exit 2) by design; re-run from inside the fixture:
  hook plane old/new exit 0 both; stdout diff = the 4-line ⚠ stanza naming ONLY new-bare (the
  backdated and undated files escape on the hook plane too); stderr new-only: one note
  `secretscan:allow:`. With HEAD tools: notes `secretscan:allow:` and `leakscan:allow:ipv4`
  (the no-reason shape, noted since 2b8bcd92).
- wrapscan: docs/reviews/ is in .wrapscanignore (WS1) and LINE_LIMIT is 85; the brief's 100-column
  rule is the brief's own, kept by hand.
- /security-review NOT RUN: it reads the session's pending diff, and this worktree's only pending
  change is the deletion of the barred .deferred.md sibling, so running it would feed that file's
  content back (REVIEW.md SL2 class). Manual code-altitude pass instead (see verdict, lens 4).

#### Findings formed (act 1)
VH1 MODERATE (A3) glued secret echoed by the note. VH2 MODERATE (A2, approach) note carries no
locator or count, stderr only, no machine surface; unparseable_seen() has no caller. VH3 MODERATE
(A5) boundary keys on the filename; undated/backdated names escape both planes; no backstop; bears
on blocking. VH4 minor (A6) header-reader tolerance gaps. VH5 minor (A7) CI visibility + six false
notes on atelier's own tree. VH6 note (V3/V4) grammar restated in five homes, unstamped.
- 23:10Z act 1 appended to the brief below `---`; Status line updated (ACT 1 WRITTEN 2026-11-22).
- Checks on the brief: datescan clean, spellscan clean, reviewscan exit 0 (1 brief, no stanza).
  secretscan first flagged my A3 prose (the vendor example key id and a URL with a password,
  quoted literally) and leakscan warned on the quoted malformed shape: rewrote A3 to describe the
  shapes without quoting them; both now clean. pathscan: my two path mentions rewritten (a reviews
  README that does not exist; the retired indexes); 4 remaining hits are the brief-writer's own
  lines 248/259/261 (the barred-list paths, two since retired, and the removed sibling), not mine
  to edit; docs/reviews is excluded by default on a tree run, so the floor does not red on them.
  All my lines <= 100 columns (two tables rewritten as lists). wrapscan: docs/reviews ignored.
- Scratch cleaned: fixture repo, the two tool archives and every scanner capture deleted; kept
  probe_note.py and the body-free commit diffs for act 2.
- ACT 1 SAVED at 23:1x UTC. Waiting for the sibling's path.

#### Act 2 (reconcile)
- Release message from orchestrator 1cdcd5c7, verbatim: "Act 1 is committed (3dd15f49, brief file
  only, unrevised). Act 2 may now begin. You may now read the held sibling, this one file:
  "/Users/mike/.claude/fable-held/atelier--2026-11-14-0225-voided-marker-note-review-header-cold.deferred.md",
  plus the records the brief opens at phase 2 (the barred intent records, queue pointer, the delta
  commits' message bodies, prior verdicts as the brief allows). Append `### Reconcile` ... Do NOT
  fold the sibling in or delete anything: the orchestrator does the fold." Process only; no
  question about the delta.
- Read: the held sibling (one file); 110/010 and 320/440 whole; pointer 160/1310; bodies of
  55c7d409 aca05c14 1c6fb376 b2da72ea a78ee8b0 2b8bcd92. No prior verdict named; none opened.
- Reconcile written 23:15Z: all six findings stand, severities unchanged. Sharpened: VH2 (author's
  stated reason is a cost, not a constraint; author's probe itself needed a human to classify the
  mentions), VH3 (320/440's blocking probe plan inherits the filename blind spot; its close rule
  conflates "template did the work" with "miss out of scope"), VH4(d) (+ existence check option,
  formed at reconcile). Sibling Q1 premise corrected (an unscoped pattern ACCEPTS word:kind: reason;
  A1 probe). Count correction: 15 call sites (author) vs 20 at HEAD. Status line -> VERDICT
  COMPLETE 2026-11-22.
- Scratch cleaned entirely (probe script, diffs). ACT 2 SAVED.
