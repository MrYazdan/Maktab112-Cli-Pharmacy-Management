from os import system as terminal, name as os_name


def clear():
    terminal("cls" if os_name.lower() == "nt" else "clear")


def banner(title: str):
    clear()
    print("_"*40, f"\u001b[38;5;4m{title.title().center(40)}\u001b[0m", "="*40, sep="\n")


def safe(callback):
    def _(route):
        try:
            callback(route)
        except Exception as e:
            banner(" Error ❗ ")
            print(f"\u001b[38;5;1m{str(e)}\u001b[0m")
            if (cmd := input("\nTry Again ? [Y|n] ").strip().lower()) and cmd[0] == "n":
                route.parent()
            else:
                banner(" ⚜️ " + route.name + " ⚜️ ")
                callback(route)
    return _
