import unittest

from markdown.markdown import markdown_to_html_node


class TestMarkdown(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """
# Heading 1

## Heading 2 with **bold**

###### Heading 6
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2 with <b>bold</b></h2><h6>Heading 6</h6></div>",
        )

    def test_blockquote(self):
        md = """
> This is a quote
> that spans multiple lines
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote that spans multiple lines</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- Item 1
- Item 2 with **bold**
- Item 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2 with <b>bold</b></li><li>Item 3</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. First item
2. Second item
3. Third item with _italic_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li><li>Third item with <i>italic</i></li></ol></div>",
        )

    def test_mixed_markdown(self):
        md = """
# My Blog Post

This is a paragraph with a [link to boot dev](https://www.boot.dev).

## Subheading

- List item 1
- List item 2

> "Knowledge is power"

1. Step one
2. Step two
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertTrue("<h1>My Blog Post</h1>" in html)
        self.assertTrue('<a href="https://www.boot.dev">link to boot dev</a>' in html)
        self.assertTrue("<h2>Subheading</h2>" in html)
        self.assertTrue("<ul><li>List item 1</li><li>List item 2</li></ul>" in html)
        self.assertTrue('<blockquote>"Knowledge is power"</blockquote>' in html)
        self.assertTrue("<ol><li>Step one</li><li>Step two</li></ol>" in html)


if __name__ == "__main__":
    unittest.main()
