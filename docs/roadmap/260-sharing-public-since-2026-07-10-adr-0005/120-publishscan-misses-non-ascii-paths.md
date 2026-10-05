- [~] 🔎 **publishscan's default and staged planes miss any path git quotes** (claimed 2026-10-05-1842, wt: atelier-qr-260-120)
      `[S][tools]`. Found 2026-10-05 by the worker that built `--history`
      (`110`). The tip plane reads `git ls-files` and the staged plane reads
      `git diff --name-only`, both without `-z`. With git's default
      `core.quotePath`, a path with a non-ASCII byte comes back C-quoted:
      `café/.env` arrives as `"caf\303\251/.env"`, and no never-publish
      pattern matches it. Confirmed on a fixture: the default scan missed a
      tracked never-publish file under a non-ASCII directory, and
      `--history`, which reads with `-z`, found it. It is a silent miss on
      a blocking guard, the same class as `110/130`'s gate risk.
      **The work:** read both planes with `-z`, as `--history` does. Output
      changes only where a quoted path is now matched. Before landing,
      measure read-only across the sibling repos how many would newly turn
      red, counts only.
