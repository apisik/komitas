from __future__ import annotations

from .base import Attribute, AttributeMeta
from . import aria as _aria  # noqa: E402
from . import global_attrs as _global_attrs  # noqa: E402
from . import htmx as _htmx  # noqa: E402
from . import specific as _specific  # noqa: E402

from .aria import *  # noqa: F401,F403,E402
from .global_attrs import *  # noqa: F401,F403,E402
from .htmx import *  # noqa: F401,F403,E402
from .specific import *  # noqa: F401,F403,E402

__all__ = [
    "AttributeMeta",
    "Attribute",
    "get_tag_attribute_mixins",
] + _global_attrs.__all__ + _aria.__all__ + _htmx.__all__ + _specific.__all__

get_tag_attribute_mixins = _specific.get_tag_attribute_mixins
