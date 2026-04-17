from datetime import date
from sqlalchemy import ForeignKey, String, Integer, Date, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional

from app.core.database import Base

class Registration(Base):
    __tablename__ = "class_registrations"
    # Vì Base đã có Id, nhưng bảng trung gian thường dùng Primary Key kép
    # Chúng ta ghi đè Id hoặc bỏ qua nếu không cần ID riêng cho bảng này
    # Ở đây tôi thiết kế theo dạng Mapping Table tiêu chuẩn
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.Id"), primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.Id"), primary_key=True)


