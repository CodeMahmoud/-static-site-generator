from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(first, second):
        if (first.text == second.text and first.text_type == second.text_type and first.url == second.url):
            return True
        
        return False
    
    def __repr__(obj):
        return f"TextNode{obj.text, obj.text_type, obj.url}"