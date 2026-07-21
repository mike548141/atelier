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
