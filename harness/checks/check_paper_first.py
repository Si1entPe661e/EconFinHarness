"""Regression checks for the independent-replication instruction boundary."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]


class PaperFirstWorkflowChecks(unittest.TestCase):
    def test_mode_is_selected_before_author_code(self):
        text = (ROOT / "harness/workflows/replicate-paper.md").read_text()
        self.assertIn("Choose the reproduction mode before opening implementation files", text)
        self.assertLess(text.index("paper-first replication"), text.index("authorized code-reading"))
        self.assertIn("command histories", text)
        self.assertIn("packaged answer tables", text)
        self.assertNotIn("Read actual sample construction, estimation and export calls.", text)

    def test_presentation_preserves_the_same_boundary(self):
        text = (ROOT / "harness/skills/tables-figures-efh/SKILL.md").read_text()
        self.assertIn("In paper-first replication, preserve the source boundary", text)
        self.assertNotIn("Read existing output code before replacing its conventions.", text)

    def test_example_and_estimator_guidance_are_linked_and_available(self):
        paths = ["harness/workflows/paper-first-replication.md",
                 "harness/examples/war-discourse/run.R",
                 "harness/examples/war-discourse/checks.R",
                 "harness/skills/fama-macbeth-efh/two-pass-pricing.md"]
        for path in paths:
            self.assertTrue((ROOT / path).is_file(), path)
        text = (ROOT / "harness/skills/fama-macbeth-efh/SKILL.md").read_text()
        self.assertIn("two-pass-pricing.md", text)


if __name__ == "__main__":
    unittest.main()
