from komitas.html.attributes import *
from komitas.html.tags import *
from komitas.components import *

from pydantic import BaseModel


class BootstrapHeaderModel(BaseModel):
    id: str = "bootstrap-header"
    LogoText: str = "Komitas"
    Pages: list[str] = ["About", "Motivation", "Principles", "Components"]


class BootstrapHeader(InteractiveComponent):
    def __init__(self, model: BootstrapHeaderModel):
        self.model = model
        self.active_page = self.model.Pages[0]
        self.id = self.model.id

    def update_state(self, params):
        if "active_page" in params:
            self.active_page = params["active_page"]

    def __call__(self):
        return (
            Div()
            .attrs(
                (Class, "container"),
                (Id, self.id),
            )
            .innrs(
                Header()
                .attrs(
                    (
                        Class,
                        "d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom",
                    )
                )
                .innrs(
                    A()
                    .attrs(
                        (Href, "/"),
                        (
                            Class,
                            "d-flex align-items-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none",
                        ),
                    )
                    .innrs(
                        Span(self.model.LogoText).attrs((Class, "fs-4")),
                    ),
                    Ul()
                    .attrs((Class, "nav nav-pills"))
                    .innrs(
                        *[
                            Li()
                            .attrs((Class, "nav-item"))
                            .innrs(
                                A(page).attrs(
                                    (Href, "#"),
                                    (
                                        Class,
                                        f"nav-link{' active' if page == self.active_page else ''}",
                                    ),
                                    *((Aria_Current, "page"),)
                                    if page == self.active_page
                                    else (),
                                    (Hx_Get, ""),
                                    (Hx_Swap, "outerHTML"),
                                    (Hx_Target, f"#{self.id}"),
                                    (Hx_Vals, f'{{"active_page": "{page}"}}'),
                                )
                            )
                            for page in self.model.Pages
                        ],
                    ),
                )
            )
        )
