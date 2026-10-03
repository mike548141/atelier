# Cold pass — ccarchive's manifest checkpoints and stale-entry heal

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this pass's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-03 0357 UTC; the review runs under the
orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:** `docs/roadmap/160-doctrine-review-owed/460-rule-4-cold-pass-queued-the-manifest-checkpoints.md`.
**Why it earns a review:** ccarchive holds the only durable copy of every session transcript; a change to how its manifest is written and repaired is a change to whether that copy can be trusted after an interrupted run.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the commits named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-03 with
  the prompt "Do all cold reviews and any other work dependent on fable", on
  the Fable tier (`claude-fable-5-1`), orchestrating six rule-4 passes queued
  by that run. It wrote this brief from the queue pointer, the landing commits'
  subjects and `--stat` file lists, and the delta paths' names; it did not open
  the intent record.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree and
  outside the harness scratchpad (subagents can read the scratchpad), commits
  the reviewer's phase-1 findings unrevised, then releases the sibling's text by
  message; the reviewer appends a reconcile section; the orchestrator folds the
  sibling in and updates the pointer. The orchestrator forms no finding and
  writes no severity. Both seats are Fable, so the off-tier clause is not
  invoked; the shape is stated anyway so the record is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the authoring run told this session over the cross-session channel
  that the pointer existed and named its subject in a phrase; nothing else from
  that run was read. Earlier in the same sitting this session commissioned
  read-only inventories of the board's open items and of every verdict in
  `docs/reviews/`, for a ruling round; the summaries it received include prior
  findings on the surfaces under review. Those summaries are author-side
  framing this pass must meet cold; every line of them that bears on this delta
  has been moved to the sibling and kept out of this brief. The brief-writer
  also read the 2026-09-25 batch's staged-plane brief as a formatting template,
  the session index entries of 2026-09-19 to 2026-10-01, and, as doctrine at
  onramp, `docs/method/REVIEW.md`, `docs/method/00-APEX.md` and
  `docs/method/COMMUNICATION.md` § *Asking for a ruling* at HEAD.

## What the work is

Landing commits (diff these; review the paths at HEAD, `17c75a9` or later):

- `0264387` (2026-10-03) — merge of `5870927`: ccarchive checkpoints the manifest and heals a lagging entry (board `210/170`)

Delta paths:

- `instruments/ccarchive` — the checkpoint writes and the heal path
- `instruments/ccarchive.test.js` — its tests
- `instruments/man/ccarchive.1` — the page's account of both

`instruments/README.md` and the ADR 0006 record did not change; whether they still describe the tool is yours to establish.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Driven, not read: in a scratch archive, run an archive pass and kill it part way (SIGKILL, and separately a full disk or a read-only manifest path); inspect the manifest and the archive for agreement; run `--verify`; then run again and record what heals, in which direction, and what is reported. Construct each lagging shape by hand (archive entry newer than manifest, manifest entry with no archive file, hash mismatch, a truncated source that is newer) and drive the heal over each. Confirm the shrink guard and `--force` still behave as the man page says. **Non-goal:** the board item that commissioned the work, and encryption at rest.

## The four lenses

1. **Approach & assumptions.** A checkpoint presumes a write order that survives a crash: find the interleaving where the manifest claims an entry the archive lacks, or the reverse. A heal presumes it can tell lagging from corrupt: find the case where healing overwrites the good copy.
2. **Correctness & quality.** Read all of `instruments/ccarchive` and its tests. Run `node --test instruments/*.test.js`, the man-page superset test, `--help`, and every state in *Scope*. Check every new exit path is in EXIT STATUS.
3. **Completeness / harvest.** Every surface that states the archive's integrity contract: man page, `instruments/README.md`, the ADR 0006 record's ccarchive addendum, `CHANGELOG.md`. Does each still hold at HEAD?
4. **Security & privacy** — mandatory. The tool writes to a durable store from untrusted source files and heals on its own judgement. Check the heal cannot be steered by a crafted source (timestamp, size, hash collision shape), that temp files and partial writes land with safe modes, and that a symlinked source or destination is handled. The house scanner is discharged by grounds (landed delta; the pending diff is this brief) — say so, and deliver the code-altitude read by hand, against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `node --test instruments/*.test.js` (foreground, once)
- `instruments/ccarchive --help`; the man page's option superset test
- every crash and heal state in *Scope*, in a scratch archive under your clone

## House rules for this run

