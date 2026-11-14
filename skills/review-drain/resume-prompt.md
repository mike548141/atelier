A usage limit stopped this review pass before it finished. The budget has since reset, and the principal has said to finish the work already started, verbatim: {APPROVAL}. That covers finishing THIS pass only: start nothing else.

Where it stopped: {STATE}
Your reviewer is agent id {AGENT}, spawned earlier in this conversation. Continue that same reviewer by SendMessage, telling it what was lost and to carry on from its own transcript. If it has already reported ACT 2 SAVED, or the pass has no act 2 and its verdict is complete, do not message it: no further review work is needed. If a SendMessage to it fails, say so and report RESULT: FAILED; do not spawn a replacement reviewer and do not move its work to another model.

Then carry on from your original steps: commit act 1 if it is not committed, release act 2 where the pass has a held sibling and it has not been released, fold, flip the board item, rebuild the board, land. Your original prompt's rules still bind, including LOAD and LIVE SYSTEMS: read-only reads are fine, live writes are not. Never wait on the principal.

LANDING: {LANDING}

Finish with the final output in your original prompt's exact shape: RESULT, ITEM, VERDICT, RULINGS OWED, COMMITS, NOTES.
