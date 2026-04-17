from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from datetime import datetime, timedelta
from typing import List

from app.api.v1.endpoint import router
from app.core.database import get_db
from app.models import classes, registration
from app.models.subscription import Subscription

router = APIRouter()

# --- REGISTRATION LOGIC ---
@router.post("/classes/{class_id}/register")
def register_student_to_class(class_id: int, student_id: int, db: Session = Depends(get_db)):
    target_class = db.query(classes).filter(classes.Id == class_id).first()
    if not target_class:
        raise HTTPException(404, "Class not found")

    # 1. Kiểm tra sĩ số
    current_count = db.query(registration).filter(registration.Registration.class_id == class_id).count()
    if current_count >= target_class.max_students:
        raise HTTPException(400, "Class is full")

    # 2. Kiểm tra trùng lịch (Cùng ngày & Cùng khung giờ)
    overlap = db.query(registration.Registration).join(classes).filter(
        registration.Registration.student_id == student_id,
        classes.day_of_week == target_class.day_of_week,
        classes.time_slot == target_class.time_slot
    ).first()
    if overlap:
        raise HTTPException(400, "Schedule conflict with another class")

    # 3. Kiểm tra gói học (Subscription)
    sub = db.query(Subscription).filter(
        Subscription.student_id == student_id,
        Subscription.end_date >= datetime.now().date(),
        Subscription.used_sessions < Subscription.total_sessions
    ).first()
    if not sub:
        raise HTTPException(400, "No active subscription or out of sessions")

    # Tiến hành đăng ký
    new_reg = registration.Registration(class_id=class_id, student_id=student_id)
    # Tự động tăng used_sessions khi đăng ký thành công
    sub.used_sessions += 1
    
    db.add(new_reg)
    db.commit()
    return {"message": "Registered successfully", "used_sessions": sub.used_sessions}

@router.delete("/registrations/{id}")
def cancel_registration(id: int, db: Session = Depends(get_db)):
    reg = db.query(registration.Registration).filter(registration.Registration.Id == id).first()
    if not reg:
        raise HTTPException(404, "Registration not found")

    # Giả định: logic kiểm tra 24h dựa trên thời gian bắt đầu lớp học
    # Ở đây lấy tạm thời gian hiện tại so với lịch học (cần logic mapping time_slot cụ thể)
    # Ví dụ đơn giản: Kiểm tra xem hôm nay có phải trước ngày học ít nhất 1 ngày không
    can_refund = True # Giả sử logic check > 24h pass
    
    if can_refund:
        sub = db.query(Subscription).filter(
            Subscription.student_id == reg.student_id,
            Subscription.used_sessions > 0
        ).first()
        if sub:
            sub.used_sessions -= 1 # Hoàn trả 1 buổi

    db.delete(reg)
    db.commit()
    return {"message": "Cancelled", "refunded": can_refund}