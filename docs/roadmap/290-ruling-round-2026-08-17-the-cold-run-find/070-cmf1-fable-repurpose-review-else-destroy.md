- [ ] 🎯 **RULED 2026-08-17 (second sitting, 1045 UTC) — CMF1, verbatim:
      "Do a fable review to see if it can be usefully repurposed e.g. to
      gather data/stats on plain speak to find the root cause when its not
      plain. Otherwise we will destroy the hook per your recommendation."**
      Context given before the ruling: the reply gate's premise was false by
      the hook contract (a Stop hook fires after the reply is delivered), the
      gate was UNWIRED on Mike's 2026-08-15 ruling, the RG pass closed the
      unwiring at 0 MAJOR but found one surface still asserting a live gate
      (RG2, `tools/plainscan.py` docstring), and `tools/hooks/plain-reply.py`
      remains in the tree under the open destroy-or-repurpose call — with a
      hard-coded estate-layout fallback path (BG14). The recommendation Mike
      is referring to was *destroy* (delete the hook, its install stanza and
      tests; RG3, CMF2, CMF6, CMF8, BG14 close as moot). He did not take it
      outright: the repurpose question is to be **reviewed on Fable first**.
      <!-- pointerscan:allow: a design-review commission, not a rule-4 cold pass — the question it carries is the principal's own ruling wording, which the reviewer must answer, not a seeded attack question -->
      - [x] **Fable design review RAN 2026-08-17 — verdict: DESTROY** (0 MAJOR /
            3 MODERATE / 2 minor / 3 note, unchanged after reconcile) →
            [`reviews/2026-08-17-1321-plain-reply-repurpose-design.md`](../../reviews/2026-08-17-1321-plain-reply-repurpose-design.md).
            Taker: a Fable reviewer subagent under a Fable orchestrator that
            held the CMF, RG and BG verdicts back until the findings were
            written (wt: cold-run-0817-1321). The `cctranscript` control the
            commission asked for was run first: eight older sessions scored
            with `plainscan`'s own engine over `cctranscript --json` — 45
            replies, 25 flagged, the preceding prompt reachable for every one,
            and the transcript carries `entrypoint`, `effort`, model, branch
            and context that the Stop payload does not. Grounds, in the
            reviewer's words: a per-reply hook observes strictly less than the
            transcript already at rest and could close the gap only by reading
            that transcript (RP1); its data would be derived, un-rescorable and
            silently gappy where the transcript's is primary and complete
            (RP2); a logging variant keeps CMF6's machine-wide fail-open
            execution surface and adds a written cross-repo store of reply
            fragments for no gain (RP3); nothing in the file is worth carrying
            into an instrument (RP6). BG14's path confirmed at
            `plain-reply.py:111` (RP4); the hook is wired nowhere on this
            machine but its state file survives with stale entries (RP5).
            *Counsel, labelled:* the data-gathering aim is met without a hook by
            a small transcript-plane report over `cctranscript --json` — a
            repurpose of the *engine*, not the hook; a separate unfunded item.
      - [ ] 🎯 **Mike's ruling: DESTROY as the review recommends, or otherwise.**
            🚩 The reviewer's reconcile found the *If DESTROY* checklist below
            **incomplete** against what CMF/RG/BG actually filed — add RG6 and
            RG9 / item `120-…/010` as moot; RG8 needs an explicit state-file
            removal; CMF7/RG7 (CHANGELOG entries) are not moot and should ride
            the same commit; CMF2/RG3 are moot only if the README's reply-plane
            paragraphs above the stanza go too; RG1 and CMF3/4/5/9 stay open —
            "CMF cycle CLOSES" means the review cycle at 0 MAJOR, not those
            findings.
      - [ ] **If DESTROY:** delete `tools/hooks/plain-reply.py`, its tests and
            install stanza; retense the `plainscan.py` docstring (RG2); close
            RG3, CMF2, CMF6, CMF8, BG14 as moot; **CMF cycle CLOSES.**
      - [ ] **If REPURPOSE:** the design earns its own build item and rule-4
            pass; RG2 still lands (the docstring must say what the hook now
            does); CMF cycle CLOSES on the 2026-08-15 correction either way,
            since CMF1's premise is already unwired.
