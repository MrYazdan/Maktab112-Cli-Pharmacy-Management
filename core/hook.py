import enum
from typing import Callable


class Mode(enum.Enum):
    """
        Define hook mode constant attr
    """
    INITIAL = "initial"
    START = "start"
    FINISH = "finish"


class Hook:
    __registered = {}

    def __init__(self, mode: Mode, callback: Callable, *args, **kwargs):
        assert isinstance(mode, Mode), "mode must be an instance of hook mode"
        self.mode = mode.value

        assert callable(callback), "callback must be callable !"
        self.callback = callback

        self.args = args
        self.kwargs = kwargs

        self.__class__.__registered.setdefault(self.mode, [])
        self.__class__.__registered[self.mode].append(self)

    @classmethod
    @property
    def registered(cls) -> dict:
        return cls.__registered

    def __call__(self, *args, **kwargs):
        return self.callback(*self.args, **self.kwargs)
