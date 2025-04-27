from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str
    SMTP_USER: str
    SMTP_PASSWORD: str

    model_config = SettingsConfigDict(env_file=".env")  # Чтение переменных из файла .env

settings = Settings()