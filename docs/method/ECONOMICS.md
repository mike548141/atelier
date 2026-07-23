# Economics

*How to split work across models, how to keep a session token-efficient, and how
CI compute is metered. The doctrine is general; the estate-specific numbers —
which exact models, their prices, this operator's plan, the CI allowance and
session-overhead figures — stay person-local (see the pointer at the foot).*

## Match the model to the job

Billing state belongs to the **marginal token**, not the model. A plan can move
the same model between states over time (it has — 2026-07), so read the state
off the current plan, never off habit. Three states:

- **Plan-included** — draws down a usage allowance; no marginal dollars.
- **Plan-included, capped** — included only up to a share of the allowance;
  past the cap the *same model's* next token silently becomes usage-billed.
- **Usage-billed** — billed per token, real money, output (including any
  always-on thinking tokens) costing several times input.

Two refinements the states force:

- **Draw-down rate.** Within the plan pool, models are not equal: a premium
  model draws the shared allowance several times faster. "No marginal dollars"
  is not "free" — what the premium model drinks, the bulk work can't.
- **Billing prices the seats; risk assigns them.** Which tier reviews and which
  builds is *One doctrine, tiered authority*'s call (below), made on risk —
  never this section's. This section only prices the assignment: **building —
  iterating, tests, docs, exploration, the long agentic sessions, anything
  mechanical or high-volume — belongs on the cheapest-drawing tier that
  genuinely does it**, because burning allowance on exploration is fine where
  burning real dollars (or premium draw) is not; **review and the hard problem
  the building model is stuck on belong to the capable tier**, whatever billing
  state the plan currently serves it in. Reviews are **scoped and short** (hand
  the reviewer the diff / commit range / named files, not the repo; ask for
  findings, not rewrites — apply fixes back on the building model); builds are
  the bulk.

## Sub-agents — isolation, not savings

A sub-agent runs in its own context and returns only its final report; the main
session carries that report, not the reading that produced it. Two corrections
to the intuition that this "saves tokens":

- **It buys context isolation, not token savings.** A sub-agent re-pays its own
  fixed overhead — its own system prompt and tool schemas — and often spends
  *more* in total than doing the work inline: more allowance drawn on a
  plan-included session, more dollars on a usage-billed one. What it buys is
  that every *subsequent* main-session turn is cheaper and sharper: the main
  context stays lean, the cached prefix stays small and stable, and
  long-context quality decay is deferred. The payback therefore scales with
  the work *remaining ahead* — every later turn re-carries whatever entered
  the main context, so delegation pays most with many turns still to come, is
  pure overhead with few, and bites hardest where every main-context token is
  metered. One caveat from item 3 below: a sub-agent that runs past the cache
  TTL idles the main session into a cache re-write — the durable win is the
  lean, stable prefix, not cache warmth.
- **The report is all that survives.** A sub-agent's return is lossy by design.
  Where the task needs the *raw* detail — the exact file content an edit
  depends on, the precise error text — delegating trades correctness for
  context, and that trade loses.

When to reach for one: **fan-out** — searching or reading across many files
where only the conclusion needs to come back; **parallel independent slices**
that share no state; and **fresh-context verification** — the inline
background review of *Triggering reviews* below. Fresh context alone is not
independence, though: the spawn prompt is a brief, usually the author's, so
the independence rules bind in full — seeded questions deferred, the
reviewer's own attack surface committed first — per `REVIEW.md`,
*Independence is more than fresh context*. Self-authored doctrine goes
further: there the spawn itself must be cold — the review comes from a
session the author neither started nor instructed (REVIEW rule 4). Fan-out
is also where tier
selection bites: mechanical reading is pattern-following work, so delegate it
to the cheapest tier that genuinely does it — which softens the total-cost
correction above. When not: a single known lookup, where the overhead
exceeds the read; tightly iterative loops, where the hand-off tax repeats every
round; anything whose correctness turns on detail a report would drop. Two
disciplines: once delegated, don't also do the work inline — pick one; and take
the *conclusion* into the main context, never the transcript — over-asking a
sub-agent is cheap, over-carrying its output is not.

## Know the marginal cost of the running model — the self-check

The subscription default is **not a reliable guard**: a model picker can save the
last choice as the new default, and a project/managed/IDE setting can outrank the
user default — so a session can silently come up on the dearest model even
when a cheaper one is pinned. The surfaces that always reflect the *real*
running model are the statusline and the model itself.

