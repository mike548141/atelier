# Cold pass — ccclose, the close-out checker

**Pass type:** code and design cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/870-rule-4-cold-pass-queued-ccclose.md`.
**Why it earns a review:** it is a first-of-kind instrument that encodes `RECORD.md`'s
close declaration as code: what it passes is what a session will cite as proof that
nothing is owed. It runs `git`, `gh` and a repo's own `tools/board.py`, reads every
project's transcripts, attributes work by a time window, and joined the expected
toolbox, so every session on the machine may now reach for it.

## Spawn provenance

- **Author of the work under review:** the queue run whose intent record is dated
  2026-10-16 15:01 UTC (an Opus orchestrator with dispatched workers; the pointer counts
  the worker's output as the run's authorship; the build commits' trailers name an Opus
  model). The `TOOLBOX.md` row landed in that run's close commit. Not opened here.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on 2026-10-17
  by the Mike-opened Fable review session working in worktree `atelier-review-1017`, on
  Mike's 2026-10-16 answer that a fresh Opus session writes these briefs. It authored
  none of the delta. It is **off-tier for review, disclosed: it forms no finding and
  writes no severity**, and it stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that passes
  rule 4's criterion. If it runs as reviewer-plus-orchestrator, rule 4's off-tier
  conditions apply and are disclosed in the claim, the pointer and the verdict. The
  reviewer repeats its own provenance in its verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This brief-writer
  read: its instruction file; the four queue pointers it was assigned (160/860–890) in
  full, and 160/500 in full as the shape of an append line (including that item's
  result line); the staging directory's file listing, and the first 50 lines of one
  peer brief of this batch (160/850) and its append, for shape; the landing commits'
  subjects, `--stat` **and message bodies** (the author's own account, including the
  merge's and the close commit's, which carry principal answers); the close commit's
  `TOOLBOX.md` diff; `instruments/ccclose.design.md` whole at HEAD; `instruments/ccclose`
  in part (its help text, helpers, wrapper and bypass tables, board, claim and floor
  checks, and `collect`'s head) and a function outline; the README's ccclose section;
  the later commit's diff on `instruments/ccclose`, the design note and the README;
  three templates in full; `docs/reviews/` filenames and filename-level greps (no prior
  verdict opened); and its harness-loaded memory index. Writing the other three briefs
  of its set, it also read those deltas' diffs and message bodies, and grep-hit lines
  of a sweep that included single lines of board items 115/290 and 115/320. It did not
  open the intent
  record, the commissioning item, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md` or `docs/method/REVIEW.md`. What its orchestrator read is the
  orchestrator's to disclose; it passed on an instruction file, three templates and a
  list of taken prefixes, and no evaluative content. Everything evaluative is in the
  sibling.

## What the work is

Landing commits (diff them; review the paths at HEAD, `2f9cfe4` or later):

- `ef3673a` (2026-10-16 15:59 UTC) — instruments: design note for ccclose, the
  close-out checker (020/180)
- `4eda680` (2026-10-16 16:17 UTC) — instruments: build ccclose, the close-out checker
  (020/180)
- `6ccbc7a` (2026-10-16 16:23 UTC) — merge: ccclose, the close-out checker (020/180).
  The merge changes none of the delta paths against `4eda680` (checked); it also
  carries a `CHANGELOG.md` entry
- `09a61b4` (2026-10-16 21:18 UTC) — session-close: record Mike's two close answers;
  install ccclose. Only its `docs/method/TOOLBOX.md` hunk is this delta

Delta paths: `instruments/ccclose`, `instruments/ccclose.test.js`,
`instruments/ccclose.design.md`, `instruments/man/ccclose.1`, the ccclose section and
any other ccclose lines of `instruments/README.md`, and the estate's-own-tools row of
the expected-toolbox table in `docs/method/TOOLBOX.md`.

**A later commit on the same files — not this delta; do not attribute it to it.**
`cea247e` (2026-10-16 16:43 UTC, merged in `99f4c2a`) — cctranscript: classify harness
text in user records instead of counting it as prompts. It replaced ccclose's own
wrapper list and record classification with cctranscript's, and rewrote design-note §6.
It is pass 160/880's subject. Review ccclose at HEAD, but where a defect sits in a hunk
`cea247e` wrote, say so and leave its charge to that pass; diff `4eda680` against
`cea247e^` to tell them apart. Nothing touches the delta paths after `99f4c2a`.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests and
live behaviour. The lenses organise it; they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **Each check against its design row.** The design note's §7 table gives, per check,
  what it reads and when it fails or is not applicable. For all eleven, drive each state
  the row names and record which the code reaches, and whether any input can produce a
  ✅ the row does not license ("a check never reports a pass it could not read for").
- **Attribution.** The window heuristic, the live session's window running to now, the
  8-character id prefix rule, and the claim-date rule. Test the claim checks against
  the claim lines actually on this repo's board at HEAD (their position in the item,
  their leading characters, the case and shape of the date), not only the fixtures'.
- **The floor check.** The sha chosen, per-workflow latest run, the red and green
  conclusion sets, pending, no runs, `gh` missing or unauthenticated — against
  `RECORD.md`'s floor-at-head rule and what `gh run list` returns at the cap.
