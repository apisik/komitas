class SinglePageApp:
    def render(self, request) -> str:
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
