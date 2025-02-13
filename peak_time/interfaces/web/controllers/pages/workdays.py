import datetime
from uuid import UUID

from litestar import Controller, get
from litestar.di import Provide
from litestar.response import Template

from peak_time.interfaces.web.dependencies import get_work_day_service
from peak_time.application.repositories import WorkDayRepositoryService


class WorkdaysPages(Controller):
    path = "/workday"
    dependencies = {
        'service': Provide(get_work_day_service)
    }

    @get(path="/")
    async def main(self) -> Template:
        return Template(template_name="base.html.jinja2", context={"name": "test"})

    @get(path="/project/{project_id:str}/today")
    async def today(self, project_id: UUID, service: WorkDayRepositoryService) -> Template:
        workday_today = await service.get_or_create(project_id, datetime.date.today(), auto_commit=True)
        return Template(template_name="workday.html.jinja2", context={"workday": workday_today})