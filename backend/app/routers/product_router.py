from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import models
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.core.database import get_db  # для работы с БД
from sqlalchemy import or_

router = APIRouter()

# Эндпоинт для создания продукта
@router.post("/products/", response_model=ProductResponse)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Эндпоинт для получения списка продуктов с фильтрацией
@router.get("/products/", response_model=list[ProductResponse])
async def get_products(
    name: str = None,
    category_id: int = None,
    category_name: str = None,
    prescription_required: bool = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Product)
    if name:
        query = query.filter(models.Product.name.ilike(f"%{name}%"))
    if category_name:
        category = db.query(models.Category).filter(models.Category.name.ilike(f"%{category_name}%")).first()
        if category:
            query = query.filter(models.Product.category_id == category.id)
        else:
            return []  # Если категория не найдена — возвращаем пустой список
    if prescription_required is not None:
        query = query.filter(models.Product.prescription_required == prescription_required)
    products = query.all()
    return products

# Эндпоинт для получения продукта по ID
@router.get("/products/{id}/", response_model=ProductResponse)
async def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Эндпоинт для обновления продукта
@router.put("/products/{id}/", response_model=ProductResponse)
async def update_product(id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

# Эндпоинт для удаления продукта
@router.delete("/products/{id}/")
async def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}