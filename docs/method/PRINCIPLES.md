# Design principles — the doctrine every build is measured against

The design doctrine for all technical work. A build that violates one of these
**without a stated, deliberate reason is a defect, not a style choice.** They
overlap on purpose — grouped so the overlaps reinforce rather than repeat — and
each carries a *generalised case* so it stays actionable, not abstract. (A
principle stripped of its cases is theatre; the cases are what make it teachable.)

**The apex (§0) sits above all of this** — honesty is absolute, then the Laws.
It is canonical in [`00-APEX.md`](00-APEX.md) and is **not** on the precedence
ladder below: it is never traded against a design goal; it bounds the whole
ladder. What follows resolves collisions *among* the design principles §1–7.

*Estate/product-specific bearings and the decided review case-law live in the
child repo that produced them (e.g. `ros`); this file is the general statement
they point up to. Children point up; the parent never points down for truth.*

## 1. Resilience — degrade, don't collapse

Keep the core job running when a part fails, is slow, or is unreachable. Partial
service beats total failure.

- **Graceful degradation.** Maintain reduced/partial function instead of failing
  whole. *Case:* a batch operation that refused the *entire* run when one target
  failed — so a single unreachable node blocked maintaining every healthy one —
  is the motivating anti-pattern. The fix: the ones that can proceed do; the ones
  that can't are skipped and reported loudly.
- **Fault isolation / bulkhead.** Compartmentalise so a failure in one partition
  can't cascade — per-unit error isolation, separate sessions, a bad input for
  one item never sinks the others.
- **Circuit breaker.** Detect a failing/hanging dependency, stop calling it fast,
  return a fallback rather than blocking. A wedged dependency is skipped on a
  timeout, never waited on indefinitely.
- **Fail-safe by design.** The state a component lands in *on failure* is the
  safe one — wipe-to-known-good, quarantine the unknown, default destructive
  actions to deny.
- **Fail-fast on bad input.** Reject corrupt/invalid data at the edge, before it
  propagates — strict schema, canonicalising validators, so a typo fails locally
  and never silently downstream. *The tension worth naming:* fail-fast on **our**
  bad data at the edge; degrade gracefully on a **remote peer's** failure. Both,
  at the right layer.
- **Design the unhappy path too.** Every feature specifies what happens when the
  dependency is offline, the field missing, the write rejected, the secret won't
  decrypt — not just the happy path. Half the value of an approach review is
  catching a happy-path-only build.
- **Build the way back before the way forward.** Every destructive action carries
  its restore path, designed *first* (not fail-safe's "where do we land" but
  carrying the rope on the way in). A destructive verb with no stated way back is
  not finished. (See [`DATA-PROTECTION.md`](DATA-PROTECTION.md); serves
  precedence rule 1.)

## 2. Structure — simple, decoupled, one source of truth

- **KISS.** Prefer the simple design over the clever one; when two designs work,
  ship the smaller. Don't add accidental complexity to an already-complex system.
