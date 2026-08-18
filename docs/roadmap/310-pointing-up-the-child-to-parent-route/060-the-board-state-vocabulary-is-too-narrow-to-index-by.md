- [ ] 🎯 **The board's state vocabulary is too narrow to index work by** —
      `[M][docs]` — **filed from a child (faves) 2026-08-18 by the § *Pointing
      up* route, on Mike's ruling that this is the house's to decide.** Options
      are **offered, not recommended**; atelier may use, adapt, replace or
      decline any of them.

      **Mike's ruling, verbatim, which is what makes this an item here rather
      than an edit there:**
      > *"changing the standard on the roadmap content is an atelier job, not
      > something for Faves or any of the child repo's to change or extend. I
      > support the idea of adding more status for the brackets on a job item
      > to make indexing them easier to understand the state of work (e.g. not
      > done, done, claimed, in-flight, declined, supersceeded etc etc) but
      > that is not something Faves or any child repo should try to fix. Faves
      > and any child repo can add problems and opportunities like these with
      > solution options for atelier to consider and remedy as it sees fit or
      > not at all."*

      🔑 **The 2026-07-23 "keep three" answer is not a refusal of the idea, and
      reading it as one is how this stalled.** It answered *should the BRACKET
      carry the disposition* — no, the bracket answers "is work owed?" and the
      disposition goes in prose. Mike's 2026-08-18 words are about **indexing**:
      being able to see, from the generated board, what state a body of work is
      in. Those are different questions and the second was never put.

      **The measured instance, from faves' board (55-venue static site, ~80
      items).** Three items sat as `[ ]` while carrying a finished ruling —
      *parked*, *ruled not to fix*, *superseded*. Two child sessions in one day
      read the index, saw an open checkbox, and treated settled questions as
      takeable work; one of them proposed a local `[-]` bracket, which is the
      overreach this route exists to prevent. **Root cause was not the
      vocabulary** — the child's copy of the legend had dropped the
      *"delivered, superseded, or declined"* clause, so `[x]` read as
      *delivered* and nobody reached for it. **But the vocabulary is why the
      dropped clause was costly**: a disposition that lives only in prose is
      invisible to the index, so the index cannot answer the question Mike is
      asking of it.

      🚩 **A second, independent symptom in the same place:** `board.py` renders
      every `[x]` as **`✅`**. A declined or superseded item therefore wears a
      green tick in the generated index, which reads as *delivered* to anyone
      scanning. **Generator and vocabulary are one question** — any answer below
      that adds meaning to `[x]` without touching the renderer leaves the index
      saying the same thing about all of them.

      **Options, in increasing cost. None is recommended; each is stated with
      what it breaks.**
      1. **Renderer only, vocabulary untouched.** `board.py` reads a leading
         disposition marker from the item's first line (`✅ SHIPPED`,
         `⏸️ PARKED`, `⛔ DECLINED`) and renders *that* glyph instead of `✅`.
         Keeps the tri-state ruling intact; costs a parse of prose, which is the
         fragile part, and gives no machine-checkable guarantee.
      2. **A disposition field, not a bracket.** `[x]` stays one state; the item
         carries a structured `disposition:` line the generator reads. Honours
         *"never a fourth bracket"* literally, is checkable, and adds a field
         every item must now get right.
      3. **More brackets, which is Mike's own phrasing** — *not done · done ·
         claimed · in-flight · declined · superseded*. Answers the indexing
         question most directly and reverses 2026-07-23; note *in-flight* is a
         genuinely new state (a claimed item that has started) which the current
         `[~]` conflates with *claimed*, and that conflation is itself causing
         drift (see `070`).
      4. **Two axes.** Bracket keeps *is work owed*; a second glyph column
         carries the disposition. Most expressive, most to learn, and the widest
         change to every board in the estate.

      ⚠️ **Whatever is chosen reaches ten children at their next pin bump** and
      every existing item is mis-marked until swept. `030` in this section is
      the precedent for costing that reach.

      📎 **The child's local state, so nothing is done twice:** faves has
      **withdrawn** its local extensions of the legend, quotes this repo's four
      states verbatim, and holds one dated, self-removing pending-upstream line
      naming this item. Its own items were re-marked to the *existing* standard
      (disposition in prose) — that is applying the rule, not changing it.
