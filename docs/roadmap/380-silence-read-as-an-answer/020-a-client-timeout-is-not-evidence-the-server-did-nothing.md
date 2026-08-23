- [ ] 🔑 **The second instance is the INVERSE of `010`, and it is the more
      dangerous half: a client timeout read as a failed WRITE.** Found live in
      docker-heap on 2026-08-24 by the peer session, within the hour of `010`
      being filed, on the same middleware and under the same host load.
  - [ ] **What happened.** Acting on the owner's ruling to close a snapshot gap,
        the session created a snapshot task and then a recursive snapshot. The
        create returned **`Call timeout`**. It re-queried: **zero snapshots**.
        Every instinct said the operation had failed and should be retried.
        **It had not failed.** Re-queried once the middleware recovered:
        **35 snapshots** — one on the parent and one on each of its 34 children,
        all correctly named. **The client timed out; the server completed the
        work.** The second query had been issued while the middleware was still
        unavailable, so it too returned nothing — the same silence, twice, about
        two different questions.
  - [ ] 🛑 **Why this half is worse than `010`'s.** A false negative about a
        *read* produces a wrong sentence in a document, and a reader may catch
        it. A false negative about your **own write** produces the instinct to
        **retry** — and on a non-idempotent operation a retry is how you get
        duplicate tasks, duplicate resources, or a second destructive pass. The
        wrong belief is about an action you have already taken, and the natural
        correction makes it worse.
  - [ ] ⚖️ **THE BARB, and it is the reason both instances belong in one item.**
        The obvious fix for `010` — *check the exit code, do not suppress
        stderr* — **actively causes this one.** Here the exit code was non-zero
        and the operation had **succeeded**. A rule that says "non-zero means it
        did not happen" is precisely the false belief. The two halves cannot both
        be fixed by trusting the client's signal harder, because the client's
        signal is what is wrong in both.
  - [ ] 🎯 **The rule that covers both, and it is not about exit codes at all:**
        **a client's signal is evidence about the CLIENT, not about the server.**
        A timeout says the answer did not arrive; it says nothing about whether
        the work was done, nor whether the state is empty. So:
    - [ ] **Before concluding from a negative — re-query the state**, and satisfy
          yourself the instrument can currently *see* a positive (`010`'s
          control). A re-query issued during the same outage is not corroboration;
          it is the same silence answering a different question.
    - [ ] **Before retrying a write — re-query the state.** Never let a client
          error be the sole basis for a repeat of a non-idempotent operation.
    - [ ] ⚠️ **And treat "the transport was unhealthy" as a reason to stop and
          re-establish, not to proceed carefully.** Both instances happened while
          the host was under heavy IO load from a concurrent job, with the
          middleware refusing connections for about a minute. Any conclusion
          drawn in that window — read or write, either direction — was worthless,
          and neither session noticed the window was open until afterwards.
  - [ ] 📄 **Provenance.** Two concurrent docker-heap sessions, same night, same
        middleware, opposite directions, neither able to see its own defect. The
        pair only exists because one session published its failure and the other
        recognised its own shape in it — which is the argument in `010`'s last
        line, arriving a second time without being sought.
