# Cold pass — the cancelled-run clause under RECORD.md's floor-at-head all-clear

**Pass type:** doctrine cold pass (REVIEW.md rule 4 — self-authored doctrine).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-09 (see *What the work is*).
- **Who spawned this review:** the principal (Mike), in a session he opened on
  2026-08-09 and pointed at the review queue — rule 4's worked example. His
  words: *"Please do any review work that waiting."*
- **Author's non-involvement:** the taker session authored no part of this
  delta, was neither started nor instructed by the authoring session, and wrote
  this brief as the non-author taker. Rule 4's single criterion is met, and the
  tier was checked at selection.
- **Orchestration shape:** the review runs under an orchestrator holding a
  context partition — the intent-record references are withheld from this brief
  and handed to the reviewer only after its own findings are durably written
  (REVIEW.md rule 1, the one arrangement honestly called structural).

## What the work is

Doctrine landed 2026-08-09, reviewed at HEAD:

1. [`docs/method/RECORD.md`](../method/RECORD.md) — § *The session log*, the
   sub-bullet under *When the close pushes, the evidence is the floor at head*
   covering cancelled CI runs.
2. The `CHANGELOG.md` entry that landed with it.

## Scope

Widest the work admits: the clause's intent, its wording as it will bind every
future session close, and its fit with the surrounding all-clear rule and with
the CI configuration it describes. **Non-goals — one, and it does not fence
the risk:** the reviewer does not decide any finding. Self-authored doctrine;
findings are the principal's to rule on (rule 3). Counsel may be recorded,
labelled as such.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Is the clause aimed at the real failure mode? Does it describe the
   CI's actual cancellation behaviour correctly?
2. **Correctness & quality** — verify the clause against the workflow files in
   `.github/workflows/` at HEAD: does the concurrency configuration it
   describes exist as described, and does the prescribed remedy work?
3. **Completeness / harvest** — what other run conclusions (failure, skipped,
   timed-out, queued-forever) does the all-clear rule meet in practice, and
   does the clause's shape cover or exclude them coherently?
4. **Security & privacy** — mandatory. If genuinely surface-free, discharge in
   one explicit line with grounds. The house security scanner reads pending
   diffs; this is a landed-delta review, so state the reach case that applied.

## Re-run obligation

