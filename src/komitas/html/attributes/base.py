from __future__ import annotations


class AttributeMeta(type):
    def __call__(self, *args, **kwargs):
        if hasattr(self, "__class_call__"):
            return self.__class_call__(*args, **kwargs)
        return super().__call__(*args, **kwargs)


class Attribute(metaclass=AttributeMeta):
    """
    Base HTML attribute. Subclasses are invoked with ``(component, value)`` and
    the attribute name is derived from the class name.
    """

    attribute_name: str | None = None

    @classmethod
    def __class_call__(cls, component, value):
        attr_name = cls.attribute_name or cls.__name__.replace("_", "-").lower()
        component.set(attr_name, value)
        return component
