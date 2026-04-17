from datetime import date
from sqlalchemy import ForeignKey, String, Integer, Date, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List, Optional

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.student import Student

class Parent(Base):
    __tablename__ = "parents"

    name: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(20), unique=True)
    email: Mapped[Optional[str]] = mapped_column(String(100), unique=True)

    students: Mapped[List["Student"]] = relationship(back_populates="parent")