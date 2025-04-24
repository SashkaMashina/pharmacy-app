from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import models
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.core.database import get_db  # для работы с БД

router = APIRouter(tags=["Products"])

# Эндпоинт для создания продукта
@router.post("/products/", response_model=ProductResponse)
async def create_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    await db.commit()  # Не забудь добавить await для commit
    await db.refresh(db_product)  # Также await для refresh
    return db_product

# Эндпоинт для получения списка продуктов с фильтрацией
@router.get("/products/", response_model=list[ProductResponse])
async def get_products(
    name: str = None,
    category_id: int = None,
    category_name: str = None,
    prescription_required: bool = None,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(models.Product)
    
    if name:
        stmt = stmt.where(models.Product.name.ilike(f"%{name}%"))
    if category_name:
        category = await db.execute(select(models.Category).filter(models.Category.name.ilike(f"%{category_name}%")))
        category = category.scalar_one_or_none()  # Получаем одну категорию или None
        if category:
            stmt = stmt.where(models.Product.category_id == category.id)
        else:
            return []  # Если категория не найдена, возвращаем пустой список
    if prescription_required is not None:
        stmt = stmt.where(models.Product.prescription_required == prescription_required)
    
    result = await db.execute(stmt)
    products = result.scalars().all()  # Для получения всех продуктов
    return products

# Эндпоинт для получения продукта по ID
@router.get("/products/{id}/", response_model=ProductResponse)
async def get_product(id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(models.Product).where(models.Product.id == id)
    result = await db.execute(stmt)
    product = result.scalar_one_or_none()  # Получаем один продукт или None
    
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Эндпоинт для обновления продукта
@router.put("/products/{id}/", response_model=ProductResponse)
async def update_product(id: int, product: ProductUpdate, db: AsyncSession = Depends(get_db)):
    stmt = select(models.Product).where(models.Product.id == id)
    result = await db.execute(stmt)
    db_product = result.scalar_one_or_none()
    
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    
    await db.commit()  # Не забудь добавить await для commit
    await db.refresh(db_product)  # И await для refresh
    return db_product

# Эндпоинт для удаления продукта
@router.delete("/products/{id}/")
async def delete_product(id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(models.Product).where(models.Product.id == id)
    result = await db.execute(stmt)
    db_product = result.scalar_one_or_none()
    
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    await db.delete(db_product)  # Удаление также должно быть асинхронным
    await db.commit()  # И коммит
    return {"message": "Product deleted successfully"}