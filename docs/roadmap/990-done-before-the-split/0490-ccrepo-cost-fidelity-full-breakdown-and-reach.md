- [x] **ccrepo — cost fidelity, full breakdown, and reach** (Mike, 2026-07-11) —
      three strands to make the DevFinOps view truer and more accessible; all
      three now addressed (the VS Code *build* stays a separate decision):
      - [x] **Actuals vs estimate — show both.** DONE 2026-07-11 (Opus, session
            38): config confirmed (USD Max-20x, all Claude families covered) and
            the code built. `~/.claude/ccrepo-billing.json` (machine-local, never
            in a repo; absent ⇒ estimate-only, byte-identical JSON contract
            preserved; malformed ⇒ ignored-with-warning, never fatal) drives an
            **Actual** column beside **Est (API)**: `covers[]` matches model
            families by prefix (after `claude-` stripped), `perTokenModels` carves
            one back out; covered tokens cost $0 marginal, the sunk plan fee is
            apportioned per repo by covered-token share (falls back to total-token
            share if nothing covered ran in range), uncovered models keep the
            API-rate figure. **Actual = plan share + uncovered spend**, so TOTAL
            Actual = fee + all uncovered — proven live: estate-wide Est
            US$2,305 vs Actual US$200 (the whole plan fee), and `--by-model`
            children sum to their repo. Both columns convert together under
            `--fx`; `--no-billing` forces estimate-only. Multi-month outlay +
            overage thresholds out of scope v1, stated as footnotes. 8 new pure
            tests (`loadBilling`/`coversPredicate`/`actualFor`/covered-split
            fold); suite 26→34 Node.
      - [x] **Full ccusage breakdown** — DONE 2026-07-11: ccrepo now shows
            Cache Create · Cache Read · **Cache Hit** (reads ÷ prompt-side
            tokens, the point-don't-paste signal made observable) alongside
            Input/Output/Total/Cost, in the table, `--by-model`/`--by-day`
            children, and `--json` (`cacheCreationTokens`/`cacheReadTokens`/
            `cacheHitRate`); definition footnoted in the output. Tests updated
            + new `cacheHitRate` unit (fixtures now mirror ccusage's real
            shape: totalTokens includes cache); driven live — repo-level hit
            rates 95–98%.
      - [x] **VS Code UI — SCOPED 2026-07-11** (the item asked for scoping
            before building; grounded via current docs, not memory). Findings:
            the official Claude Code extension exposes **no** third-party hook
            points (no API, no contributed-view extension points; open feature
            requests confirm); Claude Code's **statusline** can carry per-repo
            cost (rich stdin JSON incl. `workspace` + live session cost;
            ~1.1 s ccrepo run needs a TTL cache) but renders **only in
            terminal surfaces**, never the graphical panel. Recommended route:
            a tiny **sideloaded companion extension** (status bar item +
            tooltip breakdown reading `ccrepo --json`; local `.vsix`, no
            marketplace; declare workspace-trust, resolve PATH explicitly),
            ~4–6 h, with a ~1 h spike (40-line extension showing the workspace
            total) as the feasibility proof. Statusline script is a free
            adjunct for terminal sessions. Build is a separate decision.
