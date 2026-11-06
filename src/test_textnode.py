import unittest

from markdown_blocks import BlockType, block_to_block_type
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

    def test_blocktype(self):
        text = "This is just a normal paragraph"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

    def test_blocktype2(self):
        text = """```
def test_blocktype3(self):
    text = "This is just a normal paragraph"
    self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
```"""
        self.assertEqual(block_to_block_type(text), BlockType.CODE)

    def test_blocktype3(self):
        text = ">This is a quote"
        self.assertEqual(block_to_block_type(text), BlockType.QUOTE)

    def test_blocktype4(self):
        text = """>This is a longer quote
> Heres the second line"""
        self.assertEqual(block_to_block_type(text), BlockType.QUOTE)

    def test_blocktype5(self):
        text = "# This is a heading"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING)

    def test_blocktype6(self):
        text = "### This is a heading 3"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING)

    def test_blocktype7(self):
        text = "- This is an unordered list of 1"
        self.assertEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)

    def test_blocktype8(self):
        text = """- This is a longer list
- Here's another bit"""
        self.assertEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)

    def test_blocktype9(self):
        text = """- This is a longer list
-This bit is bad
So it this"""
        self.assertNotEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)

    def test_blocktype10(self):
        text = "1. This is a short list"
        self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST)

    def test_blocktype11(self):
        text = """1. This is a longer list
2. This bit is good
3. So it this"""
        self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST)

    def test_blocktype12(self):
        text = """1. This is a longer list
2. This bit is ok
4. This is bad"""
        self.assertNotEqual(block_to_block_type(text), BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main()