So the standing rule: **before token-heavy build/implementation work, state in
one line the running model, its billing state, and — for a capped model — the
distance from its cap; flag and confirm before spending when a guard trips.**
Where no surface reports cap distance, *unknown* trips the guard — flag and
confirm before heavy spend, or consult the plan's usage surface first; fail
toward confirmation, never toward silence.
Two guards:

- **A usage-billed or premium-draw model doing a *build*** — bulk work on the
  dearest meter. This catches the "should have been on the cheaper tier" case
  up front, when the fix is free (switch at the session boundary), not after
  the spend is gone.
- **A capped model near its cap** — past the cap the next token is real money
  with no visible switch. Capacity with billing attached **fails open** (the
  CI-minutes pattern below): nothing breaks, it just silently bills.

Crossing a cap into usage billing is spend beyond the plan, so it sits under
the standing confirmation floor (`AUTONOMY.md` — spend): at the cap the session
stops at a safe point, records, and hands the principal the choice — **delay
the work, or pay**. What the cap never does is move the work down-tier: tier
selection is risk's call alone (next section), and an empty tank is not a risk
argument. Review and hard-problem work on the capable tier is the *intended*
use — no flag for that; the guards are bulk-work-on-a-dear-meter and
silent-cap-crossing. (Grounded 2026-07-23, Mike: "we never decay the quality or
integrity of the work because the tank is low, we either stop/delay the work or
I choose to pay usage fees.")

## The compute pool — CI minutes

**CI compute** sits beside the model spend above, metered by the forge
(GitHub Actions) in **minutes**. Same know-the-marginal-cost
discipline, but its meter is coupled to something the model billing states are
not — **repository visibility**:

- **Public repo → runs are free** — on standard hosted runners; larger/GPU
  runners bill even when public. A safety gate can fire on every push at no
  marginal cost.
- **Private repo → runs meter against a monthly allowance**, billed per job
  **rounded up to the whole minute** — so a 20-second job still costs a minute,
  and *run count*, not run *duration*, is one lever; **runner class** (below) is
  the other, and often the larger. Exhaust the allowance and
  behaviour splits: at a zero spending-limit CI **fails closed** on a capacity
  error (not a broken workflow — an empty tank; report it as such, don't debug
  the YAML); with billing attached it **fails open** and silently bills overage
  (the surprise-invoice case).

The useful part is the coupling: the *same visibility flip* moves the safety
rationale and the meter together.

- **A push to a public repo *is* publication** — so a publish-safety floor gates
  every push *and* that push is free; rationale and cost align. (This is why
  atelier's own floor runs on every branch — `.github/workflows/ci.yml`.)
- **A push to a private repo is *not yet* publication** — the world can't see it,
  so every-push is a **backstop** over the pre-commit hook (catching a
  `--no-verify` bypass or a hook-less clone), bought with *metered* minutes. It
  is not value-free, though: CI re-scans the whole *tree at each pushed tip*
  (per-commit cover is the hook's job, not CI's — the scanners read the tree, not
  the log), so every-push covers the tip of every feature branch — trees that
  publish *wholesale* the day the repo goes public. Trimming the floor to
  main-only leaves those feature tips unscanned until that flip.

So a floor's **trim-down is a visibility-dependent trade** — genuinely two-sided,
and therefore *not atelier's to prescribe* (the safe every-push default is;
trimming it is the estate's call). This doc names the coupling; the **call**
(how often a given repo's floor fires, whether to pay overage, which providers
sit on which plan) turns on estate-specific numbers atelier deliberately doesn't
hold — they live in the operator's **private estate-root repo** (its financial
inventory: providers, plan entitlements, free-vs-metered, one-off costs), decided
per repo there. Whatever the call, it obeys this file's precedence: **cost never
buys down safety** (see the closing section), and **publication is never
cost-driven** — a repo goes public on its own merits and free minutes are a side
effect, never the reason.

### Runner class — the multiplier lever

A minute is not a minute. The forge meters each runner **class** at a different
per-minute rate, so *which* runner a job picks multiplies its cost before run
count is even counted. On GitHub's standard hosted runners the multipliers are
**Linux 1× · Windows 2× · macOS 10×** (larger/GPU runners bill higher still, and
**bill even on public repos** where standard runners are free). A private repo
running its whole suite on macOS burns its allowance **ten times** as fast as the
same suite on Linux — usually for no portability gain, because lint, type-check,
build and most tests are platform-independent.

The rule: **each repo uses the cheapest runner class that genuinely does its
work.** Default every job to Linux. Escalate to a dearer class *only* for the
specific slice that truly exercises that platform — and isolate that slice in its
own job so the multiplier lands on the minimum surface, never on checks that
would pass identically on Linux.

- **Single-platform repo** → all jobs Linux. No exceptions to reach for.
- **Multi-platform repo** → Linux for everything portable (lint, type-check,
  build, the platform-agnostic tests), and a **narrow** macOS/Windows job for
  only the OS-specific code paths. The worked case is `ros`: multi-platform by
  design, so Linux carries the whole pipeline except the two `tiki` pieces that
  are genuinely macOS-specific, which alone touch a macOS runner.

A full `os: [ubuntu, macos]` matrix across *every* job is the anti-pattern this
trims: it re-runs platform-independent checks at 10× for a portability claim
they don't actually test. The build-layer templates default to Linux for this
reason; a macOS/Windows job is added deliberately, scoped to its slice.

Cost hygiene applies regardless of meter: cancel superseded runs
(`concurrency: cancel-in-progress`), prefer path filters over unconditional
triggers where a job guards only part of the tree — never the publish-safety
floor itself, though: a whole-tree scan must see the whole tree — and avoid
**duplicate triggers**: an unfiltered `push` plus `pull_request` fires *twice*
per push on a branch with an open PR, so scope `push` to the branches that need
it (as the CI templates do) unless the second run genuinely earns its minutes —
scanning the merge preview a tip-push can't see, or covering fork PRs that never
raise a `push` event in the base repo. Self-hosted /
cloud runners
(e.g. AWS) take the work off the forge meter entirely — a known future option,
held for a deliberate decision, not reached for unprompted.

## One doctrine, tiered authority — not tiered rules

Every model runs the *same* doctrine (00-APEX "who it binds"). What scales with
capability is **authority over live/irreversible systems**, not which rules
apply. Match the model to the task's *risk*: pattern-following work runs on a
cheaper model; a **mechanical gate (validators/CI) holds the floor regardless of
which model ran** — that is what makes cheap-model work safe; first-of-kind or
structural work escalates to the capable model, and a smaller model that hits it
**logs and hands up** rather than improvising past its depth.

Within that risk frame, tier selection is the runner-class rule above applied
to models: **the cheapest model that genuinely does the work, at the quality
the work needs.** "Cheapest" is judged against the marginal token's billing
state and draw-down rate (the states that open this doc), because the meters
differ — a plan-included capable model can cost fewer marginal dollars than a
usage-billed small one. Read the billing state first,
then pick the tier within it. "Genuinely does" is a verifiability test, not
optimism: cheap-model work is safe where failure is *catchable* — a validator,
a test suite, a gate — because the floor converts a capability gap into a
caught failure instead of a shipped one. Where failure would be silent or the
work is judgement-heavy — doctrine text, review verdicts, structural design —
capability *is* the safety property; pay for it. Above all, price the *job*,
not the token: a dearer model that completes the work in fewer turns, retries
and re-reviews is often the cheaper way to get it done — per-token rates
compare models, but only cost-to-done compares outcomes. The rework rule is
the same truth seen from the failure side: a cheap attempt that fails and is
redone on the capable model costs more than starting capable, so when a
hand-up looks likely, escalate up front.

Two hard edges on the ladder (both grounded 2026-07-23, Mike):

- **Capacity never picks the tier.** "Cheapest that genuinely does the work" is
  judged on the work's risk and verifiability — in *every* capacity state. A
  cheaper model is welcome wherever that test passes, cap or no cap; it is
  forbidden as a *response* to a low allowance. When the tank can't fund the
  tier the work needs, the exits are stop/delay or principal-authorised spend
  (the cap rule above) — never a quieter model doing louder work. Cost is the
  lowest precedence, and an exhausted allowance doesn't promote it.
- **Hand-ups are noisy, and the ladder ends at the principal.** "Logs and hands
  up" means *fails visibly*: stop improvising, state what was attempted and
  where the work exceeded the model's depth, record it (session log / queue),
  and route the work up — workhorse → capable tier → **principal**, when every
  tier is out of its depth. A silent stall, or a plausible-but-degraded
  attempt, reads as progress and blocks the hand-up — the shipped-failure mode
  the mechanical floor exists to prevent. "This exceeds me" is a report the
  apex's honesty burden requires, not a failure it punishes.

### The orchestrated-run tier split

The rule above, applied to the queue-run rhythm (`CONCURRENCY.md` §
Orchestrated queue runs): a run's two seats map to the two tiers — seat names
for the spectrum above: the **capable tier** is the most capable model
available; the **workhorse tier** is the run's *default executor slot*, filled
per run by the cheapest model that genuinely does *the items' builds* (judged
on the run's modal item). The seat is a slot and the rule fills it — which is
what lets fan-out sit *below* it on a different work class, and the executor
trial step a slot down (2026-07-23, QR8; EB6/QA6). **The capable
tier orchestrates and reviews** — selection, dispatch, the review verdicts and
the structural judgement calls at merge are exactly the judgement-heavy,
silent-failure-prone work this section says to pay capability for. **The
workhorse tier executes** — most items' builds are pattern-following work under
a mechanical floor (the scanners, the test suite), which is where a cheaper
model is safe because failure is *catchable*. So the run spends the expensive
tier where its marginal value is highest and lets the cheap tier carry the bulk
— the "cheapest model that genuinely does the work" rule reaching its natural
shape across a chain of items. **Flex on judgement is allowed:** an
orchestrator may execute a small item inline rather than dispatch it, and a
first-of-kind, structural, **or doctrine-text** item escalates to the capable
tier per the rework rule above (a hand-up that looks likely is taken up front;
doctrine text because no scanner catches a wrong rule — this section's own
"pay for capability" example, and the modal atelier queue item; 2026-07-23,
QR5). The split is the default, not a
fence. The marginal-cost self-check still runs at whatever
seat a session takes — the **role check** `CONCURRENCY.md` mandates at run-open
*is* that self-check applied to orchestration: a session on the wrong tier for
its role stops and says so, when the fix (switch at the session boundary) is
still free.

The two seats are not the whole ladder (adopted 2026-07-23, Mike). **Fan-out
delegates below the workhorse**: the mechanical reads, searches and scans a
session hands to sub-agents are pattern-following work whose report the parent
verifies, so they run on the cheapest tier that genuinely does them — the
*Sub-agents* tier note made standing practice, and the good kind of
down-tiering: chosen because the work's risk permits it, true in every capacity
state, never a response to a low tank. And the **executor seat may step down a
tier for routine, well-floored items** — trialled per run, kept only when the
floor's evidence (scanners, tests, the orchestrator's review) shows the tier
genuinely does that class of work; extraction-from-practice applies to tier
claims as much as to doctrine.

