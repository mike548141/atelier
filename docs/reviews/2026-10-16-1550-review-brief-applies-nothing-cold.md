# Cold pass — the review-brief skill on who applies a verdict's findings

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes this pass; a session that cannot honour it stops.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or
instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/580-rule-4-cold-pass-queued-review-brief-rule-3.md`.
**Why it earns a review:** the skill is the point-of-use copy of `REVIEW.md` that a
session loads when it writes or runs a review, here and in every adopter of the
plugin; the changed paragraph says who acts on a verdict, which is the step rules
3 and 4 govern.

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
  message body (the author's own account of why) and diff; the delta file at
  HEAD (head and the changed section); `REVIEW.md` down to § *Whether work earns
  a review*; the ask halves, above the first divider, of two 2026-10-04 briefs as
  format models; filename listings of `docs/reviews/` and `docs/roadmap/`, and
  path greps over `docs/reviews/` that name prior verdicts without reading them;
  and its auto-loaded cross-session memory index (one-line notes, some on review
  independence). Its orchestrator read the `docs/SESSIONS.md` index tail (entries
  through 2026-10-16, including the authoring runs' one-paragraph summaries) and
  the 2026-10-16 session record's close section, and passed this writer nothing
  evaluative beyond the pointer list. What this writer suspects is in the sibling.

## What the work is

Landing commit (diff it; review the path at HEAD):

- `185abfb` (2026-10-03) — skills: review-brief no longer has the author apply
  findings on doctrine (200/100 C10)

Delta path: `skills/review-brief/SKILL.md`, § *Running it and landing the
verdict*. One later commit, `90c42ec` (2026-10-06, 200/050), edited the same
section to add the standing-checklist sentence; it is not this delta, but it sits
in the paragraph you will read at HEAD — attribute by `git blame`.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the section, read cold by a session that has only the skill, tells it
correctly who applies, who decides and who queues — for every kind of pass. Read
the section at HEAD and diff `185abfb`. Name the section's addressee (the
reviewer running the pass, the author landing it, or both) and test each sentence
against each. Run these cases and record a table: ordinary code reviewed warm by
its author's own spawn (`REVIEW.md` § *When to review*); code that is doctrine by
function (a validator, a CI gate, a template, this skill); a mixed delta (a guard
and the prose that states its rule); an application pass applying decided
findings to doctrine (`REVIEW.md` § *Applying decisions to doctrine*); a terminal
application after a pass with no MAJOR; a pass whose author is the principal (rule
3's distinct-parties premise); a withdrawn pass; an orchestrated pass with an
off-tier orchestrator. For each: who applies, who decides, what is queued, by
whom, and what tag is written.

**Non-goals:** `REVIEW.md` itself (the canonical text the skill compresses); the
content of the checklist sentence `90c42ec` added. Both are read only to judge
whether the delta agrees with them.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   The skill declares itself a stamped, narrowing-free copy of `REVIEW.md` (its
   header comment): test whether the new paragraph compresses the parent, or
   narrows, widens or re-words it — term by term against rules 3–4, lifecycle
   step 4 and the application paragraph.
2. **Correctness & quality.** Every sentence that cross-refers to the change:
   the skill's frontmatter description, § *First*, the lenses list, and the
   deferred-material paragraph after it. Does anything elsewhere in the skill
   still tell a session to apply or close findings itself? Check every cited
   anchor resolves.
3. **Completeness / harvest.** Every other surface that states who applies a
   finding: the child template `docs/build/templates/docs/reviews/README.md`
   (its sentence on this was changed the same day — 160/590's delta), the other
   skills under `skills/`, `commands/`, `docs/method/ECONOMICS.md` (the executor
   seat), `AUTONOMY.md`, and `README.md`. Do they say one thing (V3, V4, V5)? The
   skill ships in the plugin (`.claude-plugin/plugin.json`): is a version or
   `CHANGELOG.md` entry owed for adopters to notice the behaviour change?
4. **Security & privacy** — mandatory. Design altitude: can the new text be read
   to let an author approve or apply its own doctrine finding, or to spawn its
   own doctrine review — the independence failure rule 4 exists for? Code
   altitude: none in the delta (prose). `/security-review` is discharged by
   grounds — a landed prose delta; the session's pending diff is other passes'
   drafts — say so.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- the floor on both planes at HEAD (`python3 tools/floor.py --plane hook --root
  <root> --tools <root>/tools`, then `--plane ci --root <root>`), exit codes read
  explicitly
- `python3 tools/stampscan.py --warn --root . .` — the skill is a stamped copy
- `python3 tools/linkscan.py` over the skill, and `reviewscan`'s `--selftest`
- grep the delta's claims against `REVIEW.md` at HEAD and record each pairing

## House rules for this run

- Name your own worktree in the verdict. Run **no git command that writes** there;
  read-only git (`log`, `show`, `diff`, `blame`) is fine. Probes and checkouts of
  older commits go in a private clone under your scratchpad, named by your prefix.
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
  --also-exclude $Q/580-rule-4-cold-pass-queued-review-brief-rule-3.md \
  --also-exclude docs/reviews/2026-10-16-1550-review-brief-applies-nothing-cold.deferred.md \
  --also-exclude docs/roadmap/200-anti-slop-invariant-registry-promote-rec \
  <pattern>
```

`--include-barred` only with disclosure in the verdict. The delta and the doctrine
it must agree with are never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, findings with
stable IDs (prefix `RB`: `RB1`, `RB2`, …) and severities (MAJOR / MODERATE /
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
