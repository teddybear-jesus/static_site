import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("this is a tag", "this is a value", None, {"href": "boot.dev"})
        self.assertEqual(node.props_to_html(), "href=\"boot.dev\"")

    def test_noteq(self):
        child = HTMLNode("this is a tag", "this is a value")
        node = HTMLNode("this is a tag", "this is a value", [child], {"href": "boot.dev"})
        node2 = HTMLNode("this is a tag", "this is a value")
        self.assertNotEqual(node, node2)

    def test_noteq_2(self):
        node = HTMLNode("this is a tag", "this is a value")
        node2 = HTMLNode("this is a tag", "this is a value")
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_2(self):
        node = LeafNode("p", "Hello, world!", {"href": "boot.dev"})
        self.assertEqual(node.to_html(), "<p href=\"boot.dev\">Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()