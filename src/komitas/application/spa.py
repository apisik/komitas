"""
A single page application is the core unit of a Komitas web application.
A grouping of single paage applications can be composed into a full web application.

A single page app consists of a number of components:
    1) An AppBar
    2) A set of views
    3) A base HTML structure
"""

from komitas.application.state import State
from komitas.application.component import Component
import inspect
import xml.etree.ElementTree as ET
from komitas.html.tags import Tag


class SinglePageAppState(State):
    pass


class SinglePageApp:
    base_html: Component

    def render(self, request) -> str:
        # check if hx-request header is present
        if "HX-Request" in request.headers:
            query_params = request.query_params
            r = self.index_partial(query_params)
        else:
            r = self.index()

        return ET.tostring(r, encoding="unicode", short_empty_elements=False)

    def index(self) -> Tag:
        return self.base_html.tag().build()

    def index_partial(self, target) -> Tag:
        raise NotImplementedError

    @classmethod
    def get_class_file(cls) -> str:
        return inspect.getfile(cls)
