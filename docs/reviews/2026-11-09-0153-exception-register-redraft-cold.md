# Cold pass — the exception-register design, redrafted and reworked to one central file (160/650, 110/100)

**Pass type:** design cold pass, per `docs/method/REVIEW.md` rule 4 (a design every scanner and
child would build to, doctrine by function).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** PASS RAN 2026-11-16 UTC. Act 1 (verdict) and act 2 (reconcile) written by a
Fable 5.1 reviewer under the principal's 2026-11-16 drain order; sibling and review log folded
below by the orchestrator. Overall: FAIL, 1 MAJOR, 2 MODERATE, 3 minor, 5 note. Brief written
2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5 brief-writer.
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
(`2026-11-09-0153-exception-register-redraft-cold.deferred.md`, folded below the verdict
on 2026-11-16), every delta commit's message body,
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

### Reconcile

Written 2026-11-16 UTC, after act 1 was committed unrevised (`7076d6c3` on `origin/main`) and the
orchestrator released the sibling by message. Act-1 text above is untouched.

**Release message, in substance (rule 4):** act 1 committed and pushed unrevised as `7076d6c3`;
the sibling's path, a held copy outside the worktree, read-only; leave to read the barred records
the brief names; append this section only; never revise act 1; do not fold or delete the sibling;
the same house rules; run the gates before finishing; end with the restated line. No question
about the delta, no pointer to where risk lives, no request to revise a finding.

**Opened in phase 2, and only these:** the sibling (one pointer block, three questions, two held
facts, one re-run result); the queue pointer `160/1130`; the intent records `160/650` whole and
`110/100` to its part-2 design note (about 150 lines); the prior verdict
`docs/reviews/2026-10-04-2215-exception-register-design-cold.md` lenses, findings and reconcile
(lines 236–660); the two delta commits' bodies (`git log --format=%b`), plus one unrelated
neighbour the same command printed; the session index's two lines naming the register (both
2026-10); the author's ruling-round record's summary lines 20–32 and the brief-writer's record's
one line on `160/1130`; `git log -S` on `tools/floor.py` for one date. Not opened: the rest of
those records, any other verdict, the children.

#### Against the pointer's questions (the author's framing)

1. **Does the both-forms transition keep every child green?** By design, yes: T0 reads both
   forms, a legacy exemption exempts exactly what it does now, and no register file means no
   change (§ 6). The floorfleet re-run shows 22 wired children that would all meet T0 that way.
   The one condition the design states and cannot prove on paper is the T1 precondition (an
   older tool on a migrated repo); § 9 proof 5 owns it. Act 1 found no path to a red child at
   T0. What it found is at T1: ERD1's clause decides what "migrated" means for the stores and,
   on one reading, T2's "zero unmigrated" never arrives.
