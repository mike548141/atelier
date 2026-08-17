- [ ] 🔎 **`board`'s action word is the only bare positional in the registry,
      and `755b25b` fixed the call site rather than the signature.** That
      commit stopped `board check` aborting on the floor's rendered argv by
      swapping `parse_args` for `parse_known_args`, which was right and
      urgent — the check was blocking, not degrading, in atelier and every
      child. But the shape underneath is unchanged: `action` is a
      **positional with `choices`, `nargs="?"`, declared in front of `paths`
      (`nargs="*"`)**, so the first path is bound to `action` and rejected.
      Reproduced at HEAD 2026-08-17:
      `python3 tools/board.py check --root . docs/ROADMAP.md` → exit 0;
      `python3 tools/board.py --root . docs/ROADMAP.md` →
      *"argument action: invalid choice"*, exit 2. Nothing about the floor is
      special — **any** invocation that omits the literal `check` aborts,
      including the one a session reaches for first. This session opened by
      typing `board.py --check .` and got exit 2 before doing any work.
      🔎 **It is the odd one out, and that is the durable risk.** Every other
      entry in `floor.py`'s registry leads with a flag or with nothing —
      `sizescan` is registered `--check --root {root} {scope}`, a flag, which
      is the house precedent. Only `board` carries `hook=["check", …]`. So its
      correctness rests on someone remembering an extra token that no
      neighbour needs, and the next registry edit made by pattern-matching the
      others reintroduces the abort.
      🎯 **The fix is in the signature, not the call:** make the action a
      `--check`/`--rebuild` flag matching `sizescan`, or drop `choices` and
      validate after parsing, so a bare path list **degrades** rather than
      aborts. Either removes the special case from the registry. Left unfixed
      deliberately — it changes the CLI surface every child's hook calls, and
      the acute break is already closed, so it wants its own claim rather than
      a rider on a green tree.
      *Found by the `faves` session that filed `070`, reproducing the argv
      abort against its own shim — which inherits the same failure, and is a
      second reason that shim goes rather than gets fixed.*
