from komitas.demo.views import KomitasDemoPageBaseModel
from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.demo.views import *
from komitas.bootstrap.navbar import *
from komitas.application.spa import SinglePageApp

from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.demo.views.home import HomeView, HomeViewModel
from komitas.demo.views.todo import TodoView, TodoModel


class DemoSinglePageApp(SinglePageApp):
    base_html = KomitasDemoPageBase(
        KomitasDemoPageBaseModel(name="KomitasDemoHTMLBase")
    )
    nav_bar = CollapsibleNavbar(
        BootstrapNavbarModel(name="navbar", LogoText="Komitas Demo!")
    )
    views = [
        HomeView(HomeViewModel()),
        TodoView(TodoModel()),
    ]
