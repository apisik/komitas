from komitas.application.component import ComponentModel, InteractiveComponent
from komitas.application.component import View


class ViewState(ComponentModel):
    active_view: View
    available_views: list[View]


class NavbarButton(InteractiveComponent):
    def __init__(self, id: str, state: ViewState):
        self.id = id
        self.state = state
