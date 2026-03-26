import unittest

from markdown.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_basic(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")

    def test_extract_title_with_extra_spaces(self):
        md = "#  Hello World  "
        self.assertEqual(extract_title(md), "Hello World")

    def test_extract_title_not_at_start(self):
        md = """
This is a paragraph.

# The Real Title

More text here.
"""
        self.assertEqual(extract_title(md), "The Real Title")

    def test_extract_title_multiple_lines(self):
        md = "# Title\nMore text\nEven more text"
        self.assertEqual(extract_title(md), "Title")

    def test_extract_title_exception_no_h1(self):
        md = "## This is an H2"
        with self.assertRaises(Exception) as cm:
            extract_title(md)
        self.assertEqual(str(cm.exception), "no title found")

    def test_extract_title_exception_empty(self):
        md = ""
        with self.assertRaises(Exception) as cm:
            extract_title(md)
        self.assertEqual(str(cm.exception), "no title found")


if __name__ == "__main__":
    unittest.main()
