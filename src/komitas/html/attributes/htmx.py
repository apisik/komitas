from __future__ import annotations

from .base import Attribute

__all__ = [
    "HxAttribute",
    "Hx_Boost",
    "Hx_Confirm",
    "Hx_Delete",
    "Hx_Disable",
    "Hx_Disinherit",
    "Hx_Encoding",
    "Hx_Ext",
    "Hx_Get",
    "Hx_Headers",
    "Hx_History",
    "Hx_History_Elt",
    "Hx_Include",
    "Hx_Indicator",
    "Hx_Params",
    "Hx_Patch",
    "Hx_Post",
    "Hx_Preserve",
    "Hx_Prompt",
    "Hx_Put",
    "Hx_Request",
    "Hx_Select",
    "Hx_Select_Oob",
    "Hx_Sse",
    "Hx_Swap",
    "Hx_Swap_Oob",
    "Hx_Sync",
    "Hx_Target",
    "Hx_Trigger",
    "Hx_Vals"
]

class HxAttribute(Attribute):
    """htmx attribute namespace."""

    pass

class Hx_Boost(HxAttribute):
    attribute_name = "hx-boost"

class Hx_Confirm(HxAttribute):
    attribute_name = "hx-confirm"

class Hx_Delete(HxAttribute):
    attribute_name = "hx-delete"

class Hx_Disable(HxAttribute):
    attribute_name = "hx-disable"

class Hx_Disinherit(HxAttribute):
    attribute_name = "hx-disinherit"

class Hx_Encoding(HxAttribute):
    attribute_name = "hx-encoding"

class Hx_Ext(HxAttribute):
    attribute_name = "hx-ext"

class Hx_Get(HxAttribute):
    attribute_name = "hx-get"

class Hx_Headers(HxAttribute):
    attribute_name = "hx-headers"

class Hx_History(HxAttribute):
    attribute_name = "hx-history"

class Hx_History_Elt(HxAttribute):
    attribute_name = "hx-history-elt"

class Hx_Include(HxAttribute):
    attribute_name = "hx-include"

class Hx_Indicator(HxAttribute):
    attribute_name = "hx-indicator"

class Hx_Params(HxAttribute):
    attribute_name = "hx-params"

class Hx_Patch(HxAttribute):
    attribute_name = "hx-patch"

class Hx_Post(HxAttribute):
    attribute_name = "hx-post"

class Hx_Preserve(HxAttribute):
    attribute_name = "hx-preserve"

class Hx_Prompt(HxAttribute):
    attribute_name = "hx-prompt"

class Hx_Put(HxAttribute):
    attribute_name = "hx-put"

class Hx_Request(HxAttribute):
    attribute_name = "hx-request"

class Hx_Select(HxAttribute):
    attribute_name = "hx-select"

class Hx_Select_Oob(HxAttribute):
    attribute_name = "hx-select-oob"

class Hx_Sse(HxAttribute):
    attribute_name = "hx-sse"

class Hx_Swap(HxAttribute):
    attribute_name = "hx-swap"

class Hx_Swap_Oob(HxAttribute):
    attribute_name = "hx-swap-oob"

class Hx_Sync(HxAttribute):
    attribute_name = "hx-sync"

class Hx_Target(HxAttribute):
    attribute_name = "hx-target"

class Hx_Trigger(HxAttribute):
    attribute_name = "hx-trigger"

class Hx_Vals(HxAttribute):
    attribute_name = "hx-vals"

