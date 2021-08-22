from logging import DEBUG, INFO
from typing import Any, Dict, Optional

from .modules.debug import DebugManager
from .modules.event import EventManager
from .modules.server import start


class Engine:
    def __init__(self, configs: Optional[Dict[str, Any]] = {'debug': True}):
        self.dm = DebugManager()
        self.dm.init(DEBUG if configs['debug'] else INFO)
        if configs['debug']:
            self.dm.debug('DEBUG_TEXT')
            self.dm.info('INFO_TEXT')
            self.dm.warning('WARNING_TEXT')
            self.dm.error('ERROR_TEXT')
            self.dm.critical('CRITICAL_TEXT')
        self.em = EventManager()
        start()

    def init(self):
        pass
