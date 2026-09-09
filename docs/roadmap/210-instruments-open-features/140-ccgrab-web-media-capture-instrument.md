- [ ] 🎯 **`ccgrab` — a web-media capture instrument (Mike commissioned 2026-09-09;
  idea recorded, build NOT started and not this session's to take)**

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
  reusable part, and it is the step a session skips. But it currently survives
  only as a machine-local note outside this repo, so each future session
  rediscovers it by hand. Mike does this occasionally — rare enough to forget,
  regular enough that rediscovery has a cost.

  🤔 **The placement question is real, and it should be settled before any
  build.** ADR 0006 defines `instruments/` as observing or extending the
  **human+Claude collaboration**. A media downloader does neither — it is a task
  utility that happens to be useful to a session, and the four instruments that
  exist today (`ccarchive`, `ccrepo`, `cctranscript`, `ccmail`) all read the
  collaboration's own artefacts. Admitting this one on usefulness alone widens
  the layer's definition **by precedent instead of by decision**, which is the
  move the layer was named to prevent. Options: (a) accept task utilities into
  `instruments/` and amend ADR 0006 to say so, (b) build it as a **skill**,
  which is already where "here is how to do X" lives and needs no binary, (c)
  give task utilities a third home. This compounds the section's existing
  `tools/` vs `instruments/` naming question above — two definitional gaps
  pulling on the same word.

  ⚠️ **It cannot be zero-dependency, and every existing instrument is.** Frame
  extraction needs `ffmpeg`; the fallback path needs `yt-dlp`. Neither is
  house-managed, and there is no package manager on the target machine, so both
  arrive as unmanaged binaries with no update story. A version of this that
  scrapes the manifest and *prints the URLs* stays dependency-free and delivers
  most of the value — worth costing before assuming the fuller build.

  **Scope, unresolved.** One proven platform, or a general scraper? A general
  scraper is a maintenance treadmill against pages that change without notice,
  and its failures are silent — it returns something plausible rather than
  nothing. If it is built at all, the honest shape is probably a small set of
  named handlers plus a generic manifest grep that reports what it found and
  what it could not identify, never a confident guess.

  🚩 **Posture to fix at the item, not at the build.** Public, ungated content
  only: no credential use, no login replay, no DRM circumvention, no bypassing a
  registration wall. Stated here so a later session extending it has to argue
  against a written line rather than quietly widen the tool's reach. Output
  paths must also stay outside any git work tree, the same guard `ccarchive` and
  `ccmail` already carry.
