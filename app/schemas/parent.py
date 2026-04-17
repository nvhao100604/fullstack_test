from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from datetime import date, datetime
from typing import List, Optional

from app.schemas.base import BaseSchema
# ----------------------------------------------------------------
# PARENT SCHEMAS
# ----------------------------------------------------------------
class ParentBase(BaseSchema):
    name: str
    phone: str
    email: Optional[str] = None

class ParentCreate(ParentBase):
    pass

class ParentResponse(ParentBase):
    Id: int  # Giữ nguyên Id theo Base Model của bạn