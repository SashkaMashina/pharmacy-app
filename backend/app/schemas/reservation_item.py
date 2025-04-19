from pydantic import BaseModel

class ReservationItemBase(BaseModel):
    product_id: int
    quantity: int
    price: float  # Цена на момент заказа

class ReservationItemCreate(ReservationItemBase):
    pass

class ReservationItemResponse(ReservationItemBase):
    id: int

    class Config:
        from_attributes = True