class RouteStateManager:
    __routes = []

    @classmethod
    def add_route(cls, route_name: str) -> None:
        if not cls.__routes:
            cls.__routes.append(route_name)

        elif cls.__routes[-1] != route_name:
            cls.__routes.append(route_name)

    @classmethod
    def get_current_route(cls) -> str:
        return " > ".join(cls.__routes)

    @classmethod
    def delete_last_route(cls):
        cls.__routes.pop()
