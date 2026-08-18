- [ ] 🎯 **PROPOSAL — *capture, do not compose*: a hand-written fixture can only
      ever confirm its author's own model** `[S][docs]` — filed from a private
      child 2026-08-18 via § *Pointing up*. No owner in `docs/method/` today;
      the nearest surfaces are `EVIDENCE.md` and `GUARDS.md`, and choosing
      between them is part of the work.
      **The claim.** A hand-written test fixture encodes what the author
      **expected** the tool to print. It can therefore only confirm the author's
      own model, and **it will pass forever while being wrong**.
      **The evidence is unusually clean, which is why this is filed rather than
      noted.** It ran both ways in one day, in two lanes that did not know about
      each other. One lane's protocol-version probe shipped **the opposite of
      the truth** behind a hand-written fixture that would have passed
      indefinitely — only a live run caught it. The sibling lane captured real
      output from a **loopback-only stub it stood up itself**, and hit the same
      underlying trap immediately, **because the real output contained a marker
      the author would never have thought to write**. Same trap, two lanes, one
      day, opposite outcomes decided by fixture provenance alone.
      **The proposed rule.** Where a tool parses another program's output, the
      fixture is **captured** from that program — a loopback stub is enough and
      needs no network — and the test **records which version produced it**.
      **Why it is a class and not a repo's lesson.** Neither author was careless;
      the failure is a property of hand-written fixtures, and the honest reading
      is that any author who understands the type well enough to write the
      fixture is exactly the author who will encode their belief rather than the
      artefact. That is the same shape as `310`'s finding — *a session cannot
      check its own compression against itself* — arriving one layer down, in
      tests rather than doctrine.
      **Related, and worth reconciling rather than duplicating:** a child
      already paid for a version of this once with hand-written collector
      fixtures, and a second time at the seam between a module and its first
      caller — where **both suites were green because each side's fixture
      encoded its own belief about the shape and neither tested the other's**.
      Whether that seam rule and this fixture rule are one rule or two is a
      judgement for whoever writes it up; filing them apart here would risk the
      three-originals defect this house already names.