## Triggering reviews — inline or batched

When economics allow, the building session may **spawn a review as a background
agent inline** — verify as you go, no context switch. When they don't, **queue a
batch** to run together later. Both are sanctioned for routine work; pick per
cost and how blocking the result is. The exception is self-authored doctrine:
there the spawn must be a non-author's, whichever path the economics favour
(REVIEW rule 4). Either way a review stays *scoped and short*, and it is
still spend — so it stays inside the marginal-cost self-check above.

## Match the ceremony to the risk

Review gates, fresh-context sweeps, session breaks, and the *don't-stack* pause
below are all **spend** — reviewer tokens, a cold re-onramp, lost cache and
thinking continuity. Like every other cost they are optimised last but still
optimised: apply them **in proportion to the cost of being wrong**, not uniformly
to all work. Uniform ceremony is how a maturing repo's overhead-to-output ratio
quietly climbs — the per-unit tax stays fixed while the work-unit shrinks, until
the meta-work crowds out the building. (What counts as a unit here is a
*commitment*, not a diff — `REVIEW.md` owns that trigger; a design earns the
proportionality test the same way built work does.)

- **Earns the full ceremony** (an independent, fresh-context review before the
  work is trusted): first-of-kind or structural tooling; anything with a
  **silent-failure mode** — a gate that can report green while not actually
  checking; **doctrine text**, because a wrong rule propagates everywhere it is
  inherited; and irreversible or public-facing actions.
