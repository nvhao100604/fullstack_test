from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from datetime import datetime, timedelta
from typing import List

from app.core.database import get_db
from app.models.parent import Parent
from app.schemas.parent import ParentCreate, ParentResponse

router = APIRouter()

# --- PARENTS ---
@router.post("/parents", response_model=ParentResponse)
def create_parent(obj_in: ParentCreate, db: Session = Depends(get_db)):
    db_obj = Parent(**obj_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

@router.get("/parents/{id}", response_model=ParentResponse)
def get_parent(id: int, db: Session = Depends(get_db)):
    parent = db.query(Parent).filter(Parent.Id == id).first()
    if not parent:
        raise HTTPException(status_code=404, detail="Parent not found")
    return parent