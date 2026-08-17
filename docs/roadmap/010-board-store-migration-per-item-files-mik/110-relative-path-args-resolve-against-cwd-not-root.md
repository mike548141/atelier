- [ ] 🔥 **A scanner given `--root X` and a *relative* path scans your cwd's
      file while applying X's rules — a mixed-root run that reports
      confidently and means nothing.** Handed up by the `ros` session on
      2026-08-17, which lost a full round of "ros is clean" readings that were
      actually atelier's tree, including a floor result it nearly reported
      from. It was caught only by recognising atelier section names in
      supposed `ros` output.
      🔎 **The mechanism, verified here rather than taken on report.**
      `pathscan:849` and `wrapscan:546` both do
      `targets = [Path(p) for p in args.paths]` — a relative argument resolves
      against **cwd**, never against `--root`. But `root` is separately used
      for everything else the run depends on: the `.pathscanignore` /
      `.wrapscanignore` lookup (`:726`, `:432`), the repo-relative anchors,
      the `docs/` default. So the run reads **one repo's file under another
      repo's rules**. That is worse than simply using the wrong root, because
      neither half of the output is attributable and nothing in it says so.
      ⚠️ **`ros` reported this as "the flag is silently ignored" and as
      `linkscan`/`sizescan` behaving correctly. Both are slightly off, and the
      correction matters for the fix.** The flag is honoured — for rules, not
      for targets. And `linkscan:598` / `sizescan:643` carry the *identical*
      line; they differ only in their **default** when no path is given
      (`root` rather than `root / "docs"`), which is why an invocation with no
      path args looked right and one with a relative path did not. So this is
      not two well-built scanners and two broken ones — it is **one shape,
      shared by at least four tools**, whose blast radius depends on how each
      is called.
      🚩 **Why it is 🔥 rather than a note.** The estate's own guidance already
      records that a shell's cwd can silently revert mid-session, and the
      house hook and CI always pass `--root`, so the reading a session does
      *by hand* is exactly the one this bites. A guard that produces a
      confident false clean is worse than one that fails, and this one
      produces it in the direction of "everything is fine".
      🎯 **Fix candidates, cheapest first:** resolve a relative path argument
      against `root` (`root / p` when `not Path(p).is_absolute()`), which
      makes `--root` mean one thing; or refuse a path argument that does not
      lie under `root` and exit 2, which is louder and catches the absolute
      case too. Either belongs at the shared layer rather than four times —
      the same single-source question `115/080` already carries for the
      scanner harness. Whichever is chosen, it wants a test that a relative
      argument plus a foreign `--root` cannot silently read the cwd.
      *Source: the `ros` session's hand-up, 2026-08-17, after its board split.
      Mechanism re-derived from the four tools at HEAD; `ros` was not asked to
      re-measure and its framing is corrected above rather than repeated.*
