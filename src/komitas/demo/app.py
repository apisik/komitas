from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.demo.views import *
from komitas.bootstrap.navbar import *
from komitas.application.spa import SinglePageApp
from xml.etree import ElementTree as ET

from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.demo.views.home import HomeView, HomeViewModel
from komitas.demo.views.todo import TodoView, TodoModel


class DemoSinglePageApp(SinglePageApp):
    base_html = KomitasDemoPageBase()
    # def __init__(self):
    #     self.base_html = KomitasDemoHTMLBase
    #     self.views = [
    #         HomeView(HomeViewModel()),
    #         TodoView(TodoModel()),
    #     ]
    #
    #     self.navbar_model = BootstrapNavbarModel(
    #         name="navbar",
    #         LogoText="Komitas Demo!",
    #         views=self.views,
    #         active_view=self.views[0],
    #     )
    #     self.AppBar = CollapsibleNavbar(self.navbar_model)
    #
    #     self.html = None
    #     self.ActiveView = None
    #
    #     # self.build()
    #     # self.html.build()
    #     super().__init__()
    #
    # def build(self):
    #     self.html = KomitasDemoHTMLBase(
    #         title="Komitas Demo Application",
    #         innrs=[self.AppBar, ViewContainer(self.navbar_model)],
    #     )()
    #
    # def index(self) -> str:
    #     if self.html is None:
    #         self.build()
    #
    #     return ET.tostring(
    #         self.html.build(),
    #         encoding="unicode",
    #         method="html",
    #         short_empty_elements=False,
    #     )
    #
    # def index_partial(self, target, params) -> str:
    #     self.build()
    #
    #     # print("Building partial view for:", target)
    #
    #     target = self.html.build().find(f".//*[@id='{target}']")
    #
    #     target.obj.update_state(params)
    #
    #     additional_html = ""
    #
    #     for e in target.obj.model.registered_components:
    #         if e == target.obj:
    #             continue
    #         t = e()
    #         t.attrs((Hx_Swap_Oob, "true"))
    #         additional_html += ET.tostring(
    #             t.build(), encoding="unicode", short_empty_elements=False
    #         )
    #
    #     s1 = (
    #         ET.tostring(
    #             target.obj().build(), encoding="unicode", short_empty_elements=False
    #         )
    #         + additional_html
    #     )
    #
    #     return s1
