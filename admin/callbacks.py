from time import sleep
from models import User
from getpass import getpass
from core.state import Auth
from core.utils import safe


@safe
def login(route):
    username = input("Please enter username: ").strip().lower()
    assert username, "Username should not be empty !"

    password = getpass("Please enter password: ")
    assert password, "Password should not be empty !"

    for user in User.store:
        if user.password == password and user.username == username:
            Auth.login_status = True
            Auth.user = user
            print(f"\n\nWelcome '{user.username.title()}' ⭐ ")
            sleep(4)
            break
    else:
        raise ValueError("Username or password invalid !")


@safe
def register(route):
    username = input("Please enter username: ").strip().lower()
    assert username, "Username should not be empty !"

    password = getpass("Please enter password: ")
    assert password, "Password should not be empty !"

    confirm_password = getpass("Please re-enter password: ")
    assert confirm_password, "Confirm Password should not be empty !"
    assert confirm_password == password, "Confirm password and password doesn't match !"

    User(username, password)
    print("Register Successful ✅ ")


def logout(route):
    print("In Logout Callbacks")
    Auth.login_status = False
