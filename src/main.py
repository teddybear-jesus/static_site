from inline_markdown import text_to_textnodes


def main():
    text = r"This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)
    for node in nodes:
        print(node)
main()