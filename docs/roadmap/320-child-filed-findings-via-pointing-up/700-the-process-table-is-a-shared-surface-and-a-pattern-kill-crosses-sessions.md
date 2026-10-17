- [ ] 🔎 **Hand-up: the process table is a shared surface, so a pattern kill
      crosses sessions, and a run's wave size is judged by memory when CPU load
      binds first** `[S][doctrine]`. Handed up by a private child's
      orchestrated queue run on 2026-10-17, under `PROPAGATION.md`
      § *Pointing up*, at a peer session's suggestion. Two measured instances;
      the rule shape is the child's suggestion, unevidenced beyond them.
      **1. A pattern kill reached another session.** A peer session in a
      sibling repo called a load emergency on the shared machine. The
      orchestrator told its build workers to pause and stop their test runs.
      One worker ran `pkill -f "pytest -q"`, a pattern that matches every
      pytest on the machine. A different session's suite in another repo's
      worktree, about 30 minutes in, was not running afterwards (seen in a
      process listing taken before and after; cause inferred, not proven).
      The worker's prompt named no kill scope. `CONCURRENCY.md` already
      treats the index and a mid-rebase state as shared surfaces; the process
      table is the same kind of thing and is not named. **Suggested shape:**
      a kill is scoped by PID the session launched, or by the worktree cwd it
      owns (`lsof -p <pid> -d cwd`), never by a name pattern; and a dispatch
      prompt says so, because naming the scope is what binds a worker (the
      scratch-directory lesson in `CONCURRENCY.md`).
      **2. Waves were sized by free memory; CPU load ran out first.** The run
      checked `memory_pressure` before each wave (59 % free) and put ten
      builders up at once, each running a full test suite, one also running a
      second suite. Load average reached 168 (15-minute about 90 and rising)
      on a machine shared with about a dozen other sessions; a VS Code
      SIGTERM the day before had come at a 15-minute load near 135. The peer
      session asked for at most three in flight; load fell within minutes.
      Two workers' suites were also left orphaned (parent PID 1) when their
      shells went. **Suggested shape:** `ECONOMICS.md` or `CONCURRENCY.md`
      § *Waves* names a box-wide ceiling on concurrent heavy checks and the
      load measure to read before adding a wave (15-minute load average),
      not only memory. Adjacent: `320/680` (long checks under load), `020/370`
      (a scan that exhausts the machine).
      review: warranted, light — it would add a shared surface to the
      concurrency doctrine.
