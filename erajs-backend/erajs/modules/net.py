from .event import EventManager
from typing import Any, Optional

from . import server


class NetManager:
    def __init__(self):
        self.__debug = False
        self.__buf_size = 4096
        self.__is_connected = False
        self.__state: Any = {
            'length': 0,
            'length_bytes': '',
            'content_bytes': b''
        }
        self.em = EventManager()

    def start(self, host: str = 'localhost', port: int = 11994):
        server.start()

    def send_bytes():
        pass

    def send_text():
        pass

    def send_json():
        pass
