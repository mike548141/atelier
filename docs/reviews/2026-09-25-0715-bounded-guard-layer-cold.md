# Cold pass — the bounded-guard-layer conversion — fourteen tools streamed, capped or measured, plus the measurement harness

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/370-rule-4-cold-pass-queued-the-bounded-guard-layer.md`.
**Why it earns a review:** fourteen guards that every commit in the fleet runs
were rewritten in one day to bound memory and time; a per-line window or a cap
that silently drops a finding turns a guard into a green light, and the harness
that measured them was itself wrong once on the platform CI runs on.

## Spawn provenance

- **Author of the work under review:** the session(s) that landed the commits
  named under *What the work is*. This brief-writer was not that session, was
  neither started nor instructed by it, and has edited none of the delta's
  paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-09-20 and
  re-pointed on 2026-09-24 with the prompt "Please deliver all fable dependent
  work, and work that would be best delivered using fable", on the Fable tier
  (`claude-fable-5-1`), orchestrating this batch of twenty rule-4 passes. It
  wrote this brief from the queue pointer, the landing commits' subjects and
  file lists, and the delta paths' names; it did not open the intent record or
  any prior verdict on these surfaces.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree, commits
  the reviewer's phase-1 findings unrevised, then releases the sibling's text by
  message; the reviewer appends a reconcile section; the orchestrator folds the
  sibling in and updates the pointer. The orchestrator forms no finding and
  writes no severity. Both seats are Fable, so the off-tier clause is not
  invoked; the shape is stated anyway so the record is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the `docs/SESSIONS.md` index entries of 2026-09-11 to 2026-09-19
  (the last three summarise the 2026-09-18 and 2026-09-19 runs in the authors'
  words); the first 30 lines and the last ~3,000 characters of
  `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md`, read during an
  interrupted-session sweep on 2026-09-20; every queued `⏳` pointer on the board
  in full, including each pointer's own "lens that matters" paragraph — that
  paragraph is the author's framing and has been moved to this pass's sibling;
  the pass file `docs/reviews/2026-08-17-1000-coldsweep-cold.md` in full (brief
  and verdict) and lines 1–80 of
  `docs/reviews/2026-08-21-0820-pointing-up-cold.md`, both as formatting
  templates; the landing commits' subjects and `--stat` file lists (never the
  diffs); and, as doctrine read at onramp, `docs/method/CONCURRENCY.md` §§ *On a
  split board*, *Claiming at a dirty primary checkout* and *Surviving an
  interrupted session*, `docs/method/REVIEW.md` and `docs/method/00-APEX.md` at
  HEAD. Per-pass additions are marked ⚠️ under *Deferred reading*.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `886524f` — `leakscan`, `conflictscan` streamed
- `e6c9265` / `ca4eaac` — `sizescan`, `datescan`, `wrapscan`, `spellscan`
- `365a94b` / `a6cd2f1` — `linkscan`, `reviewscan` bounded; `publishscan` pinned
- `994bf4b`, `0bca6eb`, `8426f3e` — `memprobe` isolation rewrite (fresh
  interpreter, not the caller)
- `0008d4b` / `2ccc96c` — `licenscan`, `pathscan` bounded; `board`,
  `pointerscan` pinned
- `3d73e49` / `a557315` — `stampscan`, `blockscan`, `pins`, `floorfleet`,
  `signfleet` size-gated; `signscan` measured
- ⚠️ `db9a785` (2026-09-20, `160/410`) later added one pruning line to eleven of
  these walks; separately queued. `160/350` covers `secretscan` and the first
  `pathscan` change and is separately queued
- ⚠️ `c1a2f12` / `a59e5d0` (2026-09-21 NZ; queued separately as `160/420`) later
  single-sourced every scanner's `_walk_files` into `tools/filewalk.py`; at HEAD
  the per-scanner walks are thin wrappers. Review this delta's behaviour **as it
  stands at HEAD** and say whether the single-sourcing preserved it — the *diff
  the eleven walks* check becomes a diff of the eleven wrappers and their
  parameters

Delta paths:

- `tools/memprobe.py` and `tools/test_memprobe.py` — the isolation rewrite
- the streaming conversion in `tools/leakscan.py`, `conflictscan.py`,
  `sizescan.py`, `datescan.py`, `wrapscan.py`, `spellscan.py`, `linkscan.py`,
  `reviewscan.py`, `pathscan.py`, `licenscan.py`, `stampscan.py`
- the size-gate additions in `tools/blockscan.py`, `pins.py`, `floorfleet.py`,
  `signfleet.py`
- every corresponding `test_*.py` `BoundedMemory` class

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

For each converted tool: does any window, cap or size gate change a *verdict*
(exit code, tally) rather than only a listing, and does the tool say so when it
does? Are the ceilings each test asserts grounded in a property of the file
class the tool scans, or fitted to what one machine measured on one day — read
each `BoundedMemory` class for where its number came from. Do the copies of
`_walk_files` agree with each other at HEAD (diff them; a harness-level `diff`
across the eleven is the whole of that check). Does `memprobe` now measure the
child and only the child on both Darwin and Linux (reason from the code; CI's
floor run at the landing SHA is the Linux evidence — read it via `gh run view`).
**Non-goal:** the commissioning items.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   conversion's premise is that a guard can be made bounded without changing
   what it catches — for each tool, name the behaviour most likely lost and
   probe it. Ask whether eleven hand-copied walks is the right shape at all, as
   counsel.
2. **Correctness & quality.** Read every changed tool in full. Run every
   selftest and the full suite. For at least the four tools whose windows are
   smallest, construct a file that straddles the window and record the result.
   Run `memprobe` on `python3 -c pass` and on one real scanner and say what it
   reports on this platform.
3. **Completeness / harvest.** Which tools in the registry were *not* converted,
   and why (the pointer names fourteen; count the registry). Does
   `tools/README.md` describe each bound? Does `CONTRIBUTING.md` tell a
   contributor how to keep a new scanner bounded?
4. **Security & privacy** — mandatory. The guards read every file in every repo.
   Check no conversion introduced a temp file, a partial read that leaves a
   handle open, or a path by which a size gate can be used to *skip* a file a
   guard should have read (a secret in a file just over the gate). `memprobe`
   spawns subprocesses — check its argument handling. The house scanner is
   discharged by grounds (landed delta; pending = other passes' drafts) — say
   so, and deliver the OWASP-class read by hand.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- every changed tool's `--selftest`; the full Python suite once (`python3 -m
  unittest discover -s tools`), with its count and wall time recorded
- `python3 tools/memprobe.py` on `python3 -c pass` and on one scanner over the
  worktree — one heavy process at a time
- the floor on both planes at HEAD; `gh run view` on the landing SHAs' floor
  runs for the Linux figures
- a `diff` of the eleven `_walk_files` bodies

## House rules for this run

- You work in the shared review worktree
  `/Users/mike/worktrees/atelier-review-batch-0925` (branch
  `review-batch-0925`), read-only except for THIS brief file. Other reviewers
  are working there at the same time on their own briefs; never open another
  `docs/reviews/2026-09-25-0715-*` file — it is another pass's framing.
- Run **no git command that writes** in the worktree (no add, commit, stash,
  checkout, worktree, reset, clean). Read-only git (`log`, `show`, `diff`,
  `blame`, `branch -r`) is fine. Mutation probes, checkouts of older commits,
  scratch children and scratch linked worktrees go in your own clone: `git clone
  <worktree> <scratchpad>/<PREFIX>/probe` under the session scratchpad, named by
  your prefix so parallel reviewers do not collide.
- One heavy process at a time on this machine: run the full Python suite
  (`python3 -m unittest discover -s tools`, in the foreground, ~minutes) at most
  once, never scan any tree outside the worktree or your scratch clone, and
  never point a scanner at the machine's other repos.
- `/security-review` is **discharged by grounds** for this batch: it reads the
  session's pending diff, which in the shared worktree is other passes' unstaged
  drafts, and this is a landed-delta review. State that line in your lens-4
  answer and deliver the code-altitude read by hand, checked against the OWASP
  catalogue where the work has a code surface.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" tree-wide,
  and would block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ
  English. Never quote a secret, a placeholder token, an email address or any
  personal detail — this repo is PUBLIC; describe, don't quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/370-rule-4-cold-pass-queued-the-bounded-guard-layer.md`
