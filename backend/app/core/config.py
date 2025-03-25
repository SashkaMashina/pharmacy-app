import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost:5432/pharmacy_db") # 2-ой аргумент - это значение по умолчанию, если переменная DATABASE_URL не установлена