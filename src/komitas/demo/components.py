from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.component import *

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
                ),
                Body()
                .attrs((Class, "bg-dark text-white vh-100"))
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
