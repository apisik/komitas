from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.component import *

from xml.etree import ElementTree as ET

import inspect


class ineractive_button(InteractiveComponent):
    def __init__(self):
        self.text = "Click Me!"
        self.id = "demo-button"

    def __call__(self, *args, **kwds):
        return Button(self.text).attrs(
            (Class, "btn btn-primary mx-auto d-block mt-4"),
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


class Introduction(Component):
    def __init__(self):
        super().__init__()

    def __call__(self, *args, **kwds):
        return (
            Div()
            .attrs((Class, "container d-flex flex-column"))
            .innrs(
                H1().attrs((Class, "text-center mt-5")).innrs("Komitas"),
                P()
                .attrs((Class, "text-center"))
                .innrs(
                    "An ",
                    Span(Strong("expirimental")).attrs(
                        (Class, "text-decoration-underline fst-italic")
                    ),
                    " framework for building web applications in Python",
                ),
                P()
                .innrs(
                    "The current prevalent idea behind a lot of python web frameworks is to use ",
                    "templates to generate HTML server side. Komitas takes a different approach: ",
                    "in Komitas, HTML elements are represented as Python objects, allowing you to build ",
                    "your entire web application using pure Python code.",
                )
                .attrs((Class, "text-center")),
                Pre()
                .innrs(
                    Code(inspect.getsource(Introduction)).attrs(
                        (Class, "language-python")
                    )
                )
                .attrs((Class, "my-4 mx-auto")),
                ineractive_button(),
            )
        )


class View:
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


class DemoView(View):
    def __init__(self):
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
                    Link().attrs(
                        (
                            Href,
                            "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/an-old-hope.min.css",
                        ),
                        (Rel, "stylesheet"),
                    ),
                    Script().attrs(
                        (
                            Src,
                            "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/highlight.min.js",
                        ),
                    ),
                    # Script().attrs(
                    #     (
                    #         Src,
                    #         "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/languages/python.min.js",
                    #     ),
                    # ),
                ),
                Body()
                .attrs((Class, "bg-dark text-white vh-100"))
                .innrs(
                    Introduction(),
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
                    # Script("hljs.registerLanguage('python', window.hljsDefinePython);"),
                    Script("hljs.highlightAll();"),
                ),
            )
        )

    def index(self) -> str:
        return ET.tostring(
            self.html.build(), encoding="unicode", short_empty_elements=False
        )

    def index_partial(self, target, params) -> str:
        # get the element with the given id
        target = self.html.build().find(f".//*[@id='{target}']")
        target.obj.update_state(params.get("text", "Click Me!"))
        return ET.tostring(target.obj(), encoding="unicode", short_empty_elements=False)