- You work in the shared review worktree `/Users/mike/worktrees/atelier-review-430`
  (branch `review-430-1003`), read-only except for THIS brief file. Other
  reviewers are working there at the same time on their own briefs; never open
  another `docs/reviews/2026-10-03-*` file — it is another pass's framing. Run
  **no git command that writes** there (no add, commit, stash, checkout,
  worktree, reset, clean). Read-only git (`log`, `show`, `diff`, `blame`) is
  fine. Mutation probes, scratch children and checkouts of older commits go in
  your own clone: `git clone /Users/mike/worktrees/atelier-review-430
  <scratchpad>/MC/probe` under the session scratchpad, named by your
  prefix so parallel reviewers do not collide.
- One heavy process at a time on this machine: run the full suite at most once,
  in the foreground with a long timeout; if a memory-probe test times out, note
  it as environmental and re-run that test file alone before recording it.
  Never scan any tree outside the worktree or your scratch clone, and never
  point a scanner at the machine's other repos. Other sessions are live on this
  machine and in this repo's primary checkout; touch nothing there.
- `/security-review` is **discharged by grounds**: it reads the session's
  pending diff, which here is other passes' drafts and this brief, and this is a
  landed-delta review. State that line in your lens-4 answer and deliver the
  code-altitude read by hand.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" and would
  block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ English.
  Never quote a secret, a placeholder token, an email address, a private
  repo's name or any personal detail — this repo is PUBLIC; describe, don't
  quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/460-rule-4-cold-pass-queued-the-manifest-checkpoints.md`
(it carries the author's framing and this pass's claim line), and:

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` (the
  intent record)
- the board item `docs/roadmap/210-*/170-*.md` (the commission)
- the verdicts `docs/reviews/2026-07-17-1000-adr0006-ccarchive-preserve-cold.md` and `docs/reviews/2026-07-17-1157-cli-docs-applied-cold.md`
- `docs/roadmap/210-*/020-*.md`, `210-*/030-*.md`, `210-*/160-*.md` (open ccarchive items)

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-430 --also-exclude
docs/roadmap/160-doctrine-review-owed/460-rule-4-cold-pass-queued-the-manifest-checkpoints.md
--also-exclude docs/roadmap/210-instruments-open-features <pattern>` — rule 2's
default bar plus the items above; `--include-barred` only with disclosure in
the verdict. Reading the *delta* is never barred: the code, its tests, the
README entries and the registry are the subject. What is barred is the author's
narrative of why, and the verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `MC`: `MC1`, `MC2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, a re-run ledger with the commands and their results, and a
follow-up checklist. Then STOP and report to the orchestrator that phase 1 is
written. Do not open the sibling (it is not in the tree); do not edit the queue
pointer, the board, or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
record, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

Findings are the principal's to decide (rule 3): record all, apply nothing;
your counsel per finding is welcome, labelled as counsel and kept beneath the
finding.

---

## Verdict (phase 1) — 2026-10-03 04:22 UTC

**Overall: PASS-WITH-FINDINGS** — 2 MAJOR · 2 MODERATE · 4 minor · 2 note (10 findings).
The fix does what it set out to do: the lagging-entry shape it was built for heals on the
next run (shape A below), a thrown mid-loop error leaves a covered, signed manifest, and a
hard kill now leaves at most the checkpoint interval ahead of the manifest instead of the
whole run. But the heal reads the wrong side: it refreshes the manifest from the *source*
on an mtime inference that does not hold, and in two driven shapes that turns a correctly
reported drift into a false alarm on an intact mirror, or lets the shrink guard wave
through an overwrite of the good copy with a green `--verify` afterwards. The second MAJOR
is pre-existing and was surfaced by the real-kill drive: a mirror torn mid-write is frozen
in by its own mtime, attested from the source, and crashes `--verify` outright.

### Provenance

- **Reviewer:** `claude-fable-5-1`, a fresh subagent spawned by the brief-writer with this
  brief as its only framing. Not the author's session (the 2026-10-03 queue run), not
  started or instructed by it; none of the delta's paths edited by me.
- **Tier:** Fable, the principal-named review tier. Orchestrator also Fable; the off-tier
  clause is not invoked.
- **What I read:** this brief; the three delta paths in full at `17c75a9`; the landing
  commits `0264387` and `5870927` (subject, body, `--stat`, diff against `0264387^1`);
  `instruments/README.md` § ccarchive; ADR 0006's two addenda; `CHANGELOG.md` headings;
  `.githooks/pre-commit`, `tools/floor.py` (invocation lines) and
  `.github/workflows/ci.yml` for the floor. Nothing under the rule-2 bar was opened: no
  `docs/reviews/` verdict, no session record, no roadmap item, not the queue pointer.
