# Cold pass — the staged-positional reader the three staged-diff guards share

**Pass type:** code cold pass, doctrine by function, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes the pass. The principal's current standing ruling is that no Fable work runs
without his explicit permission, so this pass waits for that permission as well.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-26 UTC by an Opus 5.5
brief-writer subagent of session 5070f22b; the pass waits for a cold Fable session that neither
the delta's authors nor session 5070f22b (nor any of its subagents) started or instructed.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/950-rule-4-cold-pass-queued-staged-positional-reader.md`.
**Why it earns a review:** the three boundary guards (`leakscan`, `secretscan`,
`conflictscan`) in `--staged` mode are a silent-failure surface. A clean `--staged` scan is read
as "nothing barred was staged", by the pre-commit hook, by the floor's hook plane and by any
session that runs one by hand and cites it. The worst failure is a positional that filters the
staged set to nothing, or to less than its spelling says, while the scan still prints clean: a
false negative that manufactures confidence in every commit it covers, in atelier and in every
child repo that runs the same scanners from `floor.yml@main`.

## Spawn provenance

- **Author of the work under review:** a Mike-opened Opus 5.5 queue run, session `8e498ef1`,
  2026-10-18, and the Sonnet worker it dispatched, which wrote the code (the queue pointer's
  account; the brief-writer did not verify which hand wrote which line). Barred from taking
  this pass: session `8e498ef1` and every worker it dispatched.
- **Who wrote this brief:** an Opus 5.5 subagent (`claude-opus-5-5`) dispatched on 2026-10-26
  by session `5070f22b`, a headless Opus 5.5 brief-writing session started on the principal's
  instruction to have every queued brief ready for a reviewer. Neither session `5070f22b` nor
  this brief-writer authored any of this delta. It is **off-tier for review, disclosed: it forms
  no finding and writes no severity**, and it stops after this brief and its sibling. Barred
  from taking this pass: session `5070f22b` and every subagent it dispatched, this one included.
- **Who takes the review:** a further cold Fable session, not yet started, that passes rule 4's
  criterion. If it runs as reviewer-plus-orchestrator, rule 4's off-tier conditions apply and
  are disclosed in the claim, the pointer and the verdict. The reviewer repeats its own
  provenance in its verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This brief-writer read: its
  dispatch prompt and a common instruction file from session `5070f22b`;
  `skills/review-brief/SKILL.md` whole; `docs/method/REVIEW.md` lines 20–230 and 320–446; the
  queue pointer in full (including its claim line); one house-form brief pair whole
  (`2026-10-18-0511-template-history-privacy-cold`, brief and sibling) and the brief section of
  `2026-10-18-0508-body-free-commit-read-cold` above its first divider (not its verdict). Of
  this delta: commit `692c04a` read body-free through `tools/coldsweep.py --commit` (subject,
  stat, whole diff, including the new docstring and test docstrings), never the message body;
  `tools/report.py` lines 120–190, `tools/leakscan.py` lines 1885–1915 and
  `tools/floor.py` lines 100–200, 955–1000, 1070–1100 and 1560–1610 at HEAD; the subjects of
  the two later commits touching a delta path. **It read the intent record in full** (the
  author's account, held in the sibling); the record carries no quoted words of the principal,
  so this brief has no acceptance-test section. It ran a scratch probe of the reader and a
  read-only count over the adopting child repos' committed floor config (results held in the
  sibling, by count). It did not open `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md` or any prior verdict. Its harness also loaded user-level and repo
  instruction files and a memory index, which hold private context this brief does not carry.

## What the work is

One landing commit, on `main`:

- `692c04a` (2026-10-18 05:34 UTC) — tools: normalise staged positionals in one shared reader
  (115/360). Delta paths: `tools/report.py` (the new `scope_staged`), `tools/leakscan.py`,
  `tools/secretscan.py`, `tools/conflictscan.py`, and `tools/test_report.py`,
  `tools/test_leakscan.py`, `tools/test_secretscan.py`, `tools/test_conflictscan.py`.

