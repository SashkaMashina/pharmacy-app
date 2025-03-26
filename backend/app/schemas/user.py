from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    role: str  # admin или customer

class UserCreate(UserBase):  # Для создания пользователя
    password: str

class UserResponse(UserBase):  # Для ответа API
    id: int

    class Config:
        from_attributes = True