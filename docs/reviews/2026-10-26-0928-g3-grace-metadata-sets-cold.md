# Cold pass — G3: binaries gated with a dated grace, metadata kept set by set, floor flag refusal

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes the pass. The principal's current standing ruling is that no Fable work runs
without his explicit permission, so this pass waits for that permission as well.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-26 UTC by an Opus 5.5
brief-writer subagent of session 5070f22b; the pass waits for a cold Fable session that neither
the delta's authors nor session 5070f22b (nor any of its subagents) started or instructed.
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
