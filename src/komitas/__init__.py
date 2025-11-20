from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.demo.app import DemoSinglePageApp
import subprocess
from starlette.applications import Starlette
from starlette.responses import Response
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware
from livereload import Server
import secrets

app = Starlette(
    debug=True,
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


def run() -> None:
    subprocess.Popen(
        ["uvicorn", "--host", "0.0.0.0", "komitas:app", "--reload"],
        # stdout=subprocess.PIPE,
        # stderr=subprocess.PIPE,
    )


def main() -> None:
    run()

    server = Server()
    server.watch("src/", delay=1)
    server.serve(port=35729, host="127.0.0.1")
