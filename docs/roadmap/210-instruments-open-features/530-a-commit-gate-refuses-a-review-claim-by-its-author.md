- [ ] **A commit gate refuses a ⏳ review claimed by the session that
      authored, started or instructed the work.** From the principal's
      2026-11-22 ask, quoted on `210/520`, to move what can run as code out of
      the session-open prompt. The prompt's guard rail "Take a ⏳ review only
      if you are a session its author neither started nor instructed" is
      `REVIEW.md` doctrine for every session, so a gate fits whether or not
      the prompt was used. Every pointer already names its authoring session
      ("The authoring session (12a41aa2, …) queues this and does not take
      it"), and a claim names the claiming session's id. A pre-commit check
      that reads a pointer gaining `[~]` and refuses when the claim's session
      id is one the pointer names as author would make the rule hold without
      the prompt. Ground the two id forms against the board before building;
      "started or instructed" (a worker dispatched by the author) needs the
      author's dispatch record, so say what the gate cannot see.
