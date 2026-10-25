# Cold pass — the body-free commit read, in coldsweep and the review-brief skill

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** REVIEW RAN 2026-10-25 UTC, both phases — **PASS-WITH-FINDINGS: 1 MAJOR, 4 MODERATE,
5 minor, 5 note** (BF1–BF15; act-1 verdict and act-2 reconcile below the divider; no act-1
severity changed at reconcile). Brief written 2026-10-18 UTC by an Opus brief-writer; reviewed
by a Fable 5.1 subagent spawned by session 52e11d15 (Opus 5.5, orchestrator only — provenance in
the verdict); tier checked at selection. Findings are the principal's to decide (rule 3).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/930-rule-4-cold-pass-queued-body-free-commit-read.md`.
**Why it earns a review:** `coldsweep --commit` is a silent-failure surface: its clean last line
("message body not read") is what a reviewer will cite as proof it never saw the author's
account. If the tool can print part of a body, or leave an author's account in the diff it
prints, the proof is false and every later rule-4 pass that leans on it inherits the leak. The
skill text is doctrine by function: it tells every brief-writer in every repo how to point a
reviewer at a commit, and adds a duty on the brief-writer's re-run lines.

## Spawn provenance

- **Author of the work under review:** one authoring session — a Mike-opened Opus 5.5 queue run,
  session `e1d4097c`, record `docs/sessions/2026-10-18-0001-queue-run-the-plugin-installed.md`
  (barred to the reviewer until phase 2). That one session authored the whole of the `160/900`,
  `160/910` and `160/930` deltas; the pointer names its worktree for this delta as
  `atelier-qr-130-030`, and says it dispatched the Sonnet worker that wrote the code. Who wrote
  the skill text, the brief-writer cannot say: it did not read either commit's message body or
  the intent record.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on 2026-10-18 by a
  different Mike-opened Opus 5.5 queue run, session `8e498ef1` (worktree
  `atelier-qr-briefs-1018`), which Mike started directly with a bare `/atelier:queue-run`. The
  dispatching run was **neither started nor instructed by the authoring session**, and neither
  it nor the brief-writer authored any of this delta. **Verified from git** (commit times, read
  with `git log --format='%h %cI %s'`): `8132805` and `30aa8dc` were committed 2026-10-18 00:44
  and 00:45 UTC; the dispatching run's own commits are `f0d6238` (05:00 UTC) and `a9f11ff`
  (05:09 UTC), both board claims. Git cannot name a session; the session attribution is the
  dispatching run's account, and two lines of the authoring session's record agree with it (it
  records the dispatching run as "opened by Mike" and "watched from here"). One oddity, stated
  as fact: that record's identifiers line gives its window as 2026-10-17 23:59 to 2026-10-18
  04:14 UTC, while it records watching a run that opened after 04:14. **Off-tier for review,
  disclosed: it forms no finding and writes no severity**, and stops after this brief and its
  sibling.
- ⚠️ **One channel contact, disclosed for the reviewer to weigh** under roadmap `280/040` (the
  cross-session channel can contaminate review independence). After this brief-writing began,
  the authoring session sent the dispatching run's orchestrator one cross-session file-set
  notice: that `ccclose` had changed under that run's `210/290` worker, a request to rebase
  before merging, and a note that `12e6d9b` had landed and `160/900` had been widened to it. The
  orchestrator reports it carried no evaluative content about any delta. The brief-writer never
  saw the notice itself, only the orchestrator's paraphrase of it.
- **Who takes the review:** a cold Fable session, not yet started, passing rule 4's criterion. If
  it runs as reviewer-plus-orchestrator, rule 4's off-tier conditions apply and are disclosed in
  the claim, the pointer and the verdict. The reviewer repeats its own provenance in the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material met before writing):
  - its two assigned pointers in full (this one and `160/910`, refs-only, each with a claim
    line); the `160/780` pointer in full as a shape example, including its claim and the summary
    of its verdict (another pass, on `EVIDENCE.md`);
  - the precedent brief `docs/reviews/2026-10-17-0930-agreement-not-corroboration-cold.md` (ask
    half and the head of its verdict) and its sibling as first committed (`b42f305`) — another
    pass's framing, on other surfaces; no other file under `docs/reviews/` was opened;
  - the whole of `skills/review-brief/SKILL.md` at HEAD (this delta, read as the brief-writer's
    own instructions) and `docs/method/REVIEW.md` lines 25–229 at HEAD;
  - this delta's subjects, stats and diffs through `tools/coldsweep.py --commit` (the tool under
    review, used to read itself; `8132805` whole, `30aa8dc` scoped to the skill), never a
    message body;
  - it also wrote the `160/910` brief in the same sitting, whose delta (`adf75a4`) hands this
    item one of its doors; it read that diff the same way;
  - filename-level greps that listed the intent record's path, and scanner output that named one
    `docs/sessions/` file by path, line and rule (contents not seen);
  - it later wrote the `160/900` brief too, so it read that pointer and that delta (the same
    authoring session's queue-run, prompt and `RECORD.md` work) body-free, and the whole of
    `docs/method/session-open/README.md` at `origin/main`;
  - at its orchestrator's request, to check provenance, lines 139–145 and 159 of the authoring
    session's record (a passage on the dispatching run, and the record's identifiers line);
  - its harness-loaded memory index and instruction files, and recent `git log --oneline`
    subjects.

  It did **not** open the intent record, `docs/SESSIONS.md`, the rest of `docs/sessions/`,
  `docs/ROADMAP-DONE.md` or any prior verdict on these surfaces. Its orchestrator passed it an
  instruction set (pointers, the precedent pair, the prefix check, the pointer-note shape), the
  provenance account above and the paraphrased notice, and no evaluative content about the
  delta. Everything evaluative the brief-writer formed is in the
  sibling, which holds seven questions and three facts.

