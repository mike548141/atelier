- [ ] 💡 **PROPOSAL, hand-up from `faves` — a RENDERED board view, offered to
      every repo rather than built in one** `[M][instruments]` — filed
      2026-09-09 by session `faves-c1`.
      🛑 **This is a COMMISSION, not a finding, and the distinction is the first
      thing to read.** No doctrine here is wrong, unworkable, ambiguous, stale
      or missing. `board.py` does exactly what it says and `RECORD.md` § the
      records describes the index accurately. What happened is that the
      principal saw one repo render its own board as a page, said it read better
      than the transcript he usually gets, and asked for it to be offered to the
      house. Filing it as a *defect* would make the record stronger than its
      source, which is the failure this section already carries three instances
      of.

  **His words, verbatim, because the ask is the evidence.**
  > *"Usually sessions just show me in the transcript but this artifact is
  > pretty good, easy to read etc. Suggest to Atelier repo that something like
  > this would be useful for all repos to track the state of work"*

  ## What the house already owns, and what it does not

  `tools/board.py` owns the store and the text index: one file per item under
  `docs/roadmap/`, state in the item's first line and nowhere else, and
  `docs/ROADMAP.md` generated from it. That design is sound and nothing below
  proposes changing it. The store is the right store.

  What no repo has is a **reading surface for the principal**. Today a session
  answering *"what is left?"* has two shapes available, and both are poor:

  | Shape | What it costs |
  |---|---|
  | Paste the index into the transcript | 45 KB in atelier, 36 KB in `faves` — scrollback, gone next session |
  | Summarise it in prose | The session picks what he sees, and he cannot check it |

  ## Three measurements, so the size of it is not a matter of opinion

  Taken 2026-09-09, at `faves` `ca06603` and this repo's `main`.

  | | atelier | faves |
  |---|---|---|
  | Generated index | 427 lines · 45 KB | 399 lines · 36 KB |
  | Items not done | 197 | 97 |
  | `[x]` lines in the index | 0 | 0 |

  Three properties of the index follow from that, and each is a fact about the
  file rather than a complaint about it:

  1. **The index carries no size and no tag.** `[S]`, `[M]`, `[js]`, `[data]`
     are written on the *item*, so the index cannot answer *"show me the small
     ones"* without opening every item file — 97 reads in `faves`, 197 here.
  2. **`⏳` items do not grep as checkboxes.** They render `- ⏳` with no
     bracket, so `grep -c '^- \[ \]'` answers 80 in `faves` where the true
     not-done count is 97. Any count taken the obvious way is quietly short by
     the three items that are *waiting on the principal* — the ones he would
     most want to see.
  3. **Done items are already excluded**, which is the half the house has
     right: the index is a work-left view, not an archive.

  🔑 **The class, stated as § The test asks.** *Would this be true in a repo
  that shares none of `faves`' stack?* Yes, in every particular. It needs no
  JavaScript, no menus, no static site — only `docs/roadmap/`, `board.py`, and
  a principal who wants to see the state of the work. Every repo on this
  doctrine has all three. That is why it is filed here and was not built into
  `faves` as a local tool.

  ## What was actually built, with its limits named

  `faves-c1` generated one page from `docs/roadmap/` and published it as an
  artifact: 97 items, grouped by theme or by size, filterable by state, live
  search, each row linking to its item file on GitHub, and a button for the
  thirteen items that need the principal rather than a session.

  🚩 **It is a one-off script in a scratch directory, not an instrument.** It
  was thrown away after publishing. Nothing about it is reusable today, and this
  item is deliberately not a request to merge it — it is offered as a worked
  example of the shape, and the parser it used is the naive half of the problem.

  ⚠️ **Three things it does NOT solve, stated because a proposal that hides its
  weak points is a sales pitch.**
  - **It reads the same state lines the index does**, so it inherits every fault
    in them. On the same day it was built, `faves` `500/010` carried `- [ ]` and
    a 🔥 above its own *"DONE — THE KEY IS DELETED"* — the board advertised a
    deleted credential as its top open item, and the rendered page would have
    repeated that faithfully. **A view makes a stale bracket more visible; it
    cannot make it true.**
  - **Titles need parsing out of prose.** Item files open with a bullet whose
    title runs into its own description, so a title has to be cut at the size
    tag or the first em-dash. That worked on 97 items and is not a contract.
  - **An artifact is a snapshot.** It is accurate at publish and silently stale
    after the next commit, which is the property the generated index does not
    have.

  ## Options, offered and not recommended — this is atelier's to decide

  1. **Do nothing.** The index is honest and cheap, and a rendered view is one
     more artefact to keep true. The principal's ask is satisfied by any session
     making a page when he asks for one, which is what happened here.
  2. **A `board.py --html` render.** The tool already parses every item; a flag
     that emits a self-contained page reuses that parse and cannot disagree with
     the index, because it is the same reader. Every repo gets it at the next
     pin bump with no per-repo work.
  3. **An instrument beside `cctranscript` and `ccarchive`.** Reads any repo's
     `docs/roadmap/`, so one command serves the whole fleet and the fleet view
     — *what is open across every repo at once* — becomes reachable, which no
     per-repo render gives. Costs a new instrument and its own tests.
  4. **Fix the index instead.** Carry size and tag on the generated line and
     give `⏳` a bracket, so the existing text index answers the questions the
     page was built to answer. Cheapest by far, helps every reader including
     sessions, and does nothing for *"easier to read than a transcript"*, which
     was the actual ask.

  📌 Options 2, 3 and 4 are not exclusive; 4 stands on its own merits whatever
  is decided about the rest.

  🎯 **One question sits underneath all four and is the principal's, not
  atelier's:** is the wanted thing a *document he is shown* or a *place he goes*?
  Option 4 serves the first, option 3 the second, and the answer decides the
  other three. It is recorded here rather than guessed at.

  🔗 Adjacent, deliberately not merged: `220/050` — the Context Atlas — is also
  an interactive page over repo state, and is held outside this repo because it
  carries estate cost detail. A board view carries none: `docs/roadmap/` in a
  public repo is already public. So the two share a shape and not a posture, and
  whoever takes this should read that item before choosing where the code lives.
