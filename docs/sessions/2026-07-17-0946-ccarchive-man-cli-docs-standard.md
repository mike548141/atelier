# 2026-07-17 · 0946 UTC · man pages + the CLI-docs standard, ccarchive worked example

## What prompted it

Two Mike asks in one thread:
1. Roadmap future ccarchive features (local-store audit; full/delta restore;
   iCloud dataless-file awareness; sign the manifest for tamper-evidence).
2. "I like to have both man files and `--help`" — man = fuller plain-language
   with examples; `--help` far more concise. Then: capture *the roles of each*
   in atelier **as doctrine for child repos**, not just an instruments detail.

## The doctrine (`build/REPO-STANDARD.md`)

Added a repo-craft convention (§ Repo-craft conventions) — children inherit it:

- **`--help` = the digest.** One-screen, synopsis + flat option list, ends by
  pointing at `man <tool>`. Not where prose/rationale/examples live.
- **`man <tool>(1)` = the full reference.** Plain language: what & why, every
  option, and the sections a digest can't carry — FILES / EXAMPLES / EXIT STATUS
  / NOTES / SEE ALSO.
- The page is the superset, `--help` its digest — detail lives in **one** place
  so they can't drift. Ship pages as roff in a `man/` dir; the installer
  publishes them to `MANPATH`.

Self-authored doctrine ⇒ **⏳ cold review queued** in ROADMAP (rule 4; a
non-author spawns it). Not me.

## The worked example (`instruments/`)

- **`instruments/man/ccarchive.1`** — full roff manual (NAME…SEE ALSO, incl.
  SCHEDULE, INTEGRITY, FILES, EXAMPLES, EXIT STATUS). Lints clean under `mandoc`.
- **`ccarchive --help` trimmed** 40→18 lines: synopsis, options, one line
  pointing at `man ccarchive`.
- **`instruments/install`** now also symlinks `man/*.1` into
  `~/.local/share/man/man1` (auto-found because `~/.local/bin` is on PATH, so
  `man ccarchive` works post-install). Fixed a latent bug while there — the bin
  loop symlinked *directories* too (`man/`, `fixtures/`, `browser-fetch/` leaked
  into `~/.local/bin`); now requires a regular file.
- README points at the standard and documents the man step.

## Roadmap (Mike's future features)

New `## instruments/ — open features` section: ccarchive local-store audit;
full/delta restore (don't clobber a live file newer than the archive); **iCloud
dataless-file awareness** (Optimise-Mac-Storage evicts local bytes → detect
`SF_DATALESS`, don't mis-report as missing, don't bulk-materialise on `--verify`);
**sign the manifest** (key kept off-archive → tamper-evident, closing the
`--verify` caveat). Plus man-page rollout to `cctranscript` + `ccrepo` (ccrepo
after its v2 rewrite lands — not touched now, it's live in a parallel session).

## Verified

- 67 instrument tests green (+2 here: `--help` stays a ≤22-line digest pointing
  at the manual; `ccarchive.1` exists and is well-formed roff).
- `mandoc -T lint` clean; `man` renders the page; `install` into throwaway XDG
  dirs publishes CLIs + the man page and leaks **no** directory into bin.

## Concurrency

Worktree `atelier-ccarchive-man` off main; parallel `ccrepo-v2` session left
untouched (that's why ccrepo's man page/`--help` are roadmapped, not done).

## Owed

- ⏳ the REPO-STANDARD CLI-docs review (queued, non-author). Instrument code +
  install are tested/driven, self-verifying. Earlier ⏳ (ADR 0006 addendum)
  still stands.
