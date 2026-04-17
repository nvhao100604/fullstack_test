from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from datetime import date, datetime
from typing import List, Optional

from app.schemas.base import BaseSchema

# ----------------------------------------------------------------
# SUBSCRIPTION SCHEMAS
# ----------------------------------------------------------------
class SubscriptionBase(BaseSchema):
    student_id: int
    package_name: str
    start_date: date
    end_date: date
    total_sessions: int
    used_sessions: int = 0

class SubscriptionCreate(SubscriptionBase):
    pass

class SubscriptionResponse(SubscriptionBase):
    Id: int