# 2026-07-21 · 0746 UTC · man-page rollout — cctranscript + ccrepo (Opus, orchestrated)

**Mike:** open a session, hand it queued work, and when it finishes start
another — maximise plan use. First item: **man pages.** Orchestrate from an Opus
session with Opus agents doing the work (Fable permitted as fallback); expect
parallel sessions, so worktree; be ready to hit a session limit.

## What the item was

`ROADMAP.md` § "man pages — convention rollout": roll the established `--help` +
`man` split out to the two remaining **installed** CLIs. The convention
(`build/REPO-STANDARD.md` § "An installed CLI ships both") and its reviewed
worked example (`ccarchive` — `man/ccarchive.1` + trimmed `--help`, published by
`instruments/install`) were already in place; `cctranscript` and `ccrepo` were
the open tail. This closes the rollout: every tool the installer publishes to
`PATH` now documents itself in both registers.

## Approach — one orchestrator, two parallel Opus agents

- Claimed on `main` first (`[~]`, wt marker), then took **worktree-manpages** —
  isolation from Mike's other live sessions per CONCURRENCY.md (write-heavy ⇒
  worktree by default).
- Checked the one plausible shared-file conflict up front: the installer **globs
  `man/*.1`** and the bin loop is generic, so neither tool needs an `install`
  edit — the two agents' file sets are **fully disjoint** (`cctranscript` +
  `man/cctranscript.1` vs `ccrepo` + `man/ccrepo.1`, plus each tool's test file).
- Fanned out **two Opus agents in parallel**, one per tool, both in the worktree,
  each told **not to run git** (orchestrator commits, so no index race on shared
  disjoint edits). Each: read the standard + `ccarchive.1` template + its tool,
  wrote the roff page, trimmed `--help`, added the doc-convention tests, and
  self-verified (mandoc, tests, render).
- **Orchestrator re-verified independently** before committing — did not trust
  the agents' "all green".

## Shipped

| Tool | man page | `--help` | tests |
|---|---|---|---|
| cctranscript | `man/cctranscript.1` (202 ln), lint clean | 42→24 ln | +3 |
| ccrepo | `man/ccrepo.1` (358 ln), lint clean | 67→35 ln | +3 |

Each page: NAME/SYNOPSIS/DESCRIPTION (what **and why** — cctranscript's
hidden-timestamp + iMessage layout + N.M refs; ccrepo's single-message-grain
rationale + the ccusage-as-oracle reconciliation model)/OPTIONS/FILES/EXAMPLES/
EXIT STATUS/NOTES/SEE ALSO, matching `ccarchive.1`'s classic-man (`.TH`/`.SH`/
`.TP`) style. `--help` trimmed to the digest — one-line synopsis, flat option
list, closing pointer at `man <tool>`; rationale + worked examples relocated into
the page so the page is the **superset** and the two can't drift.

**EXIT STATUS enumerated against every `process.exit()` path in each source** —
the exact drift a prior ccarchive applied-batch review caught (`EXIT STATUS`
predating the tool's non-zero paths). cctranscript: 0 / 1 (five "cannot select a
session" paths). ccrepo: 0 / **2** (six `checkArgs` usage errors) / 1 (FX-fetch
failure + top-level catch) — the usage-vs-runtime split now documented.

## Verification (orchestrator, in the worktree)

- `mandoc -T lint` clean on all three pages (incl. ccarchive unchanged).
- **92 instrument tests green**, 0 fail (the 6 new doc-convention tests included:
  digest-points-at-man · well-formed-roff · superset drift-guard).
- Installer drive into a throwaway XDG dir publishes **all three** pages into
  `MANPATH` and both CLIs into `bin`; no directory leaked into `bin`.
- Both `--help` outputs end in the `man <tool>` pointer (24 / 35 lines).
- leakscan · secretscan · linkscan · sizescan all clean.

Landed via local `--no-ff` merge (preserves signatures — not the `gh pr --rebase`
strip hazard). Worktree removed, branch deleted.

## Notes

- **No review cycle owed.** This is *application* of a reviewed convention
  (REVIEW.md rule 4 fires on new self-authored doctrine, not on rolling an
  established standard to more tools). No durable design record created.
- **Digest length is legitimately per-tool.** cctranscript (13 flags) → 24 ln,
  ccrepo (~21 flags) → 35 ln; both are flat option lists whose length the flag
  count drives, not padding. The one-screen caps the agents asserted are grounded
  in terminal rows / flag count, not the current measurement.
- **Orchestration worked cleanly:** disjoint file sets + no-git-in-agents +
  orchestrator-commits is a clean pattern for parallel agents in one worktree; no
  conflicts, no index races. Recorded for reuse.
