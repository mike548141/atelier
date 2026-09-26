# Cold pass — harvestscan's prefix-filter rewrite — the similarity pass indexed, exact and bounded

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/400-rule-4-cold-pass-queued-the-harvestscan-prefix-filter.md`.
**Why it earns a review:** a warn-only guard whose fast path silently drops a
true positive never tells anyone; the rewrite rests on a mathematical claim
(exactness) that, if off by one, converts a quadratic-but-correct guard into a
linear-and-wrong one.

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

- `ea8d50b` / `82d0314` (2026-09-20) — the landing commits

Delta paths:

- `tools/harvestscan.py` — `_build_survivor_index`, `_candidate_bucket`, and
  `vanished`'s inlined containment
- `tools/test_harvestscan.py` — the `BoundedTime` class
- `tools/README.md` § *harvestscan*

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

The exactness claim, independently: state the pigeonhole argument in your own
words from the code, derive the bucket size from `SURVIVAL_SIMILARITY` and `n`,
and test it — build fingerprints at every `n` from 1 to 40 and a survivor at
exactly the threshold containment, one word below, and one above, and show the
fast path agrees with a brute-force `similarity()` on all of them (a property
test, not a sample). The inlined formula against `similarity()`: are they the
same function on every input, including empty sets and duplicates? The
`BoundedTime` ceilings: grounded in the input class or fitted to a machine? The
replay claim: how many commits were actually compared, and is "byte-identical on
749 commits" the same claim as "byte-identical on 9 in scope"? **Non-goal:** the
commissioning item.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   whole review is whether *exact* is true; treat the README's statement of it
   as the author's claim.
2. **Correctness & quality.** Read the whole tool. Run `--selftest` and
   `tools.test_harvestscan`. Write the property test in your scratch clone and
   record its result and its inputs. Check the rounding in `k` at every `n`
   where `0.6 n` is an integer or just below one.
3. **Completeness / harvest.** Does anything else call `similarity()` or
   duplicate its formula? Does the README say what the guard now cannot see, if
   anything? Is the quadratic `020/400` class closed for *every* pass in the
   tool, or one?
4. **Security & privacy** — mandatory. The tool reads git history via subprocess
   and compares roadmap text; check its argument handling and that its output
   cannot leak a private item's text from a child's history into a public log
   beyond what the warn line already shows. The house scanner is discharged by
   grounds (landed delta; pending = other passes' drafts) — say so, and deliver
   the code-altitude read by hand.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/harvestscan.py --selftest`; `python3 -m unittest
  tools.test_harvestscan`; the full Python suite once
- the property test in *Scope*, with inputs recorded so it can be re-run
- the replay: run the tool over this repo's history the way the landing commit's
  tests do and record the counts
