"""
A single page application is the core unit of a Komitas web application.
A grouping of single paage applications can be composed into a full web application.

A single page app consists of a number of components:
    1) An AppBar
    2) A set of views
    3) A base HTML structure
"""

from komitas.application.state import State

import inspect


class SinglePageAppState(State):
    pass


class SinglePageApp:
    def __init__(self):
        print(self.get_class_file())

    def render(self, request) -> str:
        # print session id
        session_id = request.session.get("count", 0)
        session_id += 1
        request.session["count"] = session_id
        print(f"Session ID: {session_id}")
        # check if hx-request header is present
        if "HX-Request" in request.headers:
            query_params = request.query_params
            return self.index_partial(request.headers["HX-Trigger"], query_params)
        else:
            return self.index()

    def index(self) -> str:
        raise NotImplementedError

    def index_partial(self, target) -> str:
        raise NotImplementedError

    @classmethod
    def get_class_file(cls) -> str:
        return inspect.getfile(cls)

