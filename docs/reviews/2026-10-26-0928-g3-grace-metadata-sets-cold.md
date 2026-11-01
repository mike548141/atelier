# Cold pass — G3: binaries gated with a dated grace, metadata kept set by set, floor flag refusal

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes the pass. The principal's current standing ruling is that no Fable work runs
without his explicit permission, so this pass waits for that permission as well.
**Status:** PASS-WITH-FINDINGS, phase 1 — 0 MAJOR · 5 MODERATE · 5 minor · 4 note. Ran
2026-11-01 UTC on Fable 5.1 under an off-tier orchestrator (session 358c8aa0); reconcile
(phase 2) owed. Brief written 2026-10-26 UTC by an Opus 5.5 brief-writer subagent of session
5070f22b; the pass was taken by a cold Fable session that neither the delta's authors nor
session 5070f22b (nor any of its subagents) started or instructed.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/980-rule-4-cold-pass-queued-g3-grace-and-metadata-sets.md`.
**Why it earns a review:** `leakscan` is the personal-data boundary of every adopting child
repo, and children float at `floor.yml@main`, so this change reached every child's next CI run
the day it merged. It does three things that a green exit is read as proof of: it decides
which binary files and which image metadata may sit in a (often public) tree; it adds a dated,
warn-only window to a scanner whose posture is that it has no advisory form (E6a); and it
hardens `floor.py` against the routes a child could use to skip the gate. The worst failure is
a silent one: a binary, or metadata in it, published past a gate that reports clean, or a
grace that can be stretched, skipped or never ends. The original G3 build (2026-10-03) was
never cold-reviewed, so this pass covers the whole PR, not only the last rework.

## Spawn provenance

- **Author of the work under review:** a Mike-opened Opus 5.5 queue run, session `8e498ef1`,
  2026-10-18 (worktree `atelier-qr-020-150`), and the Opus worker it dispatched, which rebuilt
  the held branch, as the queue pointer says. The same session widened the delta to `34dc0f0`
  (`020/440`) on 2026-10-19. The PR's first two commits carry the 2026-10-03 build, rebased;
  who wrote that build the brief-writer cannot say beyond the pointer's account (it read no
  commit body).
- **Who wrote this brief:** an Opus 5.5 subagent (`claude-opus-5-5`) dispatched on 2026-10-26
  by session `5070f22b`, a headless Opus 5.5 brief-writing session started on the principal's
  instruction to have briefs ready for a reviewer when budget allows. Neither it nor its
  dispatcher authored any of this delta. **Off-tier for review, disclosed: it forms no finding
  and writes no severity**, and stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that passes rule 4's
  criterion. **Barred from taking it:** session `8e498ef1` and its workers; session `5070f22b`
  and its subagents. If the pass runs as reviewer-plus-orchestrator, rule 4's off-tier
  conditions apply and are disclosed in the claim, the pointer and the verdict. The reviewer
  repeats its own provenance in the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before
  writing):
  - its dispatch instructions; `skills/review-brief/SKILL.md` whole; `docs/method/REVIEW.md`
    lines 20–230 and 320–450;
  - the house-form pair `docs/reviews/2026-10-18-0511-template-history-privacy-cold.md` (brief
    whole) and its **unrun** `.deferred.md` sibling whole (another pass's held-back material,
    on other surfaces); the brief section of
    `docs/reviews/2026-10-18-0508-body-free-commit-read-cold.md` above its divider, whose
    status line carries that pass's verdict counts (another pass, on `coldsweep`);
  - the queue pointer whole; **the intent record `020/150` whole, including the author's
    account below the principal's words**; `020/440` whole (author's account included);
    `020/450` lines 1–12; `010/190` whole; `020/140` lines 20–40;
  - the delta body-free through `tools/coldsweep.py --commit` (`b5a2c53` diff lines 1–433 of
    2,328: the changelog, README, `allowmarker` and `floor` hunks and the head of the
    `leakscan` hunk; `34dc0f0` lines 1–120 of 246; the four PR commits by stat only); the
    `--help` of `leakscan`, `floor`, `floorfleet`, `pins` and `coldsweep`, and lines 245–270
    of `tools/reviewscan.py`; PR #97's commit
    headlines, dates and state through `gh pr view 97 --json` with a `jq` filter (no PR body,
    comment or review);
  - `tools/test_leakscan.py` lines 1610–1665 and grep lines of it and of `tools/leakscan.py`;
    the heading list of `docs/method/SECRETS.md`; grep-line output of `coldsweep` sweeps for
    `E6a`, `G3`, `2026-11-18` and "advisory form", which surfaced single lines of several board
    items, ADR 0008 and ADR `2026-10-03-0641`; filenames (not contents) under `docs/reviews/`;
  - count-only output of read-only probes over the adopting child repos on the machine (held
    in the sibling, by count).

  It did **not** open `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any other
  prior verdict, any commit message body, or PR #97's body, comments or reviews. Its harness
  also loaded user-level and repo instruction files and a memory index, which hold private
  context this brief does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test: the principal's own words

The pass is judged against the principal's quoted words in the three records below. Print
**only** the quoted spans, before phase 1, with:

```
( cd docs/roadmap/020-policy-as-code-programme-five-tracks-mik &&
  for f in 150-e7-*.md 440-one-*.md 450-g3-*.md; do
    echo "== $f"
    python3 -c 'import re, sys
t = " ".join(l.strip() for l in open(sys.argv[1], encoding="utf-8"))
for m in re.findall(r"\*\"(.+?)\"\*", t): print("-", m)' "$f"
  done )
```

That prints his words and nothing else. The three records are `020/150`, `020/440` and `020/450`
under `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/`. In `020/150`, the first
two spans are the labels of options he chose through the decision device; the option text
around them is the author's and is barred with the rest of those records until phase 2. The
2026-08-04 ruling that G3 blocks, and the 2026-08-09 funding, are cited by the delta but not
quoted in these records: trace their verbatim words in the tree with `coldsweep` (excludes
below) and, if no verbatim record exists, say so. Also apply the repo's purpose-based
personal-data rule (`docs/build/REPO-STANDARD.md`), and the posture E6a set. E6a's doctrine
home is `docs/method/SECRETS.md` § *The boundary's posture — over-flag, because detection
enables everything* (from line 188); its landing is recorded on the E6a line of board item
`020/140`, in the same directory (`140-e6-the-floor-s-posture-and-the-dial-that-makes.md`).
The delta claims to add the one stated exception to it.

## What the work is

- **PR #97, squash `b5a2c53`** on `main`, merged 2026-10-18 09:33 UTC. Delta paths:
  `tools/leakscan.py`, `tools/floor.py`, `tools/allowmarker.py`, `tools/README.md`,
  `CHANGELOG.md` (the `020/150` entry only), and their tests `tools/test_leakscan.py`,
  `tools/test_floor.py`, `tools/test_allowmarker.py`, `tools/test_report.py`.
