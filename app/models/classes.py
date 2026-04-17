from datetime import date
from sqlalchemy import ForeignKey, String, Integer, Date, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List, Optional

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.student import Student
    
class Class(Base):
    __tablename__ = "classes"

    name: Mapped[str] = mapped_column(String(100))
    subject: Mapped[str] = mapped_column(String(50))
    day_of_week: Mapped[str] = mapped_column(String(20))
    time_slot: Mapped[str] = mapped_column(String(50))
    teacher_name: Mapped[str] = mapped_column(String(100))
    max_students: Mapped[int] = mapped_column(Integer)

    students: Mapped[List["Student"]] = relationship(
        secondary="class_registrations", back_populates="classes"
    )