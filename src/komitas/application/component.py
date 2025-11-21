from sqlmodel import SQLModel
from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema
from typing import Generic, TypeVar, Union
import komitas.html.tags as tg
import komitas.html.attributes as at
from types import NoneType


class ComponentModel(SQLModel):
    registered_components: list["Component"] = []
    name: str

    def register_component(self, component: "Component"):
        self.registered_components.append(component)


TComponentModel = TypeVar("TComponentModel", bound=ComponentModel)


class Component(Generic[TComponentModel]):
    """
    This is the base class that we extend from to define components.
    """

    def __init__(self, model: TComponentModel) -> None:
        self.model: TComponentModel = model

    def __call__(self) -> tg.Tag:
        return self.tag()

    def tag(self) -> tg.Tag:
        return tg.Div(tg.P(f"Hello, {self.__class__.__name__}"))

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.is_instance_schema(cls)


class PageBaseModel(ComponentModel):
    pass


class PageBase(Component[PageBaseModel]):
    title: str = "Base Page Title"
    innrs: list[Union[Component, tg.Tag]] = []

    def __init__(self, *args) -> None:
        self.nav_bar: Union["AppBar", tg.Tag] = tg.Div()
        super().__init__(*args)

    def tag(self) -> tg.Tag:
        return tg.Div(tg.H1(self.title), *self.innrs)


class InteractiveComponent(Component, Generic[TComponentModel]):
    """
    We subclass component and add the funcitonality for updating state.
    """

    def __init__(self, model: TComponentModel) -> None:
        self.model: TComponentModel = model

    def update_state(self, params):
        raise NotImplementedError

    def name(self):
        return self.model.name

    def name_safe(self):
        return self.model.name.lower().replace(" ", "-")


class ViewModel(ComponentModel):
    name: str


class View(InteractiveComponent[ViewModel]):
    pass


class AppBarModel(ComponentModel):
    active_view: Union[View, NoneType] = None
    views: set[View] = set()


class AppBar(InteractiveComponent[AppBarModel]):
    def register_views(self, *args: View):
        if not self.model.active_view:
            self.model.active_view = args[0]
        self.model.views.update(args)


class ViewContainer(InteractiveComponent[AppBarModel]):
    def update_state(self, params):
        pass

    def __call__(self):
        return (
            tg.Div()
            .attrs(
                (at.Id, "view-container"),
            )
            .innrs(self.model.active_view)
        )
