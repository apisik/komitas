from sqlmodel import SQLModel
from pydantic import PrivateAttr


class Component[T, TX]:
    _class_registry = {}

    model: T
    model_extras: TX

    def __init__(self, model: type[T] | T, model_extras: type[TX] | TX) -> None:
        if isinstance(model, type):
            class_name = f"{self.__class__.__name__}_{model.__name__}"

            if class_name not in Component._class_registry:
                Component._class_registry[class_name] = type(class_name, (model,), {})

            self.model = Component._class_registry[class_name]()
        else:
            self.model = model

        if isinstance(model_extras, type):
            class_name = f"{self.__class__.__name__}_{model_extras.__name__}"

            if class_name not in Component._class_registry:
                Component._class_registry[class_name] = type(
                    class_name, (model_extras,), {}
                )

            self.model_extras = Component._class_registry[class_name]()
        else:
            self.model_extras = model_extras

        if isinstance(self.model, ComponentModel):
            self.model.register_component(self)
        if isinstance(self.model_extras, ComponentModel):
            self.model_extras.register_component(self)

    def name(self):
        return self.model.name

    def name_safe(self):
        return self.model.name.lower().replace(" ", "-")

    @classmethod
    def map(
        cls, model: type[T] | T, model_extras: type[TX] | TX
    ) -> list["Component[T, TX]"]:
        pass


class SingletonBase:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # print("Creating new instance of", cls.__name__)
            instance = super(SingletonBase, cls).__new__(cls)
            cls._instances[cls] = instance

        return cls._instances[cls]


class ComponentReference(SQLModel):
    _associated_components: list = PrivateAttr(default_factory=list)

    def register_component(self, component):
        self._associated_components.append(component)

    @property
    def registered_components(self):
        return self._associated_components


class ComponentModel(SingletonBase, ComponentReference):
    def __init__(self) -> None:
        if getattr(self, "_initialized", False):
            return

        print("Initializing instance of", self.__class__.__name__)
        super().__init__()

        self._initialized = True
