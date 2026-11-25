"""The /atelier:session close action and the principal's hand copy are one text.

Board 450/030. The principal, 2026-11-24 (session 33d3cde8), copied the
"Ending the session" text out of the session-open prompt by hand to close
sessions, and asked for a command instead; his pick was `/atelier:session
close`. His standing rule for the sibling action (180/090, 2026-10-18): "You
need to ensure the there is no drift between the command and the text file
unless I authorise the drift." So the action points at the section and
restates none of it. This test fails if the action stops pointing at the
file and the section heading, starts copying the section's lines, or grows an
instruction the delivery job does not need. It cannot catch a paraphrase; the
action's own header bars that.

Same shape as tools/test_work_run_single_source.py: the committed copy is
read, never the working file, and a pending edit is warned about.
"""
import hashlib
import re
import unittest
from pathlib import Path

import test_work_run_single_source as wr

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "session" / "close.md"
ROUTER = ROOT / "skills" / "session" / "SKILL.md"
PROMPT = ROOT / "docs" / "method" / "session-open" / "session-open-prompt.md"
REF = "docs/method/session-open/session-open-prompt.md"
HEADING = "## Ending the session"

# The only files the action body may name.
ALLOWED_FILES = {REF}

# Each body paragraph must carry one of these anchors: the delivery jobs (where
# the section is, the committed read, the missing heading, the typed text, where
# it runs) and nothing else. A new paragraph of rules matches none and fails.
DELIVERY_ANCHORS = (
    "session-open prompt",       # whose text it runs
    "session-open-prompt.md",    # where the prompt is
    "under the heading",         # where the section starts and ends
    "committed copy",            # read the committed copy
    "is not there, stop",        # the heading is gone: fail loudly
    "typed after",               # where the typed text goes
    "any repo",                  # where it runs, with or without a repo
)

norm, flatten, copied_sentences, skill_body = (
    wr.norm, wr.flatten, wr.copied_sentences, wr.skill_body)

# The pinned body (test_action_body_is_pinned): set in the commit that last
# changed close.md's body, deliberately.
BODY_SHA256 = "a63e8df5ab854303c61460639bade3397e1cdac3949173fb090c4075701a8dc4"


def section(text: str) -> str:
    """The prompt's Ending the session section: from its heading to the next
    `## ` heading or the end of the file; empty if the heading is missing. A
    `## ` line inside a fenced block is the block's text, not a heading
    (review 2026-11-24, RK19: the finder stopped there)."""
    lines = text.splitlines()
    try:
        start = lines.index(HEADING)
    except ValueError:
        return ""
    out = []
    fence = None
    for line in lines[start + 1:]:
        m = re.match(r"^\s*(```|~~~)", line)
        if m:
            fence = None if fence == m.group(1) else (fence or m.group(1))
        elif fence is None and line.startswith("## "):
            break
        out.append(line)
    return "\n".join(out)


def body_digest(text: str) -> str:
    """SHA-256 of the action body, whitespace-normalised."""
    return hashlib.sha256(norm(skill_body(text)).encode("utf-8")).hexdigest()


