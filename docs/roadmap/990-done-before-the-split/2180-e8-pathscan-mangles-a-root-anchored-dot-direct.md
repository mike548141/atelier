- [x] **E8 — `pathscan` mangles a root-anchored dot-directory path**
      `[S]` — **queued from `faves`, 2026-08-09, under Track F's
      queue-never-deliver rule** (Mike ruled that a child may queue a
      finding in the target repo's own roadmap; the ruling and the tension
      it resolved are recorded in that repo's `SESSIONS.md` for the same
      date). Reported, not fixed here — the child does not write atelier's
      code.
      **The defect:** a path written root-anchored whose first segment
      starts with a dot loses its leading `.well-` and its slash.
      `/.well-known/security.txt` is extracted as `known/security.txt`,
      which then reports missing while the file plainly exists.
      **Minimal repro, in a clean throwaway repo** (so it is not an artefact
      of the reporting tree): `site/.well-known/sbom.json` and
      `site/.well-known/security.txt` both **pass**;
      `/.well-known/security.txt` on its own line **fails**. So the trigger
      is the **leading-slash-plus-dot form**, not dot-directories at large.
      **Why it is worth a fix rather than a marker:** it is exactly this
      track's premise. In `faves` these 14 findings are honest URL
      references to files that exist and are published — a `security.txt`
      and an SBOM at their well-known locations. They cannot be reworded
      without making the prose wrong, and allow-markering 14 correct lines
      is the trained-to-suppress behaviour the track exists to prevent. They
      were the entire remaining `pathscan` backlog there after that repo
      cleared its own two classes (34 findings → 14, all of them this).
      **Not attempted from the child:** no fix, no test, no marker — the
      lines are left flagging so the count stays honest until this lands.
      *Superseded in its diagnosis on close: the trigger is a hyphen before
      the token's last `/`, not the leading-slash-plus-dot form. The repro
      and the reasoning from it were sound; the shape it generalised to was
      one case of a wider class.*
