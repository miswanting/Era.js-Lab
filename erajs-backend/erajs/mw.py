from typing import Any, Callable

from .engine import Engine

e = Engine()


def init():
    e.init()


def entry(callback: Callable[[Any], None]):
    pass
