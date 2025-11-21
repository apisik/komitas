"""
A single page application is the core unit of a Komitas web application.
A grouping of single paage applications can be composed into a full web application.

A single page app consists of a number of components:
    1) An AppBar
    2) A set of views
    3) A base HTML structure
"""

from komitas.application.state import State
from komitas.application.component import AppBar, PageBase
from komitas.html.attributes import Hx_Swap_Oob
import inspect
import xml.etree.ElementTree as ET
from komitas.html.tags import Tag
from komitas.application.component import View


class SinglePageAppState(State):
    pass


class SinglePageApp:
    base_html: PageBase
    nav_bar: AppBar
    views: list[View]

    def __init__(self) -> None:
        self.nav_bar.register_views(*self.views)
        self.base_html.nav_bar = self.nav_bar

    def render(self, request) -> str:
        # check if hx-request header is present
        if "HX-Request" in request.headers:
            trigger_id = request.headers["Hx-Trigger"]
            query_parameters = request.query_params
            r = self.index_partial(trigger_id, query_parameters)
            return r
        else:
            r = self.index()

            return ET.tostring(r, encoding="unicode", short_empty_elements=False)

    def index(self) -> Tag:
        return self.base_html.tag().build()

    def index_partial(self, trigger_id, query_parameters) -> Tag:
        html = self.base_html.tag().build()
        target = html.find(f".//*[@id='{trigger_id}']")

        target.obj.update_state(query_parameters)

        additional_html = ""

        for e in target.obj.model.registered_components:
            if e == target.obj:
                continue
            t = e()
            t.attrs((Hx_Swap_Oob, "true"))
            additional_html += ET.tostring(
                t.build(), encoding="unicode", short_empty_elements=False
            )

        s1 = (
            ET.tostring(
                target.obj().build(), encoding="unicode", short_empty_elements=False
            )
            + additional_html
        )

        return s1

    @classmethod
    def get_class_file(cls) -> str:
        return inspect.getfile(cls)
