- [ ] 🎯 **Fleet rollout of the split board — `faves` done, `ros` and `shed`
      open; order and timing Mike's.** atelier is the worked example
      (board-store ADR 2026-08-15). **`faves` migrated 2026-08-17** in its own
      session (`672ad17` split · `d57e359` doctrine · `54ba716` record):
      6,274-line board → 48 sections / 54 item files / 271-line index, a 96%
      cut to the session-start read, and the `board` floor check live in a
      child for the first time. Remaining, measured at HEAD 2026-08-17 (the
      earlier figures here read 5,213 / 3,125 / 1,853 and were all low —
      `faves` alone was out by 4,421 lines): **`ros` 5,513** and **`shed`
      3,465**, both trees clean. Per repo: run the migration split, adopt the
      board floor check (already reaches every child via the registry — passes
      as out-of-scope until the directory exists), and carry each repo's own
      conventions across. **The work runs in the child's own session**
      (PROPAGATION § The problem — a child session runs in the child repo),
      as `faves` did.
      *What `faves` proved, so `ros` and `shed` need not rediscover it:* the
      cut needs no judgement — an item is a column-0 checkbox plus its
      indented continuations, which is the grammar the monolith was already
      written in; verify losslessness as a **multiset over every non-heading
      source line**, not by eye; **the links are the real work** — every
      `ROADMAP.md` link is relative to `docs/` and breaks two directories
      down, and a repointer that tests only one side of `](` silently
      repointed 40 of 102 and reported success (`linkscan` caught it); the
      generated index needs `.wrapscanignore` + `.pathscanignore` entries (a
      115-column banner, and link *text* that is path-shaped); and
      `tools/board.py` in a child is a **shim, not a copy** (ADR 0008).
      *Gate note:* this item read "gated on this cycle's review closing" and
      `faves` shipped with the cycle still open on BS1 — so both of BS1's
      probed slips (a rebuilt-but-unstaged index passing the hook; a sibling
      session's dirty state line absorbed by `rebuild`) now ride in a child
      too, and any further rollout inherits them until BS1 is ruled.
