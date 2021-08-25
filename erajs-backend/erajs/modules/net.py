from typing import Any, Optional

from . import server
from .event import EventManager


class NetManager:
    def __init__(self):
        self.em = EventManager()

    def start(self, host: str = 'localhost', port: int = 11994):
        print(f'http://{host}:{port}/')
        server.start(host,port)

