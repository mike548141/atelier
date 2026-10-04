# Cold pass — the exception-register design, before it is accepted or built

**Pass type:** design cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-04 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/650-rule-4-cold-pass-queued-exception-register-design.md`.
**Why it earns a review:** a draft ADR that would change how every guard in
every repo records an exception; reviewed now, a wrong shape costs a redraft,
and reviewed after the build it costs fourteen scanners and every child's
markers.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the commits named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-04 UTC
  with the prompt "Do all cold reviews and any other work dependent on fable",
  on the Fable tier (`claude-fable-5-1`), orchestrating four rule-4 passes (code
  and design passes from a seventeen-pointer queue; the principal sized this
  sitting to the weekly allowance he had left). It wrote this brief from the
  queue pointer, the landing commits' subjects and file lists, and the delta
  paths' names; it did not open the intent record or any prior verdict on these
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

- `0013025` (2026-10-03) — decisions: draft the exception register

Delta paths:

- `docs/decisions/2026-10-03-0641-the-exception-register.md` (draft, 114 lines)

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

This is a design review per `docs/method/REVIEW.md` § *Review the design, not
only the build*: the subject is a decision not yet taken. Whether the design
solves the problem it states, and whether that is the right problem. Read the
mechanisms it would replace or sit beside as they stand at HEAD — the inline
allow markers and their shared grammar in `tools/`, every ignore file
(`.leakscanignore` and its siblings), the floor's softening configuration, and
the deferment and allowance doctrine in `docs/method/GUARDS.md` and neighbours —
and test the draft against them: what does each existing exception become, can
every one be expressed, and what is the migration for this repo and for a child
that floats at the floor's `@main`? Whether the record's fields can all be
supplied at the moment an exception is made, by an agent and by a person, and
who checks them. Whether "narrowest unit" is decidable by a tool for text and
for binary files, and what happens when the excepted content moves, is
reformatted, or is duplicated. Whether the register can go stale, be bypassed,
or itself leak what it excuses (this repo is public; a register that quotes the
excepted string publishes it). Alternatives the draft did not weigh. What the
smallest first build would be and what it must prove. **Non-goal:** none
declared by the draft is binding on you; the principal's own words quoted in the
draft are the commission and are not under review — their interpretation is.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first,
   before reading the draft's own list if it has one. Separate what the
   principal's quoted words require from what the draft adds, and say where the
   draft narrowed, widened or re-read them.
2. **Correctness & quality.** Internal consistency and buildability: walk three
   real exceptions from this repo (one inline marker, one ignore-file glob, one
   softened guard) through the design end to end and record where each step is
   underspecified. Check every factual claim the draft makes about the current
   tools by running or reading them.
3. **Completeness / harvest.** What the draft leaves out: migration, the hook
   and CI planes, children and the template, the records and doctrine that would
   need to change, the review and ruling it needs before build, and its relation
   to open ADRs and drafts under `docs/decisions/`.
4. **Security & privacy** — mandatory. A register of exceptions is a map of
   where the guards do not look. Consider who can add to it, whether an addition
   is reviewable in a diff, whether it can be widened silently, and whether it
   discloses secrets, personal data or private repositories' names by recording
   them. `/security-review` is discharged by grounds (a prose design; no code
   delta) — say so.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- every factual claim in the draft about a tool's current behaviour: run the
  tool or read the code and record agreement or not
- count the live exceptions in this repo by mechanism (inline markers by guard,
  ignore-file lines, softened guards) so the migration's size is measured
- the floor on both planes at HEAD (the draft is a tracked file)

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
`docs/roadmap/160-doctrine-review-owed/650-rule-4-cold-pass-queued-exception-register-design.md`
(it carries the author's own lens hints), and:

- every item under `docs/roadmap/110-estate-duplication-exception-audit-mike/`
  and `docs/roadmap/115-guardrail-architecture-mike-commissioned/`
- `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md` and
  `docs/reviews/2026-08-05-1320-f1-guards-allowances-cold.md`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-1004 --also-exclude
docs/roadmap/160-doctrine-review-owed/650-rule-4-cold-pass-queued-exception-register-design.md
--also-exclude docs/roadmap/110-estate-duplication-exception-audit-mike
--also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `XR`: `XR1`, `XR2`, …) and severities (MAJOR / MODERATE
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

Findings on doctrine are the principal's to decide (rule 3): record all, apply
nothing; your counsel per finding is welcome, labelled as counsel and kept
beneath the finding.

---

# Verdict — phase 1 (written 2026-10-04 UTC, before any deferred material)

**Overall: FAIL as a design to accept as drafted — 3 MAJOR · 5 MODERATE · 4 minor · 2 note.**
The core is sound and worth keeping: required provenance fields, the three-way `granted_by`
split, and string-level narrowness. What fails is the plumbing around it: the migration, the
stale-entry rule, and the claim that every exception fits. Each needs a redraft before a ruling.

## Provenance

- **Spawned by** the brief-writer's Fable session as a subagent, with this brief as the only
  task framing. Tier: Fable (`claude-fable-5-1`). I am not the author's session and was not
  instructed by it.
- **Read:** this brief; the draft ADR; `tools/allowmarker.py`; `docs/method/GUARDS.md` in full;
  all eight scanner ignore files and `.gitignore`; `.atelier-floor.json`; `.githooks/pre-commit`;
  the head of `tools/floor.py` and its softening dataclasses; the header of `tools/pins.py`;
  `.github/workflows/floor.yml` lines 20–40; `Finding` classes in six scanners; the first 30–40
  lines of the two ADRs dated 2026-08-15 (board store) and 2026-08-05 (estate-internal context);
  the landing commit's message and stat.
- **Not opened:** `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any prior
  verdict, the queue pointer, anything under roadmap sections 110 or 115, either named review
  file, or any other brief of this batch.
