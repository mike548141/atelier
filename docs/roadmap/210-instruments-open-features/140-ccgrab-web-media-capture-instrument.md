- [ ] 🎯 **`ccgrab` — a web-media capture instrument (Mike commissioned 2026-09-09;
  placement RULED 2026-09-09 — `instruments/`; idea recorded, build NOT started)**

  **What grounded it.** A session captured a public vendor webinar end to end —
  the recording, three transcript formats, the presenters' slide deck, and a
  sampled frame set — without screen capture, HLS reassembly or a login. The
  whole asset manifest was embedded in the page's server-rendered HTML, so a
  plain `curl` plus a grep found `contentUrl`, the chapter list, the transcript
  paths and the slide deck sitting beside each other. The one non-obvious step
  was that the transcript files answered from a different host than the video,
  and the obvious host returned 403 for them.

  **Why it is worth a tool rather than a note.** The method generalises past the
  one platform: *read the raw page before reaching for a screen recorder* is the
  reusable part, and it is the step a session skips. It currently survives only
  as a machine-local note outside this repo, so each future session rediscovers
  it by hand.

  ## ✅ Placement: `instruments/` — ruled 2026-09-09, and the objection was wrong

  This item was filed arguing that `instruments/` is scoped to what observes or
  extends the human+Claude collaboration, that all four existing instruments
  read the collaboration's **own artefacts**, and that a downloader reading
  someone else's website would therefore widen the layer by precedent. Mike
  pushed back — `ccmail` had landed that same morning doing exactly that.

  **He is right, and ADR 0006 had already answered it twice.** The 2026-07-12
  addendum admitted `browser-fetch`, which drives Chrome to fetch other people's
  websites, and stated in terms that the earlier sub-norms are *"descriptive of
  the first two instruments, not constitutive of the layer"*. The 2026-09-09
  addendum then admitted `ccmail`, which authenticates to a third-party service
  and pulls down other people's data. "Reads the collaboration's own artefacts"
  was retired as a membership test two months before this item invoked it. The
  objection was not a finding; it was a stale reading of a live ADR.

  ## 🤔 The real test, which is not the one that was raised

  ADR 0006's rule is **purpose**: value must *be* the teammateship, and it draws
  the boundary explicitly — *"a general browser-automation utility Claude merely
  uses would be estate/infra, not an instrument."* That test bites here in a way
  the ownership question never did. `ccmail` passes it squarely because the
  operator has no use for it at all; they open their own mail in a mail client.
  **A downloader does not pass on those terms** — a human can want a video file
  for themselves, and a tool that just fetches one is a general utility that
  belongs with the estate.

  What makes `ccgrab` an instrument is narrower, and it should be built to it:
  **a recording is opaque to a session, and this makes it legible.** A session
  cannot watch 100 minutes of video, but it can read a transcript, chapter
  offsets and a slide deck. That is `browser-fetch`'s exact shape — reach what
  the teammate otherwise cannot — rather than a convenience download.

  **This scoping is the membership test, so it is also the design:** the
  transcript, chapters, slides and sampled frames are the **primary output**;
  the video file is a by-product for the human. Built the other way round — video
  first, text incidental — it is estate/infra by ADR 0006's own boundary and
  should be moved out. Whoever builds it should re-run that test before starting,
  not inherit it.

  ⚠️ **Dependency cost, reduced by the scoping.** The legibility core — scrape
  the manifest, fetch transcript and slide assets, report what it could not
  identify — is **zero-dependency**, which keeps it beside `ccarchive`,
  `ccrepo` and `cctranscript` rather than in `browser-fetch`'s dep-carrying
  category. Only frame extraction needs `ffmpeg`, and only the fallback path
  needs `yt-dlp`; neither is house-managed and there is no package manager on
  the machine. Make both **optional edges that degrade loudly**, not
  preconditions.

  **Scope, still open.** One proven platform or a general scraper? A general
  scraper is a maintenance treadmill against pages that change without notice,
  and its failures are silent — it returns something plausible rather than
  nothing. The honest shape is a small set of named handlers plus a generic
  manifest grep that reports what it found *and what it could not identify*,
  never a confident guess. `EVIDENCE.md`'s honest-instrument doctrine applies
  directly: "unknown" must be reachable output.

  🚩 **Posture, fixed at the item rather than at the build.** Public, ungated
  content only: no credential use, no login replay, no DRM circumvention, no
  bypassing a registration wall. Stated here so a later session extending it
  argues against a written line rather than filling a gap. Note this is a
  *narrower* posture than `ccmail`'s, which deliberately does hold a credential —
  the difference is that `ccmail` authenticates as the operator to the
  operator's own mailbox, where `ccgrab` would be authenticating to someone
  else's service to reach someone else's content. Output paths stay outside any
  git work tree, the same guard `ccarchive` and `ccmail` carry.

  📋 **Owed at build, not now:** an ADR 0006 addendum, per the layer's own
  practice of recording each admission with what it stretches. Nothing to add
  while the item is unbuilt — the addendum records a landing, and this has not
  landed.