- **`34dc0f0`** on `main`, 2026-10-19 — one specific reason may keep several named metadata
  sets (`020/440`). Delta paths: `tools/leakscan.py`, `tools/test_leakscan.py`,
  `tools/README.md`, `CHANGELOG.md` (the `020/440` entry).

**Read the whole PR, body-free.** List its commits by headline only:

```
gh pr view 97 --json commits \
  --jq '.commits[] | [.oid[0:7], .committedDate, .messageHeadline] | @tsv'
```

Keep the `--jq` filter: `--json commits` alone returns each commit's message body, and plain
`gh pr view 97` prints the PR body, the author's account. The four commits (`e72c142`,
`378399f`, `10b0bf6`, `8baace8`) are reachable in a local clone; read each, and the two `main`
commits, with `python3 tools/coldsweep.py --root . --commit <sha>` (subject, stat and diff,
never the body). Plain `git show` is barred: it prints the body before the diff, and reading is
atomic (rule 1). The pointer dates the original build 2026-10-03; the four commits carry
rebase dates. Check that the squash equals their sum (assumption 10), and review each delta path
at HEAD too. At brief
time no later commit touched a delta path; confirm with
`git log --oneline 34dc0f0..HEAD -- <the delta paths>`, and read any you find the same way.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Probe, at least:

- **The grace, on both sides of its boundary.** The cut-off is `BINARY_GRACE_UNTIL` in
  `tools/leakscan.py` (2026-11-18, UTC); its removal is tracked at board item `010/190`
  (`docs/roadmap/010-board-store-migration-per-item-files-mik/`,
  `190-remove-the-two-adoption-graces-after-their-date.md`). You may be running before or
  after that date. Either way, exercise the delta's behaviour on the day before the cut-off,
  on the cut-off and after it, by patching `_utc_today` (see the re-run list), and also under
  the real clock, saying which day that was. If the grace has
  already been removed from HEAD, extract the delta's tools from `34dc0f0` into your scratchpad
  (`git archive 34dc0f0 tools | tar -x -C <scratch dir>`) and exercise them there, and review
  the removal only as far as it bears on this delta. Test the claim that nothing a caller can
  pass (flag, env var, config key, floor `flags` or `scope`) moves, stretches or skips the
  window, on either plane.
- **The gate itself.** Which tracked binaries are gated on each plane (whole tree, staged,
  outside git); hash binding and re-blocking; stale entries; renames; `.leakscanignore` running
  first; `--disable`; the `suppressed:` accounting; exit codes, including a broken scan.
- **Metadata, set by set.** The walker for PNG, JPEG and WebP: what it sorts into each named set,
  what it reads and what it only detects, its size caps and its behaviour on malformed,
  truncated, oversized or hostile input. Judge the set-by-set and several-sets-per-line rules,
  and the refusal of a blanket reason, against the principal's words above.
- **The floor's refusals.** `forbidden_flags` and the dash-led `scope` refusal in
  `tools/floor.py`: whether every route that changes leakscan's mode or cover is refused, and
  whether anything real is refused by mistake, for every scanner the floor runs.
- **The doctrine.** The delta states an exception to E6a in `tools/README.md`, code comments and
  `CHANGELOG.md`. Check it against E6a's home, every mirror site (V3) and every decision record
  and board item that names G3 or PR #97 (sweep below), for one home (V4) and no contradiction
  (V5).
- **The adopting child repos on the machine.** Read-only, by count only, never by name: how many
  are wired to the floor, how many carry tracked binaries no entry accepts, how many lines
  `--binary-entries` would ask each to write, and whether every child's floor config still
  loads under the new `floor.py`. Say what the cut-off will do to them. Their file contents and
  names never enter the verdict.

**Non-goals:** G3's existence and its blocking shape (the principal's 2026-08-04 ruling), and
the field-by-field build tracked at `020/450`, except where the landed text or code claims more
than it does. Whether the landed docs and code describe the set-level design honestly against
his words is in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first, before the list
   below. Ask whether a dated warn-only window was the right way to honour both a blocking
   ruling and a no-advisory posture, and whether hash-bound manifest lines are the right unit
   for "a person looked".
2. **Correctness & quality.** Diff every commit. Run the probes live. Record each overclaim
   against the text that makes it (docstrings, `--help`, `tools/README.md`, `CHANGELOG.md`, the
   printed warnings and summary line).
3. **Completeness / harvest.** Every surface that states leakscan's posture or the floor's flag
   rules; the man page or stamp, if one is owed; tests that would stay green on a broken gate
   (mutate and re-run).
4. **Security & privacy** — mandatory, and the reason this pass exists. The gate is a privacy
   control, its parser reads untrusted binary input, and the floor shells out with child-supplied
   arguments: check parser robustness (resource exhaustion, decompression of compressed text
   chunks, length fields), argument and option injection (OWASP A03) and fail-open paths by
   hand. Ask what the required reasons themselves publish about a child's files. **Fixtures are a
   privacy surface in this PUBLIC repo:** confirm no tracked binary exists
   (`git ls-files --eol | awk '$1=="i/-text"' | wc -l`), then read every fixture byte string in
   `tools/test_leakscan.py`, `tools/test_report.py` and the `--selftest` code for real metadata —
   camera makes or serials, GPS, author or software names, real paths, real addresses. **Quote
   none:** locate by file and line, describe by class. Aim `/security-review` at the code diff
   only from a clean tree (see *House rules*); weigh a clean pass over markdown as nothing.

## Load-bearing assumptions to attack

Each is a falsifiable claim the delta makes or depends on; damage it with a probe or confirm it
by re-driving.

1. Before `BINARY_GRACE_UNTIL` the four G3 findings never change the exit code, and from it they
   block exactly as any leak does, on both planes.
2. No flag, environment variable, config key, floor `flags` entry or `scope` path can move,
   stretch or skip the grace or the gate.
3. Every other leakscan rule, including a personal-data hit in an image's text metadata, blocks
   during the grace.
4. A manifest line accepts only the exact bytes it was written for; any change re-blocks.
5. Every metadata set a PNG, JPEG or WebP carries is detected and named, and anything the walker
   cannot identify or read lands in `unknown` rather than passing.
6. Keeping one set never keeps another, and a blanket reason is refused.
7. Text metadata is still scanned by the normal rules whether or not its set is kept, and
   allow-markers inside metadata are ignored.
8. `forbidden_flags` refuses every argument argparse would expand to a forbidden mode, and
   refuses no legitimate flag of any atelier scanner.
