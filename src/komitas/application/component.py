from sqlmodel import SQLModel
from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema
from typing import Generic, TypeVar
import komitas.html.tags as tg
import komitas.html.attributes as at


class Component:
    """
    This is the base class that we extend from to define components.
    """

    def __call__(self) -> tg.Tag:
        return self.tag()

    def tag(self) -> tg.Tag:
        return tg.Div(tg.P(f"Hello, {self.__class__.__name__}"))

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.is_instance_schema(cls)


class ComponentModel(SQLModel):
    registered_components: list[Component] = []
    name: str

    def register_component(self, component: Component):
        self.registered_components.append(component)


TComponentModel = TypeVar("TComponentModel", bound=ComponentModel)


class InteractiveComponent(Component, Generic[TComponentModel]):
    """
    We subclass component and add the funcitonality for updating state.
    """

    def __init__(self, model: TComponentModel):
        self.model: TComponentModel = model

    def update_state(self, params):
        raise NotImplementedError

    def name(self):
        return self.model.name

    def name_safe(self):
        return self.model.name.lower().replace(" ", "-")


class ViewModel(ComponentModel):
    pass


class View(InteractiveComponent):
    pass


class AppBarModel(ComponentModel):
    active_view: View


class AppBar(InteractiveComponent):
    pass


class ViewContainer(InteractiveComponent):
    def __init__(self, model: AppBarModel):
        self.model: AppBarModel = model

    def update_state(self, params):
        pass

    def __call__(self):
        return (
            tg.Div()
            .attrs(
                (at.Id, "view-container"),
                (at.Class, "container mt-4"),
            )
            .innrs(self.model.active_view)
        )