- ⚠️ **Exposure, disclosed.** (1) The harness auto-loaded a cross-session memory index of
  one-line titles. Three bear on this subject: that children float at the floor's main branch,
  that G3 is held as an open pull request, and the principal's standing words on exceptions. I
  re-derived each from the tree before using it (XR1, XR11). (2) A `git ls-files` filter printed
  the *filenames* of the barred section-110 items and of both barred reviews; no content was
  read. (3) My marker count ran `git grep -c` and `-oh` tree-wide, records included. It printed
  only marker tokens and per-directory counts, never line content. (4) One `coldsweep` run for
  the token G3, with the three `--also-exclude` paths and without `--include-barred`, printed
  one-line hits from `CHANGELOG.md` and non-barred roadmap items; I used only the fact that G3
  is not built at HEAD. (5) `git status` showed another pass's brief filename; not opened.

## Lens 1 — approach and assumptions

Load-bearing assumptions, named before weighing the draft:

1. Every guard finding is a *string at a path*. (False for several guards — XR3.)
2. Every guard can say, on every run, whether an entry "matched nothing". (False on the hook
   plane and for any rule the plane does not run — XR2.)
3. A hash of the matched string is stable across scanner versions. (Not guaranteed — XR7.)
4. Narrowness is one ladder with a finest rung. (It is a partial order — XR4.)
5. A field written by the session is evidence of who granted. (It is an assertion — XR5.)
6. Children change scanners at a pin bump. (They do not — XR1.)
7. One shared append-only file suits parallel sessions. (House history says otherwise — XR8.)

**What the principal's words require:** each exception is recorded with why, who (session;
ruled or automatic), when, and anything else useful; and it is as narrow as possible, down to a
position or string, for binaries and for files of any size.

**What the draft adds beyond them:** one central file; *retiring* inline markers and ignore
files; hashes as the locator; stale entries that block; `review_by`; a helper CLI.

**Where it re-reads them:** "any exception" became "a scanner finding on file content" (XR3).
"True of binaries" became "binaries get a whole-file entry" (XR11). "Recorded so that it's
clear the exception exists" was read as "recorded in one place away from the content"; his
words do not ask for that, and the move costs the reader at the line (XR6).

## Lens 2 — correctness: three real exceptions walked through