class SessionCloseSingleSource(unittest.TestCase):
    def test_prompt_has_the_section(self):
        self.assertTrue(PROMPT.is_file(), f"{PROMPT} is missing")
        self.assertTrue(norm(section(PROMPT.read_text(encoding="utf-8"))),
                        f"{REF} has no {HEADING!r} section for the action to run")

    def test_section_finder_stops_at_the_next_heading(self):
        text = "## A\nalpha\n## Ending the session\nbeta\ngamma\n## Z\nomega\n"
        self.assertEqual(section(text).split(), ["beta", "gamma"])
        self.assertEqual(section("## A\nalpha\n"), "")

    def test_section_finder_reads_past_a_fenced_heading_line(self):
        text = ("## Ending the session\nbeta\n```\n## not a heading\n```\n"
                "gamma\n## Z\nomega\n")
        self.assertEqual(section(text).split(),
                         ["beta", "```", "##", "not", "a", "heading", "```", "gamma"])

    def test_action_body_is_pinned(self):
        """The anchors above let a new rule sit inside an anchored paragraph,
        a fallback section, a weakened stop or a wider read pass (review
        2026-11-24, RK19: 4 such mutations stayed green). So the body is
        pinned whole: any change to it fails here until BODY_SHA256 is set to
        the new digest in the same commit, which makes every change to the
        delivery text a deliberate one a reviewer sees in the diff."""
        self.assertEqual(body_digest(SKILL.read_text(encoding="utf-8")), BODY_SHA256,
                         "close.md's body changed: if the change is delivery "
                         "only and deliberate, set BODY_SHA256 to the new digest "
                         "in the same commit; a rule belongs in the prompt")

    def test_action_points_at_the_prompt_and_the_section(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("${CLAUDE_PLUGIN_ROOT}/" + REF, text)
        self.assertIn("../../" + REF, text)
        self.assertIn("`" + HEADING + "`", text)

    def test_action_restates_no_section_line(self):
        sect = section(PROMPT.read_text(encoding="utf-8"))
        self.assertTrue(sect)
        copied = copied_sentences(SKILL.read_text(encoding="utf-8"), sect)
        self.assertEqual(copied, [], "the action copies the section; point at "
                         "the file instead: " + "; ".join(copied))

    def test_action_restates_no_line_of_the_rest_of_the_prompt(self):
        copied = copied_sentences(SKILL.read_text(encoding="utf-8"),
                                  PROMPT.read_text(encoding="utf-8"))
        self.assertEqual(copied, [], "; ".join(copied))

    def test_copy_check_sees_a_section_line(self):
        sect = "1. Summarise the whole session succinctly, organised by the topics discussed.\n"
        skill = "Do this: summarise the whole session succinctly, organised by the topics discussed."
        self.assertEqual(len(copied_sentences(skill.replace("summarise", "Summarise"), sect)), 1)

    def test_action_body_is_delivery_only(self):
        body = skill_body(SKILL.read_text(encoding="utf-8"))
        paragraphs = [p for p in re.split(r"\n\s*\n", flatten(body)) if p.strip()]
        self.assertTrue(paragraphs)
        for para in paragraphs:
            flat = norm(para)
            self.assertTrue(
                any(a in flat for a in DELIVERY_ANCHORS),
                "a paragraph of the action body is not one of its delivery "
                "jobs (where the section is, the committed copy, the missing "
                "heading, the typed text, where it runs); a rule belongs in "
                f"the principal's prompt, not here: {flat[:80]!r}")

    def test_action_body_names_only_known_files(self):
        body = skill_body(SKILL.read_text(encoding="utf-8"))
        named = set(re.findall(r"[\w./${}-]*\w+\.(?:md|py|json|ya?ml|sh)\b", body))
        for ref in named:
            self.assertTrue(any(ref.endswith(ok) for ok in ALLOWED_FILES),
                            f"the action body names {ref!r}, not one of "
                            f"{sorted(ALLOWED_FILES)}")

    def test_action_reads_the_committed_copy_not_the_working_file(self):
        flat = norm(flatten(SKILL.read_text(encoding="utf-8")))
        self.assertIn("committed copy", flat)
        self.assertIn('git -C "${CLAUDE_PLUGIN_ROOT}" show HEAD:' + REF, flat)
        self.assertIn("do not open the working file", flat)

    def test_action_warns_when_an_edit_to_the_prompt_is_pending(self):
        flat = norm(flatten(SKILL.read_text(encoding="utf-8")))
        self.assertIn('git -C "${CLAUDE_PLUGIN_ROOT}" status --porcelain -- ' + REF, flat)
        self.assertIn("edits to the prompt are pending", flat)
        self.assertIn("you do not commit it", flat)

    def test_action_says_what_happens_without_a_checkout(self):
        flat = norm(flatten(SKILL.read_text(encoding="utf-8")))
        self.assertIn("not a git checkout", flat)
        self.assertIn("say which of the two applied", flat)

    def test_action_fails_loudly_when_the_heading_is_gone(self):
        flat = norm(flatten(SKILL.read_text(encoding="utf-8")))
        self.assertIn("If the heading is not there, stop.", flat)
        self.assertIn("no close to run", flat)
        self.assertIn("Do not close the session from memory", flat)

    def test_action_hands_the_typed_words_on_and_runs_anywhere(self):
        text = SKILL.read_text(encoding="utf-8")
        flat = norm(flatten(text))
        self.assertIn("(`$ARGUMENTS`)", text)
        self.assertIn("extra close brief", flat)
        self.assertIn("any repo", flat)
        self.assertIn("no repo, run it without --root", flat)

    def test_router_lists_close(self):
        body = ROUTER.read_text(encoding="utf-8")
        self.assertRegex(body, r"(?m)^\| `close` \| \[`close\.md`\]\(close\.md\) \|")


if __name__ == "__main__":
    unittest.main()
