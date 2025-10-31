from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.component import *
from komitas.demo.components import *
from komitas.bootstrap import *
from xml.etree import ElementTree as ET

import inspect


class ineractive_button(InteractiveComponent):
    def __init__(self):
        self.text = "Click Me!"
        self.id = "demo-button"

    def __call__(self, *args, **kwds):
        return Button(self.text).attrs(
            (Class, "btn btn-primary"),
            (Id, self.id),
            (Hx_Get, ""),
            (Hx_Swap, "outerHTML"),
            (Hx_Vals, f'{{"text": "{self.text}"}}'),
        )

    def update_state(self, text):
        text_options = [
            "Click Me!",
            "You Clicked Me!",
            "Click Again!",
            "Keep Clicking!",
            "You're Persistent!",
            "Alright, That's Enough!",
        ]

        current_index = text_options.index(text)
        next_index = (current_index + 1) % len(text_options)
        self.text = text_options[next_index]


class TwoColumnLayout(Component):
    def __init__(self, left: Component, right: Component):
        self.left = left
        self.right = right

    def __call__(self, *args, **kwds):
        return (
            Div()
            .attrs((Class, "container-fluid text-center"))
            .innrs(
                Div()
                .attrs((Class, "row"))
                .innrs(
                    Div().attrs((Class, "col-6")).innrs(self.left),
                    Div().attrs((Class, "col-6")).innrs(self.right),
                )
            )
        )


class LeftAlignedCodeBlock(Component):
    def __call__(self, code, *args, **kwds):
        return Pre().attrs((Class, "text-start")).innrs(Code().innrs(code))


class App:
    def render(self, request) -> str:
        # check if hx-request header is present
        if "HX-Request" in request.headers:
            query_params = request.query_params

            print(request.url)

            return self.index_partial(request.headers["HX-Target"], query_params)
        else:
            return self.index()

    def index(self) -> str:
        raise NotImplementedError

    def index_partial(self, target) -> str:
        raise NotImplementedError


class DemoApp(App):
    def __init__(self):
        self.html = KomitasDemoBasePage(
            innrs=[
                Div().innrs(
                    BootstrapHeader(BootstrapHeaderModel()),
                    # KomitasVision(),
                    # LeftAlignedCodeBlock()(inspect.getsource(Tag)),
                    # ineractive_button(),
                )
            ]
        )()

    def index(self) -> str:
        return ET.tostring(
            self.html.build(),
            encoding="unicode",
            method="html",
            short_empty_elements=False,
        )

    def index_partial(self, target, params) -> str:
        # get the element with the given id
        target = self.html.build().find(f".//*[@id='{target}']")
        target.obj.update_state(params)
        return ET.tostring(
            target.obj().build(), encoding="unicode", short_empty_elements=False
        )
