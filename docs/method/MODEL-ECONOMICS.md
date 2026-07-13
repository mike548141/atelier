# Model economics

*How to split work across models, how to keep a session token-efficient, and how
CI compute is metered. The doctrine is general; the estate-specific numbers —
which exact models, their prices, this operator's plan, the CI allowance and
session-overhead figures — stay person-local (see the pointer at the foot).*

## Match the model to the job

Two kinds of spend, drawn from two pools:

- **Plan-included** — a subscription's capable model. A token costs no marginal
  dollars but draws down a usage allowance.
- **Usage-billed** — billed per token, real money, output (including any
  always-on thinking tokens) costing several times input.

The split that follows from this: a **plan-included model does the *building*** —
iterating, tests, docs, exploration, the long agentic sessions, anything
mechanical or high-volume. Burning plan quota on exploration is fine; burning
real dollars on it is not. A **usage-billed model does *review*** — code, docs,
approach/assumptions, real-world validation — and the hard problem the building
model is stuck on. Reviews are **scoped and short** (hand it the diff / commit
range / named files, not the repo; ask for findings, not rewrites — apply fixes
back on the building model); builds are the bulk.

**Subagents for fan-out.** From either model, push broad reading/searching into
subagents so the expensive main context stays lean — most valuable in a
usage-billed session, where every main-context token is metered.

## Know which pool you're spending — the self-check

The subscription default is **not a reliable guard**: a model picker can save the
last choice as the new default, and a project/managed/IDE setting can outrank the
user default — so a session can silently come up on the usage-billed model even
when the plan model is pinned. The surfaces that always reflect the *real*
running model are the statusline and the model itself.

So the standing rule: **before token-heavy build/implementation work, state the
running model and its billing pool in one line; if it's the usage-billed model
and the task is a *build*, flag it and confirm before spending.** This catches
the "should have been on the plan model" case up front, when the fix is free
(switch at the session boundary), not after the dollars are gone. Review and
hard-problem work on the usage-billed model is the *intended* use — no flag
needed there. The guard is specifically usage-billed-doing-a-build.

## The compute pool — CI minutes

A **third spend pool** sits beside the two model pools above: **CI compute**,
metered by the forge (GitHub Actions) in **minutes**. Same "know which pool"
discipline, but its meter is coupled to something the model pools are not —
**repository visibility**:

- **Public repo → runs are free** — on standard hosted runners; larger/GPU
  runners bill even when public. A safety gate can fire on every push at no
  marginal cost.
- **Private repo → runs meter against a monthly allowance**, billed per job
  **rounded up to the whole minute** — so a 20-second job still costs a minute,
  and *run count*, not run *duration*, is the lever. Exhaust the allowance and
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
  is not value-free, though: a private repo's CI scans branch history at full
  cover, and that history publishes *wholesale* the day the repo goes public — so
  trimming the floor trades minutes now against unscanned history exposed at that
  flip.

So floor **frequency is a visibility-dependent trade** — genuinely two-sided, and
therefore *not atelier's to prescribe*. This doc names the coupling; the **call**
(how often a given repo's floor fires, whether to pay overage, which providers
sit on which plan) turns on estate-specific numbers atelier deliberately doesn't
hold — they live in the operator's **private estate-root repo** (its financial
inventory: providers, plan entitlements, free-vs-metered, one-off costs), decided
per repo there. Whatever the call, it obeys this file's precedence: **cost never
buys down safety** (see the closing section), and **publication is never
cost-driven** — a repo goes public on its own merits and free minutes are a side
effect, never the reason.

Cost hygiene applies regardless of meter: cancel superseded runs
(`concurrency: cancel-in-progress`), and prefer path filters over unconditional
triggers where a job guards only part of the tree. Self-hosted / cloud runners
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

## Triggering reviews — inline or batched, the building model's call

When economics allow, the building session may **spawn a review as a background
agent inline** — verify as you go, no context switch. When they don't, **queue a
batch** to run together later. Both are sanctioned; pick per cost and how
blocking the result is. Either way a review stays *scoped and short*, and it is
still spend — so it stays inside the "know which pool" rule above.

## Match the ceremony to the risk

Review gates, fresh-context sweeps, session breaks, and the *don't-stack* pause
below are all **spend** — reviewer tokens, a cold re-onramp, lost cache and
thinking continuity. Like every other cost they are optimised last but still
optimised: apply them **in proportion to the cost of being wrong**, not uniformly
to every change. Uniform ceremony is how a maturing repo's overhead-to-output
ratio quietly climbs — the per-change tax stays fixed while the work-unit shrinks,
until the meta-work crowds out the building.

- **Earns the full ceremony** (an independent, fresh-context review before the
  work is trusted): first-of-kind or structural tooling; anything with a
  **silent-failure mode** — a gate that can report green while not actually
  checking; **doctrine text**, because a wrong rule propagates everywhere it is
  inherited; and irreversible or public-facing actions.
- **Self-verifying — the mechanical floor *is* the review**: a change whose tests
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
4. **Watch context growth.** Long sessions get slower and costlier per turn.
   When a session feels long, write the record and restart — a standing practice,
   not a failure.
5. **Heavy skills are episodic costs.** A single skill/reference load can inject
   tens of thousands of tokens. Fine when needed; don't invoke speculatively, and
   especially not in a usage-billed session.
6. **Point, don't paste.** Give file paths and line ranges rather than pasting
   large content the model can read itself — reads are targeted and droppable;
   pastes live in the context forever.

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
