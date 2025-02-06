class HTMLNODE():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        # print(props_string)
        props_html = " ".join(f'{key}="{value}"' for key, value in self.props.items()) if self.props else ""

        return props_html


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNODE):
    def __init__(self. tag, value, props = None):
        super.__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        
        if self.tag is None:
            return self.value
        
        return props_string = " ".join(f'{key}="{value}"' for key, value in self.props.items()) if self.props else ""

        def __repr__(self):
            return f"LeafNode({self.tag}, {self.vale}, {self.props})"