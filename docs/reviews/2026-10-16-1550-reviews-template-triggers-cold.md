# Cold pass — the child reviews template's trigger list carries REVIEW's classes

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes this pass; a session that cannot honour it stops.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or
instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/610-rule-4-cold-pass-queued-template-review-triggers.md`.
**Why it earns a review:** the list decides, in every child created from the
template, which work earns a review at all; a class missing from it is work no
child reviews, and a class added wrongly is ceremony every child pays.

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
  previous commit on the same file (160/590's delta); the template file at HEAD
  in full; the review-brief skill's frontmatter and § *First*; `REVIEW.md` down to
  § *Whether work earns a review*; the ask halves, above the first divider, of
  two 2026-10-04 briefs as format models; filename listings of `docs/reviews/`
  and `docs/roadmap/`, and path greps over `docs/reviews/` that name prior
  verdicts without reading them; and its auto-loaded cross-session memory index.
  Its orchestrator read the `docs/SESSIONS.md` index tail (entries through
  2026-10-16, including the authoring runs' one-paragraph summaries) and the
  2026-10-16 session record's close section, and passed this writer nothing
  evaluative beyond the pointer list. What this writer suspects is in the sibling.

## What the work is

Landing commit (diff it; review the path at HEAD):

- `ebb358b` (2026-10-03) — templates: the reviews README's trigger list carries
  REVIEW's classes (200/100 C9)

Delta path: `docs/build/templates/docs/reviews/README.md`, § *When to write one*.
The previous commit on the file, `77fc609` (same day, 160/590's delta), changed
the opening and closing paragraphs; it is a non-goal here.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether a child, holding only this file, decides correctly whether a piece of
work earns a review. Read the section at HEAD and diff `ebb358b`. Read the file's
header comment and test the delta against every promise and prohibition it
states. The commit message gives a count of the copies of "what earns a review"
in atelier and says which had drifted: find every copy yourself, list them with
paths, and compare them class by class in a table — the count is a claim to
test. Parse the list as a child would: which bullets does the "in a product repo,
also" qualifier govern, and what does a child that is not a product repo (a
doctrine repo, an infrastructure repo, a records repo) read? Then drive cases:
a one-line change to a CI gate; a prose edit to a child's own `CLAUDE.md`; a new
dependency vendored; a records-only session log; a public README edit; a deploy
to an already-public site; a rename of a function nobody calls yet. For each,
the template's answer and `REVIEW.md`'s answer, side by side.

**Non-goals:** the opening and closing paragraphs (160/590's subject); the
calibration in `REVIEW.md` § *Whether work earns a review at all* (ruled
doctrine). Both are read only for consistency with the delta.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Is a restated list the right shape for this file, given what its header says
   the file is for? Are the two "product-repo additions" additions to the parent,
   or classes the parent already holds under another name?
2. **Correctness & quality.** Term-by-term agreement with the parent's wording of
   each class (V4, V5); the list's grammar and nesting as rendered; the routine
   examples in the paragraph after the list against the classes in it.
3. **Completeness / harvest.** Every surface that states the trigger — `REVIEW.md`,
   `skills/review-brief/SKILL.md` (frontmatter and § *First*), `ECONOMICS.md`,
   `README.md`, other templates — and whether any still disagrees. How does this
   change reach children created before it (V3)? Is a `CHANGELOG.md` entry, a
   stamp bump, or a create-repo note owed?
4. **Security & privacy** — mandatory. Design altitude: does the list still route
   security-relevant work (a guard, a secret path, a credential or trust-surface
   change, a silent-failure check) into review in every child shape? Code
   altitude: none (prose). `/security-review` is discharged by grounds — a landed
   prose delta; the session's pending diff is other passes' drafts — say so.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- the floor on both planes at HEAD (`python3 tools/floor.py --plane hook --root
  <root> --tools <root>/tools`, then `--plane ci --root <root>`), exit codes read
  explicitly
- `python3 tools/stampscan.py --warn --root . .` and `python3 tools/blockscan.py
  --check --warn --root .`
- the copy census in *Scope*, with the grep you used recorded so it re-runs

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
  --also-exclude $Q/610-rule-4-cold-pass-queued-template-review-triggers.md \
  --also-exclude docs/reviews/2026-10-16-1550-reviews-template-triggers-cold.deferred.md \
  --also-exclude docs/roadmap/200-anti-slop-invariant-registry-promote-rec \
  <pattern>
```

`--include-barred` only with disclosure in the verdict. The delta and the doctrine
it must agree with are never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, findings with
stable IDs (prefix `TG`: `TG1`, `TG2`, …) and severities (MAJOR / MODERATE /
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
