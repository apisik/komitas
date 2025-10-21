from komitas.html.tags import *
from komitas.html.attributes import *

from xml.etree import ElementTree as ET


class ineractive_button(InteractiveComponent):
    def __init__(self):
        self.text = "Click Me!"

    def __call__(self, *args, **kwds):
        return Button(self.text).attrs(
            (Class, "btn btn-primary mx-auto d-block mt-4"),
            (Id, "demo-button"),
            (Hx_Get, ""),
            (Hx_Swap, "outerHTML"),
        )
    
    def update_state(self):
        text_options = [
            "Click Me!",
            "You Clicked Me!",
            "Click Again!",
            "Keep Clicking!",
            "You're Persistent!",
            "Alright, That's Enough!",
        ]

        current_index = text_options.index(self.text)
        next_index = (current_index + 1) % len(text_options)
        self.text = text_options[next_index]




ibutton = ineractive_button()


body = (
    Div()
    .attrs((Class, "container"))
    .innrs(
        H1("Demo Page").attrs((Class, "text-center mt-5")),
        P("This is a simple demo page that showcases functionality!").attrs(
            (Class, "lead text-center")
        ),
        ibutton(),
    )
)


class View:
    def render(self, request) -> str:
        # check if hx-request header is present
        if "HX-Request" in request.headers:
            return self.index_partial(request.headers["HX-Target"])
        else:
            return self.index()

    def index(self) -> str:
        raise NotImplementedError

    def index_partial(self, target) -> str:
        raise NotImplementedError


class DemoView(View):

    def set_html(self):
        self.html = (
            HTML()
            .attrs(
                (Lang, "en"),
            )
            .innrs(
                Head().innrs(
                    Meta().attrs((Charset, "UTF-8")),
                    Meta().attrs(
                        (Name, "viewport"),
                        (Content, "width=device-width, initial-scale=1.0"),
                    ),
                    Title("Bootstrap Demo"),
                    Link().attrs(
                        (
                            Href,
                            "https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css",
                        ),
                        (Rel, "stylesheet"),
                        (
                            Integrity,
                            "sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB",
                        ),
                        (Crossorigin, "anonymous"),
                    ),
                    Script().attrs(
                        (
                            Src,
                            "https://cdn.jsdelivr.net/npm/htmx.org@2.0.7/dist/htmx.min.js",
                        ),
                    ),
                ),
                Body().innrs(
                    body,
                    Script().attrs(
                        (
                            Src,
                            "https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js",
                        ),
                        (
                            Integrity,
                            "sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI",
                        ),
                        (Crossorigin, "anonymous"),
                    ),
                ),
            )
        )

    def index(self) -> str:
        self.set_html()
        return ET.tostring(self.html, encoding="unicode", short_empty_elements=False)

    def index_partial(self, target) -> str:
        # get the element with the given id
        self.set_html()
        target = self.html.find(f".//*[@id='{target}']")



        ibutton.update_state()
        self.set_html()
        return ET.tostring(ibutton(), encoding="unicode", short_empty_elements=False)
