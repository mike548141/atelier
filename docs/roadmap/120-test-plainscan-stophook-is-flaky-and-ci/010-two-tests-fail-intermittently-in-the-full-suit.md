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
