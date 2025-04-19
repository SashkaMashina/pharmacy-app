from pydantic import BaseModel, EmailStr
from typing import List
import datetime
from .reservation_item import ReservationItemCreate, ReservationItemResponse

class ReservationBase(BaseModel):
    user_name: str
    user_phone: str
    user_email: EmailStr
    status: str  # pending, confirmed, canceled
    sum: float

class ReservationCreate(ReservationBase):
    items: List[ReservationItemCreate]

class ReservationResponse(ReservationBase):
    id: int
    created_at: datetime.datetime
    items: List[ReservationItemResponse]

    class Config:
        from_attributes = True