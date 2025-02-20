import re

def extract_markdown_images(text):

    image_regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_regex, text)
    return matches

def extract_markdown_links(text):

    link_regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(link_regex, text)
    return matches


# # Tests (add more comprehensive tests as needed)
# def test_extract_markdown_images():
#     text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
#     expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
#     assert extract_markdown_images(text) == expected

#     text = "![alt text](image.jpg)"
#     expected = [("alt text", "image.jpg")]
#     assert extract_markdown_images(text) == expected

#     text = ""  # Empty string
#     expected = []
#     assert extract_markdown_images(text) == expected

#     text = "No images here"
#     expected = []
#     assert extract_markdown_images(text) == expected

#     text = "![alt](url1) ![alt2](url2)" # Multiple images
#     expected = [("alt", "url1"), ("alt2", "url2")]
#     assert extract_markdown_images(text) == expected

# def test_extract_markdown_links():
#     text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
#     expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
#     assert extract_markdown_links(text) == expected

#     text = "[link](url)"
#     expected = [("link", "url")]
#     assert extract_markdown_links(text) == expected

#     text = ""  # Empty string
#     expected = []
#     assert extract_markdown_links(text) == expected

#     text = "No links here"
#     expected = []
#     assert extract_markdown_links(text) == expected

#     text = "[link1](url1) [link2](url2)" # Multiple links
#     expected = [("link1", "url1"), ("link2", "url2")]
#     assert extract_markdown_links(text) == expected


# # Run tests (you would normally use a test runner, but this is a simple example)
# test_extract_markdown_images()
# test_extract_markdown_links()
# print("All tests passed!")

# # Example usage:
# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and a link [to boot dev](https://www.boot.dev)"
# images = extract_markdown_images(text)
# links = extract_markdown_links(text)

# print("Images:", images)
# print("Links:", links)