2. **Can the provenance record be forged cheaply?** Yes, and the ADR says so in terms (§ 3 "a
   claim, not proof"). The controls are the ones XR5 asked for — `ref`, content-hash ids,
   append-only with a CI re-check, the commit as the witness of when, `by=CHOOSE` with no
   `human` default, `unknown` for migration — and act 1 confirmed each is in the text. The
   residual is sampling, which the design names. No finding beyond act 1's lens-4 item 1.
3. **Are XR1–XR16 each closed as claimed?** Thirteen are, on the prior verdict's own words:
   XR1 (both forms, dated T2, fleet count, hook-tool precondition), XR3 (claim narrowed; the
   three reason-free exemptions the reconcile said belonged in it are named in § 1), XR5, XR7
   (canonical token, `v1`, per-scanner work priced), XR8 (the second counsel taken; my probe
   reproduced the author's), XR9, XR10 (his Q2), XR11 (his Q4, out to `115/390`), XR12 (the two
   dropped qualifiers are back in Context; unit-level markers and the four non-`allowmarker`
   scanners named), XR13 (every point, including `review-kind` and the dead-glob caveat), XR14
   (five proofs, two extended), XR15 (two sizes were put to him; he chose large; the cost is
   stated), XR16 (quoted whole). Three are closed in the main and open at one edge, and the
   edges are act 1's findings: XR2's stale pass is rule-free and CI-side as counselled, but its
   domain of entries is undefined (ERD2); XR4's `file` level got the decidable test the counsel
   asked for in `fixture` only — `generated` and `store` did not (ERD1, ERD3); XR6's lens-3
   half ("what happens to markers inside frozen records — 87 marker-shaped strings sit in
   `docs/reviews/` alone") was answered by the one clause ERD1 is about, and the population has
   grown to 269 lines since.

#### Against the brief-writer's questions

1. **Did any prior answer depend on the in-place shape the rework dropped?** One. The redraft
   kept each marker where it lived, so a frozen record needed nothing: its marker stayed, with
   or without fields. The central shape has to move the exemption out of the file, and for
   files that are never edited it reached for a directory-wide `store` class. ERD1 is the cost
   of that shape change, not of his choice: the choice was "one central file", and a per-file
   or token entry written from the frozen marker is as central as a glob. The hybrid (`ex=<id>`)
   also carried `110/010`'s orphan check for free; the central design's equivalent is the stale
   pass, which is why ERD2's definition matters more here than it would have under the redraft.
2. **Union merge: two grants that conflict, and a removal?** A removal never happens by design,
   and the probe shows why that is load-bearing (an adjacent deletion resurrects). Two grants
   for the same token from two sessions do not conflict in git: both land, both are live, and
   the design does not say which applies — in effect the larger `n` and the union of both
   `why`s. Neither the duplicate-id check (the ids differ) nor the stale pass sees it. Formed
   at reconcile: ERD11, below.
3. **Where does a child's existing marker read differently under the register during the
   both-forms period?** Nowhere, by § 6 T0's words, and nothing in the design changes the
   marker reader; the one change to how a marker reads in that period is `allowmarker.py`'s
   malformed-marker grace ending 2026-12-09, which is independent of this design. § 9 proof 1
   and proof 5 are the tests. No finding.

#### Against the author's account and the held facts

- The landing commit's body says what the ADR says, with one claim act 1 re-ran: *"a
  throwaway-repo probe confirmed union's resurrection trap, which append-only closes"* —
  reproduced (adjacent case). The author's record summarises the delta as "for him to decide"
  and claims nothing further.
- Held fact 1 (the four answers are in): confirmed by `160/650`'s record of them, which matches
  the brief's quotation and the ADR's § *Open questions*.
- Held fact 2 (the rework went against the recommendation; § 8 was written after the choice):
  consistent with the ADR's own Drafting history. It changes no finding; it is why § 8 reads as
  a priced cost rather than an argument, which is the right register.
- The sibling's re-run results at `457615cc` match mine in shape (floor exit 0; 23 rows, 1
  absent); the brief-writer did not re-derive § *What exists*, and act 1 did.

#### Per act-1 finding

- **ERD1 (MAJOR) — stands.** The prior pass raised the frozen-record question at lens 3 and
  did not number it; this is the first time it has a finding. `110/100` carries his words that
  decide it: *"if it were one string in the file then only that string should be excluded"*.
  The intent record also records that he closed `115/170` on *"balancing importance and
  priority"*, which is a reason to prefer the cheapest bound (per-file `store` entries or an
  `expect` count) over a new mechanism.
- **ERD2 (MODERATE) — stands; new.** No released surface defines a live entry.
- **ERD3 (MODERATE) — stands; new.** XR13 asked for the walk case and got it; the class cases
  were not asked for and are not answered.
- **ERD4 — re-rated at reconcile from minor to note.** `git log -S` shows `disabled` gained its
  `review-by` on 2026-11-10 (`06248fba`), the day after the delta; the sentence was true when
  written and the prior pass agreed with it at `1685fd8`. It is stale, not wrong, and the fix
  is one clause at acceptance. The act-1 text stands as written; this note is the rating.
