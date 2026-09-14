- [ ] **The delivery vehicle shipped but was never installed — the hand-carried
      prompt this section retired never actually stopped.** This section's own
      README records the pattern as built 2026-07-22 and its executor trial
      concluded 2026-08-03: `CONCURRENCY.md` § *Orchestrated queue runs*,
      `ECONOMICS.md` § *the orchestrated-run tier split*, and the plugin-bundled
      `queue-run` / `session-onramp` skills, whose own header calls the skill
      "a delivery vehicle: it shrinks a hand-carried run prompt to an invocation
      plus per-run overrides." Checked 2026-09-14: the principal's global Claude
      Code settings carry `"enabledPlugins": {}` — atelier's own plugin
      (`.claude-plugin/plugin.json` + `marketplace.json`, install path documented
      in this repo's README: `/plugin marketplace add mike548141/atelier` then
      `/plugin install atelier@atelier`) has never been installed anywhere, on
      this machine, checked child repos included. Consequence, evidenced: the
      principal's own personal session-opening prompt (outside this repo, not
      atelier's to hold — see § *Estate resources* in the floor block) kept
      being hand-carried and hand-edited turn over turn for two more months
      after this pattern was declared done, because there was never a `/atelier:
      queue-run` invocation for it to shrink into. A pattern's doctrine and its
      trial can both be green while the one step that makes either reachable —
      installing the thing — is simply never done and nothing here checks for
      that.
      Two follow-ons, not yet actioned: (1) install the plugin and confirm
      `/atelier:queue-run` actually shrinks a real run prompt to per-run
      overrides in practice, not just in the skill's own description; (2) the
      per-run **spend directive** as currently framed leans on a pool/budget
      reading ("how hard to drain the pool… which pool, how much" —
      `CONCURRENCY.md` § *Orchestrated queue runs*, "Deliberately not in this
      doctrine"; `ECONOMICS.md` § *Know which pool*) — the principal's own
      restated intent (2026-09-14, this repo) is closer to *value-efficiency*:
      achieve the goal in a way that provides value to the principal, using the
      cheapest model/resource (including CI runners) that returns the same
      value rather than defaulting to the most capable one. Worth checking
      whether `ECONOMICS.md`'s existing tier-split reasoning already carries
      that framing or whether the spend-directive language should be widened to
      say it explicitly, so a run that reads only the skill doesn't infer
      "spend" as "budget" alone.