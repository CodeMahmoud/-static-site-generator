from extractmarkdownimages import extract_markdown_images, extract_markdown_links
import re
from textnode import TextNode, TextType


def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        # If not a text node, just add it to results
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue

        # Get all image tuples from the text
        images = extract_markdown_images(old_node.text)

        # If no images found, just add the original node
        if not images:
            result.append(old_node)
            continue

        # Now we need to split the text
        remaining_text = old_node.text

        for image_alt, image_url in images:
            # Split at the image markdown
            image_markdown = f"![{image_alt}]({image_url})"
            parts = remaining_text.split(image_markdown, 1)

            # Add text before the image if not empty
            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))

            # Add the image node
            result.append(TextNode(image_alt, TextType.IMAGE, image_url))

            # Update remaining text
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""

        # Add any remaining text after the last image
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))

    return result



def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        # If not a text node, just add it to results
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue

        # Get all link tuples from the text
        links = extract_markdown_links(old_node.text)

        # If no links found, just add the original node
        if not links:
            result.append(old_node)
            continue

        # Now we need to split the text
        remaining_text = old_node.text

        for link_text, link_url in links:
            # Split at the link markdown
            link_markdown = f"[{link_text}]({link_url})"
            parts = remaining_text.split(link_markdown, 1)

            # Add text before the link if not empty
            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))

            # Add the link node
            result.append(TextNode(link_text, TextType.LINK, link_url))

            # Update remaining text
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""

        # Add any remaining text after the last link
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))

    return result