- ⚠️ **Where the review ran, disclosed.** The shared worktree `atelier-review-430` sits at
  `4ff8de5`, and `0264387` is **not an ancestor of it** (`git merge-base --is-ancestor`
  says no; the worktree's `instruments/ccarchive` has no `checkpointEvery` and its test
  file has none of the five new tests). The branch forked from main before the queue run
  landed; main's `ca61feb` joins the two, the worktree never did. The brief's "review the
  paths at HEAD, `17c75a9` or later" names a commit that does contain the delta, so I
  reviewed at `17c75a9` in my scratch clone, where `instruments/` is byte-identical to
  `0264387`. My first full-suite run landed on the pre-delta worktree before this was
  caught; rather than run the full suite a second time (house rule: once), I re-ran the
  ccarchive test file alone at `17c75a9`. The pre-delta comparisons below used a second
  clone at `729c74b` (= `0264387^1`). Recorded as MC8.
  **Mid-pass update (2026-10-03, after the verdict above was drafted):** the orchestrator
  merged `origin/main` (`e5b44fe`) into the review branch; the worktree is now at
  `0a669e7`, `0264387` is an ancestor, and `git diff 17c75a9 0a669e7 -- instruments/`
  over the three delta paths is **empty**. Every read and every drive in this verdict was
  at `17c75a9`, so they stand against the worktree's HEAD unchanged. Per-SHA ledger:
  reads of the three delta paths — `4ff8de5` (pre-delta, superseded) then `17c75a9`;
  full suite — `4ff8de5`; ccarchive test file, mutations, kill drive, shapes A–H,
  read-only and symlink probes — `17c75a9`; pre-delta comparisons — `729c74b`.
- **Scratch:** everything under the session scratchpad's `MC/` directory; no scanner or
  probe touched any tree outside the worktree and that directory; no git command that
  writes ran in the worktree.

### Per-lens answers

**Lens 1 — approach and assumptions.** Two premises, one holds and one does not.

*Checkpoint write order holds.* Entries are set in memory only after `writeFileSync` +
`utimesSync` (lines 1175–1180), and `persist()` (1114) writes manifest then signature,
each by temp-and-rename. Eight real `SIGKILL`s over a 1,500-file tree never produced a
manifest claiming a mirror that was absent; the lag ran the other way, 0–42 mirrors ahead
at `CHECKPOINT_EVERY=50` and 0–1 at `=1`, each reported `UNMANIFESTED` by `--verify` (exit
1, signature `verified`) and fully healed by the next ordinary run. One interleaving does
leave the manifest and signature disagreeing — a kill between the manifest rename and the
signature rename — and `--verify` then reports it as **tampered**, the TAMPER EVIDENT
wording, until the next run re-signs (shape H). The drive never hit that window; it was
constructed by hand. The commit body's "a crash never leaves a signature that disagrees
with the manifest" is therefore not true, only narrow (MC4).

*The heal's premise does not hold.* The code's argument (comment at 1136–1142) is: the
mirror is stamped with the mtime of the source version it was written from, so on the
skip path "this source IS what the mirror holds". The inference runs backwards. The skip
path admits any mirror whose mtime is ≥ the source's (within 1 ms), and a source file can
change without its mtime advancing past the mirror's: a restore from backup (older mtime
— the man page's own INTEGRITY section names this case and says the archived copy is
left alone), `cp -p`, `rsync -t`, `touch -r`, an iCloud or Time Machine restore of the
projects directory. In each, the heal rewrites the manifest from the source while the
mirror holds something else. Driven as shapes E and F: see MC1. The archive's stated
invariant — "the manifest tracks the *archive*, not the live sources" (code 447–451, man
page INTEGRITY, README) — is what the heal violates. The second lens-1 question, "the
case where healing overwrites the good copy", is shape F exactly: the heal lowers
`rawBytes` to the truncated source's size, and the shrink guard, which compares against
`rawBytes`, then lets a later re-archive overwrite the intact mirror.

