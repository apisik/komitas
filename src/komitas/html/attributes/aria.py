from __future__ import annotations

from .base import Attribute

__all__ = [
    "AriaAttribute",
    "Aria_Activedescendant",
    "Aria_Atomic",
    "Aria_Autocomplete",
    "Aria_Busy",
    "Aria_Checked",
    "Aria_Colcount",
    "Aria_Colindex",
    "Aria_Colspan",
    "Aria_Controls",
    "Aria_Current",
    "Aria_Describedby",
    "Aria_Details",
    "Aria_Disabled",
    "Aria_Errormessage",
    "Aria_Expanded",
    "Aria_Flowto",
    "Aria_Haspopup",
    "Aria_Hidden",
    "Aria_Invalid",
    "Aria_Keyshortcuts",
    "Aria_Label",
    "Aria_Labelledby",
    "Aria_Level",
    "Aria_Live",
    "Aria_Modal",
    "Aria_Multiline",
    "Aria_Multiselectable",
    "Aria_Orientation",
    "Aria_Owns",
    "Aria_Placeholder",
    "Aria_Posinset",
    "Aria_Pressed",
    "Aria_Readonly",
    "Aria_Relevant",
    "Aria_Required",
    "Aria_Roledescription",
    "Aria_Rowcount",
    "Aria_Rowindex",
    "Aria_Rowspan",
    "Aria_Selected",
    "Aria_Setsize",
    "Aria_Sort",
    "Aria_Valuemax",
    "Aria_Valuemin",
    "Aria_Valuenow",
    "Aria_Valuetext",
    "Role"
]

class AriaAttribute(Attribute):
    """ARIA attributes shared across interactive elements."""

    pass

class Aria_Activedescendant(AriaAttribute):
    attribute_name = "aria-activedescendant"

class Aria_Atomic(AriaAttribute):
    attribute_name = "aria-atomic"

class Aria_Autocomplete(AriaAttribute):
    attribute_name = "aria-autocomplete"

class Aria_Busy(AriaAttribute):
    attribute_name = "aria-busy"

class Aria_Checked(AriaAttribute):
    attribute_name = "aria-checked"

class Aria_Colcount(AriaAttribute):
    attribute_name = "aria-colcount"

class Aria_Colindex(AriaAttribute):
    attribute_name = "aria-colindex"

class Aria_Colspan(AriaAttribute):
    attribute_name = "aria-colspan"

class Aria_Controls(AriaAttribute):
    attribute_name = "aria-controls"

class Aria_Current(AriaAttribute):
    attribute_name = "aria-current"

class Aria_Describedby(AriaAttribute):
    attribute_name = "aria-describedby"

class Aria_Details(AriaAttribute):
    attribute_name = "aria-details"

class Aria_Disabled(AriaAttribute):
    attribute_name = "aria-disabled"

class Aria_Errormessage(AriaAttribute):
    attribute_name = "aria-errormessage"

class Aria_Expanded(AriaAttribute):
    attribute_name = "aria-expanded"

class Aria_Flowto(AriaAttribute):
    attribute_name = "aria-flowto"

class Aria_Haspopup(AriaAttribute):
    attribute_name = "aria-haspopup"

class Aria_Hidden(AriaAttribute):
    attribute_name = "aria-hidden"

class Aria_Invalid(AriaAttribute):
    attribute_name = "aria-invalid"

class Aria_Keyshortcuts(AriaAttribute):
    attribute_name = "aria-keyshortcuts"

class Aria_Label(AriaAttribute):
    attribute_name = "aria-label"

class Aria_Labelledby(AriaAttribute):
    attribute_name = "aria-labelledby"

class Aria_Level(AriaAttribute):
    attribute_name = "aria-level"

class Aria_Live(AriaAttribute):
    attribute_name = "aria-live"

class Aria_Modal(AriaAttribute):
    attribute_name = "aria-modal"

class Aria_Multiline(AriaAttribute):
    attribute_name = "aria-multiline"

class Aria_Multiselectable(AriaAttribute):
    attribute_name = "aria-multiselectable"

class Aria_Orientation(AriaAttribute):
    attribute_name = "aria-orientation"

class Aria_Owns(AriaAttribute):
    attribute_name = "aria-owns"

class Aria_Placeholder(AriaAttribute):
    attribute_name = "aria-placeholder"

class Aria_Posinset(AriaAttribute):
    attribute_name = "aria-posinset"

class Aria_Pressed(AriaAttribute):
    attribute_name = "aria-pressed"

class Aria_Readonly(AriaAttribute):
    attribute_name = "aria-readonly"

class Aria_Relevant(AriaAttribute):
    attribute_name = "aria-relevant"

class Aria_Required(AriaAttribute):
    attribute_name = "aria-required"

class Aria_Roledescription(AriaAttribute):
    attribute_name = "aria-roledescription"

class Aria_Rowcount(AriaAttribute):
    attribute_name = "aria-rowcount"

class Aria_Rowindex(AriaAttribute):
    attribute_name = "aria-rowindex"

class Aria_Rowspan(AriaAttribute):
    attribute_name = "aria-rowspan"

class Aria_Selected(AriaAttribute):
    attribute_name = "aria-selected"

class Aria_Setsize(AriaAttribute):
    attribute_name = "aria-setsize"

class Aria_Sort(AriaAttribute):
    attribute_name = "aria-sort"

class Aria_Valuemax(AriaAttribute):
    attribute_name = "aria-valuemax"

class Aria_Valuemin(AriaAttribute):
    attribute_name = "aria-valuemin"

class Aria_Valuenow(AriaAttribute):
    attribute_name = "aria-valuenow"

class Aria_Valuetext(AriaAttribute):
    attribute_name = "aria-valuetext"

class Role(AriaAttribute):
    attribute_name = "role"
