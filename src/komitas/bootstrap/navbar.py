from komitas.application.component import ComponentModel, InteractiveComponent
from komitas.application.component import View
from komitas.html.tags import *
from komitas.html.attributes import *


class NavbarModel(ComponentModel):
    views: list[InteractiveComponent]
    active_view: InteractiveComponent
    LogoText: str


class NavbarButton(InteractiveComponent):
    def __init__(self, model: NavbarModel, view: InteractiveComponent):
        self.model = model
        self.view = view

    def update_state(self, params):
        self.model.active_view = self.view

    def __call__(self):
        return (
            Li()
            .attrs(
                (Class, "nav-item"),
                (Hx_Get, ""),
                (Hx_Swap, "outerHTML"),
                (Hx_Target, f"#{self.view.label.lower()}-nav-link"),
                (Id, f"{self.view.label.lower()}-nav-link"),
            )
            .innrs(
                A(self.view.label).attrs(
                    (Href, "#"),
                    (
                        Class,
                        f"nav-link{' active' if self.view == self.model.active_view else ''}",
                    ),
                    *((Aria_Current, "page"),)
                    if self.view == self.model.active_view
                    else (),
                )
            )
        )


class Navbar(Component):
    def __init__(self, model: NavbarModel):
        self.model = model

    def update_state(self, params):
        if "active_view" in params:
            self.model.active_view = params["active_view"]

    def __call__(self):
        return (
            Div()
            .attrs(
                (Class, "container"),
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
                        *[NavbarButton(self.model, view) for view in self.model.views]
                    ),
                ),
            )
        )


class ViewContainer(InteractiveComponent):
    def __init__(self, model: NavbarModel):
        self.model = model

    def update_state(self, params):
        pass

    def __call__(self):
        return (
            Div()
            .attrs(
                (Id, "view-container"),
                (Class, "container mt-4"),
            )
            .innrs(self.model.active_view)
        )