9. The staged hook now gates every binary a commit adds, modifies or renames, and path-scans the
   names of binaries, empty new files and pure renames.
10. The 2026-10-03 build and the 2026-10-18 rework compose: nothing the rework replaced survives
    as a second path, and the squash equals its four commits.
11. The exception to E6a is stated once, bounded to the four G3 rules, dated, and recorded where
    E6a's posture lives.
12. No fixture in the delta carries real-world metadata.

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, from the worktree root at `6f78d85`,
on 2026-10-26 UTC, in the foreground; its results are held in the sibling. Read exit codes
explicitly. Check `uptime` first and run the heavy lines under `nice -n 10`.

- `python3 -m unittest discover -s tools -p test_leakscan.py`, and the same for
  `test_floor.py`, `test_allowmarker.py` and `test_report.py`
- `python3 tools/leakscan.py --selftest` and `python3 tools/floor.py --selftest`
- the full suite once: `nice -n 10 python3 -m unittest discover -s tools`
- the floor at HEAD: `nice -n 10 python3 tools/floor.py --plane ci --root .`, and `--plane hook`
- `python3 tools/leakscan.py --root . --binary-entries` (atelier's own tree)
- the grace boundary, live: in a throwaway git repo under your scratchpad holding one tracked
  synthetic PNG you build from bytes (a text chunk with harmless text is enough), run from the
  worktree root the loop printed after this list (add any later day you like), then
  `python3 tools/leakscan.py --root <scratch repo>` under the real clock
- the children, read-only and by count: `python3 tools/floorfleet.py --root <the directory that
  holds the main atelier checkout and its sibling clones> --json` to a scratch file; then, for
  each child it reports `wired` and not the parent, `python3 tools/leakscan.py --root <child>
  --binary-entries` (stdout only; count file lines and `<digest>:<set>` lines) and
  `python3 tools/floor.py --root <child> --plane ci --list` and `--plane hook --list` (exit codes
  only). Report totals, never a child's name or path
- `exiftool` was not installed on the brief-writer's machine. If yours has it, you may run it,
  by path, only over fixture bytes you write from the test module into your scratchpad; never
  over any file outside your worktree and scratchpad, and quote none of its output beyond tag
  names

The grace-boundary loop (the Python lines start at column 0 inside the quotes):

```
for D in 2026,11,17 2026,11,18; do
  python3 -c 'import sys, datetime
sys.path.insert(0, "tools")
import leakscan as ls
y, m, d = map(int, sys.argv[2].split(","))
ls._utc_today = lambda: datetime.date(y, m, d)
sys.exit(ls.main(["--root", sys.argv[1]]))' <scratch repo> "$D"; echo "$D exit $?"
done
```

## House rules for this run

- Name your own review worktree in the verdict; it is read-only to you except for THIS file.
  Other sessions may be live on this machine: touch nothing outside your worktree and
  scratchpad. Never open another `docs/reviews/` file before phase 2.
- No git command that writes in the worktree, beyond committing this one file at the end of
  each phase (or handing it to your orchestrator to commit). Read-only git is fine. Scratch
  repos, extracted trees, mutated copies and fixture files go under your session scratchpad,
  named by your prefix, and are deleted when you finish; never mutate the worktree's `tools/`.
- The child repos are read-only to you: no write, no git command that writes, no file copied
  out of them. Count only.
- One heavy process at a time; foreground, with a long timeout. Never run an installed tool by
  bare name from `PATH`: use `python3 tools/<x>.py` from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds and do the code-altitude
  read by hand — never with this brief or its sibling dirty.
- This pass is pending while you run it: anything you write to the session log, the pointer or
  a commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. Never
  quote a secret, a placeholder token, an email address, a child repo's name or any metadata
  value — this repo is PUBLIC, and a finding that repeats a leak is a second leak.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content —
the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only
after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/980-rule-4-cold-pass-queued-g3-grace-and-metadata-sets.md`,
this brief's sibling `docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.deferred.md`,
every delta commit's message body, PR #97's body, comments and reviews, and — beyond the quoted
spans the acceptance test prints — the intent records and the two records that follow them.
With `$P` for `docs/roadmap/020-policy-as-code-programme-five-tracks-mik` and `$Q` for
`docs/roadmap/010-board-store-migration-per-item-files-mik`:

- `$P/150-e7-residue-g3-binary-media-funded-as-its-own-i.md` (the intent record for `b5a2c53`)
- `$P/440-one-specific-reason-may-keep-several-named-metadata-sets.md` (the intent record for
  `34dc0f0`)
- `$P/450-g3-keeps-image-metadata-field-by-field-not-by-data-type.md`
- `$Q/190-remove-the-two-adoption-graces-after-their-date.md` (its first line, the title, may
  be read in phase 1)

The delta's own docstrings, comments, `tools/README.md` and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, setting `P` and `Q` as above first:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude \
  docs/roadmap/160-doctrine-review-owed/980-rule-4-cold-pass-queued-g3-grace-and-metadata-sets.md \
  --also-exclude docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.deferred.md \
  --also-exclude "$P/150-e7-residue-g3-binary-media-funded-as-its-own-i.md" \
  --also-exclude "$P/440-one-specific-reason-may-keep-several-named-metadata-sets.md" \
  --also-exclude "$P/450-g3-keeps-image-metadata-field-by-field-not-by-data-type.md" \
  --also-exclude "$Q/190-remove-the-two-adoption-graces-after-their-date.md" \
  '<pattern>'
```

For the reconcile surfaces, the pattern is `'\bG3\b|#97\b'`. `--include-barred` only with
disclosure in the verdict.

## Process

**Phase 1.** Read the acceptance test; reproduce the floor first; work the lenses, the probes,
the assumptions and the re-run list. Append your verdict below a `---` divider in THIS file:
provenance repeated (how you were spawned, your tier, what you read, the UTC day you ran on and
which side of the cut-off that is), per-lens answers, the standing checklist V1–V7 each answered
or discharged with grounds, each numbered assumption damaged or confirmed with its probe, a
per-commit ledger (the four PR commits and `34dc0f0`: read body-free yes/no, findings by id),
findings with stable IDs (prefix `GM`: `GM1`, `GM2`, …) and severities (MAJOR / MODERATE /
minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger
(commands and results, children by count only) and a follow-up checklist. Then STOP and commit
phase 1 unrevised before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling and the barred records; screen the delta's commit bodies and PR
#97's body and comments; append `### Reconcile` beneath your verdict: per-finding notes against
the sibling's questions and the authors' account, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Then fold the sibling in below
the reconcile and delete it.

The code is a guard and the guard is doctrine by function, so every finding is the principal's
to decide (rule 3): record all, apply nothing. Counsel per finding is welcome, labelled as
counsel and kept beneath it.

---

## Verdict — phase 1 (cold, act 1)

### Provenance, repeated

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`); tier checked at selection against rule 4's
  named tier. Spawned by headless orchestrator session `358c8aa0` (Opus 5.5), itself started
  by session `c87c4ee0` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the
  context partition, form no finding and write no severity, and neither authored the delta or
  the brief. The reviewer was not started or instructed by the barred sessions `8e498ef1` (or
  its workers) or `5070f22b` (or its subagents). The pass runs under the principal's
  2026-11-02 NZDT drain approval for Fable work.
- **Review worktree:** `/Users/mike/worktrees/fable/atelier-160-980-1248/atelier` at
  `452a3e1`, read-only to the reviewer except this file. Its `git status` shows one expected
  pending change: the deferred sibling removed on purpose by the orchestrator (the partition).
  That pending deletion is why `git diff` and `/security-review` were not run here (below).
- **Run day:** 2026-11-01 UTC (`date -u`), which is **before** the 2026-11-18 cut-off, by 17
  days. The real-clock runs below therefore exercise the grace side; the other side was
  exercised by patching `_utc_today`.
- **What was read:** this brief whole; `docs/method/REVIEW.md` whole; the six delta commits
  body-free through `tools/coldsweep.py --commit` (`e72c142`, `378399f`, `10b0bf6`, `8baace8`,
  `b5a2c53`, `34dc0f0`; subject, stat and diff only; no message body); every delta path at
  HEAD (`tools/leakscan.py`, `tools/floor.py`, `tools/allowmarker.py`, `tools/README.md`, the
  four test modules, `CHANGELOG.md`); supporting code the delta calls (`tools/report.py`,
  `tools/filewalk.py`, floor's registry and `_render`); `docs/method/SECRETS.md` from line
  186; `docs/method/GUARDS.md` §§ *Acceptance and deferment*, *Who may move a deferment's
  date*, *Who, why, when*, *Adoption*; ADR 0008 lines 66–74 and 196–204; ADR
  `2026-10-03-0641` lines 1–20 and 60–115; board items `020/140` (lines 1–60), `020/410`
  whole, `110/100` lines 96–112, `300/020` lines 86–92 and 128–136, `010/170` lines 20–34;
  the first line of `010/190`; `.github/workflows/ci.yml` and `floor.yml` (Python pin only);
  PR 97's commit headlines, dates and merge state through `gh pr view 97 --json` with a `jq`
  filter (no body, comment or review); the principal's quoted spans printed by the
  acceptance test and nothing else of `020/150`, `020/440`, `020/450`.
- **Not read:** the deferred sibling, the queue pointer, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md`, any prior verdict, any commit message body, PR 97's body, comments
  or reviews, and the three intent records beyond the printed spans. Every sweep ran through
  `coldsweep` with the brief's exclusion list; no `--include-barred` sweep ran. One exposure
  to disclose: the orchestrator's dispatch instructions and the harness's user-level and repo
  instruction files loaded as usual, which carry private context this verdict does not use.

### The acceptance test, printed

The brief's command printed, from `020/150`: the option labels *"Grace period (Recommended)"*
and *"Allow with reason (Recommended)"*, and the PS *"that reason for the image metadata must
be specific to the sets of metadata it wants to keep. It should only keep the metadata it has
a need for"*. From `020/440`: *"I am fine with one reason applying to multiple fields of
metadata, but it should be specific e.g. fields A, B, and C allowed because of X"* and *"I did
mean fields as in GPS versus the camera model. Things like exif, iptc, xmp are data types, nto
fields"*. From `020/450`: the same two sentences, the first ending *"Put it on the board to do
in a future session"*. The 2026-08-04 ruling that G3 blocks and the 2026-08-09 funding are
cited by the delta (README, code comment) but no verbatim record of either exists outside the
barred paths: a `coldsweep` for `2026-08-04` over the open tree returned no line naming
binaries, media or G3. Checked at phase 2 against the intent record.

### Lens 1 — approach and assumptions

**Load-bearing assumptions the reviewer named before reading the brief's list.**
(A) The grace is decided only by `_utc_today() < BINARY_GRACE_UNTIL`, and no route through the
floor's `flags` or `scope` keys, or leakscan's own CLI, changes the *effective* result,
including routes that make the scan run over nothing. (B) The floor relays leakscan's grace
warning to the person on both planes, or "warn then block" is in truth "silent then block".
(C) `_looks_binary` and git's binary verdict agree closely enough that hook and CI gate the
same files. (D) The principal's words quoted as the authority are his, not the author's option
text. (E) The data-type "sets" are presented honestly against his 2026-10-19 clarification that
exif, iptc and xmp are data types, not the fields he meant. (F) Metadata the code classes into
a text set is in fact decoded and scanned.

Outcome: A confirmed on every route probed (ledger below). B confirmed live on both planes
(the warning block reaches the floor's output, exit 0). C holds (`_looks_binary` is a NUL in
the first 8,192 bytes; git uses 8,000). D damaged (GM1). E damaged (GM3). F damaged for one
shape (GM4).

**Was a dated warn-only window the right way to honour a blocking ruling and a no-advisory
posture?** It is the least-bad shape given `020/410`: a guard with no advisory form cannot
adopt advisory-first at repo granularity, so the only alternatives were (i) force 125 file
acceptances across the fleet in the commit that floats the pin, or (ii) a per-repo deferment
form, which E6a forbids and `floor.py` refuses. A single dated, flagless, parent-side window
keeps the no-advisory invariant in the floor's registry (probed: `advisory: leakscan` is still
refused) and makes the softening visible in every run's output. The design is sound; what is
not sound is where it is *recorded* (GM2) and what its date's kind is (GM7). The grace is also
exactly the "deferment at repo granularity, with a reason and an expiry" GUARDS § *Adoption*
describes, lifted to fleet granularity, and no doctrine says so (GM11).

**Are hash-bound manifest lines the right unit for "a person looked"?** For the file, yes: the
digest binds the attestation to the bytes, a changed file re-blocks (probed), a rename names
its old entry (probed on both planes), and the reason sits where a reviewer reads it. For
metadata, the unit is a *data type*, which is what the principal said is the wrong unit
(`020/450`); the landed text does not say so (GM3). The manifest records a reason but not who
or when, which the principal's 2026-10-03 words (quoted in ADR `2026-10-03-0641`) ask of every
exception (GM5, provisional).

### Lens 2 — correctness and quality

What the delta claims, it does, on every probe below, with these exceptions recorded as
findings: a text set that is not decoded (GM4); a no-match entry that is not reported stale
(GM6); and four sentences that claim more than the code does (GM1, GM8, GM9, GM10). The
blanket-reason refusal is textual equality: a set line whose reason differs from the file
line's by one character loads (probed, L2). That is what the README says it does ("may not
repeat the file line's own reason"), so it is not an overclaim, but the guard catches the
copied-stanza shape only; the human's judgement is the control, and the text should say so
(folded into GM14).

### Lens 3 — completeness and harvest

Mirror sites of leakscan's posture (sweep `advisory form`, `\bG3\b|#97\b`, `2026-11-18`,
`leakscanbinaries`, `four mode|five mode|FORBIDDEN_FLAGS`): `docs/method/SECRETS.md` §
posture, ADR 0008 (two sites), board `300/020` (row for `020/150`), `020/410`, and floor's own
docstring and comments. Of these, SECRETS.md, ADR 0008 and `300/020` still state the
unqualified "no advisory form" (GM2); floor's line-1441 comment still counts four forbidden
flags (GM10). No man page exists for leakscan (`instruments/man/` holds the `cc*` tools only),
so none is owed. Tests that would stay green on a broken gate: none found. Thirteen mutations
of a copied `tools/` tree each failed at least one delta test (ledger); the one gap the
mutations cannot reach is the raw-profile `xmp` branch, which no test pins either way (GM4).

