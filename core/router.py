from core.utils import banner
from importlib import import_module
from core.state import RouteStateManager


class Callback:
    def __init__(self, package: str, callback: str) -> None:
        self.callback = getattr(import_module(package), callback)

    def __call__(self, *args, **kwargs):
        return self.callback(*args, **kwargs)


class Route:
    def __init__(
            self, name: str,
            description: str | None = None,
            children: list | None = None,
            callback: Callback | None = None,
            condition=lambda: True
    ) -> None:
        self.parent = None
        self.children = None

        self.name = name
        self.description = description
        self.callback = callback
        self.condition = condition

        children and self._set_parent(children)

    def _set_parent(self, children: list) -> None:
        for child in children:
            child.parent = self

        self.children = children

    def _get_route(self):
        try:
            banner(RouteStateManager.get_current_route())
            print(self.description or '')

            if children := [child for child in self.children if child.condition()]:
                for child in children:
                    print(f"\t🔸{children.index(child) + 1}. {child.name}")
                print(f"\n\t🔹0. " + ("Exit" if not self.parent else f"Back to {self.parent.name}"))

                index = int(input("\n > ")) - 1
                route = children[index] if index != -1 else self.parent

                if not route:
                    banner("Exit")

                    if (cmd := input("Do you want to exit ? [y|N] ").strip().lower()) and cmd[0] == "y":
                        exit()
                    else:
                        self()
                return route
            else:
                return self
        except (ValueError, KeyboardInterrupt, IndexError):
            banner(" Error ❗ ")
            input("Please enter valid item\n\nPress enter to continue ...")
            self()

    def __call__(self, *args, **kwargs):
        RouteStateManager.add_route(self.name)

        route = self._get_route()

        if self.parent == route:
            RouteStateManager.delete_last_route()
            self.parent()

        elif route.children:
            route()

        else:
            banner(" ⚜️ " + route.name + " ⚜️ ")
            route.description and print(route.description)
            route.callback and route.callback(route)

            input("\n\nPress enter to continue ...")
            RouteStateManager.delete_last_route()
            route.parent()


class Router:
    def __init__(self, route: Route) -> None:
        self.route = route

    def __call__(self, *args, **kwargs):
        self.route()