**(a) Inline marker — the identity line in `CLAUDE.md`**, marked for two `leakscan` rules.
It becomes two entries (the draft forbids "every rule"), each a `match` hash. Gaps: the
scanner reports no column, no matched string and no finding ID today, and redacts its excerpt,
so `--match-from-finding` has nothing to consume (XR7). One of the two rules runs only where
the machine-local term list exists, so on a CI runner that entry matches nothing and, by the
draft, blocks (XR2). Provenance is unknown and awaits the draft's open question.

**(b) Ignore glob — `tools/test_leakscan.py` in `.leakscanignore`.** Probe: with the ignore
file emptied, `leakscan` reports 137 blocking findings tree-wide, 101 of them in this file.
The ladder gives two routes. `file` pins the file's hash, so each edit re-blocks and needs a
new grant; the file has 16 commits so far. `match` needs about a hundred entries with full
provenance, plus one per new fixture. The draft's criterion for `file` ("every finding-bearing
part of the file is exempt") does not say which applies (XR4). The same ignore file's worktree
glob is not a finding exemption at all; it is a walk-scope rule, and "guard and rule required,
never every rule" turns it into one entry per rule per guard (XR13).

**(c) Softened guard — `scope.wrapscan` in `.atelier-floor.json`**, a ruled narrowing with a
stated cover given up. It is a list of paths the check *does* look at. No locator level can
hold it, and the draft does not say whether it stays where it is (XR3).

**Factual claims checked** — see the re-run ledger. Agreements: 33 ignore globs; the `GUARDS.md`
wording; one mechanism with an expiry (the floor advisory); the session variable exists.
Disagreements or unverifiable: XR12.

## Lens 3 — completeness

Missing from the draft: a transition in which both forms are honoured (XR1); the hook and CI
planes (XR2); the floor's own softening keys (XR3); templates and scaffolded children, whose
content carries markers with it today (XR6); what happens to markers inside frozen records —
87 marker-shaped strings sit in `docs/reviews/` alone, and records are not rewritten; the
merge behaviour of the file (XR8); and any link to the open draft ADR of 2026-08-05 on
estate-internal context in public records, which governs exactly what this file would publish
(XR10). The doctrine rewrite is named (`GUARDS.md`, two sections); `REPO-STANDARD.md`, the
scanner help text that tells a reader to add a marker, and `commands/scan.md` are not.

## Lens 4 — security and privacy

`/security-review` is **discharged by grounds**: it reads the session's pending diff, which in
this shared worktree is other passes' drafts, and the subject is a prose design with no code
delta. Hand read:

- **Credit:** a `match` entry is tighter than a line marker against a real secret landing
  beside an excused one, because only the hashed string is excused.
- **Who can add:** anyone who can commit. No change from today.
- **Reviewable in a diff:** worse than today. A new entry shows a path and an opaque hash; the
  reviewer cannot see what was excused without running a tool (XR6).
- **Silent widening:** possible. An entry can be edited in place from `match` to `glob` and keep
  its ID, date and `principal-ruled` label (XR5).
- **Disclosure:** the hash is not secrecy for guessable strings, though the string is already
  published at the named path (XR9). Session IDs and verbatim rulings in a public file are
  unruled (XR10).

## Findings

### XR1 — MAJOR — Retiring markers breaks every child at its next CI run, not at a pin bump

The draft says "Each child migrates at its pin bump." The tree says otherwise. The child
workflow template calls atelier's floor at the main branch on purpose
(`docs/build/templates/workflows/floor.yml:92`; rationale at `.github/workflows/floor.yml:22`),
and the hook runs atelier's tools from a shared directory (`.githooks/pre-commit`). So the day
atelier's scanners stop honouring inline markers and ignore files, every child's CI and every
child's hook lose all their exceptions at once. Each child would go red on everything it has
ever excused, with no register yet written. The draft has no period in which both forms work.

*Counsel:* state the transition as part of the decision: scanners read both forms; the old
form reports as "unmigrated" without blocking; retirement is a separate, dated, ruled step
taken only when a fleet view shows zero unmigrated. Measure the blast radius first.

### XR2 — MAJOR — "Matched nothing blocks" cannot be decided on the hook plane and is wrong on CI

