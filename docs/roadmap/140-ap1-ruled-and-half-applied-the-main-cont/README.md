# AP1 ruled and half-applied — the `@main` control is in force (Mike, 2026-08-09)

**Mike's ruling, 2026-08-09:** *ruleset with owner bypass, plus a machine-check.*
Taken over full protection (PR-only for every change) and over re-wording the
clause to the truth. The reasoning he was given: PR-only is the strongest answer
and makes ADR 0008's clause literally true, but on a solo estate it is friction
paid on every commit forever; re-wording alone closes the honesty defect and
leaves the exposure untouched.

**APPLIED the same day — the platform half.** Repository ruleset `20603641`,
`enforcement: active`, on `~DEFAULT_BRANCH`: `deletion`, `non_fast_forward`,
`required_signatures`. Verified through the exact endpoint AP1 read as empty —
`repos/…/rules/branches/main` now returns all three rules. Chosen because none
of the three can block an ordinary signed fast-forward push, so the standing
direct-push grant is untouched; a live session was mid-work when it landed and
was unaffected. Every commit on this machine already verifies (12 of 12 sampled
`verified=true`), so `required_signatures` was safe to switch on rather than
aspirational.
