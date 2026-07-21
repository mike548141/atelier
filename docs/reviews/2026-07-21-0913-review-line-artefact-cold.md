# Cold pass — review-line artefact: templated `review:` field + reviewscan lint (delta `fa7a90f`)

- **Date/time**: 2026-07-21 0913 UTC
- **Spawn provenance (rule 4)**: taken from the ROADMAP `⏳` queue by a session
  Mike spawned with "Please do any review work" (Fable). This session authored
  none of: the `fa7a90f` delta, the reviewscan tool, the templates and doctrine
  it edits, or any record of the authoring session. Claim landed on `main`
  (`921cc1a`) before review work started; this brief is taker-written in
  wt: review-line-artefact-cold-pass.
- **Named exposure**: the queue pointer this cycle is refs-only (the SR5 class
  fixed — noted as a compliance observation, in scope). But before scoping to
  `--format=`, the taker's `git show --stat fa7a90f` printed the delta's full
  commit *body* — an author account claiming "presence only", "frozen records
  never touched", "suite 284→293; selftest + red/green legs bite-proven",
  "narrowed to per-surface honesty", "dogfoods the field". All of that is
  author framing: treated as claims to re-derive, not facts. The taker has
  also read `docs/method/REVIEW.md` in full at HEAD (it is part of the work
  under review) and the ROADMAP header block.
- **Deferred material (opened only after findings are committed)**: the intent
  record `docs/decisions/2026-07-21-0744-review-line-artefact.md` (the
  author's deliberation — it is *also* a delta file, so its **structure** is
  in scope immediately for the dogfood check, but its evaluative account is
  read for reconcile only); the CHANGELOG entry; the 0820 ADR *addendum* text
  appended by this delta; the authoring session's SESSIONS.md/session record;
  the commit body already seen (re-read for reconcile).

## What the work is (refs only)

Commit `fa7a90f` at HEAD `921cc1a`: `tools/reviewscan.py` +
`tools/test_reviewscan.py` (new); wiring into `.github/workflows/ci.yml`,
`docs/build/templates/workflows/floor.yml`, `tools/pre-commit.sample`,
`tools/test_precommit.py`; template surfaces
`docs/build/templates/docs/decisions/template.md`, `…/decisions/README.md`,
`…/docs/ROADMAP.md`; doctrine `docs/method/REVIEW.md`; records
`docs/decisions/2026-07-21-0744-review-line-artefact.md` (new),
`…/2026-07-18-0820-review-the-design-not-only-the-build.md` (addendum),
`CHANGELOG.md`, `tools/README.md`. In-scope at HEAD: those files plus every
other surface that states or relies on the review-line convention
(create-repo skill, review-brief skill, REPO-STANDARD, the decisions dir
itself, the reviews template).

## Why it earns a review

