from enum import Enum
from htmlnode import *


class TextType(Enum):
    TEXT = "text"
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (self.text == other.text and self.text_type == other.text_type and self.url == other.url):
            return True
        
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node not in TextType:
        raise Exception("Unknow TextType")
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.value)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.value)
    if text_node.text_type == TextType.ITALIC:
        return ("i", text_node.value)
    if text_node.text_type == TextType.CODE:
        return ("code", text_node.value)
    if text_node.text_type == TextType.LINK:
        return ("a", text_node.value)
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}")

            