The draft: entries "that matched nothing (stale, which blocks…)" are printed on each run.
On the hook plane the boundary scanners read only the staged added lines (`secretscan.py`
`--staged`, line 1095 onward; `floor.py` docstring). On a normal commit almost every entry
matches nothing, so either every commit blocks or the check is skipped there. On the CI plane
`leakscan` runs without the machine-local term list, permanently and by design; the three live
entries for that rule (my run: `local-term×3`) would match nothing on every runner. The same
holds for any rule a child disables, any path outside a narrowed scope, and any guard set
advisory. "Did not match in this run" and "stale" are different facts.

*Counsel:* define stale as "the path is gone, or the hashed content is absent from the file",
checked by one whole-tree pass that reads the register and the files, not as a by-product of
each scanner's findings. Say which plane runs it, and whether it blocks or reports.

### XR3 — MAJOR — "Every exception lives there" is not true of the design as drafted

The entry shape needs a `path` and a locator from string to glob. Exceptions at HEAD that do
not fit:

- the floor's four softening keys — `advisory`, `disabled`, `scope`, `flags` — each already
  carrying a `why` (`floor.py` lines 286–345); `GUARDS.md` calls these the check level and the
  repo level, and the ladder stops below both;
- registry warn-only wiring (three checks at HEAD) and the CI plane's reduced `leakscan` cover;
- subtractions built into a scanner: my run shows `secretscan` dropping 7 items by
  public-key and published-URL rules, plus truncation and the finding cap;
- findings that are not strings: a missing review line (`reviewscan`), a file's size
  (`sizescan`), a tracked path (`publishscan`), a commit's signature (`signscan`);
- the hook bypass flag.

The draft counts 26 mechanisms and describes migration for two. It rejects ignore files with
fields on the ground of "two homes for one concept", then leaves `.atelier-floor.json` as a
second home without saying so. A reader ruling on this would believe one file answers "what is
this repo not looking at"; it would not.

*Counsel:* either add levels above glob (check, repo) and absorb the floor keys, or narrow the
claim to "every content-level exception" and name what stays elsewhere and why. Add a locator
for findings that are properties of a file rather than strings in it.

### XR4 — MODERATE — The ladder is not a ladder, so "narrowest" is not mechanically decidable

`match` excuses the string "wherever it sits in that file" — every present and future
occurrence. For a short common string (a spelling, a relative-time word, an address) that is
wider than today's line marker in one direction and narrower in another. `match`, `span` and
`line` are not ordered, so "an entry coarser than the findings it covers" has no single
answer. The `file` rule ("every finding-bearing part … is exempt") is circular as written and
differs from the principal's example ("every line in a file is secrets"). Measured: the
ignore files hide 96 `secretscan` and 137 `leakscan` blocking findings, 229 of them in three
test files that are mostly code. The draft's "33 globs… become per-string entries" is
therefore a few hundred entries, or file hashes that break on every edit.

*Counsel:* give `file` a decidable test (for example a declared fixture class with a finding
density floor), let a `match` carry an optional occurrence count so growth is reported, and
state the migration size from a measurement like this one.

### XR5 — MODERATE — Provenance is asserted by the writer; "can never mark its own choice as his" overclaims