- **ERD5 (minor) — stands; new.** `160/650` records Q2 as "points to the record holding his
  words", which does not say the record must be in the same repo; the ADR's "tracked in this
  repo" is the writer's tightening.
- **ERD6 (minor) — stands.** The prior pass's XR2 reconcile noted the hook is "the weakest
  place to hang a block"; ERD6 asks for the opposite — a cheap rule-free check there — and the
  two are compatible: check what the staged blob decides, never what matched.
- **ERD7, ERD8 (minor, note) — stand; new.**
- **ERD9 (note) — stands.** `160/650`'s own closing line records the same two readings as the
  writer's, so the record already carries them to him; this note only asks that they be put
  with the acceptance rather than left in the item.
- **ERD10 (note) — stands.**

#### Formed at reconcile

**ERD11 — note (formed at reconcile) — Two live entries for one token are silently additive.**
Two sessions may each grant the same `tok` in the same file with different `n`, `why` or `by`;
union merge lands both, the ids differ, and § 2's duplicate check and § 5's stale pass see
nothing. The wider `n` governs by accident. *Counsel:* the listing flags more than one live
entry for a (`guard`, `rule`, `path`, `tok`) key, and the CI print of added entries names an
existing live twin when one exists — the same shape leakscan already uses for a digest twin.

#### Overall, restated

**FAIL — 1 MAJOR (ERD1) · 2 MODERATE (ERD2, ERD3) · 3 minor (ERD5, ERD6, ERD7) · 5 note (ERD4
re-rated, ERD8, ERD9, ERD10, ERD11 formed at reconcile).** Eleven findings. The sixteen prior
findings are closed as claimed in thirteen cases and closed in the main with one open edge in
three (XR2, XR4, XR6), and those three edges are ERD2, ERD3 and ERD1. The MAJOR count fell from
three to one, so the cycle is converging (`REVIEW.md` § *Applying decisions to doctrine*), and
it does not yet close. Nothing applied; every finding is the principal's.

Added to the follow-up checklist:

- [ ] ERD11 — the listing and the CI print flag a live twin for one token
- [ ] ERD4 — rated note; one clause at acceptance

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-16)

The text below is the brief's held-back sibling,
`2026-11-09-0153-exception-register-redraft-cold.deferred.md`, copied verbatim. It was removed
from the review worktree before the reviewer started, held outside the tree until act 1 was
committed (`7076d6c3`), then released to the reviewer for act 2. The orchestrator forms no
finding and has not edited it; the sibling file itself is deleted in the fold commit.

# Deferred reading for `2026-11-09-0153-exception-register-redraft-cold.md`

Open only after your act-1 findings are committed (`docs/method/REVIEW.md` rule 1). Fold into the
brief below the reconcile, then delete this file. A floor, never a fence.

## The queue pointer's questions (the author's framing, verbatim)

> whether the both-forms transition really keeps every child green; whether the provenance record
can be forged cheaply; whether XR1–XR16 are each closed as claimed.

## The brief-writer's questions

1. Reworking to the central shape after a redraft: did any answer to a prior finding depend on the
in-place shape the rework dropped?
2. Union merge on an append-only file: what happens to two grants that conflict, and to a removal?
3. Where does a child's existing marker read differently under the register than under today's
reader during the both-forms period?

## What the brief-writer held back

- The pointer said the pass was best run after the four questions were answered. They now are
  (`160/650`; ADR § *Open questions for Mike*), so that condition is met.
- The rework went against the option recommended to the principal on Q1; the design's reasoning and
  the costs in § 8 were written after that choice.

## Re-run results (2026-11-09 UTC, at `457615cc`)

`floorfleet --json`: exit 0; 23 rows, 1 parent, 21 wired children, 1 absent. `floor.py --plane ci`:
exit 0. **Not run by the brief-writer:** re-deriving the figures in the ADR's § *What exists,
measured*.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

