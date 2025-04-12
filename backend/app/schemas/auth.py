from pydantic import BaseModel

# Схема для входа: ожидаем логин и пароль от пользователя
class LoginRequest(BaseModel):
    username: str
    password: str

# Схема ответа при успешной аутентификации: JWT-токен
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"