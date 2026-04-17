from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from datetime import datetime, timedelta
from typing import List

from app.core.database import get_db
from app.models.subscription import Subscription
from app.schemas.subscription import SubscriptionCreate, SubscriptionResponse

router = APIRouter()

# --- SUBSCRIPTIONS ---
@router.post("/subscriptions", response_model=SubscriptionResponse)
def create_subscription(obj_in: SubscriptionCreate, db: Session = Depends(get_db)):
    db_obj = Subscription(**obj_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

@router.patch("/subscriptions/{id}/use")
def use_session(id: int, db: Session = Depends(get_db)):
    sub = db.query(Subscription).filter(Subscription.Id == id).first()
    if not sub:
        raise HTTPException(404, "Subscription not found")
    
    if sub.used_sessions >= sub.total_sessions:
        raise HTTPException(400, "No sessions left")
        
    sub.used_sessions += 1
    db.commit()
    return {"message": "Session used", "remaining": sub.total_sessions - sub.used_sessions}

@router.get("/subscriptions/{id}", response_model=SubscriptionResponse)
def get_subscription_status(id: int, db: Session = Depends(get_db)):
    sub = db.query(Subscription).filter(Subscription.Id == id).first()
    if not sub:
        raise HTTPException(404, "Subscription not found")
    return sub