**Lens 2 — correctness and quality.** Read all 1,287 lines of `instruments/ccarchive`
and the 1,517 of its tests. Floor re-run in the ledger below: full suite 277/277 (at the
pre-delta worktree — see provenance), ccarchive file alone 104/104 at `17c75a9`, `--help`
exit 0, the superset and roff tests pass, `mandoc -T lint` clean. All eight scope states
driven (ledger). Defects: the in-loop checkpoint has no discriminating test — deleting
line 1188 leaves all five new tests green, because the catch-path save (1193–1203) covers
the same assertion; only deleting the catch-path save fails one (MC3). A part-way failure
exits via an uncaught exception: status 1 by Node's default, a raw stack trace on stderr,
and **no JSON report under `--json`**; it is not in EXIT STATUS (MC5). `--verify` crashes
on a mirror that will not gunzip (line 675 rethrows anything but `ENOENT`), so a single
torn file loses the whole verify rather than being reported (MC2). The size-only heal and
its documented limit (a same-size rewrite is not detected) both behave as the page says
(shape C: `--audit` still reports it `rewritten`). The shrink guard and `--force` behave as
documented on a source that is newer (shape D) — the bypass in MC1 needs the heal first.

**Lens 3 — completeness / harvest.** Man page: the new paragraph overclaims — "a run
that dies leaves the manifest covering every mirror it had written" is true of a thrown
error and false of a hard kill, where the drive observed up to 42 mirrors uncovered (the
code comment at 108–115 says this honestly; the page does not) (MC4). The page hardcodes
"every 50" in prose, its `.TH` date is still 2026-08-09, and neither `CCARCHIVE_CHECKPOINT_EVERY`
nor `CCARCHIVE_TEST_FAIL_AFTER` is documented anywhere a reader would find them (the
existing `CCARCHIVE_SIMULATE_DATALESS` seam is likewise unnamed on the page — a
precedent, not a defence) (MC7). `instruments/README.md` § ccarchive: nothing it states is
contradicted at HEAD; it does not describe checkpoints and defers to the page, which is
fine. ADR 0006's ccarchive addendum: holds unchanged. `CHANGELOG.md`: queue runs are
logged there (2026-09-18 and 2026-09-20 entries name `210/*` items); the 2026-10-03 run
has no entry and neither does `210/170` (MC7).

**Lens 4 — security and privacy.** The house scanner is **discharged by grounds**:
`/security-review` reads the session's pending diff, which here is other passes' drafts
and this brief, and this is a landed-delta review. Code-altitude read by hand against the
OWASP catalogue, with probes:

- *Steering the heal with a crafted source* (A08 integrity failure): yes — any process
  able to rewrite a source without advancing its mtime makes the manifest attest content
  the mirror does not hold, and can lower `rawBytes` to disarm the shrink guard. No hash
  collision is needed; size alone is the trigger. MC1.
- *Partial writes / safe landing* (A04 insecure design): manifest and signature land by
  temp-and-rename; mirrors do not — `writeFileSync(destAbs, gz)` writes in place, and a
  kill mid-write leaves a torn `.gz` whose mtime is newer than its source, so it is never
  re-archived and is backfilled from the source on the skip path. Driven by construction
  (shape G) and produced by a real kill (ledger, trial 3). MC2. Modes: manifest, sig and
  mirrors land `0644` (umask); the key `0600` as documented. Mirrors are personal
  transcripts; `0644` is pre-existing and umask-dependent (MC9, note).
- *Symlinks* (A01 broken access control): a symlinked source file or directory is **not
  followed** (the walk uses dirent types; probe archived 1 of 3 entries). A **dest that is a
  symlink into a git work tree bypasses the repo-dest guard** — `insideGitWorkTree`
  (155) walks `path.resolve`, not `realpathSync`; the probe archived into a directory under
  a `.git` parent with exit 0 (MC6). A pre-planted `manifest.json.tmp` symlink in the dest
  is followed by `writeFileSync` and then renamed over `manifest.json`, which becomes the
  symlink; this needs write access to the dest, which the signing threat model already
  concedes, so note-level (MC9).
- *Test seams in production* (A05 misconfiguration): `CCARCHIVE_TEST_FAIL_AFTER` makes a
  scheduled run die after K mirrors on an environment variable alone. launchd does not
  inherit a shell's environment, so the reach is small; the seam is the established house
  pattern. Noted under MC7, no separate finding.
- *Secrets*: no key material, path or personal value enters the delta; the key is read by
  `ensureKey` at every checkpoint and never logged. Clean.

### Findings

**MC1 — MAJOR — the heal refreshes the manifest from the source, and the source is not
what the mirror holds.** `instruments/ccarchive` 1136–1146. Driven at `17c75a9` and at
`729c74b` on identical inputs:

