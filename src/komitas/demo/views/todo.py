from komitas.html.attributes import *
from komitas.html.tags import *
from komitas.application.component import ComponentModel, InteractiveComponent


class TodoModel(ComponentModel):
    pass


class TodoView(InteractiveComponent):
    def __init__(self, model: TodoModel):
        self.model = model
        self.label = "Todo"

    def __call__(self):
        return Div().innrs(H2("Todo View"), P("This is a simple Todo view."))
