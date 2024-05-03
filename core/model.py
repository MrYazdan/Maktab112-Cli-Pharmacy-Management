from abc import ABC, abstractmethod


class Model(ABC):
    @classmethod
    @property
    @abstractmethod
    def store(cls):  # noqa
        raise NotImplementedError("'store' attr is required !")

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.store.append(instance)  # noqa
        return instance
