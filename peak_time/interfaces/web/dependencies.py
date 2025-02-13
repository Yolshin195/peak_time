from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from peak_time.application.repositories import ProjectRepositoryService, WorkDayRepositoryService


async def get_project_service(db_session: AsyncSession) -> AsyncGenerator[ProjectRepositoryService, None]:
    """This provides the default ProjectServiceRepositoryService repository."""
    async with ProjectRepositoryService.new(session=db_session) as service:
        yield service


async def get_work_day_service(db_session: AsyncSession) -> AsyncGenerator[WorkDayRepositoryService, None]:
    """This provides the default WorkDayServiceRepositoryService repository."""
    async with WorkDayRepositoryService.new(session=db_session) as service:
        yield service
