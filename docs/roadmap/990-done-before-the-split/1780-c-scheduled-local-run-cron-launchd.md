- [x] **C — scheduled local run (cron/launchd).** `floorfleet --remote --check`,
      shouting on failure. **No new credential** — uses the existing `gh` login.
      Failure mode: a machine that is off does not check, so drift can sit for
      as long as the laptop does. *(Not chosen 2026-07-28: superseded by B,
      which does not stop checking when a laptop is off.)*