- **DRY.** One authoritative home for each fact and each piece of logic.
  Duplicated truth is a future divergence bug (this is [`EVIDENCE.md`](EVIDENCE.md)
  §9 and [`PROPAGATION.md`](PROPAGATION.md)'s one-source rule, at the design layer).
- **Loose coupling / modular architecture.** Components talk through narrow,
  explicit contracts, not shared internals. *Case:* the federation pattern — each
  domain is its own tool behind a thin orchestrator, joined by a structured-output
  + exit-code seam, not merged into a monolith.
- **Unix philosophy.** Do one thing well; compose small sharp tools; emit
  structured output designed to feed the next (unknown) program. Each verb is one
  job; `--json`/exit codes make the tool a citizen of a larger pipeline. The
  spirit: modularity, composition, transparency, least surprise.

## 3. Interaction model — events over polling

Prefer events and triggers; avoid polling, timers, and schedules. The latter
have a place, but only on a clear, stated need — a poll loop is a standing cost
*and* a staleness window. Convergence rides a triggered action, not a blind
sweep; recovery fires on an event. When a timer **is** the right tool, say why
(and bound the staleness — see the timer-vs-event situation test).

## 4. State & concurrency

- **Stateless and asynchronous by default**, unless there's a clear case against.
  Keep no authoritative state of your own where the world already holds it: derive
  desired truth from the source, treat the live system as the actual truth, and
  re-derive each run. Introduce persistent state only where the value is real and
  the staleness is managed.
- **Idempotent and convergent by default.** A verb declares desired state and
  converges toward it; running it twice is safe and the second run is a no-op.
  This is the property that makes automation safe at all — a verb that is not
  re-run-safe must say so **loudly** and is not automatable. (Serves rule 1.)

## 5. Security, privacy, cost — by design, not bolted on

- **Privacy, security, and financial efficiency are design inputs from the first
  line**, not later hardening passes. Secrets never land inline; no personal
  detail in a shareable artifact; cost is a written policy, not an afterthought.
- **Reproducible, least, just-in-time, short-lived credentials.** Secrets and
  privileges are the smallest set the task needs (least privilege), granted at
  the moment of use (just-in-time), and expiring (short-lived). The standing,
  broad, forever credential is the anti-pattern. Two classes:
  - **Internal** (both ends are ours) — the shared secret rotates mechanically at
    will; losing it costs a rotation, not knowledge.
  - **External** (third-party APIs) — carry the *code* that regenerates the
    credential on demand behind a one-off human approval; never a hand-kept
    irreplaceable token.

  *Honest pattern:* real systems often start with standing credentials — those
  are reproducible but neither JIT nor short-lived. The triad is the *direction*;
  each standing credential is a tracked debt to shorten, not a resting state.
  (Serves rule 1: a short-lived least credential has a small blast radius.)
- **Zero Trust — the NIST SP 800-207 tenets, right-sized.** No asset is inherently
  trusted; verify explicitly; least privilege; assume breach; network location
  alone grants no trust. NIST's own caveat is that not every tenet is achievable
  in pure form — so implement the achievable and **name the gap** rather than
  claim the posture. A location control (fencing to an internal range) is kept as
  defence-in-depth, never *as* the trust decision. *A control stricter than its
  threat trains bypass* — Zero Trust is the target; each unmet tenet is a stated,
  tracked debt, not a silent miss. (See [`AUTONOMY.md`](AUTONOMY.md),
  [`DATA-PROTECTION.md`](DATA-PROTECTION.md).)

## 6. Legibility — observable, provenanced

The enforcement arm of "tell the truth": a principle whose violation is invisible
isn't a principle, and a system that outlives any one session's understanding
must carry its own evidence.

- **Observable by design.** Every action reports what it did *and* what it did
  not do; **silent success is as much a defect as silent failure.** Structured
  output + exit codes on every verb; a bounded sweep says what it dropped ("no
  silent caps"); a partial result must announce that it's partial.
- **Every fact carries provenance; every claim carries its test.** Facts are
  dated and attributed; claims state what would prove them wrong and when that
  check runs. *The cautionary case:* a "proven" comment committed shortly after
  its proof was quietly voided — an undated, untested claim is a future lie. When
  a learning is refined, sweep the stale claims in the *same* commit. (This is
  [`EVIDENCE.md`](EVIDENCE.md) at the system-behaviour layer.)

## 7. Reproducibility — infrastructure is code

Numbered last for stability, logically first: the axiom the rest serves. Every
piece of infrastructure is reproducible from code — it exists because the source
says so, and can be rebuilt from source + secrets alone. Nothing exists that
can't be regenerated.

- **No snowflakes.** A setting that lives only in a running system's head —
  hand-config nobody codified — is a latent outage: when the box dies, the
  knowledge dies with it.
- **The code is the source of truth; the live system is a cache.** Desired state
  lives in version control; the live system is a convergence target, never the
  master. The acid test: you could lose every node and rebuild from the repo +
  the secret store.
- **The secret store is not exempt.** "Rebuild from repo + secret store" is not
  the floor — the store *itself* is reproducible: throw it away and regenerate.
  No hand-kept irreplaceable token anywhere; even a secret is *code + a repeatable
  procedure*. (Mechanism in §5.)
- **Codify before you converge; a hand-action is only a stated bridge.** A live
  fix may precede its codification, but only as a **logged, temporary** bridge
  carrying a follow-up to bring it into code — or as a documented permanent
  exception where codifying is genuinely unsafe (e.g. an action that would sever
  the agent's own access mid-run). Never as steady state. (Serves rule 1: a
  reproducible system is a recoverable one; and rule 2: undated hand-state is a
  future lie.)

---

## Trade-offs: precedence and situation tests

The principles *will* collide. Two tools resolve a collision: a precedence order
for what overrules what, and situation tests for which principle even applies.
Every ruling below generalises a real decided case — precedent, not theory. A new
collision that fits none of these gets **decided, recorded** (in the code comment
at the site, the roadmap item, and — if it generalises — a new line here), and
becomes precedent.

### Precedence — when two principles want different designs

Higher overrules lower; a lower principle is optimised only within shapes the
higher ones already accept. **§0 is not on this ladder** — honesty and the Laws
are never traded against a design principle.

1. **Protect the system and its data.** Never leave a node, network, or dataset
   in a dangerous/unrecoverable state; destructive actions verify first.
2. **Tell the truth.** Never act on data known to be untrustworthy, and never
   emit a claim stronger than its evidence. A wrong action or a false "certain"
   is worse than no action — a false positive spends trust the tool never gets
   back.
3. **Keep the core job running.** Degrade, isolate, skip-loudly — partial service
   beats total failure, but never by violating 1 or 2 (an untrustworthy plan is
   *skipped*, not applied half-read).
4. **Hold the security posture — right-sized.** Least privilege and explicit
   verification, scaled to the actual threat (see gate sizing).
5. **Keep it simple and consistent.** KISS/DRY/least-surprise break ties among
   designs that pass 1–4. Consistency of mechanism usually beats a local
   optimisation of one case.
6. **Keep it cheap.** Tokens, watts, dollars, runtime — optimised last, never by
   weakening the above.

### Situation tests — which principle applies here?

- **Whose failure is it?** *Our* data/logic/config → **fail-fast** at the edge. A
  *remote peer's* failure → **degrade + isolate** (skip it, loudly). *Precedent:*
  one unreachable node must not block healthy ones, but a unit whose *own* plan is
  partial is refused. Same fault, different owner, opposite principle.
- **Is the action reversible?** Read-only/reversible → be permissive, degrade
  freely, run ungated. Destructive/irreversible → fail-safe: gates, confirms,
  re-checks at execute, restore contracts. *Precedent:* observe/plan run anywhere;
  destructive verbs gate and re-check. (Mirrors [`AUTONOMY.md`](AUTONOMY.md)'s
  recoverable-vs-floor line.)
- **Claim or action?** An *action* on uncertain data is refused (rule 2). A
  *claim* on uncertain data is allowed but must carry honest confidence and a
  discriminator that survives the alternative explanations — and prefer the
  conservative miss over the false claim. *Precedent:* a discovery step that says
  "possible" and skips what it can't prove; a diagnosis that must not read a
  floored-but-fine input as "broken, certain, replace it".
- **Gate sizing.** Match a control to its threat, not stricter. Over-restriction
  erodes itself: a guard that blocks legitimate routine work trains the operator
  to loosen it, defeating its purpose. *Precedent:* a safety gate re-classed to a
  *looser* tier once it was clear the stricter one blocked exactly the routine
  work the tool existed to do.
- **Special case vs uniform mechanism.** When one field/path seems to want
  different semantics from its siblings, keep the mechanism uniform and make the
  special need **loud** (a lint, a report, a stated invariant). Divergent
  semantics are a least-surprise defect that surfaces years later. Escalate to a
  true special case only when the **threat model changes**, and record the trigger.
  *Precedent:* a config field that seemed to want restrict-only merge kept the
  uniform override semantics plus a loosening lint — the true special case
  pre-agreed to trigger the day the config takes a second author (the trigger
  recorded, the semantics not forked early).
- **Mitigation under uncertainty.** While a fix's own justification is unproven,
  hold the **narrowest live-proven scope** — extending an unproven mitigation
  extends unproven behaviour. *Precedent:* a live workaround whose root cause was
  still unconfirmed stayed scoped to the one surface it was proven on until a
  re-test settled the culprit; widening it fleet-wide first would have widened
  unproven behaviour.
- **Timer vs event.** Default to the event/trigger. A poll/timer needs a stated
  need *and* a stated staleness bound (e.g. "refuses if the snapshot is older than
  24h"), so the cost and the window are both deliberate.
- **Widen in rings.** A change rolls out bench → one production node → fleet,
  observing between rings. Ask "what ring is this in, and what did the last ring
  show?" before widening. A change that skips a ring needs a stated reason (e.g.
  the delta is identical everywhere and ring 1 proved it).
- **State vs stateless.** Re-derive by default. Introduce persistent state only
  when the value is real *and* the staleness is managed (dated snapshots, age
  checks) — undated state is a future lie (rule 2).
- **Codified or hand-done?** Every change lands in code first and converges. An
  out-of-band/hand action is allowed only when codifying it is unsafe
  (self-lockout) or as a **logged bridge** carrying a follow-up to codify it —
  never as steady state.
- **Standing or ephemeral credential?** Default to least + just-in-time +
  short-lived (§5). A standing credential needs a stated reason — usually the
  platform offers no JIT grant — and is a tracked debt, not a resting state.

*A stated deliberate exception is fine; a silent violation is the defect. When a
collision is resolved, the ruling lives in three places: the code comment at the
site, the roadmap item, and — if it generalises — a new precedent line here.*
