from htmlnode import LeafNode
from enum import Enum
from htmlnode import *



class TextType(Enum):
    TEXT = "text"
<<<<<<< HEAD
    NORMAL = "normal"
=======
>>>>>>> 89072548fd64700c7d2359e395b994f5add2834f
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

<<<<<<< HEAD
class TextNode():
=======

class TextNode:
>>>>>>> 89072548fd64700c7d2359e395b994f5add2834f
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
<<<<<<< HEAD
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

            
=======
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}")
>>>>>>> 89072548fd64700c7d2359e395b994f5add2834f