- *Shape E* (source replaced by an older-mtime, shorter copy — the man page's "restored
  from backup" case). Pre-delta: manifest untouched, `--verify` 0, `--audit` 1 with the
  file `shrunk` — correct. At HEAD: the heal rewrites the entry to the source's 8 bytes;
  the mirror still holds the intact 24; `--verify` then reports **MISMATCH on an intact
  mirror**, and does so on every later run (it does not settle); `--audit` reports
  **synced** while live and archive differ. Both integrity reports are now wrong.
- *Shape F* (source truncated with mtime preserved, then appended with a newer mtime).
  Pre-delta: the append is **REFUSED** by the shrink guard (16 < 24 recorded). At HEAD:
  step 1's heal lowers `rawBytes` to 8; step 2 passes the guard (16 > 8) and **overwrites
  the 24-byte good mirror with 16 truncated bytes**, `--verify` 0. The sole durable copy
  is replaced and the archive reports green.

The favourable shape (A, the one the commit was built for) heals correctly at HEAD and is
stuck at MISMATCH pre-delta, so the fix is real; it is the direction that is wrong.
*Counsel:* heal from the **mirror** — gunzip and hash the `.gz` when `rawBytes` disagrees
with the gunzipped length (skip when `isDataless`, which a just-written mirror never is),
so the manifest keeps tracking the archive. Requiring mtime equality rather than ≥ would
close E but not F. Add tests for E and F; they are three-line variants of `makeStale`.

**MC2 — MAJOR (pre-existing, surfaced by the drive) — a mirror torn mid-write is frozen
in, attested from the source, and crashes `--verify`.** Lines 1175–1180 write the mirror
in place, not temp-and-rename. A kill mid-write leaves a partial `.gz` with mtime = now,
newer than its source, so `shouldArchive` is false forever; the skip-path backfill (1149)
then records the **source's** hash and size against it. `--verify` hits `Z_BUF_ERROR` at
675, which is not `ENOENT`, and rethrows: exit 1, empty stdout, a stack trace, no per-file
report — one torn file silences the whole verify. `--audit` compares live to the recorded
hash and says synced. In 30 days the source is pruned and the torn mirror is all that
remains. A real `SIGKILL` produced this once in eight trials (a 0-byte `.gz`, manifest
entry `rawBytes: 40000`); shape G reproduces it by construction at both commits. The
commit body's "the manifest never claims one that is not there" is true of absent files
and false of torn ones. *Counsel:* write the mirror to `destAbs + '.tmp'`, `utimes` the
temp, then rename; make `--verify` report any gunzip failure as a named `CORRUPT` (exit 1)
instead of throwing; and have the skip-path backfill hash the mirror, not the source, for
the same reason as MC1.

**MC3 — MODERATE — the checkpoint has no test that fails without it.** Mutation at
`17c75a9`: delete line 1188 (the in-loop `persist()`), run the five new tests — **5/5
pass**. Delete the catch-path save instead — 1/2 fail. Both tests reach the manifest via
the catch, because the seam *throws*; nothing exercises the only path a hard kill takes.
The 50-mirror bound, the thing the constant and the man page are about, is unasserted.
*Counsel:* make the seam kill the process (`process.kill(process.pid, 'SIGKILL')`) in one
test, with `CCARCHIVE_CHECKPOINT_EVERY=1`, and assert mirrors − entries ≤ 1; or disable the
catch-path save under a second seam and re-run the first test.

**MC4 — MODERATE — the man page and commit body promise more than the mechanism.** Page
413–415: "a run that dies leaves the manifest covering every mirror it had written" — true
for a thrown error, false for a hard kill (drive: 36, 1, 18, 42, 23 mirrors uncovered at
`=50`), where the honest statement is "at most 50 behind, reported UNMANIFESTED, healed
next run" — which the code comment at 108–115 already says. Commit `5870927`: "a crash
never leaves a signature that disagrees with the manifest" — shape H (manifest renamed,
signature not) gives `--verify` **tampered**, with the TAMPER EVIDENT line, until the next
run re-signs. *Counsel:* page wording to match the comment; either close the window (write
the signature temp first, then rename manifest and signature back-to-back) or have
`--verify` note a signature older than the manifest as a hint beside the mismatch.

**MC5 — minor — a part-way failure's exit is undocumented and unstructured.** Driven with
a read-only dest root (the same throw site as ENOSPC inside `persist()`): exit 1 by
uncaught exception, stdout empty **even under `--json`**, stderr carries the one honest
line ("could not save manifest after failure") followed by a raw Node stack. The man page
now describes the part-way save but EXIT STATUS lists no exit for it. Heal after the path
is writable again: clean (4 archived, 2 orphans backfilled, `--verify` 0). A read-only
*key* path fails at the first checkpoint's `ensureKey` after the manifest is saved,
leaving it **unsigned** until the next run. *Counsel:* catch at the top level, print one
line, emit the JSON report with an `error` field, document the status.

