class AttributeMeta(type):
    def __call__(self, *args, **kwargs):
        if hasattr(self, "__class_call__"):
            return self.__class_call__(*args, **kwargs)
        return super().__call__(*args, **kwargs)


class Attribute(metaclass=AttributeMeta):
    @classmethod
    def __class_call__(cls, component, value):
        component.set(cls.__name__.replace("_", "-").lower(), value)
        return component


# Global Attributes
class GlobalAttribute(Attribute):
    pass


class Class(GlobalAttribute):
    pass


class Id(GlobalAttribute):
    pass


# HTML Attributes
class HTMLAttribute(Attribute):
    pass


class Version(HTMLAttribute):
    pass


class xmlns(HTMLAttribute):
    pass


class Lang(HTMLAttribute):
    pass


# Meta Attributes
class MetaAttribute(Attribute):
    pass


class Charset(MetaAttribute):
    pass


class Name(MetaAttribute):
    pass


class Content(MetaAttribute):
    pass


# Link Attributes
class LinkAttribute(Attribute):
    pass


class Href(LinkAttribute):
    pass


class Rel(LinkAttribute):
    pass


# script Attributes
class ScriptAttribute(Attribute):
    pass


class Integrity(LinkAttribute, ScriptAttribute):
    pass


class Crossorigin(LinkAttribute, ScriptAttribute):
    pass


class Src(ScriptAttribute):
    pass


# Aria attributes
class AriaLabel(Attribute):
    pass


class Aria_Hidden(AriaLabel):
    pass


class Aria_Current(AriaLabel):
    pass


class Width(GlobalAttribute):
    pass


class Height(GlobalAttribute):
    pass


class Data_Bs_Theme(GlobalAttribute):
    pass


# htmx attributes
class HxAttribute(Attribute):
    pass


class Hx_Get(HxAttribute):
    pass


class Hx_Vals(HxAttribute):
    pass


class Hx_Swap(HxAttribute):
    pass


class Hx_Target(HxAttribute):
    pass

class Hx_Swap_Oob(HxAttribute):
    pass
