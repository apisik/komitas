from komitas.html.tags import *
from komitas.html.attributes import *
from komitas.demo.views import DemoView
from xml.etree import ElementTree as ET
import uvicorn
import subprocess
from starlette.applications import Starlette
from starlette.responses import Response
from livereload import Server

app = Starlette(debug=True)


@app.route("/")
def index(request) -> str:
    return Response(DemoView().render(request), media_type="text/html")


def main() -> None:
    
    subprocess.run(["uvicorn", "komitas:app", "--reload"])

def rserver() -> None:
    server = Server(app)
    server.watch("src/", delay=5)
    server.serve(port=35729, host="127.0.0.1", root="*")
