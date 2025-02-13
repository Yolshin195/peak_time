from dataclasses import dataclass
from typing import Annotated

from litestar import Controller, get, post
from litestar.di import Provide
from litestar.params import Body
from litestar.response import Template, Redirect
from litestar.enums import RequestEncodingType
from pydantic import BaseModel, ConfigDict

from peak_time.application.repositories import ProjectRepositoryService
from peak_time.interfaces.web.dependencies import get_project_service

class ProjectModel(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)



class ProjectsPageController(Controller):
    path = "/"
    dependencies = {
        'service': Provide(get_project_service)
    }

    @get(path="/")
    async def list(self, service: ProjectRepositoryService) -> Template:
        rows = await service.list()
        return Template(template_name="project_list.html.jinja2", context={"rows": rows})

    async def get(self, id: int) -> dict:
        pass

    async def remove(self, id: int) -> dict:
        pass

    @post(path="/project/create")
    async def create(
            self,
            data: Annotated[ProjectModel, Body(media_type=RequestEncodingType.URL_ENCODED)],
            service: ProjectRepositoryService
    ) -> Redirect:
        await service.create(data, auto_commit=True)
        return Redirect(path="/")

    async def update(self, id: int) -> dict:
        pass