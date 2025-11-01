from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.demo.views import DemoSinglePageApp
from xml.etree import ElementTree as ET
import uvicorn
import subprocess
from starlette.applications import Starlette
from starlette.responses import Response
from livereload import Server
import threading

app = Starlette()


@app.route("/")
def index(request) -> str:
    return Response(DemoSinglePageApp().render(request), media_type="text/html")


def run() -> None:
    subprocess.Popen(
        ["uvicorn", "komitas:app", "--reload"],
        # stdout=subprocess.PIPE,
        # stderr=subprocess.PIPE,
    )


def main() -> None:
    run()

    server = Server()
    server.watch("src/", delay=1)
    server.serve(port=35729, host="127.0.0.1")
