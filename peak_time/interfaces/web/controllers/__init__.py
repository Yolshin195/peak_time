from litestar import Router
from .pages import pages

controllers = Router(path="/", route_handlers=[pages])

__all__ = [
    "controllers"
]
