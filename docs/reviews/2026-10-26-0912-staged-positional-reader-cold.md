# Cold pass — the staged-positional reader the three staged-diff guards share

**Pass type:** code cold pass, doctrine by function, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes the pass. The principal's current standing ruling is that no Fable work runs
without his explicit permission, so this pass waits for that permission as well.
**Status:** PASS RAN 2026-10-28 — PASS-WITH-FINDINGS, 1 MAJOR · 2 MODERATE · 3 minor ·
5 notes (QS1–QS11); every finding is the principal's (rule 3). Run on Fable 5.1 through the
Claude Platform API by an orchestrating session (`f7b25adb`) that started and instructed neither
the delta's authors nor the brief-writer; both phases below, the held-back sibling folded in
verbatim at the end. Brief written 2026-10-26 UTC by an Opus 5.5 brief-writer subagent of
session 5070f22b.
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

---

*Act 1 run by `claude-fable-5-1` at effort xhigh through the Claude Platform
API (an API harness, read-only sandboxed tools), 47 turn(s), metered US$7.06;
orchestrated by session f7b25adb, 2026-10-28.*

## Verdict — phase 1 (cold pass, 2026-10-28)

### Provenance, repeated

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`, effort xhigh), called through the Claude Platform
  API on the principal's monthly credit (approved 2026-10-28). The pass runs as
  reviewer-plus-orchestrator under rule 4: the orchestrator is session `f7b25adb`
  (Claude Opus 5.5), which claimed the pass, made the worktree and holds the context partition;
  it formed no finding and wrote no severity. This arrangement is disclosed here, before the
  findings, as rule 4 requires.
- **Spawn test:** I was neither started nor instructed by session `8e498ef1` (the author) or any
  worker it dispatched, nor by session `5070f22b` (the brief-writer) or any of its subagents.
- **Worktree:** a pass worktree, branch
  `fable-api-atelier-160-950-2026-10-26-0912`, HEAD `0a2b7a7`, read-only to me. Scratch work
  ran under `/private/tmp/fable-api-scratch`, now deleted.
- **What I read:** the brief whole; `docs/method/REVIEW.md` whole; commit `692c04a` body-free
  through `tools/coldsweep.py --commit` (subject, stat, diff); `tools/report.py` whole; the
  `_main` of each guard at HEAD; `tools/floor.py` lines 100–247, 440–615, 1070–1105, 1180–1240,
  1360–1420, 1560–1630 and 1760–1900; `.githooks/pre-commit`; grep hits in `.github/workflows/`;
  `tools/README.md` lines 400–445 and 1550–1600; `CHANGELOG.md` headings; `tools/test_floor.py`
  lines 268–330; `tools/test_report.py` lines 655–700; `tools/floorfleet.py` header and parser;
  `tools/board.py`, `publishscan.py`, `blockscan.py` argument parsers. Not opened:
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any prior verdict, the queue
  pointer, the sibling, the intent record, the commit body.
- **Exposure, disclosed:** a directory listing of the sibling checkouts showed me private repo
  names; none is written here. The ci-plane floor output printed one advisory finding whose
  path is a file under `docs/reviews/`; I saw a filename, not its content.
- **Limits of this pass (sandbox):** no network, no writes outside `/private/tmp`, no `tar`,
  `nice` or `uptime` (load was read with `os.getloadavg()`: 3.8 on 12 CPUs; the suite was niced
  from inside Python). The host's git config signs commits with a key the sandbox cannot read,
  so every test that commits in a scratch repo errored (exit 128); the sandbox also denies
  `stat` on the home-directory term list, so `leakscan` and `floorfleet` were run with
  `ATELIER_LEAKSCAN_TERMS` pointed at an empty scratch file. `/security-review` is not reachable
  from this harness. Each is named where it bears.

### The load-bearing assumptions, named and attacked

1. *A positional is a spelling of a git path, so normalising the spelling makes it match.*
   Attacked across 45 spellings (table below). Holds for every spelling that differs from
   git's by `./`, `//`, `/.` or a trailing `/`; fails for case and Unicode normalisation, where
   the spelling names a path that exists on this filesystem but is not git's path (QS1).
2. *Once spelling is normalised, an empty result is scope, not spelling.* Attacked: the floor's
   own run guard calls a scope that reads nothing "a silent hole, not a narrower check" and
   blocks it; tree mode refuses the same typo with exit 2. The reader passes it with exit 0 and
   the test pins that (QS2).
3. *The staged set the reader filters is the one `--root` names.* Attacked: it is the cwd's
   repository's index (QS3).
4. *The hook plane can hand the reader a scope naming a directory this repo lacks.* Attacked:
   it cannot; the floor blocks (boundary guards) or skips (local checks) first, so the docstring's
   justification for assumption 2 is unreachable (QS2).
5. *The tests fail if the reader breaks.* Attacked with nine mutations; eight caught, one not
   (QS4).

### Lens 1 — approach and assumptions

