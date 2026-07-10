# 2026-07-10 · the linkscan review: PASS-WITH-FINDINGS, all five assumptions repaired, gate cleared (Fable)

The brief run cold (`docs/reviews/2026-07-10-linkscan.md`), deep not fast, and
**driven, not read**: floor re-run first (selftest OK, whole tree clean exit 0,
171 tests OK, a planted break + bogus target both flagged exit 1), then a probe
per load-bearing assumption. **Every one of the brief's five assumptions took
damage** — four proven live before fixing. Ten findings L1–L10: eight [fixed]
same session (each pinned by a test, each fix re-driven live), L8 [verified
against GitHub's docs], L10b [stated] as a deliberate residual. Suite 171→187;
verdict below the brief's divider.

## Proven live before fixing

- **L1 — the silent green (assumption 5, the worst gate-fit defect).**
  `linkscan does-not-exist` walked an empty glob and exited **0**. Wired into a
  hook or CI with a typo'd path it would have reported clean forever while
  scanning nothing — the exact EVIDENCE §14 silent-success class the brief was
  written to hunt. Now exit 2 with a stderr message; two tests pin it.
- **L2 — case-blind on the very machine the hook runs on.** `[x](target.md)`
  against on-disk `Target.md`: green on APFS, 404 for every GitHub reader. CI's
  ubuntu would catch it *after* push; the pre-commit hook — the control meant to
  catch it first — runs on the Mac and couldn't. Now walked against on-disk
  casing, reporting the true name; NFC/NFD normalisation differences (the
  macron case) deliberately exempt so te reo filenames can't false-positive.
- **L3 — a `../` that exists locally is still a 404 for every reader.** GitHub
  serves nothing above the repository root; new `outside-root` finding kind. In
  a doctrine whose children literally point at `../atelier`, not hypothetical —
  a deliberate machine-local pointer now takes a reasoned `linkscan:allow`.
- **L4+L5 — the anchor leniency + the slugger divergence, one knot.**
  `#A-Section` matched heading "A Section" (GitHub fragment matching is exact —
  the reader lands unscrolled), because both sides were re-slugged before
  comparing. Tightening to exact-match first required fixing the slugger's one
  real GitHub divergence found: it stripped literal underscores as emphasis,
  where GitHub keeps them (`snake_case name` → `snake_case-name`). Two-tier
  compare now: exact pass; lenient-only match reports *what to write instead*.
- **L6 — `[x](a(1).md)` flagged a working link** (dest parsed as `a(1`) — the
  alarm-fatigue class assumption 1 warned about. Regex now takes one level of
  balanced parens; unbalanced stays invisible, matching GitHub's own parser.
- **L7 — the fence tracker mis-toggled on nested and info-string fences.** A
  ``` inside a ```` block "closed" it; a ```python line inside an open ```
  block did too (CommonMark: closing fences carry no info string). Example
  links inside such blocks flagged live; the dual shape swallows real links.
  One shared `_content_lines` tracker now — links and headings can never drift
  — closing only on same char, run ≥ opener, bare. Unclosed-fence-to-EOF was
  probed and **kept** (matches GitHub), pinned by a test so nobody fixes it.
- **L9 — setext-headed targets false-positived**, and the residual had filed
  setext under invisibility (false-negative flavour) when its live effect was
  flagging *valid* links. Setext headings now mint anchors, conservatively; the
  house `---` divider after a blank line mints nothing (test-pinned).

## Verified / stated, not changed

- **L8** — root-relative `/…` links: GitHub's docs confirm repo-root
  resolution; the tool already matched. A latent claim made grounded.
- **L10** — unreadable files now exit 2 tidily (was an uncaught traceback —
  never a silent green, but the wrong tier). The indented-code false positive
  is **deliberately unfixed** and stated in the residual: skipping 4-space
  indents would skip real links in nested list items — a stated FP costing one
  allow-marker beats a silent FN. HTML-minted anchors (`<a id>`) added to the
  residual too; the old list missed both.

## The gate

**Cleared** — with L1 fixed, exit 2 truly means couldn't-complete, and the tree
rescanned clean under the stricter checks (no alarm-fatigue on the live corpus).
**The wiring itself is left to the next build session**, fourth application of
don't-stack: the reviewer's own same-day fixes are fresh code, and wiring them
into the gate the hour they were written is the pattern the rule exists to stop.
The wiring is a two-line change: a floor step in `ci.yml`, a linkscan line in
`pre-commit.sample`. ROADMAP carries it as the open item.

Records: verdict appended to the brief; ROADMAP linkscan item [x] with the
wiring sub-item open; CHANGELOG entry; this file. ros pin untouched (bbdeece —
no doctrine-text change; tools-only).
