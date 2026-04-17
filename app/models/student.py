from datetime import date
from sqlalchemy import ForeignKey, String, Integer, Date, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List, Optional

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.parent import Parent
    from app.models.classes import Class
    from app.models.subscription import Subscription

class Student(Base):
    __tablename__ = "students"

    name: Mapped[str] = mapped_column(String(100))
    dob: Mapped[date] = mapped_column(Date)
    gender: Mapped[str] = mapped_column(String(10))
    current_grade: Mapped[int] = mapped_column(Integer)
    parent_id: Mapped[int] = mapped_column(ForeignKey("parents.Id"))

    parent: Mapped["Parent"] = relationship(back_populates="students")
    classes: Mapped[List["Class"]] = relationship(
        secondary="class_registrations", back_populates="students"
    )
    subscriptions: Mapped[List["Subscription"]] = relationship(back_populates="student")
