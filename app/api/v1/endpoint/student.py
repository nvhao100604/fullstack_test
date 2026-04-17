from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from datetime import datetime, timedelta
from typing import List

from app.api.v1.endpoint import router
from app.core.database import get_db
from app.models.parent import Parent
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentResponse

router = APIRouter()

# --- STUDENTS ---
@router.post("/students", response_model=StudentResponse)
def create_student(obj_in: StudentCreate, db: Session = Depends(get_db)):
    # Kiểm tra parent tồn tại
    parent = db.query(Parent).filter(Parent.Id == obj_in.parent_id).first()
    if not parent:
        raise HTTPException(status_code=404, detail="Parent ID not found")
    
    db_obj = Student(**obj_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

@router.get("/students/{id}", response_model=StudentResponse)
def get_student(id: int, db: Session = Depends(get_db)):
    student = db.query(Student).options(
        joinedload(Student.parent),
        joinedload(Student.classes),
        joinedload(Student.subscriptions)
    ).filter(Student.Id == id).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student