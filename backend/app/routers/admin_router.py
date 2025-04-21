from fastapi import APIRouter, Depends
from app.core.security import get_current_user

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/profile")
def get_admin_profile(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello, {current_user['sub']}! This is your admin profile."}