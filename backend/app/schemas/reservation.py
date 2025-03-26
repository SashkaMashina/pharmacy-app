from pydantic import BaseModel, EmailStr
import datetime

class ReservationBase(BaseModel):
    user_email: EmailStr
    name: str
    phone: str
    product_id: int
    quantity: int
    status: str  # pending, confirmed, canceled

class ReservationCreate(ReservationBase):  # Для создания бронирования
    pass

class ReservationUpdate(BaseModel):  # Для обновления бронирования
    status: str

class ReservationResponse(ReservationBase):  # Для ответа API
    id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True