# Review log — atelier 160/1130, cold pass on the exception-register ADR redraft (ERD)

Reviewer: Fable 5.1. Orchestrators: a headless Opus 5.5 session, started by drain session
1e053526 (Opus 5.5); both off-tier, form no finding. Worktree: the review worktree for
160/1130 (repo-relative paths below). Day: 2026-11-16 UTC.

## Act 1

- 06:13 UTC `uptime`: load 3.73 4.03 4.29 (16 GB laptop, several passes). `date -u`: Mon Nov 16
  06:13:58 UTC 2026. `git status --short`: only the planned deletion of the brief's `.deferred.md`
  sibling. HEAD 97206464 (board claim).
- Read the brief `docs/reviews/2026-11-09-0153-exception-register-redraft-cold.md` lines 1–223
  whole; read `docs/method/REVIEW.md` lines 1–709 whole (rules 1–4, standing checklist V1–V7,
  verdict shape, method-record requirement).
- Did NOT read: `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any file in
  `docs/reviews/` other than the brief, the queue pointer, the intent records beyond their
  titles, any commit message body.
- `git merge-base --is-ancestor 7c2beaea HEAD` → exit 0. `git log --oneline 7c2beaea..HEAD -- <ADR>
  <README>` → three commits (dd3d60d4, e36cedcb, db8c44b7); coldsweep `--commit` on each showed
  they touch only `docs/decisions/README.md` with unrelated index lines; the ADR is unchanged
  since 7c2beaea. Subject is the ADR at HEAD (532 lines), read whole; README (50 lines) read whole.
- `python3 tools/coldsweep.py --root . --commit c687e446 --path <ADR> --path <README>` → exit 0,
  531 lines (diff + stat, no body); same for 7c2beaea → exit 0, 771 lines (230 removed, 360 added).
  Both kept in scratch, read for the ledger. Removed by the rework: the small design's `ex=<id>`
  marker-plus-entry-file shape (§ 4 of the redraft), "keep each exemption where it lives".
- Counts re-derived (V2):
  - ignore files: 9 `.<scanner>ignore` files; non-blank non-comment lines 2+8+2+1+4+1+8+2+8 = 36.
    Matches the ADR's "36 reasoned lines across 9 ignore files".
  - `.atelier-floor.json`: `scope` holds wrapscan, spellscan, pathscan = 3. Matches.
  - `nice -n 10 python3 tools/floor.py --plane ci --root .` → exit 0 (06:19 UTC, load 3.40).
    "by allow-marker" per guard: secretscan 16, leakscan 91, linkscan 4, datescan 7, spellscan 2,
    pathscan 10, indexscan 10 (= 140 over 7 guards), plus licenscan "6 declaration(s)". The ADR's
    "136 across 8 guards" was measured 2026-11-09; HEAD has moved a week. Same shape, small drift.
  - "26 exception mechanisms" comes from the part-1 audit record, barred beyond its title until
    phase 2: not re-derived in act 1.
  - markers by store (tracked files carrying `scan:allow`): docs/reviews 174 files / 269 lines
    (reviewscan 164, leakscan 21, sizescan 18, indexscan 12, namescan 8, stampscan 7); docs/sessions
    23 files / 26 lines (leakscan 12, linkscan 5, datescan 5, …); docs/roadmap 36 lines (secretscan
    3, …). Used for ERD1.
- Tool facts checked:
  - `tools/floor.py` 130–150: `disabled` carries `review-by` (warns when missing or passed) →
    the ADR's "Only the floor's `advisory` carries an expiry" is wrong (ERD4). Lines 1536–1560:
    unknown keys under `disabled.<name>` raise ConfigError → "refuses unknown keys" holds.
  - `.github/workflows/floor.yml` 85–97: both checkouts `fetch-depth: 0` → "full history" holds.
  - `docs/build/templates/workflows/floor.yml` 95: `uses: …/floor.yml@main` → children at main.
  - `commands/install-hook.md` 37–42: hook resolves tools via `hooks.atelierTools` → shared dir.
  - `tools/leakscan.py` 1308–1348: PROVENANCE_KINDS 3 kinds; `_SESSION_RX` accepts `unknown` and
    8-char ids; comment 1313–1314 says a manifest line "migrates as it is" to the held register;
    2694–2698 helper writes the full `CLAUDE_CODE_SESSION_ID`; 2826 `_staged_manifest` reads the
    manifest from the index on the hook plane; MIN_DIGEST_HEX 16, up to 64 parses.
  - `tools/secretscan.py` 1246 `_looks_binary` on the first 8192 bytes; 482 HIGH_ENTROPY_RX `{32,}`.
  - `tools/allowmarker.py` imported by 19 scanners; publishscan, signscan, harvestscan, board do not.
  - reason-free exemptions named in § 1: reviewscan `deferral` scope (reviewscan.py 194–201),
    wrapscan sibling-marker padding (wrapscan.py 120–134), sizescan retired budget token (266–270).
  - unit-level markers: reviewscan whole record (173), licenscan declaration, stampscan block,
    pointerscan pointer, sizescan header — as § What exists says.
  - `docs/method/GUARDS.md` 577–597 Who, why, when: "who and when come from version control";
    narrowed 2026-11-09 for the manifest; 314–350 Granularity (line/check/repo; rule-scoped
    narrowing); 383–400 mandate/default. `docs/method/RECORD.md` 497 § The record is public.
    `docs/decisions/2026-08-05-1233-…` exists. `docs/method/CONCURRENCY.md` 1016–1019: a subagent's
    `CLAUDE_CODE_SESSION_ID` equalled its parent's on 2026-09-25 → "shares its parent's ID" has a
    recorded basis.
  - cited board items exist by title: 115/050, 115/390, 160/650, 160/980, 160/1130, 420/020,
    020/150, 110/100, 110/110. `python3 tools/reviewscan.py --root . .` → exit 0 (8 records carry
    a review line).
  - no `.gitattributes` in the tree; no template ships one (`grep merge=union` over docs/build,
    skills, commands → nothing); Consequences lists the line as build work. No CHANGELOG entry
    names c687e446 or 7c2beaea (grep '160/650|redraft|rework|central file'); the sibling draft ADR
    2026-11-09-1334 has one (CHANGELOG 28, 217). Templates shipping markers/ignore files: none
    found under docs/build/templates (only floor.yml and instance.yaml.example match the grep).
- Union-merge probe, throwaway repo under scratch (deleted after), `merge=union` on the file:
  concurrent appends merge clean, both kept; rebase clean, both kept; deleting the FIRST line
  beside an append: deletion held (no resurrection); deleting the LAST line beside an append:
  the deleted line CAME BACK (merge and rebase) → the ADR's adjacent-hunk trap confirmed; both
  sides appending the identical line → one copy, clean; one side appending without a trailing
  newline → clean, file left without a trailing newline; without the attribute → CONFLICT (UU).
- `nice -n 10 python3 tools/floorfleet.py --root <the directory holding the main checkout and its
  sibling clones> --json` → exit 0 (06:21 UTC, load 4.21): 32 entries, 29 git repos, 22 pinned;
  23 children, state wired 22 / absent 1; counted only, none named, output kept in scratch.
- `/security-review`: NOT RUN. No code in the delta; the worktree's pending diff is this brief's
  deleted sibling, so the scanner could only read deferred material. Discharged by grounds.
- Sentence attribution (grep in the two diffs): "Only the floor's advisory…" added in c687e446;
  "covered by one `store` entry", "need only the `class`", "Stale entries **block**", "and is
  reported" added in 7c2beaea.
- Left out: the three later README commits' other hunks (not this delta); any child's content
  (counted only); the 26-mechanism figure (barred source); tests (no code in the delta).
- 06:24–06:30 UTC: Status line updated (act 1 written, act 2 pending, fold is the
  orchestrator's); verdict appended below a `---` divider (brief now 500 lines). Findings:
  ERD1 MAJOR (`store` class widening over live record stores; counts above), ERD2 MODERATE
  (live/superseded/retired undefined against the stale pass; § 2 "reported" vs § 5 "block"),
  ERD3 MODERATE (`rule` required vs class entries), ERD4 minor (`disabled` expiry), ERD5 minor
  (`ref` in-repo only), ERD6 minor (hook staleness over staged files), ERD7 minor (newline in
  multi-word count), ERD8 note (trailing newline, union edge), ERD9 note (Q1 readings for his
  ruling), ERD10 note (no CHANGELOG entry). Overall FAIL 1/2/4/3.
- Gates over the brief: `datescan` clean (1 file, 500 lines); `reviewscan` clean (deferred
  material kept out); `spellscan` and `wrapscan` scope out docs/reviews (scanned nothing);
  whole-tree `leakscan` and `secretscan` name no line of the brief; my prose lines (≥ 224,
  excluding table rows) all ≤ 100 characters; grep for common US spellings → none.
  `git status --short`: only the planned sibling deletion and the modified brief.
- Scratch: `floor-ci.txt`, `floorfleet.json/.err`, two coldsweep diffs remain under the scratch
  directory for act 2; the two probe repos were deleted. All to be removed after act 2.
- ACT 1 complete; stopped before any barred file. Waiting for the sibling's path.

## Act 2

- Release message received from the orchestrator: act 1 committed and pushed unrevised as
  7076d6c3 on origin/main; the sibling's path given (a held copy outside the worktree, read-only);
  permission to read the barred records; append `### Reconcile` only; do not fold or delete the
  sibling; same house rules; run the gates before finishing. No question about the delta, no
  pointer to risk, no request to revise.
