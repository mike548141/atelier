# Cold pass — the child reviews template names tiers and seats, not models

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes this pass; a session that cannot honour it stops.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or
instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/590-rule-4-cold-pass-queued-template-tiers-not-models.md`.
**Why it earns a review:** the template is copied into every child repository at
creation and tells the child which seat reviews and which applies; a wrong or
undefined seat there misroutes every child's reviews, and a copied file does not
update itself.

## Spawn provenance

- **Author of the work under review:** the queue run whose intent record is
  dated 2026-10-03 01:44 UTC (path in the sibling; not opened by this writer),
  which landed the commit under *What the work is*. The commit carries an Opus
  co-author trailer.
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
  read: the queue pointer in full; the landing commit's subject, `--stat`,
  message body (the author's own account of why) and diff, and the same for the
  next commit on the same file (160/610's delta); the template file at HEAD in
  full; `REVIEW.md` down to § *Whether work earns a review*; the ask halves,
  above the first divider, of two 2026-10-04 briefs as format models; filename
  listings of `docs/reviews/` and `docs/roadmap/`, and path greps over
  `docs/reviews/` that name prior verdicts without reading them; and its
  auto-loaded cross-session memory index (one-line notes, some on review tiers).
  Its orchestrator read the `docs/SESSIONS.md` index tail (entries through
  2026-10-16, including the authoring runs' one-paragraph summaries) and the
  2026-10-16 session record's close section, and passed this writer nothing
  evaluative beyond the pointer list. What this writer suspects is in the sibling.

## What the work is

Landing commit (diff it; review the path at HEAD):

- `77fc609` (2026-10-03) — templates: the reviews README names tiers, not models
  (200/100 C8)

Delta path: `docs/build/templates/docs/reviews/README.md` — the opening paragraph
of § *Reviews* and the closing paragraph of § *Format*. The next commit on the
file, `ebb358b` (same day, 160/610's delta), changed § *When to write one*; it is
a non-goal here.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether a child session, holding only this file, can tell who reviews, who
applies, and who decides — and whether what it is told is what `REVIEW.md` and
`ECONOMICS.md` say. Read the file at HEAD and diff `77fc609`. List every phrase
that names a seat or a capability ("a more capable model", "the principal-named
review tier", "the builder", "the workhorse seat", "review-tier sessions") and,
for each, find where atelier defines it and whether a child can reach that
definition. Test against cases: a child created from this template before any
tier ruling exists in it; an adopter outside this estate with one model and no
named tier; a child whose principal names the builder's own tier for review; a
child whose review is of its own doctrine (rule 3/4); a child that has the file
but no copy of atelier (the header's "enough to act on without opening atelier").

**Non-goals:** the trigger list in § *When to write one* (160/610's subject);
whether review should be tiered at all (ruled doctrine). Both are read only for
consistency with the delta.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   The change swaps model names for roles; test whether each role word carries
   the same meaning the model name did, more, or less — and whether the
   surrounding sentence still reads true with the role in it.
2. **Correctness & quality.** Every sentence of the file that says who acts on a
   review, read against `REVIEW.md` § *Why review, and who reviews*, rules 3–4,
   lifecycle step 4, and `ECONOMICS.md` (grep it for the seat words). Does the
   file agree with itself, first paragraph to last (V5)? Do its `<atelier-path>`
   pointers resolve to the anchors named?
3. **Completeness / harvest.** Every other surface stamped into children or
   shipped to adopters that still names a model where a role is meant: grep
   `docs/build/templates/`, `skills/`, `commands/` and `README.md` for model
   names. How does a change to this template reach children already created —
   `stampscan`, the create-repo skill, `CHANGELOG.md`, a template version? Is
   anything owed so existing children notice (V3)?
4. **Security & privacy** — mandatory. Design altitude: can the new wording route
   a review of security-relevant work to a seat the doctrine does not intend, or
   let the author's own seat review and apply its own doctrine? Code altitude:
   none (prose). `/security-review` is discharged by grounds — a landed prose
   delta; the session's pending diff is other passes' drafts — say so.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- the floor on both planes at HEAD (`python3 tools/floor.py --plane hook --root
  <root> --tools <root>/tools`, then `--plane ci --root <root>`), exit codes read
  explicitly
- `python3 tools/stampscan.py --warn --root . .` and `python3 tools/blockscan.py
  --check --warn --root .` — the template carries a stamp header
- the model-name grep in lens 3, with counts recorded per surface

## House rules for this run

- Name your own worktree in the verdict. Run **no git command that writes** there;
  read-only git (`log`, `show`, `diff`, `blame`) is fine. Probes, scratch
  children and checkouts of older commits go in a private clone under your
  scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the full Python suite at most
  once, foreground. Never point a scanner at another repository on the machine.
- `/security-review` reads the session's pending diff. Discharge it by grounds for
  this landed delta and do the code-altitude read by hand against the OWASP
  catalogue, or keep the tree clean whenever you spawn it.
- Absolute ISO-8601 dates from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address or personal
  detail — the repo is public; describe and locate instead.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md beside this brief under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer named
above, this brief's sibling (same path, `.deferred.md`), and the commissioning
item `100-r2-found-eleven-live-contradictions.md` with every other item under
`docs/roadmap/200-anti-slop-invariant-registry-promote-rec/`.

Sweep with rule 2's default bar plus these (`<root>` is your worktree):

```sh
Q=docs/roadmap/160-doctrine-review-owed
python3 tools/coldsweep.py --root <root> \
  --also-exclude $Q/590-rule-4-cold-pass-queued-template-tiers-not-models.md \
  --also-exclude docs/reviews/2026-10-16-1550-reviews-template-tiers-cold.deferred.md \
  --also-exclude docs/roadmap/200-anti-slop-invariant-registry-promote-rec \
  <pattern>
```

`--include-barred` only with disclosure in the verdict. The delta and the doctrine
it must agree with are never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, findings with
stable IDs (prefix `TT`: `TT1`, `TT2`, …) and severities (MAJOR / MODERATE /
minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger with commands and results, and a follow-up checklist. Commit it
before opening the sibling. If an orchestrator holds the sibling outside the
tree, it releases it on your committed findings.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against its seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Fold the sibling in below the reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply
nothing; counsel per finding is welcome, labelled as counsel.
