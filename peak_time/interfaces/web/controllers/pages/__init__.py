from litestar import Router

from .workdays import WorkdaysPages
from .projects import ProjectsPageController

pages = Router(path="/", route_handlers=[
    WorkdaysPages,
    ProjectsPageController,
])

__all__ = ["pages"]