## What the work is

Landing commits (diff each on its delta paths; review the paths at HEAD, `f0d6238` or later):

- `8132805` (2026-10-18 00:35 UTC) — coldsweep: add --commit SHA, the body-free read of a landing
  commit. Delta paths: `tools/coldsweep.py`, `tools/test_coldsweep.py`.
- `30aa8dc` (2026-10-18 00:45 UTC) — review-brief: name the body-free commit read; close 130/030,
  queue 160/930. Delta path: `skills/review-brief/SKILL.md` (two hunks: item 1, *Subject under
  review*, and item 5, *Re-run every "live-proven" claim*).

No later commit touches any delta path; confirm that.

**Read the commits body-free**, with the tool under review: `python3 tools/coldsweep.py --root .
--commit 8132805` and `python3 tools/coldsweep.py --root . --commit 30aa8dc --path
skills/review-brief/SKILL.md`. Plain `git show` is barred here: it prints the message body before
the diff, and reading is atomic (rule 1). Keep the `--path` on `30aa8dc` — the commit also edits
the intent record and this pass's pointer, which coldsweep does not bar by default. Because the
tool is the subject, also check its output independently before trusting it (a scratch clone and
a plumbing command that cannot print a body are yours to choose). The board and index edits are
not the delta.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Non-goals are the only narrowing and
are themselves reviewable.

Probe, at least:

- **The guarantee, attacked live.** The docstring says the body "is never requested from git, so
  it cannot be printed". In a throwaway repo under your scratchpad, build commits whose messages
  vary in every way git's message model allows, and record for each whether any line that is
  not the subject reaches the tool's output. Do the same for notes, trailers and encodings.
- **What the diff still carries.** The barred set is applied to the diff. Build a table: for a
  landing commit that also edits its own intent record, its queue pointer, the session index,
  a session file and a prior verdict, which hunks print with no flags, with `--path`, and with
  `--also-exclude`? Then read the skill's instruction (`--commit <sha> [--path <p>]`) and say
  what a brief-writer following it literally hands the reviewer.
- **Path handling.** Renames, deletions, a barred path given to `--path`, a path spelled with
  `./` or a trailing slash, pathspec magic in `--path`, a `--root` below the repo top, a merge.
- **Exit codes and the closing line.** Every way the command can exit, and whether the
  "message body not read" line can print when something went wrong.
- **The tests.** Do they fail if the guarantee breaks? Mutate the code (for example, swap the
  subject format for one that prints the body) and re-run; a test suite that stays green on a
  broken guarantee is a finding. Check the fixture's environment is portable to CI.
- **The skill text against its parent.** `SKILL.md` declares itself a stamped copy of
  `docs/method/REVIEW.md` that may compress the parent, never contradict or extend it. Check each
  new sentence in both hunks against `REVIEW.md` (rule 1, rule 2, § *Re-run every "live-proven"
  claim*), and against any other surface that tells a brief-writer how to cite a commit — the
  reviews template under `docs/build/`, the queue-run skill, `CONCURRENCY.md`.
- **The re-run duty.** The second hunk adds a duty on the brief-writer. Who can meet it, from
  where, at what cost, and does it agree with rule 4's account of who writes a brief?

**Non-goals:** the barred set itself (REVIEW rule 2 and the 2026-08-17 coldsweep ruling). Whether
`--commit` applies it correctly, and the new text's wording, placement and consistency, are in
scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether a
   tool flag is the right fix for an unfollowable bar, set against changing the bar, and whether
   "the obvious command" a reviewer reaches for will now be this one.
2. **Correctness & quality.** Diff both commits. Run the probes above live. Record each
   overclaim, if any, against the text that makes it (docstring, `--help`, the closing line, the
   skill).
3. **Completeness / harvest.** Every surface that bars a commit body or names how to read a
   commit (see the last two probes). Is a changelog entry, a man page or a stamp owed?
4. **Security & privacy** — mandatory. The tool shells out to git with caller-supplied revisions
   and paths: check argument injection, option injection and pathspec magic against the OWASP
   catalogue (A03 Injection) by hand. Check the test fixture builds no real identity and the text
   names no private repo, person or host. Aim `/security-review` at the code diff only from a
   clean tree (see *House rules*); markdown is in its exclusions, so weigh a clean pass over the
   skill as nothing.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing. The brief-writer ran each line once, from the
worktree root at `f0d6238`; read exit codes explicitly.

- `python3 tools/coldsweep.py --root . --commit 8132805` and `python3 tools/coldsweep.py --root .
  --commit 30aa8dc --path skills/review-brief/SKILL.md` — exit 0, closing line present
- `python3 -m unittest discover -s tools -p test_coldsweep.py -v` and `python3
  tools/coldsweep.py --selftest`
- `python3 tools/wrapscan.py --root . tools/coldsweep.py tools/test_coldsweep.py`, and
  `tools/spellscan.py` and `tools/leakscan.py` over those two files plus the skill
