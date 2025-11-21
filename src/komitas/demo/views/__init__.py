from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.bootstrap.base import *
from komitas.application.component import *


class KomitasDemoPageBaseModel(PageBaseModel):
    pass


class KomitasDemoPageBase(PageBase):
    title = "Komitas Demo!"

    def tag(self):
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
                    Title().innrs(self.title),
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
                    self.nav_bar,
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


__all__ = ["KomitasDemoPageBase"]
