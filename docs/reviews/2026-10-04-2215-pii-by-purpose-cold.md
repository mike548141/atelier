# Cold pass — personal data held by purpose, with recorded exceptions

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-04 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/630-rule-4-cold-pass-queued-pii-by-purpose.md`.
**Why it earns a review:** the personal-data rule of a public repository and of
the template every child is created from was re-worded from a visibility rule to
a purpose rule; a loose word here is what lets a private detail into a public
tree, in this repo and in every child that copies the template.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the commits named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-04 UTC
  with the prompt "Do all cold reviews and any other work dependent on fable",
  on the Fable tier (`claude-fable-5-1`), orchestrating six rule-4 passes (code,
  design and doctrine passes from a seventeen-pointer queue; the principal sized
  this sitting to the weekly allowance he had left). It wrote this brief from
  the queue pointer, the landing commits' subjects and file lists, and the delta
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

- `1ffefc7` (2026-10-03) — build: personal data is held for a purpose, with
  recorded exceptions

Delta paths:

- `docs/build/REPO-STANDARD.md` — the personal-data bullet
- `docs/build/templates/CLAUDE.md` — the personal-data constraint
- `docs/build/templates/CONTRIBUTING.md` — the personal-data constraint
- `CLAUDE.md` (this repo's own) — the first hard constraint

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the four statements say the same rule, and whether that rule is workable
by a session that has only the sentence in front of it. Read each at HEAD and
diff `1ffefc7`. Test the wording against cases: a public repo, a private repo, a
repo that changes visibility, a template copied into a new child before anyone
has recorded an exception, a commit message, a session record, a review verdict,
a fixture file, git history. For each, does the text say what may be written,
who decides an exception, where it is recorded, in what form, and what happens
to an exception that is found unrecorded? Whether "purpose" is defined well
enough to refuse something, or can justify anything. Whether the exceptions this
repo itself holds (the published author identity and account name) are in fact
each declared where they appear — find every occurrence and check. Whether the
rule and the enforcing guard agree: read `tools/leakscan.py`'s documented
behaviour, its ignore file and its inline markers as they stand, and say where
the text promises more than the guard enforces or the guard enforces what the
text no longer says. Whether a child reading only its stamped template gets a
rule that is complete without atelier's own files. **Non-goal:** the principal's
rule itself, which the delta quotes — its placement, the wording around it and
its consistency are the subject.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Separate the words the delta attributes to the principal from the wording the
   authoring run put around them, and say where the surrounding text narrows,
   widens or re-reads what is quoted. Ask whether a purpose rule is weaker or
   stronger than the visibility rule it replaced, for a public repo
   specifically.
2. **Correctness & quality.** Read the four passages and every sentence that
   cross-refers to them. Check the four agree term by term (who, what, where
   recorded, which exceptions). Run the case list in *Scope* and record a table.
   Check every link and anchor the passages cite resolves.
3. **Completeness / harvest.** Every other surface that states a personal-data
   rule or the old visibility framing: `docs/method/` (SECRETS, GUARDS,
   CONVENTIONS, the apex, PROPAGATION's floor region), `SECURITY.md`,
   `CONTRIBUTING.md` (this repo's own), `README.md`, the create-repo skill,
   `tools/README.md`, and the stamped floor block if the rule is part of it.
   Which still state the old rule, and is the template's stamp version or
   changelog owed a bump for children to notice?
4. **Security & privacy** — mandatory. This lens is the subject. Hunt for the
   reading of the new text under which a session could commit personal data to
   this public repository and call it compliant; check whether the delta itself,
   or the records around it, introduced any personal detail. Never quote any
   such detail in the verdict — describe and locate it. `/security-review` is
   discharged by grounds (a prose doctrine delta already landed; the pending
   diff is other passes' drafts) — say so.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- the leak guard on both planes at HEAD, and tree-wide, with exit codes read
  explicitly
- find and count every recorded personal-data exception in this repo and check
  each is declared where it appears
- the stamp and block guards over the template files (`stampscan`, `blockscan`),
  to see whether the delta kept the stamped regions in step
- the floor on both planes at HEAD

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
`docs/roadmap/160-doctrine-review-owed/630-rule-4-cold-pass-queued-pii-by-purpose.md`
(it carries the author's own lens hints), and:

- every item under `docs/roadmap/200-anti-slop-invariant-registry-promote-rec/`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-1004 --also-exclude
docs/roadmap/160-doctrine-review-owed/630-rule-4-cold-pass-queued-pii-by-purpose.md
--also-exclude docs/roadmap/200-anti-slop-invariant-registry-promote-rec
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `PI`: `PI1`, `PI2`, …) and severities (MAJOR / MODERATE
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

## Verdict — phase 1 (written 2026-10-04 UTC, before any deferred material)

**Overall: PASS-WITH-FINDINGS — 2 MAJOR / 6 MODERATE / 2 minor / 1 note.**
The delta carries the principal's words faithfully and the floor is green on both
planes. The wording the authoring run put around those words makes two claims of
fact that the tree falsifies, and for this public repository it replaces a flat
prohibition with a rule that names no decider and no test.

### Provenance

- **How spawned:** a subagent started by the batch orchestrator named in *Spawn
  provenance*, with this brief as the only framing and the finding prefix `PI`.
  Not the author's session; not started or instructed by it.
- **Tier:** Fable (`claude-fable-5-1`), as the brief names.
- **What I read:** this brief; `git show 1ffefc7` in full; the four delta
  passages at HEAD; `tools/leakscan.py` (docstring and marker comments),
  `.leakscanignore`, `.atelier-floor.json`, `.githooks/pre-commit`, the head of
  `.github/workflows/ci.yml`; `docs/roadmap/110-…/100` (the item the delta cites
  as its standard); `docs/method/GUARDS.md` §§ *Granularity* and *Who, why,
  when*; short excerpts of `README.md`, `RECORD.md`, `PRINCIPLES.md`,
  `DATA-PROTECTION.md`, `AUTONOMY.md`, the create-repo skill and
  `tools/README.md`. The four delta paths are byte-identical between `1ffefc7`
  and the HEAD I reviewed (`3eac435`; the worktree advanced from `7f8e67d`
  during the run through other passes' commits).
- ⚠️ **Exposure to barred material, disclosed.** Two routes, neither a file
  opened.
  1. My first harvest search was a plain recursive grep whose path exclusions
     did not match the tool's output form, so it printed single truncated lines
     from barred paths: `docs/SESSIONS.md`, several `docs/sessions/` files
     (including two lines of the authoring run's own session record, which say
     only that the item was settled on the principal's words and is judged by
     purpose), `docs/ROADMAP-DONE.md`, prior verdicts in `docs/reviews/`, the
     section-200 items, and one truncated lens line (line 108) of another
     2026-10-04 brief, the exception-register design pass. Every later sweep
     used `tools/coldsweep.py` with both `--also-exclude` paths.
  2. `git show 1ffefc7` necessarily displays the commit's hunks to the queue
     pointer and to the section-200 item it closed. From those I know the
     author's framing that the rule is the principal's and the placement is the
     run's, and I saw the fuller form of the quotation (used in PI10).
  No finding below rests on either exposure except PI10, which says so.
- **Not read:** the machine-local term list (probed by behaviour only), the
  queue pointer as a file, the intent record, any prior verdict, the sibling.

### Lens 1 — approach and assumptions

Load-bearing assumptions, named before reading the surrounding text:

1. That "exception" in the principal's words (a thing a repo may hold) and
   "exception" in the guard standard the delta cites (a suppression of a guard
   finding) are the same object. They are not: most personal data the tree holds
   never produces a finding to suppress (PI1).
2. That the guard's idea of personal data matches the rule's. The quoted words
   name the hosting account as PII; the guard, at full term cover, does not
   (PI1, probe E).
3. That "purpose" can refuse something. No passage defines it, names who judges
   it, or gives a failing example (PI2).
4. That a standard exists for "recorded and narrow". The cited one is an open
   board item whose own measurement says no exception in the tree meets it (PI3).
5. That a child reaches atelier's `REPO-STANDARD.md`. The template's own floor
   block is written on the opposite assumption (PI7).

**The principal's words versus the wrapper.** His words give: PII is judged by
purpose; every repo avoids it in general; exceptions exist, the account being
one; private repos hold more because the ordered work needs it and controls
protect it. The authoring run added: (a) a seven-item list of what the default
covers, three items of which (estate topology, machine-local paths, and the old
"instance data" class generally) are not PII, so the word is widened in
`REPO-STANDARD.md` and then narrowed again in the templates, which drop those
items (PI4); (b) "recorded and narrow", joined in from a separate statement of
his about guard exceptions, under "So:" as if it followed from the quotation;
(c) "each declared where it appears" and "each exception is a declared
allowance", which are claims of fact about the tree and are false (PI1);
(d) "the leak and secret scans enforce the default", which overstates the guard
(PI9).

**Weaker or stronger for a public repo?** Weaker in the text, unchanged in the
guard. The replaced hard constraint was unconditional. The new one keeps an
unconditional sentence for four categories and opens everything else to "the few
recorded exceptions a public repo needs", with no decider (PI2). For private
children it is stronger in principle (the default now binds everywhere) and
unenforced in practice (PI8, PI9).

### Lens 2 — correctness and quality

**Term-by-term agreement of the four passages.**

| Term | `REPO-STANDARD.md` | atelier `CLAUDE.md` | template `CLAUDE.md` | template `CONTRIBUTING.md` |
|---|---|---|---|---|
| Default covers | names, contacts, health, family, finance, estate topology, machine-local paths | health, family, financial, personal-estate | health, family, financial, personal-estate | addresses, contacts, health, family, business detail |
| Exception test | "held for a purpose" | "a public repo needs" | "must hold for the work it exists to do" | "the work needs" |
| Who decides | not said | not said | not said | not said |
| Recorded where | not said | "declared where it appears" | not said | not said ("never an unremarked line") |
| Form of record | why, who, when, narrowest span, by citation | not said | "declared, narrow, recorded" | "declared, recorded" (no "narrow") |
| Which exceptions | open ("such as" author identity) | closed (author identity, account name) | none named | none named |
| Unrecorded one found | not said | not said | not said | not said |
| Guard named | leak and secret scans, as hooks | none | in an HTML comment only | none |

No two columns give the same list of what the default covers.

**The case list.**

| Case | What the text gives | Gap |
|---|---|---|
| Public repo (atelier) | closed list of two exceptions, each "declared where it appears" | the claim is false as measured (PI1); the route in PI2 |
| Private repo | "more exceptions", because the work needs them | no decider, no register, no form a session can follow (PI3) |
| Repo that changes visibility | nothing | the replaced rule's forward-looking clause is gone (PI8) |
| Fresh child from the template | a pointer to an atelier file | incomplete without atelier (PI7) |
| Commit message | nothing | cannot carry a marker; the staged scan reads content, not the message (PI3) |
| Session record | nothing in the delta; `RECORD.md` covers private-repo posture only | same marker-only mechanism as any file |
| Review verdict | nothing | same |
| Fixture file | nothing; three test files and one template are file-level ignore entries | file-level where the cited standard asks for a span (PI3) |
| Git history | nothing | author identity on every commit, no declaration mechanism (PI1); permanence at widening (PI8) |

**Links and anchors.** `linkscan` over the four files exits 0. Two citations are
not checkable by any guard: the elided board path in `REPO-STANDARD.md` (line
182), which `pathscan` and `linkscan` both pass in silence, and the template's
"atelier `build/REPO-STANDARD.md`", which is not written in the
`<atelier-path>/docs/…` form the same template uses forty lines earlier (PI3,
PI7).

### Lens 3 — completeness and harvest

The delta changed four statements. The same claim, in its old visibility or
absolute form, is still live on at least eleven other surfaces (PI6). The
personal-data rule is not part of the stamped floor region: `stampscan` reports
the one stamped block identical at HEAD and at `1ffefc7`, and `blockscan
--against` the landing commit's parent is clean, because neither guard covers
the line that changed. So the delta kept the stamped regions in step trivially,
and nothing tells an existing child that its hand-filled constraint is now stale
(PI7). `CHANGELOG.md` carries no entry for the delta; its newest heading is dated
2026-09-20.

### Lens 4 — security and privacy

`/security-review` is **discharged by grounds**: it reads the session's pending
diff, which in this shared worktree is other passes' drafts, and this is a
landed prose delta. There is no code surface in the delta, so the OWASP read
reduces to the guard behaviour the text relies on, which I probed by hand.

- **A compliant route for personal data into this public repo exists** (PI2).
  Probes B, C and G show the guard accepts a third party's contact line and a
  keyed personal fact once a marker with any non-empty reason is on the line.
  The text does not forbid it for categories outside the four it names.
- **The delta itself introduced an identifier**: the hosting account name,
  verbatim, into the adopter-facing standard, on a line with no declaration, in
  the sentence that calls it PII (PI5). No health, family, financial or address
  detail entered through the delta or through the commit message.
- **Paraphrased personal prose passes the guard** at full cover (probe A). That
  is a known, documented residual of the scanner; what is new is doctrine text
  saying the scans "enforce the default" (PI9).

### Findings

**PI1 — MAJOR. "Each declared where it appears" is false, and the guard does not
treat as personal data what the quoted rule says is.** atelier's first hard
constraint says its exceptions are the published author identity and the account
name, "each declared where it appears"; `REPO-STANDARD.md` says "each exception
is a declared allowance". Measured over the unbarred tree at `3eac435`:

- the account name is on 27 lines in 16 files. None carries an inline
  declaration. Six of those lines sit in the two plugin manifests, which have a
  reasoned file-level ignore entry; the other 21 lines, including line 5 of
  `CLAUDE.md` itself, both workflow files and the new `REPO-STANDARD.md` line,
  are declared nowhere;
- the author's first name is on 818 lines, none declared;
- the full name is on 4 lines (1 marked, 3 in the manifests) and the author
  address on 2 (1 marked, 1 in a file-level ignore entry);
- the author identity is in the header of every commit, where no marker can
  live. A decision record accepts that knowingly, which is a record, though not
  one "where it appears".

Tree-wide `leakscan --require-terms` exits 0 with exactly three `local-term`
suppressions. Probes E and F show the account name and the first name each pass
the guard at full term cover with no marker. So the guard and the rule disagree
about what an exception is: the principal's own example of PII produces no
finding, hence no declaration, hence no record. The sentence that makes this
public repo's exceptions sound enumerated and audited describes three marked
lines out of several hundred.
*Counsel:* either the claim narrows to what is true (the identity is published
by decision, recorded once, in the decision record and one register entry), or
the term list and markers are made to match it. The first is cheap and honest;
the second marks hundreds of lines for no protection.

**PI2 — MAJOR. For this public repo the new text is weaker than the text it
replaced, and it leaves a reading under which a session commits personal data
and calls it compliant.** Four gaps compound:

1. No passage says **who decides** an exception. His words tie purpose to "the
   work I ordered"; the templates turn that into "the work it exists to do" and
   "the work needs", which a session judges for itself.
2. **"Purpose" has no test.** No passage gives a purpose that fails, so any
   stated reason satisfies it.
3. The one unconditional sentence in atelier's constraint lists health, family,
   financial and personal-estate context. It omits names, contacts and
   addresses, which `REPO-STANDARD.md` lists, so a third party's name or contact
   detail falls outside the flat prohibition and inside "exceptions".
4. `REPO-STANDARD.md` makes the public list open ("such as").

The guard then agrees with the loose reading: probe B (a fictional third-party
contact line with a one-word reason) and probe C (a keyed date-of-birth with a
marker claiming purpose) both exit 0, and the staged form (probe G) reports them
as two suppressions and passes; the unmarked control (probe D) exits 1. The
replaced constraint said no personal data, ever, and that this was the point of
the repo. A pattern scanner was always bypassable by a marker; what changed is
that the text now licenses the marker.
*Counsel:* one sentence closes it without touching the principal's rule: in a
public repo an exception is the principal's to grant, in his words, and the list
is closed until he adds to it.

**PI3 — MODERATE. The standard for "recorded and narrow" is an open board item,
cited by an elided path, that nothing in the tree can yet satisfy.**
`REPO-STANDARD.md` line 182 points at a roadmap item, with an ellipsis in the
path, for "why, who, when, the narrowest span". That item is unticked work. Its
own audit records that no span form exists, that no exception in the tree
carries a session identifier, and that `GUARDS.md` § *Who, why, when* says the
opposite (who and when come from version control). So build doctrine now cites a
requirement that every existing exception fails, that the marker grammar cannot
express, and that a sibling method doc contradicts. The passages also never say
where an exception is recorded when there is no line to mark (a commit message,
git metadata, a binary, a file name), nor what a session does on finding an
unrecorded one. A draft decision record for an exception register exists and
cites this rule as its `why`; the rule does not cite it back.
*Counsel:* cite `GUARDS.md` for what binds now and name the register as the
coming home, rather than citing a work item as a standard.

**PI4 — MODERATE. The four passages give four different lists and three
different exception tests** (table in lens 2). The templates lost the old
"instance data" class entirely: estate topology, machine-local paths and the
client-names hint that the replaced template comment carried are gone from what
a child reads, while `REPO-STANDARD.md` keeps them under the label "PII", which
they are not. `CONTRIBUTING.md` alone says "business detail" and alone omits
"narrow". A child session with only its own two files cannot tell whether a
hostname, a client name or a contributor's name is covered.

**PI5 — MODERATE. The delta wrote the account name into the adopter-facing
standard, undeclared, in the sentence that calls it PII.** `REPO-STANDARD.md` is
the generic standard every adopter reads; before `1ffefc7` it named no account.
The line carries no declaration, so the rule is breached on the line that states
it. Quoting the principal verbatim is house practice; the identifier inside the
quotation is not needed for the rule to be understood.
*Counsel:* the principal's call whether the parenthesis stays; if it stays it is
the first candidate for a declaration.

**PI6 — MODERATE. The old framing is still live on at least eleven surfaces, and
the landing commit says the contradiction is fixed.** Still stating a
shareable-only or can-go-public boundary: `tools/leakscan.py` (module docstring
and the command description), `tools/floor.py` line 461 (the registry's stated
reason for the check, which every child's floor reads), `tools/README.md` § the
leakscan heading and its first paragraph, `tools/secretscan.py` and
`tools/licenscan.py` docstrings, `commands/scan.md`, `commands/install-hook.md`,
the create-repo skill (step 1), `docs/method/PRINCIPLES.md` § 5, and
`README.md` line 52. Still stating the absolute form: `README.md` § *Sharing*
("ever"), which now contradicts the hard constraint beside it, and atelier
`CLAUDE.md` lines 7 and 68, which still call it the no-personal-data boundary.
The scanner docstring also attributes the rule to the apex and the autonomy
floor; a search finds it stated in neither.

**PI7 — MODERATE. A child reading only its stamped template does not get a
complete rule, and existing children are not told theirs changed.** The
constraint sits outside the stamped floor block, whose stated purpose is to bind
"even if atelier is never read". The template points to an atelier file by a
path not in the template's own `<atelier-path>` form; the leak-scan instruction
is inside an HTML comment that the scaffold guidance says to delete. Because the
line is outside the stamp, `stampscan` cannot see drift, so every adopted child
keeps the replaced sentence with no signal. No changelog entry and no follow-up
item was found by an unbarred sweep for the rule's wording.

**PI8 — MODERATE. The visibility-change case lost its only clause.** The
replaced standard bound any repo "that may widen its audience". The new text
tells a private repo it legitimately holds more, and says nothing about what
happens to those exceptions, or to the history that holds them, when the repo's
audience widens. `RECORD.md` already says a scrub of HEAD is not remediation on a
public repo. Widening remains a principal-confirmed floor action, which bounds
the harm, but with no register (PI3) he is asked to confirm without a list of
what the repo holds.

**PI9 — minor. "The leak and secret scans enforce the default as hooks"
overstates the guard.** Probe A: fictional prose describing a person's health
and debts passes at full term cover, exit 0; `tools/README.md` line 17 says as
much. CI runs structural-only by design. The floor's `scope` setting lets a repo
scan only a shareable subtree, so in exactly the private repos the new default
now reaches, the guard may not run over most of the tree.

**PI10 — minor. The quotation in `REPO-STANDARD.md` is cut at the front without
a mark, and its lead-in differs from the commit's account.** It opens
mid-sentence in lower case. The fuller form, which I saw only in the landing
commit's hunk to a barred item, begins with a clause the standard drops. The
standard says he called the shareable-only boundary the wrong one; the commit
message says he rejected both boundaries offered.

**PI11 — note. What holds.** The quotation's substance is carried without
distortion; atelier's own constraint is the strictest of the four and keeps a
flat sentence for the gravest categories; no health, family, financial or
address detail entered through the delta or its commit message; floor, stamp and
block guards are green.

### Re-run ledger

All in the review worktree unless marked (clone) for the scratch clone under the
session scratchpad at `PI/probe`. Exit codes read directly, never off a pipe.

| Command | Result |
|---|---|
| `python3 tools/floor.py --plane hook --root .` | exit 0; leakscan clean (structural + local), 0 suppressions on an empty stage |
| `python3 tools/floor.py --plane ci --root .` | exit 0; leakscan 53 marker suppressions, 7 ignore-file files, `local-term×3`; secretscan 22 advisory; pathscan 2 warn-only findings, neither in the delta |
| `python3 tools/leakscan.py --require-terms --root . .` | exit 0; same tally |
| `python3 tools/stampscan.py --warn --root . .` | exit 0; 1 block, identical; same at `1ffefc7` (clone) |
| `python3 tools/blockscan.py --check --warn --root .` (clone) | exit 0 |
| `python3 tools/blockscan.py --against HEAD^ --warn --root .` at `1ffefc7` (clone) | exit 0, nothing moved |
| `python3 tools/linkscan.py --root .` over the four delta files | exit 0 |
| `python3 -m unittest tools.test_templates` (clone) | exit 0, 44 tests |
| `python3 tools/leakscan.py --selftest` (clone) | exit 0 |
| `coldsweep` for the account name | 27 lines, 16 files, 0 with a marker |
| `coldsweep` for the full name / the author address / the first name | 4 lines / 2 lines / 818 lines |
| Probes A to G (clone, fictional content, removed after) | A 0 · B 0 · C 0 · D 1 (control) · E 0 · F 0 · G 0 with 2 suppressions |

**Not run:** the full Python suite and the Node suite. The delta is prose in
four documents and touches no code or test; I ran the one suite that reads the
templates. Counts above exclude the rule-2 barred paths, so the true number of
undeclared occurrences is higher, not lower.

### Follow-up checklist (all for the principal to rule; nothing applied)

- [ ] PI1: make the "declared where it appears" claim true or narrow it.
- [ ] PI2: say who grants an exception in a public repo and whether the list is
      closed.
- [ ] PI3: name a binding standard and a place of record; say what happens to an
      unrecorded exception.
- [ ] PI4: one list and one test across the four passages; restore or
      deliberately drop the instance-data class in the templates.
- [ ] PI5: rule on the identifier inside the quotation.
- [ ] PI6: sweep the eleven surfaces that still state the old framing.
- [ ] PI7: decide how the rule reaches existing children, and whether it belongs
      in the stamped floor.
- [ ] PI8: say what happens to a private repo's exceptions when it widens.
- [ ] PI9, PI10: wording.
