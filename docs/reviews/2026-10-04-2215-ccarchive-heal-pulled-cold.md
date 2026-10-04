# Cold pass — ccarchive's skip-path heal pulled

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-04 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/510-rule-4-cold-pass-queued-the-heal-pulled.md`.
**Why it earns a review:** ccarchive holds the only durable copy of every
session transcript; this delta removes a repair path that an earlier pass found
could overwrite a good archived copy, and a removal that is incomplete, or that
strands the state the repair existed for, leaves that copy untrustworthy in a
different way.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the commits named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-04 UTC
  with the prompt "Do all cold reviews and any other work dependent on fable",
  on the Fable tier (`claude-fable-5-1`), orchestrating three rule-4 passes
  (code passes from a seventeen-pointer queue; the principal sized this sitting
  to the weekly allowance he had left). It wrote this brief from the queue
  pointer, the landing commits' subjects and file lists, and the delta paths'
  names; it did not open the intent record or any prior verdict on these
  surfaces.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree and outside
  the harness scratchpad, commits the reviewer's phase-1 findings unrevised,
  then releases the sibling's text by message; the reviewer appends a reconcile
  section; the orchestrator folds the sibling in and updates the pointer. The
  orchestrator forms no finding and writes no severity. Both seats are Fable, so
  the off-tier clause is not invoked; the shape is stated anyway so the record
  is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the tail of the `docs/SESSIONS.md` index (entries of 2026-09-25 to
  2026-10-03), which includes the authoring run's own one-paragraph summary of
  its work and the 2026-10-03 review session's summary naming finding MC1 in one
  line; every queued `⏳` pointer in section 160 in full (each is refs-only); the
  brief half of `docs/reviews/2026-10-03-0357-manifest-checkpoints-cold.md`
  (lines 1–140, no verdict text) as a formatting template; the landing commits'
  subjects and `--stat` file lists (never the diffs); its own cross-session
  memory notes, which carry the principal's standing words on exceptions and
  guards; and, as doctrine at onramp, `docs/method/ECONOMICS.md` § the
  self-check and the headings of `docs/method/REVIEW.md`. Everything evaluative
  it knows about this delta is in the sibling, not here.

## What the work is

Landing commits (diff these; review the paths at HEAD, `3d4fd9d` or later):

- `1da9101` (2026-10-03) — ccarchive: pull the skip-path heal
- `5870927` (2026-10-03) — the earlier commit that added the checkpoint and the
  heal; context for what was removed, already reviewed separately — review what
  `1da9101` left standing, not `5870927` afresh

Delta paths:

- `instruments/ccarchive`
- `instruments/ccarchive.test.js`
- `instruments/man/ccarchive.1`

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Driven, not read. Whether the removal is complete: no code path at HEAD lets the
source overwrite an intact mirror copy without the shrink guard or `--force`.
Whether what the removed path used to repair is now reported, silently skipped,
or left permanently wrong — construct each lagging shape by hand in a scratch
archive (a manifest entry behind its archive file, an archive file with no
manifest entry, a hash mismatch in each direction, a source truncated after it
was archived, a run killed between copy and checkpoint) and run an archive pass
then `--verify` over each, recording what changes, what is reported and the exit
code. Whether the manifest checkpoint that remains is still correct without the
heal beside it. Whether the tests removed or rewritten leave the surviving
behaviour pinned, and whether a test now asserts the overwrite cannot happen.
Whether the man page describes the tool as it stands. **Non-goal:** encryption
at rest, and the board items that commissioned the work.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Pulling a repair presumes the state it repaired is either rare, harmless, or
   caught elsewhere: find which, and test it. Ask whether removal was the
   narrowest safe answer or whether it trades one integrity failure for a
   quieter one.
2. **Correctness & quality.** Read all of `instruments/ccarchive` and its tests.
   Diff `1da9101`. Run `node --test instruments/*.test.js`, `--help`, and every
   state in *Scope*. Check every exit path is in the man page's EXIT STATUS and
   no dead code, flag, message or test fixture of the removed path survives.
3. **Completeness / harvest.** Every surface that states the archive's integrity
   contract: the man page, `instruments/README.md`, the ADR 0006 record's
   ccarchive material, `CHANGELOG.md`, `--help`. Does each still hold at HEAD,
   and does any still promise the removed repair?
4. **Security & privacy** — mandatory. The tool writes a durable store from
   source files it does not control. Check no remaining path lets a crafted or
   damaged source (timestamp, size, truncation, symlink) replace or shadow a
   good archived copy, and that partial writes land safely. The house scanner is
   discharged by grounds (landed delta; the pending diff is other passes' drafts
   and this brief) — say so, and deliver the code-altitude read by hand, against
   the OWASP catalogue.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `node --test instruments/*.test.js` (foreground, once)
- `instruments/ccarchive --help`; the man page's option superset test
- every lagging and crash state in *Scope*, in a scratch archive under your
  clone, never against the real archive or `~/.claude`

## House rules for this run

- You work in the shared review worktree
  `/Users/mike/worktrees/atelier-review-1004` (branch `review-1004`), read-only
  except for THIS brief file. Other sessions are live on this machine and in the
  primary checkout — touch nothing there. Other reviewers are working there at
  the same time on their own briefs; never open another
  `docs/reviews/2026-10-04-2215-*` file — it is another pass's framing.
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
`docs/roadmap/160-doctrine-review-owed/510-rule-4-cold-pass-queued-the-heal-pulled.md`
(it carries the author's own lens hints), and:

- `docs/reviews/2026-10-03-0357-manifest-checkpoints-cold.md` (the prior verdict
  on the heal)
- `docs/reviews/2026-07-17-1000-adr0006-ccarchive-preserve-cold.md` and
  `docs/reviews/2026-07-17-1157-cli-docs-applied-cold.md`
- every item under `docs/roadmap/210-instruments-open-features/`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-1004 --also-exclude
docs/roadmap/160-doctrine-review-owed/510-rule-4-cold-pass-queued-the-heal-pulled.md
--also-exclude docs/roadmap/210-instruments-open-features <pattern>` — rule 2's
default bar, plus `--also-exclude` for the items above; `--include-barred` only
with disclosure in the verdict. Reading the *delta* is never barred: the code,
its tests, the doctrine text and the catalogue entries are the subject. What is
barred is the author's narrative of why, and the verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `HL`: `HL1`, `HL2`, …) and severities (MAJOR / MODERATE
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

# Verdict — phase 1 (written 2026-10-04 UTC)

## Provenance

- **How I was spawned:** a fresh subagent started by the batch orchestrator with
  this brief as its only framing, plus a short task message (prefix `HL`, phase 1
  only, the worktree and scratch rules). I am not the author's session and was
  not instructed by it.
- **Tier:** Fable (`claude-fable-5-1`).
- **What I read:** this brief; all of `instruments/ccarchive` at HEAD; the diff
  of `1da9101` over the three delta paths; `instruments/ccarchive.test.js` lines
  1385–1503 and its `test(` index; `instruments/man/ccarchive.1` INTEGRITY,
  SIGNING (opening), EXIT STATUS and NOTES; `instruments/README.md` § ccarchive
  integrity bullets; `grep` hits for ccarchive in `CHANGELOG.md` and ADR 0006;
  `.githooks/pre-commit` and `ci.yml` for the floor invocations.
- ⚠️ **Exposure, disclosed:** `git show 1da9101` prints the commit message, which
  carries the author's own account of why (it names the prior finding by ID, in
  one paragraph, and quotes the principal's answer). The in-code comment at
  `ccarchive` lines 127–129 and the test title carry the same one-line summary.
  That is the delta itself and could not be avoided. One `coldsweep` run printed
  board index lines (titles only), including the queue pointer's title line in
  `docs/ROADMAP.md`. My session context also carried the standing memory index
  (process notes; nothing evaluative about this delta). I opened no barred file:
  not the pointer, not `SESSIONS`, not any prior verdict, nothing under
  `docs/roadmap/210-*`, and no other `2026-10-04-2215-*` brief.
- **Where I worked:** a scratch clone of the worktree under the session
  scratchpad (`HL/probe`), with every probe archive, source tree, history file
  and signing key pinned inside the scratchpad (`--source`, `--dest`,
  `CCARCHIVE_KEYFILE`, `CCARCHIVE_HISTORY`, `HOME` all overridden). The real
  archive, the real key and the primary checkout were never touched. One
  deviation: I also ran `node --test instruments/ccarchive.test.js` once from
  the worktree itself; it writes only to OS temp directories and left the tree
  unchanged.

## Headline

The removal itself is sound and should stand: the heal is gone, a test fails if
it is put back, and the man page no longer promises it. But the brief's first
driven question — *no code path at HEAD lets the source overwrite an intact
mirror copy without the shrink guard or `--force`* — is answered **no**, three
ways. The same trust-the-source defect the heal was pulled for is still live in
the backfill four lines below where the heal sat (HL1). The shrink guard reads
the manifest, not the mirror, so the lagging state this delta chose to leave
standing switches the guard off (HL2). And the state the heal used to repair is
now stranded: nothing in the tool repairs it, and the tool's own advice about it
is wrong (HL6).

Three further serious findings sit on the delta paths at HEAD but outside the
`1da9101` diff (HL3, HL4, HL5). I record them because the brief sets scope at
"the paths at HEAD" and asks for these states to be driven; whether earlier
passes already hold them is a phase-2 question I cannot answer from here.

## Lens 1 — approach and assumptions

Load-bearing assumptions I named before testing:

1. *The lagging state is harmless while it waits.* **False** — it disarms the
   shrink guard (HL2, probe S5).
2. *The lagging state is caught elsewhere.* **Half true** — `--verify` reports
   it and exits 1 (S1), but `--audit` calls it "grown" and prescribes a run that
   changes nothing, and `--force` does not repair it either (HL6).
3. *The lagging state is rare.* **Plausible, unmeasured.** With checkpoints it
   needs a hard kill inside a 50-mirror window, or a kill between the mirror
   write and its mtime stamp (S6a). Overlapping runs are a second, likelier
   source that I reasoned but did not probe (HL14).
4. *The source is no longer trusted over an intact mirror.* **False** — the
   skip-path backfill still does exactly that (HL1).
5. *A manifest entry is only ever set after its mirror is fully written.* True
   for the entry; but the mirror itself is written in place, so "fully written"
   is not guaranteed for the file the entry describes (HL4).

Was removal the narrowest safe answer? It was a safe answer to the reported
defect, and the right first move. It was not the complete one: it removed one of
two source-trusting writes on the skip path, and it traded a loud-but-wrong
repair for a quiet state with no repair at all. Counsel, labelled: the repair the
heal wanted is available from the *mirror* (hash the gunzipped bytes, as the
tail backfill already does), which trusts the archive over the source and so
cannot record a damaged source as truth.

## Lens 2 — correctness and quality

Floor reproduced green (ledger below). Every state in *Scope* was built by hand
and driven; the table is the record. "run" is an ordinary archive pass.

| # | State | run | then `--verify` | What changed |
|---|---|---|---|---|
| S1 | entry behind mirror, source unchanged | exit 0, "unchanged" | exit 1, MISMATCH | nothing; `--audit` says "1 grown", exit 0 |
| S1b | S1, then source pruned | exit 0 | exit 1, MISMATCH, for good | nothing; `--audit` green |
| S1c | S1, then source grows | exit 0, re-archived | exit 0 | entry and mirror refreshed |
| S1d | S1 with `--force` | exit 0, "unchanged" | exit 1 | nothing — no repair path |
| S2 | mirror, no entry, source unchanged | exit 0 | exit 0 | entry backfilled from the source |
| S2b | mirror, no entry, source swapped for an older shorter copy | exit 0 | exit 1, MISMATCH on an intact mirror | entry = the short source; a later touch overwrote the mirror, exit 0 |
| S2c | mirror, no entry, source truncated, newer | exit 0, "1 archived" | exit 0 | intact mirror overwritten, no refusal |
| S2d | mirror, no entry, no source | exit 0 | exit 0 | `fromArchive` entry from the mirror |
| S3a | mirror bytes wrong (valid gzip), manifest right | exit 0, "unchanged" | exit 1, MISMATCH | nothing; run does not repair from the intact source |
| S3b | mirror truncated mid-file, fresh mtime | exit 0, "unchanged" | **crash**, exit 1, no report | nothing; `--restore` crashes too |
| S3c | empty mirror, no entry, no source | **crash**, exit 1, every run | exit 1 | new mirrors written but never recorded |
| S4a | source truncated, newer mtime | exit 1, REFUSED | exit 0 | nothing; `--audit` exit 1 SHRUNK |
| S4b | source truncated, mtime kept | exit 0, silent | exit 0 | nothing; `--audit` exit 1 SHRUNK |
| S4c | source rewritten, same size, newer | exit 0, "1 archived" | exit 0 | mirror replaced (documented design) |
| S5 | entry behind mirror, source truncated to a size in between | exit 0, "1 archived" | exit 0 | intact mirror overwritten, loss now invisible |
| S6a | killed between mirror write and mtime stamp | exit 0, "unchanged" | exit 1, MISMATCH | nothing; same as S1 |
| S6b | throw after 3 mirrors (test seam) | exit 1 | exit 0 | catch-path save works; the following run completes |
| S7 | manifest unparseable, one source swapped older and shorter | exit 0 | exit 1, MISMATCH on an intact mirror | whole manifest rebuilt from sources |
| S12 | `--dry-run` over a lag and a missing entry | exit 0 | — | manifest byte-identical |

The checkpoint that remains is correct on its own terms: S6b shows a thrown
failure leaves a covered, signed manifest, and both existing checkpoint tests
pass. Its stated bound holds for a throw, not for a hard kill (HL12).

Dead remnants of the removed path: no code, flag or message survives. One test
section comment still states the removed behaviour (HL11). The helper
`makeStale` is still used and is not dead.

## Lens 3 — completeness / harvest

- **Man page** — the rewritten SIGNING paragraph matches the tool for the plain
  lag (S1). It overclaims in two places and omits exits (HL12), and INTEGRITY's
  promise that `--verify` reports bit rot as a mismatch is false for a mirror
  that will not decompress (HL5).
- **`--help`** — unchanged by the delta, promises no repair; superset test green.
- **`instruments/README.md`** — never described the heal or the checkpoint;
  nothing stale. Its tamper-evidence bullet inherits HL3.
- **ADR 0006** — its ccarchive material is about admission and the write
  boundary; it states nothing about the heal. Holds.
- **`CHANGELOG.md`** — carries no entry for the checkpoint or for the pull; its
  newest heading is dated 2026-09-20 (HL12).
- No surface still promises the removed repair.

## Lens 4 — security and privacy

`/security-review` is **discharged by grounds** for this batch: it reads the
session's pending diff, which in the shared worktree is other passes' unstaged
drafts, and this is a landed-delta review. The code-altitude read was done by
hand against the OWASP catalogue:

- **Software and data integrity failures** — HL1, HL2 (source trusted over the
  archive), HL3 (a manifest re-signed without being authenticated), HL7
  (restore writes unverified archive bytes over a live file).
- **Broken access control / path handling (CWE-59, link following)** — HL9: the
  mirror write follows a symlink planted in the archive. Restore's path-escape
  guard and the external-capture allowlist read correctly; source-side symlinks
  are not followed (probe S11: a symlinked `.jsonl` is not captured).
- **Security logging and monitoring failures** — HL5, HL6, HL8: the tool's
  detection modes crash, mislabel or go permanently red instead of reporting.
- **Injection** — none found. Child processes are `execFileSync` with argument
  arrays; the plist is XML-escaped; nothing parses transcript content.
- **Cryptographic failures** — the HMAC construction, constant-time compare and
  0600 key handling read correctly. The failure is in *when* it signs (HL3), not
  how.
- **Privacy** — the repo-destination refusal stands; no personal path is baked
  in. Probe output in this verdict is paraphrased, with no key fingerprints,
  paths or personal detail.
- Timestamp: an older-mtime source is left alone (documented). Size: HL2.
  Truncation: S4a refused, S4b silent to the run but caught by `--audit`.
  Partial writes: do not land safely (HL4).

## Findings

### HL1 — MAJOR — the pulled defect survives in the skip-path backfill

`ccarchive` lines 1139–1142. When a mirror exists, is fresh by mtime, and has no
manifest entry, the run writes an entry from the **source's** hash and size. That
is the same act the heal was pulled for, one branch away. Probe S2b: mirror
intact at 30 bytes, entry missing, source replaced by an older 12-byte copy. One
ordinary run recorded the 12-byte source as the truth (exit 0); `--verify` then
called the intact mirror a MISMATCH; and when the short source was merely
touched, the following run overwrote the intact mirror with it — exit 0, no
refusal, because the recorded size was now the short one. S7 shows the wholesale
version: an unparseable manifest makes *every* entry missing, so the whole
archive is re-based on whatever the sources hold.

The missing-entry state is not exotic: it is what a hard kill leaves for every
new mirror since the last checkpoint, and the code comment relies on this very
backfill to mop it up. The new regression test's comment says the outcome "must
never" happen; it still can.

*Counsel:* backfill from the mirror (gunzip, hash, record its length), as the
tail backfill does — then compare with the source if one wants a warning.

### HL2 — MAJOR — the shrink guard reads the manifest, so any lag disarms it

`isSuspectShrink` compares the source's size with the entry's `rawBytes`, never
with what the mirror actually holds. Three shapes let a shorter source overwrite
an intact mirror with no refusal and no `--force`, each exit 0:

- **lagging entry** (S5) — entry says 12 bytes, mirror holds 30, source cut to
  18 with a newer mtime: mirror overwritten with the 18-byte file;
- **no entry** (S2c) — source cut to 12: mirror overwritten;
- **`fromArchive` entry** (S10) — these carry no `rawBytes` at all, so after a
  `--restore` the guard is off for that file: mirror overwritten.

In every case `--verify` is green afterwards, so the one signal that marked the
lag is erased by the overwrite. This is the "quieter failure" the brief asked
about: the man page's new sentence (a lagging entry "stays as recorded and
`--verify` reports it") is true only until the source changes. Leaving the lag
standing therefore leaves the sole durable copy unguarded for as long as the lag
lasts.

*Counsel:* take the guard's reference size from the mirror when the entry is
missing, lacks `rawBytes`, or disagrees with the mirror; or treat any overwrite
of a mirror whose bytes are not a prefix of the source as suspect, using the
prefix test `--audit` already has. S4c (same-size rewrite replaces the mirror)
is the documented size-only design and would be covered by the same change.

### HL3 — MAJOR — an ordinary run re-signs a manifest it never authenticated

Outside the `1da9101` diff; on the delta path at HEAD. The run loads the
manifest without checking its signature, and re-signs it whenever it saves or
whenever the signature is anything but `verified` (lines 1116–1120, 1217–1222).
Probes: a swapped mirror plus a manifest edited to match is correctly reported
TAMPER EVIDENT by `--verify` (exit 1); one ordinary run later — with nothing to
archive (S8), or with one new file (P5) — `--verify` is fully green. Deleting
the signature file (P6) or replacing the manifest with garbage (P7) is laundered
the same way. With the daily scheduled run installed, tamper evidence therefore
lasts at most until that run. The man page's claim that "a forged manifest fails
`--verify`" does not hold across a run.

This also bears on the delta: hand-editing the manifest and letting the run
re-sign it is the only way an operator can clear a lagging entry at HEAD (HL6),
and it works only because of this hole.

*Counsel:* verify the signature on load in the write path; on anything but
`verified` (or a genuinely absent signature on first migration, by explicit
flag) refuse and exit non-zero rather than re-sign.

### HL4 — MODERATE — mirrors are written in place; a partial write is never repaired

`fs.writeFileSync(destAbs, gz)` at line 1165 truncates the previous good mirror
and writes over it; only the manifest and signature use write-then-rename. A
kill inside that write leaves a truncated mirror stamped with the current time,
which is newer than its source — so every later run skips it as "unchanged"
(S3b: exit 0) although the source is intact and present. If the session never
grows again, the source is pruned at the retention limit and the transcript is
gone. The state is noisy only if someone runs `--verify`, and then only as a
crash (HL5). I built the state by hand rather than by killing a live run; the
window is one file write wide. Rated MODERATE on that narrow window; the impact,
when it lands, is loss of the sole durable copy.

*Counsel:* write to a temporary name, stamp it, rename over the mirror.

### HL5 — MODERATE — an undecompressable mirror crashes `--verify`, `--restore` and the run

`--verify` treats only "file absent" as reportable; any gunzip error is rethrown
(line 677). One flipped byte in one mirror (P2), a truncated mirror (S3b) or a
non-gzip file (S11) ends `--verify` with an uncaught stack trace: exit 1, but no
report, no file name, nothing checked after it, and empty stdout under `--json`.
`--restore` fails the same way (line 989). In the run's tail backfill the same
error (S3c) is thrown outside the save path, so every run exits 1 and mirrors
written during those runs never reach the manifest. The man page says `--verify`
reports "bit rot or a sync glitch" as a mismatch; for the commonest form of bit
rot in a compressed file it does not. No test covers an undecompressable mirror.

### HL6 — MODERATE — the lagging state is stranded, and the tool's advice about it is wrong

With the heal gone there is no repair for an entry behind an intact mirror:
an ordinary run leaves it (S1), `--force` leaves it (S1d), and once the source is
pruned `--verify` exits 1 for good (S1b). Meanwhile the surfaces mislead:
`--verify` prints a bare MISMATCH with no next step (the UNMANIFESTED line has
one); `--audit` classes the file "grown", exits 0 and says to run ccarchive to
catch up, which changes nothing (S1). The only exits are the source happening to
grow (S1c), the destructive direction in HL2, or hand-editing the manifest
(HL3). A check that is permanently red stops being read. The removal was right;
what it left owing is a repair that trusts the mirror, and a message that says
what the state is.

### HL7 — MODERATE — `--restore` writes archive bytes it has not checked

Outside the diff. Restore never compares the gunzipped mirror with the manifest
hash. P1: a mirror that fails `--verify` (MISMATCH) was restored over an intact
live file — "RESTORED … rewritten", exit 0 — replacing 30 good bytes with the
bad 8. The live file's mtime guard does not help when the mirror's mtime is
unchanged, as it is after rot.

### HL8 — MODERATE — one unreadable source aborts the whole run, every run

A source file (S9) or directory (P9) that cannot be read throws out of the walk
or the loop: uncaught stack trace, exit 1, and nothing after it in walk order is
archived — on that run and on each one after. With a 30-day prune behind it, a
single bad file turns into silent loss of everything queued behind it. The same
path is taken if a source disappears between the walk and its read (reasoned
from the code, not probed). This exit is not in the man page's EXIT STATUS.

### HL9 — MODERATE — the mirror write follows a symlink in the archive

P3: with a symlink planted at a mirror's path, a run wrote the compressed bytes
through it into a file outside the archive, exit 0. The man page names anyone
who can write to the archive volume as the adversary, and its NOTES say the tool
"writes only under the destination"; this lets that adversary overwrite any file
the user can write, the signing key included. CWE-59. HL4's write-then-rename
would close it as a side effect.

### HL10 — minor — read-only modes move the manifest aside, and keep only the newest casualty

`loadManifest` renames an unparseable manifest to `manifest.json.corrupt` from
`--verify`, `--audit` and `--restore` alike (P8, S7) — modes documented as
read-only — and a second occurrence overwrites the first preserved copy (P8).
Any read error other than "absent" takes the same path (code read; not probed
for an I/O error). The following run then rebuilds the trust anchor from current
state (S7, P7). The man page does not describe the `.corrupt` behaviour.

### HL11 — minor — the regression test pins less than its comment claims; one stale comment

Mutation: reinstating the heal in the scratch clone fails exactly one test (the
renamed regression test), so the removal is pinned. But that test leaves the
source unchanged; it does not build the shape it names (a source replaced by an
older, shorter copy), does not assert the mirror's bytes survive, and nothing
covers S2b or S5. The answer to "does a test now assert the overwrite cannot
happen" is no. The section comment at `ccarchive.test.js` lines 1427–1429 still
says a lagging manifest "must heal on the next ordinary run".

### HL12 — minor — the man page overclaims the checkpoint; the changelog is silent

"A run that dies leaves the manifest covering every mirror it had written" holds
for a thrown failure (S6b), not for a hard kill; the code comment beside
`CHECKPOINT_EVERY` says as much (up to 50 ahead). The man page does not say that
unrecorded new mirrors are backfilled, or from what. EXIT STATUS lists three
reasons a run exits 1 and omits every uncaught failure (the catch path rethrows
by design). `CHANGELOG.md` has no entry for the checkpoint or for the pull.

### HL13 — note — test seams live in the production path, undocumented

`CCARCHIVE_TEST_FAIL_AFTER` and `CCARCHIVE_CHECKPOINT_EVERY` are read on every
real run and appear nowhere in the man page. Harmless unless set by accident;
the first would kill every run.

### HL14 — note — overlapping runs are a likelier source of lag than a hard kill (unprobed)

Each run holds the whole manifest in memory and saves it whole. Two overlapping
runs (the scheduled one and a manual one) would let the later save put back an
older entry for a file the other had just re-archived — a lagging entry with no
kill at all. The man page says overlap is not locked against. This is reasoning
from the code; I did not build a timing probe, so it is a note, not a finding.

## Overall

**PASS-WITH-FINDINGS** — 3 MAJOR, 6 MODERATE, 3 minor, 2 notes.

The pull stands and should not be reverted. Its completeness claim does not: the
source can still be recorded over, and written over, an intact mirror (HL1, HL2).

## Re-run ledger

All in the scratch clone at `f1a667b` unless marked; Node v24.18.0.

| Command | Result |
|---|---|
| `node --test instruments/*.test.js` | exit 0 — 285 pass, 0 fail |
| `node --test instruments/ccarchive.test.js` (worktree, once) | exit 0 — 103 pass, 0 fail |
| `instruments/ccarchive --help` | prints the digest; the man superset test is in the 285 and passes |
| `mandoc -T lint instruments/man/*.1` | exit 0, no output |
| `python3 tools/floor.py --plane ci --root .` | exit 0 — enforced checks green, three warn-only |
| `python3 -m unittest discover -s tools` | **not run** — the delta touches no Python; held back under the one-heavy-process rule with other reviewers live |
| mutation: reverse-apply the `1da9101` code hunk, run the ccarchive tests | exit 1 — 102 pass, 1 fail (the regression test); clone restored after |
| `node probe1.js` (S1–S12, 22 scratch archives) | results in the Lens 2 table and findings |
| `node probe2.js` (P1–P9, 8 scratch archives) | results in the findings |

Probe scripts and raw output are in the session scratchpad under `HL/`
(`probe1.js`, `probe1.out`, `probe2.js`, `probe2.out`, `mut1.out`, `floor.out`).

## Follow-up checklist

- [ ] HL1 — backfill an unrecorded mirror from the mirror, not the source; test
      the S2b and S7 shapes.
- [ ] HL2 — anchor the shrink guard on the mirror when the entry is missing,
      lacks `rawBytes` or disagrees; test S5, S2c, S10.
- [ ] HL3 — authenticate the manifest before any write-path re-sign; decide the
      migration path for a genuinely unsigned archive. Principal's call on shape.
- [ ] HL4 / HL9 — write mirrors by temporary file and rename.
- [ ] HL5 — report an undecompressable mirror by name as a failure in
      `--verify`, `--restore` and the tail backfill; keep going; add tests.
- [ ] HL6 — give the lagging state a mirror-trusting repair and an honest
      message in `--verify` and `--audit`.
- [ ] HL7 — check restored bytes against the manifest hash before writing.
- [ ] HL8 — skip-and-report an unreadable source; exit non-zero at the end.
- [ ] HL10 — no renames from read-only modes; never overwrite a kept copy.
- [ ] HL11 — strengthen the regression test to the named shape and pin the
      mirror bytes; fix the stale section comment.
- [ ] HL12 — correct the man page's checkpoint claim and EXIT STATUS; add the
      changelog entries.
- [ ] HL13, HL14 — document or gate the seams; decide whether overlap needs a
      lock, after a probe.
- [ ] Phase 2 — reconcile against the sibling and the prior verdicts, especially
      whether HL3, HL4, HL5 and HL7 are already held elsewhere.