**MC6 — minor (pre-existing) — the repo-dest guard is bypassed by a symlinked dest.**
`insideGitWorkTree` (155) resolves with `path.resolve`; a dest that is a symlink into a
work tree archived with exit 0 and no stderr. The guard exists for exactly the operator
slip it misses. *Counsel:* `fs.realpathSync` on the dest (and on the restore root).

**MC7 — minor — harvest.** No `CHANGELOG.md` entry for `210/170` or for the 2026-10-03
queue run (the 2026-09-18 and 2026-09-20 runs have them). `.TH` date unchanged at
2026-08-09 across a content change. "every 50" hardcoded in prose beside a named constant.
`CCARCHIVE_CHECKPOINT_EVERY` and `CCARCHIVE_TEST_FAIL_AFTER` undocumented; the page has no
ENVIRONMENT section to hold them.

**MC8 — minor (process) — the shared review worktree does not contain the delta.** See
provenance. A reviewer trusting the worktree's `instruments/` would have reviewed and
re-run pre-delta code; its 277/277 proves nothing about this change. *Counsel:* merge or
rebase main into the review branch before spawning, or have the brief name the commit to
clone rather than "HEAD".

**MC9 — note — landing modes and a planted temp symlink.** Manifest, signature and
mirrors land `0644`; a pre-planted `manifest.json.tmp` symlink is followed and becomes
`manifest.json`. Both need write access to the dest, which the signing design already
concedes to the tamperer; recorded for the catalogue, not for action.

**MC10 — note — checkpoint cost on a synced dest.** Each checkpoint rewrites the whole
manifest (a few MB at 8,000 entries) and re-signs; on iCloud Drive a bulk first run of
8,000 files uploads the manifest ~160 times. The code comment weighs this and accepts it;
recorded so the trade is visible.

### Re-run ledger

All at `17c75a9` in the scratch clone unless marked; dates 2026-10-03 UTC.

| Command | Result |
|---|---|
| `node --test instruments/*.test.js` (at `4ff8de5`, pre-delta — see provenance) | 277 pass, 0 fail, 16.3 s |
| `node --test instruments/ccarchive.test.js` | 104 pass, 0 fail |
| `instruments/ccarchive --help` | exit 0, digest points at the page |
| `node --test --test-name-pattern="superset\|roff\|digest" instruments/ccarchive.test.js` | 3/3 |
| `mandoc -T lint instruments/man/ccarchive.1` | exit 0, no output |
| Mutation: delete line 1188, run the five new tests | 5/5 pass (MC3) |
| Mutation: disable the catch-path save, run the two death tests | 1 fail, 1 pass |
| `SIGKILL` ×8 over 1,500 files (`=50` ×5, `=1` ×3), then `--verify`, next run, `--verify` | ahead 36/1/18/42/23 and 1/1/0; each `--verify` exit 1 UNMANIFESTED=ahead, sig verified; next run → 1,500 entries, `--verify` 0 — except trial 3: 1 torn mirror, `--verify` after heal **crashes** (MC2) |
| Shape A (entry lags fresh mirror) HEAD / pre | heals, `--verify` 0 / stuck MISMATCH |
| Shape B (entry, no mirror) HEAD / pre | re-archived, `--verify` 0 / same |
| Shape C (same-size rewrite, mtime kept) HEAD / pre | no heal, `--verify` 0, `--audit` 1 rewritten / same |
| Shape D (truncated, newer; then `--force`) HEAD / pre | REFUSED exit 1; forced overwrite / same |
| Shape E (older-mtime shorter source) HEAD / pre | entry→8 B, `--verify` MISMATCH ×2 runs, `--audit` synced / untouched, `--verify` 0, `--audit` shrunk (MC1) |
| Shape F (truncate mtime-kept, heal, append newer) HEAD / pre | guard passed, good mirror overwritten, `--verify` 0 / REFUSED (MC1) |
| Shape G (torn mirror, newer mtime, no entry) HEAD / pre | backfilled from source; `--verify` crash, empty stdout / same (MC2) |
| Shape H (manifest newer than signature) | `--verify` tampered; next run re-signs; `--verify` 0 (MC4) |
| Read-only dest root, `=2` | exit 1, stdout empty, stack trace; 2 mirrors, no manifest; heal clean (MC5) |
| Read-only key dir, `=1` | exit 1; manifest yes, signature no (MC5) |
| Symlinked source file + dir | not followed: total 1, archived 1 |
| Dest symlink into a `.git` parent | archived, exit 0 (MC6) |
| Planted `manifest.json.tmp` symlink | followed; `manifest.json` is a symlink (MC9) |
| `stat -f %Sp` on outputs | `0644` manifest/sig/mirror, `0600` key |

