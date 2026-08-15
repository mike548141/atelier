- [ ] 🛑 **The board-store cold pass RAN 2026-08-15 and the cycle stays OPEN —
      a MAJOR stands; BS1–BS14 await Mike's ruling round.** The rule-4 Fable
      combined doctrine + code cold pass (taker: a cold session Mike opened
      2026-08-15 ~1120 UTC, running the brief a *different* cold session wrote
      at 1024 UTC, under an orchestrator-held context partition) returned
      PASS-WITH-FINDINGS — 1 MAJOR / 4 MODERATE / 5 minor / 4 note after
      reconcile (no phase-1 severity changed; BS12–BS14 added post-reconcile) →
      [`reviews/2026-08-15-1030-board-store-migration-cold.md`](../../reviews/2026-08-15-1030-board-store-migration-cold.md).
      Held under attack: the migration is lossless (line-multiset comparison
      of the pre-migration board against the store), suites green at every
      landing commit (1,298 → 1,321), floor green both planes with `board`
      enforced, harvestscan/pointerscan/linkscan clean, index 253 lines at
      `a9abc26`. **BS1 (MAJOR):** the hook-plane guarantee — *a stale index
      cannot be committed* — is asserted in four places (the tool docstring,
      `tools/README.md`, the ADR, CONCURRENCY) and fails in two live-probed
      slips: a rebuilt-but-unstaged index passes the hook and the commit lands
      without it; and a sibling session's dirty item state line is absorbed by
      `rebuild` under CONCURRENCY's own "stage your claim alone" recipe, so a
      wrong `✅` lands on `main` under a green hook. The MODERATEs: BS2 — the
      index projects the first *physical* line, so wrapped titles are
      fragments and claim stamps or flags on continuation lines never surface;
      BS3 — non-checkbox top-level bullets (ruling asks and one live pointer)
      migrated into section READMEs and are invisible to the index; BS4 —
      with the harvest retired the read cost is unbounded and sizescan's
      remedy for the index names a step that no longer exists; BS5 — the
      legend and claim rules moved off the ordered read. *Delta:*
      `da6ba70..15d3de2` plus the records commit and merge that landed with
      it (wt: board-per-item-0815). *Intent record:*
      `docs/sessions/2026-08-15-0610-board-store-migration.md`.
