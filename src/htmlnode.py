class HTMLNODE():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'   
        return props_html

    def __repr__(self):
        return f"HTMLNODE {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNODE):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        
        props_string = self.props_to_html()  # This will call HTMLProps.to_html()
        
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}>{props_string}{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag},{self.value},{self.props})"


class ParentNode(HTMLNODE):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")

        if self.children is None:
            raise ValueError("invalid HTML: no children")

        props_string = self.props_to_html()  # This will call HTMLProps.to_html()
        children_html = "".join([child.to_html() for child in self.children])

        return f"<{self.tag}{props_string}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children} , {self.props})"

