- [x] **`core.hooksPath` was unset in the atelier clone.** Every child had it
  set; the parent did not. So atelier committed through the vendored
  2026-07-12 three-scanner hook while the registry it authors served nine
  scanners to all 13 children. The repo that writes the policy was the only one
  not bound by it at commit time.
  - **Found by measurement, not by reading.** It was first reported inside a
    review pass that Mike later rejected on tier grounds, so the finding was
    correctly treated as unverified and re-derived from scratch on 2026-07-27
    (`git config core.hooksPath` → unset on atelier, `.githooks` on all 13
    children). A finding from a withdrawn pass is a lead, never a fact.
  - **Fixed by Mike** (`git config --local core.hooksPath .githooks`),
    deliberately left to him because it changes a machine, not the repo.
    Proven after, not asserted: the hook plane now reports **9/9 enforced and
    clean**.
  - 🔎 **The half that is still open, and is the more important half.**
    `floorfleet` discovery walks *children*, so atelier is structurally
    invisible to the board whose whole purpose is proving conformance. A
    machine-local setting is not a mechanism — nothing would have caught this,
    and nothing would catch it recurring on a fresh clone or a new machine.
    Carried as **A5b** on the live roadmap. Same defect one level up, which is
    the shape ADR 0008 exists to end.
