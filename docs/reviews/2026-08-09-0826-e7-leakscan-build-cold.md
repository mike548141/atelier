# Cold pass — the E7 leakscan build (D2–D6 fixes + the G1/G2/G4/G6/G7 builds)

**Pass type:** code cold pass (rule-4 queued — an application of ruled
decisions; the applier's judgement produced the delta).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-06, and the session that landed the 2026-08-09 follow-up on the same
  surfaces (see *What the work is*).
- **Who spawned this review:** the principal (Mike), in a session he opened on
  2026-08-09 and pointed at the review queue — rule 4's worked example. His
  words: *"Please do any review work that waiting."*
- **Author's non-involvement:** the taker session authored no part of this
  delta, was neither started nor instructed by the authoring sessions, and
  wrote this brief as the non-author taker. Rule 4's single criterion is met,
  and the tier was checked at selection.
- **Orchestration shape:** the review runs under an orchestrator holding a
  context partition — the intent-record references are withheld from this brief
  and handed to the reviewer only after its own findings are durably written.

## What the work is

Code landed 2026-08-06 plus a 2026-08-09 follow-up on the same surfaces,
reviewed at HEAD:

1. [`tools/leakscan.py`](../../tools/leakscan.py) and
   [`tools/test_leakscan.py`](../../tools/test_leakscan.py) — the D2–D6 fixes
   and the G1/G2/G4/G6/G7 builds; the suite grew 53 → 114, then 114 → 119 in
   the follow-up.
2. [`tools/leakscan-terms.example.txt`](../../tools/leakscan-terms.example.txt)
   — the `forms:` syntax.
3. The `CHANGELOG.md` entry (2026-08-06), and the 2026-08-09 follow-up: the
   scoped `local-term` marker (delta widened per the landing-commit rule).

## Hard constraint — read before running anything

**atelier is a PUBLIC repo.** The scanner under review exists to keep
machine-local terms out of it. The operator's real term list is machine-local
(`$ATELIER_LEAKSCAN_TERMS`, else `~/.claude/leakscan-terms.txt`), outside
every repo by design.

- Probe with a **scratch term list** written to the session scratchpad only.
  Do not read the operator's real list into your context, do not modify it,
  and never point a probe at it.
- **Never write any machine-local term** — or any private repo's name — into
  any file in any repo, including your verdict and any scratch file inside a
  working tree. Counts and classes only.

## Scope

Widest the work admits: the intent of each fix and build as the code expresses
it, the `forms:` syntax design, the scoped-marker design, the code, the tests,
and live behaviour on both planes (staged and tree). **Non-goals:** none
narrows the delta. The reviewer does not decide findings' dispositions;
residue joins the principal's ruling round per house practice.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Does the `forms:` syntax cover the shapes a real term takes, and
   does the scoped marker's scope model leave a hatch wider than the finding
   it suppresses?
2. **Correctness & quality** — run the suite; probe the scanner live with a
   scratch term list on both planes; verify marker scoping suppresses exactly
   the scoped class and nothing else, and that exit codes hold.
3. **Completeness / harvest** — which term shapes or file classes escape;
   does the example file teach the syntax the code actually implements?
4. **Security & privacy** — mandatory and central: this delta *is* the
   privacy control. Check for bypasses — a term reachable through an encoding
   or splitting the `forms:` model misses, a marker scope that silently
   swallows a genuinely new leak, ignore-file precedence making a term
   unreachable where it should bind. Your verdict itself must honour the hard
   constraint above. The house security scanner reads pending diffs; this is
   a landed-delta review, so state the reach case that applied.

## Re-run obligation

Re-run, do not read, at least: the suite-count claims (53 → 114 at the
2026-08-06 landing, 114 → 119 at the follow-up) and the full suite at HEAD
(house invocations in [`.githooks/pre-commit`](../../.githooks/pre-commit)),
a live probe with a scratch term list on both planes, the `forms:` syntax
against the example file, and the scoped `local-term` marker's behaviour on
the three published-identity lines it exists for.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the intent-record refs are orchestrator-held under the rule-1 context partition, handed over only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/sessions/`, and every prior verdict
in `docs/reviews/`. The intent record (the sweep record and the ruling the
delta applies) is held by the orchestrator and will be provided on receipt of
your committed findings. Reconcile after, never anchor before.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `LK`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then report; the deferred
references arrive; append a reconcile section and finalise.