- `git log --oneline 8132805..HEAD -- tools/coldsweep.py tools/test_coldsweep.py` and `git log
  --oneline 30aa8dc..HEAD -- skills/review-brief/SKILL.md` — empty, or each commit named
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`, and `--plane
  hook`); at `f0d6238` the ci plane exited non-zero on findings outside the delta paths, so read
  which scanner and which file before you weigh it

## House rules for this run

- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and your scratch
  clone. Never open another `docs/reviews/2026-10-18-*` file — it is another pass's framing.
- No git command that writes in the worktree, beyond committing this one file at the end of each
  phase (or handing it to your orchestrator to commit). Read-only git is fine. Probe repos,
  mutated copies and older checkouts go under your session scratchpad, named by your prefix;
  never mutate the worktree's `tools/`.
- One heavy process at a time: the coldsweep suite as often as your mutations need, the full
  Python suite at most once, all in the foreground; never point a scanner at another repo.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds and do the code-altitude
  read by hand — never with this brief or its sibling dirty.
- This pass is itself pending while you run it: anything you write to the session log, the
  pointer or a commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. Never quote
  a secret, a placeholder token, an email address or a personal detail — this repo is PUBLIC.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/930-rule-4-cold-pass-queued-body-free-commit-read.md`,
the sibling `docs/reviews/2026-10-18-0508-body-free-commit-read-cold.deferred.md`, both landing
commits' message bodies (read subject, stat and diff only), and the intent record:

- `docs/roadmap/130-a-closed-cycle-can-keep-its-and-pointers/030-the-brief-bars-the-commit-body-but-names-no-command-that-avoids-it.md`

The tool's own docstring and `--help` carry a short account of why it exists; they are the
delta, and reading the delta is never barred.

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/930-rule-4-cold-pass-queued-body-free-commit-read.md
--also-exclude docs/reviews/2026-10-18-0508-body-free-commit-read-cold.deferred.md
--also-exclude
docs/roadmap/130-a-closed-cycle-can-keep-its-and-pointers/030-the-brief-bars-the-commit-body-but-names-no-command-that-avoids-it.md
<pattern>`; `--include-barred` only with disclosure in the verdict. The author's narrative of why,
and the verdicts that recorded it, are barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses, the probes and the re-run list. Append
your verdict below a `---` divider in THIS file: provenance repeated (how you were spawned, your
tier, what you read), per-lens answers, findings with stable IDs (prefix `BF`: `BF1`, `BF2`, …)
and severities (MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, a re-run ledger (commands and results) and a follow-up checklist. Then STOP and
commit this file before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling. Append `### Reconcile` beneath your verdict: per-finding notes
against its seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Fold the sibling in below the
reconcile and delete it.

The code is ordinary code but the skill is doctrine, and both were queued together as one
doctrine pass: record all findings and apply nothing (rule 3); the principal decides. Counsel
per finding is welcome, labelled as counsel.

---

# Verdict — phase 1 (written 2026-10-25 UTC, launch 22:34 UTC)

## Provenance (REVIEW.md rule 4, V7)