The register is a text file. A session can write `principal-ruled` by hand, or pass any words
to `--ruling`. Nothing compares the quoted words with a record. An entry can also be edited
in place — widened, or its `why` changed — while keeping its ID, date and grant label; nothing
makes the file append-only. The session variable is real, but a subagent inherits its parent's
value (mine equals the orchestrator's), and any shell without it would be recorded as `human`,
which includes other tools and CI. So the fields record a claim, not a fact, and the weakest
point is the label that matters most.

*Counsel:* say so plainly in the decision. Cheap hardening: a `ruling_ref` naming the record
where his words sit; an ID that includes a hash of the entry's content, so an in-place edit is
visible; a check that a commit only adds or supersedes entries; `unknown`, not `human`, when
the variable is absent. Keep the commit as the independent witness of when — the draft drops
version control entirely where it could keep it as a cross-check.

### XR6 — MODERATE — The reason leaves the line, and entries do not travel with content

`GUARDS.md` requires the reason "on the line or in the file a reviewer reads". A central
register reverses that: the reader of a file sees a secret-shaped string with no explanation,
and the reviewer of a diff sees a hash with no content. Path-keyed entries also break where
markers survive: a rename, a move to an archive store, a copy between files, a cherry-pick,
and scaffolding. Eight non-record files carry marker text at HEAD, including two under
`docs/build/` and one under `skills/create-repo/`; a scaffolded child gets the content but
not the entry. The draft's rejected list covers richer markers and ignore files with fields.
It does not weigh the hybrid: keep a short inline marker that names an entry ID, with the
long fields in the register. That keeps the reason at the point of use, lets a guard detect an
orphan in either direction, and needs no hash for text files.

*Counsel:* weigh the hybrid in the Rejected section, or adopt it for text and reserve hash
locators for files that cannot hold a marker (JSON, binaries).

### XR7 — MODERATE — The hash ties every exception to a scanner's exact match text, and the plumbing is absent

A `match` hash is of "the exact matched string". That string is whatever the rule's pattern
returns. A pattern change that moves a boundary by one character voids every hash for that
rule, in every repo, at the next run. `allowmarker.py`'s own header records this class: a
shared-parsing change on 2026-08-09 silently voided nine markers in three children. Combined
with XR1 and XR2 the failure would be estate-wide and blocking. Separately, the helper's
`--match-from-finding <finding-id>` assumes finding IDs and retrievable match text. Neither
exists: no scanner has a finding ID, and the two boundary scanners redact the excerpt by
design (`Finding.excerpt` in both).

*Counsel:* hash a declared canonical token (for example the maximal non-space run around the
hit) rather than the pattern's match, version the locator scheme, and list the per-scanner
work in the decision so the build is priced.

### XR8 — MODERATE — One append-only file is the shape the house already moved away from

Every session that grants an exception appends to the tail of the same file. Two branches
doing so conflict at merge; there is no `.gitattributes` and the draft names no merge rule.
The accepted ADR of 2026-08-15 moved the board to one file per item after three recorded
incidents of sessions damaging each other's edits to a shared file. The draft does not cite
it or say why this file is different.

*Counsel:* one small file per entry under a directory, with the ID as the filename, or a
declared union merge with a duplicate-ID check.

### XR9 — minor — "The secret itself is never stored" overclaims, and the register is noise to `secretscan`

A SHA-256 of an address, a number or a name is recoverable by guessing. In practice the
string is already in the tracked file the entry names, so the hash adds little exposure; the
sentence should claim that, not secrecy. Probe: a three-entry register produced three
`secretscan` advisory findings, one per hash. At a few hundred entries the advisory tier (22
findings today) is buried. The register is JSON and cannot hold a marker, so it would need an
entry excusing itself, which the draft does not address.

### XR10 — minor — Publishing session IDs and verbatim rulings is a publication choice the draft does not make

This repo is public. The register would publish a transcript ID per entry and the principal's
words per ruled entry. `GUARDS.md` § *Fail noisy* already says the inventory of allowances is
part of the publication surface. A draft ADR of 2026-08-05 on estate-internal context in
public records is open on this exact class and is not cited. `leakscan` would still scan the
file on the hook, which limits the risk; the choice is still his to make, not a by-product.

### XR11 — minor — Binaries are given the coarsest content rung, on the strength of an unbuilt design

His words: narrowness "should be true of binaries". The draft: "For binaries, this is G3's
entry" — a whole-file hash, with an optional string for "a metadata segment". G3 is not at
HEAD (the board lists it as funded, not built), so "blocks like G3's stale entry" cites
behaviour a reader of this tree cannot check. Both boundary scanners skip a file whose first
chunk holds a NUL byte, so today nothing is found inside a binary to narrow to.

### XR12 — minor — Three of the draft's facts about the current tools do not hold as stated

- "91 live line markers, **all whole-line**": several markers are not line-scoped. `sizescan`
  reports a file-level header, `reviewscan` a record, `licenscan` a declaration, `stampscan` a
  block, `pointerscan` a pointer (each guard's own "suppressed" line). These do not map to
  `match` entries.
- The count itself: at HEAD the CI-plane floor reports 96 findings suppressed by marker across
  seven guards. That is findings, not markers, so it neither confirms nor refutes 91; the "92%
  not rule-scoped" figure I could not re-derive without the barred audit.
- "Every guard reads it through `tools/allowmarker.py`": 14 scanners import that module today.
  `publishscan`, `signscan`, `harvestscan` and the board check do not.

### XR13 — note — Small unspecified points

The index is "keyed by (guard, rule, path)" but glob entries have no single path.
`granted_by: unknown` is proposed for migration yet is not in the field's allowed values, and
a guard "refuses an entry that lacks any required field". A walk-scope exclusion such as the
nested-worktree glob (present in seven ignore files) has no rule, yet `rule` is required and
"every rule" is forbidden. `review_by` does not carry the mandate-or-default kind that
`GUARDS.md` requires of a fleet date. `pathscan` already reports the draft for naming
`tools/exception.py`, which does not exist (warn-only).

### XR14 — note — Smallest first build (counsel)

One guard, one repo, additive: `leakscan` in atelier reads a register *as well as* markers and
ignore files, for `match` and `glob` only. It must prove four things before anything is
retired: the hook plane neither blocks nor lies about staleness; a CI runner without the term
list stays green; a pattern edit does not void entries; and two worktrees granting at once
merge cleanly. A child is untouched until those hold.

## Re-run ledger

All runs 2026-10-04 UTC. Scratch clone of the worktree at `91b4d43` under the session
scratchpad, directory `XR/probe`; nothing written in the worktree but this file.

| Command (in the scratch clone unless noted) | Result |
|---|---|
| `python3 tools/floor.py --plane ci --root <clone> --tools <clone>/tools` | exit 0; all enforced checks clean; `pathscan` (warn-only) 2 findings, one on the draft |
| `python3 tools/floor.py --plane hook --root <clone> --tools <clone>/tools` | exit 0 |
| Suppressed-by-marker lines from the CI run | `secretscan` 15, `leakscan` 53, `linkscan` 4, `datescan` 7, `spellscan` 2, `pathscan` 10, `licenscan` 5 = 96 |
| Non-comment lines per ignore file (worktree, read-only) | 8+2+1+4+1+7+2+8 = 33 — agrees with the draft |
| `git grep -ohE` for marker-shaped tokens (worktree) | 377 strings tree-wide, 214 under `tools/`, 87 under `docs/reviews/` |
| `secretscan` and `leakscan` on a three-entry probe register | `secretscan` exit 0 with 3 advisory findings; `leakscan` clean |
| `secretscan --root . .` with its ignore file emptied | exit 1, 96 blocking findings; 93 in one test file |
| `leakscan --root . .` with its ignore file emptied | exit 1, 137 blocking findings; 101, 24 and 7 in three test files |
| `licenscan` with its ignore file emptied | exit 2 (not pursued; no finding rests on it) |
| Session variable in a subagent shell (worktree) | set, and equal to the orchestrator's session |
| `grep` for a finding-ID field across `tools/*.py` | none |
| `git log --format=%an` (worktree) | two spellings of one author; model named only in trailers — agrees with the draft |
| Full Python suite | not run (design review; brief permits at most once) |

Ignore files in the clone were restored after each probe; the clone is disposable.

## Follow-up checklist

- [ ] XR1 — add the both-forms transition and a measured blast radius to the decision.
- [ ] XR2 — redefine stale; name the plane that checks it and whether it blocks.
- [ ] XR3 — extend the levels or narrow the claim; say where the floor keys live.
- [ ] XR4 — decidable `file` test; occurrence count on `match`; measured migration size.
- [ ] XR5 — state that provenance is asserted; choose hardening; fix the `human` default.
- [ ] XR6 — weigh the inline-ID hybrid; cover renames, templates and frozen records.
- [ ] XR7 — canonical hashed token; locator version; price the per-scanner plumbing.
- [ ] XR8 — per-entry files or a declared merge rule.
- [ ] XR9–XR13 — wording and small specifications, with the redraft.
- [ ] XR10 — the principal's ruling on publishing session IDs and ruling text.
- [ ] XR14 — first-build scope, if the redraft is accepted.

All findings are on a draft decision and are the principal's to rule (rule 3). Nothing applied.
