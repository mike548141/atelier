# Review brief — Track A application A1–A5b (rule-4 cold pass)

- **Date**: 2026-07-28 01:23 UTC (brief written; verdict stamped below)
- **Subject**: the Track A fail-opens application — four commits `4e6d1cc`,
  `278da34`, `3799a` (LS1–LS5), `ac6f096`, landed 2026-07-27 from worktree
  `track-a-fail-opens`. Files in the delta per the queued pointer:
  `tools/floor.py`, `tools/floorfleet.py`, `tools/test_floor.py`,
  `tools/test_floorfleet.py`, `tools/test_precommit.py`,
  `docs/build/templates/CONTRIBUTING.md`. Reviewed as applied code at HEAD
  `fe6a8dc` (the taker's claim commit); applied-text provenance below.
- **Review class**: application review under REVIEW.md § *Applying decisions
  to doctrine*. Two of the applied verdicts carried standing MAJORs (EP1,
  EP3), so the application inherits rule-4 status. The floor and fleet
  scripts are doctrine by function — enforcement code that governs future
  agent behaviour estate-wide — so rule 3 binds: findings are the
  principal's to decide; this reviewer recommends and applies nothing.
- **Spawn provenance** (stated here, repeated in the verdict): this review
  was spawned by the principal (Mike) opening a fresh Fable session on
  2026-07-28 and pointing it at the review queue ("Please do any review
  work"). Neither the applier session (Opus, wt `track-a-fail-opens`), the
  prior verdicts' authors, nor any of their subagents started or instructed
  this session. The taker authored none of the chain; the queued pointer
  gave refs only. Tier: Fable, the required tier for cold passes.

## Applied-text provenance

Delta files at `f52b703` vs HEAD `fe6a8dc`: to verify — expected untouched
(the only later commits are the records close `f52b703` itself and the
taker's ROADMAP claim). If untouched, HEAD text is the applied text
verbatim.

## Sequencing note (rule 2 residual — named, not denied)

Deferred until findings are durably committed in this file: the intent
record `docs/sessions/2026-07-27-2301-track-a-fail-opens.md`, the two prior
verdicts (`2026-07-26-2215-adr0008-enforcement-propagation-cold.md`,
`2026-07-26-2215-floor-local-seam-cold.md`), the Track A entries in
`ROADMAP-DONE.md`, and all other `docs/reviews/` files.

Unavoidable exposure, named not denied: (a) the repo's own onramp read
order had this session read the `SESSIONS.md` tail before the claim, and
its 2026-07-27-2301 entry carries the applier's full evaluative account —
the rulings (A1 → (a)+(c), A2 → (c) for measurement over inference), the
zero-blast-radius measurement, the contract-test reversal, the env-gated
test find, and the 694 → 720 both-green claim; (b) the four commit
messages, read to establish the subject; (c) the queued pointer itself.
All three are the applier's framing and are treated as claims to test, not
settled scope. The ruling-faithfulness reconcile (delta vs the two
verdicts' decision stamps) is written only after findings are committed.

## Attack surface (named by the reviewer as its first act)

1. **Is the fail-open actually closed, or moved?** The class under repair
   is *a check that runs, exits 0, and covers nothing*. Attack the fixes
   with live probes, not the tests' word: a declared scope path that does
   not resolve (and a partially-resolving pair) must block; a hook-plane
   `leakscan` without a machine term list must fail, not degrade silently;
   CI's structural-only pass must render as partial, never as full cover.
2. **Did the narrowing delete protection?** A contract test that banned
   `--require-terms` on both planes was narrowed to CI with "complement
   added, not deleted". Attack: what does the CI plane now assert, and is
   the hook-plane assertion genuinely the complement or a weaker cousin?
3. **Are the pinned tests env-independent in both directions?** The claim
   is every suite ran twice, with and without `~/.claude/leakscan-terms.txt`.
   Re-run both ways live; a suite green only in one env is the exact
   defect class the fix claims to end.
4. **Does the parent row tell the truth?** `floorfleet` gained a row for
   atelier itself. Attack: can that row show green while the parent's own
   hook plane checks nothing (unset `core.hooksPath`, missing scanners) —
   i.e. does the fix re-introduce the class one level up?
5. **The widened claim.** The applier says the scope fix was widened past
   the finding: *any* declared path that fails to resolve blocks, partial
   drift included. Verify the widening is real and symmetric across the
   scanners that take scope declarations, not just the probed one.
6. **Security & privacy lens** (mandatory, both altitudes). The floor is
   privileged code: it runs on every commit in every child, parses
   repo-supplied config, and the repo-local seam (LS1–LS5) by design
   executes repo-resident check code in the committer's context. Attack:
   path traversal or injection via declared scope paths / config values;
   what a malicious or compromised child config can make the parent-run
   tooling do; whether the seam edges closed include the obvious abuse
   edges (a `local` check that shadows a registry check, exfiltrates, or
   lies about its own result); term-list handling (the machine term list
   is estate-sensitive by nature — does any failure path print its
   contents into logs/CI output?).
7. **New-machine ergonomics as a fail-closed trade.** A fresh clone now
   blocks on its first commit until the term list exists. Is the failure
   message actionable enough to stop the predictable `--no-verify` reflex
   (Track C4 names that route as unobserved), and is the once-per-machine
   step documented where a new adopter will actually meet it?
8. **Test honesty.** 26 new tests: do they exercise behaviour or mirror
   implementation? Especially: the three pre-commit tests formerly green
   *because* the hook was degraded — are they now pinned to a fixture in a
   way that would catch the original defect if reintroduced?

## Live proofs to re-run (claims taken from the exposure, to test)

- Both suites (`node --test instruments/*.test.js`; `python3 -m unittest
  discover -s tools`) twice — with the machine term list present and
  absent. Claimed: 720 tests, both green, both ways.
- The scope fail-open probe (unresolvable + partially-resolving declared
  paths) against `floor.py` at HEAD.
- Hook-plane `leakscan --require-terms` behaviour with and without a term
  list; CI plane rendering of the structural-only pass.
- `floorfleet` parent row against the real parent state.

## Scanner reach (stated per doctrine)

`/security-review` scans pending diffs; this is a landed-delta review with
no diff in flight, and running it here would scan this brief pre-draft (the
SL2 caution). It is discharged on those grounds; the security lens runs
manually at both altitudes instead, against the checklist above.

*Ask on top; verdict below the divider once findings are committed.*
