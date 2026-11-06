import re
from enum import Enum

from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in blocks if block.strip()]
    return blocks

def block_to_block_type(markdown: str) -> BlockType:
    if re.fullmatch(r"#{1,6} .*", markdown):
        return BlockType.HEADING
    if re.fullmatch(r"```\n.*```", markdown, re.DOTALL):
        return BlockType.CODE
    if all(line.startswith(">") for line in markdown.splitlines()):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in markdown.splitlines()):
        return BlockType.UNORDERED_LIST
    if markdown.startswith("1. "):
        count = 1
        ordered = True
        for line in markdown.splitlines():
            if line.startswith(f"{count}. "):
                count += 1
            else:
                ordered = False
        if ordered:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(text: str) -> list[HTMLNode]:
    return [text_node_to_html_node(node) for node in text_to_textnodes(text.replace("\n", " "))]

def markdown_to_html_node(markdown: str) -> ParentNode:
    page = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                children = text_to_children(block)
                html_block = ParentNode("p", children)
            case BlockType.HEADING:
                stripped = block.lstrip("#")
                heading_count = len(block) - len(stripped)
                children = text_to_children(stripped.strip())
                html_block = ParentNode(f"h{heading_count}", children)
            case BlockType.QUOTE:
                stripped = "\n".join(line.lstrip(">").strip() for line in block.splitlines())
                children = text_to_children(stripped.strip())
                html_block = ParentNode("blockquote", children)
            case BlockType.UNORDERED_LIST:
                children = [text_to_children(line[2:].strip()) for line in block.splitlines()]
                stripped = [ParentNode("li", child) for child in children]
                html_block = ParentNode("ul", stripped)
            case BlockType.ORDERED_LIST:
                children = [text_to_children(line.split(f"{i+1}. ", 1)[1].strip()) for i, line in enumerate(block.splitlines())]
                stripped = [ParentNode("li", child) for child in children]
                html_block = ParentNode("ol", stripped)
            case BlockType.CODE:
                code_node = [text_node_to_html_node(TextNode(block[4:-3], TextType.CODE))]
                html_block = ParentNode("pre", code_node)
        page.children.append(html_block)
    return page


                
