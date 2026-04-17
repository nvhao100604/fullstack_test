from fastapi import APIRouter

from app.api.v1.endpoint import classes, parent, registration, student, subscription


api_router = APIRouter()

api_router.include_router(
    parent.router, 
    prefix="/parents", 
    tags=["Parents"]
)

api_router.include_router(
    student.router, 
    prefix="/students", 
    tags=["Students"]
)

api_router.include_router(
    classes.router, 
    prefix="/classes", 
    tags=["Classes"]
)

api_router.include_router(
    subscription.router, 
    prefix="/subscriptions", 
    tags=["Subscriptions"]
)

# Đối với các endpoint về đăng ký (registrations), 
# bạn có thể gộp vào classes hoặc tách riêng tùy logic
api_router.include_router(
    registration.router, 
    prefix="/registrations", 
    tags=["Class Registrations"]
)