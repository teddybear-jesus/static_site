class HTMLNode():
    def __init__(self, tag: str | None = None, value: str| None = None, children: list[HTMLNode]| None = None, props: dict| None = None):
        self.tag: str = tag
        self.value: str = value
        self.children: list[HTMLNode] = children
        self.props: dict = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        formatted_props = []
        for k, v in self.props.items():
            formatted_props.append(f"{k}=\"{v}\"")
        return " ".join(formatted_props)

    def __repr__(self):
        output = []
        if self.tag is not None:
            output.append(f"tag: {self.tag}")
        if self.value is not None:
            output.append(f"value: {self.value}")
        if self.children is not None:
            for child in self.children:
                output.append(f"child: {child}")
        if self.props is not None:
            output.append(f"props: {self.props_to_html()}")
        return "\n".join(output)

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError()
        if not self.tag:
            return self.value
        elif self.props is not None:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"


    def __repr__(self):
        output = []
        if self.tag is not None:
            output.append(f"tag: {self.tag}")
        if self.value is not None:
            output.append(f"value: {self.value}")
        if self.props is not None:
            output.append(f"props: {self.props_to_html()}")
        return "\n".join(output)

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("missing tag")
        if self.children is None:
            raise ValueError("missing children")
        else:
            if self.props is not None:
                output = [f"<{self.tag} {self.props_to_html()}>"]
            else:
                output =  [f"<{self.tag}>"]
            for child in self.children:
                output.append(child.to_html())
            output.append(f"</{self.tag}>")
        return "".join(output)
