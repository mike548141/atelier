- [ ] **Mechanise the private-repo × posture join** (anti-slop invariant
      registry). `RECORD.md` already says keep private repos generic, and the
      2026-07-12 review sharpened the harmful class to the **join** — a private
      repo's name sitting next to its debt or security posture, not the name
      alone. It has now been breached three times (2026-07-11, 2026-07-12,
      2026-07-25), every time at the identical moment: *summarising fleet-wide
      scan state into an atelier record*. The rule is not unclear; it loses to
      the fact that the generic form is harder to write while holding a concrete
      finding list in mind.
      **No existing scanner can catch it** — a repo name beside a file path is
      neither personal data nor a credential, so leakscan and secretscan both
      pass it. It sits squarely in the judgement residual `tools/README.md`
      declares, which is exactly the shape the registry exists to promote to an
      always-on check. Sketch: flag a private-sibling repo name (discoverable via
      `pins.discover`) co-occurring with finding-shaped vocabulary in `docs/`,
      with an allow-marker for the deliberate worked examples. Needs a review
      before wiring — the false-positive surface is prose, and this repo's own
      doctrine names sibling repos legitimately.
