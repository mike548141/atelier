- [ ] 🛠️ **`ccfleet`, the `fleet-sweep` and `review-drain` skills, and the
      `modelguard` hook: the fleet kits versioned in atelier.** Built
      2026-11-14 by session 559edaec (Opus 5.5, headless, started by an
      estate health sweep, orchestrator session 58027096).
      **Why:** the principal asked, 2026-11-13, verbatim: *"Also are all the
      tools and skills like this based in Atelier? Things like fable drain,
      ccmail etc alongside the guardrails like pathscan, ccrepo etc"*. 💬 To
      the options a session then offered, the principal picked the split
      (an answer, not a ruling): the general parts come here, after a scrub,
      and each estate's repo list, rulings and results stay in its private
      config. The option's own words name a private repo, so they are not
      quoted here.
      **What was built:**
      `instruments/ccfleet` (standard-library Python): `run` starts one
      headless `claude -p --model <tier>` session inside a worktree whose
      basename is the repo (the per-repo billing key), stdin from
      `/dev/null`; `drive` runs a jobs file under a load, memory and disk
      gate, optionally one job per repo at a time; `drain` keeps review
      passes running from the adopter's own queue through a three-command
      interface (`next`, `take`, `release`); `resume` finishes a cut-off
      pass in its own session; `run --in` adopts an existing worktree for a
      fold. Every estate value comes from a JSON config
      (`instruments/ccfleet.example.json`, fictional). A public repo's prompt
      that names a configured private name is refused before any worktree
      is made. 17 tests (`instruments/test_ccfleet.py`) drive `run`,
      `drive` and `drain` end to end against throwaway repos with a local
      bare remote and a stand-in `claude`.
      `skills/fleet-sweep/` (the six-part definition of healthy, the billing
      rule, the steps, and worker, task and brief-writer prompt templates)
      and `skills/review-drain/` (the four rules, drain and resume modes,
      the reviewer prompt, and orchestrator, resume and fold templates).
      `tools/modelguard.py`, a `PreToolUse` hook that blocks a session or
      subagent started with no model, with `tools/test_modelguard.py`; not
      wired by the plugin (an adopter's choice to switch on).
      **What changed in the move:** the source kits were zsh; `ccfleet` is
      Python, because zsh reads a script as it runs and an edit mid-run had
      broken every running job (the docstring keeps the lesson). The drain's
      per-drain picker, held list and priority file became the queue
      interface; the queue tool itself stays the adopter's. A sandboxed
      API-credit route the source kit described was dropped: its own review
      had failed and it is estate-specific.
      **Still owed:** a `man/ccfleet.1` page and the trimmed `--help` the
      two-register convention asks for (`--doc` prints the full reference
      today); and the rule-4 cold pass, queued as
      [`160/1450`](../160-doctrine-review-owed/1450-rule-4-cold-pass-queued-ccfleet-fleet-sweep-review-drain-modelguard.md).
