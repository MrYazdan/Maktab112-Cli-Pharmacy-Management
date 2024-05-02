import pickle


class DataBase:
    __store = {}
    __models = set()

    def __init__(self, path: str) -> None:
        self.path = path

    def __getitem__(self, key):
        return self.__store[key]

    def load(self):
        try:
            with open(self.path, "rb") as file:
                self.__store = pickle.load(file)

                for model in self.__models:
                    model.store = self.__store[model.__name__]
        except (FileNotFoundError, EOFError):
            pass

    def save(self):
        with open(self.path, "wb") as file:
            for model in self.__models:
                self.__store[model.__name__] = model.store

            pickle.dump(self.__store, file)

    def register(self, model):
        self.__class__.__models.add(model)
        self.__class__.__store.setdefault(model.__name__, [])
