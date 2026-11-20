# 2026-11-20 · 2026 UTC — the session index retired; the folder is the log (Opus 5.5, worker)

A worker of session 19378351 (queue orchestrator), in its own worktree
(`worktree-agent-a8696f668ed5bde69`), building board item `010/270` on the
principal's pick of 2026-11-20 UTC, *"Retire SESSIONS.md"*, after his words
*"This does not sound like doctrine, they should not be in one big sessions
file in the first place"*. This is the first session record written with no
index line: the file itself is the record, and the folder is the index.

## What was built

- **`tools/archivecut.py` retires a one-file session log, files only.** Each
  entry of `docs/SESSIONS.md` (and of a frozen `SESSIONS-ARCHIVE.md`, oldest
  first) goes word for word into the session file it links: the one it opens
  by linking, else the only one it links anywhere. It sits right after the
  file's first line where that is a `# ` heading, so the title stays first
  and the old index line reads as the file's summary, under "From the
  retired session log" and a comment giving its source and line numbers. An
  entry linking no session file gets a new file named for its date:
  `<date>-<HHMM>-<slug>.md` when it states its time straight after the date,
  a two-digit day counter in the time's place when it does not (a time is
  never guessed). Every non-entry line goes into `docs/sessions/README.md`,
  fenced, so the old `indexscan` markers are kept as record and act on
  nothing. A README the folder already had is kept above the tool's part.
  The proof runs before anything is written and there is no fallback.
  `--verify` rebuilds from disk, including an archive cut by the earlier
  route, whose detail files it reads as they stood before the index was
  retired.
- **Link paths:** a link into the folder loses its `sessions/`, any other
  gains `../`, so each maps back exactly; normalising would have lost the
  log's own `../docs/ROADMAP.md` spellings. A same-page anchor or a link to
  the log itself fails the proof.
- **Guards and instruments:** `ccclose` reads the folder, and accepts a kept
  index until 2026-12-04 (`010/290`); `pathscan`, `coldsweep` and `sizescan`
  keep a kept index as a record until no repo has one.
- **Doctrine:** RECORD.md § *The session log* (folder only, the rotation rule
  retired, one sentence of why the index existed), CONCURRENCY.md's recovery
  sweep and worktree line, REVIEW.md, CLAUDE.md, REPO-STANDARD.md, the
  template (`docs/sessions/README.md` in, `SESSIONS.md` out), `create-repo`,
  `fleet-sweep` and its prompts, `tools/README.md`, the CHANGELOG with a
  notice to children.

## The run on atelier

340 entries: 295 placed in the session file they link, 45 in new files (14
with a day counter). 358 non-blank lines matched as a multiset, 332 link
paths re-pointed and each mapped back, the log rebuilt byte for byte from the
outputs as written, 257 existing session files unchanged but for the placed
entries; `--verify` passes from disk after the commit.

## Found on the way

- **The answer's date.** `010/270` records the pick as "2026-11-21 UTC"; its
  commit is at 20:25 UTC on 2026-11-20, so that was the New Zealand date. The
  item's DONE note says so; the answer line is left as written.
- **Names that do not sort by start time.** Of the names already here, three
  `NN` files of 2026-07-13 (`-50-`, `-51-`, `-52-`) sort after that day's
  `HHMM` files although they came first; two files share `2026-07-11-39-`.
  Of the new files, the day-counter names on days that also have `HHMM`
  names (2026-07-14, 2026-07-15, 2026-07-21, 2026-07-22, 2026-08-09) sort by
  counter, not time. None is renamed: the rule keeps old names, and no time
  is known for the new ones. The newest-few read is unaffected.
- **pathscan (warn-only)** now reports three census snapshots naming
  `docs/SESSIONS.md` as a path that does not exist; they are records, left
  as written. **attribscan** warned on 17 moved index lines (advisory, the
  class `010/280` item 5 already names).
- `010/280` item 2 (the session-index line too wide to wrap) has no subject
  left: the tool writes no index line.
- A read-only dry run on fourteen children: every session log would pass its
  proof (one child keeps its own sessions README, which is kept above the
  tool's part).

## Identifiers

- **Session:** worker of 19378351 (agent `a8696f668ed5bde69`), Opus 5.5,
  2026-11-20 about 20:26 to 21:20 UTC.
- **Commits:** `b68cf410` (tool, guards, doctrine), `e5f9f245` (atelier's
  run); this record's own commit is named in the closing message.
- **Pull requests:** none.
- **Board:** completed `010/270`; created `010/290` (grace removal) and the
  `⏳` pointer `160/1700`.
- **Worktrees and branches:** `worktree-agent-a8696f668ed5bde69`, left for
  the orchestrator to merge; not pushed.
- **Agents:** none launched.
- **Other repos:** none written; fourteen read for the dry run.