Doctrine by function (a lint that governs what future records must carry,
stamped into every child's floor), plus a silent-failure surface: a lint
whose green exit is read as "the convention is enforced". Worst failure
modes: (a) a false negative — a decision record with no review line passes
and the estate believes omission is now impossible; (b) an over-broad lint
that reds frozen history or non-decision files, training sessions to
appease it; (c) the "structural" claim in REVIEW.md overstating what the
machine actually reaches.

## Lenses and the taker's attack surface

Lens 1 — approach & assumptions (named by the taker as its first act):

- **A1 — "presence only" is the right depth, but presence must be
  well-defined.** What exactly satisfies the lint — any line matching
  `review:`? Case? A `Review` field in a table? A `review:` inside a code
  fence or blockquote (REVIEW.md itself quotes the convention — is it a
  decisions-dir-only scan)? Probe: a record with `review:` only inside a
  fenced example; a record with `**Review**:` styled per the template; a
  record with the line but empty after the colon. An empty-value pass is
  the costume: `review:` with nothing after it satisfies "presence" and
  says nothing.
- **A2 — the date boundary must not be gameable or wrong-way.** Boundary =
  record dated ≥ 2026-07-21, read from where — filename? Front matter? If
  filename, a new record deliberately (or accidentally) dated 2026-07-20
  escapes the lint forever; if mtime/git-date, frozen records could red.
  Probe both directions: a backdated new file passes silently (false
  negative, silent); a legitimately old record must never red (fail-loud
  but wrong). Also the UTC question: the boundary date vs local-date
  filenames (the estate's own at-rest-UTC rule).
- **A3 — the lint must fail loud on an unscannable state.** The §14
  silent-success class: if `docs/decisions/` is missing, or a path arg is
  typo'd, does it exit 0 having scanned nothing? Does it distinguish
  "scanned N, all carry the line" from "nothing matched my idea of a
  record"? README.md in the decisions dir must be exempt without the
  exemption mechanism being a general escape.
- **A4 — the per-surface honesty split must be real, both directions.**
  REVIEW.md now claims structural-for-decision-records,
  conventional-for-roadmap. Attack both: is the decision-record half
  actually structural at every enforcement point (pre-commit only fires on
  *staged* files — does a new record added without staging escape? does CI
  red it?), and is the roadmap half genuinely unlintable or just unbuilt
  (the stated grounds: a heading lint would be trained away — does that
  argument survive)?
- **A5 — the templates must teach the field so it survives stamping.** The
  child gets the lint via floor.yml and the field via template.md — are the
  two consistent (does the template's field format satisfy the child's own
  lint verbatim)? Does the ROADMAP template's prose-only convention match
  what REVIEW.md says of it? create-repo stamps templates into children —
  does the stamped tree pass its own floor at birth (a child born
  yesterday: its first decision record is dated after the boundary — does
  the scaffold's example/seed content red)?
- **A6 — the delta must dogfood.** The intent record is itself a decision
  record dated 2026-07-21 — it must carry the field and pass its own lint;
  the 0820 addendum is an edit to a *frozen* pre-boundary record — the lint
  must not demand retro-fitting it, per the delta's own boundary rule.
- **A7 — the wiring must be complete and symmetric.** ci.yml, floor.yml,
  pre-commit.sample: same tool, same mode, same failure semantics? A lint
  in CI but not pre-commit (or vice versa) has a stated-vs-actual gap;
  floor.yml is what children copy — is its invocation self-contained
  (reviewscan present in the child's tools/ at stamp time? pinned copy?).

Lens 2 — correctness & quality: re-run everything stamped proven — the
suite (claimed 284→293) and its pass; `reviewscan.py --selftest` if it has
one; the red/green legs live (a synthetic offending record must red, its
fix must green); floor green at HEAD; pre-commit hook fires on a staged
offending record; no stale "no template carries the review: field" /
"enforcement is structural [unqualified]" phrasing left at HEAD.

Lens 3 — completeness / harvest: surfaces that state the old truth ("F6
open", "no artefact", "the review: templates haven't landed") — REVIEW.md,
the 0819/0100 decision records, ROADMAP(-DONE), skills/review-brief,
skills/create-repo, docs/reviews template, tools/README; whether the
reviews-dir brief template itself should carry the convention; whether
`sizescan`/other scanners' exemption idioms were reused or reinvented.

Live re-runs owed in scope: full tools suite (count + pass); reviewscan
against HEAD; synthetic red/green probes for A1/A2/A3/A6 edges (in the
worktree or scratch, never landed); the pre-commit staged-file leg; grep
sweeps for stale phrasing.

---

# Verdict — 2026-07-21 0950 UTC

**Provenance repeated (rule 4):** reviewed by the rule-4 taker named in the
brief — Fable, Mike-spawned ("Please do any review work"), author of none of
the delta, the tool, or their records. Findings below were committed before
any deferred material was opened. **Added exposure discovered mid-run, named
not denied:** two mid-turn messages arrived that Mike then identified as
pasted from a previous session, not from him — one pointed at PR #13 (the v2
plugin de-instance), one reported a `worktree.py list` bug. Neither was
treated as scope or fact: PR #13 was inspected only far enough (title + file
list) to establish it is a *different* strand, and this pass's scope stayed
the `fa7a90f` delta the `⏳` pointer names.

## Lens 1 — approach

**The build is sound and honestly scoped.** Presence-only is the right depth
(the tool proves the line exists; honesty of the grounds stays judgement —
layers, not alternatives), the decisions-dir-only scope honours the 0820
record's grounds rather than quietly overreaching, and the filename-date
boundary is the floor.yml SIGN_BOUNDARY shape: frozen records blameless by
construction, no history rewrite demanded (A6 confirmed — the 0820 addendum
edits a pre-boundary file and the lint correctly ignores it). The per-surface
honesty split (A4) is real in both directions: structural for decision
records at all three enforcement points — pre-commit (whole-tree, so no
staged-file hole; **fail-closed** when the scanner is missing), atelier
`ci.yml`, child `floor.yml`, all invoking whole-repo-root — and the roadmap
half is genuinely convention-only, stated as such where a reader meets it.
Templates teach the field in a form the lint accepts verbatim (A5), and the
templates-tree skip prevents the scaffold's own forms from redding a child at
birth. The delta dogfoods: its intent record is the one post-boundary record
at HEAD and carries the line.

## Live re-runs — all reproduce

- Suite: **Ran 293 tests, OK** — the "284→293" claim checks out.
  `reviewscan --selftest`: OK (red + green legs both bitten in-fixture).
- Whole-tree scan at HEAD: **✓ clean, 1 post-boundary record, exit 0.**
- Red/green legs re-driven live in scratch: an offending post-boundary record
  reds (exit 1, named in output); adding the line greens. Boundary edges
  re-proven: pre-boundary, retired-scheme (`0001-…`), `README.md`,
  `template.md`, and a dated example inside a templates tree are all skipped.
- Fail-loud floor: nonexistent `--root` → exit 2; pre-commit blocks when the
  scanner file is absent rather than skipping it.

## Findings

- **RS1 (MEDIUM, lens 2 — the §14 silent-success class, on the tool's most
  natural hand-run).** `find_records` discovers records only by
  `rglob("docs/decisions")` *under* a given base, so an explicit path arg
  that is the decisions dir itself — or a single record file — matches
  nothing: `reviewscan --root . docs/decisions` and
  `reviewscan --root . docs/decisions/<record>.md` both print "✓ clean — 0
  records" and **exit 0**, having scanned nothing. Probed live, both legs.
  This is the linkscan L1 class (a plausible path arg silently scans nothing
  and greens), already paid for once in this house. All three *wired*
  invocations pass the repo root, so CI/pre-commit are unaffected — the
  exposure is the hand-run and any future wiring that scopes the arg. The
  honest zero (a repo with no `docs/decisions` yet) is legitimate and must
  stay green; the defect is only the explicitly-named-but-unscannable arg.
  *Counsel: teach `find_records` to accept a decisions dir or a record file
  directly (base named `decisions` under `docs`, or a `.md` matching
  RECORD_NAME whose parent qualifies); two suite cases. Alternatively exit 2
  when an explicit path arg contributes zero decisions dirs — but the
  direct-accept fix is better: the natural invocation should work, not
  error.*
- **RS2 (LOW, lens 2 — fence false-pass).** A `review:` line inside a fenced
  code block satisfies the lint: a record that *quotes the convention* while
  omitting its own judgement passes — probed live (a record whose only
  review-mention is a fenced example greens). Exactly the sibling edge the
  size-rebalance pass found in sizescan (SR3), inverted: there the fence
  false-*reds*, here it false-*greens*, which is the worse direction for a
  lint whose green is read as "the judgement is stated". Low because the
  colliding record shape (fenced example, no real field) is rare outside
  doctrine-about-the-convention — but atelier is exactly the repo that writes
  doctrine-about-the-convention. *Counsel: fence-state toggle in
  `scan_record` (the sizescan counsel's shape), one suite case.*
- **RS3 (LOW, lens 1/2 — the empty field is a blank in the field's
  clothes).** `**Review**:` with nothing after the colon passes — probed
  live. Presence-only is the stated design, but the thing whose presence the
  rule demands is *a judgement*; an empty value is precisely the blank that
  "omission is the bug" exists to make impossible, now machine-blessed.
  *Counsel: require non-whitespace after the colon (`:\s*\S`) — still
  presence-only, one regex touch + one suite case.*
- **RS4 (LOW, lens 2 — boundary and typography edges, stated not fixed).**
  (a) A *backdated* filename (`2026-07-20-…` created after the boundary)
  escapes the lint silently — inherent to filename-dated boundaries; the
  house's real date-error mode (NZ local vs UTC) errs *forward*, which is
  the safe direction, and a gaming author has a cheaper honest hatch
  (`reviewscan:allow:`) sitting in plain sight. (b) `REVIEW:` all-caps reds
  as missing — fail-loud, cosmetic. *Counsel: state (a) as a residual in the
  docstring beside the boundary rationale; (b) fold `REVIEW` into the regex
  or leave — either is defensible.*
- **RS5 (LOW, lens 3 — stale scanner enumeration, pre-existing and widened).**
  `docs/build/REPO-STANDARD.md:94` describes the child floor as running
  "secretscan · structural leakscan · linkscan" — already stale by sizescan
  and signscan before this delta, and now by reviewscan too. Each scanner
  addition has walked past it; this delta had the same-commit-currency duty
  at the moment it added a fourth. *Counsel: replace the parenthetical
  enumeration with a non-enumerating pointer ("its public `tools/` scanners —
  see tools/README.md") so the list can never go stale again.*

**Compliance observation (positive):** this cycle's `⏳` queue pointer was
refs-only — the first pointer to honour rule 4's ceiling after two
consecutive breaches (the 1355 and 2040 passes' SR5 class). The
point-of-use fix (the ceiling stated in the ROADMAP header) appears to have
worked on its first exercise.

## Verdict

**PASS — 0 MAJOR / 1 MEDIUM / 4 LOW.** The mechanism is right, narrow on
purpose, honestly stated per surface, and every recorded proof reproduces.
The MEDIUM is the house's own silent-success class on the unwired hand-run
path; nothing found touches the wired enforcement. Per rule 3, all findings
on this self-authored doctrine are **Mike's to decide**; counsel above,
nothing applied by this pass.

## Reconcile — deferred material opened after the findings commit (`ed478ee`)

Opened: the intent record `2026-07-21-0744` (evaluative account), the
CHANGELOG entry, the 0820 addendum text, and the delta commit body (re-read).

- **The account matches the build.** Every decision the intent record states
  (presence-only, decisions-dir scope, landing-date boundary, the three
  rejections) is what the code does; the "children inherit immediately via
  floor.yml's float-to-main checkout" consequence is accurate — reviewscan
  is on `main`, so children's floors already run it ahead of any pin bump.
  The commit body's claims all reproduced (suite, selftest, red/green,
  dogfood, per-surface narrowing). No finding is contradicted; RS1–RS5
  stand as written.
- **One new finding from the deferred material itself — RS6 (LOW, lens 2 —
  the addendum is an insertion, not an append).** The 0820 record's
  2026-07-21 addendum was spliced into the middle of the earlier F6
  qualification note: the prior note's closing sentence ("This record's
  Rejected section already carries that honesty; this line saves a reader
  the inference") was detached and now dangles at the end of the *new*
  paragraph, where "this line" reads as the addendum and the sentence no
  longer says what its author meant. Append-only means the earlier appended
  note's text should also have stayed intact, with the addendum below it.
  Substance is unharmed; the record now misreads slightly. *Counsel: a
  records-only touch — restore the orphaned sentence to the F6 note it
  belongs to and let the addendum stand whole beneath it.* Named honestly:
  found after the findings commit, from deferred material, and flagged as
  such per the application-review sequence REVIEW.md prescribes.
- The CHANGELOG entry also records a fleet re-stamp strand (three children's
  reviews templates) that is outside this delta's scope; nothing in it
  touches the reviewscan claims.

**Final: PASS — 0 MAJOR / 1 MEDIUM / 5 LOW (RS6 added at reconcile). All
findings await the principal's ruling; this pass returned no MAJOR, so per
the close rule the applying session's work closes the cycle without a
further full ceremony.**
