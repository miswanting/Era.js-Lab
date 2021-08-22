from logging import (CRITICAL, DEBUG, ERROR, INFO, NOTSET, WARNING,
                     FileHandler, Formatter, StreamHandler, getLogger)
from sys import stdout
from typing import Any

from colorama import Fore, init

from ..prototypes.singleton import Singleton
from .tools import Tools


class DebugManager(Singleton):
    DebugLevelText = {
        0: ['    ', Fore.RESET],
        10: ['DEBG', Fore.RESET],
        20: ['INFO', Fore.CYAN],
        30: ['WARN', Fore.YELLOW],
        40: ['ERRO', Fore.RED],
        50: ['!!!!', Fore.RED],
    }

    def init(self, level=NOTSET):
        self.level = level
        if level in [NOTSET, DEBUG]:
            print('Setup Debug System...', end='')

        init()

        formatter = Formatter()

        stream_handler = StreamHandler(stdout)
        stream_handler.setFormatter(formatter)

        file_handler = FileHandler('Erajs.log', 'w', 'utf-8')
        file_handler.setFormatter(formatter)

        self.__logger = getLogger()
        # self.__logger.basiv
        self.__logger.setLevel(level)

        # if len(self.__logger.handlers) == 0:
        self.__logger.addHandler(stream_handler)
        self.__logger.addHandler(file_handler)

        if level in [NOTSET, DEBUG]:
            print('OK')

    def debug(self, *arg: Any, **kw: Any):
        self.__logger.debug(self.__get_debug_text(DEBUG, *arg, **kw))

    def info(self,  *arg: Any, **kw: Any):
        self.__logger.info(self.__get_debug_text(INFO, *arg, **kw))

    def warning(self, *arg: Any, **kw: Any):
        self.__logger.warning(self.__get_debug_text(WARNING, *arg, **kw))

    def error(self, *arg: Any, **kw: Any):
        self.__logger.error(self.__get_debug_text(ERROR, *arg, **kw))

    def critical(self,  *arg: Any, **kw: Any):
        self.__logger.critical(self.__get_debug_text(CRITICAL, *arg, **kw))

    def __get_debug_text(self, level: int, *arg: Any, **kw: Any):
        template = self.DebugLevelText[level][1]+'[{}]({}){}'+Fore.RESET
        prefix = self.DebugLevelText[level][0]
        timestamp = Tools.timestamp()
        text = ' '.join([str(msg) for msg in arg])
        return template.format(prefix, timestamp, text)
