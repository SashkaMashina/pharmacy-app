from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import models
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse
from app.core.database import get_db

router = APIRouter(tags=["Categories"])

@router.post("/categories/", response_model=CategoryResponse)
async def create_category(category: CategoryCreate, db: AsyncSession = Depends(get_db)):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category

@router.get("/categories/", response_model=list[CategoryResponse])
async def get_categories(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Category))
    categories = result.scalars().all()
    return categories

@router.get("/categories/{id}/", response_model=CategoryResponse)
async def get_category(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Category).where(models.Category.id == id))
    category = result.scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/categories/{id}/", response_model=CategoryResponse)
async def update_category(id: int, update: CategoryUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Category).where(models.Category.id == id))
    category = result.scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    if update.name is not None:
        category.name = update.name
    await db.commit()
    await db.refresh(category)
    return category

@router.delete("/categories/{id}/")
async def delete_category(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Category).where(models.Category.id == id))
    category = result.scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    await db.delete(category)
    await db.commit()
    return {"message": "Category deleted"}