- **Who reviewed:** a Claude Fable 5.1 reviewer subagent — the tier the principal names for cold
  passes, checked at selection — spawned by session `52e11d15` (Claude Opus 5.5). That session
  orchestrates only: it holds the context partition, released nothing before this verdict was
  written, forms no finding and writes no severity. It authored neither the delta nor this brief,
  and was not started or instructed by session `e1d4097c` (the author) or `8e498ef1` (the
  brief-writer's run). It launched this reviewer at 2026-10-25 22:34 UTC under the principal's
  approval of Fable work for the week ending 2026-10-25 23:00 UTC; he ruled that a review started
  before then may finish after it. This is the reviewer-plus-orchestrator arrangement rule 4
  allows, disclosed here before the findings, as the claim and the pointer disclose it.
- **Where:** branch `atelier-cold-160-930`, a worktree at `a40438e` (= `origin/main` at launch),
  read-only to me except this file; probes, mutated copies and fixture repos in a fresh directory
  under the system temp root. The worktree's only pending change is the sibling `.deferred.md`,
  removed on purpose by the orchestrator (it shows as a deletion in `git status`); I did not open
  it, look for it, or read any scratch listing.
- **What I read before writing:** this brief in full; `docs/method/REVIEW.md` in full;
  `tools/coldsweep.py`, `tools/test_coldsweep.py` and `skills/review-brief/SKILL.md` at HEAD; both
  commits through the tool under review (`--commit 8132805`; `--commit 30aa8dc --path
  skills/review-brief/SKILL.md`), cross-checked against `git diff-tree -p --no-commit-id`, a
  plumbing command that prints no message at all; `.githooks/pre-commit`,
  `.github/workflows/ci.yml`, `tools/floor.py` (docstring and the registry lines for the three
  scanners), `.atelier-floor.json`, the `coldsweep` section of `tools/README.md`, the head of
  `CHANGELOG.md`, `docs/build/templates/docs/reviews/README.md`, and the lines of `REVIEW.md` the
  skill cites. Tree sweeps ran through `coldsweep` with the brief's three `--also-exclude`s; I
  filtered every `docs/roadmap/` hit out unread, except that one sweep surfaced the board index's
  own claim line for this item (the arrangement, no evaluative content) — disclosed.
- **Not read:** any commit message body; the intent record; the queue pointer; `docs/SESSIONS.md`;
  `docs/sessions/`; `docs/ROADMAP-DONE.md`; any other file under `docs/reviews/`; the sibling. The
  harness loaded user-level instruction and memory files at start; none concerns this delta.
- **Exposure to weigh:** the one channel contact and the brief-writer's exposure are as the brief
  states; I had none of my own beyond the above. `--include-barred` was used once, on a fixture
  repo, never on this tree.

## Lens 1 — approach and assumptions

The load-bearing assumptions, named first and then tested:

1. *The subject, stat and diff are not the author's account; the body is.* **Half true.** The
   diff of a rule-4 landing commit carries the intent record and the pointer, which doctrine
   designates as the home of the evaluative account (BF1). The subject is git's first paragraph,
   not the first line (BF2).
2. *Git's `%s` is the subject line.* **False in general** — `%s` folds the first paragraph into
   one line (probe cases b, g, j, k).
3. *Applying rule 2's barred set to the diff is the right exclusion for a landing commit.* Only
   the index, records and verdicts are in that set; the board store, where rule 4 puts the
   account, is not — the docstring itself names only `docs/SESSIONS.md` as "the author's account".
4. *A tool flag is the right fix for an unfollowable bar.* **Agreed, with a caveat.** The bar was
   followable without a tool — `git log -1 --format=%s` plus `git diff-tree -p --no-commit-id -r`
   prints the same diff byte for byte (verified on both commits) — but nobody reached for that
   pair; the defect was the *obvious* command, so the remedy has to become the obvious command.
   That only happens if it is named where briefs are written and where tools are documented;
   at `a40438e` it is named in the skill and nowhere in the parent or the README (BF5, BF8).
5. *The brief-writer can run every re-run line first.* Feasible — this brief's writer did — but
   the duty exists only in the stamped copy (BF5), doubles the cost of every re-run line, and in an
   orchestrated run of several briefs meets the "one heavy process at a time" rule head-on.

## Lens 2 — correctness and quality (probes, all live)

Fixture repos were built under the scratch directory with a synthetic `.invalid` identity, no
global or system git config, and marker strings in every message body, note, trailer and record.

**The guarantee, attacked.** Fourteen message shapes. No non-subject text reached the output for:
`-m`/`-m` paragraphs, leading blank lines under `--cleanup=verbatim`, trailers, a git note (with
and without `notes.displayRef`), a Latin-1 encoded message, a whitespace-only separator line, a
subject-only message, an empty message, `log.showSignature=true`, a configured `diff.external`
(the `--no-ext-diff` flag held), `core.abbrev=12` (only `%h` widened) and `diff.noprefix=true`.
**It leaked** — the second line printed as part of the "subject" — whenever the first paragraph
ran past line one: no blank line after the subject (b), CRLF under `verbatim` (g), a `#` comment
line kept by `verbatim` (j), and a tab-indented second line under the default cleanup (k). Both
real commits have one-line first paragraphs (counted, not read), so the reads above were clean.

**What the diff still carries** — a landing commit that edits code, its intent record, its queue
pointer, `docs/SESSIONS.md`, a `docs/sessions/` record, a `docs/reviews/` verdict and
`docs/ROADMAP-DONE.md`:

| invocation                                   | intent | pointer | index/record/verdict/done |
|----------------------------------------------|--------|---------|---------------------------|
| `--commit <sha>`                             | shown  | shown   | left out, named           |
| `--commit <sha> --path <code>`               | hidden | hidden  | left out, named           |
| `--commit <sha> --also-exclude <both files>` | hidden | hidden  | left out, named           |
| `--commit <sha> --also-exclude docs/roadmap` | hidden | hidden  | left out, named           |
| `--commit <sha> --include-barred`            | shown  | shown   | shown, banner             |

A brief-writer following the skill literally — `--commit <sha> [--path <p>]`, the flag optional
and no trigger stated — hands the reviewer the intent record's closing hunk and the pointer on
every rule-4 landing commit, because rule 4 puts the pointer in that commit and the close of the
intent record normally rides with it. `30aa8dc` is exactly that shape (`git diff-tree
--name-status`: the intent record, the pointer, the index and the skill). The brief's own author
knew to add `--path`; the skill does not say so.

**Path handling.** `./x`, `x/`, `x//y` all scope correctly. A barred path given to `--path` prints
"(no changes in scope)" and still lists the file as left out (good). Pathspec magic is accepted:
`:(exclude)…` and `:!…` as the only positive spec mean "everything else", `:(glob)` and
`:(icase)` work, and in every case the barred exclusions held. A rename out of `docs/sessions/`
prints the record's content as an add; a rename into it prints the old content as a deletion; a
deleted barred file is left out and named. A merge diffs against its first parent. `--root` below
the repo top: the exclusions stay top-anchored (right), but `--path` becomes relative to that
directory, so the brief's `--path skills/…` silently matches nothing; the tree-search mode, by
contrast, anchors its bar at `--root`, so from `--root docs` the index is searched and the
closing line says "0 excluded". An absolute `--also-exclude` is not applied in either mode and is
listed as excluded in both.

**Exit codes and the closing line.** Exit 2, no closing line: unknown revision, not a repository,
`git` absent from `PATH` (caught as `OSError`), `--commit` with a pattern or `--list-barred`,
`--path` without `--commit`, option-shaped revisions. Exit 0 **with** the proof line: a `--path`
that matches nothing (typo, wrong case, or `--root` below the top), and a shallow clone's boundary
commit, which is labelled "root commit" and diffed against the empty tree — the whole tree prints
as the delta.

**The tests.** 34 tests, green on the system interpreter (3.9) and the `PATH` interpreter (3.14);
CI pins 3.12. Mutations of a scratch copy: swapping `%s` for `%B` fails 8 tests; ignoring `--path`
fails 3; suppressing the dropped-file list fails 2; mislabelling the root-commit basis fails 2.
The suite **stays green** when any of these is removed: the `top` anchor on the exclusions,
`--no-notes`, `--no-ext-diff`, `--no-color`, `--end-of-options`, and the git-failure check that
returns 2 instead of printing "(no changes in scope)" under a proof line. The fixture's
environment is portable to CI by reading (ubuntu, `git` on `/usr/bin`, `HOME` redirected,
`GIT_CONFIG_NOSYSTEM`); I did not run it on Linux. The isolation covers only the fixture's own
git calls — the tool's `_git` inherits the real environment, so a developer's global
`core.abbrev` would fail the `%h` assertion.

**Overclaims, against the text that makes them.** Docstring: "The body is never requested from
git, so it cannot be printed" — true of the request, false of the printing (BF2). `--help`:
"NEVER its message body" — same. `_pathspec` docstring: "no spelling of a barred path can fail to
match" — an absolute spelling does (BF4). The closing line: "message body not read" is literally
true in every run observed, including the ones where the first paragraph or the intent record
printed; it is a narrower proof than a reader will take it for (BF1, BF2).

## Lens 3 — completeness and harvest

Surfaces that bar a commit body or say how to cite a commit: `REVIEW.md` rule 1 ("the
commit-message door is `130/030`'s" — a pointer to the item this delta closes); the skill (this
delta); the child reviews template (`docs/build/templates/docs/reviews/README.md`: "point, don't
paste", no commit command); the queue-run skill and `CONCURRENCY.md` (nothing). `tools/README.md`
documents `coldsweep` without `--commit` or `--path`; `CHANGELOG.md` has the 2026-08-17 entry and
nothing for this delta; the skill carries no stamp marker and `stampscan` does not watch it. No
man page is owed (`coldsweep` is a tool, not an instrument). The `--selftest` corpus covers the
tree search only; CI covers `--commit` through the unittest step, not the selftest loop.

## Lens 4 — security and privacy

Checked by hand against OWASP A03 (injection), for the tool's class (a wrapper over `git` with
caller-supplied revisions and paths). `subprocess.run` with an argument list and no shell — a
`--root` carrying `;` is a directory name (rejected as not a directory). The one caller-supplied
revision passes through `rev-parse --verify --quiet --end-of-options <rev>^{commit}` and only the
resolved SHA is reused: `--all`, `--output=…`, `HEAD --output=…`, `HEAD^{tree}` and
`HEAD:<path>` are all rejected with exit 2; the `:/<regex>` message-search revision is rejected
too, because the `^{commit}` suffix becomes part of the regex — a message-content oracle closed by
accident rather than design (note BF12). Every path goes after `--`: `--path --output=…` and
`--also-exclude --output=…` created no file. `--no-ext-diff` and `--no-textconv` hold against a
configured external diff. Nothing is written anywhere. Privacy: the fixture identity is built, not
a literal address, and lands on a reserved `.invalid` domain; the delta's text names no private
repo, person or host. `/security-review` is **discharged with grounds**: it reads this session's
pending diff, which in my worktree is this brief and the removed sibling — deferred material the
rule says never to scan — and the landed diff was read at code altitude by hand as above.

## Findings

- **BF1 — MAJOR.** *The default read hands over the author's account on the commits it was built
  for.* On a rule-4 landing commit, `--commit <sha>` with no `--path` prints the intent record's
  closing hunk and the pointer under a clean "message body not read" line; the skill makes
  `--path` optional and names no trigger, and the docstring calls `docs/SESSIONS.md` "the author's
  account" while `REVIEW.md` rule 4 puts the evaluative account in the intent record and the
  pointer in the landing commit. Evidence: the table above; `30aa8dc`'s own file list. *Counsel
  (the principal decides; the barred set itself is a non-goal here):* in the skill, make the
  `--path` list mandatory whenever the landing commit touches a board item and say why; in the
  tool, name any `docs/roadmap/` file the diff shows on the closing line so the proof line stops
  reading as complete; the brief-writer always writes the full command with its `--path`s, as this
  brief did.
- **BF2 — MODERATE.** *`%s` is the first paragraph, not the first line.* A message with no blank
  line after its subject, a CRLF message, a verbatim comment line or an indented second line
  prints that line as part of the subject; the docstring and `--help` say the body "cannot be
  printed". Not MAJOR because it needs an author to omit the blank line, which the house's
  `-m`/`-m` habit inserts, and both real commits are clean — but a reviewer citing the proof line
  cannot tell. *Counsel:* read the raw message into memory and print only its first line, and
  reword the guarantee from "never requested" to "never printed"; or keep `%s` and refuse (exit 2)
  when the first paragraph has more than one line; add case b to the tests either way.
- **BF3 — MODERATE.** *A `--path` that matches nothing is a clean run.* A typo, a case slip, one
  bad path among good ones, or a `--root` below the top yields "(no changes in scope)", the proof
  line and exit 0 — and this brief's own re-run criterion is "exit 0, closing line present".
  `test_path_with_no_changes_says_so` pins that as intended. *Counsel:* exit 1 when nothing was in
  scope (the tool's own grep contract already means "no match" by 1) and name each `--path` that
  matched no changed file; flip the test with it.
- **BF4 — MODERATE.** *An absolute `--also-exclude` is not applied but is reported as excluded*,
  in both modes. `_parts` (pre-existing) says an absolute path under the root yields the same parts;
  `_pathspec` (this delta) says no spelling can fail to match. The disclosure line is therefore
  false in exactly the class — a silently unapplied exclusion — the tool exists to end.
  *Counsel:* make an absolute path relative to the resolved repo top, exit 2 if it lies outside,
  and test both modes.
- **BF5 — MODERATE.** *Both new skill sentences have no home in the parent (V4, V3).* The parent's
  only word on the commit-message door is the pointer to `130/030`, which this delta closes, so
  after it the rule lives only in a stamped copy that declares itself "not a second source"; the
  brief-writer's re-run duty appears in no parent section at all — the copy extends where its
  header says it may only compress. *Counsel:* one sentence in `REVIEW.md` rule 2 naming the
  body-free read beside the tree sweep, replacing the `130/030` pointer; the re-run duty either
  lands in § *Re-run every "live-proven" claim* or comes out of the skill.
- **BF6 — minor.** *Six guards have no test.* The suite stays green with the `top` anchor,
  `--no-notes`, `--no-ext-diff`, `--no-color`, `--end-of-options` or the git-failure check
  removed. The last three are the ones that matter: an external diff may print anything, the
  options guard is the injection defence, and a failed `git diff` would otherwise print "(no
  changes in scope)" under the proof line. *Counsel:* one test each, using repo-local config for
  the first two.
- **BF7 — minor.** *The fixture isolates its own git, not the tool's.* `_git` inherits the real
  environment, so a global `core.abbrev` fails the `%h` assertion on a developer machine (CI is
  unaffected). *Counsel:* pass the fixture's environment into the tool under test, or assert on
  the subject text rather than the abbreviated hash.
- **BF8 — minor.** *Mirror sites missed (V3).* `tools/README.md`'s `coldsweep` section and
  `CHANGELOG.md` do not mention `--commit` or `--path`; the README's usage block is the first
  place a reviewer who is not reading a brief will look.
- **BF9 — minor.** *`--root` means two things.* In `--commit` mode the exclusions are top-anchored
  but `--path` is relative to `--root`; in tree-search mode the bar is relative to `--root`
  (pre-existing), so a root below the top searches the index. *Counsel:* resolve `--root` to the
  repo top for both modes, or refuse a root below it.
- **BF10 — minor.** *A shallow clone's boundary commit is reported as a root commit* and the whole
  tree prints as its delta under the proof line. *Counsel:* detect a shallow repository and exit 2
  with a message; a reviewer's scratch clone is where this will happen.
- **BF11 — note.** The bar follows the path, not the content: a record renamed out of
  `docs/sessions/` prints as an add, and a file renamed into it prints its old content as a
  deletion. By design; worth one docstring sentence.
- **BF12 — note.** `--path` accepts pathspec magic, including negative-only specs that mean
  "everything else"; harmless (every exclusion held) but undocumented. The `:/<regex>` revision is
  rejected only because `^{commit}` joins the regex — a comment would stop a refactor reopening
  the oracle.
- **BF13 — note.** Brief inconsistencies, neither steering a finding: `8132805` is "00:35 UTC" in
  *What the work is* and "00:44" in the provenance (author time and committer time; both true);
  the brief says the skill may "never contradict or extend" the parent where the stamp says
  "never contradict it".
- **BF14 — note.** "Four of twenty-one reviewers in one batch" in the docstring is the author's
  claim; its grounding sits in records barred to me in phase 1, so it is carried as a claim.

## Overall

**PASS-WITH-FINDINGS — 1 MAJOR (BF1), 4 MODERATE (BF2–BF5), 5 minor (BF6–BF10), 4 note
(BF11–BF14).** The code does what its tests say and nothing in it is unsafe to run; what fails is
the proof it offers. Per rule 3 nothing is applied; every counsel line is counsel.

## Standing checklist

V1 → BF1, BF2, BF4 (claims wider than their evidence). V2 → the ledger below, all reproduced.
V3 → BF5, BF8. V4 → BF5. V5 → docstring against behaviour (BF2, BF4); skill against parent
(BF5); `--root` against itself (BF9). V6 → lens 4. V7 → the provenance block above.

## Re-run ledger (from the worktree root at `a40438e`, system `python3` 3.9 unless stated)

| command                                                                     | exit | result |
|-----------------------------------------------------------------------------|------|--------|
| `tools/coldsweep.py --root . --commit 8132805`                              | 0    | subject, stat, diff; closing line; 0 barred files touched |
| `tools/coldsweep.py --root . --commit 30aa8dc --path skills/review-brief/SKILL.md` | 0 | as above; diff identical to `git diff-tree -p --no-commit-id` |
| `python3 -m unittest discover -s tools -p test_coldsweep.py -v`             | 0    | 34 tests OK (3.9); 34 OK on the `PATH` interpreter (3.14) |
| `tools/coldsweep.py --selftest`                                             | 0    | selftest OK |
| `tools/wrapscan.py --root . tools/coldsweep.py tools/test_coldsweep.py`      | 0    | clean |
| `tools/spellscan.py --root . <two files> skills/review-brief/SKILL.md`       | 0    | clean |
| `tools/leakscan.py --root . <two files> skills/review-brief/SKILL.md`        | 0    | clean (structural + local) |
| `git log --oneline 8132805..HEAD -- tools/coldsweep.py tools/test_coldsweep.py` | 0 | empty — no later commit on the code paths |
| `git log --oneline 30aa8dc..HEAD -- skills/review-brief/SKILL.md`           | 0    | empty — no later commit on the skill |
| `tools/floor.py --plane ci --root .`                                        | 0    | all enforced checks clean; `pathscan` (warn-only) 3 findings, none on a delta path; `secretscan` 23 advisory, none on a delta path |
| `tools/floor.py --plane hook --root .`                                      | 0    | clean (nothing staged) |

The ci plane was red at `f0d6238` per the brief and is green at `a40438e`; the remaining
warn-only findings are outside the delta. The full Python suite was not run — the re-run list does
not name it and CI runs it on every push.

## Follow-up checklist (for the principal's decision, rule 3)

- [ ] BF1 — skill: mandatory `--path` on board-touching landing commits; tool: name shown
      `docs/roadmap/` files on the closing line; brief-writers write the full command.
- [ ] BF2 — print the first line only (or refuse a folded subject); reword "cannot be printed";
      test case b.
- [ ] BF3 — exit 1 and name unmatched `--path`s; flip the test.
- [ ] BF4 — resolve absolute `--also-exclude` against the repo top or exit 2; test both modes.
- [ ] BF5 — home the body-free read and the re-run duty in `REVIEW.md`, or drop the duty.
- [ ] BF6, BF7 — tests for the six untested guards; isolate the tool's environment under test.
- [ ] BF8 — `tools/README.md` usage block and a `CHANGELOG.md` entry.
- [ ] BF9, BF10 — one meaning for `--root`; refuse a shallow repository.
- [ ] BF11–BF14 — docstring sentences and comments; the brief's two inconsistencies, for the
      record.

### Reconcile — act 2 (written 2026-10-25 UTC, after act 1 was received by session 52e11d15)

Opened at release, in this order: the held sibling (three facts, seven questions), the intent
record `130/030`, the queue pointer `160/930`, and both message bodies. The prior verdict the
sibling points to (`2026-08-17-1000-coldsweep-cold.md`) predates `--commit` and does not mention
it; named, not opened. The neighbouring pass's brief (`160/910`) stays unopened per this brief's
house rules. Nothing in act 1 is revised; where the record changes the weight or the counsel of a
finding, that is said under the finding.

**Against the seeded questions.**

1. *`%s` is the first paragraph.* Found independently as BF2, with the same mechanism and four
   live cases. The brief-writer's suspicion and mine coincide; the sibling adds nothing to the
   severity, which stays MODERATE for the reason given there. One test (the `%B` mutation) does
   cover the body; none covers a folded first paragraph.
2. *The intent record is in the diff.* Found independently as BF1 (MAJOR). The sibling names
   `adf75a4` as a second instance; I re-drove the intent record's own recorded proof — "a real
   run on `adf75a4` matched none of that commit's body lines" — and it reproduces (0 of 8 body
   lines in the output), **and that same run prints the `160/910` pointer and the `320/720` item
   hunks**. The author's proof of the body guarantee is itself the BF1 case: the body stayed out
   while the
   board items came through under the clean closing line. Weight up; severity unchanged.
