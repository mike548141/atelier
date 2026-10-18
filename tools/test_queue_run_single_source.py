"""The /atelier:queue-run skill and the principal's hand copy are one text.

Mike, 2026-10-18 (180/090): "You need to ensure the there is no drift between
the command and the text file unless I authorise the drift." The skill loads
docs/method/session-open/session-open-prompt.md and restates none of it, so
the command runs exactly the file he can open and paste. This test fails if
the skill stops pointing at the file, or starts copying the file's lines into
itself (a second copy is the start of drift). It cannot catch a paraphrase;
the skill's own header bars that.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "queue-run" / "SKILL.md"
PROMPT = ROOT / "docs" / "method" / "session-open" / "session-open-prompt.md"
REF = "docs/method/session-open/session-open-prompt.md"


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


class QueueRunSingleSource(unittest.TestCase):
    def test_prompt_file_exists(self):
        self.assertTrue(PROMPT.is_file(), f"{PROMPT} is missing")

    def test_skill_points_at_the_prompt(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("${CLAUDE_PLUGIN_ROOT}/" + REF, text)
        self.assertIn("../../" + REF, text)

    def test_skill_restates_no_prompt_line(self):
        skill = norm(SKILL.read_text(encoding="utf-8"))
        copied = []
        for para in PROMPT.read_text(encoding="utf-8").split("\n\n"):
            for sentence in re.split(r"(?<=[.!?])\s+", norm(para)):
                if len(sentence) >= 40 and sentence in skill:
                    copied.append(sentence)
        self.assertEqual(copied, [], "the skill copies prompt text; point at "
                         "the file instead: " + "; ".join(copied))


if __name__ == "__main__":
    unittest.main()
