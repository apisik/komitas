from komitas.html.attributes import *
from komitas.html.tags import *
from komitas.application.component import View, ViewModel


class TodoModel(ViewModel):
    name: str = "To Do"


class TodoView(View[TodoModel]):
    def tag(self) -> Tag:
        return (
            Div()
            .attrs((Class, "container mt-4"), (Name, self.model_extras.name))
            .innrs(H2("Todo View"), P("This is a simple Todo view."))
        )
