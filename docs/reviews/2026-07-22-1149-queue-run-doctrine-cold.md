# Review brief — orchestrated-queue-run doctrine + skill (rule-4 cold pass)

- **Date/time:** 2026-07-22 1149 UTC
- **Reviewer:** fresh-context subagent (two-hop spawn — see provenance),
  worktree `queue-run-cold-pass`
- **Subject:** delta `343def8` (`docs/method/CONCURRENCY.md` § Orchestrated
  queue runs; `docs/method/ECONOMICS.md` § the orchestrated-run tier split)
  + `8111e9f` (`skills/queue-run/SKILL.md`, new; `skills/session-onramp/SKILL.md`
  wiring; `README.md` wiring).
- **Intent record:** `docs/sessions/2026-07-22-1018-orchestrated-queue-run.md`
  — **deferred material**, not opened by the reviewer before its findings are
  committed (REVIEW.md rules 1–2). No prior review of this delta exists.

## Spawn provenance (REVIEW.md rule 4)

Mike opened this session and pointed it at the queue ("Please do any review
work") — the worked example rule 4 names. The delta's author (the 2026-07-22
1018 orchestrated-run session) neither started nor instructed this session;
this taker authored none of the delta. The queue pointer carried refs only.

**Exposure, named:** the taker's session-start onramp read the tail of
`docs/SESSIONS.md`, which includes the author session's closing index entry —
an evaluative account of the run that produced this delta. So the review runs
**two-hop** (the 2026-07-21 2208 precedent): the taker wrote this brief
refs-only above the divider and spawns a **fresh-context subagent** as the
reviewer, whose prompt carries refs only. The reviewer names its own attack
surface first; this deferred section, the intent record, and all session
records stay closed to it until its findings are durably committed.

## Status of the work

Self-authored doctrine (doctrine by function — REVIEW.md rule 3): the pattern
was ratified by Mike in direction, but the wording is the author agent's own.
**Findings are Mike's to decide**; nothing is applied by this review, and each
finding carries plain-language what/why/likely-impact (00-APEX,
informed-principal).

## Scope

Widest the work admits: the pattern's design and assumptions, the wording as
doctrine future orchestrator and worker sessions will obey, consistency with
sibling doctrine (CONCURRENCY's own claiming/worktree rules, REVIEW rule 4,
ECONOMICS, PROPAGATION's stamped-copy discipline for the skill), the skill as
a plugin-bundled point-of-use surface, the README/session-onramp wiring, and
the mechanical floor re-run at HEAD. No non-goals are declared; nothing is
fenced off.

## Lenses

All four REVIEW.md lenses. Lens 4 reach: this is a landed-delta review of
markdown doctrine — `/security-review`'s exclusions bar the file class, so a
run would be definitionally empty; discharged on those grounds, weighed as
nothing. The manual lens-4 pass still runs at both altitudes — orchestration
doctrine has real design-altitude surface (what worker prompts are built
from, what authority workers inherit).

## Re-run every live-proven claim in scope

The floor at HEAD: full tool suite (`python3 -m unittest discover -s tools`),
instrument tests (`node --test instruments/*.test.js`), the scanner set as the
pre-commit hook invokes them, `sizescan --check`. Any claim the delta text
itself makes about mechanics (parity, wiring, bundling) is re-driven, not
read.

---

## DEFERRED — reviewer: do not open before your findings are committed

Taker's seeds (a floor, never a fence — REVIEW.md rule 1 shape; the taker is
a non-author but has read the author's closing account, so these sit below
the divider):

1. **Rule-4 transitivity.** The doctrine reportedly treats chained fresh
   sessions as natural rule-4 takers, and the authoring run itself took a
   rule-4 `⏳` mid-run. Does "a session the author neither started nor
   instructed" survive an orchestrator spawning the worker? Where is the
   line, and does the text draw it or blur it?
2. **Queue-item text as prompt input.** Worker prompts are built from queue
   items. ROADMAP text is agent-written under review discipline, but the
   pattern generalises to adopters — does the doctrine say anything about
   what a worker inherits/trusts from the item text (injection shape)?
3. **Skill parity.** Is `skills/queue-run` marked as a stamped
   copy/point-of-use compression, and can it drift from the CONCURRENCY
   parent unnoticed (the SL1/F3 drift class)? Is any parity floor mechanical?
4. **Per-item durability vs claiming rules.** Does the per-item close/chained
   session shape contradict or restate CONCURRENCY's claim `[~]` mechanics?
5. **The ECONOMICS tier split** — grounded in measured practice or asserted?