(it carries the author's own lens hints), and:

- `docs/sessions/2026-09-19-0038-queue-run-the-morning-rulings.md` and
  `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md`
- the board items `docs/roadmap/020-*/370-*.md`, `020-*/380-*.md`,
  `020-*/400-*.md`, `docs/roadmap/115-*/080-*.md`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/370-rule-4-cold-pass-queued-the-bounded-guard-layer.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `BL`: `BL1`, `BL2`, …) and severities (MAJOR / MODERATE
/ minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger with the commands and their results, and a follow-up checklist.
Then STOP and report to the orchestrator that phase 1 is written. Do not open
the sibling (it is not in the tree); do not edit the queue pointer, the board,
or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
records, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

The author is not the taker, so record every finding and apply nothing; counsel
on fixes is welcome, labelled as counsel.

---

## Verdict — cold pass, phase 1 (2026-09-26 UTC)

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 6 minor · 4 notes.**

### Provenance, repeated

- **Spawn.** A fresh Fable subagent (`claude-fable-5-1`, tier checked at claim), spawned by
  the batch orchestrator with this brief as its only framing. I am not the author's session
  and was not instructed by it. Reviewer-plus-orchestrator shape, disclosed above; both seats
  Fable, so the off-tier clause is not invoked. The orchestrator formed no finding.
- **Where.** The shared worktree `/Users/mike/worktrees/atelier-review-batch-0925` at
  `f81a98f`, read-only; probes and a scratch clone under my own scratchpad area (`BL/`).
  No git command that writes ran in the worktree.
- **What I read.** This brief; `docs/method/REVIEW.md` and `00-APEX.md`; every delta path at
  HEAD in full (`memprobe.py`, `test_memprobe.py`, `filewalk.py`, the readers and walks in
  the eleven streamed scanners, the size gates in `blockscan`/`pins`/`floorfleet`/`signfleet`,
  and all nineteen `BoundedMemory` classes); `.githooks/pre-commit`, `tools/floor.py`,
  `.github/workflows/ci.yml`, `tools/README.md`, `docs/build/templates/CONTRIBUTING.md`;
  `git show --stat` of the twelve landing commits and the full diffs of `886524f`, `0008d4b`
  and `3d73e49`; CI run metadata and failure logs via `gh`.
- **Exposure, disclosed.** (a) The full commit messages of `0008d4b` and `3d73e49` carry the
  author's own account of the work (measurements, what was left undone); I read them before
  designing the straddle probes. (b) `git log --oneline -1` on the day's CI SHAs printed the
  *subjects* of several session and board-close commits (no bodies). (c) A longest-line
  probe over `docs/**/*.md` counted line lengths in `docs/SESSIONS.md` (it holds the longest
  line, 6,409 chars); no content was printed. (d) `coldsweep` hits printed single matching
  lines from four unbarred board items (`160/350`, `160/420`, `115/220`, `020/390`),
  `CHANGELOG.md` and the generated `ROADMAP.md` index — refs only. I did not open
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any prior verdict, the queue
  pointer, the four barred items, or the sibling. Every sweep ran with `--also-exclude` for
  all five barred items (exclusion set printed by the tool: 351 files barred of 857).
- **`/security-review`** is discharged by grounds: it reads the session's pending diff, which
  in this shared worktree is other passes' unstaged drafts, and this is a landed-delta review.
  The code-altitude read was delivered by hand (lens 4).

### Lens 1 — approach and assumptions

Load-bearing assumptions, named by me and probed:

1. *A guard can be bounded without changing what it catches.* **Half true.** The delta uses
   three mechanisms, and only one preserves verdicts. The **windowed readers** (leakscan,
   conflictscan at 4 MiB + 64 KiB overlap; linkscan, reviewscan at 256 KiB + 4 KiB) keep every
   match reachable and count findings past the 50,000 cap into the exit code — a genuine
   bound with no verdict loss (probed: a token in the overlap is found — twice, BL3). The
   **truncation readers** (datescan, wrapscan, spellscan, sizescan, stampscan at 8 KiB per
   line) never scan the tail of an over-long line, so a finding there exits 0 (probed, BL1).
   The **size gates** refuse or skip whole files (blockscan exit 2; pins/floorfleet/signfleet
   skip with a stderr line; licenscan truncates at 8 MiB and counts it).
2. *"Every guard, regardless of input size" covers the plane every commit runs.* **False.**
   The tree walk was converted; the hook plane's `--staged` path in leakscan and conflictscan
   still captures the whole `git diff --cached` and splits it in memory (probed: ~6× growth
   with staged bytes, BL2). The CHANGELOG's "every guard now runs in bounded memory" is
   therefore an overclaim on the hook.
3. *Whole-process peak RSS, measured from outside, is the right instrument.* **True**, and
   the CI history is the proof: four consecutive runs on 2026-09-20 (`48c181f`, `692563a`,
   `40a4356`, `0bca6eb`) failed only in `test_memprobe`/`test_datescan` with readings of a
   bare `python -c pass` at 187 MB and 254 MB — the forking parent's own footprint, exactly
   as the isolation docstring says — and `8426f3e` went green once the measurement moved
   one interpreter down. On Darwin my probe shows the effect absent (a 200 MB ballast in the
   caller moved the direct-path reading by −0.2 MB), so the isolation layer is a Linux fix
   that costs nothing here. Residual: on Linux the inner interpreter's own footprint is still
   inherited as a constant offset; harmless for growth assertions, worth knowing for the
   absolute ones (BL9).
4. *8 KiB is two-plus orders past any real line.* True for hand-written prose (this repo's
   longest doc line is 6,409 chars, and that is a records file the prose scanners exclude),
   but generated Markdown — index lines of links, tables, an inlined image — is the class
   where it is closest, and the margin at HEAD is under 2×, not two orders.
5. *Growth between two sizes is the right regression signal.* Yes; it cannot catch a large
   constant, but the constant is not the incident's shape. What it does not tolerate is a
   loaded host: the classes' 60 s ceilings, not their memory bounds, went red under six
   concurrent suites (BL12).
6. *Eleven hand-copied walks was the wrong shape.* Agreed, and `115/080` part 1 has since
   single-sourced the walk; at HEAD the eleven wrappers are one-line calls into
   `filewalk.walk_files` with a per-guard skip set (ten identical ten-name sets, licenscan's
   twelve-name set) — a `diff` of the eleven bodies shows only the skip-set name. The
   single-sourcing preserved the behaviour, including the E9 `.git`-file prune. **Counsel:**
   the *readers* are still hand-copied — five copies of the truncation reader, four of the
   windowed reader, one fence-aware variant — and BL3 is a defect copied verbatim from
   secretscan into leakscan; the next reader bug will land in N places too.

### Lens 2 — correctness and quality

- All twenty `--selftest`s exit 0 on this box (ledger). The floor exits 0 on both planes at
  HEAD; the ci-plane board renders every tally line, including the new `over-long line(s)
  scanned truncated` and `beyond the 50000-finding cap` counters, all zero over this tree.
- Straddle probes on the four smallest windows and beyond (ledger): datescan, spellscan and
  wrapscan each return **exit 0** with a real finding past the 8 KiB cap, and their `--json`
  carries no truncation field at all; stampscan reports two lines that differ only past the
  cap as `identical`; sizescan is unaffected (its checks are line-start anchored, and a `[x]`
  item on a 9 KB line still gates). leakscan and linkscan both **double-report** a token that
  sits in the overlap region of the first window cut.
- The `--staged` probe: leakscan grows 148.5 MB and conflictscan 136.4 MB of peak RSS for
  24 MB more staged content — linear, roughly six times the input.
- `BoundedMemory` ceilings, read one by one: leakscan, conflictscan (4× window+overlap),
  sizescan, datescan, wrapscan, spellscan, stampscan (8× chunk+line cap) and blockscan (5× the
  cap delta) are grounded in the design constant. linkscan, reviewscan and publishscan use an
  8 MB literal justified as headroom over a measured noise floor and below the measured
  pre-fix growth — a discriminating bound, honestly labelled. pathscan (12 MB, below the
  predicted 18 MB pre-fix growth) and licenscan (20 MB, below ~36 MB) likewise. Two are
  fitted rather than grounded: pointerscan's per-item bound is "roughly 2× the measured
  rate", and linkscan's single-line test allows 100 MB of growth for a 24 MB longer line,
  loose enough to pass a reader that had quietly gone back to scaling (BL7). board's
  2 KiB/item is 4× measured and argued from the O(n²) alternative — acceptable.
- memprobe's CLI accepts only `--selftest`; any other argument exits 0 silently (BL5).

### Lens 3 — completeness and harvest

- Registry count at HEAD: **15** scanners (`floor.py --list`). This delta streamed or
  bounded ten of them (leakscan, conflictscan, linkscan, reviewscan, sizescan, datescan,
  wrapscan, spellscan, pathscan, licenscan) and pinned three as measured (publishscan, board,
  pointerscan). The other two are handled under separate items: secretscan (`160/350`) and
  harvestscan (`020/400`, its quadratic pass now bucketed at HEAD). Outside the registry the
  delta bounded stampscan, blockscan, pins, floorfleet and signfleet and measured signscan.
  Untouched and unconverted: `coldsweep.py` (a reviewer's instrument, not a guard; it reads
  each file whole via `read_bytes`), `floor.py` itself (buffers a scanner's whole stdout for
  the advisory-count scanners — bounded by the 50,000-finding cap, so acceptable), and
  `worktree.py` (reads no files). So "fourteen" is the honest count of guards converted or
  pinned here, plus the harness.
- `tools/README.md` documents the bounds for **secretscan only** (its `Bounded memory`
  section) plus the memprobe harness. The 8 KiB line cap, the 256 KiB windows, leakscan's and
  conflictscan's 4 MiB windows and 50,000 cap, licenscan's 8 MiB truncation, blockscan's
  4 MiB refusal and the fleet tools' 2 MiB caps live only in module docstrings and comments.
  The README's wrapscan/datescan/spellscan sections still describe whole-file behaviour and
  say nothing about the cap (BL4).
- There is no root `CONTRIBUTING.md`; the scaffold template at
  `docs/build/templates/CONTRIBUTING.md` says nothing about keeping a new scanner bounded.
  The only contributor guidance is one README sentence pointing at
  `test_secretscan.py::BoundedMemory` as "the pattern every guard is meant to reuse". Nothing
  mechanical requires a `BoundedMemory` class for a new registry entry (BL4).

### Lens 4 — security and privacy

`/security-review`: discharged by grounds (stated above). Hand read against the OWASP
classes that reach this surface — injection via subprocess arguments, unsafe file handling,
resource exhaustion, and fail-open paths:

- **Temp files.** Only memprobe creates any, and they are anonymous `TemporaryFile`s
  (unlinked at creation) holding the child's stdout/stderr; tests use `mkdtemp` with
  cleanup. Nothing writes into the scanned tree.
- **Handles.** Every reader opens with `with`. The generator readers hold the file open for
  the life of the generator; reviewscan's `scan_record`/`scan_brief` return mid-iteration on
  the first hit, so the handle closes on the generator's finalisation — prompt under CPython's
  refcounting, deferred under a tracing GC. Not a leak on the interpreter this repo runs.
- **Size gates as a skip path.** The three boundary scanners have no size gate at all
  (windows plus overlap, cap counted into the exit code) — no file over any threshold escapes
  them. licenscan truncates at 8 MiB and counts it; an SPDX header sits at the top of a file,
  so the gate cannot hide one. blockscan refuses an oversized mapped file with exit 2 —
  fail-closed. pins treats an oversized `CLAUDE.md` as `no-pin`, which is actionable under
  `--check` — fail-visible. floorfleet treats an oversized local file as absent — renders as
  unwired, fail-visible. signfleet treats an oversized `floor.yml` as "no floor.yml" and the
  child ends `skip`, which `--check` does not count as a failure — the one gate that lands on
  the quiet side, on a fleet observability tool rather than a commit gate (BL8).
- **memprobe's subprocesses.** `argv` reaches `Popen` as a list, never a shell; `cwd` is
  passed through unchanged; the isolated hop serialises its arguments as JSON on argv and
  adds only memprobe's own directory to `sys.path`; the live-RSS poll calls `ps` with fixed
  arguments. No injection path. The 900 MB kill and the timeout are present in every
  `BoundedMemory` class. One contract gap: if the *inner* isolated interpreter hangs past
  `timeout + 60 s`, `subprocess.run` raises `TimeoutExpired` rather than returning a
  `ProbeResult` — the "never raises on a hang" promise holds for the target, not the hop (BL9).
- **Privacy.** No scanner output is written anywhere new; leakscan's redacted excerpt shape
  is unchanged; the tests' fixture identities are fictional and marked.

### Findings

**BL1 — MODERATE. The 8 KiB truncation readers change the verdict, and only the human
tally says so.** datescan, spellscan and wrapscan are `enforced` on both planes of atelier's
floor. A relative-time word, a US spelling, or a wrap violation whose evidence sits past
character 8,192 of a physical line is never scanned: the scan exits 0, the board prints
`✅ enforced`, and the only trace is `1 over-long line(s) scanned truncated` in the prose
tally — absent from `--json`. wrapscan additionally *flips* an exemption: an 8,300-char
unbreakable token followed by prose is a finding pre-fix and `clean` post-fix (the retained
prefix is a single token), which the module comment names as an "honest residual" but the
README does not. stampscan reports two region lines that differ only past the cap as
`identical`, exit 0 (its `--json` does carry `lines_truncated`). sizescan is unaffected. The
boundary scanners solved the same problem without verdict loss (windows + overlap), so the
premise that a bound need not change what a guard catches was available and not applied
here. Exposure at HEAD is low — no doc line in this tree is within 25% of the cap — but this
is precisely the "cap that turns a guard into a green light" the brief names, and it is a
one-line adversarial input. Probes: `datescan`, `spellscan`, `wrapscan`, `stampscan`,
`sizescan` in the ledger. *Counsel:* either window with overlap as the boundary readers do,
or fail closed — emit an `over-long-line` finding of its own kind on a blocking plane (for
wrapscan a >8 KiB prose line is a wrap violation by definition), and put `lines_truncated`
into every `--json` document so a machine reader sees what the prose tally shows.

**BL2 — MODERATE. The hook plane is not bounded: `--staged` still buffers the whole diff.**
leakscan and conflictscan (and secretscan, out of this pass's scope) run `--staged` on every
commit in the fleet. That path is unchanged by the conversion: `staged_added_lines()`
captures `git diff --cached` whole, splits it, re-joins each file's added lines into one
string, and `scan_lines` then `splitlines()` it again. Measured in the scratch clone: staging
8 MB then 32 MB of leak-free text, leakscan peaks at 66.9 MB then 215.4 MB (+148.5 MB for
+24 MB), conflictscan 59.3 MB then 195.7 MB (+136.4 MB) — linear at roughly six times the
staged bytes. A commit that adds a 300 MB text dump costs the hook ~2 GB on the developer's
machine, the incident's shape on the other plane. No verdict changes; the defect is the
overclaim: `CHANGELOG.md` line 9 says every guard now runs in bounded memory, and the tree
plane is the only one that does. *Counsel:* stream `git diff --cached` through `Popen` and
feed each file's added lines to the scanner as they arrive, reusing the windowed reader on
the joined text rather than materialising it; pin with a `BoundedMemory` case that stages
two sizes, which is a four-line addition to the existing classes. The same fix belongs in
secretscan under `160/350`.

**BL3 — minor. A token in the first window's overlap is reported twice.** leakscan's dedupe
only engages from the second window of an over-long line onward: the first window's findings
are `extend`ed without entering `seen_in_window`, so a match inside the 64 KiB carried into
window two is appended again. Probe: one placeholder address placed 2,000 chars before the
4 MiB cut yields `2 finding(s)`, both on line 1, in prose and in `--json`. linkscan has no
dedupe at all and double-reports a broken link inside its 4 KiB overlap the same way. Exit
codes are right; the tally and `--json` counts are wrong, and a reader chasing "2 findings"
finds one. The leakscan shape is copied verbatim from secretscan's `_scan_file`, so the same
defect is almost certainly there (for `160/350` to confirm). *Counsel:* record the first
window's keys into `seen_in_window` too — a two-line change — and add a straddle fixture to
each affected `BoundedMemory` class or a sibling test.

**BL4 — minor. The bounds are documented in one tool's README section out of fourteen, and
no contributor guidance keeps a new scanner bounded.** See lens 3. The README's own sections
for wrapscan, datescan, spellscan, linkscan, reviewscan, licenscan, stampscan and blockscan
still read as whole-file tools. *Counsel:* a short "Bounded memory" table in the README's
residuals section (tool → mechanism → constant → what is counted, what is refused), and a
sentence in the tools README and the CONTRIBUTING template: a new scanner ships with a
`BoundedMemory` class built on memprobe, and reuses `filewalk` and one of the three readers.

**BL5 — minor. `memprobe.py` has no command-line measurement mode and fails open on unknown
arguments.** `python3 tools/memprobe.py --measure "python3 -c pass"` exits 0 with no output;
only `--selftest` does anything. The brief's "run memprobe on `python3 -c pass`" is only
possible through the Python API. Every sibling tool exits 2 on an unrecognised argument; a
silent zero is the shape this repo forbids elsewhere. *Counsel:* an `argparse` front with
`--selftest` and a `-- <argv…>` measurement mode printing the `ProbeResult`, exit 2 otherwise.

**BL6 — minor. sizescan's docstring overclaims what the caller does with truncation.**
`_iter_physical_lines` says "the caller counts the truncation rather than scanning silently
short"; `_scan_file_metrics` binds the flag to `_truncated` and discards it, and sizescan's
tally has no counter. Harmless in verdict terms (its regexes are line-start anchored), but
the record says a count exists that does not. stampscan, by contrast, counts the *source*
line once per read, so a single over-long line in a region reported as `3 over-long line(s)`
in the probe — a cosmetic over-count.

**BL7 — minor. Two ceilings are fitted rather than grounded.** pointerscan's
`MAX_BYTES_PER_ITEM = 8 KiB` is justified as "roughly 2× the measured rate" — the
`ground-numeric-limits` shape the other classes explicitly avoid. linkscan's over-long-line
case allows 100 MB of growth for a 24 MB longer line: a reader that regressed to holding the
line whole plus one copy would show ~48–72 MB and pass. *Counsel:* derive pointerscan's bound
from its per-item record shape as signscan does, and cap linkscan's single-line growth at a
multiple of `LINE_WINDOW_BYTES + LINE_WINDOW_OVERLAP` like its siblings.

**BL12 — minor. The regression guards' time ceilings turn host load into a red.** Running
the nineteen `BoundedMemory` classes plus `test_memprobe` while six other suites shared this
16 GB machine (about 1.8 GB in the compressor, 3.8 M pageouts): 42 tests in 684.5 s, three
failures — leakscan, spellscan and pins — every one on `scan did not finish in time`, the
classes' 60 s (pins) and 60 s (scanners) ceilings; none on a memory bound. Re-run alone,
all three pass in 169.2 s. The memory assertion is robust; the timeout is a fixed wall-clock
number on a shared machine, so a loaded host reads as a regression and an author learns to
re-run rather than trust the red. *Counsel:* ground the ceiling in the scan's own linear
rate (bytes per second measured on the small run, times a generous multiple) rather than a
fixed 60 s, or mark timeouts as `skipped: host too loaded` rather than `FAIL` when the
small run itself took more than a set fraction of the ceiling.

**BL8 — note. signfleet's size gate lands a child on `skip`.** An oversized `floor.yml`
prints a stderr warning and returns `None`, which `read_boundary` documents as "no
floor.yml" — the child ends `skip`, not `fail`, and `--check` passes. It is an observability
tool, not a commit gate, and the warning is printed, so this is a note; a distinct
`error`-status reason would make the board say what happened.

**BL9 — note. memprobe residuals to record, not fix.** (a) On Linux the isolated hop's own
interpreter (json, subprocess, tempfile, memprobe) is inherited as a constant offset by the
measured child; growth assertions are immune, absolute ones (`< 500 MB`, publishscan's
`< 200 MB`) have ample headroom. (b) A hung *inner* process raises `TimeoutExpired` past
`timeout + 60 s` instead of returning a `ProbeResult`. (c) The isolated path round-trips the
child's stdout through UTF-8 with replacement, so binary output is altered; no current caller
cares. (d) The docstring's "macOS spawns instead of forking" is the right observation for
the wrong reason on this interpreter (CPython 3.14 reports `posix_spawn` in use); the
measured fact — a fat caller does not inflate a Darwin reading — is what matters and holds.

**BL10 — note. The local full-suite verdict was lost to my own pipe.** I ran the full
Python suite once (14:19:01 → 14:36:03 UTC, 17 min 02 s wall under six concurrent suites on
this machine) through `tail -25`; unittest's summary went to stderr ahead of the
block-buffered stdout and fell outside the window, and the pipeline's exit 0 was `tail`'s.
Per the house rule I did not re-run the full suite. The delta's own regression guards were
re-run to a file instead (ledger, BL12), and the Linux full-suite evidence is CI's green run
on the first push after the last landing commit: `f94fe35` (run 35497193421), 1,519 tests
in 152.0 s, success.

**BL11 — note. The landing series was red on CI for 39 minutes, and the record of it is
honest.** Runs on `48c181f` (06:29 UTC), `692563a`, `40a4356` and `0bca6eb` all failed in
the harness's own tests with the Linux readings quoted under lens 1; `8426f3e` (06:51 UTC)
passed, and the memprobe rewrite commits' messages describe exactly that sequence. The
cancelled runs on `ca4eaac` and `994bf4b` are cancel-in-progress supersessions, not
evidence either way.

### Re-run ledger

All dates 2026-09-26 UTC; worktree HEAD `f81a98f`; Python 3.14.6 on Darwin; the machine
was shared with several other reviewers' suites throughout, so wall times are inflated.

| What | Command (from the worktree) | Result |
|---|---|---|
| Twenty selftests | `python3 tools/<t>.py --selftest` for memprobe, leakscan, conflictscan, sizescan, datescan, wrapscan, spellscan, linkscan, reviewscan, pathscan, licenscan, stampscan, blockscan, pins, floorfleet, signfleet, signscan, publishscan, board, pointerscan | all exit 0 (14:16 UTC) |
| Full Python suite | `python3 -m unittest discover -s tools -p 'test_*.py'` | ran once, 17 min 02 s wall; verdict line lost to my pipe (BL10); not re-run |
| Delta regression guards | `python3 -m unittest -v test_memprobe` + all 19 `BoundedMemory` classes, output to a file | 42 tests, 684.5 s (14:42:31 → 14:53:57), 39 ok, 3 FAIL on the 60 s ceiling (leakscan, spellscan, pins); the same three alone: 3/3 OK in 169.2 s (BL12) |
| Linux suite at the landing | `gh run view 35497193421` (`f94fe35`, first push after `a557315`) | success, 1,519 tests in 152.0 s |
| Linux failures in the series | `gh run view --log-failed` on 35494375424, 35494487269, 35494852791, 35495156906 | memprobe/datescan failures only; readings 62/78 MB, 145/187 MB, 254 MB for a bare interpreter — the forking-parent effect |
| Floor, ci plane | `python3 tools/floor.py --plane ci --root <worktree>` | exit 0; secretscan 22 advisory (unchanged class), leakscan 🟡 structural-only as designed; all truncation/cap tallies 0 |
| Floor, hook plane | `python3 tools/floor.py --plane hook --root <worktree>` | exit 0 (index clean, so the staged scanners read nothing) |
| memprobe, bare interpreter | `run_and_measure([python3, -c, pass])` (API; no CLI exists, BL5) | rc 0, peak 9.0 MB |
| memprobe, real scanner | `run_and_measure([python3, tools/conflictscan.py, --root, <worktree>, <worktree>])` | rc 0, peak 26.1 MB, clean |
| Darwin fat-caller probe | 200 MB touched ballast in the caller, direct path vs isolated | 9.07 → 8.87 MB direct, 9.00 MB isolated: no inflation on Darwin |
| Eleven `_walk_files` | `awk` over the eleven `return` lines + the eleven skip-set definitions | all eleven call `filewalk.walk_files(base, <set>)`; ten identical ten-name sets, licenscan's adds `dist`, `build`; sizescan names its set `NON_CONTENT_DIR_NAMES` |
| Straddle: datescan | 8,200 filler chars then a relative-time word, one line, `--root <tmp> docs` | exit 0, tally `1 over-long line(s) scanned truncated`; control at 100 chars exit 1; `--json` has no truncation field |
| Straddle: spellscan | same shape with a US spelling | exit 0 (control exit 1); `--json` no field |
| Straddle: wrapscan | 8,300-char unbreakable token then prose | exit 0 `clean` (control at 300 chars: exit 1, 370 cols) |
| Straddle: sizescan | `ROADMAP.md` with a `[x]` item on a 9 KB line, `--check` | exit 1, cold-content gated — unaffected |
| Straddle: stampscan | region line differing only after 8,300 chars | exit 0 `identical`, `3 over-long line(s)` |
| Overlap: linkscan | broken link 2,000 chars before the 1 MiB chunk boundary of a 1.1 MB line | exit 1, **2** findings for one link |
| Overlap: leakscan | placeholder address 2,000 chars before the 4 MiB cut of one line, empty terms file | exit 1, **2** findings for one token (`--json` also 2) |
| Hook plane growth | scratch clone; stage 8 MB then 32 MB filler; `leakscan --staged`, `conflictscan --staged` via memprobe | leakscan 66.9 → 215.4 MB; conflictscan 59.3 → 195.7 MB |
| Longest doc line | `awk` over `docs/**/*.md` excluding `sessions/`, `reviews/` | 6,409 chars |
| Sweeps | `tools/coldsweep.py --root <worktree> <pattern> --also-exclude ×5` for `memprobe`, `BoundedMemory…`, `020/380`, the three constants, `filewalk` | 351 files barred; hits outside `tools/` listed under Exposure |

### Follow-up checklist

- [ ] BL1 — decide window-with-overlap vs fail-closed `over-long-line` finding for the 8 KiB
      readers; add `lines_truncated` to datescan/wrapscan/spellscan `--json`.
- [ ] BL2 — stream the `--staged` path in leakscan and conflictscan (and secretscan under
      `160/350`); add a staged `BoundedMemory` case; correct the CHANGELOG claim or scope it
      to the tree plane.
- [ ] BL3 — seed the first window's keys into `seen_in_window` (leakscan); add dedupe to
      linkscan's windowed path; straddle fixtures for both; carry to secretscan via `160/350`.
- [ ] BL4 — README bounds table; contributor sentence in tools README and the CONTRIBUTING
      template.
- [ ] BL5 — argparse front for memprobe; exit 2 on unknown arguments.
- [ ] BL6 — correct sizescan's docstring or wire the counter; stampscan source-line count.
- [ ] BL7 — re-ground pointerscan's and linkscan's single-line bounds.
- [ ] BL12 — ground the `BoundedMemory` time ceilings in the small run's own rate, or skip
      rather than fail when the host is visibly loaded.
- [ ] BL8/BL9 — record as residuals in the respective docstrings; no code change required.
- [ ] Counsel (lens 1) — single-source the three readers as `115/080`'s next part; the
      `115/220` item already names them as three mechanisms.
- [ ] Out of delta, no finding: `coldsweep --also-exclude` is repeatable and parses a
      pattern after the excludes; my first failed sweep was zsh's word-splitting of an
      unquoted variable, not the tool.
