# Withdrawn reviews — kept, not counted

Review passes that **happened and were not accepted**. They are preserved
because this repo does not rewrite history; they are quarantined here because
an unaccepted verdict sitting next to accepted ones is worse than no verdict
at all.

Nothing in this directory is a finding, a ruling, or a completed review. A
`⏳` item with a file here is still `⏳`.

## The convention

1. **Preserved verbatim.** The file is restored exactly as it was written,
   with a `⛔ WITHDRAWN` banner prepended and nothing else changed. The
   banner names who rejected it, when, and on what ground.
2. **Not in `docs/reviews/`.** A reader scanning accepted verdicts, or an
   index over them, must not meet a rejected one by accident.
3. **Never a queue ref.** The ROADMAP `⏳` pointer for the item may *say* an
   unaccepted pass exists — it must not hand the reviewer the file as
   reading. The pointer's ceiling is refs and intent, and a rejected pass's
   framing is the contamination `REVIEW.md` rule 2 exists to prevent.
4. **Read after, not before.** The accepted reviewer for the item may read
   this once their own verdict is written and committed. Before that, no.
5. **Findings die with the pass.** Nothing queued by a withdrawn pass carries
   forward. If a finding is real, the accepted pass finds it independently —
   and that is the point of the redo.

## What is here

### The 0647 triple pass — wrong reviewer tier (2026-07-26)

Three cold reviews run in one session on 2026-07-26 0647 UTC, merged at
`4252bc6`, and **rejected in full by Mike the same day**: cold review passes
are Fable's, and this pass was run by Opus. The rejection was not about the
content — it was never assessed on content. A pass on the wrong tier is not a
pass.

| File | Item it covered | Its own stated verdict (**not accepted**) |
| --- | --- | --- |
| [`…adr0008-called-not-copied-cold.md`](2026-07-26-0647-adr0008-called-not-copied-cold.md) | ADR 0008 + estate rollout | 3 MAJOR · 2 minor · 2 LOW · 1 nit |
| [`…pathscan-s2-cold.md`](2026-07-26-0647-pathscan-s2-cold.md) | `pathscan` (S2) first-of-kind | 1 MAJOR · 3 minor · 2 LOW · 1 nit |
| [`…stampscan-s4-cold.md`](2026-07-26-0647-stampscan-s4-cold.md) | `stampscan` (S4) first-of-kind | 3 MAJOR · 1 minor · 3 LOW · 1 nit |

Those counts are recorded as *what the withdrawn pass claimed*, so the shape
of what was discarded is legible. They are not a baseline, not a target, and
not something an accepted pass should reconcile against.

Trail: merged `4252bc6` → withdrawn from the tree `625ee0e` → restored here
2026-07-26 1007 UTC. All three items were re-queued unchanged and still await
their first accepted review.
