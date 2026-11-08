- [ ] 🎯 **Fleet rollout of the split board** — nine children split on
      2026-08-17, two monolithic boards left; order and timing Mike's.
      atelier is the worked example (board-store ADR 2026-08-15) and its own
      split landed then. The rollout itself did not run from here: Mike sent
      one standing prompt to one session per repo, and each child cut its own
      board in its own session, which is what **PROPAGATION § The problem**
      already required. This item is therefore the fleet's *record*, not its
      plan — and it has been wrong in both directions before, so every figure
      below names what it counted.
      **Measured 2026-08-17 1057 UTC**, one pattern applied to every repo
      under the estate root: a `docs/roadmap/` directory ⇒ split; `wc -l
      docs/ROADMAP.md` at the split commit and at its parent for the two index
      figures. A peer atelier session re-ran the same count independently and
      agreed; `cbom` split *between* two reads twenty minutes apart in this
      session, so the state below is a timestamp, not a standing fact.

      | child | split commit | monolith → index | note |
      |---|---|---|---|
      | `faves` | `672ad17` | 6,274 → 268 | first child; proved the playbook |
      | `ros` | `98ec234` | 5,513 → 384 | regenerated `5cff027` on the fixed generator |
      | `shed` | `8755a62` | 3,465 → 136 | bumped its pin twice the same day |
      | `cbom` | `8d4975f` | 1,367 → 118 | **local `main` only — no remote** |
      | `kainga` | `c6e4479` | 323 → 103 | |
      | `tuhura` | `78e31b1` | 173 → 58 | |
      | `stewart-drive` | `a3c1c4a` | 98 → 66 | |
      | `derry-hill` | `4c67be9` | 74 → 69 | |
      | `rpi` | `4bd429c` | 245 → 69 | monolith at the repo **root**; see the correction below |

      **Still monolithic:** `docker-heap` 302 lines (tree not clean at the
      reading, last commit 2026-08-15) and `nova` 274 lines (clean, last
      commit 2026-08-09). `numen` 24 lines is **archived and never pushed**,
      so it is out of scope rather than outstanding. Per repo the work is
      unchanged: run the migration split, adopt the board floor check (already
      reaches every child via the registry — it passes as out-of-scope until
      the directory exists), and carry that repo's own conventions across.
      🚩 **Two readings the table does not make on its own.** `cbom` has no
      remote and no remote-tracking branch, so "pushed" is not a category
      there — its split exists on a local `main` and is *not* equivalent to
      the others for anything that depends on origin. ~~And `rpi` never
      migrated: it had no `ROADMAP.md` before `4bd429c`, so its board was
      *written* in the store form from nothing.~~ **Corrected 2026-11-03
      (`320/710`, the child's hand-up, re-measured here):** `4bd429c` deletes
      a 245-line `ROADMAP.md` at the repo root, which a method that looked
      only for `docs/ROADMAP.md` at the parent commit could not see, and
      inferred birth from. The inference built on it ("adoptable without a
      monolith to convert") is withdrawn. The truth is the opposite case: none
      of that monolith's 27 bullets used the checkbox grammar, so a mechanical
      cut would have produced zero items, and every state was a judgement read
      off prose glyphs.
      ⚠️ *One figure is not a correction.* `faves`' index reads 268 lines at
      `672ad17` under the definition above; this item previously recorded 271
      under a definition it did not state. Three lines, and which point in
      that session was counted is the likely difference — so it is flagged,
      not overwritten as an error. The three figures this item *did* get wrong
      (5,213 / 3,125 / 1,853, all low, `faves` alone out by 4,421) were
      corrected 2026-08-17 and are named here because the failure mode
      recurs: a rollout record adjusted by intuition rather than swept.
      *What `faves` proved, so no later child rediscovers it:* the cut needs
      no judgement — an item is a column-0 checkbox plus its indented
      continuations, which is the grammar the monolith was already written in
      (and only then: `rpi`'s board, above, is the counter-example);
      verify losslessness as a **multiset over every non-heading source
      line**, not by eye; **the links are the real work** — every
      `ROADMAP.md` link is relative to `docs/` and breaks two directories
      down, and a repointer that tests only one side of `](` silently
      repointed 40 of 102 and reported success (`linkscan` caught it); and
      `tools/board.py` in a child is a **shim, not a copy** (ADR 0008) — and
      since the generator was fixed 2026-08-17 to resolve its rebuild
      instruction per root, not even a shim: `ros`, `shed` and `cbom` all
      carry none. The `.wrapscanignore` + `.pathscanignore` entries `faves`
      needed for the generated index are also **no longer required** — the
      same fix took the banner to 69 columns and stopped the index repeating
      section paths as link text, so `faves` deleted the pair it opened.
      *Gate note:* this item read "gated on this cycle's review closing" and
      `faves` shipped with the cycle still open on BS1 — so both of BS1's
      probed slips (a rebuilt-but-unstaged index passing the hook; a sibling
      session's dirty state line absorbed by `rebuild`) ride in nine children
      now, not one, and the two remaining boards inherit them until BS1 is
      ruled. *Superseded 2026-09-20:* both slips are caught at the hook now
      (`010/020`), and that reaches every child at its next commit, since the
      children call atelier's tools.
      *Handed up by children mid-rollout and open here:* `100` (`ros`' 38
      items using `[~]` for *partially delivered*, Mike's to rule) and `110`
      (a relative path argument scanned against cwd while `--root`'s rules
      apply — 🔥, four tools).
      🚩 **A split board's item bodies are invisible to `wrapscan`, by
      construction** (`320/710` §2, 2026-11-03). `wrapscan` exempts a line
      indented four or more columns as code, and a split item's continuation
      lines are indented four or more by the board's grammar, so every item
      body in every split board is exempt. A child's reviewer measured raw
      over-width lines rising 180 → 208 across its split while the flagged
      count fell 133 → 38. So a width ruling that reads `wrapscan`'s count on
      a split board reads the state lines and legend only; read the raw count
      instead. Changing the exemption would raise every split child's count
      at once, and is not taken here.
