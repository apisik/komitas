from komitas.html.attributes import *
from komitas.html.tags import *
from komitas.application.component import ComponentModel, View, ViewModel


class HomeViewModel(ViewModel):
    name: str = "Home"


class HomeView(View):
    def tag(self) -> Tag:
        return Div().innrs(
            H2("Home View"),
            P().innrs(
                """
                Welcome to the Home view of the Komitas demo application.
                This is a simple demonstration of a single-page application using Komitas.
                """,
            ),
            P().innrs(
                "Made with ❤️ by ",
                A("Avo Pisikyan").attrs((Href, "https://avop.me")),
            ),
        )
