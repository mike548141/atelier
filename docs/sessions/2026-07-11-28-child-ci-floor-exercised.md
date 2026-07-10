# 2026-07-11 · child-CI floor exercised on numen; a four-session linkscan false-negative found + fixed (Opus)

Took session 27's two explicit owed items — **run `floor.yml` on a real child**
and **review-owed** — and closed the first while surfacing an atelier bug worth
more than the exercise itself. The house discipline earned its keep exactly as
session 19 predicted: *driving* the tool on a live target found a §14
silent-success a scratch dry-run could not.

## The exercise, and what it caught before any push

numen (`mike548141/numen`, private, scaffolded session 21 as pre-code with a
**stated no-CI-gate** — "the content scans can't run in CI yet") was the natural
real child: adopting `floor.yml` closes numen's *own* stated open item, unblocked
by atelier going public (ADR 0005). Pre-flighting atelier's current scanners over
numen's tree — drive-not-assume — flagged **two real linkscan breaks** in numen
before a single push:

1. `README.md` `[tiki](../ros)` — a disk-only relative link that 404s on GitHub
   (`ros` is a separate private repo). De-linked to prose.
2. `docs/decisions/README.md` `[0001](0001-slug.md)` — the scaffolded placeholder,
   a break **every child inherits**.

## The bug the exercise exposed (the real payoff)

Chasing #2 upstream: atelier's own `docs/decisions/README.md` template carries
the same placeholder, yet atelier's tree scanned *clean*. The contradiction
resolved into a genuine **false negative in linkscan itself**: `SKIP_DIR_NAMES`
carried `build` as build-output noise, so the whole-tree walk had been **silently
skipping atelier's entire `docs/build/` doctrine layer** — 14 files — since it was
built. Session 24's "whole tree clean (55 files, 36 links)" was really "clean
except the layer we never looked at". The exact cardinal sin the linkscan review
(session 25) was constructed to prevent, live for four sessions (24–27), because a
doctrine dir happened to share a name with a build-artifact convention.

**Fix (atelier `d0870a4`):** hardcode-skip now holds only names that are *never*
human-authored prose (VCS, deps, tool caches); `build`/`dist` are gone — the tool
cannot tell "build output" from "content named build" by name, and guessing wrong
masks a doctrine layer, the worse error. A repo with a real build-output dir
names it in `.linkscanignore`. Mike chose the recommended full-drop over a
top-level-only skip (a nested `packages/app/build/` would defeat top-level-only
anyway). Pinned by `test_content_dir_named_build_is_walked`; suite **195→196**.
Unmasking `docs/build/` immediately caught the template placeholder — fixed there
(and in numen) by wrapping the example in a single-line code span so it renders as
the format it illustrates and isn't scanned as a real link. All templates
re-scanned as-if-scaffolded: clean, the decisions-README was the only offender.

## numen, driven not read

`floor.yml` copied in verbatim (testing the template as delivered) + the two link
fixes + honest-prose corrections (numen's workflows-README and CLAUDE.md both
claimed "the only automated gate is the hook" — now false). Committed `0958cd5`,
pushed. Then, per REVIEW's re-run rule, both claims proven on **real GitHub
Actions**, not asserted:

- **Happy path** (run `29092514962`, green 8s): atelier fetched as sibling,
  `repo/` scanned, `✓ secretscan` / `✓ leakscan (structural only)` / `✓ linkscan`
  — the real-infra proof `floor.yml` never had.
- **Fail-closed** (throwaway PR #1, since closed + branch deleted; run
  `29092599385`, **red**): one planted broken link → secretscan ✓, leakscan ✓,
  **linkscan ✗**, job exit 1. The load-bearing disproof of the false-negative
  fear, on real infra.

A sharp incidental: numen's commit ran only secret+leak locally — its
**pre-commit hook is frozen at scaffold time** (bbdeece, before session 26 added
linkscan to the hook), so it doesn't run linkscan at all. So on numen, `floor.yml`
in CI is the *only* thing that catches a link break — which is precisely what the
fail-closed run demonstrated. Child hooks drift from atelier's evolving one; the
floating-`atelier@main` CI floor is the mitigation. Named as a review assumption.

## Left open — the review, deliberately not stacked

Brief written: `docs/reviews/2026-07-11-child-ci-floor.md` (range `bafeaa3` +
`d0870a4`, plus numen `0958cd5` as the live rig). Nine load-bearing assumptions,
four lenses; sharpest: floor.yml's trigger gaps (a never-PR'd branch push is
scanned by nothing), `atelier@main` as a supply-chain trust, and whether the
broken-link fail-closed proof generalises to a secret or the real-infra
secret-block is still owed (only `act`-proven in session 27). Fifth application of
don't-stack-a-gate-on-unreviewed-tooling: `floor.yml` is not rolled to further
children, and the linkscan behaviour change is not leaned on, until the verdict.
numen keeps `floor.yml` (its exercise host, and low-stakes/private) — stated, not
silently.
