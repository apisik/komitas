from xml.etree.ElementTree import Element
from komitas.html.attributes import (
    Attribute,
    GlobalAttribute,
    HxAttribute,
    AriaAttribute,
    get_tag_attribute_mixins,
)

from typing import Union
from types import NoneType

import komitas.application.component as cmp


class ObjReferencingElement(Element):
    def __init__(self, *args, **kwargs) -> None:
        self.obj: Union[cmp.InteractiveComponent, NoneType] = None
        super().__init__(*args, **kwargs)

    def find(
        self, path: str, namespaces: dict[str, str] | None = None
    ) -> "ObjReferencingElement | None":
        return super().find(path, namespaces)  # type: ignore


class Tag(ObjReferencingElement):
    """
    The `Tag` element serves as the base class for all HTML tags in
    this framework.
    """

    allowed_attributes = [
        GlobalAttribute,
        HxAttribute,
        AriaAttribute,
    ]

    attribute_extensions = []

    def __init_subclass__(cls):
        cls.allowed_attributes = list(cls.allowed_attributes)
        cls.__extend_attributes()
        cls.__extend_tag_specific_attributes()
        return super().__init_subclass__()

    def __init__(self, text: Union[str, "Tag"] = ""):
        super().__init__(self.__class__.__name__.lower())
        self.elements: list[
            Union[str, cmp.Component, cmp.InteractiveComponent, "Tag"]
        ] = []
        self.interactive_components: dict[str, cmp.InteractiveComponent] = {}
        if text is not None and isinstance(text, str):
            self.text = text
        elif text is not None and isinstance(text, Tag):
            self.elements.append(text)

    @classmethod
    def __extend_attributes(cls):
        for extension in cls.attribute_extensions:
            cls.allowed_attributes.append(extension)

    @classmethod
    def __extend_tag_specific_attributes(cls):
        for mixin in get_tag_attribute_mixins(cls.__name__.lower()):
            if mixin not in cls.allowed_attributes:
                cls.allowed_attributes.append(mixin)

    def attrs(self, *attributes: tuple[type[Attribute], str]):
        for attribute, value in attributes:
            if not issubclass(attribute, tuple(self.allowed_attributes)):
                raise TypeError(
                    f"Attribute {attribute.__name__} is not allowed for tag {self.__class__.__name__}"
                )
            attribute(self, value)
        return self

    def innrs(
        self,
        *elements: Union[str, cmp.Component, cmp.InteractiveComponent, "Tag"],
    ):
        for element in elements:
            self.elements.append(element)
        return self

    def build(self):
        first_element = True
        last_element: Union[NoneType, Tag, cmp.Component, cmp.InteractiveComponent] = (
            None
        )
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
                and isinstance(last_element, "Tag")
            ):
                last_element.tail = (
                    element
                    if last_element.tail is None
                    else last_element.tail + element
                )

                continue

            if issubclass(element.__class__, cmp.InteractiveComponent) and isinstance(
                element, cmp.InteractiveComponent
            ):
                element_temp = element()
                element_temp.obj = element
                element = element_temp
                if element.obj is not None:
                    element.obj.model.register_component(element.obj)
            if (
                issubclass(element.__class__, cmp.Component)
                and not isinstance(element, str)
                and not isinstance(element, "Tag")
            ):
                element = element()

            if not isinstance(element, Element):
                raise TypeError(
                    f"Element {element} is not an instance of ElementTree.Element"
                )
            element.build()
            self.append(element)
        return self


class HTML(Tag):
    pass


class Head(Tag):
    pass


class Title(Tag):
    def __init__(self, text: str = ""):
        super().__init__()
        self.text = text


class Base(Tag):
    pass


class Link(Tag):
    pass


class Meta(Tag):
    pass


class Style(Tag):
    pass


class Body(Tag):
    pass


# Sectioning content
class Address(Tag):
    pass


class Article(Tag):
    pass


