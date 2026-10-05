- [x] **A `private-key-header` that was prose, not key material** — BEGIN and END
      markers on one line, no base64 body: documentation describing a key file's
      format. Resolved; wants an allow-marker, never rotation. Recorded because
      it is the archetypal false positive of this rule and will recur.

      ✅ **Closed 2026-10-05 — resolved in its own text** (queue run, Opus
      5.5). The item records the finding as resolved: an allow-marker, never
      rotation. It stayed open as a note about the archetypal false positive.
      That lesson is carried by `030/030`, which counts this false positive
      among the instances of its archetype class (a rule deciding on a
      fragment of a value instead of its whole shape). Whether the marker
      landed is the child's own record, not atelier's.
