- [x] 🔥 **`allowmarker.py` cannot be loaded by file path since 2026-11-17,
      and that blocks every commit in a child whose hook loads it so.**
      Found 2026-11-20 UTC by a worker of queue run 08cd3b95 filing an item in
      a private child: the child's own pre-commit check loads atelier's
      `tools/allowmarker.py` with `importlib.util.spec_from_file_location`
      and `exec_module`, without registering it in `sys.modules`. The
      `110/060` change (2026-11-17) added a `@dataclass` (`Deferment`), and
      `dataclasses` looks its class's module up in `sys.modules` while it
      builds the class, so the load raises on Python 3.14
      (`AttributeError: 'NoneType' object has no attribute '__dict__'`) and on
      the system 3.9. Every commit in that child has failed its hook since; a
      worker refused `--no-verify` and left the child clean.
      **Owed:** make the module loadable by path again (no `dataclass` in a
      module other repos load by path), a test that loads it that way on every
      run, and a line in `tools/README.md` saying the module must stay so.
      🔒 CLAIMED 2026-11-20T08:10Z (claimed 2026-11-20-0810, wt: inline, no
      worktree) by queue-run session 08cd3b95 (Opus 5.5, principal-opened).
      ✅ **Fixed 2026-11-20 UTC, same session.** `Deferment` is a `NamedTuple`;
      `test_allowmarker.TestLoadsByFilePath` loads the module by path in a fresh
      interpreter (control: the old module fails that load with the error
      above); `tools/README.md` says the module must stay so. Checked in the
      child: its hook check now exits 0 on Python 3.14, and the old module and
      the new both load on the system 3.9 except for the dataclass. One other
      test in that child fails for its own reason (a temporary venv without a
      linter), unrelated to this. The child's own item that the filing worker
      could not commit is the next thing filed there.