Any claim in the delta text stamped as measured, live-proven, or grounded is
re-run, not read, where the repo admits it — the grounding incident's
mechanics can be verified against the workflow configuration and the GitHub
Actions run history (`gh run list`, full SHA).

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the intent-record refs are orchestrator-held under the rule-1 context partition, handed over only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/sessions/`, every prior verdict in
`docs/reviews/`, and the intent-record item for this delta (its reference is
held by the orchestrator and will be provided on receipt of your committed
findings). Reconcile after, never anchor before.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `CR`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then report; the deferred
references arrive; append a reconcile section and finalise.

---

# Verdict — cold pass, 2026-08-09

**Provenance repeated:** spawned by the principal (Mike) in a session he
opened on 2026-08-09 and pointed at the review queue — rule 4's worked
example. The reviewing session authored no part of this delta and was neither
started nor instructed by the authoring session. Tier: Fable, checked at
selection (ruling 2026-08-04). The review ran under an orchestrator holding
the rule-1 context partition; intent-record references were withheld until
these findings were durably written. Reviewed at HEAD `5f2e4c7`; the delta is
commit `bbfac7b` (its `docs/method/RECORD.md` and `CHANGELOG.md` hunks — the
roadmap and session hunks of the same commit were left unread per rule 2,
verified present by diffstat only).

## Load-bearing assumptions, named first

- **A1 — the config exists as described.** `ci.yml` runs the floor under
  `concurrency: group: floor-${{ github.ref }}`, `cancel-in-progress: true`.
- **A2 — cancellation is routine, not freak.** Parallel sessions pushing the
  same ref make cancelled conclusions a normal occurrence.
- **A3 — the remedy works.** A re-run of the cancelled run executes against
  the original SHA and yields a genuine pass/fail for that tree.
- **A4 — the right fix is a reading discipline, not a config change.** Rests
  on the claim that `cancel-in-progress` earns its keep.
- **A5 — a later commit's green covers your tree only if your commit is its
  ancestor.**

## Per-lens answers

### 1 — Approach & assumptions

The clause aims at a real failure mode and the right one: the surrounding
floor-at-head rule already demanded the pushed run's result, and a cancelled
conclusion is precisely the case where "the run finished" reads as compliance
while evidencing nothing. Point-of-use placement (a sibling bullet directly
beneath the floor-at-head clause) is the correct altitude.

- A1 **verified**: `.github/workflows/ci.yml` lines 59–62 carry exactly the
  described block.
- A2 **verified**: in the most recent 40 floor runs, 5 ended `cancelled` —
  four of them on 2026-08-09 alone. "As a matter of routine" holds.
- A3 **verified live** (see lens 2): the grounding incident's attempt 2 ran
  against the original SHA and returned success.
- A4 **holds in conclusion, not in its recorded grounds** — CR1.
- A5 sound, and carefully hedged ("reassuring", not "proof") — the
  whole-tree scanners mean a descendant's green genuinely covers the merged
  content.

The remedy carries one unexamined edge — CR2.

### 2 — Correctness & quality

The mechanism account is accurate: a queued run in the same group cancels
the in-flight one; the cancelled run's conclusion is `cancelled`, neither
pass nor fail; no result ever lands for the cancelled commit unless re-run.

**Re-run obligation discharged — the grounding incident reproduces in full
from the GitHub Actions history:**

- Recent-run window inspected via `gh run list` (full-SHA discipline
  observed). Run **31290845122** on
  `98a6f374ca94de1b31caaf3152a49baf5956f7d7` ("principles: §9 binds
  retrofits…" — the ruling commit): attempt 1 started 02:41:06Z, ended
  `cancelled` 02:42:50Z.
- The cancelling push: `00f6f593`'s run was created 02:42:47Z — **101 s
  after attempt 1 started**, with the cancellation stamped 3 s later. The
  clause's "~90 seconds" is a slight understatement (measured 101–104 s)
  but within an honest "~" — noted as CR6.
- Attempt 2: started 02:47:52Z, **success** 02:49:27Z, against the same SHA.
- `git merge-base --is-ancestor` confirms `98a6f374` **is** an ancestor of
  `00f6f593`, so the incident narrative's "the superseding green was true
  and did cover this tree" is itself correct.

Every factual element of the delta's account reproduces. Rule 4's
landing = queuing held structurally: the same commit's diffstat shows the
roadmap pointer landing with the work (content unread per the bar). The one
overclaim found is in the decision grounds, not the mechanism — CR1.

### 3 — Completeness / harvest

Other conclusions the all-clear can meet: `failure` and `timed_out` are
visibly red; `startup_failure` and `action_required` are rare and visibly
not green; `skipped` cannot arise here (no path filters or conditions on the
floor job). `cancelled` is the only conclusion that is both routine on this
ref and neither pass nor fail — special-casing it is coherent. The clause's
general sentence ("read the conclusion, never just 'the run finished'")
carries the rest of the family; a positive formulation would subsume them
all — CR4, note-level.

No duplication: `ECONOMICS.md` (§ CI minutes, "cost hygiene applies
regardless of meter") holds the config-side rule for `cancel-in-progress`;
this clause holds the reading-side discipline. They dovetail rather than
repeat. `CONCURRENCY.md` does not cover cancelled runs. One portability
gap — CR3.

### 4 — Security & privacy

Discharged in one line with grounds: the delta is markdown doctrine with no
execution surface, no secret handling, no personal data, and no private-repo
detail (the grounding anecdote names only "a parallel session"). Scanner
reach case: this is a landed-delta review with a clean tree — the house
pending-diff scanner has nothing it can read, and its exclusions bar
markdown documentation regardless, so a run would be definitionally empty
and was not performed.

## Findings

- **CR1 (MODERATE) — the un-build decision's recorded grounds contradict
  the workflow's own cost documentation.** The CHANGELOG entry (and the
  landing commit's message) justify "a reading discipline, not a config
  change" on `cancel-in-progress` "stopp[ing] a busy ref burning Actions
  minutes on superseded trees", the commit adding "those minutes are a real
  pool". But `ci.yml`'s own COST NOTE (lines 35–41) states public-repo
  Actions runs are free and that atelier's every-push economics exist
  *because* it is public — on this repo, cancelled runs save zero metered
  minutes. The decision itself survives on grounds the doctrine already
  holds — `ECONOMICS.md`'s "cost hygiene applies regardless of meter" — but
  the delta cites the metered-pool rationale, which is false for the repo it
  describes. A future session pricing a config change would read wrong
  economics from this record. *Counsel (labelled as such):* re-ground the
  sentence on the hygiene rule (and runner/queue concurrency, a shared pool
  even when free) rather than on minutes; conclusion unchanged.
- **CR2 (MODERATE) — the prescribed remedy can cancel the concurrent
  session's in-flight run.** A re-run attempt re-enters the same concurrency
  group (`floor-${{ github.ref }}`), and with `cancel-in-progress: true` a
  newly queued attempt cancels whatever is running — including the
  superseding commit's run if it is still in flight. The doctrine would then
  instruct *that* session to re-run, cancelling back. Practically: following
  this clause can silently destroy the other session's close evidence — the
  same harm the clause exists to prevent, now inflicted rather than
  suffered. Reasoned from the concurrency semantics, not live-exercised
  (exercising it requires mutating pushes, barred for this reviewer); in the
  grounding incident no collision occurred only because the newer run had
  completed ~3.5 minutes before the re-run. *Counsel:* one added sentence —
  re-run once the group is quiet (no floor run in flight on the ref).
- **CR3 (minor) — the config claim is stated unconditionally in doctrine
  that travels.** "The floor workflow runs under `cancel-in-progress: true`"
  is true of atelier's `ci.yml`; the reusable `floor.yml` children call
  declares no concurrency group, so whether a child's floor run can be
  cancelled depends entirely on its caller workflow. In a child without the
  block, the clause's factual premise fails (harmlessly — the discipline
  stays correct). *Counsel:* one conditional word — "where the floor runs
  under `cancel-in-progress` — as atelier's does —…".
- **CR4 (note) — negative enumeration where a positive rule is available.**
  "The all-clear is conclusion `success` on a run for your SHA" subsumes
  cancelled, timed-out, startup-failure and anything a future forge invents.
  The clause's general sentence gestures at this; stating it positively
  would close the family for good. Verified against the 40-run window: 35
  success, 5 cancelled, nothing else occurring in practice.
- **CR5 (note) — brief framing slightly off.** The brief locates the clause
  as "the sub-bullet under *When the close pushes…*"; structurally it is a
  **sibling** of that bullet, both nested under *The all-clear carries its
  evidence*. The point-of-use claim holds; recorded for pointer accuracy.
- **CR6 (note) — "~90 seconds" measured at 101–104 s.** Within an honest
  approximation; recorded because this repo's numeric claims have a history
  of drifting in both directions, and the run history gives the exact
  figure for free.

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR, 2 MODERATE, 1 minor, 3 note.**

The clause is aimed at a real, live-proven failure mode; every mechanism and
incident claim in it reproduced from the workflow config and the Actions run
history. The two MODERATEs are a mis-grounded decision rationale (CR1) and
an unexamined edge in the remedy (CR2) — neither undermines the discipline
the clause installs. Self-authored doctrine: nothing here is decided by this
reviewer; all findings are the principal's to rule on, counsel labelled
where offered.

## Follow-up checklist

- [ ] Principal rules CR1 — re-ground the un-build rationale, or accept the
      record as-is with the contradiction noted.
- [ ] Principal rules CR2 — add the group-quiet sentence, or accept the
      reciprocal-cancellation edge as tolerable at current push frequency.
- [ ] Principal rules CR3 — portability conditional, or scope RECORD.md's
      clause to atelier explicitly.
- [ ] CR4–CR6 — accept as notes or fold into whichever edit CR1–CR3 earn.
- [ ] Reviewer: reconcile section on receipt of the deferred intent-record
      references (below, when they arrive).

## Reconcile — post-verdict, intent record read (2026-08-09)

Deferred reference received and read: the ROADMAP item *"The floor-at-head
all-clear has a cancelled-run hole (found 2026-08-09)"* — that item only; the
rest of the roadmap and all other verdicts stayed barred. Phase-1 text above
is unrevised; everything below is post-reconcile.

**Agreements.**

- The intent record's account of the mechanism, the incident, and the
  point-of-use placement matches what the review verified independently.
  Its "a sub-bullet under the existing all-clear rule" is structurally
  accurate — the imprecision CR5 records was the *brief's* phrasing, not the
  intent record's. CR5 stands as written, aimed where it was aimed.
- "~90 seconds" appears in the intent record too; CR6 unchanged (measured
  101–104 s, within an honest "~").
- The watch item — a close-time probe that refuses to report green on a
  `cancelled` conclusion, left unbuilt pending recurrence — is the
  mechanised twin of CR4's positive rule ("only `success` on your SHA is an
  all-clear"). No divergence; noted so that if the probe is ever built, CR4's
  formulation is the spec it should implement. The one-instance-grounds-a-
  clause-not-a-build call is sound calibration and the review does not
  contest it.

**Divergences.**

- **CR1 nuance, status unchanged (MODERATE).** The intent record's wording
  is more defensible than the CHANGELOG's: it says "the **estate's** minutes
  are a real pool", which is true — private children meter. But the config
  the clause describes lives only in atelier's `ci.yml`, where runs are free
  by the file's own COST NOTE, and the reusable `floor.yml` children call
  declares no concurrency group — so whether any metered minute is actually
  saved depends on private callers' workflows, which neither the delta nor
  this review examined. The recorded grounds still overreach their evidence
  on the repo they describe; the decision still survives on `ECONOMICS.md`'s
  meter-independent hygiene rule. The principal's ruling on CR1 may
  reasonably prefer the intent record's estate-level framing as the
  replacement wording.
- CR2 (remedy can cancel the concurrent session's run) and CR3 (the config
  claim stated unconditionally in doctrine that travels) are not anticipated
  anywhere in the intent record. Both stand as written.

**Missed by phase 1, revealed by the record:** nothing that changes a
finding. The record's explicit `- [ ]` watch checkbox is the one element the
delta's in-scope files did not carry; it strengthens the delta's honesty case
(the unbuilt probe is tracked, not merely mentioned) and needed no finding.

**Post-reconcile status: no finding's severity or status changed.**
PASS-WITH-FINDINGS stands — 0 MAJOR, 2 MODERATE, 1 minor, 3 note.
