"""
A single page application is the core unit of a Komitas web application.
A grouping of single paage applications can be composed into a full web application.

A single page app consists of a number of components:
    1) An AppBar
    2) A set of views
    3) A base HTML structure
"""

from komitas.application.base_component import Component
from komitas.application.state import State
from komitas.application.component import (
    AppBar,
    PageBase,
    PageBaseModel,
    AppBarModel,
    ComponentModel,
    ViewModel,
)
from komitas.html.attributes import Hx_Swap_Oob
import inspect
import xml.etree.ElementTree as ET
from komitas.html.tags import Tag
from komitas.application.component import View


class SinglePageAppState(State):
    pass


class SinglePageApp:
    base_html: tuple[type[PageBase], type[PageBaseModel], type[ComponentModel]]
    nav_bar: tuple[type[AppBar], type[AppBarModel], type[ComponentModel]]
    views: list[tuple[type[View], type[ViewModel], type[ComponentModel]]]

    def __init__(self) -> None:
        self._views = [x(y, z) for x, y, z in self.views]
        nb, nbm, nbd = self.nav_bar

        nmodels = nbm()
        nmodels._views = self._views
        nmodels._active_view = self._views[0]

        self._nav_bar = nb(nmodels, nbd)

        bh, bhm, bhd = self.base_html
        model = bhm()
        model._nav_bar = self._nav_bar
        self._base_html = bh(model, bhd)

        print(len(self._nav_bar.model._associated_components))
        print(self._nav_bar.model._associated_components)

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
        return self._base_html.tag().build()

    def index_partial(self, trigger_id, query_parameters) -> str:
        html = self._base_html.tag().build()
        target = html.find(f".//*[@id='{trigger_id}']")

        if target is None:
            raise ValueError("Target should not be None!")
        if target.obj is None:
            raise ValueError("Target.obj should not be None!")
        #
        # from xml.etree.ElementTree import Element
        #
        # if isinstance(target, Element):
        #     raise TypeError("Target should be of type Element")

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