class Aside(Tag):
    pass


class Footer(Tag):
    pass


class Header(Tag):
    pass


class Hgroup(Tag):
    pass


class Main(Tag):
    pass


class Nav(Tag):
    pass


class Section(Tag):
    pass


# Text content
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


class P(Tag):
    pass


class Blockquote(Tag):
    pass


class Pre(Tag):
    def __init__(self, text: str = ""):
        super().__init__()
        self.text = text


class Ol(Tag):
    pass


class Ul(Tag):
    pass


class Li(Tag):
    pass


class Dl(Tag):
    pass


class Dt(Tag):
    pass


class Dd(Tag):
    pass


class Figure(Tag):
    pass


class Figcaption(Tag):
    pass


class Hr(Tag):
    pass


class Div(Tag):
    pass


# Inline text semantics
class A(Tag):
    pass


class Abbr(Tag):
    pass


class B(Tag):
    pass


class Bdi(Tag):
    pass


class Bdo(Tag):
    pass


class Br(Tag):
    pass


class Cite(Tag):
    pass


class Code(Tag):
    def __init__(self, text: str = ""):
        super().__init__()
        self.text = text


class Data(Tag):
    pass


class Dfn(Tag):
    pass


class Em(Tag):
    pass


class I(Tag):  # noqa: E742
    pass


class Kbd(Tag):
    pass


class Mark(Tag):
    pass


class Q(Tag):
    pass


class Rp(Tag):
    pass


class Rt(Tag):
    pass


class Ruby(Tag):
    pass


class S(Tag):
    pass


class Samp(Tag):
    pass


class Small(Tag):
    pass


class Span(Tag):
    pass


class Strong(Tag):
    pass


class Sub(Tag):
    pass


class Sup(Tag):
    pass


class Time(Tag):
    pass


class U(Tag):
    pass


class Var(Tag):
    pass


class Wbr(Tag):
    pass


class Del(Tag):
    pass


class Ins(Tag):
    pass


# Media elements
class Area(Tag):
    pass


class Audio(Tag):
    pass


class Img(Tag):
    pass


class Map(Tag):
    pass


class Track(Tag):
    pass


class Video(Tag):
    pass


class Picture(Tag):
    pass


class Source(Tag):
    pass


class Canvas(Tag):
    pass


class Svg(Tag):
    pass


class Use(Tag):
    pass


# Embedded content
class Embed(Tag):
    pass


class Iframe(Tag):
    pass


class Object(Tag):
    pass


class Param(Tag):
    pass


class Portal(Tag):
    pass


class Math(Tag):
    pass


# Scripting
class Script(Tag):
    def __init__(self, text: str = ""):
        super().__init__()
        self.text = text


class Noscript(Tag):
    pass


class Template(Tag):
    pass


class Slot(Tag):
    pass


# Table content
class Table(Tag):
    pass


class Caption(Tag):
    pass


class Colgroup(Tag):
    pass


class Col(Tag):
    pass


class Tbody(Tag):
    pass


class Thead(Tag):
    pass


class Tfoot(Tag):
    pass


class Tr(Tag):
    pass


class Td(Tag):
    pass


class Th(Tag):
    pass


# Forms
class Form(Tag):
    pass


class Label(Tag):
    pass


class Input(Tag):
    pass


class Button(Tag):
    def __init__(self, text: str = ""):
        super().__init__()
        self.text = text


class Select(Tag):
    pass


class Datalist(Tag):
    pass


class Optgroup(Tag):
    pass


class Option(Tag):
    pass


class Textarea(Tag):
    pass


class Output(Tag):
    pass


class Progress(Tag):
    pass


class Meter(Tag):
    pass


class Fieldset(Tag):
    pass


class Legend(Tag):
    pass


class Details(Tag):
    pass


class Summary(Tag):
    pass


class Dialog(Tag):
    pass


class Menu(Tag):
    pass
