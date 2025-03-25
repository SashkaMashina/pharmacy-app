from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL

# Создаем движок подключения к БД
engine = create_async_engine(DATABASE_URL, future=True, echo=True)

# Создаем фабрику сессий для работы с БД
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Функция для получения сессии (для работы с зависимостями в FastAPI)
async def get_db():
    async with async_session() as session:
        yield session