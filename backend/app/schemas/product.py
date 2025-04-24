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
    prescription_required: bool

    # Метод для преобразования HttpUrl в строку, если URL задан
    def dict(self, *args, **kwargs):
        data = super().dict(*args, **kwargs)
        if data.get('image_url') and isinstance(data['image_url'], HttpUrl):
            data['image_url'] = str(data['image_url'])  # Преобразуем в строку
        return data

class ProductCreate(ProductBase):  # Для создания продукта
    pass

class ProductUpdate(ProductBase):  # Для обновления продукта
    pass

class ProductResponse(ProductBase):  # Для ответа API
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True  # Чтобы работало с SQLAlchemy