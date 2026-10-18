# Cold pass — the body-free commit read, in coldsweep and the review-brief skill

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-18 UTC by an Opus brief-writer;
the pass waits for a cold Fable session that neither the delta's author nor this brief-writer
(nor its orchestrator) started or instructed; tier checked at selection (rule 4).
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