- **Self-verifying — the mechanical floor *is* the review**: work whose tests
  and dogfooding exercise it end-to-end over *already-reviewed* machinery. Wiring
  an already-reviewed tool into a gate, a refactor its suite fully covers, a
  records-only edit — these do not each earn a brief→verdict cycle. Demanding one
  is the overhead, not the safety.

**What *don't-stack* actually covers.** The rule is narrow: *do not build a gate
on top of unreviewed tooling or doctrine* — a gate is only as trustworthy as the
thing behind it, so that thing earns its review first (why a new scanner is
reviewed before it is wired into CI). It is **not** a ban on doing several
related, already-grounded things in one session. The trigger is an *unreviewed
dependency* between two pieces of work; mere sequence is not one.

## Session hygiene (both models)

The prompt cache is **per-model** and the whole context is resent every turn, so
context size and continuity are the levers:

1. **One task per session — but a task is a coherent *line* of work, not a single
   checkbox.** The cost is *pivoting to an unrelated task*: that drags the old
   task's tokens along every turn for no benefit. Related, already-grounded work
   sharing the same context is the *same* task — keep going through it. Break for a
   genuine reason (an unrelated pivot, a decision only the principal can make, a
   real unreviewed dependency, or context/cache degradation), **not because one
   item went green**. Then wrap up (write the session record) and start fresh.
