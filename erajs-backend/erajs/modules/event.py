from threading import Thread
from typing import Any, Callable, Dict, List, Optional

from .debug import DebugManager
from .tools import Tools


class EventManager:
    def __init__(self):
        super().__init__()
        self.dm = DebugManager()

        self.__listeners: Dict[str, Any] = {}

    def on(self, event_type: str, callback: Callable[[Any], None], once: bool = False, tags: Optional[List[str]] = None):
        listener: Dict[str, Any] = {
            'hash': Tools.random_hash(),
            'type': event_type,
            'callback': callback,
            'once': once,
            'tags': [] if tags is None else tags
        }
        self.dm.debug('Event Listener Add: {}'.format(event_type))
        self.__listeners[str(listener['hash'])] = listener
        return listener

    def off(self, event_type: str, callback: Callable[[Any], None]):
        for key in list(self.__listeners.keys()):
            self.dm.debug('Event Listener Remove: {}'.format(event_type))
            if self.__listeners[key]['type'] == event_type and str(self.__listeners[key]['callback'].__name__) == callback.__name__:
                del self.__listeners[key]

    def emit(self, event_type: str, *arg: Any, **kw: Any):
        for hash in list(self.__listeners.keys()):
            if hash in self.__listeners and self.__listeners[hash]['type'] == event_type:
                self.dm.debug('Event Emit: {}'.format(event_type))
                t = Thread(
                    target=self.__listeners[hash]['callback'], args=arg, kwargs=kw)
                if self.__listeners[hash]['once']:
                    del self.__listeners[hash]
                t.start()

    def remove_all_listeners(self, *exception_tags: str):
        for key in list(self.__listeners.keys()):
            is_exception = False
            for tag in self.__listeners[key]['tags']:
                if tag in exception_tags:
                    is_exception = True
                    break
            if not is_exception:
                del self.__listeners[key]

    def get_listener_list(self):
        return self.__listeners
