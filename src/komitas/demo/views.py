from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.component import *
from komitas.demo.components import *
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
                Div()
                .attrs(
                    (Class, "text-start"),
                )
                .innrs(
                    P().innrs(
                        "The current prevalent idea behind a lot of python web frameworks is to use ",
                        "templates to generate HTML server side. ",
                        "There are some attempts to challenge this templating paradigm using ",
                        "Domain Specific Languages (DSLs) which allow you to express HTML in pure python, ",
                        "but I always felt these framework fall short in their value proposition. ",
                        "If I have to learn a new DSL to use a framework and still have to deal with a lot of the ",
                        "same overhead as traditional frameworks, why not just use templates directly? ",
                    ),
                    P("Two prominent value propositions are: "),
                    DD().innrs(
                        DT().innrs("1. Component Architecture"),
                        DD().innrs(
                            "This is nice, but its possible to do something similar ",
                            "with templates using partial templates and includes. ",
                            "Although not as elegant, it does get the job done.",
                        ),
                        DT().innrs("2. First Class HTMX Support"),
                        DD().innrs(
                            "Again, nice, but the first class support implemented doesnt solve ",
                            "one of the biggest problems I have with HTMX. ",
                            "Which is the need for unique endpoints for every interactive component. ",
                            "This means that for every button, form, or other interactive element ",
                            "you generally create separate endpoint to handle its requests. ",
                        ),
                    ),
                    Hr(),
                    H6("The idea motivating Komitas is..."),
                    P().attrs(
                        (Class, "lead"),
                    ).innrs(
                        "A properly deigned DSL, should be able to express what ",
                        "we want and it should simply work. I draw a lot of inspiration from FastAPI's ",
                        "auto documenetation. Zero cost and it just works. ",
                        "Komitas aims to have a similar zero cost integration with HTMX. ",
                    ),
                    Hr(),
                ),
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
        self.html = KomitasDemoBasePage(
            innrs=[
                Introduction(),
            ]
        )()

    def index(self) -> str:
        return ET.tostring(
            self.html.build(), encoding="unicode", short_empty_elements=False
        )

    def index_partial(self, target, params) -> str:
        # get the element with the given id
        target = self.html.build().find(f".//*[@id='{target}']")
        target.obj.update_state(params.get("text", "Click Me!"))
        return ET.tostring(target.obj(), encoding="unicode", short_empty_elements=False)
