from typing import Any, ClassVar, Optional


class Singleton:
    """
    # 单例模式原型
    """
    __instance: ClassVar[Optional['Singleton']] = None

    def __new__(cls, *args: Any, **kw: Any):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls.__instance
