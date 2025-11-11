from komitas.html.attributes import *
from komitas.html.tags import *
from komitas.application.component import ComponentModel, InteractiveComponent


class HomeModel(ComponentModel):
    pass


class HomeView(InteractiveComponent):
    def __init__(self, model: HomeModel):
        self.model = model
        self.label = "Home"

    def __call__(self):
        return Div().innrs(
            H2("Home View"),
            P("Welcome to the Home view of the Komitas demo application."),
        )