Full-disk was driven as the read-only-path equivalent (same `writeFileSync` throw inside
`persist()`), not a real ENOSPC; stated as such.

### Follow-up checklist

- [ ] MC1 — heal direction: mirror, not source; tests for shapes E and F (Mike's call)
- [ ] MC2 — atomic mirror write; `--verify` reports rather than throws on a bad gzip
- [ ] MC3 — a test the checkpoint can fail
- [ ] MC4 — man page hard-kill wording; signature-window claim
- [ ] MC5 — top-level catch, JSON error report, EXIT STATUS entry
- [ ] MC6 — `realpathSync` in the repo-dest guard
- [ ] MC7 — CHANGELOG entry, `.TH` date, document the two env seams
- [ ] MC8 — review-branch provenance for the remaining 160/440–480 passes in this worktree
- [ ] MC9, MC10 — record only

Phase 1 ends here. Sibling not opened; no other `docs/reviews/2026-10-03-*` file opened; no
file but this one edited.

### Reconcile

Phase 1 was committed unrevised at `b3c972b` (merged to main in `d253354`) before the
sibling was released. Opened for this section, in this order: the sibling's text (by
message), the board item `210/170`, the intent record's `210/170` section (lines 143–153),
and the two 2026-07-17 verdicts the sibling names. Nothing in phase 1 is revised.

**Against the intent record and the board item.** The author's framing is that the fix
"heals an entry whose size disagrees with a fresh-by-mtime source", and the board item
adds the warrant: "this is sound because a mirror is only ever stamped with the mtime of
the source version it was written from." That is the premise MC1 falsifies — the stamp
proves what the mirror *was written from*, not what the source *now is*. The item's own
measurement is consistent with either direction of heal (in 11 of 14 the mirror already
equals the source, so healing from the source and healing from the mirror give the same
entry there), which is why the field case did not expose it; shapes E and F are the cases
where the two directions disagree. The item's second claim, "the manifest never claims a
mirror that is not there", is true of absent mirrors and not of torn ones (MC2). Its third,
"a hard kill can now leave at most 50 mirrors ahead", the real-kill drive confirms (max 42
observed); the man page's stronger wording is what MC4 is about, not the item's.

**The board item's residual, and a mis-fit I can now name.** The item records "locking is
still open" and keeps itself `[ ]`. Phase 1 did not probe overlapping runs (not in the
brief's scope), so nothing here speaks to the lost-update hypothesis. But the item's
*first* hypothesis for the field lag — a stale in-memory manifest from one run overwriting
a newer one — is also the shape MC1's heal makes worse, not better: after a lost update, a
later run's heal rewrites the surviving entries from whatever the source then holds. Noted
as a consequence, not a new finding.

**Against the prior findings.**

- *2026-07-17 F1 (ruled, fixed)* — the shrink guard. **MC1's shape F re-opens it by a side
  door.** F1's attack was a smaller source with a *newer* mtime; the guard still refuses
  that (shape D). The heal supplies a path F1 never had: a smaller source with a
  *not-newer* mtime lowers the recorded `rawBytes` first, and the next append then passes
  the guard the ruling installed. The item itself calls the stale-comparand direction
  "permissive, which is the direction that loses data" — the heal was built to raise the
  comparand and in shape F lowers it. Severity stands at MAJOR.
- *2026-07-17 F4 (ruled)* — unmanifested files and the circular `fromArchive` hash. The
  kill drive shows the `UNMANIFESTED` report doing its job (every killed run reported the
  gap, exit 1), so F4's fix is what makes the hard-kill residual visible. No change.
- *2026-07-17 cli-docs F1 (ruled)* — EXIT STATUS fell behind new non-zero exits; the
  ruling's doctrine was "every new non-zero exit path owes coverage in both registers".
  **MC5 is a recurrence of that class**: the part-way failure is a new documented behaviour
  with an undocumented exit, and the superset test cannot see it (it pins flags, not
  exits). Severity stays minor; the class recurrence is the point for the principal.
- *Open 210/020, 210/030 (encryption at rest), 210/160 (file vs session counts)* — out of
  this pass's scope by the brief's non-goal; MC2's atomic-mirror counsel and 210/020's
  "encrypt with age" counsel touch the same write path, so a fix for one should be designed
  with the other in view. No finding.

**The sibling's seeded questions, answered from phase 1's drives.**

