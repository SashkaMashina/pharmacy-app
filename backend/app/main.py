from fastapi import FastAPI, Depends
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from app.middlewares.jwt_middleware import JWTMiddleware

from app.routers.auth_router import router as auth_router
from app.routers.admin_router import router as admin_router
from app.routers.product_router import router as product_router
from app.routers.category_router import router as category_router


app = FastAPI(title="Pharmacy API")
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(product_router)
app.include_router(category_router)

app.add_middleware(JWTMiddleware)


@app.get("/")
def read_root():
    return {"message": "Pharmacy API is running"}


@app.get("/ping_db")
async def ping_db(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(text("SELECT 1"))
        return {"message": "Database connected successfully"}
    except Exception as e:
        return {"error": str(e)}