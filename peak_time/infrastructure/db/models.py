from datetime import datetime
from uuid import UUID

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Base(UUIDAuditBase):
    __abstract__ = True


class Project(Base):
    __tablename__ = "project"
    name: Mapped[str] = mapped_column(unique=True)

    work_days: Mapped[list["WorkDay"]] = relationship(back_populates="project")


class WorkDayTask(Base):
    __tablename__ = "workday_task"

    workday_id: Mapped[UUID] = mapped_column(ForeignKey("work_day.id"), primary_key=True)
    work_day: Mapped["WorkDay"] = relationship(foreign_keys=[workday_id])

    task_id: Mapped[UUID] = mapped_column(ForeignKey("task.id"), primary_key=True)
    task: Mapped["Task"] = relationship(foreign_keys=[task_id])


class WorkDay(Base):
    __tablename__ = "work_day"

    start_time: Mapped[datetime | None] = mapped_column(nullable=True, comment="Start of the workday")
    end_time: Mapped[datetime | None] = mapped_column(nullable=True, comment="End of the workday")

    project_id: Mapped[UUID] = mapped_column(ForeignKey("project.id"))
    project: Mapped["Project"] = relationship(back_populates="work_days")


class Task(Base):
    __tablename__ = "task"

    timers: Mapped[list["TaskTimer"]] = relationship(back_populates="task")


class TaskTimer(Base):
    __tablename__ = "task_timer"

    task_id: Mapped[UUID] = mapped_column(ForeignKey("task.id"))
    task: Mapped["Task"] = relationship(back_populates="timers")
