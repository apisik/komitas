from komitas.demo.app import DemoSinglePageApp
import subprocess
from starlette.applications import Starlette
from starlette.responses import Response
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware
import secrets

app = Starlette(
    # debug=True,
)
app.add_middleware(
    SessionMiddleware,
    secret_key=secrets.token_urlsafe(32),
    max_age=3600,
    same_site="lax",
    https_only=False,
)


@app.route("/")
def index(request: Request) -> Response:
    return Response(DemoSinglePageApp().render(request), media_type="text/html")
