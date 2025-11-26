from komitas.application.component import AppBarModel, PageBaseModel, ViewModel
from komitas.demo.views import KomitasDemoPageBaseModel
from komitas.demo.views import KomitasDemoPageBase
from komitas.bootstrap.navbar import CollapsibleNavbar, BootstrapNavbarModel
from komitas.application.spa import SinglePageApp

from komitas.demo.views.home import HomeView, HomeViewModel
from komitas.demo.views.todo import TodoView, TodoModel


class DemoSinglePageApp(SinglePageApp):
    base_html = (
        KomitasDemoPageBase,
        PageBaseModel,
        KomitasDemoPageBaseModel,
    )
    nav_bar = (CollapsibleNavbar, AppBarModel, BootstrapNavbarModel)
    views = [
        (HomeView, ViewModel, HomeViewModel),
        (TodoView, ViewModel, TodoModel),
    ]
