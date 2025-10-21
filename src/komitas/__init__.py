from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.demo.views import DemoView
from xml.etree import ElementTree as ET
import uvicorn
import subprocess
from starlette.applications import Starlette
from starlette.responses import Response

app = Starlette()


@app.route("/")
def index(request) -> str:
    return Response(DemoView().render(request), media_type="text/html")


def main() -> None:
    subprocess.run(["uvicorn", "komitas:app", "--reload"])
