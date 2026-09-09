- ⏳ **Rule-4 review queued (tier: Fable; pass type: code + doctrine cold pass,
  the `ccmail` build).**
  *Delta:* `instruments/ccmail` (new) + `instruments/ccmail.test.js` (new, 25
  tests) + `instruments/man/ccmail.1` (new) + `instruments/README.md` (the
  layer table row and the `ccmail` section) +
  `docs/decisions/0006-instruments-in-atelier.md` (the 2026-09-09 addendum —
  the layer's first third-party credential) +
  `docs/roadmap/210-instruments-open-features/120-drive-binaries-have-the-same-gap-ccmail-just-closed.md`
  (the Drive finding filed beside it). One surface sits **outside this repo** and
  cannot be read from it: the machine-local `~/.claude/CLAUDE.md` entry that
  routes every session to `ccmail` instead of reporting the gap.
  *Intent record:*
  [`sessions/2026-09-09-0005-ccmail-the-attachment-a-session-could-name-but-not-open.md`](../../sessions/2026-09-09-0005-ccmail-the-attachment-a-session-could-name-but-not-open.md).
  *Self-authored*, so the review is not this session's to take. Two facts a
  taker needs at selection rather than after: the live Gmail round trip is
  **untested and untestable without a credential** that exists only after a
  human runs `--auth`, and the build's own three defects were all found by
  reading, all in the layers between this code and something else, and none by
  the test suite.
