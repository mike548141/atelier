- [ ] **D2 residue — stampscan registry wiring stays barred on ST3.** The
      advisory wiring landed 2026-08-05 (atelier `ci.yml` only, the
      reviewer's bar step 1); registry wiring — which reaches every child
      (ADR 0008) — waits on the child-side `source=` resolution story:
      pin-aware (a child at `atelier@<SHA>` may lawfully differ from
      atelier@main), and `create-repo` taught that the markers are
      load-bearing scaffold content. Any blocking flip is a separate later
      ruling after an advisory soak (the wrapscan/datescan precedent).
