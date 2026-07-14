# 2026-07-15 · MODEL-ECONOMICS triple delta — sub-agents, tier selection, reset-by-record (Fable)

**Mike's prompt:** for economics, (1) are we using sub-agents efficiently and
effectively — should doctrine tell repos when/how/why to use or not use them;
(2) Claude appears to treat ~150K context as a large/inefficient session and
suggests `/clear`/`/compact` — should we keep context under 150K and put that
in the doctrine? Follow-up: (3) should doctrine also cover choosing model tier
by balancing cost against quality and risk — a cheaper model when it gets the
job done to the quality we want?

## Assessment (agreed before drafting)

- **Sub-agents: yes, doctrine-worthy.** The existing coverage was one sentence
  that implied token *savings*; the truth is context *isolation* — a sub-agent
  re-pays its own overhead and often costs more total, buying a lean main
  context and deferred long-context decay. The when-not half (lossiness — the
  report is all that survives) was entirely missing.
- **150K: adopt the practice, not the number.** No official threshold exists —
  it's ~75% of the 200K window where harness warnings loom; encoding the
  constant would bake a harness/plan-specific number into doctrine (the
  person-local footer exists to keep those out). The real gap was mechanism
  guidance: record-and-restart ≠ `/compact` ≠ `/clear`. The doctrinal line:
  **the session record is this method's compaction** — deliberate, curated,
  versioned; in-place compaction is the mid-task fallback; a bare wipe only
  after the record is written.
- **Tier selection: yes — and the doc already held its own precedent**, the
  runner-class rule ("cheapest runner class that genuinely does its work"),
  which generalises to models: cheapest model that genuinely does the work,
  where "genuinely does" is a *verifiability* test (catchable failure makes
  cheap safe; silent-failure/judgement-heavy work pays for capability) plus
  rework pricing (likely hand-up ⇒ escalate up front).

## Done

- Three deltas to `method/MODEL-ECONOMICS.md` (commit `a27bb90`): new
  *Sub-agents — isolation, not savings* section; tier-selection paragraph in
  *One doctrine, tiered authority*; hygiene item 4 rewritten as *reset by
  record, not by compaction*.
- Cold pass ran same session (inline background agent, author-written brief
  with seeded questions deferred below the divider per REVIEW's independence
  rules): **PASS-WITH-FINDINGS — 0 MAJOR · 3 MEDIUM · 3 LOW**, verdict in
  `reviews/2026-07-15-0910-model-economics-triple-delta.md`. The reviewer
  re-ran every pricing/caching claim against the current API reference — all
  held, including one it attacked expecting to fail ("cost is linear the whole
  way" — no long-context premium on current-generation pricing).
- Findings: F1 sub-agent≡cold-reviewer overclaims independence (drops the
  spawn-prompt-is-a-warm-brief bind REVIEW.md states); F2 the economics-flip
  axis is mis-specified (the lever is work *remaining ahead*, not depth
  accrued); F3 tier selection + the total-cost claim are pool-blind (precedence
  vs the pool split unstated); F4 sub-agents × cheap-tier fan-out never
  composed; F5 "cache stays warm" can invert past the TTL (the real benefit is
  a lean, stable prefix); F6 child template still carries the pre-delta
  one-liner.
  Author counsels **accept all six**; self-authored doctrine ⇒ **Mike's ruling
  owed** (REVIEW rule 3). 0 MAJOR ⇒ once ruled, application closes the cycle.

## Open

- 🎯 Mike's ruling on F1–F6 (counsel: accept all; six small edits — five
  one-clause fixes in MODEL-ECONOMICS, one template sweep).
