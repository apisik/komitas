from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.demo.components import *
from komitas.bootstrap.navbar import *
from komitas.application.spa import SinglePageApp
from xml.etree import ElementTree as ET

from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.demo.views.home import HomeView, HomeModel
from komitas.demo.views.todo import TodoView, TodoModel


class DemoSinglePageApp(SinglePageApp):
    def __init__(self):
        self.base_html = KomitasDemoHTMLBase
        self.views = [
            HomeView(HomeModel()),
            TodoView(TodoModel()),
        ]

        self.navbar_model = NavbarModel(
            LogoText="Komitas Demo Application",
            views=self.views,
            active_view=self.views[0],
        )
        self.AppBar = Navbar(self.navbar_model)

        self.html = None
        self.ActiveView = None

        # self.build()
        # self.html.build()

    def build(self):
        self.html = KomitasDemoHTMLBase(
            innrs=[Div().innrs(self.AppBar, ViewContainer(self.navbar_model))]
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