Two later commits touch a delta path (`tools/leakscan.py`): `b5a2c53` and `34dc0f0`. They are
not this delta, but the first adds further callers of the same reader; review the delta paths
at HEAD, and weigh every caller of `scope_staged` that exists there, in or out of the delta.

**Read the commit body-free:** `python3 tools/coldsweep.py --root . --commit 692c04a` (subject,
stat and diff, never the message body). Plain `git show` is barred here: it prints the message
body before the diff, and reading is atomic (rule 1). The docstrings and code comments the
delta adds are the delta, and reading the delta is never barred.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Non-goals are the only narrowing and
are themselves reviewable.

Probe, at least:

- **Old match against new, both directions.** In a throwaway repo under your scratchpad, run
  each guard at `692c04a^` and at HEAD (extract each with `git archive <rev> tools`, run the
  extracted copy by path) over one staged finding, across every positional spelling you can
  construct. Build the table and answer two questions from it: what happens to a scope the old
  exact-spelling match accepted and the new reader does not; and what happens to one the new
  reader accepts that the old match did not. For each row say whether the change widens cover,
  narrows it, refuses, or leaves it as it was, and whether any row exits 0 while covering less
  than its spelling names.
- **Did any child rely on the old match?** The question the author could not settle alone.
  Probe the adopting child repos on the machine, read-only: discover them with
  `python3 tools/floorfleet.py --root <the directory holding the principal's main atelier
  checkout> --json`, then read each child's COMMITTED floor config with
  `git -C <child> show HEAD:.atelier-floor.json` (never its working tree), and render each
  declared scope for the three guards (fleet `scope` and any `local` check that runs
  `--staged`) through `floor.py`'s staged-mode render before comparing old and new. Look also
  for any child whose committed hooks or workflows call a guard with `--staged` directly rather
  than through the floor. Report **by count only, never by name or path**: how many children,
  how many declare a scope, how many scope paths, how many would behave differently. Point no
  scanner at a child and write nothing there. From a session without the clones, state the
  impossibility with its grounds.
- **Every path a positional reaches the reader by.** `floor.py`'s `_render` (hook and ci
  planes, fleet `scope`, `local` scope), `.githooks/pre-commit`, the CI workflows, and a hand
  invocation. For each, what spelling arrives, and is the reader's normalisation consistent
  with `floor.py`'s own validation of a scope path (`_reject_escaping_scope`) and its render
  (`strip("/")`, dropping `.`)?
- **The refusals and the exit codes.** Every way `scope_staged` and its callers can exit; any
  caller that discards the returned code; whether a refusal and a clean pass can be confused.
- **The tests.** Do they fail if the reader breaks? Mutate it (for example, restore the old
  prefix match, or drop the normalisation) and re-run; a suite that stays green on a broken
  reader is a finding.
- **The surfaces that describe the reader.** Each guard's `--help`, `tools/README.md`,
  `CHANGELOG.md`, `floor.py`'s comments on staged positionals, and any doctrine that tells a
  session how to run a staged scan by hand.

**Non-goals:** the decision that the three guards run on the staged diff at all, and the
barred-path set. Whether the reader keeps the staged plane's promise, and everything it now
touches, are in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first, then attack
   each with a probe. Ask whether normalising a spelling is the right fix for a silent-empty
   class, set against refusing what cannot match, and where the line between the two now sits.
2. **Correctness & quality.** Does the reader do what its docstring and the callers' comments
   say, on every spelling and every caller? Record each overclaim against the text that makes
   it.
3. **Completeness / harvest.** Every caller of the reader at HEAD; every other `--staged`
   scanner in `tools/` that filters by positional and does not use it; every child scope; every
   surface that documents how to scope a staged scan. Is a changelog entry or a `--help` line
   owed?
4. **Security & privacy** — mandatory. The reader turns caller-supplied strings into a filter
   over a boundary scan: check path traversal, option injection and pathspec handling by hand
   against the OWASP catalogue (A01 and A03). Check the fixtures build no real identity and
   plant nothing a scanner elsewhere would treat as live. Aim `/security-review` at the code
   diff only from a clean tree (see *House rules*), or discharge it by grounds and do the
   code-altitude read by hand. Report the child probe by count; a finding that names a private
   repo is itself a leak.