1. *Can a mid-run checkpoint make `--verify` approve an archive missing bytes?* Not by the
   checkpoint itself: every killed run's `--verify` exited 1 with the gap named. **Yes by
   the heal** (shape E): the manifest is rewritten to describe bytes the mirror does not
   hold — `--verify` then fails on an intact mirror, and `--audit` approves a live store
   that differs from the archive. And **yes after a torn write** (shape G, MC2): the
   manifest attests the source's bytes against a 0-byte mirror, and `--verify` does not
   approve — it crashes, which is worse than a wrong answer because it reports nothing.
2. *Which way does the heal move data, and can a bad source win?* Source → manifest, never
   touching the mirror's bytes. A bad source wins whenever its mtime is not newer than the
   mirror's (E, F). The one direction the manifest should never be written from is the one
   the heal reads (MC1).
3. *Is every new exit in EXIT STATUS, and does the superset test cover it?* No and no
   (MC5). The superset test checks flags against the page; it has no view of exits.
4. *Does the heal respect the shrink guard?* It runs on the skip path, where the guard
   does not fire, so the two never meet in one run — and that is the problem: the heal
   rewrites the guard's comparand (`rawBytes`) without the guard's protection, and the
   guard then trusts it next run (shape F, MC1).

**Findings formed at reconcile:** none. Every finding above was formed and recorded in
phase 1 before the sibling, the intent record or the prior verdicts were opened; this
section relates them to that material and changes no severity.

**Overall line, restated: PASS-WITH-FINDINGS — 2 MAJOR · 2 MODERATE · 4 minor · 2 note
(MC1–MC10).** Findings are the principal's to decide (rule 3); nothing applied.

Phase 2 ends here. Reviewer `claude-fable-5-1`, spawned by the brief-writer, Fable tier.

## Folded sibling — released after the phase-1 findings were committed

The `.deferred.md` sibling the orchestrator held outside the worktree, folded in
verbatim at close; the reviewer met it only in phase 2.

# Deferred sibling — ccarchive's manifest checkpoints and stale-entry heal (MC)

Held by the orchestrator outside the worktree and outside the harness
scratchpad. Released to the reviewer only after its phase-1 findings are
committed. Folded into the verdict file at close.

## 1. The queue pointer's own framing (author's words)

> - ⏳ **Rule-4 cold pass queued: ccarchive's manifest checkpoints and
> stale-entry heal (`210/170`).** The run authored this itself (its
> dispatched workers' output counts as the run's authorship). It was
> queued at landing, and the run neither takes it nor spawns a reviewer
> for it. *Tier:* Fable, the principal-named review tier, checked at
> selection. *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
> *Delta, scoped to paths:* `instruments/ccarchive`,
> `instruments/ccarchive.test.js` and `instruments/man/ccarchive.1`. It
> landed on `main` on 2026-10-03, in merge `0264387`.
> *Intent record:*
> `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`.

## 2. Intent record and commissioning item (read in phase 2)

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`
- the board item named in the pointer

## 3. What the authoring run said to the orchestrator (channel, verbatim)

> A fourth refs-only pointer of mine is on main, docs/roadmap/160-doctrine-review-owed/460-rule-4-cold-pass-queued-the-manifest-checkpoints.md, a code pass on ccarchive. No other detail.

Nothing else from that run was read by the orchestrator.

## 4. Prior findings and seeded questions (the orchestrator's, labelled)

Prior findings on this instrument (ruled unless stated):

- 2026-07-17 ADR 0006 / ccarchive-preserve pass, F1 (MODERATE, ruled, fixed): a
  corrupt or truncated source with a newer timestamp overwrote the only durable copy
  and `--verify` approved it; the fix refuses a re-archive smaller than the recorded
  size without `--force`. F2: guard 2 was a default, not code. F3: layout drift
  failed silently with exit 0. F4: unmanifested files and the circular `fromArchive`
  hash.
- 2026-07-17 cli-docs-applied F1 (MODERATE, ruled): the man page's EXIT STATUS
  predated the new non-zero exits; the layout-drift alarm was missing from the page.
- Open board items: 210/020 and 210/030 (encryption at rest; one decision, counsel
  "encrypt with age, decrypt in-process"), 210/160 (reports file counts, not session
  counts). All await the principal.

Seeded questions (the orchestrator's): (1) Can a checkpoint written mid-run ever
make `--verify` approve an archive that is missing bytes? (2) Which way does the
heal move data, and can a bad source win? (3) Is every new exit in EXIT STATUS, and
does the superset test cover it? (4) Does the heal respect the shrink guard?
