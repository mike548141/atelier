# Cold pass — the exception-register design, redrafted and reworked to one central file (160/650, 110/100)

**Pass type:** design cold pass, per `docs/method/REVIEW.md` rule 4 (a design every scanner and
child would build to, doctrine by function).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** act 1 (verdict) written 2026-11-16 UTC by a Fable 5.1 reviewer under the principal's
2026-11-16 drain order; act 2 (reconcile) pending the sibling's release; the fold is the
orchestrator's. Brief written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5
brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1130-rule-4-cold-pass-queued-exception-register-redraft.md`
(barred until phase 2).
**Size:** large: a 532-line draft ADR on a failed design (16 prior findings to trace), with counts
over the child repos to re-derive; no code to run.
**Why it earns a review:** The design replaces how every guard exception in every child is recorded.
It forecloses alternatives and it is a commitment before build, the cheapest moment to catch a wrong
premise. The worst failure is a migration that turns children red, or a register that records a
grant nobody can check.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `722ac2e2`,
  2026-11-09, and the Opus worker it dispatched, which wrote both the redraft and the rework (per
  the queue pointer and `160/650`). The author queued this pass and does not take it.
- **Who wrote this brief:** session `d16dc612` (`claude-opus-5-5`), a headless brief-writer started
  on 2026-11-09 by coordinating session `74f2b8cd` (Opus 5.5). `74f2b8cd` built none of this delta
  and forms no finding; its launch prompt was the only instruction, and it carried item numbers, the
  owed-or-not test and house rules, no framing of the work. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, ran no review and used no Fable model.
  Neither was started or instructed by the author. Whoever writes a brief does not run it (the
  principal's rule), so both are barred from this pass.
- **Who reviews:** a session on Fable 5.1 that passes rule 4's criterion, started once the principal
  has approved the Fable pass. **Barred from reviewing:** session `722ac2e2` and every worker it
  dispatched; `d16dc612`; `74f2b8cd`.
- **The principal's approval of this brief:** his request, 2026-11-09, verbatim: *"Check all the
  repo's, any work that requires a fable review but does not have a brief written yet I want you to
  write those briefs then finish this session when thats all done"*. That approves the brief only;
  the Fable gate on the pass is unchanged.
- **Contact, disclosed (rule 4):** the brief-writer had no contact with `722ac2e2` or its workers.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  `skills/review-brief/SKILL.md` and `docs/method/REVIEW.md` whole; the house-form brief
  `docs/reviews/2026-11-06-2027-secretscan-exempt-private-keys-cold.md` lines 1–728, verdict
  included (another surface); the queue pointer whole; the intent records' answer and closing notes,
  by extraction; commit subjects and file lists; the delta's `CHANGELOG.md` entries; the results of
  the re-run lines; parts of the delta's own files at HEAD (outlines, constants, comments). It
  opened no commit message body of this delta, and did not open `docs/SESSIONS.md`, `docs/sessions/`
  or the prior verdict on this subject. Its harness loaded user-level and repo instruction files and
  a memory index, which hold private context this brief does not carry. Everything evaluative is in
  the sibling, by count here: a held-back sibling with one pointer block, 3 questions and 2 facts.

## The acceptance test

The principal's answers to the redraft's four questions, 2026-11-09, verbatim, each a pick from
offered options: Q1 *"Large: one central file"*; Q2 *"Yes, short ID + pointer"*; Q3 *"Mark
'unrecorded' + review date"*; Q4 *"Separate investigation"* (binary contents go to `115/390`,
outside this design). The design is a draft: the principal rules on acceptance after this pass, and
approves this pass first. The ADR's § *Open questions for Mike* says none remains, with what is left
his.

The offered option's words were written by the authoring session and put to the principal; the
quoted pick is his. Recorded as an answer, not a ruling in his words: where the delta's wording goes
past what he picked, say so. These are claims to test, not settled scope.

## What the work is

A draft ADR, no code. Two commits on `main`: `c687e446` redrafted it on the failed pass's counsel;
`7c2beaea` then reworked it to the one-central-file shape on the principal's answers. **The subject
is the ADR at HEAD.** Read both commits; the queue pointer's delta names the file at HEAD, since
the rework came after the redraft.

Commits on `main`: `c687e446`, `7c2beaea`. The landing commit is `7c2beaea`. **Check your tree has
it before reading anything:** `git merge-base --is-ancestor 7c2beaea HEAD` exits 0, and an
orchestrator merges `origin/main` into the review branch before it spawns.

Delta paths: `docs/decisions/2026-10-03-0641-the-exception-register.md`, `docs/decisions/README.md`.
Read each at HEAD and read each commit body-free, scoped to paths so board records stay barred:

```
python3 tools/coldsweep.py --root . --commit c687e446 --path docs/decisions/2026-10-03-0641-the-exception-register.md --path docs/decisions/README.md
python3 tools/coldsweep.py --root . --commit 7c2beaea --path docs/decisions/2026-10-03-0641-the-exception-register.md --path docs/decisions/README.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Commits since the delta on these paths:

