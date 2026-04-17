from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from datetime import date, datetime
from typing import List, Optional

from app.schemas.base import BaseSchema
from app.schemas.classes import ClassResponse
from app.schemas.parent import ParentResponse
from app.schemas.subscription import SubscriptionResponse

# ----------------------------------------------------------------
# STUDENT SCHEMAS
# ----------------------------------------------------------------
class StudentBase(BaseSchema):
    name: str
    dob: date
    gender: str
    current_grade: int
    parent_id: int

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseSchema):
    name: Optional[str] = None
    dob: Optional[date] = None
    current_grade: Optional[int] = None

class StudentResponse(StudentBase):
    Id: int
    # Quan hệ mở rộng
    parent: Optional[ParentResponse] = None
    subscriptions: List[SubscriptionResponse] = []
    classes: List[ClassResponse] = []