3. *The closing line's claim.* Covered in act 1 under *Overclaims* and in BF1/BF2: the line is true
   of the `log` call and narrower than a reader takes it for. Added to BF1's counsel: have the
   closing line say what it is — "subject, stat and diff of N file(s) printed; message body not
   requested" — and name any board-store file shown, rather than asserting a negative.
4. *The stamped copy extends its parent.* Found independently as BF5 (MODERATE). The intent record
   now supplies the grounding the sibling lacked: the re-run duty answers a real defect (PF10, a
   brief's re-run line that failed from the repo root). That strengthens the case for homing the
   duty in `REVIEW.md` § *Re-run every "live-proven" claim* and weakens the "or drop it" branch of
   my counsel; the duty as worded is also broader than its grounding, which "from where the brief
   says to run it" alone would meet. Counsel amended: home it, scoped to its ground.
5. *"Plain `git show` is barred."* Not in act 1; formed here as **BF15 — note (formed at
   reconcile)**. The bar on the body is the brief's and the skill's, not the parent's: `REVIEW.md`
   rule 2 bars the author's records and names the body nowhere, and body-free `git show` forms
   exist (`--format=%s --stat`, `--no-patch`). The intent record's own proposed fix was exactly
   `git show --stat --format=%s <sha>`; the shipped skill then calls plain `git show` "barred"
   without the qualifier "in its default format" and without the parent saying so. The same
   homing as BF5 cures it: state in the parent that the body is barred until phase 2 and that the
   default `git show` prints it.
6. *Test portability and strength.* Covered: lens 2 (portable to CI by reading; not run on Linux),
   BF6 (six guards untested), BF7 (the tool's own git calls inherit the real environment). The
   `%B` mutation fails eight tests, so the sibling's second question is answered yes.
7. *The re-run duty's reach.* Covered under lens 1 (assumption 5) and BF5. The record confirms the
   duty's origin (PF10) and that the brief-writer who wrote this brief met it from a worktree at
   `f0d6238`; it assumes a brief-writer on the same machine with the same tools, which the
   2026-10-16 practice supplies and the parent nowhere requires. No change.

**Against the three facts.** (1) The intent record and both bodies were read only now; nothing in
them contradicts a finding. The body of `8132805` says "exclusions are anchored at the repo top,
so no spelling of a path can miss" — BF4 (absolute paths) and BF9 (`--path` is not anchored) are
the two spellings that do. (2) The `160/910` coupling is real: BF5's counsel to replace the parent's
"the commit-message door is `130/030`'s" with a sentence naming the read edits the paragraph that
pass reviews; the principal should decide the two together. (3) Addressed above.

**Against the intent record's other claims.** "Never asks git for the body" — true of the request,
and BF2 stands on the printing. "Built by a Sonnet worker and read before merge" — consistent with
the trailer on `8132805`; carried as stated. "The tools suite went from 1916 to 1930 tests" — the
delta adds 14 tests to `test_coldsweep.py` (counted), which matches the difference; I ran the full
suite once, as this brief allows, and my capture took a selftest's trailing lines instead of the
`Ran N tests` summary, so the total is **not re-verified by me**, and I did not run it twice.
The record's proposed fix (name plumbing commands in the brief) was superseded by the tool-only
remedy; lens 1 assumption 4 already weighs that trade and it stands.

**BF14 resolved at reconcile.** "Four of twenty-one" is grounded: the intent record names the five
2026-10-16 verdict files (not opened) — four body reads by `git show` and one `grep` exclusion
miss. The body of `30aa8dc` says "five reviewers … read a barred commit body by the obvious `git
show`", folding the grep slip into the body count; the docstring's four is the accurate figure.
Stays a note.

**Overall, restated: PASS-WITH-FINDINGS — 1 MAJOR (BF1), 4 MODERATE (BF2–BF5), 5 minor
(BF6–BF10), 5 note (BF11–BF15).** No act-1 severity changed; BF1 gained the author's own proof
run as evidence; BF5's counsel narrowed to homing; BF15 added. Nothing applied — the principal
decides, with `160/910` beside it.

Follow-up addition:

- [ ] BF15 — when BF5 is homed, say in the parent what is barred (the body, until phase 2) and
      why the default `git show` is the trap; "barred" with its qualifier, or a softer word.

---

## Deferred sibling, folded below the verdict (orchestrator, 2026-10-25)

*Released to the reviewer only after its act-1 findings were saved; folded here verbatim and
the sibling file deleted, per the brief. The orchestrator (session `52e11d15`, Claude Opus 5.5)
formed no finding and wrote no severity.*

### Sibling to the body-free-commit-read cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-18-0508-body-free-commit-read-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-18 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Facts held back

1. **Intent record:** `130/030` (the item whose path the brief bars) — **not opened by the
   brief-writer**. Neither commit's message body was read either, so this sibling carries no
   account of the author's reasons beyond what the tool's docstring states; read both at
   reconcile.
2. **The neighbouring pass.** `adf75a4`'s new *side doors* paragraph in `REVIEW.md` rule 1 ends
   "The commit-message door is `130/030`'s", so it treats this delta as the fix for one of its
   doors. That paragraph is queued at `160/910`, briefed in the same sitting by this same
   brief-writer. The two passes share a brief-writer's framing; neither was told what the other
   found.
3. **Prior verdicts on this surface** (named by filename only, not opened, not exhaustive): the
   pass behind the 2026-08-17 coldsweep ruling is the nearest; find it with
   `ls docs/reviews | grep -iE 'coldsweep|cold-sweep|sweep'` at reconcile.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. **`%s` is not the first line.** The tool prints `git log --format=%h %s`. Git's `%s` is the
   first *paragraph* of the message, joined onto one line. A message with no blank line after its
   first line prints its whole first paragraph as the "subject". Does the docstring's "cannot be
   printed" survive that, and does any test cover it?
2. **The intent record is in the diff.** Landing commits here routinely edit their own intent
   record and queue pointer (`adf75a4` and `30aa8dc` both do), and neither is in the default
   barred set. The skill tells a brief-writer to cite `--commit <sha> [--path <p>]`, with
   `--path` optional and no mention of `--also-exclude`. Does a literal follower print the
   author's account through the hunk the tool was built to avoid, under a closing line saying the
   body was not read?
3. **The closing line's claim.** "message body not read" is printed after any successful run. Is
   it a statement about what the tool printed (true by construction of the `log` call), or a
   wider claim a reviewer will read as "nothing of the author's account reached me"?
4. **The stamped copy extends its parent.** The skill's header says it may compress
   `REVIEW.md`, never contradict it. As far as a grep of `REVIEW.md` shows, the parent names
   neither `--commit` nor a duty on the brief-writer to run re-run lines; both hunks may be
   content the parent does not hold, which inverts the stamped-copy direction (one fact, one
   home).
5. **"Plain `git show` is barred."** The skill says plain `git show` prints the body before the
   diff. That is true of its default format; `git show --format=%s` or `--no-patch` variants do
   not. Is "barred" the right word for a command whose default leaks, and does the parent bar it?
6. **Test portability and strength.** The fixture's `PATH` is hard-coded to four directories and
   `HOME` to the temp dir. Does that run on CI's image and on a machine with git elsewhere? And is
   there a test that would fail if `--format=%h %s` became `--format=%h %B`?
7. **The re-run duty's reach.** Item 5 now says the brief-writer runs every re-run line once
   before writing it down. Rule 4 says the brief is written by the non-author who takes the
   item; under the 2026-10-16 practice a separate Opus brief-writer writes it instead. Does the
   duty assume a brief-writer with the reviewer's tools and machine, and does rule 4 or `REVIEW.md`
   § *Re-run every "live-proven" claim* say the same?
