- [ ] 🔎 **`PROPAGATION.md` and the root `README.md` say the plugin's scanner path is
      "pinned to the installed plugin version", and the plugin no longer carries a
      version** `[S][doctrine]`. Found 2026-11-27 by the `115/540` worker of session
      9c5fa72c (`atelier-fa`), while judging that item's defect 2 (`repo create`'s
      bundled-mode proof reads a removed `version` key). Since the principal's 2026-10-18
      pick to track every commit, the manifest has no `version`, so "the installed
      version" names nothing exact; what the path is pinned to is now the install
      directory the harness picks, which was not checked for a plugin with no version.
      **Owed:** say what the path is pinned to, in both places, once `115/540` defect 2's
      question (which side moves for `<VERSION>`) is answered, since the answer decides the
      referent. **Not fixed in passing:** reported first, per `CLAUDE.md`.
