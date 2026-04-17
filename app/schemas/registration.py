from app.schemas.base import BaseSchema

# ----------------------------------------------------------------
# REGISTRATION SCHEMA
# ----------------------------------------------------------------
class ClassRegistrationRequest(BaseSchema):
    student_id: int
    class_id: int