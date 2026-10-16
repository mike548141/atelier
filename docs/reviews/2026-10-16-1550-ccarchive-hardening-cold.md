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
