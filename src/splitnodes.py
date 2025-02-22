from textnode import *
from htmlnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)

        else:
            parts = node.text.split(delimiter)
            inside_delimiter = False
            for i, part in enumerate(parts):
                if part:
                    current_type = text_type if inside_delimiter else TextType.TEXT
                    new_nodes.append(TextNode(part, current_type))
                inside_delimiter = not inside_delimiter if i < len(parts) - 1 else inside_delimiter

    return new_nodes
