from pydantic import BaseModel, HttpUrl
from typing import Optional
import datetime

class ProductBase(BaseModel):
    name: str
    category_id: int
    price: float
    stock: int
    description: Optional[str] = None
    image_url: Optional[HttpUrl] = None
    manufacturer: Optional[str] = None
    release_form: Optional[str] = None

class ProductCreate(ProductBase):  # Для создания продукта
    pass

class ProductUpdate(ProductBase):  # Для обновления продукта
    pass

class ProductResponse(ProductBase):  # Для ответа API
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True  # Чтобы работало с SQLAlchemy