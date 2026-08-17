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
      - [ ] ⏳ **Fable design review queued — "can `plain-reply.py` be
            usefully repurposed as a data-gathering instrument?"** *Tier:*
            Fable, checked at selection. *Pass type:* design review
            (`REVIEW.md` § *Review the design, not only the build*), not a
            rule-4 doctrine pass — the hook is nobody's self-authored doctrine
            and the question is a build/no-build. *Delta under review:*
            `tools/hooks/plain-reply.py` · `tools/plainscan.py` § the reply
            plane · `tools/README.md` § `plainscan.py` (the two-planes section
            and the install stanza) · `docs/method/COMMUNICATION.md` § *Some of
            it is enforceable*. *The question, in Mike's words:* gather
            data/stats on plain speak to find the root cause when it's not
            plain. *What the review must weigh:* whether a record-only Stop
            hook (run `plainscan` over the last assistant message, log
            findings + rule + context to a machine-local store, never block)
            would produce data that finds root causes — or whether the
            existing `cctranscript` instruments already reach the same data
            from transcripts without a hook (check the instruments' `--help`
            first); the CMF6 threat surface (machine-wide, fail-open hook
            running branch-tracking code from a public repo) as applied to a
            logging-only variant; and the private-layout path (BG14). *Verdict
            shape:* REPURPOSE (with the design) or DESTROY, with grounds; the
            decision stays Mike's. *Prior verdicts:*
            `reviews/2026-08-15-1033-communication-floor-cold.md` (CMF),
            `reviews/2026-08-15-1126-reply-gate-unwired-cold.md` (RG), and the
            BG verdict for BG14 — reconcile after, never anchor before.
      - [ ] **If DESTROY:** delete `tools/hooks/plain-reply.py`, its tests and
            install stanza; retense the `plainscan.py` docstring (RG2); close
            RG3, CMF2, CMF6, CMF8, BG14 as moot; **CMF cycle CLOSES.**
      - [ ] **If REPURPOSE:** the design earns its own build item and rule-4
            pass; RG2 still lands (the docstring must say what the hook now
            does); CMF cycle CLOSES on the 2026-08-15 correction either way,
            since CMF1's premise is already unwired.
