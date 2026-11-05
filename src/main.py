from textnode import TextNode, TextType


def main():
    node = TextNode("this is text", TextType.LINK, "boot.dev")
    print(node)
main()