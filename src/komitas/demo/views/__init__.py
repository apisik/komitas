from komitas.application.base_component import ComponentModel
from komitas.bootstrap import navbar
import komitas.html.tags as tg
import komitas.html.attributes as at
import komitas.application.component as cmp


class KomitasDemoPageBaseModel(ComponentModel):
    pass


class KomitasDemoPageBase(cmp.PageBase[KomitasDemoPageBaseModel]):
    def tag(self):
        return (
            tg.HTML()
            .attrs(
                (at.Lang, "en"),
            )
            .innrs(
                tg.Head().innrs(
                    tg.Meta().attrs((at.Charset, "UTF-8")),
                    tg.Meta().attrs(
                        (at.Name, "viewport"),
                        (at.Content, "width=device-width, initial-scale=1.0"),
                    ),
                    tg.Title().innrs(self.model.title),
                    tg.Link().attrs(
                        (
                            at.Href,
                            "https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css",
                        ),
                        (at.Rel, "stylesheet"),
                        (
                            at.Integrity,
                            "sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB",
                        ),
                        (at.Crossorigin, "anonymous"),
                    ),
                    tg.Script().attrs(
                        (
                            at.Src,
                            "https://cdn.jsdelivr.net/npm/htmx.org@2.0.7/dist/htmx.min.js",
                        ),
                    ),
                ),
                tg.Body()
                .attrs((at.Data_Bs_Theme, "dark"))
                .innrs(
                    self.model._nav_bar if self.model._nav_bar is not None else "",
                    *self.model._innrs,
                    tg.Script().attrs(
                        (
                            at.Src,
                            "https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js",
                        ),
                        (
                            at.Integrity,
                            "sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI",
                        ),
                        (at.Crossorigin, "anonymous"),
                    ),
                    tg.Script("hljs.highlightAll();"),
                ),
            )
        )


__all__ = ["KomitasDemoPageBase"]
