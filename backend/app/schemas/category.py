from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str  # Название категории

class CategoryCreate(CategoryBase):  # Используется при создании категории
    pass

class CategoryUpdate(BaseModel):  # Используется при обновлении категории
    name: Optional[str] = None

class CategoryResponse(CategoryBase):  # Используется для ответа API
    id: int

    class Config:
        from_attributes = True