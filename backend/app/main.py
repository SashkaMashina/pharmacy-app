from fastapi import FastAPI, Depends
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

app = FastAPI(title="Pharmacy API")


@app.get("/") # Добавляем корневой эндпоинт / для проверки работы
def read_root():
    return {"message": "Pharmacy API is running"}


@app.get("/ping_db")
async def ping_db(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(text("SELECT 1"))
        return {"message": "Database connected successfully"}
    except Exception as e:
        return {"error": str(e)}