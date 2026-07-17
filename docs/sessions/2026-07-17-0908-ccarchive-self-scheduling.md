# 2026-07-17 · 0908 UTC · ccarchive — self-installing schedule

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