- the floor on both planes at HEAD

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
`docs/roadmap/160-doctrine-review-owed/400-rule-4-cold-pass-queued-the-harvestscan-prefix-filter.md`
(it carries the author's own lens hints), and:

- `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md` (⚠️ head and tail
  read by the brief-writer; the `020/400` section not opened)
- the board items `docs/roadmap/020-*/400-*.md`, `docs/roadmap/115-*/080-*.md`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/400-rule-4-cold-pass-queued-the-harvestscan-prefix-filter.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `HP`: `HP1`, `HP2`, …) and severities (MAJOR / MODERATE
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

## Verdict — phase 1, written 2026-09-26 UTC

### Provenance, repeated

- **Spawn.** A fresh subagent on `claude-fable-5-1`, spawned by the batch orchestrator
  with this brief as its only framing. Not the author's session; not started or
  instructed by the author of `ea8d50b` / `82d0314`. Shape: reviewer-plus-orchestrator,
  both seats Fable; the orchestrator holds the `.deferred.md` sibling outside the tree
  and forms no finding.
- **Tier at claim:** Fable. Rule 4's bar is met without the off-tier clause.
- **Where.** The shared review worktree at `f81a98f` when the pass began; the branch
  advanced to `999e354` (11 commits, other passes' records) while it ran, and none of
  the three delta paths changed between the two (`git diff --stat` empty). Probes ran
  in a scratch clone of the worktree at `f81a98f`. No git command that writes was run
  in the worktree; the scratch clone took one staged deletion and one `reset --hard`.
- **What I read.** This brief; `docs/method/REVIEW.md` and `00-APEX.md` at HEAD; the
  three delta paths at HEAD and the full diff of `ea8d50b`; `tools/floor.py`'s
  harvestscan registry entry; `.github/workflows/ci.yml` lines 195–235;
  `.githooks/pre-commit` (grep only); `tools/test_spellscan.py`'s
  `PathUrlStripIsLinearTime` (the precedent `BoundedTime` cites);
  `tools/README.md` § harvestscan; coldsweep's `--list-barred` output.
- **What I did not open.** The sibling; `docs/SESSIONS.md`; `docs/sessions/`;
  `docs/ROADMAP-DONE.md`; any prior verdict in `docs/reviews/`; the queue pointer; the
  board items `020/400`, `115/080`; the 2026-09-20 session record. Every tree sweep
  went through `tools/coldsweep.py` with `--also-exclude` for all four barred items.
- ⚠️ **Residual exposure, disclosed.** (1) Coldsweep hit lines outside the bar that
  name the barred item: two lines of board item `020/380` saying harvestscan's pass
  was "split out to `020/400`", the generated index lines in `docs/ROADMAP.md` carrying
  the titles of `020/400` (marked done) and of this pass's own pointer, and one
  `CHANGELOG.md` line. Titles and a split-out note only; no lens hint, no verdict text.
  (2) `gh run list` printed the subjects of two board commits of 2026-09-20 (one
  closing `020/400`). Subjects only.

### Lens 1 — approach & assumptions

**Load-bearing assumptions, named by me from the code:**

1. *Exactness.* For a fingerprint of `n` distinct words and threshold `t`, a survivor
   is accepted iff it shares `s` words with `s / n >= t` under float comparison; the
   filter assumes this is equivalent to `s >= k = ceil(t * n)`, and that any set of
   `n - k + 1` fingerprint words must be hit by every accepted survivor. The second
   half is a true pigeonhole for *any* subset of that size (a survivor missing all of
   them has at most `k - 1` words left to share), so ranking by rarity affects cost
   only, never the verdict, and words with zero postings placed first cost nothing. The
   first half is a float identity that happens to hold at `0.6` — **HP4**.
2. *The optimisation's unit matches the tool's call shape.* The index is built inside
   `vanished()`, "once per call", on the assumption that one call sees all candidates.
   On the split board `scan()` calls `vanished()` **once per watched file** — 331 files
   at HEAD — so the index is rebuilt 331 times per scan. This is the assumption that
   fails, and it fails on exactly the hook-plane bulk-delete path the guard exists for
   — **HP1**.
3. *"Bounded by bucket size" bounds the worst case.* It bounds the typical case on a
   Zipf-shaped corpus; a common-vocabulary corpus makes the bucket the corpus — **HP3**.
4. *The synthetic corpus is the hard case.* It is (no candidate matches, so no
   short-circuit), but it is single-text, so it cannot see assumption 2 fail.
5. *Rev arguments are trusted.* `--against` reaches `git diff` and `git show` as a bare
   argument — **HP5** (pre-existing, not the delta's).

**Is this the right problem, solved the right way?** The prefix filter is the right
technique and it is exact. But the item was funded for bounded *time on the estate*,
and the estate's real shape — hundreds of one-item files — is the one shape neither
the tests nor the replay exercise. On that shape the delta is slower than the code it
replaced. The problem was solved for the pre-split board.

### Lens 2 — correctness & quality

- **Exactness, independently derived and tested.** Property test at
  `<scratchpad>/HP/hp_property.py` (inputs recorded inside it; re-runnable):
  - A. `math.ceil(0.6 * n)` equals the smallest `s` with `s / n >= 0.6` under the same
    float comparison `vanished()` makes, for every `n` in 1..100 000 — 0 mismatches.
  - B. For every `n` in 1..40, survivors sharing exactly `k-1`, `k`, `k+1` words, with
    the shared words chosen as the *commonest* in the index (decoys make them so, which
    puts the fingerprint's rarest words — the prefix — among the unshared ones) and
    separately as the rarest; each in exact, superset and duplicated-word shapes, with
    empty survivors alongside, and fingerprints padded with duplicates to clear
    `MIN_SIGNAL_WORDS` for `n < 8` — 708 cases, `vanished()` agreed with brute-force
    `any(similarity() >= 0.6)` on all of them.
  - C. Bucket ⊇ accepted set on 20 seeded Zipf corpora × 200 fingerprints × 400
    survivors (lengths 0..40, including empties) — 4 000 checks, 0 violations.
  - D. End-to-end old-formula vs `vanished()` on 30 seeded corpora (150 items × 300
    survivors, near-copies and duplicates mixed in) — 0 mismatches.
- **Inlined formula vs `similarity()`.** Same function on every input where the
  fingerprint is non-empty (guaranteed by `MIN_SIGNAL_WORDS`): both take the set of
  the first argument, an empty second argument yields `0.0` either way, duplicates
  collapse identically. Verified by D and by the real-tree run (below).
- **Rounding in `k`.** Exact at `0.6` for all `n` ≤ 200 000, including every `n` where
  `0.6 n` is an integer. The identity is a property of the constant, not of the code:
  at `0.55` the float product overshoots the integer for 228 values of `n` ≤ 10 000
  (`n = 100` gives `k = 56`, one too many, so the prefix is one word short and a true
  match can be skipped, silently). **HP4.**
- **Real tree, function level.** 331 watched files at HEAD, 10 429 survivor bodies
  (395 779 words, 18 729 distinct). New `vanished()` over all 331 files: index rebuilt
  331×, **226.5 s**; old `vanished()` on the same inputs: **13.8 s**; verdicts
  identical (0 findings both). The same work with the index and sets built once:
  0.51 s + 2.36 s. **HP1.**
- **Real tree, the shipped hook plane, live.** In the scratch clone I staged the
  deletion of five item files (214 net lines — a routine five-item harvest trips the
  50-line gate). `harvestscan --root . --staged --only-bulk-deletes`: new code
  **248 s** wall; the pre-fix module on the same staged plane **82 s**. Both warned.
  Restored with `reset --hard`; clone clean after. **HP1.**
- **`--selftest`:** ok (0 failures). **`tools.test_harvestscan`:** 37 tests OK in
  14.1 s (BoundedTime included). **Full suite once:** 1 564 tests OK in 509 s, in the
  scratch clone under a hard 585 s limit.
- **BoundedTime on this (loaded) machine.** New 1.35 s / 6.38 s against ceilings of
  6 s / 15 s; old 17.3 s / 152.6 s on the same inputs (author recorded ~0.9 / ~3.5 and
  ~13.5 / ~50). The corpus vanishes 1 200 / 1 200 and 3 000 / 3 000 — every candidate,
  not "most". **HP2.**
- **Machine-independent count** on BoundedTime's own corpus: 126 915 comparisons of
  1 440 000 (8.8 %) at 1 200; 817 722 of 9 000 000 (9.1 %) at 3 000; bucket mean 106 /
  273, max 389 / 1 605.

### Lens 3 — completeness / harvest

- **Other callers of `similarity()` / copies of its formula:** none outside
  `harvestscan.py` and its tests (coldsweep, barred paths excluded). The only two
  spellings of the containment formula are `similarity()` and the inlined line.
- **Does the README say what the guard now cannot see?** It says the filter "cannot
  change a verdict", and that is true (above). It also says the worst case is bounded
  by bucket size, not corpus size, which overstates — **HP3**.
- **Is the quadratic class closed for every pass in the tool?** The only pass that was
  quadratic in item count was `vanished()`'s inner loop, and it is now bucketed — but
  the per-file rebuild re-introduces a cost proportional to `files × survivors`, which
  on the split board is worse than what was removed (**HP1**). `survivors()`, `replay()`
  and `expand_records()` are linear in files and subprocess-bound; not this item's.
- **Replay claim.** Old and new `--replay --only-bulk-deletes --json` over the clone's
  history are **byte-identical**: `{commits: 773, in_scope: 9, fired: 4, items: 16}`.
  The nine in-scope commits all predate 2026-08-07 and each has exactly **two** watched
  files at its parent (pre-split), so "byte-identical on 749 commits" is, in content,
  "identical on 9 commits × 2 files, none of them split-board shaped". The 749 does
  not reproduce at the landing commit (764 there; 773 at `f81a98f`; 784 at `999e354`)
  — the figure was the author's worktree base, not the recording commit. **HP6.**
- The docstring's own "6 in scope, 3 warn, 15 items" is stale at HEAD (9 / 4 / 16);
  not the delta's line — **HP7**.
- No `bench_harvestscan` exists in the tree; the test docstring cites it as the
  generator's reasoning source. It lived in a session's scratch space, so the fix's
  measurements (5 000 items 217.6 s → 6.5 s) are re-runnable only via BoundedTime's
  generator, not via the named bench. Note, folded into HP2.

### Lens 4 — security & privacy

`/security-review` is **discharged by grounds** for this pass: it reads the session's
pending diff, which in the shared worktree is other passes' unstaged drafts, and this is
a landed-delta review. Code-altitude read delivered by hand, checked against OWASP
Top 10 (2021) A03 injection and CWE-88 (argument injection):

- **The delta itself** adds no I/O, no subprocess, no argument, no output. Pure set and
  dict work over data the tool already held. No new threat surface; no new data leaves.
- **Output.** The 160-character excerpt of a removed item is unchanged by the delta; it
  prints text already in the scanned repo's own history into that repo's own hook or
  CI log. Nothing crosses a repo boundary; a child's private text reaches only the
  child's log. Exactness means the filter cannot add or hide an excerpt.
- **Argument handling (pre-existing, probed).** All subprocess calls are list-form; no
  shell. But `--against` reaches `git diff --numstat` as a bare argument before the
  `--`: `--against=--output=<path>` made the gate write its diff to that path and read
  an empty result, so the scan reported "not in scope — 0 net lines" — a fail-open, and
  an arbitrary-file-create. The `git show` path rejected the same value (argparse
  refuses the bare `--against --x` form; the `=` form gets through). The trust boundary
  is the invoker (a user at the CLI, or the floor registry in CI), so this is a
  hardening item, not an exposure of the estate. **HP5**, minor, pre-existing.
- **Tests.** The fixture identity is RFC 2606; BoundedTime is seeded and deterministic;
  temp repos only.

### Findings

- **HP1 — MAJOR.** *The index is rebuilt once per watched file, so on the split board
  the "bounded" pass is 3–16× slower than the quadratic one it replaced, on exactly
  the bulk-delete path the guard exists for.* `scan()` and `replay()` call `vanished()`
  per file; `vanished()` builds `_build_survivor_index(alive)` and `alive_sets` on
  every call. Measured at HEAD: 331 rebuilds; 226.5 s vs 13.8 s at function level;
  248 s vs 82 s at the shipped hook plane on a five-file harvest that trips the gate.
  Built once, the same scan is under 3 s. Nothing in the tests can see it — BoundedTime
  drives one text with all candidates; the split-board tests use one file — and the
  replay's nine in-scope commits are all pre-split. The commit and README record the
  work as "linear, exactly" and "bounded"; on the estate's real shape neither holds.
  Why MAJOR rather than MODERATE: a warn-only hook that takes four minutes on a
  routine harvest invites `--no-verify`, which silences the whole floor for that
  commit, not just this guard — the silent-failure class the brief's opening names.
  *Counsel:* hoist the index and sets out of `vanished()` — build them once in
  `scan()` / per replay revision and pass them in (a small survivor-index object, or
  `vanished(old_text, alive, index=None)` that builds only when not given) — and add a
  test that runs `scan()` on a synthetic split board of a few hundred one-item files
  with a comparison-count or rebuild-count assertion, so the shape that failed here is
  the shape the test drives.
- **HP2 — minor.** *BoundedTime's ceilings are absolute wall-clock fitted to one
  machine.* On this loaded machine the fix ran at 2.3× under the ceilings while the old
  code ran 3× over its recorded times; a slower or busier runner fails a correct
  implementation, a faster one could pass the quadratic one. The property the test
  wants — comparisons ≪ items × survivors — is machine-independent and measured at
  8.8 % / 9.1 % on the test's own corpus. The docstring's "most candidates find no
  survivor" is "all of them" (1 200 / 1 200, 3 000 / 3 000); say so, since that is the
  reason the case is hard. *Counsel:* assert a comparison or bucket count (or a
  rebuild count once HP1 lands) beside, or instead of, the seconds.
- **HP3 — minor.** *"Worst case is bounded by the buckets a candidate's vocabulary
  touches, not by the corpus size" overstates.* The bucket can be the corpus: on a
  30-word common vocabulary with no possible match, the bucket averaged 75 % of the
  survivors and the pass stayed quadratic (6.7 M of 9 M comparisons; 33 s vs 72 s at
  3 000). On the real tree the buckets are 8 % on average and 29 % at worst
  (mean 839, max 2 979 of 10 429). *Counsel:* say "typical case, on a long-tail
  vocabulary" in README and docstring; the exactness sentence stands.
- **HP4 — minor.** *`k = math.ceil(SURVIVAL_SIMILARITY * n)` is exact only because the
  constant is 0.6.* The identity with the float comparison the check makes fails at
  other constants (0.55: 228 values of `n` ≤ 10 000, `n = 100` → `k` one too high →
  prefix one short → a true match skipped, silently). The constant's docstring
  forbids tuning to fit, not changing. *Counsel:* derive `k` with the same comparison
  (`k = ceil(t*n)`, then step down while `(k-1)/n >= t`), or pin the identity in
  `_selftest` for `n` in 1..10 000 so a constant change reds the floor.
- **HP5 — minor, pre-existing, security (CWE-88).** *A dash-led `--against` value is
  passed to git as an option.* `--against=--output=<path>` turns the bulk gate into
  "0 net lines, not in scope" and creates a file. Invoker-trusted surface, so a
  hardening item. *Counsel and recurrence prevention:* validate revs with
  `git rev-parse --verify --end-of-options <rev>` (or reject a leading `-`) in
  `git_show`, `list_markdown` and `net_line_loss`; the same pattern is worth one sweep
  across the other scanners that take a revision argument.
- **HP6 — note.** *The replay figure does not reproduce at the recording commit.* 749
  was the author's worktree base (764 at `82d0314`, 773 at `f81a98f`); the in-scope set
  of nine is the same at both, so the byte-identical claim stands in substance and the
  population number is the stale part. The claim's content is nine commits × two files.
- **HP7 — note, pre-existing.** The module docstring's "Re-measured at this landing:
  6 in scope, 3 warn, 15 items" is 9 / 4 / 16 at HEAD; its own "run `--replay` rather
  than trusting this line" is the right instruction.

### Overall

**PASS-WITH-FINDINGS — 1 MAJOR, 0 MODERATE, 4 minor, 2 note.** The exactness claim —
the one that would have made the guard linear-and-wrong — is true and tested at every
`n` and at the boundary. The bounded-time claim is false on the estate's real shape,
and the cycle should stay open on HP1.

### Re-run ledger

All in the scratch clone (`<scratchpad>/HP/probe`, HEAD `f81a98f`) unless noted; UTC.

| # | Command | Result |
|---|---------|--------|
| 1 | `python3 tools/harvestscan.py --selftest` (worktree) | ok, 0 failures, exit 0 |
| 2 | `python3 -m unittest tools.test_harvestscan -v` (worktree) | 37 tests OK, 14.1 s |
| 3 | `python3 -m unittest discover -s tools -p 'test_*.py'` (once, hard 585 s cap) | 1 564 tests OK, 509 s, exit 0 |
| 4 | `python3 hp_property.py` | A/B/C/D all PASS; 708 boundary cases, 4 000 bucket checks, 30 corpora |
| 5 | `python3 hp_realtree_timing.py probe HEAD` | new 226.5 s (331 rebuilds) vs old 13.8 s; hoisted 0.51 + 2.36 s; identical |
| 6 | staged five-file deletion → `harvestscan --root . --staged --only-bulk-deletes` | gate tripped (214 lines); new 248 s, old 82 s; both warned; clone restored |
| 7 | `python3 hp_counts_and_adversarial.py probe/tools` | synthetic 8.8 % / 9.1 % of full scan, 12.8× / 23.9× faster; adversarial 74 % / 75 %, 3.6 / 33 s vs 12.7 / 71.6 s; identical |
| 8 | `harvestscan --replay --only-bulk-deletes --json` new vs pre-fix module | byte-identical; 773 / 9 / 4 / 16; 181 s and 148 s |
| 9 | `python3 tools/floor.py --plane hook --root . --tools tools` | exit 0; harvestscan not in scope (0 lines) |
| 10 | `python3 tools/floor.py --plane ci --root . --tools tools` | exit 0; harvestscan not in scope (−16 lines); pathscan 1 warn-only finding, pre-existing, not in the delta |
| 11 | float probe `ceil(t*n)` vs exact, `t ∈ {0.5..0.9, 0.35}` | 0.6 exact to n = 200 000; 0.55 fails 228× ≤ 10 000 |
| 12 | `--against=--output=<file>` probe | file created on the numstat path; gate read 0 lines |
| 13 | `gh run list --branch main` | run at `0bc4093` (contains `82d0314`, verified by `merge-base --is-ancestor`) success 2026-09-20T12:01:04Z |

Harness files, all under `<scratchpad>/HP/`: `hp_property.py`, `hp_realtree_timing.py`,
`hp_counts_and_adversarial.py`, `hp_replay_old.py`, `harvestscan_old.py` (from
`ea8d50b^`), `replay_new.json`, `replay_old.json`, `suite.txt`, `floor_hook.txt`,
`floor_ci.txt`. Environment: Python 3.14.6, git 2.50.1, shared machine under load.

### Follow-up checklist

- [ ] HP1 — hoist the survivor index out of `vanished()`; add a split-board-shaped
      timing/count test; re-measure the hook plane on a real harvest (target: seconds).
- [ ] HP2 — replace or back the wall-clock ceilings with a comparison/rebuild count.
- [ ] HP3 — reword README § harvestscan and the `_candidate_bucket` docstring.
- [ ] HP4 — derive `k` by the check's own comparison, or pin the identity in selftest.
- [ ] HP5 — `--end-of-options` / rev validation in the three git helpers; sweep the class.
- [ ] HP6, HP7 — refresh the recorded figures where they are restated.
