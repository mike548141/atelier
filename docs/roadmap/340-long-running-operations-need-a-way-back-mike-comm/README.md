# ⏳ Long-running operations need a way back — Mike-commissioned, 2026-08-22

**His words:** *"long running sessions, especially if they could risk data
integrity, need recovery mechanisms for failure conditions and verification post.
It goes back to the principle that we don't do something that we can't undo / a
way back."*

🔑 **He named the connection himself, and it is the important half.** The house
already holds *don't do what you can't undo*. What it does not yet say is that a
**long operation fails differently from a short one** — not by being wrong, but by
being *interrupted*. An interrupted operation can leave a state that is neither
the before nor the after, and which **looks like the after**. That is the failure
the undo principle does not currently cover, because there is nothing obvious to
undo.

## What surfaced it

A `docker-heap` session began migrating ~25 TB of media into per-folder ZFS
datasets — a copy per folder, the largest 11 TB and hours long. The procedure as
first written ran `rsync` in the foreground over SSH. Mike asked the question the
procedure had no answer to: *what happens when the connection drops, the laptop
reboots, or the session ends?*

Three gaps, all real, none noticed until he asked:

1. **No detachment.** A foreground process over SSH dies on `SIGHUP`. Hours of
   copying lost to a closed lid.
2. **No safe resumption.** Without `--partial-dir`, an interrupted large file
   restarts from zero **and sits at its real filename looking complete** — the
   dangerous half is the second one.
3. **Verification existed, but was being asked to carry the whole load.** It would
   have caught the truncation. Relying on that is a worse design than not creating
   the truncation.
