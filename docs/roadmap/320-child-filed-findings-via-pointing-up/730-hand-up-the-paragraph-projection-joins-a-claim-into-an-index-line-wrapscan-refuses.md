- [ ] 🔎 **Hand-up: the paragraph projection joins a wrapped claim into one
      index line, which a child that runs wrapscan on its index refuses**
      `[tool]`. Handed up from a private child on 2026-10-18 under
      `PROPAGATION.md` § *Pointing up*, measured at a queue run's landing
      (Opus 5.5, no reviewer). Formed against the child's tree with this
      repo's `tools/board.py` at `351d718`; stated class-only.
      Consideration and remediation are atelier's; the child stops here.
      **The collision.** `28ef94a` (the 320/450 §1 fix) projects an item's
      logical first paragraph, so a `(claimed …, wt: …)` block on line two
      now reaches the index — as intended. The rendered entry puts the whole
      claim text ahead of the title on ONE index line. In the child, the
      index line for a claimed item came out at 321 columns. The child runs
      `wrapscan` enforced over its whole tree, generated `docs/ROADMAP.md`
      included (this repo scopes wrapscan to its doctrine dirs, so it never
      meets the case), and the commit hook refused the landing. A claim is
      a multi-line block whenever it names a worktree path, so on such a
      child every claim commit reds the hook once the index is rebuilt on
      the new projection.
      **Measured:** one rebuild with the sibling checkout's `board.py`
      while one item was claimed; 207 index lines changed; `wrapscan` 1
      finding, the claimed item's line, 321 columns over the 85 limit; the
      commit refused. The child's stopgap: rebuild with the pinned
      `board.py` (previous projection), which `board --check` accepts under
      the grace until 2026-11-18.
      **The child's options, for atelier's notice to children:** exempt
      the generated index from wrapscan; keep claims short enough for one
      index line; or a projection that caps or wraps a claim fragment in
      the index. The last is atelier's to decide; the first two are the
      child's, and the CHANGELOG notice may want to name the case so other
      children meet it at their pin bump rather than at a landing.
      review: not warranted — a hand-up of one measured finding; the fix is
      atelier's to decide.