Normalising is the right fix for the class the delta names: `.`, `./x`, `x/.`, `x//`, `./-name`
and `x/` on a file all named a real git path and silently emptied the set. Every one now covers
what it names (table). Refusing `..`-forms and absolute paths is right too: they can never spell
a git path. Where the line now sits is the problem. The delta draws it at *lexical* spelling,
but the invariant the hook plane needs is *names a git path*. A string that exists on a
case-insensitive, normalisation-insensitive filesystem (this machine's) passes every lexical
test, passes `floor.py`'s `exists()` guard, and still matches no byte of git's path list. That
member of the silent-empty class is open at HEAD, reachable from committed config, and the
delta's docstring and tests document the behaviour that leaves it open. The brief's question
("normalise, or refuse what cannot match?") has a third answer the delta did not take: refuse
what matches nothing *git lists*, which closes QS1 and QS2 in the one shared place.

### Lens 2 — correctness and quality

The reader does what its docstring says on every spelling I constructed, and the three callers
behave identically row for row. Overclaims, each against the text that makes it:

- `scope_staged` docstring: "so does a scope naming a directory this repo lacks" is offered as a
  legitimate hook-plane shape; the floor never renders one (lines 1797–1848), so the hook plane
  never produces it, and by hand it is the tree-mode typo `refuse_missing_paths` exists to
  refuse (QS2).
- `floor.py` 1809–1819: "the class is shut end to end ... all three of its members now block".
  A fourth member (filesystem-folded existence) does not block (QS1).
- `floor.py` 1588–1595 and `test_floor.py` `test_default_staged_scope_passes_no_positional`:
  a bare `.` "matches nothing at all" / "an absolute-path-shaped miss in disguise" — false at
  HEAD; `.` now means the whole diff (QS5).
- `--root` help, all three guards: "repo root for relative paths" — in staged mode relative
  positionals are matched against the cwd repository's git output, not resolved against
  `--root` (QS3).

### Lens 3 — completeness and harvest

- Callers of `scope_staged` at HEAD: three in `leakscan.py` (1900, 1903, 1905), one each in
  `secretscan.py` (1344) and `conflictscan.py` (603). Two of the leakscan calls discard the code
  (QS7).
- Other `--staged` scanners in `tools/`: `publishscan`, `board` and `blockscan` accept and
  ignore `paths`; `harvestscan` takes none. No other positional filter exists, so the reader is
  the single home. Discharged.
- Child scopes: see the count probe below; none would change.
- Surfaces: `--help` says nothing of repo-relative spelling or `.`; `CHANGELOG.md` records
  `115/270`, `115/280`, `115/300` and `020/150` at this grain but not `115/360`; the
  `report.py` section of `tools/README.md` lists the `115/260`, `115/280` and `115/300` readers
  and not this one (QS5). The one doctrine surface that tells a session how to scope a staged
  scan by hand tells it to edit the hook (QS6).

### Lens 4 — security and privacy

Threats enumerated for the reader's class: (a) a caller-supplied string steering the scan at
files outside the repo — not possible, the strings never touch the filesystem or a subprocess;
they are compared against git's own output, and `..`/absolute forms are refused lexically
(OWASP A01 checked by hand, nothing reachable); (b) option injection — argparse consumes a
leading `-` before the reader (row `-dash`: usage error, exit 2 on both), the floor refuses a
`-` scope at parse and documents `./-name`, and positionals never reach git, so no pathspec
magic applies (A03 checked by hand, nothing reachable); (c) a hostile or careless child config
can only *narrow* the scan, which the floor already treats as a cover decision needing a `why`
and shows on the board — the residual is a narrowing that reads as none (QS1). Fixtures: all
planted shapes are assembled by concatenation, identities are RFC 2606, the leakscan test sets
the term list to an empty file so the machine's list is never read; the ci-plane floor at HEAD
is clean over `tools/test_*.py`, so nothing planted reads as live elsewhere.
`/security-review` cannot be aimed from this harness: discharged by grounds, with the code-
altitude read above in its place. The child probe is reported by count only.

### Old against new — one staged finding, every spelling

Probe repo: staged `docs/a.txt`, `docs/sub/b.txt`, `top.txt`, `-dash/d.txt`, `docs-extra/c.txt`
each holding a conflict marker, a private-key header and a token; `src/` present with nothing
staged. Each guard run from the `692c04a^` copy and the HEAD copy, cwd = repo root unless
stated. Exit `0/1` reads old/new; all three guards agreed on every row.

| spelling | old/new | effect |
|---|---|---|
| (none) | 1/1 | as it was: whole diff |
| `.` `./` `./.` `''` | 0/1 | widens: silent-empty → whole diff |
| `docs` `docs/` `docs//` `docs/sub` `docs/sub/` `docs-extra` `top.txt` `docs/a.txt` | 1/1 | as it was |
| `./docs` `./docs/` `docs/.` `docs/sub/..` `./docs/a.txt` `./top.txt` | 0/1 | widens: silent-empty → named path |
| `docs/a.txt/` `top.txt/` | 0/1 | widens: a file spelt with a slash now matches |
| `./-dash` (the floor's documented spelling for a dash directory) | 0/1 | widens |
| `src .` | 0/1 | widens: `.` dominates |
| `docs/..` | 0/1 | widens: normalises to the root |
| `..` `../x` `docs/../../x` `../repo` `../repo/docs` | 0/2 | refuses: silent-empty → exit 2 |
| `/abs`, an absolute path into the repo | 2/2 | as it was: refused |
| `-dash` | 2/2 | as it was: argparse usage error |
| `src` `./src` (exists, nothing staged under it) | 0/0 | as it was: legitimately empty |
| `no-such-dir` `docs/*` `~/docs` | 0/0 | **exit 0 covering less than spelt** (QS2) |
| `Docs` `DOCS/a.txt` | 0/0 | **exit 0 covering less than spelt** (QS1) |
| NFD spelling of a directory git stores NFC | 0/0 | **exit 0 covering less than spelt** (QS1) |
| cwd `docs/`: `.` | 0/1 | widens |
| cwd `docs/`: `sub` `a.txt` | 0/0 | **exit 0 covering less than spelt** (QS3) |
| cwd in another repo, `--root` this one, `docs` | 0/0 | **exit 0 reading the wrong index** (QS3) |

*Scope the old match accepted and the new does not:* none. Every spelling the old match
covered is covered identically. The refusals replace rows that were silent-empty.
*Scope the new reader accepts that the old did not:* the 17 widening rows above; each now
covers exactly what it spells (`docs/..` and `src .` spell the root). No row covers more than
its spelling names. The rows that exit 0 while covering less are all unchanged by the delta,
and all remain open at HEAD.

### Consistency with `floor.py`'s validation and render

`_reject_escaping_scope` (absolute or `..` in parts, `-` prefix) is a strict subset of the
reader's refusals: anything the floor rejects the reader would refuse or normalise safely, so
the reader is never stricter than the floor on a rendered scope. `_render` drops `.` and `""`
and strips slashes, but passes `./` through as `.` and `x/.` as `x/.` — before the delta both
silently emptied the set; now they mean the whole diff and `x`. The floor's run guard checks
existence with `(root / p).exists()`; the reader matches bytes. That seam is QS1.

### Child probe — by count

Discovered read-only with `floorfleet.py --atelier . --root ..` (31 entries, 30 git repos, 22
with an atelier pin; 23 rows, one the parent). Committed config read with
`git show HEAD:.atelier-floor.json` only; no scanner pointed at any child; nothing written.

- children: 22; with a committed floor config: 20; with a tracked `.githooks/`: 20
- fleet `scope` declarations naming one of the three guards: 2; `local` checks running
  `--staged`: 4; scope paths across both: 10
- rendered through the floor's staged render and both readers: 10 identical, 0 refused,
  0 widened, 0 narrowed — **0 children behave differently**
- scope paths present in the committed tree in exact spelling: 10 of 10 (none case-folded, so
  no child is in QS1's state today)
- committed hook or workflow files calling a guard with `--staged` directly: 0

### Findings

**QS1 — MAJOR.** A committed scope whose spelling differs from git's by case or Unicode
normalisation renders, passes every floor guard, and the boundary guards print clean over a
staged live-shaped secret. Reproduced live on this filesystem: `.atelier-floor.json` with
`scope.secretscan` and `scope.conflictscan` of `Docs` over staged `docs/a.txt`; `floor.py
--plane hook` rendered `✅ enforced`, both guards exit 0, output "✓ secretscan clean — no
credentials in the scanned lines." Same result by direct invocation for a directory spelt NFD
where git (with `core.precomposeunicode=true`, set by git itself here) stores NFC: secretscan
and leakscan exit 0 over a staged private-key header. The lexical half (`_reject_escaping_scope`)
and the resolved half (`exists()`, `floor.py` 1797) both pass because the filesystem folds case
and normalisation and git does not. `floor.py` 1809–1819 claims this class "shut end to end";
the reader's docstring and `test_empty_by_scope_is_not_refused` treat the leftover emptiness as
scope. Pre-existing: the old match behaves identically, and no child on this machine is in this
state today; recorded as MAJOR because it is the exact failure the brief names, reachable from
committed config on the house platform, and the hook is the only gate before the remote.
*Counsel:* in the shared reader, refuse a positional that matches no staged path *and* names
nothing in the index (`git ls-files -z -- <normalised>` empty, byte-exact); that is the one
check that distinguishes "nothing staged under it this commit" from "names no git path", and
it closes QS2 in the same stroke. Then correct the `floor.py` claim or make it true.

**QS2 — MODERATE.** The reader passes a positional that names nothing at all — `no-such-dir`,
a literal glob, an unexpanded `~/x` — with exit 0, and pins it as deliberate. Tree mode
(`refuse_missing_paths`: "a typo'd path that scans nothing must never read as a clean pass")
refuses the same typo with exit 2; the floor blocks it for these three guards with "a scope that
reads nothing is a silent hole, not a narrower check". The docstring's justification is that
the hook plane renders a declared scope the repo lacks; it does not (`floor.py` 1797–1848 blocks
or skips first), so the only road to this behaviour is a hand invocation, where a session
running `leakscan --staged tikii/` cites a false clean. V5: the reader contradicts both the
tree-mode rule and the floor's for the same input. *Counsel:* as QS1.

**QS3 — MODERATE.** `--root` does not govern the staged diff. `report.staged_added()` and
leakscan's `staged_changes()`/`_staged_blob()` run `git` in the process cwd with no `-C`, and
positionals are matched against that repository's root-relative paths. Reproduced: cwd in a
second scratch repo with nothing staged, `--root` the repo holding the planted findings,
positional `docs` — all three guards exit 0 and print clean. From a subdirectory of the right
repo, cwd-relative spellings (`sub`, `a.txt`) silently empty too. Hand invocation only (the hook
runs from the repo root), pre-existing, but the `--root` help ("repo root for relative paths")
promises the opposite, and roadmap `010/110` closed exactly this cwd/root mixing for tree mode.
*Counsel:* run the staged git commands with `-C root` (one shared constant, three call sites),
or refuse when the cwd's `rev-parse --show-toplevel` is not `root`; say in `--help` that staged
positionals are repo-root-relative.

**QS4 — minor.** The suite stays green when the prefix boundary is removed. Mutation M7
(`prefixes = tuple(norm)` instead of `n + "/"`) makes `docs` match `docs-extra/`; the four delta
test files and `test_report.py` report the same results as unmutated. No fixture has a sibling
sharing a name prefix. Over-match is in the safe direction, but the reader's contract (`docs` is
the `docs/` subtree) is unpinned. The other eight mutations (old match restored, escaping
refusal dropped, `.` case dropped, filter ignored, refuse-on-empty, exact-file match dropped,
refusal demoted to a print, first leakscan caller discarding its code) were each caught.
*Counsel:* one fixture row `docs-extra/…` in `test_report.py`'s dict and the three repos.

**QS5 — minor.** Stale or absent mirror sites (V3): `floor.py` 1588–1595 and
`test_floor.py`'s `test_default_staged_scope_passes_no_positional` docstring say a bare `.`
matches nothing (false at HEAD; the floor still drops `.`, so behaviour is unchanged, the claim
is not); no `CHANGELOG.md` entry for `115/360` where `115/270`, `115/280`, `115/300` each have
one; `tools/README.md`'s `report.py` section names the `115/260`/`280`/`300` readers and not
this one; each guard's `--help` for `paths` and `--staged` says nothing of repo-relative
spelling, `.` or the refusals. A changelog entry and a `--help` line are owed.

**QS6 — minor, pre-existing.** `tools/README.md` "Wiring it in" (lines 422–430) tells a
session scoping a staged scan to "edit the hook's leakscan invocation", and describes a hook
that "runs `secretscan --staged` and `leakscan --staged`". The tracked hook says "THIS FILE
NAMES NO SCANNER" (ADR 0008) and the floor's `scope` key is the mechanism. The one doctrine
surface on hand-scoping points at the retired path (V5 with `.githooks/pre-commit`).

**QS7 — note.** `leakscan.py` 1903–1906 call `scope_staged` twice more and bind the code to
`_rc`. Safe today — a refusal depends only on `paths`, which the first call has already judged —
but the shape is the one the exit-code contract forbids, and a later refusal that depends on the
set would be swallowed. *Counsel:* normalise once, return the normalised list or a predicate,
apply it to each of the three dicts. (Doing so also removes the fifteen-line absolute-path
comment at 1885–1899 that restates the helper's own docstring; V4 otherwise discharged.)

**QS8 — note.** `../repo/docs` is refused as "outside the repo" though it lexically names an
in-repo path. The refusal is the safe outcome and matches `_reject_escaping_scope`'s rule; the
message overclaims slightly. No change needed beyond wording.

**QS9 — note, outside the delta, on delta paths at HEAD.** The suite is not runnable on the
system Python 3.9: `test_leakscan.py` 1929 uses `contextlib.chdir` (3.11+) and
`test_allowmarker.py` 179 uses `Path.write_text(newline=)` (3.10+), while every scanner ran on
3.9 in this pass and the hook's text promises "Python 3, stdlib only". CI pins 3.12, so CI is
unaffected. Separately, fixtures that commit inherit the host's signing config; a
`-c commit.gpgsign=false` on their `git` calls would make them host-independent (the
`ParseAddedLinesTest` and `StagedRealGitRepo` errors below are this, not the code).

### Standing checklist

- **V1** — Overclaims found: QS1 (`floor.py` "shut end to end"), QS2 (docstring's hook-plane
  justification), QS3 (`--root` help), QS5 (bare `.` "matches nothing").
- **V2** — Re-ran: the four delta test files, the full suite once, coldsweep, both floor planes,
  the git log; drove the reader old-against-new across 45 spellings and the floor end to end
  over a probe config. One recorded claim did not reproduce: `floor.py`'s "class shut end to
  end" (QS1).
- **V3** — Mirror sites swept: QS5, QS6; templates seed a plain `src` spelling (clean).
- **V4** — The reader is the one home; caller comments are stamped pointers. Discharged, with
  the duplicate comment noted under QS7.
- **V5** — QS2 (reader against `refuse_missing_paths` and the floor's run guard); QS5 and QS6
  (stale text against live behaviour).
- **V6** — Lens 4 run by hand against OWASP A01/A03; `/security-review` discharged by grounds.
- **V7** — Spawn provenance stated in the brief and repeated above.

### Overall

**PASS-WITH-FINDINGS** — 1 MAJOR, 2 MODERATE, 3 minor, 3 notes (QS1–QS9). The delta does what it
says: every spelling the old match silently emptied now covers what it names or is refused, no
previously covered scope is lost, and no child on this machine changes behaviour. The MAJOR is a
pre-existing member of the same silent-empty class that the delta's chosen line leaves open and
documents as acceptable; it is the principal's to decide (rule 3), and the counsel under QS1
closes QS1 and QS2 together in the shared reader.

### Re-run ledger

| command | result |
|---|---|
| `python3 tools/coldsweep.py --root . --commit 692c04a` | exit 0; subject, stat, 8-file diff; body not read; 0 barred files touched |
| `git log --oneline 692c04a..HEAD -- <8 delta paths>` | exit 0; `34dc0f0` (020/440), `b5a2c53` (020/150), both `leakscan.py` only |
| `python3 -m unittest discover -s tools -p test_report.py` | exit 1; 71 run, 4 errors, all `ParseAddedLinesTest` at `git commit` exit 128 (host signing key unreadable in sandbox; same commit succeeds with `-c commit.gpgsign=false`); the delta's `test_scope_staged_normalises_and_refuses_only_spelling` passed |
| `… -p test_conflictscan.py` | exit 1; 56 run, 1 error (`StagedRealGitRepo`, same signing limit); `StagedPositionalScope` 5/5 passed |
| `… -p test_secretscan.py` | exit 1; 174 run, 1 error (`StagedSpacedPathAndMultiHunkTest`, signing limit); `StagedPositionalScope` 5/5 passed |
| `… -p test_leakscan.py` | exit 1; 219 run, 2 failures + 1 error from the sandbox's denied `stat` on the home term list, 7 errors `contextlib.chdir` (QS9); `StagedPositionalScope` 5/5 passed |
| full suite, once, `os.nice(10)`, foreground | ran to completion; output exceeded the harness return limit and the summary line was lost; not re-run under the one-heavy-run rule; visible errors are the signing limit, the denied `stat`, and the two 3.9 incompatibilities (QS9) |
| `python3 tools/floor.py --plane ci --root .` | exit 0; 1 warn-only pathscan finding in a decision record (not this delta); leakscan run with an empty term list (sandbox) |
| `python3 tools/floor.py --plane hook --root .` | exit 0; staged set empty (the sibling's removal is unstaged) |
| old (`692c04a^`) and HEAD `tools/` materialised via `git show`, byte-verified against both revisions; 45 spellings × 3 guards × 2 revisions | table above |
| floor hook plane over the probe repo with `scope: Docs` | rc 1 overall (leakscan unscoped caught it); secretscan and conflictscan `enforced`, rc 0 (QS1) |
| NFD/NFC probe | NFC spelling rc 1; NFD spelling exists on FS, rc 0 for secretscan and leakscan (QS1) |
| cwd-in-another-repo probe | all three guards rc 0, clean; cwd not a repo: rc 2 "git diff failed" (QS3) |
| 9 mutations on a scratch copy, four delta files `-k Staged -k scope_staged` | 8 caught; M7 identical to baseline (QS4); baseline non-passes were the runner's non-repo cwd reaching `git diff` before the absolute-path refusal |
| `floorfleet.py --atelier . --root .. --json` + `git show HEAD:.atelier-floor.json` per child | counts above; crashed once on the denied `stat` before the term-list variable was set |

### Follow-up checklist (for the principal's decision; nothing applied)

- [ ] QS1 — decide whether the reader refuses a positional that names nothing git lists; fix or
      soften the "shut end to end" claim in `floor.py` to match.
- [ ] QS2 — same decision; either way, make the `scope_staged` docstring's hook-plane claim
      true or remove it, and reconcile with `refuse_missing_paths`.
- [ ] QS3 — anchor the staged git commands to `--root` (or refuse a cwd mismatch); correct the
      `--root` help in all three guards.
- [ ] QS4 — add a `docs-extra`-shaped fixture to the reader tests.
- [ ] QS5 — CHANGELOG entry for `115/360`; `report.py` README paragraph; `--help` wording;
      refresh the two bare-`.` comments.
- [ ] QS6 — rewrite `tools/README.md` "Wiring it in" to the floor's `scope` mechanism.
- [ ] QS7 — normalise once in leakscan, drop the discarded codes.
- [ ] QS8 — reword the escaping-path message.
- [ ] QS9 — pin the suite's minimum Python or restore 3.9 compatibility in the two tests; make
      committing fixtures independent of the host's signing config.

Tally: 9 findings — 1 MAJOR, 2 MODERATE, 3 minor, 3 notes. Overall PASS-WITH-FINDINGS.

ACT 1 SAVED

---

*Act 2 run by `claude-fable-5-1` at effort xhigh through the Claude Platform
API (an API harness, read-only sandboxed tools), 5 turn(s), metered US$1.29;
orchestrated by session f7b25adb, 2026-10-28.*

### Reconcile

**Written:** 2026-10-28, after phase 1 was handed to the orchestrator (session `f7b25adb`)
for commit and the sibling was released. Opened at this step, in this order: the sibling; the
intent record `115/360`; the message body of `692c04a`; and, of the prior verdicts the sibling
names, `2026-10-17-0930-staged-diff-structure-cold.md` by grep for `SX1` and at the passages
found (rule 2 permits it now, to reconcile). Not opened: `docs/SESSIONS.md`, `docs/sessions/`,
`docs/ROADMAP-DONE.md`, the queue pointer, any other verdict. Phase-1 text above is unrevised.
I cannot write files: the folding of the sibling below this section and its deletion are the
orchestrator's to do, per the brief's phase 2.

**Against the author's account (intent record lines 42–54, commit body).**

- *"Once spelling is normalised, no spelling of an in-repo path can still miss."* Refuted by
  QS1: a case-folded or NFD spelling is a spelling of an in-repo path on this filesystem and
  still misses. The claim is true lexically and false on the platform the hook runs on.
- *"Rejected: … refusing a positional naming no existing path. The hook plane renders the
  check's declared scope as the positionals, so a commit that stages only files outside that
  scope (or a scope naming a directory this repo lacks) legitimately filters to nothing;
  refusing it would block valid commits."* The author weighed exactly the refusal QS2 asks for
  and declined it on a premise the floor contradicts: `floor.py` 1797–1835 blocks a declared
  scope that does not exist for these three guards ("a scope that reads nothing is a silent
  hole") and 1844–1848 skips it for softenable and local checks, so no hook-plane invocation
  ever carries a non-existent path. The author's own probe ("scoped to `src/` passes over
  staged `docs/` findings") exercises the *exists, nothing staged* case, which is legitimate and
  which my `src` row confirms; it does not exercise the *directory this repo lacks* case, which
  the floor would have blocked before any guard ran. QS2 stands and is sharper for it: a
  refusal was considered and rejected on a false ground.
- *"The real hook plane is not affected"* (intent record lines 17–19). True of the bare `.`,
  which the floor drops. Not true of the class: the floor passes `./x` and `x/.` through its
  render, so a child scope spelt that way was affected before the delta, and QS1's members are
  affected after it. A narrower statement than the record makes.
- *"16 new tests; 1949 Python tests green."* 16 confirmed from the diff. The suite count I could
  not read (summary lost; phase-1 ledger). The brief-writer's 2032 on 2026-10-26 is consistent
  with growth over the later commits.
- The record's `SX1` of the 2026-10-17 pass is a different class — the diff parser refusing a
  legitimate diff under `diff.suppressBlankEmpty` — in the same `report.py` family, not the
  same defect. No overlap with QS1–QS9; nothing in that verdict anticipates the filesystem seam.

**Against the sibling's held-back results.**

- Old-against-new (brief-writer: `secretscan` only, ten spellings; six 0→1, one 0→2, three
  unchanged): my table reproduces every class across all three guards and 45 spellings, and
  adds the rows the brief-writer's set did not reach — case, NFD, glob, tilde, cwd and
  `--root` mismatch — which are where the findings are.
- Four delta test files: the sibling's per-file counts are the same set as mine
  (71, 56, 174, 219) with the `conflictscan`/`secretscan`/`leakscan` labels permuted; the
  brief-writer's runs were green outside the sandbox, mine show only sandbox-limit errors, so
  the two agree. Floor at HEAD: both planes exit 0 on both runs.
- Child probe: the sibling's 29 is every git repo beside the checkout, mine (and `floorfleet`'s,
  on both runs) is 22 children with an atelier pin; the 10 scope paths and 0 changed agree
  exactly. Committed configs 19 (2026-10-26) against 20 (2026-10-28): 1 child's config was
  first committed after 2026-10-26, which accounts for the difference. The sibling's one grep
  hit for `--staged` in a child's committed hooks or workflows is a `floor.py` line or a
  comment, not a guard call — reconciled at 0 direct calls.

**Against the sibling's hypotheses.**

1. *`os.path.normpath` follows the host.* Confirmed lexically here too (`ntpath` gives
   `docs\sub`). The floor's lexical check already uses `PurePosixPath`; the reader's `os.path`
   is the odd one out. Formed at reconcile as **QS10** below.
2. *Empty string → whole diff.* Row `''` in the table (0→1); safe direction, floor drops it, hand
   only. Agreed; no finding.
3. *Lexical collapse through a symlink.* git's own namespace is lexical (`a/link` is an index
   entry, `a/link/../b` never is), so collapsing to `a/b` matches git, which is the right target;
   the floor rejects `..` before render. Discharged; row `docs/sub/..` covers it.
4. *Discarded codes in leakscan.* QS7. The inputs do not differ — refusal depends on `paths`
   alone, identical across the three calls — so the discards are unreachable as refusals today;
   mutation M9 shows the suite catches the first caller discarding.
5. *Can the guards tell a hand typo from a declared scope?* They do not need to: the floor
   never hands them a non-existent path, so refusing a positional that names nothing git lists
   blocks no floor invocation. That is QS2, and QS1 is the member of the same surface the
   floor *does* reach.
6. *Two normalisers in series; stale floor comment.* QS5 records the comment. The floor's drop
   of `.` is now redundant with the reader and harmless; it is the comment that must stop
   claiming the guard would miss. V4 was discharged on the reader being the one home for the
   match; the hypothesis is right that "what `.` means" now has two homes, and that is a
   one-line stamp once QS5 is applied.
7. *Near-identical test copies; mutation; env patch portability.* Nine mutations run (phase 1);
   eight red every copy, one (prefix boundary) reds none — QS4. The leakscan copy's
   `patch.dict(os.environ)` is an environment-variable patch only and ran in CI (3.12) and in
   this sandbox; portable. Three copies are per-guard pins of a shared behaviour with the unit
   test in `test_report.py` as the home; acceptable.

**Refinement to QS1's counsel (reconcile; phase-1 text unchanged).** My phase-1 counsel — refuse
when nothing is staged under the positional *and* `git ls-files -- <n>` is empty — closes the
case-fold and typo members but not the NFD one: on this platform git precomposes its pathspec
arguments (`ls-files -- <NFD>` lists the NFC entry), while the staged-diff output is NFC and the
reader's match is byte-exact. The sound shape is to let git resolve the positional entirely:
`allowed = nul_paths(git ls-files -z -- <normalised>)`, keep the staged paths in `allowed`,
and refuse when `allowed` is empty. One home for "what this spelling names" — the same code
that wrote the staged paths — and it closes QS1 (both members) and QS2 together. Residual to
weigh: a declared scope whose directory exists but holds nothing tracked or staged would then
be refused on the hook plane, which the floor's own doctrine calls correct and a first commit
that does not touch the scope would feel as a block.

**QS10 — note (formed at reconcile).** `scope_staged` normalises with `os.path.normpath`, which
on a host whose separator is not `/` turns `docs/sub` into `docs\sub` and matches no git path —
the delta's own class, reintroduced for nested scopes on that host. `floor.py` already chose
`PurePosixPath` for the lexical check; the reader should use `posixpath.normpath`, since the
strings it matches are git's and git's are POSIX. No evidence of a Windows runner or adopter
(the hook is `/bin/sh`, CI is Linux), hence a note.

**QS11 — note (formed at reconcile).** The intent record's "the real hook plane is not
affected" and the commit body's "no spelling of an in-repo path can still miss" are the
record-side statements QS1 refutes; when QS1 is ruled, the record should carry the narrower
truth beside the ruling so the next reader of `115/360` does not inherit the claim.

**Overall line, restated:** PASS-WITH-FINDINGS — 1 MAJOR · 2 MODERATE · 3 minor · 5 notes
(QS10 and QS11 added at reconcile). Headline unchanged: QS1, with its counsel refined above.
The sibling is to be folded in below this section and deleted by the orchestrator.

ACT 2 SAVED

---

## Deferred sibling, folded below the verdict

*Folded by the orchestrator, session f7b25adb, 2026-10-28: the held-back
sibling's text follows verbatim, as REVIEW.md rule 1 requires, and the sibling
file is removed in this commit.*

# Sibling to the staged-positional reader cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-26-0912-staged-positional-reader-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-26 UTC by the Opus 5.5 brief-writer subagent of session `5070f22b`
named in the brief's provenance; it forms no finding and writes no severity. Fold this file in
below the reconcile and delete it at phase 2.

## Intent record

- `docs/roadmap/115-guardrail-architecture-mike-commissioned/360-a-bare-dot-scope-makes-the-staged-plane-scan-nothing.md`
  — read in full by the brief-writer. It carries no quoted words of the principal. Lines 2–41
  are the finding as filed: the old prefix match, a scratch-clone measurement, a statement
  that the floor's hook plane was not affected, the cost (a run of commits citing a
  `.`-scoped staged scan as green), and a proposed fix with two parts. It also names a
  neighbouring finding id from a 2026-10-17 staged-diff pass (a prior verdict, not opened).
  Lines 42–54 are the author's closing account: one shared reader, what it normalises and
  refuses, that the proposed refusal of "a positional that empties a non-empty set" was
  deliberately not built and why, a scratch-clone before/after probe, a count of new tests and
  a count of the full suite green. Read it now as the author's claims to reconcile against.
- The message body of `692c04a` — not read by the brief-writer.

## Re-run results held back from the brief

Run once each by the brief-writer, 2026-10-26, from its worktree root at `2f6dbf6`, on the
principal's machine, in the foreground:

- `coldsweep --commit 692c04a`: exit 0, closing line present, no barred file in the diff.
- The four delta test files: each exit 0 — `test_conflictscan` 174 tests, `test_leakscan`
  56, `test_report` 71, `test_secretscan` 219, all OK (each also printed its scanner's
  selftest OK).
- Full suite under `nice -n 10`: exit 0, 2032 tests OK, 664 s on a heavily loaded machine
  (load average rose from about 7 to about 29 during the run; other sessions were live).
- `git log --oneline 692c04a..HEAD` over the eight delta paths: two commits, `b5a2c53` and
  `34dc0f0`, both on `tools/leakscan.py`.
- Floor at HEAD: hook plane exit 0; ci plane exit 0 (advisory warn-only lines only). Both ran
  with this brief untracked in the tree.

## Probe results held back from the brief

- **Old against new, one scanner.** `secretscan` extracted at `692c04a^` and at `692c04a`,
  one staged live-shaped key at `docs/sub/a.txt`, ten positional spellings. Six spellings
  changed from exit 0 (old) to exit 1 (new): the empty string, `.`, `./docs`,
  `docs/sub/..`, `docs/./sub`, `./docs/sub/a.txt`. One changed from exit 0 to exit 2: `..`.
  Three were unchanged: `docs` and the exact file path (1 → 1), and an out-of-scope
  directory (0 → 0). The other two guards were not probed this way.
- **Child probe, by count.** Of 29 git repos beside the principal's main atelier checkout
  (atelier excluded), 19 carry a committed floor config; 2 declare a scope for one of the
  three guards (10 scope paths in all, fleet `scope` plus `local` checks that run
  `--staged`); 0 of those paths change spelling under `normpath` once rendered by the
  floor's staged-mode render. 1 repo's committed hooks or workflows mention `--staged`
  (a grep hit only; the file was not opened, so whether it calls a guard directly with a
  positional is unknown). `floorfleet --json` over the same directory listed 22 children.

## Hypotheses (the brief-writer's suspicions, a floor not a fence)

1. The reader normalises with `os.path.normpath`, which follows the host platform. On a
   platform whose separator is not `/`, a nested scope such as `docs/sub` normalises to a
   backslash spelling, the `/` prefix test matches no git path, and the set silently empties
   — the class the delta exists to close, reintroduced for nested scopes where the old match
   worked. Confirmed only lexically (`ntpath.normpath('docs/sub')` gives `docs\\sub`); whether
   any supported runner or adopter runs on such a platform is open.
2. The empty-string positional, and any spelling that normalises to `.`, now means "no
   restriction". That widens cover, which is the safe direction, but it is a change a caller
   passing an empty scope by accident would not see. The floor drops `.` and `""` before
   render, so the hook plane never reaches this; a hand or bespoke caller can.
3. `normpath` is lexical: `a/link/../b` collapses to `a/b` whatever `link` is. The floor
   rejects `..` in a scope path before render, but a hand caller is not so guarded. Whether a
   collapse can point a scope at a different subtree than the caller meant is open.
4. The later commit `b5a2c53` calls `scope_staged` twice more in `leakscan` and discards the
   returned code. The first call already refused on the same positionals, so the discarded
   codes may be unreachable — or may not be, if the inputs differ. Out of delta, but the
   reader's contract is now relied on by callers its own tests do not exercise.
5. The author declined the item's proposed refusal of a positional that empties a non-empty
   set, on the ground that the hook plane legitimately filters to nothing. That ground holds
   for a declared scope; it does not obviously hold for a hand invocation, where an empty
   result after a typo (`dcos`) still prints clean. Whether the guards can tell the two
   callers apart, and whether they should, is the residual silent-empty surface.
6. By grep, `.githooks/pre-commit` delegates to `floor.py` and no workflow passes
   `--staged`, so in atelier every automated positional passes two normalisers in series:
   the floor's render (`strip("/")`, dropping `.` and `""`) and then the reader's
   `normpath`. Two homes for one spelling rule is a V4 question, and the floor's comment on
   staged positionals (it names "a bare `.`" as matching nothing) may now be stale.
7. The three new test classes are near-identical copies across three files. Whether a
   mutation of the shared reader (for example, restoring the old prefix match) reds all of
   them, and whether the leakscan copy's environment patch keeps it portable to CI, is
   unprobed.

## Prior verdicts on nearby surfaces (named by filename, not opened, not exhaustive)

- The intent record names a 2026-10-17 staged-diff pass. Its file is under `docs/reviews/`;
  the brief-writer did not search for or open it.