### Lens 4 — security and privacy (mandatory)

- **`/security-review`: discharged with grounds.** The scanner reads the session's pending
  diff. In this worktree that diff is the deliberately removed deferred sibling (a scan would
  print its content into the reviewer before act 2, the SL2 shape) and this brief; the delta
  itself is landed, not pending. The code-altitude read was done by hand instead, below.
- **Injection (OWASP A03).** Every `subprocess.run` in the delta is an argv list with no
  shell: `git -C <root> ls-files -z`, `git diff --cached -z …` with fixed options, `git
  cat-file blob :0:<path>` where `<path>` comes from git's own NUL-separated output and the
  `:0:` prefix stops it reading as an option. Child-supplied `flags` reach the scanner only as
  separate argv tokens after the template; the forbidden-prefix test refuses `--b…`, `--se…`,
  `--w…`, `--j…`, `--ch…` for every scanner (probed, including `--`-then-flag and a flag aimed
  at a different scanner); a dash-led `scope` path is refused; `./--binary-entries` as a scope
  path fails closed as a missing directory; a short `-b` is an argparse usage error (exit 2).
  No legitimate flag of any atelier scanner is a strict prefix of a forbidden one (inventory
  of every `add_argument` across `tools/`: the only short option in the tree is coldsweep's
  `-i`).
