# 2026-07-17 · 0908 UTC · ccarchive — self-installing schedule

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 107+1 -->
- [2026-07-17 · 0908 UTC · ccarchive — self-installing schedule (Opus)](2026-07-17-0908-ccarchive-self-scheduling.md) — Mike: how does the schedule survive a new laptop — a feature in ccarchive? It was a hand-written launchd plist, reproducible by nothing (a new machine restores the tool via `install` but not the schedule). Made scheduling built-in: **`--install-schedule`** (writes + loads `com.ccarchive.archive` launchd agent, daily + RunAtLoad, idempotent, pointing at `~/.local/bin/ccarchive` + `process.execPath`, logging to `~/Library/Logs/ccarchive.log`), **`--schedule-status`** (read-only), **`--uninstall-schedule`**; non-macOS prints the cron line. New-machine recovery is now two documented commands (`./instruments/install` → `ccarchive --install-schedule`). +6 tests (18 total; pure builders incl. XML-escaping + read-only status spawn, never spawning install/uninstall to avoid mutating a dev's launchd). Driven live: status→install→status→RunAtLoad archived; migrated off the old hand-made `nz.cxi.ccarchive` agent (`launchctl list` now shows only the tool-managed one). No ADR change (doctrine unchanged); README updated. No new review owed.


## What prompted it

Mike, right after the ccarchive session: "How do we re-establish the schedule if
I replace my laptop? Feature in ccarchive?" The gap was real — the daily run was
a **hand-written launchd plist** in `~/Library/LaunchAgents/`, reproducible by
nothing: on a new machine `./instruments/install` restores the *tool* but the
*schedule* would be silently missing. (Also asked whether the schedule/settings
had tests + docs; they didn't — this closes that too.)

## The change (`instruments/ccarchive`)

Scheduling is now a built-in feature, generated from runtime-derived paths:

- **`--install-schedule`** — writes `~/Library/LaunchAgents/com.ccarchive.archive.plist`
  (neutral label, no personal data) and `launchctl load`s it; daily +
  `RunAtLoad`. Idempotent (unload-then-load), so it's also the *update* path.
  Points the agent at the stable installed entrypoint (`~/.local/bin/ccarchive`)
  and `process.execPath` for node, logging to `~/Library/Logs/ccarchive.log`.
- **`--schedule-status`** — read-only: is the plist installed, is it loaded.
- **`--uninstall-schedule`** — unload + remove.
- **Non-macOS** — each prints the equivalent `cron` line rather than pretending
  launchd exists. Platform honesty; the estate is macOS today.

So new-machine recovery is now two documented commands: `./instruments/install`
then `ccarchive --install-schedule`. Documented in `instruments/README.md`
(install section + the ccarchive section's scheduling bullet). No ADR change —
the doctrine (ADR 0006 addendum: first writing instrument, machine-local write
target) is unchanged; the plist just moves from hand-made to tool-made.

## Verified

- **18 tests** green (was 12; +6). Pure builders (`schedulePaths`,
  `resolveScriptPath` both branches, `launchdPlist` incl. XML-escaping an `&` in
  a path, `cronLine`) + a read-only `--schedule-status` spawn. Tests deliberately
  **never** spawn install/uninstall — that would mutate a developer's real
  launchd on macOS.
- **Driven live end-to-end:** status (not-installed) → install (loaded, agent
  points at `node` + `~/.local/bin/ccarchive`) → status (installed + loaded) →
  RunAtLoad archived 2 changed sessions into the new log. **Migrated off** the
  old hand-written `nz.cxi.ccarchive` agent (unloaded + removed, stale log
  deleted); `launchctl list` now shows only `com.ccarchive.archive`.

## Owed

Nothing new. The earlier ⏳ ADR-0006-addendum cold review still stands (queued,
non-author). This delta is routine instrument code — tested and driven,
self-verifying.