- **Read-only, in fact.** Every subprocess ccclose starts and every file it opens.
  `--no-optional-locks` covers git; does anything else write (`gh`'s own caches,
  `python3` byte-compiling a repo's `board.py`)? Which code from the repo under check
  does it execute, and with what?
- **The heuristics' errors.** The close-ask patterns and the workaround-command table:
  for each, a false negative on a phrasing or command shape the house actually uses,
  and a false positive a session would have to answer every close.
- **The output contract.** Field-set stability, caps and whether a capped list says it
  was cut, the `unknown` versus `0` rule, `--json` parity with the text form, exit
  codes, and the help-versus-man drift guards the design names.
- **Where a session is told to run it.** `RECORD.md`, `CONCURRENCY.md`, the onramp and
  queue-run skills, `TOOLBOX.md`: is the tool referenced where a closing session would
  look, and does any text now claim more than the tool proves?

**Non-goals:** the principal's decision to build a close-out checker and his acceptance
shape (quoted verbatim in the design note), and the model-router idea the design marks
out of scope. The checks chosen, their states and the wording around the quote are in
scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Among
   them: that a transcript window attributes work well enough to print a ❌; that a
   tool whose passes are cited as evidence may rest three checks on "never fails"; that
   `instruments/` is the right home for something with a doctrine role (ADR 0006).
2. **Correctness & quality.** Read `instruments/ccclose` and its tests whole; diff the
   two build commits. Build the check table from *Scope*, one row per check and state,
   with the input that reaches it. Check whether the tests' fixtures were derived from
   the board's real claim grammar and real `gh` output or from the same reading that
   wrote the code.
3. **Completeness / harvest.** The design note against the code at HEAD (every "added in
   the build" mark, every claim of reuse); the man page and README against both; the
   `CHANGELOG.md` entry; the doctrine sites in *Scope*; `instruments/install` and the
   README's install section, now that the toolbox lists the tool.
4. **Security & privacy** — mandatory. Transcript discovery reads every project folder
   under the operator's Claude directory; `--session` accepts any path; the asks list
   quotes the principal's prompts into output that is "pasted into records" — in a
   PUBLIC repo. `CCCLOSE_GH` chooses which binary runs. A checked repo's own
   `tools/board.py` is executed. Weigh each. Never quote real transcript content in the
   verdict. `/security-review` is discharged by grounds (a landed delta; the pending diff
   is not the work) — say so, and do the code-altitude read by hand against the OWASP
   catalogue.

## Re-run obligation

Re-run, do not read. Lift invocations from `.github/workflows/ci.yml` (the instruments
job) rather than guessing.

- `node --test instruments/ccclose.test.js`, then the whole instruments suite once as CI
  runs it (`node --test instruments/*.test.js`), foreground
- `mandoc -T lint instruments/man/ccclose.1`; `node instruments/ccclose --help` by path
- live runs by path, never by bare name: build throwaway git repos, a fake `HOME` and
  synthetic transcripts in your scratchpad, stub `gh` through `CCCLOSE_GH`, and drive
  each state in the check table; snapshot `.git` (index, refs, lock files, mtimes)
  before and after to test the read-only claim
- one run against your own scratch clone of this repo, only after the read-only claim
  has held on a throwaway; never against the shared checkout or another repo
- mutation, in a scratch clone: flip one load-bearing condition per check and record
  which tests fail
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`, and
  the hook plane as `.githooks/pre-commit` invokes it)

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only git is
  fine. Probes, fixtures, mutated copies and older checkouts go in a private clone under
  your session scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the instruments suite at most once
  whole, in the foreground. Never point a scanner or ccclose at any other repo on the
  machine. Never run an installed tool by bare name from `PATH`; instruments are
  symlinked onto it from another checkout.
- `/security-review` reads the session's pending diff: discharge it by grounds for this
  landed delta, or keep the tree clean whenever you spawn it — never with this brief or
  its sibling dirty.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ English.
  Never quote a secret, placeholder token, email address, personal detail or real
  transcript text — this repo is PUBLIC; describe and locate instead.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling `docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.deferred.md`,
the landing commits' message bodies (the author's account; read subjects, stats and
diffs only), and the commissioning and neighbouring items:

- `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/180-the-mechanisable-form-of-it.md`
- `docs/roadmap/210-instruments-open-features/250-cctranscript-counts-harness-text-as-prompts.md`

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/870-rule-4-cold-pass-queued-ccclose.md
--also-exclude docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.deferred.md
--also-exclude
docs/roadmap/020-policy-as-code-programme-five-tracks-mik/180-the-mechanisable-form-of-it.md
--also-exclude
docs/roadmap/210-instruments-open-features/250-cctranscript-counts-harness-text-as-prompts.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is
never barred; the design note is part of the delta.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then append
your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, what you read), per-lens answers, the standing checklist V1–V7 each
answered or discharged with grounds, the check table, findings with stable IDs (prefix
`CL`: `CL1`, `CL2`, …) and severities (MAJOR / MODERATE / minor / note), an overall
PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger, and a follow-up
checklist. Then STOP and commit phase 1 unrevised before opening the sibling. Edit no
other file.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict: per-finding
notes against the seeded questions and the intent record, any finding formed at
reconcile marked as such, and the overall line restated. Never revise phase-1 text.
Then fold the sibling in below the reconcile and delete it.

Findings on a tool that encodes doctrine are the principal's to decide (rule 3): record
all, apply nothing; counsel per finding is welcome, labelled and kept beneath it.

---

# Verdict — phase 1 (CL), written 2026-10-18 UTC

## Provenance, repeated

- **Reviewer.** This session, running as **Fable 5.1** (`claude-fable-5-1`); tier checked
  at selection, so rule 4's stop clause did not fire. I am a subagent dispatched on
  2026-10-18 by a Mike-opened Claude Code **cloud** session (`claude-fable-5-1`,
  orchestrating; it opened on `claude-opus-5` and Mike switched it to Fable before any
  claim or pass). The orchestrator authored none of the delta or the brief and was not
  started or instructed by their authors. It forms no finding and writes no severity; it
  holds the `.deferred.md` sibling outside the checkout at a path I was not given; it
  commits this phase-1 text before releasing the sibling; it received one operational note
  from Mike's watching session (model, queue scope, container facts, merge instruction — no
  evaluative content) and, mid-pass, one correction of two container facts (no evaluative
  content). The queue pointer's claim line discloses the same shape; I have not opened it.
- **Where.** The shared checkout `/home/user/atelier` on branch
  `claude/review-work-briefs-adj6ad`: HEAD `c9d8a0d` when I started, advancing to
  `13ceaa4e` during the pass as the orchestrator committed other passes' files; nothing
  after `99f4c2a` touches a delta path except `09a61b4` (re-checked with `git log`). The
  locally fetched `origin/main` is `fe020b1`, one board-item commit past the `0aff4d8` I was
  told, touching no delta path. This is a cloud container: one checkout, no worktrees, no
  sibling repos, no estate root. I ran no git command that writes in the checkout. Every
  probe, fixture, log and the private clone live under `/home/user/scratch/CL/`.
- **What I read, in order.** `REVIEW.md` whole, this brief whole, `00-APEX.md` once; then
  the delta at HEAD (`instruments/ccclose`, `ccclose.test.js`, `ccclose.design.md`,
  `man/ccclose.1`, the ccclose lines of `instruments/README.md`, the `TOOLBOX.md` row) and
  the diffs `ef3673a→4eda680`, `4eda680→6ccbc7a`, `cea247e^→cea247e`, `09a61b4^→09a61b4`
  (TOOLBOX hunk) and `6ccbc7a^1→6ccbc7a` (CHANGELOG hunk) — `--stat --format=%s` and
  `git diff` only, no commit body. For grounding: `RECORD.md` (the close declaration and
  *The record is public*), `CONCURRENCY.md` (claiming, *Every branch ends put away*,
  *Orchestrated queue runs*), ADR 0006, `SECURITY.md` and the 2026-08-05 ADR heads,
  `docs/roadmap/README.md`'s legend, `tools/pointerscan.py`'s grammar, `tools/board.py`'s
  `run_check` and argument parser, `cctranscript`'s classifiers and numbering, `ci.yml`,
  `.githooks/pre-commit`, `.atelier-floor.json`, `CLAUDE.md`, and greps of the two skills.
  Sweeps ran through `tools/coldsweep.py` with the brief's four exclusions; never
  `--include-barred`.
- **Exposures, disclosed.** (1) The branch's `git log` subjects name other passes'
  verdicts; I read subjects only and opened none. (2) A coldsweep hit showed the generated
  index line for this pass's pointer (`docs/ROADMAP.md:311`, title only). (3) To test the
  claim regexes against the board's real claim lines, which at HEAD exist only inside
  barred files, I ran a **masked mechanical probe** over the three barred board items
  (the pointer, 020/180, 210/250): for lines containing `[~]` or "claimed" it printed only
  regex-match booleans, the line number and a character-class mask (letters→a/A,
  digits→9). No words were read. It reported one claim-shaped line in the pointer (L22:
  indented continuation, inline-code `[~]`, a capitalised word of seven letters followed
  by a `9999-99-99 9999 AAA` stamp, bold) and one inline-code `[~]` mention in 020/180 L90.
  (4) Coldsweep hit lines included single lines of board items 020/420, 160/880 and
  210/260 that name ccclose; not opened. (5) An env probe printed my own session id to my
  terminal; it is not reproduced here. (6) **No probe pointed at `$HOME`, `~/.claude` or
  `/root/.claude`** (which the orchestrator later confirmed exists and is live). Every
  instrument run used a `HOME` under my scratch directory — the test harness's own fake
  HOME, my fixture worlds, the read-only probe, the skew fixture; the one bare invocation
  was `--help`, which exits before any read; two probes `require()` the module, which
  loads code only. `gcloud` was never invoked. (7) One fixture probe exercised ccclose's
  fallback to the **shared checkout's** `tools/board.py` (run by python3 against a fixture
  repo); it wrote nothing new there (no `.pyc` newer than my start; the dir is gitignored),
  and the two floor runs on the shared checkout likewise refreshed nothing.
- **`/security-review`:** discharged by grounds. It reads the session's pending diff,
  which here is only this brief; the delta is landed. The code-altitude read was done by
  hand (lens 4). The OWASP and CWE hosts did not resolve from this container, so the vector
  classes are the lens's own list (injection, path handling, secret handling, unsafe input,
  information exposure), not a fetched catalogue — said plainly rather than implied.
- **Not re-driven here (relayed):** anything needing an authenticated `gh` (`gh` is on
  PATH, its token is invalid, so the floor and PR checks against the real host print
  *unknown* here), a live transcript store, another repo or the estate root. Anonymous
  read-only GETs to `api.github.com` were used for the Actions facts below.

## Lens 1 — approach and assumptions

Named first, then attacked. Verdicts in brackets.

- **A1 — a transcript window attributes work well enough to print ❌.** The design says
  so and prints the heuristic every run. The ❌ direction is cheap and honest. The ✅
  direction is the problem: the window also *credits* the session with a peer's green run
  (CL2) and, through `git log --since`'s stop-at-first-older-commit semantics, can hide the
  session's own commits (CL1). [False as implemented for ✅; see CL1, CL2.]
- **A2 — `git log --since=<first − 1 day>` lists every commit whose committer time is in
  the window; the day of slack covers time zones.** Plain `--since` stops the walk at the
  first commit older than the bound and marks that commit's ancestors uninteresting; a
  back-dated commit *above* the window (this repo has one: `4d80321`, committed
  2026-09-14 by date yet a descendant of the 2026-10-16 landing) hides everything beneath
  it. The slack addresses a different risk. [False; CL1.]
- **A3 — the floor's sha is "the newest window commit the remote ref contains, not the
  ref's head".** For a live session the window runs to now, so the newest window commit
  *is* the ref's head whenever anyone pushed; the protection is vacuous exactly where
  RECORD.md grounds the rule. [False for the live case; CL2.]
- **A4 — a `[~]` claim is a checkbox-line bullet, and the queue-run form names an 8-char
  id prefix.** The board's legend defines `- [~] … (claimed <date>-<HHMM>, wt: <branch>)`.
  No doctrine I can find defines an id-bearing form; the one live claim on the board at
  HEAD is a body line under a `⏳` state line, not a bullet. [Ungrounded and incomplete;
  CL4.]
- **A5 — a `⏳` on an added board line means a review was queued in the window.** A
  modified line containing `⏳` is also a `+` line. [Over-broad; CL5.]
- **A6 — "pushed" = contained in a remote-tracking ref as of the last fetch.** Stated on
  every run. [Holds, honestly bounded.]
- **A7 — a tool whose passes are cited as evidence may rest three checks on
  "never fails".** Listing-not-judging is the honest shape for a judgement the tool cannot
  make, and the verdict line counts them as "need a look". [Holds — provided the lists are
  complete enough to be worth answering; CL6, CL7 say they are not yet.]
- **A8 — `instruments/` is the right home (ADR 0006).** User-invoked, transcript-reading,
  never hook-wired: an instrument by the ADR's purpose rule. Its *status* is the thing to
  hold: its ✅ lines become doctrine-grade claims at close, which is why a rule-4 pass is
  the right response rather than a move to `tools/`. [Holds; note CL24.]
- **A9 — `$CLAUDE_CODE_SESSION_ID` is set in every session's shell.** Set in this cloud
  container's shell (value not reproduced). [Holds here.]
- **A10 — `board.py --check` only reads.** python3 writes bytecode beside the modules it
  imports, inside the repo under check. [False in detail; CL10.]
- **A11 — the brief's own account: "the merge changes none of the delta paths against
  `4eda680` (checked)".** It changes three (one-line date fixes). [False; CL16.]

## Lens 2 — correctness and quality

The eleven checks reach the states the design table names (check table below): every ➖
and ⚠️ row was driven by fixture, and the ❌ rows too. The honesty of the *unknown* path
is good — `gh` absent, unauthenticated or failing; python3 missing; board.py exit 2; no
transcript — all print ⚠️ with the reason, and `--json` carries `null` not `0`. The two
build commits are told apart cleanly from `cea247e`'s later hunk, and the design note's
three "added in the build" marks match the diff. The test file is well built: fixture
worlds, a fake HOME, a `gh` stub keyed on sha length, drift guards; 23 tests pass in
3.5 s and the whole instruments suite passes as CI runs it. Mutation testing killed 17 of
23 flips; the six survivors (CL18) cluster where the fixtures could not reach: the
read-only contract's one mechanical guard (`--no-optional-locks`), the window machinery
(`--since`, the slack, the bound), unknown conclusions, and the unknown-birth-time branch,
which on a filesystem that records birth times is never executed under test.

The fixtures were derived from the author's reading, not from the board or the host:
every fixture history is linear with monotonic dates (the real history is not — CL1); the
claim fixtures encode a `(claimed by queue run <id>)` form that no doctrine defines and
omit the body-line form actually on the board (CL4); the `gh` fixture field names are the
real `--json` field names, and its one behavioural claim — a short `--commit` sha returns
nothing — I re-drove against the Actions API and it holds (re-run ledger).

Two false-✅ paths are worse than heuristic error because the row explicitly says the
state is unlicensed: a check "never reports a pass it could not read for", yet check 7
passes with the window unknown (CL3) and check 8 passes on `skipped` (CL11).

## Lens 3 — completeness and harvest

Design note against code at HEAD: §6's five functions and the two wrapper lists are what
the code requires; §7's table matches the states reached; §10's verdict example does not
match the emitted line (CL15); §8's "only reads" is not quite true (CL10). Man page and
README: consistent with the code on the check list, the states, the caps and the exit
codes; `mandoc -T lint` clean; `--help` is 16 lines and every flag it prints is in the
page. `CHANGELOG.md` carries the entry; its "Not yet installed" line was overtaken three
hours later by `09a61b4`'s TOOLBOX row and not swept (CL17). `instruments/install` picks
the tool up by its generic glob; the README's install section needs no change, though its
Requirements paragraph names only `node` while ccclose also wants `python3` (board check)
and optionally `gh` — the ccclose section says so, the Requirements paragraph does not.

**Where a session is told to run it: nowhere.** A coldsweep for `ccclose` outside the
delta finds `CHANGELOG.md`, the index line for this pointer, the TOOLBOX row, three board
items and two code comments in cctranscript. `RECORD.md`'s close declaration — the rule
the tool mechanises — does not mention it; neither do `CONCURRENCY.md`, the session-onramp
or queue-run skills, nor `CLAUDE.md`'s "Before finishing a session". The one durable site
is the expected-toolbox table, which says *installed*, not *run at close* (CL9).

## Lens 4 — security and privacy

**Design altitude.** The design note enumerates no threats as such; §8 covers read-only
and network, §13 scope. The surfaces it should have named: (a) the output is *designed* to
be pasted into records, and this repo's records are public — by default it prints the
operator's absolute home path (Transcript row, Repo row, every worktree item) and up to
240 characters of each of the principal's close-out prompts verbatim (CL8); (b) it
executes code from the repo under check — the repo's own `tools/board.py` and whatever
that imports — with the operator's privileges, preferring it over atelier's copy, the
reverse of the hook's ADR 0008 resolution order, and with no trust note where the hook
carries one (CL10); (c) `CCCLOSE_GH` selects the executable that runs — the same trust
class as `PATH`, documented in the man page's ENVIRONMENT; acceptable, and worth one line
in §8. Transcript discovery is minimal: it opens `<id>.jsonl` by exact name in each
project folder, never other files. `--session <path>` reads any file the operator can
read — not an escalation for a local tool.

**Code altitude, by hand.** All subprocesses use `spawnSync(cmd, argv[])` with no shell,
so no command injection from transcript text, branch names or PR titles; `gh` output is
`JSON.parse`d under try/catch; absent inputs never throw (fixture S18: a non-JSON line and
an unparseable timestamp are skipped). No secret is read or written. The only writes are
python's bytecode caches (CL10). The bypass regexes run over whole Bash command strings;
two patterns have the `[^|;&]*…[^|;&]*` shape, quadratic on a very long command with many
`git` tokens — the transcript is the operator's own, so this is a note, not a finding.
Never-quoted here: no real transcript line entered any probe; every transcript was
synthetic.

## The check table

Each row: the state the design licenses, the fixture that reached it (drive scenario
`S*`, test `T`, or the clone run `C`), and what the code did. "✅ unlicensed" marks a pass
the row does not license.

| # | Check | ➖ reached | ⚠️ reached | ❌ reached | ✅ reached | Defects |
|---|---|---|---|---|---|---|
| 1 | Worktrees | not git (S1) | no window + linked (S3); unknown birth: untestable here, FS records birth | born in window (S13, T) | none; others only (T) | from inside own worktree always ❌ (CL21) |
| 2 | Branches | not git (S1) | no window (S3) | not merged, merged-not-deleted (T, S13) | none; others only (T) | branch born in window, old tip → ✅ (CL19) |
| 3 | Pushed | not git; no remote (S1, S2) | no window (S3) | unpushed in window (T) | all on remote (T, C) | `--since` walk drops window commits → ✅ unlicensed (CL1) |
| 4 | PRs | not git; no GitHub remote (S1, S2) | gh missing/unauth/`pr list` fails; no window + open (T, S3, S7) | created in window; headed by session branch (T, S15) | none open; others only (T) | `--limit 100` silent cap (note) |
| 5 | Session record | not git; no log (S1, S2) | no window; index without detail; committed + dirty (S3, S9) | none in window; dirty only; untracked detail only (S9) | index + detail (T, S9) | false ❌ on the real history via CL1 (C) |
| 6 | Board | not git; no board; hand-kept; roadmap/ without banner (S1, S2, S10) | board.py not found; exit 2; python3 missing (S10) | exit 1 (T, S10) | exit 0 (T) | exit 1 always worded "stale" (CL14); bytecode write (CL10) |
| 7 | Claims | not git; no board (S1, S2) | no window and no id (code path; T asserts neither) | id prefix; date in window (T, S4) | none; others only (T, C) | window unknown + id → ✅ unlicensed (CL3); body-line/capitalised form invisible (CL4); path-named id (CL13) |
| 8 | Floor | not git; no GitHub; no workflows; no remote ref; nothing reached (S1, S2, S7b) | no window; gh reason; `run list` fails; no run; pending; unknown conclusion (S3, S7, T) | failure, timed_out, startup_failure, action_required, cancelled, mixed (S7, T) | success (T); skipped, neutral (S7) | peer's sha chosen → ✅ unlicensed (CL2); skipped as green (CL11) |
| 9 | Reviews | not git; no board; no doctrine dirs (S1, S2) | no window; changed and no ⏳ (S3, T) | never (by design) | none changed; ⏳ added (T, C) | modified ⏳ line counts (CL5); CI/hook paths not doctrine (CL12); drop via CL1 (C) |
| 10 | Bypasses | no transcript (S3) | any hit (T) | never | none (T) | misses and a false positive (CL7) |
| 11 | Tree | not git (S1) | dirty (T, S3) | never | clean (T, C) | — |

Verdict line and exit: 0/1/2 as documented (T, S1, S3); "✅ ready to close" over ten ➖
on a non-git `--root` (CL20).

## Standing checklist V1–V7

- **V1 — no claim stronger than its evidence.** Bitten five times: "a check never reports
  a pass it could not read for" (CL1, CL2, CL3, CL5, CL11); "`board.py --check` … only
  reads" (CL10); "the queue-run claim form" naming an 8-char id (CL4); the brief's
  "(checked)" merge claim (CL16); "ready to close" over nothing applicable (CL20).
- **V2 — re-run every live-proven claim.** Ledger below. Two did not reproduce: the
  brief's merge claim (CL16) and, on the repo's own history, the window machinery (CL1).
- **V3 — a changed rule swept to every mirror.** The check list, states, caps and exit
  codes agree across help, man page, README table, README section, design §7/§10 and
  CHANGELOG, bar the §10 example (CL15). The merge swept the three local-date stamps to
  UTC in README, man page and design note together. The "Not yet installed" CHANGELOG line
  was not swept when the TOOLBOX row landed (CL17).
- **V4 — one fact, one home.** The claim grammar now has three: the board legend, ccclose's
  regexes, and the id form in the design and fixtures (CL4). "Doctrine by function" has
  two: REVIEW.md rule 3 and `DOCTRINE_TOOL_DIRS`, and they disagree on the CI gate and the
  hook (CL12). The board-tool resolution order has two: the hook's (env → config → in-repo)
  and ccclose's (in-repo → beside) (CL10).
- **V5 — no internal contradiction.** Design §7's "not the ref's head" sentence contradicts
  the live-window rule in §4 (CL2); §8's "only reads" contradicts python's behaviour (CL10);
  §10's example contradicts the code and the man page (CL15).
- **V6 — security and privacy on every review.** Done above; `/security-review` discharged
  by grounds; catalogue hosts unreachable, said so.
- **V7 — spawn provenance in brief and verdict.** The brief states its writer, its
  orchestrator, its exposures and the taker's duty; this verdict repeats mine above.

## Findings

Severity: MAJOR / MODERATE / minor / note. Each carries its probe. Counsel is labelled and
sits beneath; nothing is applied (rule 3).

### CL1 — MAJOR. `git log --since` stops the walk; a back-dated commit above the window hides every in-window commit beneath it from all window checks

**Probe.** Against my private clone of this checkout with a synthetic window of
2026-10-16 15:00 → 2026-10-17 00:00 UTC (which holds the four landing commits, committer
times 15:59–21:18 UTC): ccclose printed *Commits 0 in the window*, ❌ *Session record
written — no commit in the window touches docs/SESSIONS.md* (`09a61b4` does), and ✅
*Reviews queued where owed — no doctrine or tool path changed in the window* (the whole
delta changed). ccclose's own form, `git log --branches --remotes --since=<first − 1 day>`,
returns 71 commits and none of the four; `--since-as-filter` with the same bound returns
137 and all four. The cause is git's documented semantics: plain `--since` stops at the
first commit older than the bound and marks its ancestors uninteresting
(`--since-as-filter`, git ≥ 2.37, exists for exactly this). The commit that trips it in
this repo is `4d80321` — committer date 2026-09-14, a descendant of the landing (a
deliberately back-dated insert, by its subject). **Minimal repro** in a fixture: three
commits, in-window → committer-dated ten days earlier → in-window; ccclose reports *1 in
the window* and ❌ on a session record the hidden commit wrote. All six `sinceArg` call
sites share it: pushed (false ✅ *every commit from the window is on a remote*), session
record (false ❌), floor (wrong or no sha), reviews (false ✅), and the two header figures.
Nothing in the output hints that commits were dropped. Fixtures are linear with monotonic
dates, so no test reaches it; mutation M15 (window filter removed) and M14 (slack removed)
survive.

*Counsel.* Replace `--since` with `--since-as-filter` (and state the git floor in the man
page), or drop the pre-filter and filter on `%ct` alone with `--max-count` sanity; add a
fixture with a back-dated descendant; and when `--since-as-filter` is unavailable, print
⚠️ rather than a number.

### CL2 — MAJOR. The floor check passes on a peer's sha in RECORD.md's own grounded case

**Probe (S6).** Fixture: my doctrine commit at −30 min (its floor run *cancelled*), a
peer's push 90 s later (its run *success*), both inside the window; `gh` stubbed per sha.
Past-session form: ✅ *floor green* on the peer's sha. Live-session form: the same, and the
verdict *✅ ready to close*. The design (§7) says the sha is "the newest commit from the
window that the default branch's remote-tracking ref contains, not the ref's head: a later
push by another session evidences a different tree" — but a later push *inside the window*
is chosen, and for a live session the window runs to now, so the ref's head is chosen
whenever anyone has pushed. The *moved on to* suffix only appears for pushes after the
window, so the output gives no hint. This is `RECORD.md`'s 2026-08-09 case — "the close
cited the superseding commit's green — true, but evidence for someone else's tree" —
mechanised into a ✅. Test coverage: the floor tests use one commit per window.

*Counsel.* Check every window commit the remote ref contains (capped), not the newest:
❌ if any has a cancelled or red latest run, ⚠️ if any has none; list the shas. Or, at
minimum, say in the summary that the sha may be a peer's when more than one window commit
reached the ref.

### CL3 — MODERATE. Claims pass with the window unknown when an id is given

**Probe (S3).** `--session no-such-session` (id set, transcript not found) against a board
with a `[~]` claim stamped five minutes ago: ✅ *none of this session's · 1 other live
claim(s) not attributed*. Every other window-dependent check in the same run printed ⚠️
with `NO_WINDOW`. The code warns only when both window and id are absent
(`!w && !sid8 && others.length`); with an id but no window the date rule silently cannot
run and the result is a pass. The row licenses ❌ for a claim dated inside the window —
unknowable here — so the honest state is ⚠️. No test covers claims in the no-transcript
scenario.

*Counsel.* `if (!w && others.length)` → ⚠️, whatever the id; add the assertion to the
no-transcript test.

### CL4 — MODERATE. The claim shape actually on the board at HEAD is invisible to check 7, and the id-bearing form the design and fixtures encode is defined nowhere

**Probe.** The board at HEAD has **zero** `- [~]` checkbox-line claims (grep count over
`docs/roadmap` and the index: 0), and ccclose on the clone reported *0 other live
claim(s)*. Yet one live claim exists — this pass's own, in the pointer item (masked probe:
an indented body line under a `⏳` state line, inline-code `[~]`, a capitalised
seven-letter word, a `9999-99-99 9999 AAA` stamp). Fixture S4 reproduces both misses:
`CLAIM_LINE` requires a bullet, so the body line is not counted at all, and `CLAIM_TIME`
is case-sensitive, so a capitalised stamp on a bullet line goes to "others". The board
legend's own form `(claimed <date>-<HHMM>, wt: <branch>)` is matched; the hyphen, `T`,
space and `*`/indented bullet variants all match. The design's "a `[~]` claim line that
names the session's 8-character id prefix (the queue-run claim form)" and the fixture
`(claimed by queue run <id>)` correspond to no definition I can find in `CONCURRENCY.md`,
the board legend or the queue-run skill (coldsweep over the unbarred tree) — the single
stronger attribution rests on a grammar nobody wrote down. Phase 2 may confirm the
pointer's text; the regex results do not depend on it.

*Counsel.* One home for the claim grammar (the board legend), covering the `⏳`-item case
the 130/020 ruling created ("a pass running under a claim keeps it" — keeps it *how*?);
then ccclose reads `[~]` anywhere in an item, case-insensitively, and the fixtures take
their lines from that legend. This is a doctrine question for the principal before it is
a code fix.

### CL5 — MODERATE. Reviews: a modified ⏳ line counts as a newly queued pointer

**Probe (S8).** A tool path changes in the window and an *existing* pointer line is edited
(closed with its ⏳ left in the title, as the board's own 130/020 wording allows a running
pass to keep it): ✅ *1 doctrine/tool path(s) changed · 2 ⏳ line(s) added to the board*,
with no new pointer queued. A pointer removed outright (⏳ only on a `-` line) correctly
warns. The code counts `+` lines containing ⏳, and a modified line is a `+` line; a board
rebuild that reorders sections has the same effect. Realistic trigger: the application
flow — a session applying rulings to doctrine edits the pointer it is closing; REVIEW.md
requires it to queue a *new* ⏳, and this check would say it did.

*Counsel.* Count a ⏳ `+` line only when no `-` line in the same hunk also carries ⏳ (net
new), or compare pointer *counts* before and after the window.

### CL6 — MODERATE. The ask heuristic misses the plainest close phrasings and every question-form check

**Probe (S12).** Missed: "close the session", "Close this session please", "closing the
session now", "close it out", "is everything committed and pushed?", "is the floor
green?", "are the PRs merged?", "finish up and we are done for today", "are we done?
anything left owing?", "merge the PR". Listed: "clean up the parser code", "tidy up the
imports", "cleanup the test fixtures", "Update the README and push". `OBJECT` needs
"session" to be followed by log/record/entry, so the word *session* alone never counts;
`STRONG`'s `close[- ]?out` needs the two words adjacent; question forms have no `CUE`. The
design's own words: "a missed ask is the costly error".

*Counsel.* Add `clos(?:e|ing)\b.{0,20}\bsession` and `close it out|finish(?:ing)? up|done
for (?:today|the day)` to `STRONG`; add a question-form rule (`^(?:is|are|did|have|has)\b`
with an `OBJECT`); drop `clean[- ]?up`/`tidy[- ]?up` from `STRONG` unless an `OBJECT` is
present.

### CL7 — MODERATE. The workaround list misses the contention workarounds the house names, and flags ADR 0007's own signing format

**Probe (S11).** Missed: `git commit -n` (the documented short form of `--no-verify`, the
one flag the list does catch); `git pull --rebase --autostash` (the hazard `CLAUDE.md`'s
read order opens with); `git checkout -- .`, `git restore .`, `git clean -fd` (the
"wholesale revert destroyed a sibling's in-flight work" class `CONCURRENCY.md` grounds the
board split on); `git stash -u`, `git stash drop`; `git branch -D`; `git worktree remove
--force`. False positive: `git -c gpg.format=ssh commit -S` is reported as *signing
switched off* — it switches SSH signing *on* (ADR 0007). Mike's acceptance shape was "no
work arounds when issues come up like contention on commits"; of the shapes that resolve
contention on a shared checkout, two of eight are listed.

*Counsel.* Add `\bcommit\b[^|;&]*\s-n\b`, `--autostash\b`, `\bgit\s+(?:checkout|restore)\s+
(?:--\s+)?\.`, `\bgit\s+clean\b`, `\bgit\s+stash\s+(?:-u|--include-untracked|drop)`,
`\bbranch\s+-D\b`, `worktree\s+remove\b[^|;&]*--force`; narrow the signing pattern to
`gpg\.format=` without `ssh`, or drop it.

### CL8 — MODERATE (design altitude). Output designed for pasting into public records prints the operator's home path and the principal's words; the design enumerates no threats

**Probe (S13, S16, C).** The Transcript row prints the transcript's absolute path (which
on a workstation encodes the home directory and user name), the Repo row the absolute
checkout path, and every worktree item an absolute path; the asks list prints up to 240
characters of each matching prompt verbatim. `RECORD.md` says the output "gets pasted into
records"; this repo's records are public, and `pathscan`'s scope excludes record stores
by design, so a pasted home path is caught only by the local hook's user term list, if the
user name is on it. The design note has no threat enumeration (lens 4's build-time
obligation); §8 names read-only and network but not what the output *exposes*, nor the
code it executes (CL10), nor the env-selected binary.

*Counsel.* Print paths relative to `~` and the repo root as its basename; print the asks
as refs with a short quote and say in the heading that they are the principal's words;
add a §8 paragraph naming the three trust surfaces.

### CL9 — MODERATE (harvest). No doctrine or skill site tells a closing session to run it

**Probe.** Coldsweep for `ccclose` outside the delta: `CHANGELOG.md`, the index line of
this pointer, the TOOLBOX row, three board items, two cctranscript comments. `RECORD.md`'s
close declaration, `CONCURRENCY.md`, `skills/session-onramp`, `skills/queue-run` and
`CLAUDE.md`'s closing line do not name it. The tool exists to be "code that every session
uses when I ask it to close out"; a tool that exists is not a tool that is run
(`PROPAGATION.md`'s category error). The one site that names it says *installed*.

*Counsel.* One sentence in `RECORD.md`'s all-clear bullet ("run `ccclose`; the all-clear
carries its lines") and one in the queue-run skill's per-item close — doctrine edits, so
the principal's; queue their own pointer with the application, per REVIEW.md.

### CL10 — minor. "board.py --check only reads" is false in detail; the executed-code surface is undocumented and resolved in the reverse order to ADR 0008's hook

**Probe.** Clean clone, no `__pycache__`; one ccclose run; `tools/__pycache__/` appears
with five `.pyc` files (board.py imports `harvestscan`, `pointerscan`, `filewalk`,
`allowmarker`, `report`). `.git` was untouched (file list, sizes and mtimes identical;
index hash identical; no lock files) — the read-only claim holds for git. With a
`python3 -B` shim the directory does not appear. atelier ignores `__pycache__/`; a repo
that does not would read dirty after its own close check. Separately: ccclose runs the
checked repo's own `tools/board.py` first and atelier's copy second; the hook resolves
`ATELIER_TOOLS` → `hooks.atelierTools` → in-repo, and carries a trust note; ccclose's man
page has none. Test gap: mutation M1 (drop `--no-optional-locks`) survives.

*Counsel.* `run('python3', ['-B', tool, …])`; one trust sentence in NOTES; consider the
hook's resolution order, or say why not.

### CL11 — minor. `skipped` and `neutral` conclusions count as green

**Probe (S7).** A single workflow with conclusion `skipped` → ✅ *1 workflow(s) green*.
A skipped floor run executed nothing, so nothing was read for the pass. `neutral` is the
same shape.

*Counsel.* Move `skipped` (and arguably `neutral`) to ⚠️ with the reason.

### CL12 — minor. The doctrine-path list omits the CI gate, the hook and the floor declaration

**Probe (S8c).** `.github/workflows/ci.yml` and `.githooks/pre-commit` change in the
window: ✅ *no doctrine or tool path changed in the window*. REVIEW.md rule 3 names "a CI
gate" as doctrine by function; ADR 0008 makes the hook the enforcement plane;
`.atelier-floor.json` scopes it. `CLAUDE.md` and `docs/roadmap/README.md` (the legend) are
in the same class.

*Counsel.* Add them to `DOCTRINE_TOOL_DIRS` (as files where needed), and point the list at
rule 3 as its source.

### CL13 — minor. A path-named `--session` seeds the id prefix with a date

**Probe (S5).** `--session …/2026-10-17-notes.jsonl` → id `2026-10-17-notes`, prefix
`2026-10-`; a claim stamped `claimed 2026-10-01-…` by another session is attributed and
❌'d. The cheap direction, but wrong attribution all the same.

*Counsel.* Apply the prefix rule only to a prefix that looks like a session id (hex or
UUID head), and only when the id came from an id, not a file name.

### CL14 — minor. Board exit 1 is always worded "stale"

**Probe (S10).** `board.py` exits 1 for item-grammar problems with a current index; the
summary says *is stale against docs/roadmap/*. The listed lines carry the truth.

*Counsel.* "board.py --check failed (stale index or item problems); see lines".

### CL15 — minor. Design §10's verdict example does not match the emitted line

**Probe.** Emitted: `✅ ready to close · 0 fail · 0 unknown or partial · … · 0 ask(s) to
answer`; §10's example uses a colon, "unknown" and "asks". The man page's example matches
the code.

### CL16 — minor (on the brief). The merge did change delta paths

**Probe.** `git diff --stat 4eda680 6ccbc7a` on the delta paths: README, design note and
man page each change one line — the stamp `2026-10-17` → `2026-10-16` (local date to UTC,
the right fix). The brief's "(checked)" did not reproduce; the brief's account of the work
is the author's framing to test (rule 1), and this is the only instance I found.

### CL17 — minor. CHANGELOG "Not yet installed onto the machine's path" not swept

**Probe.** `09a61b4` ("install ccclose") added the TOOLBOX row three hours after the
CHANGELOG entry; the entry still says it is not installed. Both are dated 2026-10-16.

### CL18 — minor. Test gaps shown by mutation

**Probe.** 23 flips in the private clone, each followed by the test file: killed 17;
survived M1 (`--no-optional-locks` removed — the read-only contract's one mechanical
guard), M7 (an unknown conclusion passes), M14 (since slack removed), M15 (window filter
removed), M16 (upper bound exclusive), M17 (unknown birth time passes — that branch is
dead under test on a filesystem that records birth times, as this one does). Fixtures are
linear with monotonic dates and one commit per window (CL1, CL2).

### CL19 — minor. A branch created in the window with an old tip passes

**Probe (S14).** `git branch fresh-but-empty` at an old main: ✅ *none with a tip in the
window · 1 other(s) not attributed*; the reflog's first entry records the creation time.

### CL20 — minor. "unknown" and "ready to close" where the figure was read, or nothing was

**Probe (S16, S1).** A transcript with no assistant record prints *models unknown* (the
figure was read; it is empty), inverting the unknown-vs-0 rule; a `--root` that is not a
git repository prints *✅ ready to close · 0 fail · 0 unknown or partial · 1 pass · 10 not
applicable* — a strong verdict over ten ➖, exit 0.

*Counsel.* Print *none* for an empty read figure; when the repo is not git or the session
is unknown, phrase the verdict as *nothing applicable to check* rather than *ready*.

### CL21 — note. Run from inside its own worktree, check 1 always fails

**Probe (S13).** Correct (the worktree still exists), but neither the design nor the man
page says where to run the check from; a session in a worktree will meet a ❌ it cannot
clear without leaving.

### CL22 — note. A timed-out `gh auth status` reads as "not installed"

**Probe.** Code reading: `run()` returns `code: null` for both ENOENT and a timeout;
`ghReady` maps `null` to *not installed*. Twenty seconds is generous, so rare.

### CL23 — note. The transcript-store assumption

`$CLAUDE_CODE_SESSION_ID` is set in this cloud shell, as §4 assumes. A `~/.claude/projects`
store exists on this host too (the orchestrator's correction); I did not look at it, so
nothing is claimed about ccclose's behaviour against it.

### CL24 — note. The home question (lens 1, A8)

`instruments/` is the right home by ADR 0006's purpose rule; what gives the tool a
doctrine role is that its ✅ lines are cited as RECORD's evidence, and the right response
to that is this review and the design's §14 posture, not a move to `tools/`. No action.

## Overall

**FAIL — 2 MAJOR · 7 MODERATE · 11 minor · 4 note.** The architecture is right — a fresh
read, honest *unknown* states, heuristics printed on every run, a sound test harness —
and the fixes for both MAJORs are small. But as landed the tool's ✅ is false on this
repository's own history (CL1: every window check answers on a truncated walk, with no
hint) and in the exact scenario `RECORD.md` grounds the floor rule on (CL2), so its pass
cannot yet be cited as the evidence the close declaration requires. Both are the
principal's to decide (rule 3); counsel is beneath each.

## Re-run ledger

| Claim | How re-run | Result |
|---|---|---|
| `node --test instruments/ccclose.test.js` passes | run once, `TMPDIR` in scratch, fake HOME (the harness's own) | 23/23 pass, 3.5 s |
| The instruments suite passes as CI runs it | `node --test instruments/*.test.js` once, foreground | 447 tests, 431 pass, 16 skipped, 0 fail, 22 s |
| Man page well-formed | `mandoc -T lint instruments/man/ccclose.1` | clean, exit 0 |
| `--help` one screen, points at man | `node instruments/ccclose --help` by path | 16 lines, names `man ccclose`, exit 0 |
| Floor at HEAD, CI plane | `python3 tools/floor.py --plane ci --root .` at HEAD `ec20c7d` | exit 0; pathscan 1 advisory (an ADR, not this delta); secretscan 23 advisory; leakscan structural-only |
| Floor at HEAD, hook plane | `floor.py --plane hook --root . --tools tools` at `ec20c7d` | BLOCKED by leakscan only (no user term list in this container, by design — 115/350); every other gate green |
| Read-only: `.git` untouched | clone; snapshot file list/sizes/mtimes, index hash, locks; run; snapshot | identical; no locks; stderr empty |
| Read-only: nothing else written | same probe, tree file list + `__pycache__` search | `tools/__pycache__/` with five `.pyc` appears (CL10); gone with `python3 -B` |
| Short `--commit` sha returns nothing (stub premise) | anonymous `GET /repos/…/actions/runs?head_sha=` with 7-, 12-, 39- and 40-char shas of `6ccbc7a` | the 40-char sha: 1 run (floor, success, push, main); the 7-, 12- and 39-char shas: 0 |
| Landing's floor at the pushed head was green | same API for `6ccbc7a` and `09a61b4` | both: floor success on main; `4eda680` and `ef3673a` have no run (never pushed as a branch) |
| Merge changes none of the delta paths (brief) | `git diff --stat 4eda680 6ccbc7a -- <delta>` | three files, one line each (CL16) |
| `cea247e` is the only later change; nothing after `99f4c2a` | `git log 99f4c2a..HEAD -- <delta>` | only `09a61b4` (TOOLBOX) |
| `$CLAUDE_CODE_SESSION_ID` is set | `echo` in this shell | set |
| Each design-table state reachable | fixture drive (18 scenarios) + skew fixture + S6 | table above; `git worktree list failed`, `for-each-ref failed`, `git log failed` and the board-history-unreadable ⚠️ states not reached by fixture (need an injected git failure) |
| Floor check against the real host; live transcript store; another repo | — | not re-driven here (relayed): no authenticated `gh`, no store read, no other repo |

## Follow-up checklist

- [ ] CL1 — `--since-as-filter` (or no pre-filter) at all six call sites; a back-dated
      fixture; a git-floor note in the man page.
- [ ] CL2 — floor check over every window commit the ref contains; summary names a
      possible peer sha.
- [ ] CL3 — claims ⚠️ whenever the window is unknown and live claims exist.
- [ ] CL4 — principal: settle the claim grammar for `⏳` items in the board legend; then
      ccclose reads it case-insensitively anywhere in an item; fixtures from the legend.
- [ ] CL5 — count net-new ⏳ lines.
- [ ] CL6, CL7 — the regex additions and the signing false positive.
- [ ] CL8 — `~`-relative paths, basename root, asks as refs with short quotes; a §8 threat
      paragraph.
- [ ] CL9 — principal: a sentence in `RECORD.md`'s all-clear and in the queue-run skill
      (doctrine edits; their own pointer).
- [ ] CL10 — `python3 -B`; a NOTES trust sentence; resolution order decided.
- [ ] CL11–CL20 — as counselled; CL16/CL17 are record fixes.
- [ ] CL18 — tests for `--no-optional-locks` (assert no `index.lock` write), unknown
      conclusions, the window bound, a skewed history, and claims with no window.
