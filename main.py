import atexit
import signal
import models
from core.db import DataBase


def goodbye():
    print("Bye Bye :)")


if __name__ == '__main__':
    db = DataBase("db.pickle")
    db.load()

    db.register(models.User)

    models.User("yazdan", "1234")
    # models.User("sepehr", "kheili-ajib")
    # models.User("reyhane", "1234")
    # print(*[u.username for u in db[models.User.__name__]])
    print(*[u.username for u in models.User.store])

    atexit.register(db.save)
    signal.signal(signal.SIGTERM, lambda signum, frame: exit())
