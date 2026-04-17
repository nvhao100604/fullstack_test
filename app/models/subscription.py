from datetime import date
from sqlalchemy import ForeignKey, String, Integer, Date, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List, Optional

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.student import Student
    
class Subscription(Base):
    __tablename__ = "subscriptions"

    student_id: Mapped[int] = mapped_column(ForeignKey("students.Id"))
    package_name: Mapped[str] = mapped_column(String(100))
    start_date: Mapped[date] = mapped_column(Date)
    end_date: Mapped[date] = mapped_column(Date)
    total_sessions: Mapped[int] = mapped_column(Integer)
    used_sessions: Mapped[int] = mapped_column(Integer, default=0)

    student: Mapped["Student"] = relationship(back_populates="subscriptions")