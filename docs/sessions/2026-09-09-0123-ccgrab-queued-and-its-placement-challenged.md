# 2026-09-09 · 0123 UTC · `ccgrab` queued, and its placement challenged

**Session:** Opus 5 (1M context) · `main`, in place · one commit

A short atelier visit at the tail of an estate task. The task itself is not
recorded here — it was personal-estate work and carries nothing this repo may
hold. What reached the board is the reusable part and Mike's commission.

## What happened

A session captured a public vendor webinar end to end — recording, three
transcript formats, the presenters' slide deck, and a sampled frame set —
without screen capture, stream reassembly or a login. The page server-rendered
its entire asset manifest into the initial HTML, so `curl` plus a grep found the
video URL, the chapter list, the transcript paths and the deck sitting beside
one another.

The generalisable step is small and easy to skip: **read the raw page before
reaching for a screen recorder.** The method survived the session only as a
machine-local note outside this repo, which is exactly the shape of knowledge
that gets rediscovered by hand every time.

Mike, on being offered the idea rather than asked for a build: *"yes good idea,
queue it in the atelier roadmap"* — so it is recorded, and deliberately **not
started**.

## Filed as `210/140`, with three objections attached

The item would have been thin as a feature request, so it carries the arguments
against itself:

**Placement.** ADR 0006 defines `instruments/` as observing or extending the
human+Claude collaboration. The four that exist all read the collaboration's own
artefacts. A media downloader reads someone else's website. Admitting it on
usefulness alone widens the layer's definition **by precedent instead of by
decision** — the move the layer was named to prevent. Options recorded: amend
ADR 0006, build it as a skill instead, or give task utilities a third home. This
lands on top of the section's existing `tools/` vs `instruments/` naming
question, so two definitional gaps are now pulling on the same word.

**Dependencies.** Every existing instrument is zero-dependency. This one needs
`ffmpeg` for frames and `yt-dlp` for the fallback path, neither house-managed,
on a machine with no package manager. A manifest-scraper that prints URLs and
stops stays dependency-free and delivers most of the value — costed in the item
so the fuller build has to justify itself.

**Scope.** A general scraper fails silently against pages that change, returning
something plausible rather than nothing. If built, the honest shape is named
handlers plus a generic grep that reports what it could not identify.

The item also fixes a posture line now rather than at build time: public,
ungated content only — no credential use, no login replay, no registration-wall
bypass — so a later session widening it has to argue against written text.

## State

Board rebuilt, `board check` exit 0. Nothing claimed, nothing started, no
worktree taken (single small commit, tree clean on arrival and no evidence of a
parallel session).
