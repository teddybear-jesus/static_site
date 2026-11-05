import unittest

from textnode import (
    TextNode,
    TextType,
    text_node_to_html_node,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("banana", TextType.LINK, "boot.dev")
        node2 = TextNode("banana", TextType.LINK, "boot.dev")
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("banana", TextType.ITALIC, "boot.dev")
        node2 = TextNode("bananas", TextType.BOLD, "banana.dev")
        self.assertNotEqual(node, node2)

    def test_noteq_2(self):
        node = TextNode("banana", TextType.LINK, "boot.dev")
        node2 = TextNode("yippee", TextType.CODE, "boot.dev")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()
