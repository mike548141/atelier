# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-git-resolved-staged-scope-cold.md` (`REVIEW.md` rule 1).
Written 2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta.
Open this only after act 1 is committed. Everything here is a floor, never a fence, and none of it
is a finding.

## The queue pointer's questions (author-written, verbatim)

> whether any spelling still lets a staged secret past (symlinks, submodules, a scope naming a
removed directory); whether refusing an unknown scope can strand a child.

## The brief-writer's own questions

1. "A declared directory with no tracked file is the same case" sits beside the changelog's "no
declared scope changes behaviour". A directory that exists on disk but tracks nothing passes the
floor's `exists()` and then exits 2. Is the changelog's sentence true, and what does it cost a
child?
2. A commit that moves every file out of a scope directory: rename detection is on by default, so
`--diff-filter=D` does not list the old paths. Is the scope then refused, blocking a legitimate
move?
3. Unmerged index entries, `git add -N`, sparse-checkout, a gitlink positional, a tracked symlink:
what does `ls-files` answer for each?
4. Hooks set `GIT_DIR`, and `core.precomposeunicode` makes macOS normalise argv while Linux does
not. Does a scope resolve on the hook and refuse in CI, or the reverse?
5. `GIT_LITERAL_PATHSPECS="0"` and the magic prefix: what does a positional beginning with `:` do?
6. Run the five other scanners' refusals, not only the three staged-diff guards.
7. The first commit of a repo, with no `HEAD`.

## What the brief-writer ran, and what it got

- `gs_tests`: python3 3.14: 1019 tests OK, exit 0, 417 s under load.
- `p1070`: scope docs: exit 1 (marker found). Docs: 2. nosuchdir/: 2. '*.md': 2. '.': 1. wrong cwd:
  2. subdirectory cwd: 1.
- `floor`: at c132cc1c: hook exit 0, ci exit 0. pathscan reports 3 findings, warn-only:
  docs/method/EVIDENCE.md:427, docs/method/session-open/session-open-prompt.md:13 and
  docs/method/session-open/template-history.md:10 (paths that do not exist from the repo root).
