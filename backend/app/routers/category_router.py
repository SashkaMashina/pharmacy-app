from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import models
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse
from app.core.database import get_db

router = APIRouter()

@router.post("/categories/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/categories/", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()

@router.get("/categories/{id}/", response_model=CategoryResponse)
def get_category(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/categories/{id}/", response_model=CategoryResponse)
def update_category(id: int, update: CategoryUpdate, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    if update.name is not None:
        category.name = update.name
    db.commit()
    db.refresh(category)
    return category

@router.delete("/categories/{id}/")
def delete_category(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(category)
    db.commit()
    return {"message": "Category deleted"}