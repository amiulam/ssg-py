import unittest

from nodes.textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_diff_text_property(self):
        node = TextNode("Test different text type", TextType.BOLD)
        node2 = TextNode("Test different text type", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://amiulam.cloud")
        node2 = TextNode(
            "This is a text node", TextType.ITALIC, "https://amiulam.cloud"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://amiulam.cloud")
        self.assertEqual(
            "TextNode(This is a text node, text, https://amiulam.cloud)", repr(node)
        )

    def test_text_to_html(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image_to_html(self):
        node = TextNode("test image", TextType.IMAGE, "/public/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props, {"src": "/public/image.png", "alt": "test image"}
        )

    def test_bold_to_html(self):
        node = TextNode("test bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "test bold")

    def test_link_to_html(self):
        node = TextNode("my portfolio", TextType.LINK, "https://amiulam.cloud")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "my portfolio")
        self.assertEqual(html_node.props, {"href": "https://amiulam.cloud"})


if __name__ == "__main__":
    unittest.main()