```
git log --oneline 7c2beaea..HEAD -- docs/decisions/2026-10-03-0641-the-exception-register.md docs/decisions/README.md
```

At `457615cc` this printed nothing. Read anything new the same way.

**Application pass.** This delta reworks a design on the counsel of a failed pass, and the ADR's own
§ *What changed, and why* names those findings. It cannot fully honour rule 2: the delta carries
finding ids and the decisions stamped on them. Sequence (`REVIEW.md` § *Applying decisions to
doctrine*): review the work at HEAD and commit findings first; open the prior verdict after. Name
that residual exposure in the verdict.

**Claims the work makes (extracted from its own changelog entry and files, not evaluated):**

- One central file per repo, `.atelier-exceptions.jsonl`, append-only under a union merge, replaces
  the scattered notes.
- Each record names who granted it (`principal-ruled`, `principal-answer`, `agent`), the short
  session id, the date and a pointer to his words.
- Old and new forms both work from the start; the old form retires only on a later dated ruling at
  zero unmigrated, so no child goes red.
- § 8 states what the central choice costs and how each cost is paid; § 9 is the smallest first
  build.
- § *What changed, and why* answers each of the sixteen findings of the failed pass.
- `.leakscanbinaries` moves in and floor softening stays in `.atelier-floor.json`, stated as the
  writer's readings.
- § *What exists, measured* states counts over the tree and the child repos. Re-derive them
  read-only and by count (V2); the brief-writer did not.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** scanning inside binary files (`115/390`, by his answer); building any of it; ruling
on acceptance, which is the principal's.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself, first, and damage each
with a probe or confirm it by re-driving. Ask whether this is the right problem, solved at the right
altitude.
2. **Correctness & quality** — does the work do what its claims above say; honest about done versus
stubbed; any overclaim or silent scope cut, each recorded against the text that makes it.
3. **Completeness / harvest** — every surface that states the rule (V3), one home (V4), no
contradiction with sibling doctrine (V5), tests that would stay green on a broken check, what
already exists that this ignored.
4. **Security & privacy** — mandatory. A design that records who granted what, in repos some of
which are public. Enumerate the threats yourself at design altitude: who can write a record, what a
record exposes, what trusts it. No code exists, so `/security-review` has nothing to read: discharge
it in one line.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root
at `457615cc`; results are in the sibling. Read exit codes explicitly. Check `uptime` first and run
heavy lines under `nice -n 10`. Python is the `python3` on `PATH` (the tests need 3.10 or later;
`/usr/bin/python3` is 3.9 on this machine and some modules fail at import).

- the adopting child repos, read-only and by count only: `python3 tools/floorfleet.py --root <the
  directory that holds the main atelier checkout and its sibling clones> --json` to a scratch file
- `nice -n 10 python3 tools/floor.py --plane ci --root .`

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; **no live writes**. A check that
  would need a write is marked NOT RUN in the verdict, with what it would have shown.
- Probes run on scratch copies and synthetic fixtures under your scratchpad only, deleted when you
  finish. Never mutate the worktree's `tools/` or `instruments/`.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live: touch nothing outside your worktree and scratchpad.
- Read-only git only, beyond committing this one file at the end of each phase (or handing it to the
  orchestrator to commit).
- Child repos are read-only and counted, never named: quote no child's name, path or excerpt.
- One heavy process at a time; foreground, long timeout. Never run an installed tool by bare name
  from `PATH`: use the worktree's own copy.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds, never with this brief or its
  sibling dirty. Over markdown its clean pass is empty; weigh it as nothing.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, placeholder token, email address, child repo name or path.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the
deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the
reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
(`2026-11-09-0153-exception-register-redraft-cold.deferred.md`), every delta commit's message body,
the queue pointer
`docs/roadmap/160-doctrine-review-owed/1130-rule-4-cold-pass-queued-exception-register-redraft.md`,
and the intent records beyond their titles:

- `docs/roadmap/160-doctrine-review-owed/650-rule-4-cold-pass-queued-exception-register-design.md`
- `docs/roadmap/110-estate-duplication-exception-audit-mike/100-two-granularities-the-2026-08-09-audit-never-asked-about.md`

Prior verdicts on this subject, barred until your own findings are committed (rule 2; `coldsweep`
excludes `docs/reviews/` by default):
`docs/reviews/2026-10-04-2215-exception-register-design-cold.md`. The delta's docstrings, comments,
ADR text, `tools/README.md` and `CHANGELOG.md` entries carry the author's account of why; they are
the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1130-rule-4-cold-pass-queued-exception-register-redraft.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/650-rule-4-cold-pass-queued-exception-register-design.md \
  --also-exclude docs/roadmap/110-estate-duplication-exception-audit-mike/100-two-granularities-the-2026-08-09-audit-never-asked-about.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, any orchestrator, what you read, the UTC day you ran on),
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`c687e446` and `7c2beaea`: read body-free
yes/no, findings by id), findings with stable ids (prefix `ERD`: `ERD1`, `ERD2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results, children by count only) and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta commits' bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling's questions and
the author's account, any finding formed at reconcile marked as such, and the overall line restated.
Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding on this delta is the principal's to decide (rule 3): record all, apply nothing.
Counsel per finding is welcome, labelled as counsel and kept beneath it.


---

## Verdict — act 1 (2026-11-16 UTC)

### Provenance (rule 4, V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. The judgement that forms every finding below is this session's.
- **Spawn:** a headless Opus 5.5 orchestrator session, itself started by drain session `1e053526`
  (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the context partition, form no
  finding and write no severity. Neither wrote the brief or the delta. Neither `722ac2e2` nor any
  worker it dispatched, nor `d16dc612`, nor `74f2b8cd`, started or instructed this session.
- **Orchestrator direction received, in substance:** the worktree path and git discipline; the
  brief path and the order "read it in full first and follow it exactly"; the partition (the
  sibling removed from the worktree, not to be sought in history, other checkouts or scratch);
  the review-log path and what it holds; what may be written (this file and the log); live
  reads only, no writes; load limits; the floorfleet re-run line with the children's directory
  named by description only; the public-repo wording rules; the act-1 / act-2 shape and the
  closing words. It carried no question about the delta, no pointer to where risk lives and no
  request to revise a finding. Its release message will be recorded in act 2.
- **Approval:** the principal's drain order of 2026-11-16, verbatim: *"I want to use things other
  than my weekly budget to clear as many fable reviews as possible like using fable drain. I
  thought we could start by using up all the API credits I have."* and *"As always you must
  ensure that nothing harms the integrity or quality of the review process and verdicts, for
  example if the review is done by API it must be as good as running it locally"*.
- **Worktree:** the 160/1130 review worktree, HEAD `97206464` (the claim commit), with
  `7c2beaea` an ancestor (`merge-base --is-ancestor` exit 0). Read-only to me except this file.
- **What I read, in order:** this brief whole; `docs/method/REVIEW.md` whole; the ADR
  `docs/decisions/2026-10-03-0641-the-exception-register.md` at HEAD, whole; `docs/decisions/
  README.md` at HEAD; both delta commits and the three later README-only commits through
  `coldsweep --commit`, body-free; then the sibling doctrine and tools the ADR's claims rest on
  (listed in the re-run ledger). **Not read:** `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md`, any other file in `docs/reviews/`, the queue pointer, the two intent
  records beyond their titles, any commit message body, the sibling. The harness loaded user-level
  and repo instruction files and a memory index at start; nothing in them concerns this delta.
- **Exposure, disclosed:** the ADR itself names the prior pass's finding ids (XR1–XR16) and the
  decision stamped on each (its § *What changed, and why*); that is the delta and was read. I did
  not open the prior verdict. The residual exposure is the author's one-line account of each
  prior finding, which I treated as a claim to test, not as the finding.
- **Running record:** a work log of every command, file range and probe was kept as I went
  (`REVIEW.md` § *A verdict is only as trustworthy as the method behind it*); it is appended to
  this file at the fold.

### The acceptance test, applied

The four answers are answers, not rulings, and the ADR says so (Drafting history, Context's
fourth requirement). Q1 *"Large: one central file"*: the design is one register file plus
`.atelier-floor.json` kept separate, with the listing as the one view; the ADR states that as the
writer's reading (§ 1) — see ERD9, for his ruling. Q2 *"Yes, short ID + pointer"*: met (§ 3,
8-character `session`, `ref`). Q3 *"Mark 'unrecorded' + review date"*: met (§ 3, § 6). Q4
*"Separate investigation"*: met (`115/390`; Context). The ADR's § *Open questions for Mike* says
none remains; after this pass three things are his (ERD1, ERD9, acceptance itself).

### Load-bearing assumptions, named first and probed

| # | Assumption | Probe | Result |
|---|---|---|---|
| A1 | Git's union merge makes one append-only file safe for parallel sessions | throwaway repo in scratch: two appends merged and rebased; last-line deletion beside an append; identical appends; no attribute | **confirmed**: appends clean both ways; adjacent deletion resurrects (the ADR's trap, real); no attribute conflicts loudly. One edge: a side without a trailing newline merges clean and leaves none (ERD8) |
| A2 | The CI checkouts carry full history (append-only re-check; `on` vs commit date) | `.github/workflows/floor.yml` 85–97 | **confirmed**: both checkouts `fetch-depth: 0` |
| A3 | Children run the floor at `main` and hooks from a shared tools directory, so T0 reaches every child at once | template `floor.yml` 95; `commands/install-hook.md` 37–42 | **confirmed** |
| A4 | A 16-hex digest and `v1:` prefix sit under secretscan's nets | `secretscan.py` 482 (`{32,}`) | **confirmed** for `tok` and `id`; binary `digest` values up to 64 hex move in from the manifest, whose own comment says full digests buy advisories — the ADR defers that to the first build, honestly |
| A5 | The hook can read the register from the staged copy as leakscan does for the manifest | `leakscan.py` 2826 `_staged_manifest` | **confirmed** |
| A6 | `floor.py` refuses unknown keys, so the new fields cannot be written early | `floor.py` 1536–1560 | **confirmed** for `disabled`; same shape for `advisory` and `scope` |
| A7 | Staleness is decidable rule-free on every plane | § 5's list against the fields | **holds** for path, glob, `tok`, `ctx`, `id`, `supersedes`, `ref`; but which entries the pass applies to is undefined (ERD2) |
| A8 | The marker and ignore-line population can be expressed at the levels § 4 offers, as narrowly as today | counted markers by store and guard; read `store` and `fixture` classes | **damaged**: the frozen-record clause routes the largest population through an uncounted directory-wide class (ERD1); class entries have no rule grammar (ERD3) |
| A9 | A subagent shares its parent's session id | `CONCURRENCY.md` 1016–1019 | **confirmed** as recorded on 2026-09-25 |
| A10 | The ADR's measured facts are current | re-derived (re-run ledger) | 36 ignore lines / 9 files exact; 3 scope entries exact; marker-suppressed count drifted a week (140 + 6 licenscan declarations today vs 136); one fact wrong (ERD4); 26 mechanisms not re-derivable in act 1 |

### Lens 1 — approach and assumptions

Right problem, right altitude: his three requirements are stated verbatim and the fourth
(answer vs ruling) is carried into the record (`by`). The core — a required provenance triple,
a three-way grant kind plus `unrecorded`, append-only with supersession, and the token level
with a count — is sound and answers his "only that string" directly. The central-file choice is
his, and § 8 prices it honestly, which is the right shape for an answer that went against the
recommendation. Where the design is mis-built is not the register but the **migration of what
exists**: the one clause that handles frozen records sends the largest marker population through
the widest class the design has (ERD1), and the class entries' grammar is unfinished (ERD3). The
other lens-1 gap is the register's state machine: "live", "superseded" and "retired" are used but
never defined against the stale pass (ERD2).

### Lens 2 — correctness and quality (V1)

The ADR is honest about done versus stubbed: no code is claimed; § 9's five proofs are owed, not
asserted; the self-exemption question is deferred to the first build in words. Its claims against
the tree hold with one exception (ERD4). The union-merge probe it reports reproduced. One phrase
overclaims: § 2 "a line deleted on one branch beside another branch's append silently comes back"
is true for an adjacent hunk (last line deleted) and false for a distant one (first line
deleted) — harmless here because the design never deletes, and the sentence is read as the
adjacent case. Two internal statements disagree (ERD2: § 2 "reported" vs § 5 "block" for an
edited entry). No silent scope cut found: binaries' contents are named out (Q4), floor softening
is named as staying put with its reason.

### Lens 3 — completeness and harvest (V3, V4, V5)

- **V3, mirror sites.** A draft binds nothing yet; the ADR lists the surfaces to rewrite at
  acceptance (`GUARDS.md` two sections, `REPO-STANDARD.md`, scanner help text,
  `commands/scan.md`, the child templates). `GUARDS.md` § *Who, why, when* already carries the
  2026-11-09 narrowing that points at this register. The README index line matches the ADR's
  status at HEAD. No CHANGELOG entry names the delta (ERD10).
- **V4, one home.** The record vocabulary (`by`, `session`, `on`) is stated once here and
  consumed by `leakscan.py` 1308–1319 by reference to this ADR: one home, stamped copy. GUARDS'
  "who and when come from version control" is the fact this ADR replaces; until acceptance the
  two coexist with GUARDS pointing here, which is the right interim.
- **V5, cross-references, rule reached.** `GUARDS.md` § *Who may move a deferment's date* → holds
  mandate/default, reached. `RECORD.md` § *The record is public* → holds the public-record rule,
  reached. ADR `2026-08-05-1233` → exists, governs estate-internal context, reached. ADR
  `2026-08-15-0610` → the board's one-file-per-item decision, reached. `115/050`, `115/390`,
  `160/980`, `420/020`, `020/150`, `110/110` → exist by title. `floor.yml` template rationale →
  present at lines 37–46. Internal: ERD2 (two statements), ERD3 (`rule` required vs class
  entries), ERD5 (`ref` in-repo vs Rejected's "copies his words").
- **What exists that it ignored:** nothing found. `160/980`'s manifest grammar is reused, not
  re-invented; the three reason-free exemptions it names exist as described; the scanners outside
  `allowmarker.py` are the four it lists.

### Lens 4 — security and privacy (V6)

Threats at design altitude, enumerated by me:

1. **Who can write a record.** Anyone who can commit. The ADR says so (§ 3 "a claim, not
   proof") and gives checkability (one file, `ref` one step away, content-hash ids, append-only,
   CI prints what a push added). No regression against a marker, which the same hand writes today
   with less to answer for. Discharged.
2. **A record that exempts more than it says.** This is where the design is weakest: class entries
   with no count (ERD1, ERD3) exempt every finding of a guard over a path, and the ADR's own
   `fixture`/`expect` reasoning (the `115/050` near miss) says why that is unsafe in a public repo.
   Finding, not discharge.
3. **What a record exposes.** Short session ids, `ref` paths, `why` text, and digests in public
   repos. `why` is governed by `RECORD.md`'s public rule; the digest locates a string already in
   the tree (§ Consequences, "not secrecy"). Discharged with the ADR's own text.
4. **What trusts it.** The floor and the hook. An unverifiable `by=principal-ruled` is accepted as
   written; sampling is the control. Counsel below ERD1.
5. **`/security-review`:** NOT RUN. There is no code, and the session's pending diff is this
   brief's deleted sibling, so aiming the scanner would read deferred material. Weighed as nothing.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `c687e446` (redraft) | yes, `coldsweep --commit`, 531 lines | ERD4 (sentence added here) |
| `7c2beaea` (rework, the landing commit) | yes, `coldsweep --commit`, 771 lines | ERD1, ERD2, ERD3, ERD5, ERD6, ERD7, ERD8, ERD9, ERD10 |
| `db8c44b7`, `e36cedcb`, `dd3d60d4` (later, README only) | yes, body-free | none; unrelated index lines |

### Findings

**ERD1 — MAJOR. The frozen-record clause migrates the largest marker population into an
uncounted, rule-wide, directory-wide exemption, against his words.** § 6 T1: *"Frozen records
are never edited: their markers stay as text, and their store is covered by one `store` entry"*;
§ 4: `store` needs *"only the `class`"*; § 8: *"`store` entries cover archives"*. Measured at
HEAD: `docs/reviews/` holds 269 marker lines across 174 files (164 reviewscan, 21 leakscan, 18
sizescan, 12 indexscan, 8 namescan, 7 stampscan), `docs/sessions/` 26 lines (12 leakscan),
`docs/roadmap/` 36 lines (3 secretscan). Those stores are not frozen as directories: every
session writes a new file into them, this brief included. A `store` glob over any of them exempts
every finding of that guard in every file, present and future, with no count — wider than the
markers it replaces by three axes (line → tree, one rule → all rules, one finding → unbounded).
That is the widening GUARDS § *Granularity* calls a defect, the "spread" the ADR itself closes at
the token level (XR4, `n`), and the `115/050` class the `fixture` class exists to stop — in the
public repo's largest text store. His 2026-10-03 words: *"if it were one string in the file then
only that string should be excluded"*. Read the other way ("frozen" means only archives such as
`docs/reviews/withdrawn/`), the clause gives the ~330 marker lines in live stores no migration
path at all, and T2's "zero unmigrated" never arrives while they stay as text. Either reading is
a hole where the design's biggest migration sits.
*Counsel:* bound `store`: per-file entries (`level` `file`, `class` `store`, no glob) for files
frozen at migration, written by the helper from each file's own markers at token level where the
string is still there; or a glob with an `expect` count like `fixture`; or a `frozen-before=<sha>`
bound so files added after are uncovered. State whether a legacy marker left as text in a frozen
file counts as unmigrated. Of the three, per-file token entries keep his "only that string".

**ERD2 — MODERATE. "Live", "superseded" and "retired" are used but never defined, so the stale
pass as written blocks forever on every supersession.** § 2: changing an entry *"means adding a
new one with `supersedes=<old id>`"*; withdrawing adds a `retired` line; nothing is ever removed.
§ 5: an entry whose `tok` matches no span or whose `ctx` matches no line is stale, and *"Stale
entries **block**"*. A superseded `ctx` entry (the line was edited, which is why it was
superseded) matches nothing from then on; the design never says superseded or retired entries are
left out of the stale pass or out of matching. § 2 also says an edited entry *"is reported"*
while § 5 lists the same id mismatch under stale, which blocks. § 7's "live exemptions" presumes
the definition the text lacks.
*Counsel:* one paragraph in § 2: an entry is *live* unless a later entry supersedes it or retires
it; only live entries exempt, only live entries are checked for staleness; a `retired` entry still
needs its `supersedes` to resolve. Reconcile "reported" with "block".

**ERD3 — MODERATE. Class entries have no rule grammar.** § 3 makes `rule` required (*"`walk`
class excepted"*) and reserves `guard` `*` for `walk`. § 4's `generated` and `store` classes exempt
every finding in a file, and `fixture` carries `expect=<rule>:<count>[,…]` across several rules —
none of which fits one required `rule`. A builder must invent `rule` `*`, or one entry per rule
per store, and GUARDS' "within a level, scope narrows further by rule" has no expression for
these entries.
*Counsel:* define `rule` `*` for class entries, say which classes may use it, and make the
listing print it loudly; or require `expect` on every class entry so the per-rule count is the
grammar.

**ERD4 — minor. Fact: "Only the floor's `advisory` carries an expiry" (§ *What exists*).**
`floor.py` 136–150: `disabled` carries `review-by` too (warns when missing or passed). Added in
`c687e446`, carried into HEAD. One word to fix; it matters because § 3's `review-by` claims to
mirror the floor's own behaviour.

**ERD5 — minor. `ref` must be a file tracked in *this* repo, which copies his words into every
child.** § 3: *"`ref` must name a file tracked in this repo … If they are recorded nowhere in the
repo, they get recorded first."* A fleet ruling lives once, in the parent's doctrine; a child
holding a `principal-ruled` entry under it would have to copy his words in, which § Rejected
refuses for the entry (*"copies his words into a second place"*).
*Counsel:* allow a parent form, `ref=atelier:<path>` resolved at the child's pin, so one home
stays one home.

**ERD6 — minor. The hook decides nothing about staleness even for files it already holds, so in a
push-to-main house a voided `ctx` or an `n` overrun lands as a red main after publication.** § 5:
*"The hook never judges staleness from what matched, and it does not count copies, so one beyond
`n` passes the hook and blocks on CI."* Both checks are rule-free and the staged blob of each
changed file is in the hook's hands; running them over staged files only (not the tree) keeps
the hook cheap and moves the block before the push. The design's own stranded-path check already
takes that shape.

**ERD7 — minor. Multi-word counting across a line wrap is undefined.** § 4: a hit of several
words is digested *"with its inner whitespace collapsed"* and `n` counts *"whitespace-bounded
spans"*. A copy wrapped over two lines is never a hit for a line-based guard, but if the count
collapses newlines as whitespace it is a counted span, so prose reflow can push a file over `n`
and block with no finding to exempt. Say whether a newline is inner whitespace for the count
(the safe answer: no, so the count and the guard see the same spans).

**ERD8 — note. The union probe, re-run: one edge the ADR does not state.** A side that appends
without a trailing newline merges clean and leaves the file without one; the next append from a
naive writer would join two objects on a line. § 5's "new entries are well formed" would catch
the join on the hook; state that the file ends in a newline and that the helper, not the hand,
writes it. Also for the record: the resurrection trap is the adjacent-hunk case (last line
deleted beside an append); a distant deletion does not resurrect.

**ERD9 — note, for his ruling. Two readings of Q1 are the writer's, and the ADR says so.** (a)
"One central file" is realised as the register *plus* `.atelier-floor.json` kept separate, with
the listing as the one view (§ 1); (b) `.leakscanbinaries` lines move in, floor softening stays
out. Both are reasonable, both are disclosed as readings; neither is his word. Put to him with
the acceptance, not assumed.

**ERD10 — note. No CHANGELOG entry names the delta.** ADR 0002 makes the CHANGELOG the index;
the same-day draft ADR `2026-11-09-1334` has an entry (CHANGELOG lines 28, 217) and this one has
none for `c687e446` or `7c2beaea`. A reader walking the index does not find that the register's
design changed shape on 2026-11-09.

### Overall

**FAIL — 1 MAJOR, 2 MODERATE, 4 minor, 3 note.** The register itself — provenance triple, grant
kinds, append-only with supersession, token level with a count, both-forms transition, priced
costs — is sound and is the right answer to his words. The FAIL is narrow: one migration clause
(ERD1) undoes the narrowness the rest of the design buys, and two definitions a builder would have
to invent (ERD2, ERD3) sit on the path to the first build. All three are paragraphs, not a
re-think. Every finding is the principal's to decide (rule 3); nothing is applied.

### Re-run ledger

| Line | Result |
|---|---|
| `git merge-base --is-ancestor 7c2beaea HEAD` | exit 0 |
| `git log --oneline 7c2beaea..HEAD -- <ADR> <README>` | 3 commits, README-only, read body-free |
| `coldsweep --commit c687e446 / 7c2beaea --path <ADR> --path <README>` | exit 0 / 0; 531 / 771 lines |
| `nice -n 10 python3 tools/floor.py --plane ci --root .` (06:19 UTC, load 3.40) | exit 0; by marker: secretscan 16, leakscan 91, linkscan 4, datescan 7, spellscan 2, pathscan 10, indexscan 10, licenscan 6 declarations |
| `nice -n 10 python3 tools/floorfleet.py --root <the directory holding the main checkout and its sibling clones> --json` (06:21 UTC, load 4.21) | exit 0; 29 git repos, 22 pinned; 23 children: wired 22, absent 1; counted only |
| `python3 tools/reviewscan.py --root . .` | exit 0; 8 post-2026-07-21 records carry a review line |
| ignore-line count over the 9 `.<scanner>ignore` files | 36, exact |
| `scope` entries in `.atelier-floor.json` | 3, exact |
| union-merge probe (throwaway repo in scratch, deleted) | see A1 |
| `/security-review` | NOT RUN, grounds above |

### Follow-up checklist (for the principal's decision; nothing applied)

- [ ] ERD1 — bound the `store` class and name the frozen-record migration path (rule on counsel)
- [ ] ERD2 — define live / superseded / retired against matching and the stale pass
- [ ] ERD3 — a rule grammar for class entries
- [ ] ERD4 — correct the `disabled` expiry fact
- [ ] ERD5 — a parent-repo `ref` form
- [ ] ERD6 — hook-plane staleness over staged files
- [ ] ERD7 — newline as inner whitespace, decided
- [ ] ERD8 — trailing newline stated; helper writes the line
- [ ] ERD9 — Q1's two readings put to him with acceptance
- [ ] ERD10 — CHANGELOG entry for the 2026-11-09 redraft and rework
- [ ] Act 2: reconcile against the sibling, the prior verdict and the intent records
