import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is text", TextType.BOLD_TEXT)
        node2 = TextNode("This is different text", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("Text", TextType.PLAIN_TEXT, None)
        node2 = TextNode("Text", TextType.PLAIN_TEXT, "https://boot.dev")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