- **Parser robustness.** 48 synthetic inputs (PNG, JPEG, WebP, GIF, TIFF, empty): header-only
  files, missing IEND, a 4 GiB chunk length, lengths past EOF, segment length 0 and 1, a
  stuffed `FF 00` before SOS, one million RST markers (0.50 s), one million fill bytes
  (0.39 s), 200,000 zero-length chunks (0.24 s), a zlib bomb of 200 MiB inflating to the 1 MiB
  cap (opaque, 0.00 s), truncated iTXt, garbage zTXt, segments at and past the cap, an
  extended-XMP segment shorter than its 40-byte header, a WebP whose RIFF size exceeds the
  file and one whose RIFF size is zero. None raised, none hung, every malformed shape landed in
  `unknown`. Peak memory is bounded by the 1 MiB segment cap and JPEG's 64 KiB segment limit,
  as the docstring claims.
- **Fail-open paths.** An unreadable file blocks (`binary-unlisted`); a manifest that does not
  parse or lacks a reason is exit 2 on both planes, grace or not (probed); a git failure in
  `tracked_files` gates every binary; a `git cat-file` failure on the hook is exit 2; findings
  past the materialisation cap stay blocking during the grace (code read; not probed at
  50,000 findings).
- **What the required reasons publish.** `.leakscanbinaries` is a text file at the repo root,
  so its reasons and paths run through every leakscan rule like any other line (the file is
  not special-cased in `iter_files`; probed implicitly by the scratch runs). A reason that
  describes a photo's subject is a disclosure the human chose to make in a public tree, which
  is the design: the README's own examples model the right register.
- **Fixtures.** `git ls-files --eol` lists 0 tracked binaries at HEAD. Every image in
  `tools/test_leakscan.py` and `--selftest` is built from bytes at run time; every digest is
  computed, never literal. Byte strings read (by class, none quoted): reserved-domain mailbox
  addresses, a private-range IPv4 in a filename, a public software project's website as a
  `Software` tag, the standard APP13 and XMP namespace signatures, synthetic profile bytes. No
  camera make, serial, GPS, author, real path or address. `test_report.py` adds no bytes.
  Assumption 12 confirmed.
- **Design-altitude threat enumeration.** The delta enumerates its threats in comments (bomb,
  caps, listing-mode bypass, abbreviation, dash-led scope, markers inside metadata) rather
  than in one place; adequate for its class, and no gap was found beyond GM4.

### The standing checklist V1–V7

