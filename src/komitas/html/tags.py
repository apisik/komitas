from xml.etree.ElementTree import Element
from komitas.html.attributes import (
    GlobalAttribute,
    Attribute,
    HTMLAttribute,
    MetaAttribute,
    LinkAttribute,
    ScriptAttribute,
    HxAttribute,
    AriaLabel,
)

from typing import Union
from types import NoneType
from komitas.components import InteractiveComponent, Component


class Tag(Element):
    """
    The `Tag` element serves as the base class for all HTML tags in
    this framework.
    """

    allowed_attributes = [
        GlobalAttribute,
        HxAttribute,
        AriaLabel,
    ]

    attribute_extensions = []

    def __init_subclass__(cls):
        cls.__extend_attributes()
        return super().__init_subclass__()

    def __init__(self, text: str = None):
        super().__init__(self.__class__.__name__.lower())
        self.elements: list[Tag] = []
        self.interactive_components: dict[str, InteractiveComponent] = {}
        if text is not None and isinstance(text, str):
            self.text = text
        elif text is not None and isinstance(text, Tag):
            self.elements.append(text)

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

    def innrs(self, *elements: Union[str, Component, InteractiveComponent, "Tag"]):
        for element in elements:
            self.elements.append(element)
        return self

    def build(self):
        first_element = True
        last_element: Union[NoneType, Tag] = None
        for element in self.elements:
            if not isinstance(element, str):
                last_element = element

            if first_element and isinstance(element, str):
                self.text = element if self.text is None else self.text + element
                continue
            first_element = False

            if (
                not first_element
                and isinstance(element, str)
                and last_element is not None
            ):
                last_element.tail = (
                    element
                    if last_element.tail is None
                    else last_element.tail + element
                )

                continue

            if issubclass(element.__class__, InteractiveComponent) and isinstance(
                element, InteractiveComponent
            ):
                element_temp = element()
                element_temp.obj = element
                element = element_temp
            if issubclass(element.__class__, Component):
                element = element()

            if not isinstance(element, Element):
                raise TypeError(
                    f"Element {element} is not an instance of ElementTree.Element"
                )
            element.build()
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

    def __init__(self, text: str = ""):
        super().__init__()
        self.text = text


class H1(Tag):
    pass


class H2(Tag):
    pass


class H3(Tag):
    pass


class H4(Tag):
    pass


class H5(Tag):
    pass


class H6(Tag):
    pass


class Div(Tag):
    pass


class Button(Tag):
    def __init__(self, text: str = ""):
        super().__init__()
        self.text = text


class Pre(Tag):
    def __init__(self, text: str = ""):
        super().__init__()
        self.text = text


class Code(Tag):
    def __init__(self, text: str = ""):
        super().__init__()
        self.text = text


class Strong(Tag):
    pass


class Span(Tag):
    pass


class DD(Tag):
    pass


class DL(Tag):
    pass


class DT(Tag):
    pass


class Hr(Tag):
    pass


class Header(Tag):
    pass


class Ul(Tag):
    pass


class Li(Tag):
    pass


class Svg(Tag):
    pass


class Use(Tag):
    pass
