from core.model import Model


class User(Model):
    store = []

    def validate_username(self, username: str) -> bool:
        assert isinstance(username, str) and len(username) >= 4, "Username must be str type and length >= 4"
        for user in self.__class__.store:
            if hasattr(user, "username"):
                assert user.username != username, "Username already exists !"
        return True

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, new_username: str) -> None:
        self.validate_username(new_username)
        self.__username = new_username


class Drug:
    pass