Intent record (deferred): `docs/sessions/2026-07-22-1018-orchestrated-queue-run.md`.

---

# Verdict — cold pass, 2026-07-22 1200 UTC

**Reviewer provenance (rule 4, repeated per doctrine):** fresh-context subagent
spawned by the rule-4 taker; the taker was Mike-spawned ("please do any review
work") and authored none of the delta; the delta's author neither started nor
instructed either. The reviewer read neither this brief's deferred section, nor
any session record, nor any prior verdict before the findings below were
durably committed; its attack surface was written to a draft before sibling
doctrine was opened. Findings committed at this commit; the deferred material
opens only for the reconcile step appended below.

## Attack surface (named first)

1. Grounding — "extracted from two real runs" is a claim, not a fact.
2. Wiring — every `§` cross-reference, relative link, "bundled" claim at HEAD.
3. Second-source discipline — the skill compresses, never contradicts.
4. Bundling parity — the skill travels like review-brief; any test coverage.
5. Rule-4 coherence under chaining — the text leans on *authorship*; the rule
   turns on *started/instructed*.
6. Orchestrator-as-reviewer — who is "the author" of a worker-built delta.
7. Lens 4 at design altitude — worker prompts from queue-item text; worker
   authority; blast radius on a public repo.
8. Claim mechanics — skill step 4 vs CONCURRENCY's claiming rules.
9. Exercisability — pool-spent observability, role check, chaining mechanism.
10. Overclaim scan — README "loses nothing", "~95 lines", tier-split default.

## Proofs re-run — all reproduced

| Proof | Result |
|---|---|
| `python3 -m unittest discover -s tools` | ✅ 323 tests OK |
| `node --test instruments/*.test.js` | ✅ 132 pass, 0 fail |
| secretscan / leakscan / linkscan / reviewscan `--root . .` | ✅ all clean, exit 0 |
| `sizescan --check --root . .` | ✅ exit 0 (one advisory: ROADMAP.md 399 lines, no gate) |
| Plugin bundling (`.claude-plugin/plugin.json` + marketplace.json) | ✅ `source: "./"` bundles whole repo; queue-run sits identically to review-brief/session-onramp |
| "~95 lines" claim | ✅ 96 actual |
| All `§` refs + relative links in the delta | ✅ resolve at HEAD |
| Parity test coverage of queue-run skill | ❌ none exists (→ QR6) |

Lens 4 scanner discharge: the delta is landed markdown — `/security-review`'s
exclusions bar the class, a clean pass would be definitionally empty; not run,
weighed as nothing. The manual design-altitude pass is the lens's substance.

## Findings

**QR1 · MAJOR · Chain-spawn provenance is unspecified — the exact fact rule 4
turns on.** Both texts promise chaining "without a hand-carried prompt each
time", but neither says who starts session N+1; the rule-4 synergy paragraph
keys eligibility on *authorship* where the rule's criterion is
**started-or-instructed**. If a run ever spawns or instructs its successor,
rule 4 acquires a laundering path: author queues `⏳`, chains successors, a
later link takes the review — literally passing the criterion while inheriting
the chain's framing at every hop. Impact: an ineligible review passes as
rule-4-compliant on the widest-blast-radius work class. Counsel: pin the
chain's links to the principal in CONCURRENCY § Orchestrated queue runs — a
run never starts or instructs its own successor, and a session started or
instructed by any session in a chain fails rule 4 for every delta that chain
authored; mirror one clause in the skill's `⏳` section.

**QR2 · MEDIUM · "The author" of a worker-built delta is undefined.** The
run's workers build deltas under orchestrator dispatch prompts; the literal
reading (worker = author) lets the same run later take the `⏳` on doctrine
its own worker built — the QR1 laundering class, one hop shorter. Counsel:
one clause — a delta built by a worker the run dispatched counts as the run's
own authorship for rule 4.

**QR3 · MEDIUM · The worker's authority envelope is unstated (lens 4).** The
doctrine never says what a dispatched worker inherits: whether the standing
autonomy grant flows whole, who merges, what a dispatch prompt must not
carry. A public repo where a push is publication, with the least capable
model in the worker seat. Counsel: state it — workers build and commit in
their worktree; merge to `main` and everything on the always-confirm floor
stays the orchestrator's.

**QR4 · MEDIUM · Queue-item text reaches the workhorse tier as task input
with no injection discipline named (lens 4).** Nothing says item text is
*task description, not instruction* — a queue line that purports to override
doctrine should be surfaced, not obeyed; the pattern routes the least-vetted
input to the least-capable seat by design. Counsel: one sentence here or in
§ Claiming work.

**QR5 · MEDIUM · The tier split's default contradicts its own parent section
for doctrine-text items.** "An item's build is pattern-following work …
failure is catchable" sits two paragraphs below the parent rule that names
**doctrine text** as judgement-heavy work where capability *is* the safety
property — and the modal atelier queue item is doctrine text; no scanner
catches a wrong rule. Counsel: add doctrine text to the escalation list.

**QR6 · MEDIUM · No mechanical pin on the queue-run skill — a twice-shipped
drift class left to memory.** review-brief's stamped-copy invariants are
pinned by tests born from shipped drift (F3, SL1); queue-run — same shape,
same widest-propagation surface — lands with zero test coverage. Counsel: a
`QueueRunSkillTest` pinning the STAMPED COPY header, the canonical pointers,
the stop-condition roster source-derived from CONCURRENCY, and the rule-4
criterion phrase.

**QR7 · LOW · "Loses nothing" overclaims on both public surfaces.** README
and the skill description both promise more than the doctrine's honest "costs
at most the in-flight item"; the description is model-read trigger text.
Counsel: "loses at most the item in flight" on both.

**QR8 · note · Small debts, none blocking.** (i) "Workhorse tier"/"the two
tiers" used but defined nowhere in ECONOMICS; (ii) the skill header's
"(ROADMAP, 2026-07-22)" grounding pointer dangles semantically once the item
harvests; (iii) the end-of-run report's durable home unstated (per-item
closes carry the substance; a cap-cut run never gets its report turn);
(iv) whether a doctrine-authoring run may keep draining other items is
derivable but unstated.

