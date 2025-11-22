import komitas.html.tags as tg


class AttributeMeta(type):
    attribute_name: str | None = None

    def __call__(self, tag: tg.Tag, value: str):
        if hasattr(self, "__class_call__"):
            return self.__class_call__(tag, value)
        return super().__call__(tag, value)

    @classmethod
    def __class_call__(cls, tag, value):
        attr_name = cls.attribute_name or cls.__name__.replace("_", "-").lower()
        tag.set(attr_name, value)
        return tag


class Attribute(metaclass=AttributeMeta):
    """
    Base HTML attribute. Subclasses are invoked with ``(tag, value)`` and
    the attribute name is derived from the class name.
    """

    attribute_name: str | None = None

    def __init__(self, tag: tg.Tag, value: str) -> None:
        self.tag = tag
        self.value = value

    @classmethod
    def __class_call__(cls, tag, value):
        attr_name = cls.attribute_name or cls.__name__.replace("_", "-").lower()
        tag.set(attr_name, value)
        return tag
