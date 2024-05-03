import pickle


class DataBase:
    __store = {}
    __models = {}

    def __init__(self, path: str) -> None:
        self.path = path

    def __getitem__(self, key):
        return self.__models[key].store

    def load(self):
        try:
            with open(self.path, "rb") as file:
                self.__store = pickle.load(file)

                for model in self.__models.values():
                    model.store = self.__store.get(model.__name__, [])
        except (FileNotFoundError, EOFError):
            pass

    def save(self):
        with open(self.path, "wb") as file:
            for model in self.__models.values():
                self.__store[model.__name__] = model.store

            pickle.dump(self.__store, file)

    def register(self, model):
        self.__class__.__models[model.__name__] = model
        self.__class__.__store.setdefault(model.__name__, model.store)