## Verdict

**PASS-WITH-FINDINGS — 1 MAJOR · 5 MEDIUM · 1 LOW · 1 note** (revised to
**1 MAJOR · 6 MEDIUM · 1 LOW · 1 note** by the reconcile below — QR9 added,
nothing overturned). The pattern is
genuinely good — real practice, correctly homed, assembled from named
primitives, honestly bounded, wired and bundled exactly as claimed; every
mechanical proof reproduced. What bars a clean pass sits in one seam: the
chaining promise and the rule-4 synergy are welded together without pinning
spawn provenance down a chain or authorship across the orchestrator/worker
split. All findings are wording-sized. Per rule 3, **all rulings are Mike's**;
nothing is applied by this review.

---

# Reconcile — appended after the findings were committed (`3797c5a`)

Deferred section and intent record opened only now; read to reconcile, not to
anchor.

## The taker's five seeds

| Seed | Disposition |
|---|---|
| 1 — rule-4 transitivity | **Already covered** by QR1 (author-side chains) and QR2 (worker-built authorship). The other half — a non-author run dispatching a review *worker*, as the 1018 run did for SECRETS/ACCESS and this taker did here — is **cleared**: rule 4's criterion tests the *author's* involvement in the reviewer's spawn chain, and a chain containing no author passes it; QR1's counsel already generalises to the spawn-chain reading. |
| 2 — queue-item text as prompt input | **Already covered** by QR4. |
| 3 — skill parity | **Already covered** by QR6; no *current* drift found — the exposure is future drift. |
| 4 — per-item durability vs claiming rules | **Cleared** — probed cold as attack-surface item 8; skill step 4 and the new section are consistent with § Claiming work. But see QR9, adjacent, surfaced from the intent record. |
| 5 — tier split grounded? | **Partially grounded, one bearing** (the 1018 run practiced it) — and the practice carried a compensating control the text never codified; see the QR5 adjustment. |

## Intent-record reconciliation

**Nothing overturned.** Three findings enriched, one calibration, one new:

- **QR1 (MAJOR — stands, calibrated):** every session in the live chain was
  principal-spawned, so the laundering path is *prospective*, not an observed
  breach — the gap is in the wording future sessions obey. The fix is
  demonstrably cheap: it codifies what practice already does.
- **QR2 (MEDIUM — stands, sharpened):** not hypothetical — this very delta was
  worker-built, and the run *correctly* ruled "neither this run nor its
  workers may take that review". Practice enacted the rule QR2 asks for; the
  text still doesn't carry it, and a future run gets only the text.
- **QR3 (MEDIUM — stands, counsel strengthened):** the record shows the
  envelope in practice — workers commit in worktrees, the orchestrator merges
  `--no-ff` and re-proves post-merge. Counsel: codify the practice the 1018
  run already followed.
