- [x] **REVIEWED 2026-10-18** (from session e1d4097c)
      **Review the first real `/atelier:queue-run` against its spec.** Mike,
      2026-10-18: *"The parallel session that I used "/atelier:queue-run" has
      finished. Review its whole session transcript to see if everything
      worked as specified and if there are any improvements we should put on
      the board for it"*. The session is `8e498ef1`: opened bare, 1h54m, five
      agents. It loaded the skill as it stood before `180/090` and `180/100`.
      Owed: a clause-by-clause check of its transcript against that skill
      text, the prompt and doctrine, with every gap filed as its own item.

  **Closed 2026-10-18.** Read in full: the transcript's 22 turns, every
  tool call, the five dispatch prompts and every permission refusal. **What
  worked as specified:**
  - It stated its session id and model at open and checked load before each
    wave.
  - It saw a peer's live claim, stayed off it, and held the dependent brief
    (`160/900`) until that peer landed.
  - Every claim went to `main` before its work. It used a separate records
    worktree rather than absorb the peer's staged files.
  - It ran the full suite on a worker's head before landing, and did not
    take a cancelled CI run as a pass.
  - It told workers to rebase when `main` went red. It declined an item's
    proposed fix that would have blocked ordinary commits, and surfaced
    that decision.
  - Each item was closed with its record. The close had the identifiers
    block, the peer's status, and an honest account of its stop.

  **Gaps, each filed:**
  - `180/120`: four of five dispatches had no scratch directory or terminal
    marker, and 50 files were left in its scratchpad.
  - `180/130`: three briefs were landed unread.
  - `180/140`: it stopped by judgement, with the remaining items untriaged.
  - `180/150`: its decision went into prose, not through the decision
    device.
  - `180/160`: worktree names carry no session id, which caused a wrong
    rule-4 refusal.

  The run had no brief after the invocation, so it used the default
  selection order. It ran the skill as it stood before `180/090`.
