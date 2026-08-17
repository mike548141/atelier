- [ ] 🔥 **Two tests fail intermittently in the full-suite run and pass when the
      module runs alone.** Found by a parallel session rebasing onto `main`, on
      content **byte-identical to `origin/main`** (`tools/plainscan.py`,
      `tools/test_plainscan.py`, `tools/hooks/plain-reply.py` and `tools/floor.py`
      all verified identical, and none of the finder's own commits touch them).
      The two are `StopHook.test_bad_reply_is_blocked` (FAIL) and
      `StopHook.test_reason_names_the_rule_and_the_remedy` (ERROR).
      **Evidence — four full runs of `unittest discover -s tools`, same tree, same
      machine: red, green, red, green.** The module alone passes 47/47 every time.
      🛑 **Why this is 🔥 rather than a nuisance.** The tool suite gates the
      pre-commit hook and CI, so a 50% flake means commits and CI runs fail at
      random on work that is fine — and worse, the failures land on *whoever
      commits next*, not on the author. `main`'s CI is currently green on
      `5c16a59` and `f4d4cb3`, but that is a coin landing heads, not evidence the
      suite is sound.
      ⚠️ **A false lead, recorded so nobody re-chases it.** The finder first
      hypothesised an `GITHUB_ACTIONS`/`CI` env gate, because a run with those set
      came back green. The control falsified it — a plain re-run also came back
      green — so the variable is *run-to-run*, not environmental. No `tools/` code
      outside `floor.py`/`test_floor.py` reads either variable. Likely a shared
      resource or a subprocess race in the `StopHook` fixtures; **not diagnosed
      further, deliberately.**
      🚩 **This is another session's live lane.** `tools/plainscan.py` was
      uncommitted-dirty in the primary checkout while this was found, so the
      author was mid-work and may already have it. Queued rather than delivered
      (`CONCURRENCY.md` § *Stay in your lane*); **verify against HEAD before
      acting**, and close this if the live session already landed a fix.
      ✅ **FIXED in `b879b02`, and verified 2026-08-17 by a session that did not
      author the fix.** The cause is one shared state file: `plain-reply.py` kept
      its block counter at `~/.claude/.plain-reply-state.json`, so a session id
      reused across runs carried its count forward. The fix makes the path
      overridable (`PLAIN_REPLY_STATE`) and gives each test its own. The
      verification did not take the fix on report — it reproduced the defect
      first, then falsified it:
      🔎 **Reproduced deterministically.** Firing the hook repeatedly at one
      shared state file, the **third** call for a session id gives up instead of
      blocking, because the give-up path clears the counter. That is exactly the
      recorded pair — the assertion fails on one test and the other raises
      `KeyError` on `reason`. Not random: a fixed 1-in-3 cycle.
      🔎 **Control run on the pre-fix code**, extracted at `b879b02^` into a
      throwaway tree with an isolated `HOME`: **failed on runs 3 and 6 of 6**,
      `failures=1, errors=1` both times.
      ⚠️ **Two claims in the evidence above are WRONG, and are corrected here
      rather than harvested as written.** (1) *"The module alone passes 47/47
      every time"* — false. The control proves the pre-fix module fails **alone**
      at the same 1-in-3 rate, so the full-suite-versus-alone asymmetry never
      existed. That asymmetry is what sent the finder after a fixture race, which
      was the wrong scent. (2) *"red, green, red, green"* reads as a 50% random
      rate; the true rate is one in three and deterministic. The finder's
      sequence is explained by interleaving the two run modes, which increment
      the same counter.
      ✅ **The title's claim is right, and now has a mechanism.** CI cannot see
      this: every run gets a fresh `HOME`, so the counter always starts at one
      and the tests always pass. `main` being green was never evidence either
      way.
      🔎 **Post-fix measurements.** 8 full-suite runs green (spanning
      `36bd5ae..e2fddc5`, so read as green across that range rather than pinned
      to one commit) and 8 module runs green. The live counter is provably
      untouched — `~/.claude/.plain-reply-state.json` byte-identical, same
      checksum, across all 8 module runs. `test_malformed_input_fails_open` is
      the one test that does not pass the override, and it provably never
      writes: the hook returns before it reads `STATE`.
      🎯 **One thing left, and it is Mike's call — nothing guards the fix.** The
      isolation is a single line of test `setUp`. Delete it and the flake returns
      silently, at one failure in three, invisible to CI. There is no test
      asserting that the suite uses its own counter. Options: add the guard
      (~10 lines) then close; close and queue the guard as its own item; or close
      bare and accept the regression path. The verifying session recommends the
      first — a fix with no forcing function is the decay this repo's whole
      argument is about.
