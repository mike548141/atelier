# 2026-11-20 · 0915 UTC — The board's next shape: open-only index, archives cut into the store, every repo on the board

**Session:** `19378351`, Claude Opus 5.5, opened by the principal in the VS Code extension
with a question about how the board works. Orchestrator; workers on Opus 5.5 (`010/210`,
`010/220`) and Sonnet 5.5 (`010/240`) in their own worktrees; children's work run as
headless sessions inside each child through `ccfleet`, so each child is billed for its own.
No review-tier model used; no review run.

## What the principal asked and answered

- He described the board from memory and asked whether every repo keeps it. The
  description was right on the per-item files; the index is generated and claims live in
  the item; a done item stays in its file (his words: *"I never said the file gets moved,
  my intention is the file stays as you described and it builds up git history as its
  edited etc."*).
- His words on scope, recorded in `010/230`: every repo but archives and forks keeps the
  house board, and the health sweep finds and fixes the ones that do not.
- His words on the frozen archives, recorded in `010/220`, which supersede a 2026-11-14
  pick to leave them whole.
- Four answers (picks from offered options, not rulings): the index becomes a summary
  table plus unfinished items; archives are split with a move as the fallback; the
  changelog stays one file and is exempt; the one never-adopted, unforked, unarchived
  repo is adopted fully.

## Landed in atelier

- `010/030` closed: the split-board rollout is complete. A first reading said two
  children were unconverted; six local checkouts were behind their remotes, and the
  claim was withdrawn in the same conversation.
- `010/210`: `board.py` writes the new index (816 → 470 lines here); the old form passes
  `--check` until 2026-12-04 (`010/250` removes the grace). Pass queued `160/1670`.
- `010/220`: `tools/archivecut.py`; this repo's `ROADMAP-DONE.md` cut into 218 item files
  under `990-done-before-the-split/`, rebuilt byte for byte, 157 link edits. Pass queued
  `160/1680` (widened by `010/260`).
- `010/230`: `fleet-sweep` healthy item 6 fails a repo with no board, cuts archives,
  exempts the changelog; the survey exempts forks and adopts an unpinned repo.
- `010/240`: the repo template scaffolds the per-item board and the split session log.
  Pass queued `160/1690`.
- `010/260` closed: RECORD.md no longer names the retired archive. Filed `010/270`
  (where a rotated session-index tail goes now, the principal's to answer), `010/280`
  (five rough edges from the first fleet run), `210/450` (ccfleet skips jobs sharing a
  label), `320/890` (licenscan cannot read CC0-1.0), and a shape for `320/880` (a closed
  item is a record by its state line, answering a peer session's finding without a move).

## Children

Nineteen children with a board rebuilt their index in the new form; eleven cut their
frozen board archive and three their session archive, each proved byte for byte by the
tool, every one green on CI at its pushed head. One cut fell back to a whole-file move
(no checkbox entries). Two adopted children without a board got one, and the
never-adopted repo was adopted. One public child's commit went through its contributor
gate after the gate's owner rebuilt its corpus index; this session read the packet as
the non-writer and attested it. One private child with live sessions rebuilt its own
index; its archive cut waits until it is idle.

## Left open

- Three cold passes (`160/1670`, `1680`, `1690`) wait on the principal's approval for
  review-tier time.
- `010/270` waits on the principal. Every child's atelier pin is far behind main; a pin
  sweep is the fleet-sweep's work, not taken here.

## At close (2026-11-21 UTC, his picks from offered options)

- The three cold passes: *"Next weekly drain (Recommended)"*; nothing runs before it.
- The fleet pin sweep: *"Later"*.
- `010/270`: a typed reply, recorded in the item; its reading is being confirmed.
