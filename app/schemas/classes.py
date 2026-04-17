from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from datetime import date, datetime
from typing import List, Optional

from app.schemas.base import BaseSchema

# ----------------------------------------------------------------
# CLASS SCHEMAS
# ----------------------------------------------------------------
class ClassBase(BaseSchema):
    name: str
    subject: str
    day_of_week: str
    time_slot: str
    teacher_name: str
    max_students: int

class ClassCreate(ClassBase):
    pass

class ClassResponse(ClassBase):
    Id: int