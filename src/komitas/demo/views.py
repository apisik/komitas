from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.demo.components import *
from komitas.bootstrap.navbar import *
from komitas.application.spa import SinglePageApp
from xml.etree import ElementTree as ET

from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.application.component import ComponentModel
import inspect
import sys
import gc


class DemoSinglePageApp(SinglePageApp):
    def __init__(self):
        self.base_html = KomitasDemoHTMLBase

        self.navbar_model = NavbarModel()
        self.AppBar = Navbar(self.navbar_model)

        self.html = None
        self.AciveView = None

        # self.build()
        # self.html.build()

    def get_refs(self, model_obj):
        refs = gc.get_referrers(model_obj)

        return refs

    def build(self):
        self.html = KomitasDemoHTMLBase(
            innrs=[
                Div().innrs(
                    self.AppBar,
                )
            ]
        )()

    def index(self) -> str:
        if self.html is None:
            self.build()

        return ET.tostring(
            self.html.build(),
            encoding="unicode",
            method="html",
            short_empty_elements=False,
        )

    def index_partial(self, target, params) -> str:
        self.build()

        # print("Building partial view for:", target)

        target = self.html.build().find(f".//*[@id='{target}']")

        target.obj.update_state(params)

        additional_html = ""

        for e in target.obj.model.registered_components:
            if e == target.obj:
                continue
            # e.update_state(params)
            t = e()
            # add hx-swap-oob attribute
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
