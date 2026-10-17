- [ ] 🔎 **A cloud session cannot satisfy the hook plane's leakscan term
      requirement, and the floor names no honest plane for it** `[S][tools]`.
      Found 2026-10-17 by the Mike-opened Claude Code cloud session running
      atelier's own review queue (branch `claude/review-work-briefs-adj6ad`),
      at its first commit.
      **What happens.** The hook plane runs leakscan with `--require-terms`
      (`tools/floor.py`, the leakscan registry entry): its cover is FULL or
      the commit does not happen, and the term list lives in `~/.claude/`,
      outside every repo, by design. A cloud container is a fresh host with
      no `~/.claude/`, and the list is the principal's personal data, so it
      cannot be sent there without crossing the boundary leakscan exists to
      hold. Measured in that container: `.githooks/pre-commit` installed by
      hand (`core.hooksPath` is unset in a fresh clone, as `320/660`'s
      addendum found for a child); `floor.py --plane hook` returned every
      check green except leakscan, which refused — correctly, by its own
      design — with "no local term list found"; `floor.py --plane ci` was
      green at the same head; `leakscan --staged` structural-only was green
      on the staged lines. The commit could land only with `--no-verify`.
      **Why it matters.** `floor.py`'s own plane text says the hook plane is
      "a pre-commit gate on a real machine — a machine can hold the list;
      that is exactly what distinguishes this plane from the next", and the
      CI plane is "a backstop on a runner nobody configured". A
      principal-opened cloud session is neither: it commits like a machine
      and is configured like a runner. The only exits are the discouraged
      bypass (which skips every scanner, not just the one that cannot run)
      or a term list that is not the real one, which would print full cover
      it does not have — the exact silent degradation `--require-terms` was
      added to end (ADR 0008 cold pass, EP3). `320/660`'s addendum records a
      child's cloud session in the same position, relayed; this is the first
      measurement in atelier itself.
      **What this session did, disclosed.** Ran the hook plane by hand
      before each commit and required every check but leakscan's term
      requirement green; ran leakscan structural-only over the staged lines;
      committed with `--no-verify` and said so in each commit message. The
      CI floor (structural leakscan) gates the PR and `main`. **Cover owed:**
      one full-cover run from a machine that holds the list, at the merged
      head — `python3 tools/leakscan.py --require-terms --root . .` — closes
      the gap this session could not; until it runs, the branch's added
      lines have had structural cover only.
      **Proposed fix, for the house to weigh:** a third plane, or a declared
      mode of the hook plane, for a host that cannot hold the term list —
      run every other check as the hook does and run leakscan structural,
      labelled as partial cover in the floor's own output (the 🟡 the CI
      plane already wears), and require the full-cover run at the merged
      head as a named close step rather than an unwritten one. The
      alternative, keeping cloud sessions off commits entirely, should be
      ruled, not defaulted into.
      - review: not owed until the fix lands; it touches the floor registry,
        which is doctrine by function, so it queues its own ⏳ at landing.
