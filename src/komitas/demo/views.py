from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.demo.components import *
from komitas.bootstrap.base import *
from komitas.application.spa import SinglePageApp
from xml.etree import ElementTree as ET

from komitas.html.tags import *
from komitas.html.attributes import *


class IntroducitonPage(Component):
    def __call__(self):
        return (
            Div()
            .attrs((Class, "container mt-4"), (Id, "view"))
            .innrs(
                H1("Welcome to Komitas"),
                P(
                    "Komitas is a modern web framework designed to simplify the "
                    "process of building interactive web applications using "
                    "component-based architecture."
                ),
                H2("Getting Started"),
                P(
                    "To get started with Komitas, check out the documentation "
                    "and explore the various components and features available."
                ),
            )
        )


class MotivationPage(Component):
    def __call__(self):
        return (
            Div()
            .attrs(
                (Class, "container mt-4"),
                (Id, "view"),
                (Hx_Swap_Oob, "true"),
            )
            .innrs(
                H1("Motivation"),
                P(
                    "The motivation behind Komitas is to provide developers with "
                    "a powerful yet easy-to-use framework that leverages Python's "
                    "capabilities for web development."
                ),
                P(
                    "By focusing on components, Komitas allows for reusable and "
                    "maintainable code, making it easier to build complex UIs."
                ),
            )
        )


class DemoSinglePageApp(SinglePageApp):
    def __init__(self):
        self.base_html = KomitasDemoHTMLBase

        self.AppBar = BootstrapHeader(BootstrapHeaderModel())
        self.Views = [
            IntroducitonPage(),
            MotivationPage(),
            # PrinciplesPage(),
            # ComponentsPage(),
        ]

        self.html = None
        self.AciveView = None

    def build(self):
        self.AciveView = self.Views[0]

        self.html = KomitasDemoHTMLBase(
            innrs=[
                Div().innrs(
                    self.AppBar,
                    self.AciveView,
                    # KomitasVision(),
                    # LeftAlignedCodeBlock()(inspect.getsource(Tag)),
                    # ineractive_button(),
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

        # get the element with the given id
        target = self.html.build().find(f".//*[@id='{target}']")

        oob = target.obj.update_state(params)

        if oob is not None:
            # find the element with the given id

            oob_target = self.html.find(f".//*[@id='{oob}']")

            # oob_html = ET.tostring(oob_target, encoding="unicode", short_empty_elements=False)

            print("OOB HTML:", oob_target)

        s1 = ET.tostring(
            target.obj().build(), encoding="unicode", short_empty_elements=False
        )

        s2 = self.Views[1]
        s2 = ET.tostring(s2().build(), encoding="unicode", short_empty_elements=False)

        return s1 + s2
