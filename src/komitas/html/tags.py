from xml.etree.ElementTree import Element
from komitas.html.attributes import (
    GlobalAttribute,
    Attribute,
    HTMLAttribute,
    MetaAttribute,
    LinkAttribute,
    ScriptAttribute,
    HxAttribute,
)
class InteractiveComponent:
    pass


class Tag(Element):
    allowed_attributes = [
        GlobalAttribute,
        HxAttribute,
    ]

    attribute_extensions = []

    def __init_subclass__(cls):
        cls.__extend_attributes()
        return super().__init_subclass__()

    def __init__(self):
        super().__init__(self.__class__.__name__.lower())

    @classmethod
    def __extend_attributes(cls):
        for extension in cls.attribute_extensions:
            cls.allowed_attributes.append(extension)

    def attrs(self, *attributes: tuple[Attribute, str]):
        for attribute, value in attributes:
            if not issubclass(attribute, tuple(self.allowed_attributes)):
                raise TypeError(
                    f"Attribute {attribute.__name__} is not allowed for tag {self.__class__.__name__}"
                )
            attribute(self, value)
        return self

    def innrs(self, *elements: Element):
        for element in elements:
            # if isinstance(element, InteractiveComponent):
            #     element = element()
            self.append(element)
        return self


# Main Root


class HTML(Tag):
    attribute_extensions = [
        HTMLAttribute,
    ]


class Head(Tag):
    pass


class Title(Tag):
    def __init__(self, text: str = ""):
        super().__init__()
        self.text = text

    pass


class Body(Tag):
    pass


class P(Tag):
    def __init__(self, text: str = ""):
        super().__init__()
        self.text = text


class A(Tag):
    pass


class Meta(Tag):
    attribute_extensions = [
        MetaAttribute,
    ]
    pass


class Link(Tag):
    attribute_extensions = [
        LinkAttribute,
    ]
    pass


class Script(Tag):
    attribute_extensions = [
        ScriptAttribute,
    ]
    pass


class H1(Tag):
    def __init__(self, text: str = ""):
        super().__init__()
        self.text = text


class Div(Tag):
    pass


class Button(Tag):
    def __init__(self, text: str = ""):
        super().__init__()
        self.text = text
