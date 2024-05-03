from core.hook import Hook, Mode


class LifeCycle:
    @staticmethod
    def __hook_handler(mode: Mode):
        for hook in Hook.registered.get(mode.value, []):  # noqa
            hook()

    def __init__(self):
        self.__hook_handler(Mode.INITIAL)

    def __enter__(self):
        self.__hook_handler(Mode.START)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__hook_handler(Mode.FINISH)
