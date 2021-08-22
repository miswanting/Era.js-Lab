from threading import Thread

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from uvicorn import run


def server():
    app = FastAPI()
    @app.get('{file_path:path}')
    def root(file_path):
        with open('erajs/dist/index.html') as html:
            return HTMLResponse(html.read())
    run(app, log_level='warning')


def start():
    t = Thread(target=server)
    t.start()
