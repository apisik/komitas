from komitas.application.component import (
    ComponentModel,
    InteractiveComponent,
    View,
    AppBarButton,
)
from komitas.application.component import *
from komitas.html.tags import *
from komitas.html.attributes import *


class BootstrapNavbarModel(AppBarModel):
    LogoText: str = "Komitas"


class BootstrapNavbarButton(AppBar[BootstrapNavbarModel]):
    def __init__(self, model, model_extra, view: View):
        super().__init__(model, model_extra)
        self.view = view

    def update_state(self, params):
        self.model._active_view = self.view

    def __call__(self):
        return (
            Li()
            .attrs(
                (Class, "nav-item"),
                (Hx_Get, ""),
                (Hx_Swap, "outerHTML"),
                (
                    Hx_Target,
                    f"#{self.view.model_extras.name.replace(' ', '-').lower()}-nav-link",
                ),
                (
                    Id,
                    f"{self.view.model_extras.name.replace(' ', '-').lower()}-nav-link",
                ),
            )
            .innrs(
                A(self.view.model_extras.name).attrs(
                    (Href, "#"),
                    (
                        Class,
                        f"nav-link{' active' if self.view is self.model._active_view else ''}",
                    ),
                    *((Aria_Current, "page"),)
                    if self.view == self.model._active_view
                    else (),
                )
            )
        )


class CollapsibleNavbar(AppBar[BootstrapNavbarModel]):
    """
    Renders a Bootstrap collapsible navbar similar to the provided HTML.
    Use with a NavbarModel (or pass a model with .active_view if you need dynamic behaviour).
    """

    def __call__(self):
        return (
            Nav()
            .attrs((Class, "navbar navbar-expand-lg bg-body-tertiary"))
            .innrs(
                Div()
                .attrs((Class, "container"))
                .innrs(
                    A(self.model_extras.LogoText).attrs((Class, "navbar-brand")),
                    Button()
                    .attrs(
                        (Class, "navbar-toggler"),
                        (Type, "button"),
                        (Data_Bs_Toggle, "collapse"),
                        (Data_Bs_Target, "#navbarSupportedContent"),
                        (Aria_Controls, "navbarSupportedContent"),
                        (Aria_Expanded, "false"),
                        (Aria_Label, "Toggle navigation"),
                    )
                    .innrs(Span().attrs((Class, "navbar-toggler-icon"))),
                    Div()
                    .attrs(
                        (Class, "collapse navbar-collapse"),
                        (Id, "navbarSupportedContent"),
                    )
                    .innrs(
                        Ul()
                        .attrs((Class, "navbar-nav mb-2 mb-lg-0"))
                        .innrs(
                            *[
                                BootstrapNavbarButton(
                                    self.model, self.model_extras, view
                                )
                                for view in self.model._views
                            ]
                            # *[
                            #     Li()
                            #     .attrs(
                            #         (Class, "nav-item"),
                            #         (Hx_Get, ""),
                            #         (Hx_Swap, "outerHTML"),
                            #         (Hx_Target, f"#{view.name_safe()}-nav-link"),
                            #         (Id, f"{view.name_safe()}-nav-link"),
                            #     )
                            #     .innrs(
                            #         A(view.name()).attrs(
                            #             (Href, "#"),
                            #             (
                            #                 Class,
                            #                 f"nav-link{' active' if view == self.model.active_view else ''}",
                            #             ),
                            #             *((Aria_Current, "page"),)
                            #             if view == self.model.active_view
                            #             else (),
                            #         )
                            #     )
                            #     for view in self.model.views
                            # ]
                        ),
                        Div().attrs(
                            (Class, "me-auto"),
                        ),
                    ),
                ),
            )
        )
