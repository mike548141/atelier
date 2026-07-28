# Review brief — the TA1–TA9 application (rule-4 cold pass)

- **Date:** 2026-07-28 1136 UTC
- **Reviewer tier:** Fable (matches the queue's stated tier)
- **Spawn provenance:** taken from the ROADMAP `⏳` queue by a session Mike
  opened with "Please do any review work" — the rule-4 worked example. The
  session authored none of the TA chain: not the Track A application, not the
  prior cold pass, not this application. The applier session did not spawn
  this review. Claim commit `d930d7b` on main.

## What the work is (refs only, from the queue pointer)

The application of the TA1–TA9 rulings from the Track A application cold
pass. The reviewed cycle carried a MAJOR, so the cycle is open and this
application earns its own pass; `docs/method/REVIEW.md` was edited in the
delta, which is self-authored doctrine (rule 3/4 territory — findings on it
are Mike's to decide).

**Delta under review:** commits `3fb6437`, `321bbd3`, `0ca4b75`, `d80f9d8`,
`f204fba`, and the queue commit `f3a3cd4`. Files: `tools/floor.py`,
`tools/floorfleet.py`, `tools/test_floor.py`, `tools/test_floorfleet.py`,
`tools/test_precommit.py`, `docs/method/REVIEW.md`,
`docs/sessions/2026-07-27-2301-track-a-fail-opens.md`, plus `f3a3cd4`'s
records hunks.

**Context at HEAD:** a later commit (`549930b`, C1 phase 1) touched the same
enforcement files and carries its own queued `⏳`. This review examines the TA
delta's diffs and current behaviour at HEAD; defects introduced by the C1
delta belong to that review, but any interaction between the two is in scope
here.

## Sequence and deferred material

Per REVIEW.md's application-review sequence: the reviewer meets the work
cold, commits its own findings first, and only then opens the deferred
material to reconcile. Deferred until findings are committed:

- the intent record
  [`2026-07-28-0214-ta-findings-application`](../sessions/2026-07-28-0214-ta-findings-application.md)
- the prior verdict
  [`2026-07-28-0123-track-a-application-cold`](2026-07-28-0123-track-a-application-cold.md)
  and any decision stamps on it
- the evaluative harvest hunks in `f3a3cd4` (`ROADMAP-DONE.md` and the
  intent record's content)

The residual exposure of an application review — commit messages carry the
finding IDs and one-line ruling summaries, so some framing leaks through the
delta itself — is named here, not denied.

## Scope — widest the work admits, four lenses

1. **Approach & assumptions** — are these the right fixes for what the
   commit subjects claim to fix? Attack the load-bearing assumptions in the
   new guard/cover/estate-discovery logic on their own merits.
2. **Correctness & quality** — do the diffs do what their messages claim; is
   anything overclaimed or silently narrowed; are the tests real tests
   (wrong tests verify nothing).
3. **Completeness / harvest** — what the application should have covered and
   didn't; whether the queue pointer's delta list is complete (AW6);
   whether landing = queuing held (AWA2/TA9 — the pointer commit is 6
   minutes after `f204fba`).
4. **Security & privacy** — the delta edits the security floor's enforcement
   plane (`floor.py`, `floorfleet.py`): scope-widening, path handling,
   worktree discovery, YAML reading are all attack surface. `/security-review`
   reach: this is a landed-delta review with no pending diff, so the scanner
   cannot be aimed at the work; discharged on those grounds — the mechanical
   floor here is the repo's own scan suite plus the test suites, re-run live.

**Live proofs to re-run:** the full test suites (`test_floor.py`,
`test_floorfleet.py`, `test_precommit.py`, and the rest of `tools/` +
`instruments/`), the pre-commit floor scan, and the specific probes the
commit messages claim (scope-path guard, shrunken-cover labelling, worktree
estate discovery) — exercised at HEAD, red legs where reconstructible.

**Non-goals:** the C1 delta's own merits (its queued review covers it); the
prior cycle's un-appealed rulings themselves (Mike's decisions are not
re-litigated — what is reviewable is whether the application implemented
them faithfully, which is reconcile-step work).

---
