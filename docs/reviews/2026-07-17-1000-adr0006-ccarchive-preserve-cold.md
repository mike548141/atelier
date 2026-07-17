# Cold review — ADR 0006 addendum: ccarchive and the *preserve* verb

**Scope:** the doctrine hunk of commit `a153a31` (2026-07-17) — the ADR 0006
addendum in `docs/decisions/0006-instruments-in-atelier.md`: the `instruments/`
layer gains a fourth verb (**preserve**) and its first *writing* instrument,
admitted under the existing purpose rule with two guards (no personal data in
code — dest runtime-derived from `$HOME`; the write target is a personal store
outside any repo). Review the whole ADR at HEAD plus the delta. The ccarchive
code, tests, and README in the same commit (and its follow-on commits — the
self-installing schedule, the sha256 manifest/`--verify`, the man page) are
tested and driven, in scope for **consistency with the addendum's doctrine
claims** (do the guards hold in the code as shipped; does the README's §8
reconciliation with `instruments/ccrepo.design.md` hold), not for a
line-by-line code review. This repo is public — the writing-instrument
boundary is a publication-safety claim, not a style point.

**Sequencing (REVIEW.md rules 1–2):** (1) read this brief **only above the
first `---` divider** (use a limited read); (2) review the ADR at HEAD plus
the delta, naming and attacking the load-bearing assumptions yourself, and
**write your attack surface durably into the verdict section of this file
first**; (3) only then open the deferred section below the divider, and the
intent record `docs/sessions/2026-07-17-0810-ccarchive-transcript-preservation.md`
(the author's account — reconcile, never anchor). Name any residual exposure
rather than denying it.

**Spawn provenance (rule 4):** this brief is written by a **non-author** — a
fresh session the principal opened and pointed at the queue ("do any review
work"); the author session (Opus, intent record above) neither started nor
instructed the taking session or this reviewer. The reviewer is a cold spawn of
the taking session. One disclosure: the ROADMAP `⏳` pointer the taking session
read carried three seed questions (reproduced in the deferred section) — a
refs-only pointer is the spec; the exposure is named, not denied. The verdict
must repeat this provenance.

**This is self-authored doctrine (by function):** all findings are the
principal's to decide (rule 3) — record counsel per finding, labelled as the
reviewer's counsel; apply nothing.

**Re-run live proofs in scope:** the commits claim the instrument suite green
(12 ccarchive tests at the delta; more since) and the floor green (247 tool
tests · scan triad · sizescan · linkscan). Re-run what falls in scope. Do
**not** run anything that writes outside the repo (no live archive runs against
the operator's transcripts; `--dry-run` and the test suite are the honest
substitutes).

**Run all three lenses** (approach & assumptions · correctness/honesty ·
completeness/harvest), deep not fast; findings get stable IDs (F1…) with
severity MAJOR/MEDIUM/LOW. Append your verdict to this file below the second
`---` divider.

---

## Deferred — seeded questions (open only after your attack surface is committed)

Carried from the author's ROADMAP pointer:

- Q1. Is "preserve" a real fourth verb, or does it fold into observe?
- Q2. Is the writing-instrument boundary (personal dest, runtime-derived) drawn
  tightly enough for a public repo?
- Q3. Does the §8 reconciliation — ccarchive subsumes ccrepo's deferred
  retention-ledger's survival rationale — hold?

---

## Verdict — cold review (Fable 5, 2026-07-17)

### Reviewer's attack surface — written before opening the deferred section or the intent record

Formed from the brief's above-divider scope, the ADR at HEAD, the `a153a31`
doctrine hunk, and the shipped instrument (code, tests, README, design §8).
Nothing below the first divider and no session record has been read yet.

- **A1 — Purpose-rule fit vs layer erosion.** Does *preserve* genuinely pass
  the purpose rule, or is the layer's membership rule eroding addendum by
  addendum? The "sub-norms are descriptive, not constitutive" move has now
  been used twice (browser-fetch, ccarchive) — is anything still constitutive
  besides "value is the teammateship", and does that still exclude anything?
- **A2 — Guard 1 (no personal data in code), tested at HEAD.** Across the
  instrument, tests, man page, and fixtures: the committed iCloud path
  constant, launchd label, log path, plist contents — does any of it carry
  personal data, and does the scan gate actually cover these files?
- **A3 — Guard 2 (write target outside any repo): guard or default?**
  `--dest`/`CCARCHIVE_DEST` can point anywhere, including inside a public
  repo. Is the ADR's word "guard" honest for what is a default plus doctrine,
  with no enforcement in code?
- **A4 — "Append-only" vs overwrite-on-newer-mtime.** The tool never
  *deletes*, but it *overwrites* an archived `.gz` whenever the source is
  newer — can a truncated/corrupted source destroy the only durable copy and
  simultaneously rewrite the manifest to bless the damage?
- **A5 — "Immune to schema drift" is not immunity to layout drift.** A moved
  or renamed source root yields a silent, permanent exit-0 no-op ("nothing to
  archive") under a schedule that keeps reporting success. Does anything
  alarm on archive staleness?
- **A6 — Integrity claims.** `--verify` doesn't fail on unmanifested files;
  `fromArchive` backfill hashes are circular (hash of the archive attests the
  archive); re-archiving replaces the manifest hash so prior snapshots leave
  no trace. Is "trust anchor" overstated beyond its own stated tamper caveat?
- **A7 — Recorded proofs reproduce?** 12 tests at the delta; suite and floor
  green (247 tool tests · scan triad · sizescan · linkscan). Re-run in scope;
  `--dry-run` only, no live archive run.
- **A8 — README §8 reconciliation.** Does the "subsumes the retention
  ledger's survival rationale" claim square with `ccrepo.design.md` §8, and is
  the open seam (observers can't read the archive) stated rather than
  papered over?
- **A9 — Zero-dep and read-only claims at the edges.** Zero-dep holds
  (node: builtins only)? The require-guard keeps import side-effect-free?
  `--install-schedule` *mutates launchd state* — an acting facet of a
  "preserve" tool; does the doctrine own it?
- **A10 — Freshness edge cases.** The 1 ms mtime tolerance; a source restored
  from backup with an *older* mtime is silently never re-archived.

### Verdict

**PASS-WITH-FINDINGS** — 0 MAJOR · 1 MEDIUM · 3 LOW.

**Spawn provenance (repeated per rule 4):** this brief was written by a
non-author — a fresh session the principal opened and pointed at the queue
("do any review work"); the author session (Opus, intent record) neither
started nor instructed the taking session or this reviewer. The reviewer is a
cold spawn of the taking session. Named exposure carried from the brief: the
ROADMAP ⏳ pointer the taking session read carried three seed questions,
reproduced in the deferred section.

**Reviewer exposure disclosure:** the brief was read only above the first
divider before the attack surface was committed (divider positions located by
line-number grep only, no content). The deferred section and the intent record
were opened only after the attack surface above was durably written. The three
seed questions were already covered by A1 (Q1), A2/A3 (Q2), and A8 (Q3) —
anchoring risk low and named. Additional live reads on the operator's machine,
all read-only and within the brief's rules: `ccarchive --dry-run` and
`--schedule-status` (the brief's named honest substitutes), plus an `ls` of
`~/Library/LaunchAgents` and `launchctl list` to reconcile the intent record's
hand-wired schedule against the shipped self-installer. Nothing was written
outside this file; no commit, no push.

### Proofs re-run (actual results, this worktree at `325011b`)

- ✅ Instrument suite: `node --test instruments/*.test.js` → **67 pass, 0 fail**
  (27 are ccarchive's at HEAD; the delta's claim of 12 verified by counting
  `git show a153a31:instruments/ccarchive.test.js` → exactly 12).
- ✅ Tool suite: `python3 -m unittest discover -s tools` → **Ran 247, OK**.
- ✅ Selftests: leakscan · secretscan · licenscan · linkscan · sizescan all
  `selftest OK`.
- ✅ Full-tree scans: secretscan clean · **leakscan clean (structural + local
  term list)** — so the instrument files are covered at full local strength,
  not just CI's structural pass · licenscan Apache-2.0 clean · linkscan clean ·
  sizescan clean.
- ✅ Live substitutes: `--dry-run` → 432 transcripts, 6 would-archive, wrote
  nothing; `--schedule-status` → `com.ccarchive.archive` plist installed and
  launchd-loaded. The intent record's hand-wired `nz.cxi.ccarchive.plist` is
  **gone** — no duplicate schedule; machine state matches the self-installer
  commit (`36ecb28`).
- ✅ Personal-data spot check: every `/Users/…` literal in code/tests/man is a
  placeholder (`/Users/x`, `/Users/a&b`); dest, plist, and log paths are
  runtime-derived. Guard 1 holds as shipped.

### Findings

**F1 · MEDIUM — "Append-only" is delete-proof, not overwrite-proof; a corrupt
source can destroy the only durable copy and re-anchor the manifest to the
damage.** The contract (ADR addendum, README, code header) is "never deletes
from the archive". True — but `run()` *overwrites* an archived `.gz` whenever
the source mtime is newer, and immediately replaces the manifest hash
(`instruments/ccarchive` lines 399–408). A truncated or corrupted live
`.jsonl` (crash, disk fault, sync accident) with a fresh mtime propagates into
the archive on the next daily run, and `--verify` then *blesses* the damage —
the exact source-side failure the instrument exists to survive. The stakes
were raised by the operator's own call recorded in the intent record: the
`cleanupPeriodDays: 3650` lever was reverted *because* "the archive alone is
the durable copy" — so after day 30 there is exactly one copy, and it is
mutable from the source side. *Reviewer's counsel:* the manifest already
records `rawBytes` — refuse (or version aside, e.g. `.jsonl.gz.prev`) any
re-archive where the new source is smaller than the recorded `rawBytes`,
absent a `--force`; sessions only ever grow, so a shrink is always suspect. At
minimum, name this exposure in the README/man the way the manifest-tamper
caveat is honestly named. Related edge, folded in rather than a separate
finding: a source restored from backup with an *older* mtime is silently never
re-archived (`shouldArchive` skips when the mirror is newer).

**F2 · LOW — Guard 2 is a default plus doctrine, not a guard in code.** The
addendum presents two "guards" with equal force, but they differ in kind:
guard 1 (no personal data in code) is *enforced* — the scan gate re-proven
above — while guard 2 (write target outside any repo) is a safe **default**
that `--dest`/`CCARCHIVE_DEST` can point anywhere, including inside a public
repo; nothing in the code refuses. For a publication-safety claim in a public
repo, the ADR's wording slightly overstates the mechanism. *Reviewer's
counsel:* either reword guard 2 as "default + operator doctrine" for honesty,
or make it a real guard cheaply — warn/refuse when the resolved dest sits
inside a git work tree, overridable by flag.

**F3 · LOW — Preservation fails silently on layout drift.** "Immune to schema
drift" (true — bytes are copied, not parsed) is not immunity to *layout*
drift: if Claude Code ever moves or renames `~/.claude/projects/`, `listJsonl`
returns empty on ENOENT, the run reports "0 transcripts" and exits 0, and the
launchd schedule keeps logging success while the archive quietly stops
growing — for a durability tool, success-shaped failure. *Reviewer's counsel:*
warn (or exit non-zero) when the source yields zero transcripts while the
manifest is non-empty; and/or teach `--verify` a staleness check (newest
`archivedAt` older than N days ⇒ warn).

**F4 · LOW — Two quiet soft spots in the integrity story.** (a) Unmanifested
archive files are reported by `--verify` but never affect the exit code, so a
file *injected* into the archive passes a scripted verify. (b) The
`fromArchive` backfill hashes a `.gz` and records that as the trust anchor —
circular (the archive attesting itself); the code comments this honestly, but
README/man present the manifest as anchoring "each transcript's raw bytes"
without noting some entries never saw the raw bytes. *Reviewer's counsel:*
count unmanifested files into the non-zero exit (or add `--strict`); surface
`fromArchive` entries distinctly in `--verify` output and note them in the man
page's INTEGRITY section.

### Seeded questions (deferred section), answered

- **Q1 — is "preserve" a real fourth verb?** Yes. Observers are pure reads
  (transform on read, keep nothing); ccarchive's value *is* the durable
  written state that outlives its source. Folding it into "observe" would
  erase exactly the property the two ADR guards exist to govern — the write.
  The verb split does real doctrinal work here. The wider pattern — the
  "descriptive, not constitutive" move now used twice — was attacked (A1) and
  holds for now: "value is the teammateship" is still doing genuine exclusion
  (the archive and the schedule are kept machine-local; the tool alone enters
  the repo), but each addendum spends more of that rule's sharpness; a fifth
  verb should trigger re-stating what the layer refuses.
- **Q2 — boundary tight enough for a public repo?** For what's *committed*,
  yes — verified, not trusted (scans re-run with the local term list; all
  path literals placeholder or runtime-derived; the archived personal data and
  the schedule live outside any repo). The residual looseness is F2: guard 2
  binds the operator, not the code.
- **Q3 — does the §8 reconciliation hold?** Yes. `ccrepo.design.md` §8 defers
  a rollup ledger whose *motivation* is survival past the ~30-day prune; a
  lossless raw mirror strictly dominates a lossy rollup for survival, so the
  ledger correctly drops to a precompute/speed concern. The README states the
  open seam honestly (observers read the live dir, not the archive; hydrate/
  `--source <archive>` unbuilt), and the intent record correctly left §8
  itself unedited to avoid a collision with the parallel session — the
  cross-pointer remains owed there, as recorded. The "~2.8× smaller" and
  "~1.2 GB/yr" figures reconcile with the intent record's first live run
  (396 MB → 143 MB over 428 transcripts ≈ 2.77×).

### What was attacked and held

A2 (guard 1 at HEAD), A7 (every recorded proof reproduced, including the
12-at-delta test count), A8 (§8 reconciliation), A9 (zero-dep holds —
`node:` builtins only; the require-guard is itself tested; the schedule's
*acting* facet is owned by the addendum's "the schedule is machine-local too"
and the plist/label/log carry no personal data), A10 (the 1 ms tolerance is
justified and documented — the intent record's bug narrative and the shipped
comment agree). The launchd label migration (`nz.cxi.*` → `com.ccarchive.*`)
was verified live: no orphaned duplicate schedule.

All findings are the principal's to decide (rule 3); counsel above is the
reviewer's, applied nowhere.

— Cold reviewer (Fable 5), 2026-07-17, worktree `fable-review` at `325011b`.
