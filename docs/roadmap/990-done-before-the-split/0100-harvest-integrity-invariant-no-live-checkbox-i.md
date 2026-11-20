- [x] **Harvest-integrity invariant — no live checkbox in ROADMAP-DONE**
  **RATIFIED 2026-07-22 (Mike): "I like this idea of embedding it into the
  CI" — build as counselled (extend sizescan; CI embedding comes free via
  the floor's existing `sizescan --check`).** (claimed 2026-07-22-0634,
  wt: harvest-integrity-gate)
  (Mike, 2026-07-22; triggered by IR5 and confirmed real by its first manual
  run — see below). The invariant: `[ ]` / `[~]` / `⏳` state markers must
  never sit in `ROADMAP-DONE.md` — the archive records finished history, and
  a live marker there is either a botched harvest (open work silently
  buried) or an untrue state (done work never flipped). **Deliberately NOT
  delivery-verification of `[x]` items** (Mike's explicit bound — overhead
  too high); this checks *state coherence*, one grep's worth of cost.
  - **Counsel — extend `sizescan`, not a new tool**: it already owns the
    ROADMAP↔ROADMAP-DONE seam and reads both files; add a red on live
    markers in any `*-DONE` store, with a machine-readable escape for
    sanctioned non-delivery states. Legend gains one state for those:
    `[-]` **dropped** `— superseded / no longer required: <grounds>` — the
    only live-box-shaped thing the archive may hold.
  - **On hit, the finding is investigative, never auto-fixed**: the session
    that reds checks the evidence (children's states, sessions log, the
    codebase) for delivered-but-unmarked vs genuinely-open, then notifies
    Mike with the evidence and a recommendation — flip with a dated note,
    un-harvest back to ROADMAP, or mark `[-]` dropped. The scanner finds;
    the agent investigates; Mike decides.
  - **First manual run already caught one**: a `[ ]` parent
    ("Batch-review follow-ups") sat in ROADMAP-DONE with both children
    `[x]` DONE — delivered, never flipped; corrected with a dated note
    (this session). *review: WARRANTED when built — a CI gate is
    policy-as-code doctrine; brief owed at pickup.*
  **BUILT 2026-07-22, delta `0bdccf3`** (suite 302→314 green; live repo
  scan green). Two counsel points superseded by Mike's mid-build rulings,
  disposition noted: the `[-]` dropped state was replaced by the
  **work-owed tri-state** ([x] = no more work owed, disposition in the
  item's text); the "one grep" scope grew line-based parent/child
  coverage per Mike's four-situation taxonomy. Review queued ⏳ (rule 4).
