import datetime
from uuid import UUID

from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from sqlalchemy import cast, Date

from peak_time.infrastructure.db import Project, WorkDay


class ProjectRepository(SQLAlchemyAsyncRepository[Project]):
    model_type = Project


class ProjectRepositoryService(SQLAlchemyAsyncRepositoryService[Project]):
    repository_type = ProjectRepository


class WorkDayRepository(SQLAlchemyAsyncRepository[WorkDay]):
    model_type = WorkDay


class WorkDayRepositoryService(SQLAlchemyAsyncRepositoryService[WorkDay]):
    repository_type = WorkDayRepository

    async def get_or_create(self, project_id: UUID, date: datetime.date, auto_commit=False) -> WorkDay:
        today = await self.get_one_or_none(
            cast(WorkDay.created_at, Date) == date,
            WorkDay.project_id == project_id
        )
        if today is None:
            return await self.create(WorkDay(project_id=project_id), auto_commit=auto_commit)
        return today

