from os import system as terminal, name as os_name


def clear():
    terminal("cls" if os_name.lower() == "nt" else "clear")


def banner(title: str):
    clear()
    print("="*40, title.title().center(40), "="*40, sep="\n", end="\n\n")
