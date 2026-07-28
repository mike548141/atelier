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

---

## Verdict — Track A application cold pass (Fable, 2026-07-28)

**Spawn provenance, repeated from the brief**: spawned by the principal
opening a fresh Fable session on 2026-07-28 and pointing it at the queue;
the applier session and prior verdict authors neither started nor
instructed it; the taker authored none of the chain.

### Findings (committed before the intent record or prior verdicts were
### opened; reconcile follows below the marked divider)

**TA1 (MAJOR) — a declared scope path that RESOLVES, but not to this
repo's tree, still vacates a boundary check — proven live on the hook
plane.** The new guard tests existence (`(root / p).exists()`), not
membership. Probe, at HEAD: a repo declaring
`{"scope": {"secretscan": ["/etc"]}}` with a staged AWS credential —
the control run blocks (`❌ secretscan`, BLOCKED); the scoped run prints
`✓ secretscan clean` and `✅ secretscan enforced`, exit 0. Mechanism: on
the hook plane `_render` strips the leading `/`, the staged-diff prefix
filter then matches nothing, and a scan that matches nothing exits 0 —
the exact shape the delta's own comment in `_render` documents as "a
genuine sharp edge". `..`-shaped declarations do the same
(`scope: {"secretscan": [".."]}` renders `✅ enforced` on both planes
while reading the repo's *parent* tree on CI). The same commit series
closes exactly this lexical-vs-resolved gap for local `run` paths (LS3:
"a stated invariant that holds only against typos and not against the
file system") but leaves fleet `scope` paths with neither the lexical nor
the resolved membership check — the asymmetry sits inside one diff. The
guard's comment claims "it is the rest of that class"; the class has a
third member (does not resolve / resolves outside / resolves via symlink
outside) and only the first is shut. Reach matches EP1's: an explicit
declaration is required — and EP1 was fixed at that same reach.
Severity: security. Recurrence-prevention shape (counsel only, rule 3):
validate fleet `scope` paths at `Config.validate` the way `local.run` is
validated — refuse absolute and `..` at parse, and check the resolved
path is inside the root where the path exists.

**TA2 (minor) — an absolute scope path on the CI plane blocks by crash,
not by message.** Same probe, `--plane ci`: secretscan takes a traceback
(`scan_paths`) and the floor reports `❌ secretscan` — fail-closed by
exit code, but a crash reads as broken tooling rather than a config
error, which is the precise LS2 rationale, here for a fleet scanner.
`../sibling` is worse: it exits 0 cleanly against the wrong tree (folded
into TA1 for the pass/fail half; this finding is the crash-UX half).

**TA3 (minor) — partial scope drift on a softenable scanner is silent.**
`{"scope": {"wrapscan": ["docs", "gone"]}}`: runs on `docs` alone, exit
0, no line anywhere — the blocking guard covers only no-advisory-form
scanners, and the skip message covers only the all-missing case.
`floorfleet` shows the declared scope but not that a path stopped
resolving. Cover shrank with no signal; a one-line "N of M scope paths
missing" note on the result would close it without blocking anyone.

**TA4 (minor) — `partial` is read off argv and can contradict the
scanner's own report.** On a machine holding the term list, a `--plane
ci` run has leakscan print `✓ leakscan clean (structural + local)` — it
found and used the list — while the summary line says `🟡 partial cover
— no --require-terms on the ci plane`. The code comment asserts "the
rendered command is the only thing that knows what cover this run had";
the probe shows the opposite — the scanner's own output knows, the argv
only knows what was *demanded*. Harmless on a real runner (no list, so
the line is true there), and it errs toward claiming less cover, but
"identical output for materially different cover" is the delta's own
test, failed in mirror image.

**TA5 (minor) — `PARENT_RUN_RE` classifies a commented-out invocation as
wired.** Probe: a `ci.yml` whose only floor line is
`# - run: python3 tools/floor.py --plane ci --root .` evaluates to
`wired` / ok. A parent that disabled its floor while keeping the line in
a comment reads green on the very board built to catch a parent quietly
dropping its floor (A5b). Text-match heuristics are the board's existing
idiom, but the child classifier matches a structural caller line; the
parent regex matches anywhere in concatenated text, comments included.

**TA6 (note) — `test_precommit._TERMS` is a module-import side effect.**
`tempfile.mkdtemp` at module scope writes a file on every import
(including unrelated test selections) and is never cleaned up. Cosmetic;
the fixture-pinning it implements is correct and is the fix that matters.

**TA7 (note) — the board cannot run from a worktree, the mode this
repo's own doctrine prescribes.** From the review worktree,
`floorfleet` reports "no atelier children found" — the default search
root is the checkout's parent, which for a worktree is
`.claude/worktrees/`. Pre-existing discovery behaviour, not introduced
here — but the delta's `_repo_name` docstring names worktree sessions as
the case it serves, so the intent reached the row label and not the
discovery. `--root`-style search roots are accepted, so there is a
manual way out.

### Re-run and verified (the live proofs, each exercised at HEAD)

- ✅ 720 Python tests + 207 node tests, run twice — machine term list
  present and absent (HOME redirected, env var cleared) — all green both
  ways. The 694 → 720 claim's endpoint reproduces.
- ✅ EP1 core: unresolvable scope on a no-advisory scanner blocks with
  both remedies named (suite, exercised live); partial drift on a
  boundary scanner blocks too (the widened class).
- ✅ EP3: hook-plane registry carries `--require-terms`; leakscan
  without a list refuses (rc=2) naming the remedy; a hookless-clone
  commit blocks rather than half-scanning (suite); CI plane renders
  `🟡 partial` in both environments, never a plain ✅; `--json` carries
  `partial` and the board's `terms` block.
- ✅ Contract-test narrowing is genuinely the complement: the CI ban
  stands, the hook demand is asserted, `full_cover_flag` pins the
  render — strictly stronger than the both-planes ban it replaced.
- ✅ LS1: injection payload in a child `why` survives as inert `%0A`
  text, real annotation still emitted; `%` encoded first (unit-pinned).
- ✅ LS2: shebang-less executable blocks cleanly, summary survives.
- ✅ LS3: out-of-tree symlink refused with nothing executed; in-tree
  symlink still runs.
- ✅ LS4: unknown local keys refused; key-set/parser drift pinned.
- ✅ LS5: disabled local check keeps `local: true` in JSON and render.
- ✅ A5b: parent row live on the real estate — parent first, `wired`,
  its own scope declarations printed; 13 children counted without it;
  the parent-specific remedy renders when absent (suite).
- ✅ `leakscan-terms.example.txt` exists at the path the CONTRIBUTING
  template and the board remedy both name; the once-per-machine step is
  documented in the child template with the block explained as
  deliberate.
- ✅ Term-list handling leaks nothing: the board prints the list's
  *path* only; CI never holds a list, so no term can reach a runner log.

**Scanner reach**: `/security-review` discharged as stated in the brief
(landed delta, nothing in flight it can read; running it would scan this
verdict pre-commit). The security lens ran manually: the workflow-command
injection surface (LS1) verified closed, the seam's execution surface
probed (LS3 both directions, TA1's scope escape found adjacent to it),
term-list secrecy checked end-to-end.
