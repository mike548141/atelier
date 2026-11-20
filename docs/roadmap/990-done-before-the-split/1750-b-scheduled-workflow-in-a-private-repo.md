- [x] **B — scheduled workflow in a PRIVATE repo.** Mike ruled B on 2026-07-28
  from four costed options; built and pushed the same day. The estate-root repo
  hosts a daily workflow that checks out atelier, enumerates the account and
  asserts the full claim — every repo calls the floor **and** its floor is
  green. atelier is public, so a token spanning the private estate belongs in
  the private counterpart's secret store rather than the shop window; GitHub's
  schedule runs it whether or not a machine is switched on, which local cron
  (option C) cannot promise.
