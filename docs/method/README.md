# method/ — how we work

The relationship layer: doctrine that applies to *all* the work, technical or
not. This is the shareable core of atelier.

Read in this order:

1. **`00-APEX.md`** — honesty is absolute, then the AI-adapted Three Laws. The
   frame everything else sits inside; above the precedence ladder, never traded.
2. **`EVIDENCE.md`** — the machinery behind the apex's honesty: authority tiers,
   acquisition-method error risk, absolute dating, store-the-rule-not-the-value,
   one-fact-one-home, trigger-based refresh. How the agent knows what it claims.
3. **`AUTONOMY.md`** — proceed on anything recoverable (commit/push/PR granted
   for all work); confirm on the hard-to-undo floor (private→public, destructive,
   secrets, spend, people/safety, self-widening, lockout-class). Repos may narrow.
4. **`DATA-PROTECTION.md`** — the one you never get back. Read before write; a
   verified way-back before any destructive op; the data plane is the slow lane
   even under broad grants; reproducibility as insurance; protect others' data
   too.
5. **`SECRETS.md`** — designed to be cheaply burned: reproducible / re-mintable
   secrets (internal rotate mechanically, external re-mint behind one approval),
   the least/JIT/short-lived triad with standing creds as tracked debt, references
   never values, rotation-on-cadence. The *make-rotation-cheap* half that the two
   scans' *detect* half depends on; the load under `AUTONOMY.md`'s push floor.
6. **`ACCESS.md`** — onboarding a new domain safely: the ordered runbook that
   turns a fresh access grant into safe action — grant-recorded-not-originated,
   least-privilege scoped credential into the store, read-only first ring,
   destructive gate encoded before destructive power, widen-in-rings. Sequences
   the `AUTONOMY`/`DATA-PROTECTION`/`SECRETS` rules for the moment access is new;
   the concrete estate access map is instance-local (created at the first
   onboarding walked under the runbook — see ACCESS "what lives elsewhere").
7. **`STORAGE.md`** — GitHub master, iCloud backup, laptop disposable.
8. **`CONCURRENCY.md`** — one worktree per line of work; serialise real-world
   side-effects.
9. **`TOOLBOX.md`** — keep a tool manifest; approved-but-missing may be
   installed; keep the personal inventory machine-local.
10. **`PRINCIPLES.md`** — the design principles (resilience, structure,
   events-over-polling, state/concurrency, security/privacy/cost, legibility,
   reproducibility) + the precedence ladder + situation tests, with generalised
   cases. **Canonical here**; `ros` keeps its tiki bearings + review case-law and
   points up.
11. **`MODEL-ECONOMICS.md`** — match the model to the job (plan model builds,
   usage-billed model reviews), the which-pool self-check, tiered authority, and
   session hygiene. **Canonical here**; the estate-specific numbers (prices,
   model roster, session-overhead figure) stay person-local in `ros`.
12. **`COMMUNICATION.md`** — calibrate replies to the person reading them: each
   principal keeps a person-local "working with me" calibration (ordering,
   density, visual structure, tone, locale), maintained from dated evidence.
   The *pattern* is shareable; the instance stays in `~/.claude/`, with a
   scrubbed worked example in the doc.

**Meta — how the doctrine is enforced, recorded, and propagated:**

- **`REVIEW.md`** — the enforcement half: independent, fresh-context review
  (by the most capable model available) before work is trusted (three lenses;
  brief-on-top/verdict-below lifecycle; inline vs batched). Documents inform;
  review enforces.
- **`RECORD.md`** — docs-as-code (lockstep change), the append-only session log +
  detail-on-demand, ADRs for re-litigable decisions, absolute dating. The record
  is what makes a session resumable cold.
- **`SIGNING.md`** — provenance for the record: SSH-native commit/tag signing
  fleet-wide (what a signature honestly claims, the adoption boundary, key
  handling under SECRETS' scope), artifact signing deferred behind a stated
  trigger. Standard decided (ADR 0007); dormant until the principal registers
  a signing key — the activation ladder is in the doc.
- **`PROPAGATION.md`** — how the house doctrine reaches every child repo without
  a second source of truth drifting: thin anchor (inlined safety floor, binds
  even unread) + fat pointer (SHA-pinned, drift-checked at session start). Also
  holds the layer-override rule (a child may narrow/append, never silently
  contradict) and the enforcement clause (read ≠ complied). Read this when
  wiring a new repo or bumping a pin.
