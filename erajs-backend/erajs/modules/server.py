from os.path import exists, splitext
from threading import Thread

from fastapi import FastAPI, Response, WebSocket
from fastapi.responses import HTMLResponse
from uvicorn import run

mime = {
    '.html': 'text/html',
    '.js': 'text/javascript',
    '.css': 'text/css',
    '.ttf': 'font/ttf',
    '.woff': 'font/woff',
    '.woff2': 'font/woff2',
}


def server():
    app = FastAPI()

    @app.websocket('/ws')
    async def web_socket(ws: WebSocket):
        await ws.accept()
        while True:
            data = await ws.receive_text()
            await ws.send_text(data)

    @app.get('/assets{file_path:path}')
    def assets(file_path):
        path = '../erajs-frontend-web/dist/assets{}'.format(file_path)
        if exists(path):
            ext = splitext(path)[1]
            m = mime[ext]
            with open(path, 'rb') as file:
                return Response(file.read(), media_type=m)

    @app.get('{file_path:path}')
    def root(file_path):
        with open('../erajs-frontend-web/dist/index.html') as file:
            return HTMLResponse(file.read())
    run(app, log_level='warning')


def start():
    t = Thread(target=server)
    t.start()
