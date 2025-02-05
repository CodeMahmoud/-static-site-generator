import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    global TextNode
    global TextType
    doc = TextType
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        # if node.url == None or node2 == None:
        #     raise Exception("please provide a valid url address")
        self.assertEqual(node, node2)
    
    # def test_url(self):
    #     if self.url == None:
    #         raise Exception("please provide a valid url address")

   
    
if __name__ == "__main__":
    unittest.main()