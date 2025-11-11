from pydantic import BaseModel, ConfigDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from komitas.html.tags import Tag


class Component:
    pass


class InteractiveComponent(Component):
    def update_state(self, params):
        raise NotImplementedError

    def __call__(self) -> Tag:
        raise NotImplementedError


class ComponentModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    registered_components: list[Component] = []

    def register_component(self, component: Component):
        self.registered_components.append(component)


class AppBar:
    pass


class View:
    pass