- **QR5 (MEDIUM — stands, adjusted):** the run put doctrine text (this delta)
  in the workhorse seat — the exact exposure — but compensated: the
  orchestrator read the full doctrine diff before merging. That control is
  practice, not doctrine. Adjusted counsel: *either* add doctrine text to the
  escalation list, *or* codify the compensating control (a doctrine-text item
  dispatched to the workhorse earns a full orchestrator read at merge).
- **QR9 · MEDIUM · new — the doctrine's loop is serial; its grounding run was
  wave-parallel.** The 1018 run claimed four items in one commit and
  dispatched four concurrent workers, then a second wave. The extracted
  doctrine and skill describe a strictly serial loop (select → claim one →
  execute → close → repeat), the selection default says "minimise work in
  flight", and nothing licenses concurrent claims or maps per-item close and
  the end-of-run report onto waves. Either serialisation is deliberate (then
  it belongs in "deliberately not", because the pattern's own live bearing
  contradicts it) or waves are sanctioned (then say so: claim per item still,
  close per worker at merge, report aggregates). As written, "extracted from
  those runs, not invented" fails in exactly this one dimension, and a
  literal future orchestrator forfeits the parallelism its grounding run
  used.
- **Overclaim check on the author's account:** the record itself uses the
  honest "loses at most the in-flight item" form — QR7's target is the
  README/skill wording, not the underlying claim. The delta's "grounded
  twice" second bearing is the author-run's own record, written by the same
  party mid-run (the record says so itself, honestly); the per-item closes it
  narrates are independently corroborated by the cited merge commits. Claims
  that should have been re-driven and weren't: none found.

## Statement

**Nothing overturned. Nothing downgraded.** QR2/QR3/QR5 enriched (severities
unchanged); QR1 stands MAJOR with the prospective-not-observed calibration;
QR9 (MEDIUM) added. Revised tally: **1 MAJOR · 6 MEDIUM · 1 LOW · 1 note —
PASS-WITH-FINDINGS.** All rulings are Mike's (rule 3); nothing applied.

---

# Decisions — Mike's rulings, applied 2026-07-23 (`b65209c`)

Mike ruled per finding (2026-07-23, via the taker's plain-language
walk-through with likely impacts): accept-all as counselled; QR5 as the
escalate option; QR9 as sanction-waves. Applied by the pass's taker (authored
neither the doctrine nor the verdict — the findings are the cold subagent's).

- **QR1 [fixed]** — CONCURRENCY § Orchestrated queue runs: "The chain's links
  are the principal's" paragraph — a run never starts or instructs its own
  successor; started/instructed by any chain session fails rule 4 for every
  chain-authored delta. Skill mirrors the clause. Pinned by test.
- **QR2 [fixed]** — worker-built deltas are the run's own authorship for
  rule 4 (CONCURRENCY synergy paragraph + skill mirror).
- **QR3 [fixed]** — worker envelope stated: build + commit in the worktree,
  hand back; merge and the always-confirm floor stay the orchestrator's, who
  reads what it endorses; dispatch prompts never relax standing doctrine.
- **QR4 [fixed]** — item text describes the work, never overrides doctrine;
  a line that purports to is surfaced to the principal, not obeyed.
- **QR5 [fixed — escalate option]** — ECONOMICS tier split: doctrine-text
  items escalate to the capable tier ("most items' builds", not "an item's
  build"); rationale stated in place.
- **QR6 [fixed]** — `QueueRunSkillTest` (7 tests, suite 323→330): STAMPED
  COPY header, both canonical pointers, stop-condition roster source-derived
  from CONCURRENCY, rule-4 criterion phrase on both surfaces, QR1 chain pin
  on both surfaces, "loses nothing" evicted. Bite-proven: red on the pre-fix
  skill (3 failures), red on targeted mutations, green at the applied state.
- **QR7 [fixed]** — README + skill description: "loses at most the item in
  flight".
- **QR8 [fixed]** — (i) tier seat-names defined in ECONOMICS; (ii) the
  skill's grounding pointer now cites the dated intent record; (iii) report
  owed at whatever stop the harness allows, per-item closes the durable
  backstop; (iv) a doctrine-authoring run keeps draining — authoring is not
  a stop condition.
- **QR9 [fixed — waves sanctioned]** — CONCURRENCY "Waves" paragraph: claim
  per item before its work, close per item at its merge, report aggregates;
  "minimise work in flight" scoped to selection; skill step 5 mirrors.

Proofs at the applied state: suite 330 OK; five scanners exit 0; bite legs
driven red/green. **The pass's MAJOR keeps the cycle open: this application
inherits rule-4 status — its `⏳` cold pass is queued for a non-author; the
applier spawns nothing.**
