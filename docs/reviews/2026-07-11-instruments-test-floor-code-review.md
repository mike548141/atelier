# Code review — instruments/ test floor (commit `8536971`)

**Scope:** `HEAD~1..HEAD` at `8536971` (the instruments test floor: the
`node:test` suites, the testability refactor of `ccrepo`/`cctranscript`, the
synthetic fixture, the `ci.yml` wiring). High-effort multi-angle review: 8
finder agents (3 correctness — line-by-line, removed-behaviour, cross-file
tracer; 5 quality — reuse, simplification, efficiency, altitude, conventions),
~14 deduped candidates, each independently verified (most empirically, by
running the failure). 12 survived: 10 CONFIRMED, 2 PLAUSIBLE; report capped at
the 10 most severe.

**Reviewer:** Fable, separate session (2026-07-11, session `738f1fbc`), while
the builder session was still open elsewhere. Findings summarised below;
verbatim report in that session's transcript.

---

VERDICT: PASS-WITH-FINDINGS — 10 confirmed, correctness first.

1. **[major] Timezone-dependent test.** The `--by-day` fixture timestamps
   (03:00Z/04:00Z) straddle local midnight at UTC-4/-3:30, so the suite fails
   in those zones (proven: `TZ=America/Halifax`) while CI's UTC runners mask
   it — the new floor was itself flaky.
2. **[major] The documented run command didn't work.** `node --test
   instruments/` can't discover `test_*.js` (not node:test's naming
   convention); Node 24 errors MODULE_NOT_FOUND, Node 20 discovers nothing.
   `ci.yml` hand-enumerated the files, so a future test file could exist yet
   silently never run in CI.
3. **[major] The testability seam was half-done.** The `require.main` guard
   deferred only `main()`; help/validation parsing with `process.exit` paths
   still ran at module load against the *requiring* process's argv — a host
   with `-h` in its argv got the instrument's help printed and was killed
   (proven live). Tests passed only because node:test children have empty argv.
4. **[minor] Crash on missing `modelName`** — `shortModel(mb.modelName)`
   unguarded, outside the try/catch: a drifted ccusage breakdown row killed
   `--by-model` with a raw TypeError.
5. **[minor] Crash on envelope drift** — `JSON.parse(out).session` undefined
   (ccusage renaming its key) reached `aggregate()` as a raw "not iterable"
   stack instead of the friendly failure message.
6. **[minor] Crash on dangling symlink** — unguarded `statSync` in ccrepo's
   projects walk (cctranscript guards the same walk; reproduced).
7. **[minor] `main()` invoked bare with no `.catch`** — index-build failures
   became unhandled rejections; under some runtime modes that's exit 0 with no
   output, a silent success signal from a failed run (the EVIDENCE §14 class).
8. **[cleanup] `pt` painter duplicated `paint`** verbatim in `styleInline`,
   40 lines apart — a future escape-handling fix would silently miss one copy.
9. **[cleanup] Explicit-path branch hand-built the session record**
   `allSessions()` already constructs, with divergent label fallback and a
   hardcoded `mtime: 0` that rendered a blank timestamp in list view.
10. **[cleanup] `buildIndex()` communicated via mutable module-level Maps**
    while `aggregate()` took its index as a parameter — a caller could consult
    a silently empty index.

Cut by the severity cap (real, least severe, recorded not fixed): the
over-broad export list with impure `readTurns` under a "pure functions"
comment; cross-instrument `cwdFromLog` duplication (PLAUSIBLE —
`instruments/README.md` deliberately isolates parsing per tool); a duplicate
child-process spawn in the cctranscript tests.

---

**Disposition (2026-07-11, same day, follow-up session):** all ten **[fixed]**
and pinned by tests where a test can hold them (suite 20→26):

- (1) fixture timestamps moved to midday-UTC minutes apart — same local
  calendar day in every real offset (-12:00..+14:00); suite proven green under
  `TZ=UTC`, `America/Halifax`, and `Pacific/Chatham` (+13:45).
- (2) renamed `test_*.js` → `*.test.js` (git mv); the honest correction to the
  finding's suggested fix: node:test *directory* args are rejected by Node 22+
  and quoted globs need Node 21+, so the documented + CI command is the shell
  glob `node --test instruments/*.test.js` — expands at run time, so a future
  test file can't skip CI, and works on every Node the job might pin.
- (3) help/validation moved into `checkArgs()` called from `main()` (ccrepo)
  and into the `require.main` guard (cctranscript); pinned by require-survival
  tests that spawn a host with `-h` / conflicting flags in argv.
- (4) `shortModel` made total (`'unknown'` fallback), pinned incl. the
  missing-`modelName` fold; (5) `Array.isArray(sessions)` guard with a
  friendly message; (6) `isDir()` try/catch mirror of cctranscript's, proven
  against a planted dangling symlink; (7) `main().catch(…)` → stderr + exit 1,
  proven against a missing `~/.claude/projects`.
- (8) `paint` gained a defaulted `on` param; `pt` deleted; (9) one
  `sessionRecord()` constructor for walked and explicit-path routes, real
  `stat` mtime, pinned by a `--list --json` contract test; (10) `buildIndex()`
  returns its maps; `label()` takes the map explicitly.

Both instruments re-driven live after the fixes (ccrepo table unchanged;
cctranscript list/help/explicit-path). Full floor green: 205 Python + 26 Node
tests, secretscan/leakscan/licenscan/linkscan clean. The three cut-by-cap
items stay recorded above, deliberately unfixed. Gate cleared.
