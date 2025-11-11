from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.demo.app import DemoSinglePageApp
from xml.etree import ElementTree as ET
import uvicorn
import subprocess
from starlette.applications import Starlette
from starlette.responses import Response
from starlette.requests import Request
from livereload import Server
import threading

app = Starlette()


@app.route("/")
def index(request: Request) -> str:
    # for k, v in request.headers.items():
    #     if k.lower().startswith("hx-"):
    #         print(f"{k}: {v}")

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
