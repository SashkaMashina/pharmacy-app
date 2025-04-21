from datetime import datetime, timedelta
from typing import Optional

from passlib.context import CryptContext
from jose import jwt

from app.core.config import settings  # Подключаем настройки из config.py

# Инициализация контекста для bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Функция для хеширования пароля
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Функция для проверки пароля
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Функции для работы с JWT
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Функция для создания JWT-токена.
    :param data: Данные для токена (например, идентификатор пользователя)
    :param expires_delta: Время жизни токена
    :return: JWT-токен в виде строки
    """
    if expires_delta:
        expiration = datetime.utcnow() + expires_delta
    else:
        expiration = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = data.copy()
    to_encode.update({"exp": expiration})
    
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> dict:
    """
    Функция для проверки JWT-токена.
    :param token: JWT-токен для проверки
    :return: Данные из токена, если токен валиден
    :raises: Ошибка, если токен некорректен
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload  # Возвращаем данные из токена
    except jwt.ExpiredSignatureError:
        raise Exception("Signature has expired")
    except jwt.JWTError:
        raise Exception("Invalid token")

# Функция для защиты эндпоинтов с использованием токена
def get_current_user(token: str) -> dict:
    """
    Извлечение пользователя из токена.
    :param token: JWT-токен
    :return: Данные пользователя
    """
    return verify_token(token)