- Read in phase 2: the held sibling (pointer block, 3 questions, 2 held facts, re-run results at
  457615cc); the queue pointer `160/1130`; intent `160/650` whole; intent `110/100` lines 1–150;
  prior verdict `docs/reviews/2026-10-04-2215-exception-register-design-cold.md` lines 236–500
  (lenses, XR1–XR14) and 538–660 (reconcile, XR15, XR16); `git log -2 --format=%b 7c2beaea`
  (the landing body plus one unrelated neighbour); `docs/SESSIONS.md` grep for the register (two
  2026-10 index lines only); author's record `docs/sessions/2026-11-08-1059-…` lines 20–32;
  brief-writer's record `docs/sessions/2026-11-09-0153-…` line 23. `git log -S
  disabled_review_by -- tools/floor.py` → 06248fba 2026-11-10: `disabled` gained `review-by`
  the day after the delta, so ERD4's sentence was true when written → re-rated to note.
- Checked the XR trace: 13 closed as claimed; XR2, XR4, XR6 closed in the main with one open
  edge each (ERD2, ERD3, ERD1). Prior lens 3 named the frozen-record question unnumbered ("87
  marker-shaped strings in docs/reviews"); now 269 lines; ERD1 is its first finding.
- Brief-writer's Q2 produced ERD11 (note, formed at reconcile): two live entries for one token
  are additive and unseen by the duplicate-id and stale checks.
- `### Reconcile` appended (release message in substance, what was opened, the seeded
  questions, per-finding notes, ERD11, restated overall). Gates over the brief: datescan clean;
  spellscan and wrapscan scope out docs/reviews (scanned nothing); reviewscan clean; whole-tree
  leakscan and secretscan name no line of the brief; reconcile prose lines ≤ 100 characters.
  `git status --short`: only the sibling deletion and the modified brief. Scratch directory
  removed (floor and floorfleet outputs, coldsweep diffs); no captures left.
- Restated overall: FAIL — 1 MAJOR, 2 MODERATE, 3 minor, 5 note (11 findings). ACT 2 complete.
