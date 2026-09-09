- ⏳ **Rule-4 review queued (tier: Fable; pass type: code + doctrine cold pass,
  the `ccmail` build).**
  *Delta:* `instruments/ccmail` (new) + `instruments/ccmail.test.js` (new, 25
  tests) + `instruments/man/ccmail.1` (new) + `instruments/README.md` (the
  layer table row and the `ccmail` section) +
  `docs/decisions/0006-instruments-in-atelier.md` (the 2026-09-09 addendum —
  the layer's first third-party credential) +
  `docs/roadmap/210-instruments-open-features/120-drive-binaries-have-the-same-gap-ccmail-just-closed.md`
  (the Drive finding filed beside it). **Delta widened 2026-09-09** per the
  landing-commit rule: `instruments/ccmail` again (the two-route resolver, the
  removal of the plaintext-file store) + `instruments/ccpdf/` (new: renderer,
  `setup`, `selftest`) + the 0006 amendment and third addendum + the
  `instruments/README.md` `ccpdf` section. Surfaces **outside this repo** and
  unreadable from it: the machine-local global-instructions entries routing
  sessions to `ccmail` and to the web-media method, and `~/.claude/ccmail.json`
  (identifiers only, no secret).
  *Intent record:*
  [`sessions/2026-09-09-0005-ccmail-the-attachment-a-session-could-name-but-not-open.md`](../../sessions/2026-09-09-0005-ccmail-the-attachment-a-session-could-name-but-not-open.md).
  *Self-authored*, so the review is not this session's to take. Two facts a
  taker needs at selection rather than after: the live Gmail round trip is now
  **proven end to end** against a real mailbox via the delegation route (the
  earlier "untestable" note is superseded), and the build's own **five** defects
  were found by reading and by an adversarial selftest, all in the layers
  between this code and something else, and none by using the tool.
