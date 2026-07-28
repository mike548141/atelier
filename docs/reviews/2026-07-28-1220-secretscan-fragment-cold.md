# Review brief — secretscan fragment-match exemptions (rule-4 cold pass)

- **Date:** 2026-07-28 1220 UTC
- **Tier / spawn provenance:** Fable — the tier the queue item asks for on
  the security floor. The Mike-spawned "do any review work" taker session,
  fourth queue item today; author of nothing in this delta, not spawned by
  its author. Claim commit on main precedes this worktree.

## What the work is (refs only)

Commit `dd902aa` (#14): four secretscan suppression rules re-anchored from
fragment matches to whole-shape matches (the env-var `\b` lead, the
extensionless secret-store path, unclosed templating markers, the stray
bracket), plus three suppressions added for false positives the fix itself
introduced. Files: `tools/secretscan.py`, `tools/test_secretscan.py`, and
the queue pointer in `docs/ROADMAP.md`.

**Deferred until findings are committed:** the boundary-findings triage
session record
[`2026-07-28-0430-boundary-findings-triage`](../sessions/2026-07-28-0430-boundary-findings-triage.md)
(the applier's evaluative account). Named exposure: the commit message and
the queue item's own two aimed questions, treated as a floor of questions,
never a fence.

## Scope — four lenses, security-first

1. **Approach:** the queue's first aimed question — is *re-scan the
   corpus* a sound acceptance test for a security gate, or does it tune
   the gate to one estate's content? Attack each of the three
   corpus-driven suppressions (minified-JS code shapes, kebab slugs,
   comment prose) for what *else* its widened net catches.
2. **Correctness:** red legs for all four defect classes at `dd902aa^` vs
   HEAD, with synthetic values; check the new regexes' edges (`_LEAD`
   against `BYPASS`/`passport`-type neighbours; `ABS_PATH_RX` vs base64;
   closed-marker templates; `CODE_EXPR_RX`'s charset argument).
3. **Completeness:** the second aimed question — the pre-existing
   lowercase-hex gap, to be *ruled on* rather than inherited; whether the
   new suppressions open siblings of that same low-charset-diversity
   family; independent re-scan of the estate against the claimed result
   (12 clean stay clean; the two exposed repos 2→9 and 25→26).
4. **Security & privacy:** the delta *is* the security lens; also verify
   the "test values are synthetic / two real values removed before
   commit" claim (no live credential in the test file or its history).
   `/security-review` reach: landed delta, nothing in flight — discharged;
   the probes below are the mechanical floor.

---
