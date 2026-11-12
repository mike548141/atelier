- [x] **Hand-up from a private child: leakscan G3 has no form for a binary that
      is rebuilt.** Filed 2026-11-09 by a child session, as a suspicion from one
      repo and not a proven defect; the child owes nothing and asks for nothing.
      Waiting on Mike's answer, listed on `420/030`.

      **The shape.** A `.leakscanbinaries` entry accepts one digest. A generated
      binary, such as an Office document rebuilt by a render, can come out with
      new bytes when no visible content changed. Each render then raises
      `binary-changed`, and from `BINARY_GRACE_UNTIL` (2026-11-18) that blocks the
      hook and CI. Read in `tools/leakscan.py`: the entry matches by digest prefix
      and nothing path-scoped exists, so the mechanism is confirmed. How many
      children hold such files is not measured.

      **What the child did.** It wrote a local helper that rewrites only the
      digest for paths under named generated folders and reports anything else
      that moved. The reason and the metadata decision on each entry stay.

      **The question it raises.** Should G3 accept a path-scoped "generated, digest
      may change" entry, so children stop building this themselves?

      **Judgement, for Mike to rule.** A digest-free entry cuts against what G3 is
      for. The gate's comment says the digest is what makes the acceptance
      one-time: the person who re-lists a changed binary is looking at the new
      bytes. Mike's answer of 2026-11-08 (`160/980` GM9) put the gate ahead of the
      ignore file so that a path glob cannot skip G3, and a path-scoped entry is
      that glob under another name. Office documents are also the format G3 cannot
      see inside, so the digest is the only thing binding them. An automatic
      digest rewrite has the same weakness, in one repo.

      Better options, in order:
      1. Make the render reproducible (fixed archive timestamps and document
         properties), so the bytes change only when the content does and the
         ordinary entry works.
      2. Stop tracking the generated output where the source can rebuild it.
      3. If neither fits, a G3 form that compares extracted content rather than
         raw bytes. This is new reading code per format, so it is the costliest.

      **Done means** the fleet is measured for generated binaries, Mike has ruled
      on whether any path-scoped form exists, and whichever answer holds is
      written in the G3 block and in `GUARDS.md`.
  - [x] ✅ **Closed 2026-11-12 UTC.** 💬 Mike's pick, 2026-11-12 UTC, from options
        session d0ca5d24 offered: "No; fix at source (Recommended)". An answer, not a
        ruling.
        No path-scoped entry is built. The G3 block in `tools/leakscan.py` says so.
        The child already carries its own item to make its render reproducible
        and retire its digest helper, and that item records the answer. The fleet
        measurement in "done means" is dropped: with no new form, there is nothing
        to size.