2. **Never switch model mid-session.** The cache is per-model — a switch
   re-processes the entire context at full input price and loses the prior
   model's thinking continuity. Switch at session boundaries.
3. **Mind the cache TTL.** A prompt cache expires after a few minutes; a gap
   longer than that re-writes it (a full input re-read). Cache *writes* cost more
   than cache *reads*, so churn is the expensive pattern — it bites hardest on a
   usage-billed session.
4. **Watch context growth — and reset by record, not by compaction.** Long
   sessions get slower and costlier per turn, and the harness signals it
   (context meters, auto-compaction warnings). Heed the signal, don't chase a
   number — thresholds are harness- and plan-specific, and the cost is linear
   the whole way. The standing reset is **write the session record and restart
   fresh**: the record is this method's compaction — deliberate, curated,
   versioned, and doubling as the institutional memory (`RECORD.md`). An
   in-place compaction (the harness summarising the conversation for itself) is
   the lossy fallback for a mid-task rescue, not the practice; a bare context
   wipe is fine only *after* the record is written. (In today's harness those
   are `/compact` and `/clear`; mechanism names change, the order doesn't —
   record first, then reset.)
5. **Heavy skills are episodic costs.** A single skill/reference load can inject
   tens of thousands of tokens. Fine when needed; don't invoke speculatively, and
   especially not in a usage-billed session.
6. **Point, don't paste.** Give file paths and line ranges rather than pasting
   large content the model can read itself — reads are targeted and droppable;
   pastes live in the context forever.
7. **Surface the boundary — and stop safely under overload.** A session boundary
   is often the principal's call, not one to cross silently. When the economics
   point to a fresh session — context degrading, cache churn, a genuine pivot —
   *say so* rather than press on into a slow, costly context or start anew
   without a word. And when handed more work than one session can carry well,
   don't push a degrading context to the end of the list: use the economics to
   pick a **safe stopping point**, write the record, put the work away, and hand
   the remainder to a fresh session. A clean handoff of half the list beats a
   muddy completion of all of it — item 1's "one task per session" seen from the
   overload side. (Grounded 2026-07-20, Mike.)

Keep the every-session read path lean: **bulk — completed detail, append-only
logs, verbose specs — does not accumulate in the docs a session loads at start**
(split it out, tail-read or grep on demand). The cost is linear, not a cliff, so
never sacrifice clarity to hit a number; the rule is only that bulk stays off the
hot path.

## Cost is the lowest precedence

Cost is optimised **last** (see PRINCIPLES' precedence ladder) — never by
weakening honesty, safety, or correctness. A cheaper session that ships a wrong
or unsafe result saved nothing.

---

*Person-local (kept in the operator's repo / machine, not here): the exact model
roster and their pools, current per-token prices and cache multipliers, the
CI-minutes allowance and per-minute overage price, the rules-of-thumb constants
(chars-per-token), and the measured fixed per-session overhead. Those are plan
details and change with pricing; this doctrine does not.*
