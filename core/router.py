from importlib import import_module
from typing import Callable

from core.state import RouteStateManager
from core.utils import banner


class Callback:
    def __init__(self, package: str, callback: str) -> None:
        self.callback = getattr(import_module(package), callback)

    def __call__(self, *args, **kwargs):
        return self.callback(*args, **kwargs)


class Route:
    def __init__(self, name: str,
                 description: str | None = None,
                 children: list | None = None,
                 callback: Callable = None,
                 condition=lambda: True
                 ) -> None:
        self.parent = None

        self.name = name
        self.description = description
        self.callback = callback
        self.condition = condition

        if children:
            self._set_parent(children)
            self.children = children
        else:
            self.children = None

    def _set_parent(self, children: list) -> None:
        for child in children:
            child.parent = self

    def _get_route(self):
        try:
            banner(RouteStateManager.get_current_route())
            print(self.description or '', end="\n\n")

            if children := [child for child in self.children if child.condition()]:
                for child in children:
                    print(f"\t{children.index(child) + 1}. {child.name}")
                print(f"\n\t0. " + ("Exit" if not self.parent else f"Back to {self.parent.name}"))

                index = int(input("\n > ")) - 1
                route = children[index] if index != -1 else self.parent

                if not route:
                    banner("Exit")

                    if input("Do you want to exit ? [y|N] ").strip().lower()[0] == "y":
                        exit()
                    else:
                        self()
                return route
            else:
                return self
        except (ValueError, KeyboardInterrupt, IndexError):
            banner("Error")
            input("Please enter valid item\n\nPress enter to continue ...")
            self()

    def __call__(self, *args, **kwargs):
        RouteStateManager.add_route(self.name)

        route = self._get_route()

        print(route)
        if self.parent == route:
            RouteStateManager.delete_last_route()
            route()

        elif route.children:
            route()

        else:
            try:
                banner(route.name)
                route.description and print(route.description, end="\n\n")
                route.callback and route.callback(route)
            except Exception as e:
                banner("Error")
                print(e)

            input("\n\nPress enter to continue ...")
            RouteStateManager.delete_last_route()
            route.parent()


class Router:
    def __init__(self, route: Route) -> None:
        self.route = route
        RouteStateManager.add_route(route.name)

    def __call__(self, *args, **kwargs):
        self.route()
