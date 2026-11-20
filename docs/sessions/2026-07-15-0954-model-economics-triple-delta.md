# 2026-07-15 · MODEL-ECONOMICS triple delta — sub-agents, tier selection, reset-by-record (Fable)

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 99+1 -->
- [2026-07-15 · MODEL-ECONOMICS triple delta — sub-agents, tier selection, reset-by-record (Fable)](2026-07-15-0954-model-economics-triple-delta.md) — Mike's three economics questions answered and codified: sub-agents earn a real section (isolation-not-savings — a sub-agent re-pays its own overhead and often costs *more* total, buying a lean main context; when/when-not; the report is all that survives), model-tier selection made explicit (the runner-class rule applied to models — cheapest model that genuinely does the work, "genuinely" = a verifiability test, plus rework pricing), and hygiene item 4 rewritten as reset-by-record (no numeric context thresholds; the session record *is* this method's compaction; /compact = mid-task fallback, /clear only after the record). Cold pass ran inline same session: **PASS-WITH-FINDINGS — 0 MAJOR · 3 MEDIUM · 3 LOW** (F1 independence bind dropped, F2 flip-axis mis-specified as depth not work-remaining, F3 pool-blindness, F4 tier×sub-agent uncomposed, F5 cache-warmth inverts past TTL, F6 stale child template); every pricing claim re-ran clean against the current API reference. Mike ruled same day: **F1–F6 [fixed], cycle CLOSED** — F1 applied as the independence *bind* on warm spawns (ban held in reserve, distinction flagged), and Mike supplied a further nuance applied with the batch: **price the job, not the token** (a dearer model finishing in fewer turns/retries is often the cheaper job — only cost-to-done compares outcomes). Child template swept (F6); floor green; propagates on the next pin bump. Coda, same day: Mike reopened F1 — the conditional agreement hadn't matched his intent — and after a plain-language walk-through ruled **tiered independence, now REVIEW rule 4**: routine work may warm-spawn under the deferral bind; **self-authored doctrine is banned from warm spawns** (non-author spawn only — principal, scheduled batch, or neutral session), highest-stakes category stated explicitly in the rule. Rule 4's own cold pass queued for Mike to trigger (can't be warm-spawned by its author). Sentence-shape feedback also codified into COMMUNICATION.md on Mike's yes.


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

## Ruling + application (same day) — cycle CLOSED

Mike ruled F1–F6 accepted. F1 nuance handled honestly: Mike's wording reached
up to a full ban on warm spawns; the counsel was the *bind* (independence
rules on author-spawned reviews, per REVIEW.md), which is what was applied —
the distinction flagged to Mike, the ban held in reserve if the bind proves
insufficient. Mike also supplied a new nuance, applied with the batch: **price
the job, not the token** — a dearer model that completes the work in fewer
turns/retries is often the cheaper job; only cost-to-done compares outcomes.
All fixes applied to `method/MODEL-ECONOMICS.md` + the child template (F6);
decision recorded in the verdict file; floor green. 0 MAJOR ⇒ closed on the
ruled application.

Separately, Mike gave standing communication feedback (all repos): stop
interrupting sentences with long bracketed asides — restructure instead.
Saved to agent memory; on Mike's yes, codified into COMMUNICATION.md's
accessibility axis (sentence shape).

## F1 re-ruled — REVIEW rule 4 (later, same day)

Mike reopened F1: the conditional "if that's what you're counselling"
agreement had not matched his intention — a live case of the informed-principal
rule. After a plain-language walk-through of the options (bind vs ban vs
tiered), Mike ruled **tiered, with the highest stakes explicit**: routine work
keeps warm-spawn-plus-deferral; **self-authored doctrine** — by function:
prose, ADR, schema, validator, CI gate, behaviour-stamping template/skill —
is **banned from warm spawns**; its review must be spawned by a non-author
(the principal, a scheduled batch, or a neutral session). Applied as
REVIEW.md rule 4 + the rules lead-in + the inline-bullet carve-out, plus a
pointer clause in MODEL-ECONOMICS' sub-agent section. Rule 4's own wording is
agent-drafted, so by its own terms its cold pass cannot be warm-spawned —
queued on the ROADMAP for **Mike to trigger** from a fresh session. Agent
memory updated to match (including the lesson: for doctrine rulings, walk the
options plainly and confirm intent before applying a conditional agreement).
