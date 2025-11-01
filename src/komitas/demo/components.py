from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.components import *
from komitas.bootstrap import *
from komitas.demo import snippets
import inspect

from types import NoneType
from typing import Union


class KomitasDemoBasePage(Component):
    def __init__(
        self, title: Union[str, NoneType] = None, innrs: Union[Tag, NoneType] = None
    ):
        self.title = title
        self.innrs = innrs

    def __call__(self, *args, **kwds):
        return (
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
                    Title().innrs(
                        self.title if self.title is not None else "Komitas Demo"
                    ),
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
                    Script().attrs(
                        (
                            Src,
                            "http://127.0.0.1:35729/livereload.js?snipver=1",
                        ),
                    ),
                ),
                Body()
                .attrs((Data_Bs_Theme, "dark"))
                .innrs(
                    *self.innrs,
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
                    Script("hljs.highlightAll();"),
                ),
            )
        )


class Introduction(Component):
    def __call__(self, *args, **kwds):
        return (
            Div()
            .attrs((Class, "container-fluid d-flex flex-column"))
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
                    Div()
                    .attrs((Class, "mx-5 my-3"))
                    .innrs(
                        Hr(),
                        P()
                        .attrs(
                            (Class, "lead mx-3"),
                        )
                        .innrs(
                            "I'll think of something that goes here later :P",
                        ),
                        Hr(),
                    ),
                    P().innrs(
                        "This means in addition to being able to declare the structure ",
                        "of your HTML in pure python, Komitas also provides a way to declare ",
                        "interactivity.",
                    ),
                ),
            )
        )


class LeftAlignedCodeBlock(Component):
    def __call__(self, code, *args, **kwds):
        lang = "language-python" if ("<" != code.lstrip()[0]) else "language-html"

        # delete first line and 4 spaces from each line
        lines = code.split("\n")
        # delete first line
        lines = lines[1:]
        # if starts with < do nothing else remove 4 spaces
        code = "\n".join(
            line[4:] if lang == "language-python" else line for line in lines
        )

        return (
            Pre()
            .attrs((Class, "text-start"))
            .innrs(Code().attrs((Class, lang)).innrs(code))
        )


class KomitasVision(Component):
    def __call__(self, *args, **kwds):
        return (
            Div()
            .attrs(
                (Class, "container-fluid d-flex flex-column"),
            )
            .innrs(
                # BootstrapHeader(),
                H2().attrs((Class, "text-center mt-1")).innrs("HTML is Just XML"),
                Div()
                .attrs((Class, "text-start"))
                .innrs(
                    P().innrs(
                        "To build a DSL for HTML in python, we shouldn't ",
                        "try to reinvent the wheel. The ",
                        Code("xml").attrs((Class, "language-python")),
                        " module in the python standard library provides us with ",
                        "majority of the functionality we need to represent HTML. ",
                        "What I find lacking in the ",
                        Code("xml").attrs((Class, "language-python")),
                        " module is ergonomics.",
                    ),
                    LeftAlignedCodeBlock()(inspect.getsource(snippets.ExmapleCode)),
                    P("outputs"),
                    LeftAlignedCodeBlock()(snippets.ExmapleCode.output),
                    P().innrs(
                        "Using Komitas, we can express the same HTML structure ",
                        "in a more ergonomic way:",
                    ),
                    LeftAlignedCodeBlock()(inspect.getsource(snippets.ExampleCode2)),
                    P("outputs"),
                    LeftAlignedCodeBlock()(snippets.ExampleCode2.output),
                ),
            )
        )
