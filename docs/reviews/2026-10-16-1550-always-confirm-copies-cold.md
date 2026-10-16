# Cold pass — the always-confirm floor list's copies match AUTONOMY

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes this pass; a session that cannot honour it stops.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or
instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/620-rule-4-cold-pass-queued-floor-list-membership.md`.
**Why it earns a review:** the always-confirm floor is the list of actions an
agent must stop and ask before taking, whatever its grant; a session that reads
a copy missing a member proceeds where it should stop, and the apex is the first
document every session reads.

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
  message body (the author's own account of why, which names one AUTONOMY stop
  it chose not to add) and diff; grep hits for the floor-list terms across the
  tree (records excluded) and the matching lines of `AUTONOMY.md`,
  `PROPAGATION.md`, the child `CLAUDE.md` template and the session-onramp skill;
  `REVIEW.md` down to § *Whether work earns a review*; the ask halves, above the
  first divider, of two 2026-10-04 briefs as format models; filename listings of
  `docs/reviews/` and `docs/roadmap/`, and path greps over `docs/reviews/` that
  name prior verdicts without reading them; and its auto-loaded cross-session
  memory index. Its orchestrator read the `docs/SESSIONS.md` index tail (entries
  through 2026-10-16, including the authoring runs' one-paragraph summaries) and
  the 2026-10-16 session record's close section, and passed this writer nothing
  evaluative beyond the pointer list. What this writer suspects is in the sibling.

## What the work is

Landing commit (diff it; review the paths at HEAD):

- `7c2ab8b` (2026-10-03) — apex: the always-confirm list names unapproved tools in
  every copy (200/100 C7)

Delta paths: `docs/method/00-APEX.md` (two inline floor lists, in § on the
principal's authority) and `docs/method/README.md` (item 3, the `AUTONOMY.md`
summary). No later commit has touched either path.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether every statement of the floor in this repo, and in what it stamps into
children, names the same members as the canonical list — and whether the three
edited lists now do. Read `AUTONOMY.md`'s floor at HEAD and treat it as the
reference. Then find every copy yourself — prose lists, stamped blocks,
templates, skills, the onramp, tool docstrings, ADRs, `README.md`,
`CHANGELOG.md` — and build a membership matrix (floor member × copy), marking
each copy as stamped (watched by `stampscan`/`blockscan`) or free text, and as a
full list or a declared summary. For each of the three edited lists, read the
sentence it sits in and say what kind of text it is (narrative, a summary, a
ruling's restatement) and whether the edit leaves that text saying what its
attribution says. Test the words themselves on cases: a session about to add a
CI secret, enable a GitHub App, install a CLI from a package manager, add an MCP
server, start a deploy-on-push to an already-public site with a new content
class, or rotate a key that locks out a second machine. Does each copy route
each case to the same answer?

**Non-goal:** which actions belong on the floor (`AUTONOMY.md`'s membership is
ruled doctrine). It is read as the reference, and any internal inconsistency in
it is in scope as a finding.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Is "every copy matches AUTONOMY" the right invariant for a summary that says
   "Repos may narrow"? Should a copy enumerate the floor, or point at it?
2. **Correctness & quality.** The matrix. Wording drift between copies of the same
   member ("a new trust surface" against "adding a new trust surface (deploy
   keys, webhooks, OAuth/app grants)"); whether "unapproved" is defined — who
   approves a tool, and where is approval recorded? The commit's account of the
   one stop it did not add is a claim: test it against `AUTONOMY.md`'s own text.
3. **Completeness / harvest.** Copies the commit did not touch that differ from
   the reference after it; any doc that names the floor by a count ("seven
   stops"); whether `stampscan` and `blockscan` watch every copy that is meant to
   be a stamp, and whether an unstamped copy should be one (V3, V4).
4. **Security & privacy** — mandatory and central: the floor is the
   security-and-safety stop list. Hunt for any path by which a session reading
   only one copy installs a tool, grants an app, adds a credential or widens an
   audience without asking. Code altitude: none in the delta (prose), but if a
   tool's docstring carries the list, read it. `/security-review` is discharged by
   grounds — a landed prose delta; the session's pending diff is other passes'
   drafts — say so.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- the floor on both planes at HEAD (`python3 tools/floor.py --plane hook --root
  <root> --tools <root>/tools`, then `--plane ci --root <root>`), exit codes read
  explicitly
- `python3 tools/stampscan.py --warn --root . .`, `python3 tools/blockscan.py
  --check --warn --root .` and `python3 tools/blockscan.py --against 7c2ab8b^
  --warn --root .`
- the matrix's grep, recorded so it re-runs, with its exclusions stated

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
  --also-exclude $Q/620-rule-4-cold-pass-queued-floor-list-membership.md \
  --also-exclude docs/reviews/2026-10-16-1550-always-confirm-copies-cold.deferred.md \
  --also-exclude docs/roadmap/200-anti-slop-invariant-registry-promote-rec \
  <pattern>
```

`--include-barred` only with disclosure in the verdict. The delta and the doctrine
it must agree with are never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, findings with
stable IDs (prefix `FM`: `FM1`, `FM2`, …) and severities (MAJOR / MODERATE /
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