## Re-run obligation

Re-run, do not read. Each line below was run once by the brief-writer from its worktree root
at `2f6dbf6`; its results are held in the sibling, not offered here. Read exit codes explicitly.

- `python3 tools/coldsweep.py --root . --commit 692c04a`
- `python3 -m unittest discover -s tools -p test_report.py`, and the same for
  `test_leakscan.py`, `test_secretscan.py` and `test_conflictscan.py`
- the full Python suite, once, in the foreground under `nice -n 10`:
  `python3 -m unittest discover -s tools`
- `git log --oneline 692c04a..HEAD -- <the eight delta paths>` — each commit named
- the floor at HEAD: `python3 tools/floor.py --plane ci --root .` and
  `python3 tools/floor.py --plane hook --root .`; if the ci plane exits non-zero, read which
  scanner and which file before you weigh it

## House rules for this run

- Name your own review worktree in the verdict; it is read-only to you except for THIS file.
  Other sessions may be live on this machine: touch nothing outside your worktree and your
  scratchpad. Never open another `docs/reviews/` file before phase 2.
- No git command that writes in the worktree, beyond committing this one file at the end of
  each phase (or handing it to your orchestrator to commit). Read-only git is fine. Probe repos,
  extracted revisions and mutated copies go under your session scratchpad, named by your
  prefix, and are deleted when you finish; never mutate the worktree's `tools/`.
- One heavy process at a time: check `uptime` first; the four delta test files as often as your
  mutations need, the full suite at most once, all in the foreground. Never run an installed
  tool by bare name from `PATH`; run the worktree's copy by path.
- The child probe is read-only and reads committed config only. Never point a scanner at a
  child repo, never write there, and never name one: report by count.
- `/security-review` reads the session's pending diff, not this delta: reproduce the diff in a
  scratch clone or discharge it by grounds, and never run it with this brief or its sibling
  dirty.
- This pass is pending while you run it: anything you write to the session log, the pointer
  or a commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo
  is PUBLIC: never quote a secret, a placeholder token, an email address, a private repo's
  name or a personal detail.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/950-rule-4-cold-pass-queued-staged-positional-reader.md`,
this brief's sibling
`docs/reviews/2026-10-26-0912-staged-positional-reader-cold.deferred.md`, the message body of
`692c04a` (read subject, stat and diff only), and the intent record:

- `docs/roadmap/115-guardrail-architecture-mike-commissioned/360-a-bare-dot-scope-makes-the-staged-plane-scan-nothing.md`

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/950-rule-4-cold-pass-queued-staged-positional-reader.md
--also-exclude docs/reviews/2026-10-26-0912-staged-positional-reader-cold.deferred.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/360-a-bare-dot-scope-makes-the-staged-plane-scan-nothing.md
<pattern>`; `--include-barred` only with disclosure in the verdict. The delta's own docstrings
and comments are the delta, and reading them is never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses, the probes and the re-run list; run
the standing checklist V1–V7, each answered or discharged in one line with grounds. Append your
verdict below a `---` divider in THIS file: provenance repeated (how you were spawned, your
tier, what you read), per-lens answers, the old-against-new spelling table, the child probe by
count, findings with stable IDs (prefix `QS`: `QS1`, `QS2`, …) and severities (MAJOR /
MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results) and a follow-up checklist. Then STOP and commit phase 1
unrevised before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling, the intent record and the commit body. Append `### Reconcile`
beneath your verdict: per-finding notes against the sibling's questions and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never
revise phase-1 text. Then fold the sibling in below the reconcile and delete it.

The guards are doctrine by function: a clean `--staged` scan governs what every session and
every child commits. Record all findings and apply nothing (rule 3); the principal decides.
Counsel per finding is welcome, labelled as counsel and kept beneath it.