- **V1 — no claim stronger than its evidence:** GM1 (authority text), GM3 (set-level honesty),
  GM4 ("text sets are still scanned"), GM8 (`_render` "never displace"), GM9 ("the only ways to
  skip the gate"), GM10 (stale counts and "after").
- **V2 — every recorded live-proven claim re-run:** all re-run (ledger). All reproduce except
  the two the findings above record.
- **V3 — a changed rule swept to every mirror site:** GM2 (E6a's home, ADR 0008, `300/020`),
  GM10 (floor comment).
- **V4 — one fact, one home:** GM2: the exception is stated in three tool-level sites and at
  no doctrine home.
- **V5 — no internal contradiction:** GM2 (SECRETS.md vs README), GM3 (the quoted words vs the
  same-day clarification), GM7 (GUARDS "names its kind" vs an unkinded date), GM10 (CHANGELOG
  "after" vs code "on and after"), GM11 (GUARDS § Adoption vs `020/410`).
- **V6 — security and privacy:** lens 4 above; GM4 is the one security finding and carries a
  severity and a recurrence step.
- **V7 — rule-4 provenance in brief and verdict:** the brief states it (§ *Spawn provenance*);
  repeated above.

### The twelve assumptions, damaged or confirmed

1. **Confirmed.** Patched-clock loop on the scratch repo: 2026-11-17 exit 0 with both G3
   findings as warnings; 2026-11-18, 2026-11-19 and 2027-01-01 exit 1 with the same two
   findings blocking. Hook plane: the delta's own staged test on `_BEFORE`/`_CUTOFF` plus a
   live hook-plane floor run (exit 0, warning relayed). JSON: `clean: true`, `findings: []`,
   `binary_grace.active: true` with both warnings listed, and the `where` field present.
2. **Confirmed on every route probed; one docstring falsified (GM8).** Refused or failing
   closed: `--binary-entries`, `--binary`, `--bin`, `--b`, `--self`, `--war`, `--js`, `--chec`,
   `--binary-entries=yes`, `--` then `--binary-entries`, `--binary-entries` on another
   scanner, `scope` paths `-x`, `--bin`, `./--binary-entries`, an empty directory, `advisory:
   leakscan`, `--disable=<any G3 rule>` (exit 2), `-b` (exit 2), `--staged` and `--st` on the
   CI plane (exit 2: absolute positional refused in staged mode), `--grace-until`, `--grace`,
   `--today` (exit 2). No env var or config key reaches `_utc_today`. Accepted with a `why`
   and running: `--root <elsewhere>` and `--terms /dev/null`, which displace the template's
   values (probe Q2) but gate *more*, not less; and, by design and visibly, a reasoned
   `.leakscanignore` glob (GM9).
3. **Confirmed.** An email in a PNG `tEXt` chunk blocked (exit 1) on the real clock during the
   grace, with the file's own G3 findings printed as warnings above it; the delta's test
   `test_a_text_metadata_hit_still_blocks_during_the_grace` pins it.
4. **Confirmed.** `test_a_changed_binary_blocks_again` and the hook's index-copy test; mutation
   `hash-always-matches` failed four tests; the live scratch run with a one-byte change
   re-blocked.
5. **Damaged for one shape (GM4).** Every set is detected and named (the delta's
   `test_inspect_media_names_each_set` covers all seven, and the 48-input probe agreed), and
   everything unidentifiable landed in `unknown`. But an ImageMagick raw `xmp` profile is
   named `xmp` and never read, so "detected and named" holds while "text set, scanned" does
   not.
6. **Confirmed.** Keeping `icc` left `exif` blocking by name (test and probe); a shared stanza
   over file and set lines is refused as a blanket (probe L1, exit 2); `34dc0f0`'s comma form
   names each set explicitly, with no wildcard (`:icc,` and `:icc,icc` refused).
7. **Confirmed, with the GM4 exception.** Kept `png-text`, `xmp` (packet forms) and
   `jpeg-comment` are scanned; a marker inside metadata is read as text (probe and mutation
   `markers-honoured-in-metadata`, one test failed).
8. **Confirmed.** Inventory of every long flag across `tools/*.py`: none is a strict prefix of
   a forbidden flag, so the prefix test refuses nothing real; `--disable ipv4` and
   `./-odd-dir` still parse (delta test). Mutation `forbidden-exact-match` failed ten tests.
9. **Confirmed.** Staged binary added (blocks, name read), modified in the index only
   (`binary-changed`), removed (`binary-stale-entry`), renamed by `git mv` (stale entry plus
   `binary-unlisted` naming the old entry, probe N), pure text rename (name read), a text file
   under a `binary` attribute (read in full), an empty new file (name read; code path). A
   tracked symlink to a binary outside the repo is gated on neither plane (probe O): nothing of
   it but the link text reaches a remote, so this is consistent, not a gap.
10. **Confirmed.** `git diff b5a2c53 8baace8` is empty (the squash tree equals the branch tip,
    same base `4afe5ea`); `34dc0f0` applies on top. The first build's `:binary-metadata` scope
    and `SCOPE_METADATA` survive only as a refused-set test; `grep` at HEAD finds no leftover.
    No commit after `34dc0f0` touched a delta path.
11. **Damaged (GM2).** The exception is stated three times (README, code comment, CHANGELOG),
    bounded to the four rules and dated in each, and recorded at **no** doctrine home: E6a's
    posture paragraph in `SECRETS.md` is unchanged and unqualified.
12. **Confirmed** (lens 4).

### Per-commit ledger

Each read body-free through `coldsweep --commit` (subject, stat, diff; never the message body).

- `e72c142` leakscan: block unread binaries until a hash-bound reasoned entry accepts them —
  findings GM4 (the raw-profile early return), GM5, GM6, GM12.
- `378399f` floor: refuse leakscan's `--binary-entries` through a child's flags — GM8 (the
  blocklist rests on "never displace").
- `10b0bf6` leakscan: G3 warns until 2026-11-18, and keeps metadata only set by set — GM1,
  GM2, GM3, GM4 (`xmp` named a text set), GM7, GM9, GM11.
- `8baace8` floor: refuse abbreviated mode flags and dash-led scope paths — GM8, GM10 (the
  comment left at "four").
- `b5a2c53` the squash of the four (tree equals their sum) — GM10 (CHANGELOG "after"), GM13.
- `34dc0f0` one specific reason may keep several named metadata sets — GM3 (the "fields A, B,
  and C" quote as the authority for data-type sets), GM14.

### Findings

Severities: MAJOR / MODERATE / minor / note. Every finding is the principal's to decide
(rule 3): recorded, nothing applied. Counsel is labelled and kept beneath each.

**GM1 — MODERATE — author-written option text is quoted as the principal's words, and named
the authority for the exception.** `tools/README.md` (the paragraph "The adoption grace, until
2026-11-18") renders *"unlisted files print a warning naming a cut-off date (~30 days), then
start blocking…"* in the house form for his verbatim words, and `tools/leakscan.py`'s grace
block says "Mike's answer on 020/150 … chose to land G3 with a grace period: "unlisted files
…"" and "That answer is the authority for this exception". The acceptance test printed his
words in `020/150`: the labels *"Grace period (Recommended)"* and *"Allow with reason
(Recommended)"* and the PS. The quoted sentence is not among them; the brief says the option
text around the labels is the author's. The decision is his; the sentence is not, and the
"~30 days" inside it is the author's number that his label adopted. Reconciled at phase 2
against the record's text. *Counsel:* in all three sites, cite the label he chose and attribute
the option text to the queue run, e.g. "Mike chose the option labelled *"Grace period
(Recommended)"*; the option's text, the queue run's, read: …".

**GM2 — MODERATE — the one exception to E6a is recorded at no doctrine home.** E6a lives in
`docs/method/SECRETS.md` § *The boundary's posture* (line 234: "`leakscan` gains no advisory
form, and that asymmetry is now decided rather than incidental"), which the delta did not touch.
The same paragraph rules that a narrowing is "recorded where they will meet it — the roadmap
or an ADR … never let the code comment be the record". The grace is stated in `tools/README.md`,
a `leakscan.py` comment and `CHANGELOG.md` only. ADR 0008 (lines 70–71) and board `300/020`'s
row for `020/150` ("No advisory or dated form") still state the unqualified posture, so the
tree contradicts itself for the 31 days the window is open. Assumption 11's "recorded where
E6a's posture lives" is false. *Counsel:* one dated sentence in SECRETS.md § posture naming
the four rules, `BINARY_GRACE_UNTIL` and `010/190`, with the three tool sites stamped as
copies; a one-line note on `300/020`'s row.

**GM3 — MODERATE — the set-level design is described as meeting his words while omitting his
same-day correction of the unit.** `tools/README.md`, `CHANGELOG.md` (the `020/440` entry) and
the `leakscan.py` G3 comment quote *"I am fine with one reason applying to multiple fields of
metadata, but it should be specific e.g. fields A, B, and C allowed because of X"* as the
authority for comma-joined *sets* (`:icc,xmp`). His next sentence in the same record, printed
by the acceptance test, is *"I did mean fields as in GPS versus the camera model. Things like
exif, iptc, xmp are data types, nto fields. Put it on the board to do in a future session"*.
None of the three sites says the sets are data types, that the field-level keep he asked for
is owed, or points at `020/450` (grep: no `450` and no "data type" in any delta path). A
reader of the README is told the manifest keeps "exactly those sets" the person needs; the
principal has said that is not the granularity he meant. The field-by-field build is the
brief's non-goal; the honesty of the landed text about it is not. *Counsel:* one sentence in
each site: "These sets are data types (Exif, XMP, …); the field-level keep he asked for — GPS
versus camera model — is `020/450`, not built."

**GM4 — MODERATE (security) — a metadata shape classed as a text set is never decoded or
scanned.** `_png_text_chunk` maps a PNG text chunk whose keyword begins `Raw profile type` to a
set by kind and returns before any decoding; for kind `xmp` the set is `xmp`, which
`METADATA_SETS`, `tools/README.md` ("`png-text`, `xmp` and `jpeg-comment` are decoded and run
through the normal rules and term list, kept or not") and the G3 comment all call a text set
that the scan still reads. The payload is ImageMagick's hex dump of the XMP packet, decodable
with `bytes.fromhex` after stripping whitespace. Probe: the same reserved-domain address
produced an `email` finding in an iTXt XMP packet, a zTXt XMP packet, a JPEG XMP segment and
a WebP XMP chunk, and **no finding** in a raw-profile `xmp` chunk, compressed or not. Effect:
the set still blocks by presence, so nothing passes silently, but a person who keeps it with a
`:xmp` line is told the scan read it when it read nothing, and after the cut-off a kept raw
profile carrying a creator, a description or GPS in XMP form is published unscanned. The
README's "What it can't see" list does not name it. *Recurrence step (counsel):* decode the hex
for kind `xmp` and scan it like the other XMP forms, or class the raw `xmp` profile as
`unknown` and say so in the table; pin either with a test (no test reaches this branch, so
the mutation ledger could not).

**GM5 — MODERATE, provisional — the manifest records a reason only, against a verbatim
requirement and a recorded hold.** ADR `2026-10-03-0641` quotes the principal, 2026-10-03:
every exception is "recorded so that its clear that the exception exists, why it is necessary,
who created it (e.g. session transcript ID, did I rule or did you do it automatically etc),
when the exception was granted"; its § *Consequences* says "G3 (PR #97) is reworked onto this
register as `file` entries"; board `110/100` says "G3 (PR #97) is held until it meets (1)
and (2)". `.leakscanbinaries` lines carry a reason and nothing else; GUARDS § *Who, why, when*
defers who and when to git, which the ADR's part 1 measured as unable to name a session or a
ruling. Whether `020/150` records the hold lifted by his word, or *"Allow with reason
(Recommended)"* was put to him with that trade stated, is barred until phase 2; if it was, this
reduces to a note that the delta's text should cite the lift. *Counsel:* if not lifted, the
`--binary-entries` printer can emit the session id and date into each stanza at no cost to the
grammar.

**GM6 — minor — a manifest entry that can match nothing is silently inert, against the
README's claim.** `tools/README.md`: "An entry that accepts nothing blocks as
`binary-stale-entry`". Probe K: an entry whose path is absolute loaded without error and
produced no stale finding (`root / "/etc/x"` resolves outside every scanned path, and the stale
loop `continue`s on `_under_any`). The same holds for a `../x` path. Neither can accept a
repo-relative file, so the gate is unharmed; the inventory is wrong without saying so.
*Counsel:* refuse absolute and `..` paths at load as a config error, the floor's
`_reject_escaping_scope` shape.

**GM7 — minor — the fleet-wide date names no kind.** GUARDS § *Who may move a deferment's
date* carries the principal's 2026-08-09 rule and concludes "a ruling that sets a date for the
fleet names its kind" (mandate or default). The delta states the day "was the queue run's pick
… not a ruling" and builds it so no child can set an earlier or later date; under his rule a
mandate still lets a child argue for an exemption through its parent, and the delta names no
route. *Counsel:* the principal says which kind 2026-11-18 is (an owed ask below), and the
README states it in one line.

**GM8 — minor — `_render`'s "never displace" is false, and the refusals are carried by other
guards than the docstring says.** `floor.py` `_render`: "A child's extra `flags` are appended
LAST, so they can add to the template's arguments but never displace them." For a repeated
store option argparse keeps the last value. Probe Q2: `--root <repo> <repo> --root
<nonexistent>` through the same shape read the manifest from the nonexistent root (the listed
file turned `binary-unlisted`). `--terms /dev/null` likewise ran. `--staged` on the CI plane
fails closed only because leakscan refuses an absolute positional in staged mode, not because
the template held. All three displacements gate more, not less, so no bypass follows; the
docstring is the overclaim, and `8baace8`'s prefix test is sound on its own. *Counsel:* reword
the docstring; consider `--root`, `--terms` and `--staged` for `FORBIDDEN_FLAGS`, since each
changes what the check reads, not where it looks.

**GM9 — minor — "Those were the only ways to skip the gate" overclaims.** `tools/README.md`
line 382. A reasoned `.leakscanignore` glob skips the gate for a path (the same README says so
twenty lines earlier, and counts it), and a reasoned floor `scope` narrowing skips it for
everything outside the scope. Both are visible and on the record by design; the sentence
should say the *quiet* ways. *Counsel:* "the only unrecorded ways".

**GM10 — minor — stale text left by the rework.** (a) `floor.py` line 1441, in the `flags`
validation: "it stops the four arguments we know weaken a check" — the delta made it five and
updated the selftest comment and `test_floor`'s docstring, not this one. (b) `CHANGELOG.md`
`020/150` entry: "**After 2026-11-18** the same findings block" — the code blocks *on* that day
(`<`, confirmed on the day itself), as the README's "From that date" says. *Counsel:* two
one-word edits.

**GM11 — note — the grace is the adoption-time deferment `020/410` says a no-advisory guard
lacks, and no doctrine says so.** GUARDS § *Adoption* still reads "the guard installs
advisory-first, with a reason and an expiry"; `020/410` is open with the question "whether E6a
gets an adoption-time exception" and says it "is the first decision in PR #97". The delta is
that decision in code and leaves the item and the section unchanged. *Counsel:* a line on
`020/410` recording that the grace answered it for G3, and whether the shape generalises is
the principal's.

**GM12 — note — the hook reads `.leakscanbinaries` from the working tree, not the index.**
Same shape as `.leakscanignore` (pre-existing), so a commit whose manifest edit is unstaged
passes the hook and fails CI, or the reverse. Fail-closed on CI either way. *Counsel:* read
the index copy when the manifest is itself staged.

**GM13 — note — the delta's tests need Python ≥ 3.11.** `BinaryGitTracking.staged` uses
`contextlib.chdir`; CI pins 3.12, so CI is unaffected. On this machine the system
`/usr/bin/python3` (3.9) errors on seven delta tests (and, pre-existing, on `test_floor` and
`test_allowmarker`); all pass on 3.14. The tools themselves run on 3.9 (both selftests pass
there). *Counsel:* one line in `tools/README.md` naming the test floor.

**GM14 — note — two guards weaker than a reader may assume, honestly stated.** The blanket
refusal is textual equality (a one-character difference loads, probe L2); and the JPEG walker's
cost is linear in the length of a degenerate marker stream (one million RST markers, 0.50 s),
bounded but unbudgeted. Neither is a defect against the text; both are worth one sentence
each.

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 5 MODERATE · 5 minor · 4 note (14).** The gate, the grace
and the floor's refusals do what the delta claims on every live probe and every mutation; the
findings are about what the text records and attributes (GM1–GM3, GM5), one unscanned text
shape (GM4), and small overclaims. No MAJOR, so under REVIEW.md's close rule the cycle closes
on the principal's decisions without a further ceremony, unless phase 2 moves GM5.

### Re-run ledger

All from the worktree root at `452a3e1`, 2026-11-01 UTC, foreground, one heavy process at a
time, `nice -n 10` on the heavy lines; `uptime` load 5–11 throughout. Interpreters by absolute
path: `/usr/bin/python3` (3.9.6) and `/usr/local/bin/python3` (3.14.6; CI pins 3.12).

- `unittest discover -s tools -p test_leakscan.py` (3.14): 219 tests OK, exit 0. Same for
  `test_floor.py` (150 OK), `test_allowmarker.py` (31 OK), `test_report.py` (71 OK). The four
  on 3.9: 7 + 1 + 9 errors, all interpreter-version (GM13); `test_report` 71 OK.
- `leakscan.py --selftest` and `floor.py --selftest`: OK on 3.9 and 3.14; floor reports 16
  scanners, 0 failures.
- Full suite (3.14) under `nice -n 10`: 2,032 tests OK in 502 s, exit 0 (on 3.9: 1,752 ran, 20
  version errors).
- `floor.py --plane ci --root <worktree> --list` and `--plane hook --list`: plan listed, exit
  0. The whole-tree floor runs were made on the scratch repo (below), because a hook-plane run
  in this worktree reads its staged diff.
- `leakscan.py --root <worktree> --binary-entries`: "0 entries to review", exit 0;
  `git ls-files --eol` shows 0 tracked binaries.
- Grace loop on a scratch git repo holding one tracked synthetic PNG with a `tEXt` chunk:
  2026-11-17 exit 0 (2 warnings); 2026-11-18, 2026-11-19 and 2027-01-01 exit 1.
- Same tree on the real clock (2026-11-01): exit 0, 2 warnings, the summary line counts "2 G3
  finding(s) warned"; `--json` gives `clean: true`, `active: true`, both warnings listed.
- An email in a `tEXt` chunk, real clock: exit 1 (`email` blocks), G3 warnings printed above.
- `floor.py --plane ci --root <scratch> --tools <worktree>/tools`: exit 0, leakscan's warning
  block appears in the floor's output. `--plane hook` with the PNG staged: exit 0, relayed.
- 13 floor config variants (assumption 2): every bypass route refused or failing closed; two
  displacements accepted and gating more.
- 48 hostile and edge media inputs (`gm_media_probes.py`): 0 exceptions, 0 hangs, every
  malformed shape lands in `unknown`; the raw-profile `xmp` chunk is unscanned (GM4).
- 13 mutations of a copied `tools/`: each failed at least one delta test (1 to 12 per
  mutation).
- `test_leakscan.py` under a 2027-01-01 clock, patched before discovery: 219 OK, so the suite
  is clock-independent.
- Hook plane, `git mv` of a listed binary: `binary-stale-entry` plus `binary-unlisted` naming
  the old entry.
- `exiftool`: NOT RUN, not installed at `/usr/local/bin` or `/opt/homebrew/bin`.
- The children, read-only, counts only: `floorfleet.py --atelier <main checkout> --root <its
  parent> --json`, then per wired child `leakscan.py --root <child> --binary-entries`,
  `floor.py --root <child> --plane ci --list` and `--plane hook --list`. 23 repos listed; 21
  wired children excluding the parent; `--binary-entries` exit 0 on all 21; **3 children carry
  owed lines, 125 file lines and 43 set lines in total** (68/0, 50/43, 7/0); 18 carry none;
  the floor config loads on both planes for 21 of 21.

**What the cut-off does to them:** on 2026-11-18 UTC the three children with owed lines go red
on their next CI run (whole-tree) and on any hook commit that stages a binary, unless they
list or strip first; the other eighteen see no change. For comparison `020/410` counted 152
files across 7 children on 2026-10-03.

Scratch artefacts (repo, extracted copies, mutant trees, probe scripts) live under the session
scratchpad and are deleted at the end of act 2.

### Follow-up checklist

- [ ] GM1–GM14 to the principal under rule 3; nothing applied by this pass.
- [ ] Phase 2: reconcile GM1 and GM5 against `020/150`'s text (does the option text match the
      quoted sentence; was the `110/100` hold lifted by his word); reconcile GM3 against
      `020/440` and `020/450`; read the sibling, the pointer, the commit bodies and PR 97's
      body and comments; restate the overall line.
- [ ] ⏳ Owed asks for the principal, put on the board rather than asked mid-drain: (a) is
      2026-11-18 a mandate or a default for the children (GM7); (b) decode or declare-opaque
      for the raw `xmp` profile (GM4); (c) whether `.leakscanbinaries` must record who and when
      per his 2026-10-03 words, or the reason-only form stands (GM5).
- [ ] `010/190` removes the grace after the date; this pass found nothing that changes that.
- [ ] Trace the 2026-08-04 ruling's verbatim words at phase 2 (none in the open tree).
