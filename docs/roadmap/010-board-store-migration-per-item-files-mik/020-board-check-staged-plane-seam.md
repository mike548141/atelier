- [x] **`board --check` reads the worktree, not the staged plane.** The check
      compares worktree item files against the worktree index, so a commit
      staging an item edit without the rebuilt index is caught only when the
      two agree on disk — the same seam harvestscan closed as HV4 (its hook
      question is the INDEX: what is this commit about to make true?). Bring
      the check to the staged plane the same way. Stated as a residual in
      `tools/README.md` and the tool's docstring at birth.
      **FUNDED 2026-08-17 (Mike's BS1 ruling, `290-ruling-round-…/050`):** build
      the staged-plane check **and** a `rebuild` source flag that regenerates
      from the index rather than the worktree (BS1 counsel (b)); name the flag
      in CONCURRENCY CF3 at landing; code cold pass queued at landing.
      **The interim wording to retire at landing (BW6, ruled 2026-08-23):**
      the staged-plane residual is spelled on five surfaces, each to be
      re-worded or dropped when this check lands — `tools/board.py` (the
      hook clause in § *Why the index is committed and checked* and the
      merged § *STATED RESIDUAL*) · `tools/README.md` § **board** ·
      `docs/method/CONCURRENCY.md` § *On a split board* ·
      `docs/roadmap/README.md` (the preamble qualifier) · the 2026-08-23
      amendment at the foot of the board-store ADR. This item's landing
      commit sweeps them; nothing machine-checks the unwind, so the list
      lives here where the work is funded.
      ---
      ✅ **BUILT AND LANDED 2026-09-20**, discharging Mike's BS1 fund of
      2026-08-17. `board check --staged` reads the git **index** on both
      sides — item files via `git show :path`, and the committed
      `docs/ROADMAP.md` the same way — reusing `harvestscan`'s own
      `WORKTREE`/`INDEX`/`git_show` plumbing rather than inventing a second
      mechanism, which is what the fund specified. `rebuild --from-index` is
      the write-side twin. The flag is named for what it **selects**, per the
      house rule against imperative flag names.
      **Both of BS1's slips reproduced before and after**, in a throwaway
      repository rather than only in unit tests: (a) an item edit staged with
      the index rebuilt but never staged passed the worktree plane and fails
      the staged one; (b) a rebuild at a dirty checkout absorbed a sibling's
      `WIP, uncommitted` line into the index, and `--from-index` renders that
      sibling from its last **committed** text instead, leaving its on-disk
      file untouched. Eleven regression tests pin them.
      **Registry wired, and verified against real children rather than
      reasoned about:** `floor.py`'s `board` Scanner runs `--staged` at the
      hook and the plain worktree form on CI. Safe in the registry because
      children do not vendor these tools (ADR 0008) — hook and code resolve
      from one atelier checkout, so flag and parser cannot skew. Probed at
      exit 0 on atelier, a split child, a newly-split child, and a monolithic
      child (which correctly reported out-of-scope).
      **The five interim wording surfaces are swept** as BW6 required:
      `tools/board.py`'s docstring (both the hook clause and the merged
      *STATED RESIDUAL*), `tools/README.md` § **board**,
      `docs/method/CONCURRENCY.md` § *On a split board*,
      `docs/roadmap/README.md`'s preamble, and the board-store ADR by
      **appended amendment**, never an edit.
      ⚠️ **Not claimed:** a commit that deliberately stages a stale item edit
      *and* a stale index together passes both planes. That is a wrong commit,
      not a plane confusion.
      🎯 **One consequence left for Mike:** CF3's dirty-sibling stop is now
      stricter than its mechanical cause requires — `010/160`. The building
      worker surfaced it and declined to decide it, correctly.
      Rule-4 `⏳` at `160/390`; this run may not take it.
