# method/ — how we work

The relationship layer: doctrine that applies to *all* the work, technical or
not. This is the shareable core of atelier.

Read in this order:

1. **`00-APEX.md`** — honesty is absolute, adaptation is continuous, then the
   AI-adapted Three Laws. The frame everything else sits inside; above the
   precedence ladder, never traded.
2. **`EVIDENCE.md`** — the machinery behind the apex's honesty and adaptation
   (the truth bar both rest on): authority tiers, acquisition-method error risk,
   absolute dating, store-the-rule-not-the-value, one-fact-one-home,
   trigger-based refresh. How the agent knows what it claims.
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
7. **`REACH.md`** — getting past a block, and the line you won't cross for it:
   escalate cheapest-first (the fetch ladder — built-in → raw client → real
   engine → the operator's session → ask), and the credential boundary as a
   **purpose-of-storage test** (provisioned stores are the intended path;
   personal convenience stores off-limits by default; ride a session, never the
   saved credentials that mint one; the principal grants across the line). The
   instruments' third verb — *extend reach*; the built instance is
   `instruments/browser-fetch/`.
8. **`STORAGE.md`** — GitHub master, iCloud backup, laptop disposable.
9. **`CONCURRENCY.md`** — one worktree per line of work; serialise real-world
   side-effects.
10. **`TOOLBOX.md`** — keep a tool manifest; approved-but-missing may be
   installed; keep the personal inventory machine-local.
11. **`PRINCIPLES.md`** — the design principles (resilience, structure,
   events-over-polling, state/concurrency, security/privacy/cost, legibility,
   reproducibility) + the precedence ladder + situation tests, with generalised
   cases. **Canonical here**; `ros` keeps its tiki bearings + review case-law and
   points up.
12. **`ECONOMICS.md`** — match the model to the job by risk (workhorse builds,
   capable tier reviews), the billing states of the marginal token, the
   marginal-cost self-check, tiered authority, and
   session hygiene. **Canonical here**; the estate-specific numbers (prices,
   model roster, session-overhead figure) stay person-local in `ros`.
13. **`COMMUNICATION.md`** — calibrate replies to the person reading them: each
   principal keeps a person-local "working with me" calibration (ordering,
   density, visual structure, tone, locale), maintained from dated evidence.
   The *pattern* is shareable; the instance stays in `~/.claude/`, with a
   scrubbed worked example in the doc.
14. **`CONVENTIONS.md`** — the default frame: a value carrying a frame (a time
    needs a zone, a price a currency, text an encoding) is read against a
    declared default, stated once and silent, labelled only on a deviation or a
    collision; foreign data is kept as-is with its frame as metadata. Declares
    the estate's defaults — UTC at rest, NZD, ISO 8601, UTF-8, NZ English + te
    reo. Time's full case is ADR 2026-07-15.
15. **`DOCUMENTATION.md`** — transfer intent and capability at the reader's
    altitude: "great" is the right artefact per cell of two axes — **Diátaxis**
    (tutorial/how-to/reference/explanation, the what/who) × the **consumer**
    (human · AI · orchestrating software, the how). Error messages and the
    `--json`/exit-code machine contract are documentation too; a fact lives once
    and everything points; docs change in the behaviour's commit and carry their
    proving rung; the vendor-docs seam points, never mirrors. Generalises `ros`
    `PRINCIPLES §6`; tiki is the named exemplar. *(review-owed; draft authored
    2026-07-20.)*

**Meta — how the doctrine is enforced, recorded, and propagated:**

- **`GLOSSARY.md`** — the shared language: load-bearing terms defined once or
  pointed to their canonical home (thin anchor; tiki's admission rule). SEED —
  the principal's ratify pass is owed.
- **`REVIEW.md`** — the enforcement half: independent, fresh-context review
  (by the most capable model available) before work is trusted (four lenses;
  brief-on-top/verdict-below lifecycle; inline vs batched). Documents inform;
  review enforces.
- **`RECORD.md`** — docs-as-code (lockstep change), the append-only session log +
  detail-on-demand, ADRs for re-litigable decisions, absolute dating. The record
  is what makes a session resumable cold.
- **`SIGNING.md`** — provenance for the record: SSH-native commit/tag signing
  fleet-wide (what a signature honestly claims, the adoption boundary, key
  handling under SECRETS' scope), artefact signing deferred behind a stated
  trigger. Standard decided (ADR 0007); dormant until the principal registers
  a signing key — the activation ladder is in the doc.
- **`PROPAGATION.md`** — how the house doctrine reaches every child repo without
  a second source of truth drifting: thin anchor (inlined safety floor, binds
  even unread) + fat pointer (SHA-pinned, drift-checked at session start). Also
  holds the layer-override rule (a child may narrow/append, never silently
  contradict) and the enforcement clause (read ≠ complied). Read this when
  wiring a new repo or bumping a pin.
