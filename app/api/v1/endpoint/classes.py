from pyclbr import Class

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from datetime import datetime, timedelta
from typing import List

from app.api.v1.endpoint import router
from app.core.database import get_db
from app.schemas.classes import ClassCreate, ClassResponse

router = APIRouter()

# --- CLASSES ---
@router.post("/classes", response_model=ClassResponse)
def create_class(obj_in: ClassCreate, db: Session = Depends(get_db)):
    db_obj = Class(**obj_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

@router.get("/classes", response_model=List[ClassResponse])
def list_classes(day: str = None, db: Session = Depends(get_db)):
    query = db.query(Class)
    if day:
        query = query.filter(Class.day_of_week == day)
    return query.all()