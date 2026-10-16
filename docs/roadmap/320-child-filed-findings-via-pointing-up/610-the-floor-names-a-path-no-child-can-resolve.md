- [ ] 🔎 **Hand-up: the floor region now names a path no child can resolve,
      so `pathscan` flags every verbatim child copy** `[XS][doctrine][tools]`.
      Handed up by a public child's queue run on 2026-10-16 under
      `PROPAGATION.md` § *Pointing up*, found while bumping its pin to
      `fd63df8` and re-stamping the floor word for word.
      **Evidence, reproduced in the child:** `320/500` (`55572b1`) added the
      sentence *"The **expected toolbox** … is atelier's:
      `method/TOOLBOX.md`."* to the `floor` region. In atelier that path
      resolves (docs-relative). In a child it cannot: the child's
      `pathscan` reports `CLAUDE.md:<line> [missing-path] method/TOOLBOX.md
      → … does not exist`. It is warn-only there, so nothing blocks; but it
      is a finding in every child on every commit that touches the file, and
      the child **cannot** silence it the usual way, because a
      `<!-- pathscan:allow -->` marker on that line is a difference from the
      canonical text and the hand stamp check reports it as drift. The
      floor's other cross-repo reference, `../atelier/docs/method/` in
      *Source & drift*, is not flagged.
      **Options, offered, not recommended:** (1) spell it the way *Source &
      drift* does (`../atelier/docs/method/TOOLBOX.md`, or "atelier's
      `docs/method/TOOLBOX.md`" in a form `pathscan` does not read as a
      local path); (2) carry the allow-marker in the canonical text itself,
      so every copy inherits it; (3) teach `pathscan` to skip a
      `stamp:begin … region=floor` block in a child, since that text is
      checked by the stamp, not by the child's tree; (4) leave it, and
      record that this one warn-only finding is expected in children.
      🔎 **Verified at HEAD 2026-10-16** (1501 UTC queue run, a read-only
      Sonnet worker): ✅ confirmed, reproduced. `pathscan.py --root . .` on
      a copy of the template floor: exit 1, `CLAUDE.md:89 [missing-path]
      method/TOOLBOX.md`; an allow-marker clears it but stampscan then
      reports drift. One detail off: *Source & drift* reads `<atelier-path>`
      (a skipped placeholder), not `../atelier`. Overlaps `320/010`, `170`.
