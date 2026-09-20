- [ ] 🔎 **Hand-up: nothing catches an orphaned session-detail file once the
      session log is an index.** Filed from the public child `tuhura`
      2026-09-20 (finding F7 of the rule-4 cold pass on its session-log
      split). The child's own intent record flagged this as a residual it
      was accepting; the review found the residual is **half already
      solved**, which changes what is left to build.

      **The shape.** `RECORD.md` § *The session log* sanctions splitting the
      log into a short index plus per-session detail files. That creates two
      artefacts that can disagree, with nothing mechanical holding them
      together.

      **The half that is already guarded.** `linkscan` fails a commit whose
      index line points at a file that does not exist — the dangling-pointer
      direction is covered today, in both planes, and the child verified it
      resolves nine of nine at its head.

      **The half that is not**, and it is the quieter direction:

      - a **detail file with no index line** — written, committed, and
        invisible to every session that reads only the index, which is what
        the index exists to make them do;
      - an index line whose **date or slug disagrees** with the name of the
        file it resolves to, which `linkscan` passes because the link still
        resolves.

      Both are the same class the estate keeps re-recording: a derived or
      paired artefact drifting from its source with no collision to fire.
      The index is read at every session open, so a record that never
      appears there is a record that functionally does not exist.

      **Why here and not in the child.** One source. The split-log shape is
      atelier's, sanctioned in `RECORD.md`, and every repo that adopts it
      inherits the same gap; a check written in one child would have to be
      copied into each of the others, which is the vendoring failure ADR
      0008 was written after. The child has deliberately not built it.

      **Cheap, on the evidence**: a directory listing against the index's
      parsed lines, set-difference both ways. Nearest existing home looks
      like `linkscan` (it already parses these lines) or a small sibling
      beside it; which, and whether it enforces or warns, is atelier's call.

      review: not warranted — a finding filed for consideration, taking no
      decision.
