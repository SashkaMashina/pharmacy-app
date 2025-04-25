from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.admin import LoginRequest, TokenResponse
from app.models.models import Admin
from passlib.context import CryptContext
from jose import jwt, JWTError
from app.core.config import settings
from datetime import datetime, timedelta
from sqlalchemy import select


router = APIRouter(prefix="/auth", tags=["Authentication"])

# Настройка контекста для хэширования паролей (используем bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 

# Функция для генерации JWT токена с временем жизни
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})  # Добавляем время истечения
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


@router.post("/login", response_model=TokenResponse)
async def login(data: LoginRequest, db: AsyncSession = Depends(get_db)):  # Note: AsyncSession
    result = await db.execute(select(Admin).where(Admin.username == data.username))
    admin = result.scalar_one_or_none()
    # Ищем администратора по имени пользователя
    
    # Если не нашли или пароль не совпадает — ошибка
    if not admin or not pwd_context.verify(data.password, admin.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    # Генерация JWT-токена при успешном входе
    token_data = {"sub": admin.username}  # Это будет идентификатор пользователя
    access_token = create_access_token(data=token_data)  # Передаем данные для создания токена

    return TokenResponse(access_token=access_token, token_type="bearer")