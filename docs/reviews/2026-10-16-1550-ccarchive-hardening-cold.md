# Cold pass — ccarchive hardening: atomic writes, a trust model, two kinds of data, a schedule

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes this pass; a session that cannot honour it stops.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or
instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/670-rule-4-cold-pass-queued-ccarchive-hardening.md`.
**Why it earns a review:** `ccarchive` is the only kept copy of the principal's
Claude Code history once the live files age out; the delta rewrites how it
writes, what it trusts, what it overwrites and when it runs unattended. A
defect here destroys or silently corrupts the one record nothing else holds,
and the tool now installs an operating-system schedule.

## Spawn provenance

- **Author of the work under review:** the run whose intent record is dated
  2026-10-04 23:29 UTC (path in the sibling; not opened by this writer). Its
  commits carry Sonnet and Opus co-author trailers (dispatched workers and the
  orchestrator). Two widening commits, `bab1451` and `72e0093`, landed after that
  run's close commit `7e5c489`; the pointer counts them in the delta, and the
  reviewer establishes their authorship from metadata.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched by the
  Mike-opened Opus queue-run session `abe96d8d` on 2026-10-16 UTC, on Mike's
  answer that day that a fresh Opus session writes these briefs. Neither it nor
  its orchestrator authored, started or instructed the authoring run, and
  neither edited the delta. It is **off-tier for review, disclosed: it forms no
  finding and writes no severity**, and it stopped after this brief and its
  sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that
  passes rule 4's criterion. It repeats its own provenance in its verdict and, if
  it runs under an orchestrator, discloses that shape as rule 4 requires.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This writer
  read: the queue pointer in full; the subjects, `--stat` and full message bodies
  (the author's account, which cite finding IDs from earlier verdicts and board
  items) of every commit in the series; targeted greps of `instruments/ccarchive`
  at HEAD (subprocess, crypto, lock, schedule and reserved-area sites), the man
  page's section list and § FILES, and the test file's isolation preamble — not
  the full diffs; `REVIEW.md` down to § *Whether work earns a review*; the ask
  halves of two 2026-10-04 briefs as format models; filename listings of
  `docs/reviews/` and `docs/roadmap/`, and path and ID greps over `docs/reviews/`
  that name prior verdicts without reading them; and its auto-loaded
  cross-session memory index, whose one-line notes include one on this tool's
  schedule flags. Its orchestrator read the `docs/SESSIONS.md` index tail (entries
  through 2026-10-16, including the authoring runs' one-paragraph summaries) and
  the 2026-10-16 session record's close section, and passed this writer nothing
  evaluative beyond the pointer list. What this writer suspects is in the sibling.

## What the work is

The whole delta is `git diff ee7db7a eade807 --` the delta paths (≈5,400 lines
added). Landing commits, in order:

- `90683d3` (2026-10-05) — ccarchive: harden writes and failures, drop the
  schedule installer *(Part A)*
- `dcdf40b` (2026-10-05) — ccarchive: build the archive's trust model —
  authenticate, journal, adopt, lock *(Part B)*
- `cafa292` (2026-10-05) — ccarchive: keep two kinds of data apart — anomalies
  aside, versions beside, counts a person reads *(Part C)*; all three landed in
  merge `8540a1d` (210/210)
- `bab1451` (2026-10-05) — cctranscript: skip ccarchive's kept-copy areas too
- `72e0093` (2026-10-05) — ccarchive: rebuild the schedule installer as a real
  calendar schedule; landed in merge `eade807` (210/230)

Delta paths: `instruments/ccarchive`, `instruments/ccarchive.test.js`,
`instruments/man/ccarchive.1`, `instruments/README.md`, `instruments/ccrepo`,
`instruments/ccrepo.test.js`, `instruments/cctranscript`, `CHANGELOG.md`. Review
at HEAD; since `eade807` only `instruments/cctranscript` has moved on these paths
(160/680's change, a non-goal here).

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the archive is never lost, never silently wrong, and never trusted past
what the tool can vouch for — on every state a run can meet. Drive, in a scratch
HOME with a scratch source, destination and key, every state below and record a
table (state × mode → files touched, exit code, report line):

- **Writes and failures (Part A).** A kill at each step of the temp → fsync →
  rename sequence; a symlink at a mirror path, at a directory, at the destination
  root; a stale temp whose pid is now a live, unrelated process; an unreadable
  source file and directory; an undecompressable mirror under `--verify`,
  `--restore`, `--audit` and an ordinary run; a restore whose bytes miss the
  recorded hash, with and without `--force`; an evicted (dataless) mirror via the
  test seam. Is every exit code what § EXIT STATUS says, plain and `--json`?
- **Trust (Part B).** Name the adversary the signature defends against and the
  one it does not. Then: a manifest edited by one byte; an older valid manifest
  and signature pair put back (rollback); a journal record replayed from an
  earlier run; a mirror planted with no entry; a planted mirror identical to the
  live copy; a legacy entry with no stat fields; a destination reached through a
  symlink or renamed (the journal's id is a hash of the real path); two runs at
  once; a lock left by a dead run, by a reused pid, by another host; one
  destination shared by two machines while the lock lives under each machine's
  own home; `--rekey`, `--lock-status`, `--clear-lock`.
- **Two kinds of data (Part C).** Every captured class against the kind table,
  and a path the table does not know; an append-only record that grows, shrinks,
  is rewritten at equal length, or is rewritten then grows; a living document
  that only appends; the same anomaly met on three runs; `--force` on an
  anomaly; a kill between the version rename and the new write; the
  signature-then-manifest swap killed at each step; the legacy-entry budget at
  zero, negative, non-numeric and huge; the count fields across runs with zeros.
- **Schedule (`72e0093`).** Generated launchd, systemd and crontab text for a
  home path or tool path holding spaces, quotes, `&`, `<`, `%` and a newline;
  `--at` at `24:00`, `23:60`, `7:5`, empty and padded; re-install over the old
  login-style agent; uninstall where another program's agent sits beside it;
  every schedule flag combined with every archive flag. All of it under the
  scheduler-log seam — never a real scheduler.
- **Cross-tool.** The reserved area names (`_external`, `_untrusted`,
  `_anomalies`, `_versions`) as each of `ccarchive`, `ccrepo` and `cctranscript`
  skips them; whether a real project directory can carry one of those names.

**Non-goals:** encryption at rest (the man page marks it planned, not built);
the first-prompt prefix read in `cctranscript` (160/680's subject); the records
commit `21a772f`, which touches barred paths only. Each is reviewable as a
narrowing.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first —
   among them, what "vouch for" means, what a same-user attacker can and cannot
   do to a key that sits in the same home as the transcripts, and whether a
   two-kind data model fits every class the tool captures.
2. **Correctness & quality.** Read the source, tests and man page at HEAD, the
   diff in parts by commit. Drive the tables above. Every claim in the commit
   messages and § CHANGELOG is a claim to test: test counts, "fails against the
   previous code", "N targeted mutations each caught" — re-run a sample with
   mutations of your own choosing in your clone.
3. **Completeness / harvest.** Man page against behaviour, section by section
   (§ ENVIRONMENT complete? § EXIT STATUS complete? § FILES exact?); `--help`;
   `instruments/README.md`; `CHANGELOG.md`; the reserved-name lists as one fact in
   three tools (V4); BSD-only subprocess calls (`stat -f`, `ps -o lstart=`) now
   that the schedule claims Linux; what CI on Ubuntu actually exercises.
4. **Security & privacy** — mandatory and central. Code altitude, against the
   OWASP catalogue: argument injection into `stat`, `ps`, `launchctl` and
   `systemctl` argv (a path beginning with `-`); path traversal through a
   manifest or journal `rel` on restore, adopt, set-aside and version; symlink
   races between check and rename; HMAC use (constant-time compare, key
   generation, a pre-existing key file with wide permissions); environment test
   seams (`CCARCHIVE_TEST_*`, `CCARCHIVE_SIMULATE_DATALESS`,
   `CCARCHIVE_SCHEDULER_*`) live in the shipped tool; injection into generated
   plist, unit and crontab text; newline and control characters from file names
   into reports and `--json`; decompression bombs under `--verify`. Design
   altitude: kept copies multiply retained private transcripts — where do they
   live, with what modes, and is any retention ever bounded? `/security-review`:
   discharge by grounds (landed delta; the pending diff is other passes' drafts)
   and do this read by hand, or aim it only at a clean tree.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- after confirming the test file's isolation (it is under review too):
  `node --test instruments/ccarchive.test.js`, then `ccrepo.test.js` and
  `cctranscript.test.js`, then `node --test instruments/*.test.js` once, all in
  the foreground, from your clone
- `mandoc -T lint instruments/man/ccarchive.1` and `man -P cat` on the same file;
  `instruments/ccarchive --help` by path, under the scratch environment below
- the state tables in *Scope*, at the parent of each part and at HEAD
- the floor on both planes at HEAD, exit codes read explicitly

## House rules for this run

- **This tool touches real private data and the real operating system.** Never run
  `ccarchive`, `ccrepo` or `cctranscript` by bare name (the installed copies
  resolve to the primary checkout); run them by absolute path from your clone.
  Every probe sets `HOME`, `CCARCHIVE_DEST`, `CCARCHIVE_KEYFILE` and
  `CCARCHIVE_HISTORY` into your scratchpad and `CCARCHIVE_SCHEDULER_LOG` to a
  scratch file. Never point any mode at the principal's `~/.claude` or real
  archive, and never run a schedule flag without the seam. Never quote transcript
  content; synthetic fixtures only.
- Name your own worktree in the verdict. Run **no git command that writes** there;
  read-only git is fine. Probes and older checkouts go in a private clone under
  your scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: each suite at most once,
  foreground. Never point a scanner at another repository on the machine.
- Absolute ISO-8601 dates from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, key, placeholder token, email address or
  personal detail — the repo is public; describe and locate instead.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md beside this brief under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/` (including those whose
finding IDs the commit messages cite as answered), the queue pointer named above,
this brief's sibling (same path, `.deferred.md`), and the commissioning items
under `docs/roadmap/210-instruments-open-features/` numbered 010, 160, 170, 190,
200, 210, 230 and 240. In phase 1 judge the code at HEAD on its own terms; in
phase 2 check each cited answer against the verdict it answers.

Sweep with rule 2's default bar plus these (`<root>` is your worktree):

```sh
Q=docs/roadmap/160-doctrine-review-owed
python3 tools/coldsweep.py --root <root> \
  --also-exclude $Q/670-rule-4-cold-pass-queued-ccarchive-hardening.md \
  --also-exclude docs/reviews/2026-10-16-1550-ccarchive-hardening-cold.deferred.md \
  --also-exclude docs/roadmap/210-instruments-open-features \
  <pattern>
```

That bars the whole 210 section, wider than the list; read an unlisted 210 item
only if you need it, and say so. `--include-barred` only with disclosure.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, findings with
stable IDs (prefix `HD`: `HD1`, `HD2`, …) and severities (MAJOR / MODERATE /
minor / note), a security finding also carrying a recurrence-prevention step, an
overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger with
commands and results, and a follow-up checklist. Commit it before opening the
sibling. If an orchestrator holds the sibling outside the tree, it releases it on
your committed findings.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against its seeded questions, the intent record and the earlier
verdicts it names, any finding formed at reconcile marked as such, and the
overall line restated. Never revise phase-1 text. Fold the sibling in below the
reconcile and delete it.

The author is not the taker, so record every finding and apply nothing; counsel
on fixes is welcome, labelled as counsel.

---

# Verdict — phase 1 (2026-10-17 UTC)

## Provenance (V7)

- **Reviewer:** a fresh `claude-fable-5-1` subagent (the principal-named tier, checked at
  claim), spawned 2026-10-17 UTC by a Fable orchestrator that authored none of the delta
  and none of this brief, holds the deferred sibling outside the tree until this verdict
  is committed, and forms no finding and writes no severity. Reviewer-plus-orchestrator
  shape, disclosed here as rule 4 requires. Neither the authoring run (Sonnet and Opus
  workers under an Opus orchestrator, per the commits' co-author trailers) nor the Opus
  brief-writer started or instructed this session.
- **Worktree:** `/Users/mike/worktrees/atelier-review-1017`, branch `review-1017`, read
  at `c7039c9` and re-checked at `c394683` (the delta paths are byte-identical at both).
  No git command that writes was run there. Probes, mutations and the test suite ran in
  a private clone under this session's scratchpad, named by prefix `HD`.
- **What was read:** this brief; `docs/method/REVIEW.md` §§ *Independence* through
  *The standing checklist*; the eight delta paths in full at HEAD; the per-commit diffs
  of the delta (`git diff <parent> <commit> -- <path>`, never `git show`), the commits'
  subjects and co-author trailers only — **no commit message body was opened**; the
  `.githooks/pre-commit`, `tools/floor.py` and `.github/workflows/ci.yml` invocation
  lines; `docs/ROADMAP.md` line 368 (one hit from the cold sweep, the closed 210/190
  index line); the GitHub Actions run list for `main` (titles are other sessions' commit
  subjects — exposure to their *existence*, not their content, disclosed) and one failing
  step's log. The cold sweep ran with the three `--also-exclude` paths the brief names and
  **without** `--include-barred`. The clone's `ls` showed a sibling design file for
  encryption; it was not opened (non-goal).
- **Exposure:** the probe output printed this machine's hostname and scratch paths; none
  is reproduced here.

## Lens 1 — approach and assumptions (named first, then attacked)

1. **The adversary** is anyone or anything that can write the archive volume but not
   the operator's home: iCloud itself, another device sharing the account, a sync fault.
   Same-user processes (every Claude Code session, which reads and writes `~/.claude`)
   are trusted by construction; the key sits where they can read it. The man page says
   so (SIGNING, "an attacker who also steals the key"). *Holds, with one gap:* the
   adversary it names can **roll the index back**, and nothing detects that (HD1).
2. **One key per home, one journal and lock per destination.** The asymmetry is
   load-bearing and unstated: `--rekey` is a per-destination remedy wired to a per-home
   key (HD2).
3. **`--rekey` is "the deliberate clear", taken once the operator is satisfied.** The
   code trusts the word *deliberate* and never checks what it clears; the same page
   advises rolling on a cadence (HD3).
4. **The lock is per machine.** "One run at a time per archive" is true per home; two
   machines sharing one iCloud destination are not serialised, and the only way the
   `foreign` state is reached in the default layout is a hostname change (HD5).
5. **mtime is the change signal.** A rewrite that preserves the live file's mtime is
   invisible to an ordinary run until `--audit` (probed: run exit 0, audit exit 1). The
   man page documents the *older*-mtime case; the equal case is implied, not stated.
   The two-kinds check only runs on files the mtime test lets through (HD13).
6. **A dataless placeholder keeps its size and mtime**, so the stat-vouch never reads an
   evicted mirror. Everything the DATALESS section promises rests on this, and the tests
   can only simulate it. Not checkable from here; recorded as the open assumption it is
   (HD13).
7. **Two kinds fit every class.** Transcripts, subagent logs and tool-result sidecars as
   append-only; memory and `.meta.json` as living; the unknown defaults strict. The
   fit is right for what the tool knows; if Claude Code ever compacts `history.jsonl`
   the daily run turns red with an anomaly, which is noise in the safe direction, not
   loss. Fine.
8. **"Vouch for" means:** the signed index says so, and the mirror's stat agrees. A
   swap that keeps size and mtime passes an ordinary run (it is healed by the next
   append and caught by `--verify`); the design says this is the trade, and it is.

The non-goals are legitimate narrowings: encryption at rest is declared "planned, not
yet built" in DESIGN; the cctranscript prefix read and the records commit touch nothing
here.

## Lens 2 — correctness and quality

Driven in the clone, every probe under a scratch HOME, source, destination, key, history
and scheduler seam. The state table (exit codes read explicitly, plain and `--json`):

| state × mode | exit | matches § EXIT STATUS |
|---|---|---|
| fresh, idle, idle dry-run; verify; audit; restore nothing-to-do | 0 0 0 · 0 · 0 · 0 | yes |
| shrunk transcript: dry-run / run / run again / json / audit | 1 1 1 1 1 | yes (STILL DIFFERS) |
| shrunk: restore --delta / --delta --force / audit after | 1 / 0 / 0 | yes |
| same-length rewrite: run / --force / run / verify | 1 / 0 / 0 / 0 | yes; version kept |
| rewritten then grown | 1 | yes (anomaly) |
| memory note append / same-length rewrite / shrink / verify | 0 0 0 0 | yes; `-2` stamp |
| same-size rewrite with mtime preserved: run / audit | 0 / 1 | run silent (HD13) |
| unreadable source file / directory | 1 / 1 | yes, named |
| corrupt mirror: verify / audit / restore / run / run, live grown | 1 0 1 1 0 | yes; set aside |
| restore, mirror misses its hash, without and with --force | 1 / 1 | yes, force refused |
| symlink at mirror path / at a directory / at dest root | 0 / 1 / 0 | yes; nothing outside |
| stale temps (live pid, dead pid) | 0 | dead removed; live kept |
| hard kill after mirror 2, verify, next run, verify | KILL 1 0 0 | REPAIRED; lock cleared |
| thrown death after mirror 1, next run | 2 / 0 | catch-path save held |
| journal replay: intact entry / planted mirror it matches | 0 / 0 | no-op / adopted (needs key) |
| planted mirror, no entry, no live / identical to live | 1 / 0 | set aside / ADOPTED |
| legacy entry; budget 0, -5, abc, huge | 0 0 0 0 0 | yes |
| lock held by a live pid: run / rekey / verify / clear / status | 2 2 0 2 0 | yes |
| reused pid / unreadable lock | 0 / 0 | cleared, said so |
| evicted (seam): stat agrees, live grew / verify / audit / stat differs | 0 0 0 1 | yes |
| source dirs named `_versions`, `_untrusted` | 1 | NOT WRITTEN, reserved |
| dest in a git work tree: run / json / restore | 1 1 1 | yes; json silent (HD12) |
| manifest edited one byte: run / dry-run / restore / verify / audit | 2 2 2 1 1 | yes |
| unsigned; no key with manifest; no key verify | 2 / 2 / 1 | yes |
| no key: --rekey over the edited manifest; run; verify after | 0 / 0 / 0 | **laundered** (HD3) |
| two destinations, --rekey on A: verify B / run B / audit B | 1 / 2 / 1 | **B refused** (HD2) |
| rollback: older pair back, b.gz kept / removed / audit / run | 1 / 0 / 0 / 0 | **silent** (HD1) |
| rollback with b since pruned (mirror kept) | 1 | set aside to `_untrusted` |
| 256 MB bomb planted unmanifested: ordinary run | 1 | 564 MB RSS (HD7) |
| `--at` 24:00, 23:60, 7:5, "", padded ×2 / 03:00 | 2 ×6 / 0 | yes |
| schedule flag + dry-run, dest, json, verify, 2nd flag, bare --at | 2 ×7 | yes; 1 seam call |
| re-install over an agent, bootstrap fails | 2 | old agent gone (HD6) |

Every claim re-driven held except those marked. `--help` by path under the scratch
environment: exit 0, 22 lines, points at the man page. `--bogus --json`: exit 2 with a
structured error object. Mutation sample (five of my own, each against the matching test
subset): four were caught (in-loop checkpoint removed → MC3 fails; `classifyChange`
always-append → 4 fail; foreign-lock check removed → 1 fails; restore root check removed →
1 fails); **one survived**: swapping the manifest-then-signature write order in
`saveManifestSigned` leaves the MC4 test green, because that test builds the killed state
by hand rather than driving the write (HD4).

## Lens 3 — completeness and harvest

- Man page against behaviour, section by section: SCHEDULING, INTEGRITY, KEPT COPIES,
  SIGNING, TRUST, LOCK, AUDIT, DATALESS, ATOMIC WRITES, ONE BAD FILE, RESTORE, ENVIRONMENT
  (every `CCARCHIVE_*` the script reads is listed; the drift guard test pins it), FILES
  (exact, including `.sig.next`, `.orphan-`, the state files and the schedule files),
  EXIT STATUS (every exit-1 reason observed is listed) — all agree with what ran, with
  the exceptions in HD5, HD6, HD12, HD13 and HD15.
- `--help`: agrees with the man page's option set.
- `instruments/README.md`: § *ccarchive* still says it installs no schedule and refuses
  the `--install-schedule` family by name (HD9) — the one mirror site `72e0093` missed.
- `CHANGELOG.md`: the two entries match the delta; the "Run by hand" claim of the first
  is superseded by the second, correctly.
- The reserved-name list as one fact in three tools (V4): three literal copies with no
  stamp; ccrepo's gained a test, cctranscript's did not (HD11).
- BSD-only subprocess calls: `stat -f` is platform-gated; `ps -o lstart=` is valid on
  procps. CI on Ubuntu exercises every test except the real `stat -f` path and the one
  CLI schedule test skipped off darwin/linux (it runs on linux). Adequate.

## Lens 4 — security and privacy

`/security-review` discharged by grounds: it reads the session's pending diff, which is
other reviewers' drafts, not this landed delta. Read by hand against the OWASP Top 10 /
ASVS vectors for this class:

- **Injection into argv:** no shell anywhere; `execFileSync`/`spawnSync` with arrays.
  `launchctl`/`systemctl` arguments are fixed strings plus a home-derived path. `stat`
  is given paths without `--`: a destination beginning with `-` makes `stat` fail and
  eviction detection silently no-op — harmless, untidy (HD14). `ps` gets a number.
- **Path traversal:** restore keys pass `isInsideRoot`; external rels are a fixed list;
  journal rels are checked against the dest root and the reserved areas; kept keys are
  built from source-relative paths. Mutation M5 shows the restore guard is tested.
- **Symlinks:** mirror path, directory on the way, temp name and the manifest temp are
  all handled (probed: nothing written outside). The check-then-rename race needs a
  same-user attacker — outside the model.
- **Crypto:** HMAC-SHA256, 32 random bytes, constant-time compare, keyId is 12 hex of a
  hash (leaks nothing). Gaps: no freshness, so rollback passes (HD1); a pre-existing
  key with wide mode is used as-is (HD10); a key file with a non-hex byte mid-string is
  silently truncated by `Buffer.from(…, 'hex')` into a different, shorter key (HD14).
- **Test seams in the shipped tool:** all read on every run and documented as such; the
  dangerous one is the scheduler seam, which makes `--install-schedule` *report success*
  while asking no scheduler (status discloses the seam; install does not) (HD14).
- **Generated plist/unit/crontab:** XML-escaped; systemd `%`, `$`, `"` and `\` escaped;
  cron `%` escaped. A newline in a path breaks the systemd line and splits the cron line
  — self-inflicted only (HD14).
- **Output injection:** a file name carrying a newline forges lines in the plain report
  (probed: a fake "every archived transcript matches" line appeared mid-report);
  `--json` is safe (HD8).
- **Decompression bombs:** `gunzipSync` is unbounded; a planted unmanifested `.gz` is
  inflated whole by the ordinary run's adoption check (HD7).
- **Design altitude, privacy:** kept copies multiply retained transcripts, unbounded by
  design and documented ("never deletes"). Mirrors land `0644` in `0755` directories
  (umask), the same as the live files; the archive lives in iCloud Drive unencrypted,
  declared as planned-not-built in DESIGN. The schedule log appends forever and holds
  encoded project paths, not content. Nothing undeclared.

## Findings

**HD1 — MODERATE — a rolled-back index is a signed index: the stated adversary can erase
pruned history without evidence.** Probe: run 1 archives `a`; run 2 adds `b`; the older
manifest and signature pair is put back and `b.jsonl.gz` removed. `--verify` 0, `--audit`
0, the next run 0 — `b` is gone from the archive and from every report. Only sessions
whose live copy is already pruned (the ones the archive exists for) can be erased this
way; a live one is simply re-archived. With the mirror left in place the rollback is
noisy (set aside under `_untrusted/`, exit 1), but there is no mode to re-adopt from
there, so a *non-adversarial* rollback (a sync fault restoring an older pair) costs hand
recovery. The HMAC has no freshness and the journal is cleared after every clean run, so
nothing off the volume remembers which index is current. **Recurrence prevention
(counsel):** keep a signed record of the last-saved manifest's digest and a counter in the
state directory; refuse (or flag as `rolled-back`) when the volume's index predates it;
let `--rekey`, or a named flag, clear that deliberately. Document rollback as an attack
the signature alone does not cover.

**HD2 — MODERATE — one key per home, `--rekey` per destination: rolling the key for one
archive breaks every other archive signed under it.** Probe: archives A and B under the
same key verify; `--rekey` (A) → `--verify --dest B` exits 1 "signed by a different key —
an unexpected key roll, or tampering"; an ordinary run on B is refused, exit 2. The only
documented remedy is `--rekey --dest B`, which re-signs B's index **unverified** (HD3). The
man page's own EXAMPLES show a second destination, and SIGNING advises rolling on a
cadence. **Counsel:** either a key per destination (keyed like the journal and lock) or a
`--rekey` that re-signs every destination the state directory knows, verifying each under
the old key first; at minimum, name this in SIGNING § Rotation.

**HD3 — MODERATE — `--rekey` never checks the signature it replaces, so the routine roll
the page recommends launders whatever is on the volume.** Probe: a manifest edited by one
byte with the key removed (state `no-key`, unverifiable) → `--rekey` exits 0 with no
mention of the state it cleared → the next run exits 0 → `--verify` green. The same holds
with the old key present and the manifest tampered. TRUST calls `--rekey` "the one
deliberate clear, once the operator is satisfied the archive is intact"; SIGNING says to
roll "on a cadence besides". The two uses share one flag and the flag does not know which
it is (V5). **Recurrence prevention (counsel):** `--rekey` verifies under the old key
first and refuses anything but `verified` unless told to clear (a separate flag, or
`--rekey --accept-unverified`), and prints the state it cleared in both report shapes.

**HD4 — minor — the MC4 guard does not guard the write order.** The test builds the
killed state by hand ("Do exactly what saveManifestSigned does, stopping after the
manifest rename"); with the two writes swapped in `saveManifestSigned` it still passes
(mutation M3). The property at HEAD is correct; its regression guard is absent. Counsel:
drive the kill through a seam at the point between the two writes, as MC3 does.

**HD5 — minor — `foreign` is reachable only by a hostname change, and then it blocks
everything.** The lock lives under the local home, so a lock "from another host" cannot
arrive by sharing; what does arrive is this machine's own dead lock read under a changed
`os.hostname()` (macOS laptops change it with the network). Probe: a dead local lock
under another hostname → the run is refused (exit 2), `--lock-status` reports another
host, `--clear-lock` refuses and tells the operator to delete the file by hand. A
scheduled archive then stops until someone notices. LOCK's "one run at a time per
archive" is also per machine, not per archive, for a destination two machines share.
Counsel: compare a stable machine identity stored in the state directory, or let
`--clear-lock` clear a foreign lock with an explicit flag; say "per machine" in LOCK.

**HD6 — minor — a failed re-install removes the schedule that was there and reports that
nothing was installed.** Probe (seam, bootstrap pretends exit 5): the old plist is booted
out and overwritten before `launchctl bootstrap` runs; on failure the new file is removed
and the message reads "nothing was installed; the file it wrote was removed". The previous
agent is gone and the message does not say so. Counsel: keep the old plist bytes and put
them back (and bootstrap them) on failure, or say plainly that the previous schedule was
removed.

**HD7 — minor — decompression is unbounded, so the stated adversary can make every
ordinary run inflate a planted file whole.** Probe: a 255 KB `.gz` of 256 MB planted as
an unmanifested mirror → the ordinary run's adoption check inflates it entirely (peak RSS
564 MB) before setting it aside. Linear in the expansion; a few MB of gzip is an
out-of-memory kill, and an OOM is not a thrown error, so the catch-path save does not
run (the journal repairs the index next time, but the run never completes while the file
sits there). `--verify` and `--restore` read only manifested entries, so they are exposed
only to what the key can sign. **Recurrence prevention (counsel):** pass
`maxOutputLength` to every `gunzipSync` — the signed entry's `rawBytes` plus one where an
entry exists (a longer stream is a mismatch by definition), a fixed ceiling otherwise —
and classify the overflow as `corrupt`.

**HD8 — minor — a file name can forge lines in the plain report.** Probe: a source file
whose name carries a newline and a fake "every archived transcript matches its recorded
sha256." line produced exactly that line, twice, in the middle of an anomaly report (exit
1). `--json` escapes it. The names come from the live store (encoded working-directory
paths and Claude Code's own names), so the realistic source is a repository path, not an
attacker; still, the human report is the one a person reads in the schedule log.
**Recurrence prevention (counsel):** render every `rel` in the plain report through one
escaper (JSON-style for control characters) — one function, used at every print site.

**HD9 — minor — V5/V3: `instruments/README.md` § *ccarchive* still says the tool installs
no launchd agent and "refuses the old `--install-schedule` family of flags by name"
(lines 524–526), while line 128 of the same file, `--help`, the man page and the CHANGELOG
say it installs a calendar schedule when asked.** `72e0093` swept the man page and
CHANGELOG but not this bullet.

**HD10 — minor — a pre-existing key file with wide permissions is used as-is.** Probe: a
key written `0644` before the first run → the run signs with it and leaves it `0644`;
`mintKey` enforces `0600` only on the key it mints. A key the operator copied in by hand
(the documented out-of-band path) keeps whatever mode the copy gave it. **Recurrence
prevention (counsel):** `loadKey` refuses, or chmods and says so, when the mode is wider
than `0600`, and validates the hex strictly (HD14).

**HD11 — minor — V4: the reserved-area list is three unstamped literal copies, and the
cctranscript copy landed without a test.** `ccarchive` (`RESERVED_DIRS` plus
`EXTERNAL_PREFIX`), `ccrepo` line 865 and `cctranscript` line 361 each spell the four names
out; `ccrepo.test.js` gained a test in the delta; `cctranscript.test.js` has none for
`_anomalies`/`_versions` (grep: no hit). A fifth reserved name added to ccarchive reaches
the other two only by someone remembering. Counsel: export the list from ccarchive and
stamp the two copies, or add the missing cctranscript test now and a cross-tool drift
guard.

**HD12 — note — `--json` prints nothing on stdout for the two early exit-1 refusals**
(a destination inside a git work tree; the layout-drift alarm). A machine caller gets
exit 1 and an empty document; every other failure shape yields an object. Counsel: emit
`{"error": …}` on stdout under `--json` for these two as `reportFatal` does.

**HD13 — note — two assumptions the record should carry.** (a) A rewrite that preserves
the live file's mtime is invisible to an ordinary run (probe: run 0, audit 1); INTEGRITY
documents the older-mtime case only. (b) The stat-vouch of an evicted mirror assumes a
dataless placeholder keeps its size and mtime; the tests simulate eviction, and the one
real observation recorded is of the `SF_DATALESS` bit, not of `st_size`/`st_mtime`. If
(b) is false, every evicted mirror reads as unvouched and any growth behind it goes NOT
ARCHIVED. Counsel: state (a) in INTEGRITY; verify (b) once against a real evicted file and
record the observation beside the existing one.

**HD14 — note — small hygiene items, each probed.** `stat` is called without `--` (a
destination named `-L` makes it fail silently and eviction detection no-op). A key file
with a non-hex pair mid-string is truncated by `Buffer.from(…, 'hex')` into a shorter key
(probe: a 5-pair string gave 2 bytes) and reads as `key-mismatch`, blaming tampering. A
newline in a home or script path breaks the systemd `ExecStart` line and splits the
crontab line into two. With `CCARCHIVE_SCHEDULER_LOG` set outside a test,
`--install-schedule` writes the plist and reports "Scheduled" while asking no scheduler;
only `--schedule-status` discloses the seam. The fatal line for a bad key reads
"ccarchive: ccarchive: …" (double prefix).

**HD15 — note — the plain report's version line misnames a forced transcript.** After
`--force` on an anomaly the report says "1 version kept: living documents (memory notes,
subagent metadata) that changed other than by appending"; the version kept is of a
transcript the operator forced. KEPT COPIES states both cases; the line states one.

**HD16 — note — CI plane, for the ledger.** The delta's landing merge `eade807` never got
a completed run (cancelled by the next push, cancel-in-progress); the first completed run
after it on `main` was green on 2026-10-05 (`68e9baf`). `main` was red on 2026-10-17 at
the *man page lint* step on a page outside this delta (`ccmail.1`, a mandoc 1.14.6 STYLE
line-length warning that the local mandoc does not raise); `ccarchive.1` lints clean on
both.

## Standing checklist (V1–V7)

- **V1** — the record's claims held under re-run except where findings say otherwise:
  "tamper-evident" is true for edits and false for rollback (HD1); "one run at a time
  per archive" is per machine (HD5); the MC4 claim is true but unguarded (HD4).
- **V2** — every live-proven claim in scope re-run: suite, floor (hook plane), man lint
  and render, `--help`, the state table, the seams, the mutations. CI plane read from the
  run list (HD16).
- **V3** — the schedule's return was swept to the man page and CHANGELOG, not to the README
  bullet (HD9); the reserved-name change was swept to ccrepo with a test and to
  cctranscript without one (HD11).
- **V4** — the reserved-name list has three homes (HD11); the kind table has one home with
  a stated copy and a drift guard — fine.
- **V5** — `--rekey` as deliberate clear versus `--rekey` on a cadence (HD3); README
  against itself (HD9); report wording against KEPT COPIES (HD15).
- **V6** — run, by hand, against the catalogue; `/security-review` discharged by grounds
  (lens 4).
- **V7** — stated in the brief and repeated above.

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 8 minor · 5 note.**

The archive is never lost or silently overwritten on any state the run can meet from the
live side, and every refusal, set-aside and repair the record claims reproduced. The
three MODERATEs are all in the trust model's edges — what the signature does not cover
(rollback), and what `--rekey` does without checking (two destinations; a routine roll
over an unverified index) — and each is the principal's to decide under rule 3.

## Re-run ledger

| command (from the clone unless noted) | result |
|---|---|
| `nice -n 10 node --test instruments/ccarchive.test.js` (once) | 223 pass, 0 fail, exit 0, 122 s |
| `node --test --test-name-pattern <subset>` × 5 mutations | 4 caught, 1 survived (HD4) |
| `mandoc -T lint instruments/man/ccarchive.1` (worktree) | exit 0, no output |
| `man -P cat instruments/man/ccarchive.1` (worktree) | exit 0, 1,135 lines |
| `instruments/ccarchive --help` by path, scratch env | exit 0 |
| `tools/floor.py --plane hook --root <worktree> --tools …` | exit 0; 11 enforced, 4 warn-only |
| CI plane: `gh run list --branch main` + one failed-step log | see HD16 |
| `tools/coldsweep.py --root . --also-exclude ×3 '<pattern>'` | 37 hits / 614 files; 423 barred |
| `probe.js` (state table, P1–P12) and `probe2.js` | logs under the HD scratchpad |
| `ccrepo.test.js`, `cctranscript.test.js`, the Python suite | **not run** (load rule); follow-up |

## Follow-up checklist

- [ ] HD1–HD3: the principal rules; counsel is labelled above.
- [ ] HD4: a seam-driven kill between the two writes of `saveManifestSigned`.
- [ ] HD5, HD6, HD7, HD8, HD10, HD12, HD14, HD15: ordinary code fixes, each one commit.
- [ ] HD9, HD11: README sweep; cctranscript test; stamp or export the reserved list.
- [ ] HD13(b): one observation of `st_size`/`st_mtime` on a real evicted mirror, recorded
      beside the `SF_DATALESS` note.
- [ ] HD16: the `ccmail.1` line-length warning is another item's; this pass only notes it.
- [ ] Run `node --test instruments/*.test.js` once in a quiet window (not run here).

### Reconcile

Phase 1 was committed as `18a6aed` before any surface below was opened. Opened at
reconcile, reads only (the orchestrator's load rule: no suite, no scanner, no probe):
the sibling's text as relayed; the queue pointer; both intent records; the two verdicts
whose IDs the commits cite (`HL`, `MC`), in full for their findings and reconcile
sections; the five landing commits' message bodies; the ADR 0006 verdict's launchd
lines; the `210` items' file names and the charter's encryption lines. Nothing in
phase 1 is revised; where a seed changed my reading, it says so here.

**Seeded questions.**

1. *One destination, two machines.* Confirmed from the code, not probed: the lock and
   journal are keyed by the destination's real path but live under the running home, so
   machine B is never excluded by A's lock, and B cannot read A's journal. A mirror A
   wrote and had not yet indexed is, to B, a mirror with no entry: adopted only if B's
   live copy is byte-identical, otherwise set aside under `_untrusted/` with exit 1 —
   and A's next run then finds its journalled mirror gone (ENOENT: "the write never
   landed") and re-archives from its live copy, so nothing is lost but B's report stays
   red until the set-aside copy is removed by hand. **HD5, extended at reconcile:** the
   lock section's "one run at a time per archive" is per machine, and a shared
   destination needs either a destination-side lock or a stated "one machine writes"
   rule. No change of severity.
2. *Rollback.* HD1, formed before the seed was read; the seed names the same three
   sources (sync conflict, backup restore, destination write). Nothing binds freshness.
3. *Legacy trust.* The catch-up converges (probed: budget 0, negative, junk, huge all
   progress) and each entry is hashed once; the weakness the seed names is real but
   bounded and documented. One residue the intent record adds: the 44 entries a one-off
   script wrote on 2026-10-05 outside the tool carry an `adoptedBy` mark; whether they
   carry the mirror stat fields is not visible from here — if not, they are legacy entries
   the catch-up will read once. Evicted legacy mirrors are never read by the catch-up and
   stay "trusted as signed" for as long as they are evicted, by design.
4. *Platform.* Answered in lenses 3 and 4: `stat -f` is behind a darwin gate, so GNU
   `stat` is never called; `ps -o lstart=` is a procps form; the Ubuntu CI run reaches
   the lock tests (process identity) and the seam-driven dataless tests, and skips only
   the real `SF_DATALESS` path. The missing `--` is HD14.
5. *Seams.* HD14 and ENVIRONMENT: a stale `CCARCHIVE_SCHEDULER_LOG` makes
   `--install-schedule` report "Scheduled" having asked no scheduler; `CCARCHIVE_TEST_FAIL_AFTER`
   kills every run (the page says so). A scheduled run does not inherit the shell, so
   the reach is a hand run, as MC7's note in the `MC` verdict already judged.
6. *Uninstall reach.* It removes one fixed path, `~/Library/LaunchAgents/` under the
   tool's own label, and classes it login-style by the presence of `RunAtLoad`,
   `StartInterval` or `KeepAlive`. It cannot reach another program's file. The ADR 0006
   verdict records an earlier hand-wired plist under a different label (`nz.cxi.*`),
   verified gone on 2026-07-17; the man page's "under the same label" is right for every
   installer the tool itself shipped. No finding.
7. *Retention.* A stated choice, not an unexamined default: KEPT COPIES says nothing is
   ever deleted; DESIGN says the archive is readable by anyone who can read the
   destination and encryption is not built; `210/240` holds the charter with encryption
   pending. What no surface says is the privacy consequence of the two new areas — more
   copies of private text in a cloud folder — which lens 4 records above. Counsel only:
   one sentence in KEPT COPIES, and `210/240`'s encryption item is where the weight sits.
8. *Story drift.* HD9: the README bullet is the one surface still telling Part A's
   story; `--help`, the man page and both CHANGELOG entries (the second superseding the
   first in plain words) agree with the code.

**Cited IDs, checked against the verdict that raised each, not the commit's account.**

| ID | what the finding said | at HEAD | verdict |
|---|---|---|---|
| HL1 / MC1 | skip-path backfill recorded the source's hash | adoption rule reads the mirror; `HL11` test builds the shape | answered |
| HL2 | shrink guard read the manifest; lag, no-entry, no-length disarmed it | `classifyChange` fed only vouched entries; S5/S2c/S10 tests; probed | answered |
| HL3 | a run re-signed an unauthenticated index | `authenticateManifest`; probed exit 2 in run, dry-run, restore | answered; `--rekey` is now the one path, unchecked (HD3) |
| HL4 / MC2 | in-place mirror write | `writeFileAtomic` everywhere; probed | answered |
| HL5 | gunzip error crashed verify, restore, run | `readMirror` classifies; probed in all four modes | answered |
| HL6 | lag stranded, advice wrong | journal repair + adoption + next-step lines; probed | answered |
| HL7 | restore wrote unchecked bytes | hash check, `--force` cannot override; probed | answered |
| HL8 | one unreadable source aborted the run | named and skipped; probed file and dir | answered |
| HL9 / MC9 | mirror write followed a symlink; planted temp link | lstat + unique temp + O_EXCL; probed | answered (MC9's `0644` point unchanged, by its own terms) |
| HL10 | read-only modes moved the manifest | `onCorrupt: 'throw'` on every read-only path; test 2361 | answered |
| HL11 | regression test did not build its shape | test at line 1913 does; mutation M2 catches it | answered |
| HL12 / MC4 (page) | checkpoint overclaimed; CHANGELOG silent | SIGNING states throw vs hard kill; two entries | answered |
| HL13 / MC7 | seams undocumented | ENVIRONMENT + drift-guard test | answered |
| HL14 | overlapping runs unlocked | a lock, per machine | answered on one machine (HD5) |
| MC3 | no test fails without the checkpoint | hard-kill test; mutation M1 fails it | answered |
| MC4 (mechanism) | a kill between the two renames read as tampered | `.sig.next` swap; MC4 test | answered; the order itself is unguarded (HD4) |
| MC5 | part-way failure unstructured | top-level catch, exit 2, JSON object | answered; two exit-1 refusals still print no JSON (HD12) |
| MC6 | symlinked dest bypassed the repo guard | `realpathNearest`; test 2403 | answered |

**Uncited findings in those two verdicts:** HL15 (process: the recommendation put to the
principal is not on the record), MC8 (process: the review worktree lacked the delta) and
MC10 (checkpoint cost on a synced destination, "recorded so the trade is visible"). None
is code; MC10's trade is unchanged at HEAD (whole-manifest rewrite every 50 mirrors). The
`S2c`, `S4c` and `S5` the commits name are probe shapes from the `HL` verdict, all
covered by tests at HEAD.

**The intent record's own residue list** (five items "for that pass to weigh") against
phase 1: the older-mtime rewrite is HD13(a), which adds the equal-mtime case; the
per-state anomaly copies are documented; the pre-journal lag "set aside once" was met in
the field by the 2026-10-05 one-off adoption; a narrow race when clearing a stuck lock is
documented in the code. The fourth — *`--rekey` mints the key before it re-signs* — is
true at HEAD (`mintKey` then `signManifest`): a kill between the two leaves every
destination signed under a key that no longer exists, and the only recovery is another
`--rekey`, which re-signs unverified. **HD2 and HD3, extended at reconcile:** the residue
the authors recorded is the same mechanism, seen from the crash side. No change of
severity.

**Commit claims against the record.** The test counts the bodies give (103 → 129 → 156
→ 194) sit below HEAD's 223 because `72e0093` added the schedule tests; the "17 targeted
mutations each caught" and "14 … each caught" claims could not be re-run as stated (the
mutations are not in the record) — my five of my own choosing are the sample, with one
survivor (HD4). The 2026-10-05 whole-archive `--verify` figure in the intent record is
the record's own; nothing here contradicts it.

**Provenance, restated.** The pointer's claim shape (reviewer-plus-orchestrator, both
seats Fable, the sibling held outside the worktree and the harness scratchpad) matches
what this session experienced. The queue-run session that opened the claim is the
orchestrator named in phase 1; it authored none of the delta.

**Findings formed at reconcile:** none with a new ID. HD5 (two machines), HD2 and HD3
(the crash-side residue) are extended above without a change of severity.

**Overall line, restated: PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 8 minor · 5 note.**
Nothing applied; the findings are the principal's. Phase 2 ends here; no file but this
one edited, nothing folded or deleted (the orchestrator folds the sibling in).

## Deferred material — folded in at reconcile

# Deferred sibling — ccarchive hardening

**Held under rule 1's split** (`docs/method/REVIEW.md`). Open only after your
phase-1 findings are committed to the brief
`docs/reviews/2026-10-16-1550-ccarchive-hardening-cold.md`. At verdict, fold this
file in below your reconcile and delete it.

Written 2026-10-16 UTC by the Opus brief-writer named in the brief, which authored
none of the delta and forms no finding: the questions below are seeds, a floor
and never a fence.

## Intent record

- `docs/sessions/2026-10-04-2329-ccarchive-hardening.md` — **not opened by the
  brief-writer**. The records commit `21a772f` appended to it after the run's
  close; the widening commits `bab1451` and `72e0093` may be recorded there or in
  `docs/sessions/2026-10-05-1120-queue-run-closes-and-builds.md` (also not
  opened).

## The earlier verdicts this delta answers (named, not opened)

The commit messages cite finding IDs as answered. ID greps over `docs/reviews/`
place them in these two files; neither was opened by the brief-writer:

- `docs/reviews/2026-10-04-2215-ccarchive-heal-pulled-cold.md` — the `HL` IDs
- `docs/reviews/2026-10-03-0357-manifest-checkpoints-cold.md` — the `MC` IDs

For each cited ID, check at reconcile that the code at HEAD answers what the
finding said, not what the commit message says it said; and list any finding in
those two verdicts the series does not cite.

## Other prior verdicts naming the tool (named, not opened)

- `docs/reviews/2026-07-17-1000-adr0006-ccarchive-preserve-cold.md`
- `docs/reviews/2026-07-17-1000-cli-docs-standard-cold.md` and
  `docs/reviews/2026-07-17-1157-cli-docs-applied-cold.md`
- `docs/reviews/2026-07-17-1000-conventions-utc-at-rest-cold.md` and
  `docs/reviews/2026-07-17-1157-conventions-utc-applied-cold.md`
- `docs/reviews/2026-07-20-2040-size-rebalance-cold.md`
- `docs/reviews/2026-08-15-1032-cctranscript-search-cold.md`
- `docs/reviews/2026-08-17-1321-plain-reply-repurpose-design.md`
- `docs/reviews/2026-09-25-0715-ccmail-build-cold.md`
- `docs/reviews/2026-10-03-0357-archive-pool-speedup-cold.md`

## The pointer's own lens hints

None. The pointer is refs-only (delta, intent record, tier, pass type).

## Seeded questions

1. **One destination, two machines.** The lock and the intent journal both live
   under the running machine's home, not on the destination. If the destination
   syncs between machines, does the lock exclude the other machine at all, and
   what does machine B do with a mirror machine A wrote but has not yet indexed
   (no entry → set aside as untrusted)?
2. **Rollback.** The signature is an HMAC over the manifest bytes. Does anything
   bind freshness, so that an older, validly signed manifest-and-signature pair
   (from a sync conflict, a backup restore, or an attacker with destination
   write) is refused rather than read as `verified`?
3. **Legacy trust.** Entries written before the hardening carry no mirror stat
   and are "trusted as signed until their next write". Every archive that
   predates the change starts in that state; is the stat-vouching weakest
   exactly where the most data sits, and does the legacy budget close it?
4. **Platform.** `stat -f` and `ps -o lstart=` are BSD and macOS forms; GNU
   `stat -f` reports file-system status instead. The schedule now supports
   Linux. Does the legacy batched stat, or the lock's process identity, behave
   on Linux, and does the Ubuntu CI run reach those paths or skip them? The
   `stat` argv also passes paths with no `--` separator.
5. **Seams in the shipped tool.** `CCARCHIVE_SCHEDULER_LOG` turns every scheduler
   call into a log line, and `CCARCHIVE_SCHEDULER_EXIT` fakes its result. Can a
   variable left set in a user's shell make `--install-schedule` report success
   while installing nothing, or make a real run inject a fault?
6. **Uninstall reach.** `--uninstall-schedule` also removes "an old login-style
   plist". By what test does it decide a file is its own, and can it remove a
   file another program owns?
7. **Retention.** `_anomalies/` and `_versions/` are never deleted, hold private
   transcripts and memory notes, and the destination may be a cloud-synced
   folder with encryption at rest unbuilt. Is unbounded retention of extra copies
   a privacy design choice the man page states, or an unexamined default?
8. **Story drift.** Part A removed the installer and refused its flags by name;
   `72e0093` brought it back two hours later. Do the man page, `--help`, the
   README and both CHANGELOG entries now tell one consistent story?
