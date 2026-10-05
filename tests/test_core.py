import tempfile
import unittest
from pathlib import Path

from ats_auditor.core import (
    detect_contacts,
    detect_sections,
    experience_date_order,
    keyword_match,
)


SAMPLE = """Avery Candidate
Sample City, CA | +1 (555) 010-2040 | avery.candidate@example.invalid
linkedin.com/in/example-candidate | github.com/example-candidate
EDUCATION
Example University
EXPERIENCE
Company A | Jul 2026 - Present
• Built automated testing in Python.
Company B | Nov 2023 - Feb 2024
• Improved SQL pipelines by 20%.
PROJECTS
Local Tool
• Developed a private scanner.
TECHNICAL SKILLS
Python, SQL, Docker
"""


class CoreTests(unittest.TestCase):
    def test_sections(self):
        self.assertEqual(detect_sections(SAMPLE), ["education", "experience", "projects", "skills"])

    def test_markdown_sections(self):
        text = "# Candidate\n\n## Education\n\n## Experience\n\n## Projects\n\n## Technical Skills"
        self.assertEqual(detect_sections(text), ["education", "experience", "projects", "skills"])

    def test_contacts(self):
        contacts = detect_contacts(SAMPLE)
        self.assertTrue(all(contacts.values()))

    def test_reverse_chronology(self):
        ordered, endpoints = experience_date_order(SAMPLE)
        self.assertTrue(ordered)
        self.assertEqual(endpoints, [9999, 2024])

    def test_bad_chronology(self):
        text = SAMPLE.replace(
            "Company B | Nov 2023 - Feb 2024",
            "Company B | May 2022 - Aug 2022\nCompany C | Nov 2023 - Feb 2024",
        )
        ordered, _ = experience_date_order(text)
        self.assertFalse(ordered)

    def test_keyword_match(self):
        matched, missing = keyword_match("Python and Docker", "Python, Docker, and Kubernetes required", ["python", "docker", "kubernetes"])
        self.assertEqual(matched, ["docker", "python"])
        self.assertEqual(missing, ["kubernetes"])


if __name__ == "__main__":
    unittest.main()
