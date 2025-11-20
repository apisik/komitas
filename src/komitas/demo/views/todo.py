from komitas.html.attributes import *
from komitas.html.tags import *
from komitas.application.component import View, ViewModel


class TodoModel(ViewModel):
    name: str = "To Do"


class TodoView(View):
    def __init__(self, model: TodoModel):
        self.model = model
        self.label = "Todo"

    def __call__(self):
        return (
            Div()
            .attrs((Class, "container mt-4"))
            .innrs(H2("Todo View"), P("This is a simple Todo view."))
        )
