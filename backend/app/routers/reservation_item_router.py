from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import models
from app.schemas.reservation_item import ReservationItemResponse

router = APIRouter(prefix="/reservation_items", tags=["Reservation Items"])

# Получить все зарезервированные товары
@router.get("/", response_model=list[ReservationItemResponse])
def get_all_items(db: Session = Depends(get_db)):
    return db.query(models.ReservationItem).all()

# Получить товар по ID
@router.get("/{id}", response_model=ReservationItemResponse)
def get_item_by_id(id: int, db: Session = Depends(get_db)):
    item = db.query(models.ReservationItem).filter(models.ReservationItem.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Reservation item not found")
    return item

# Получить все товары по ID бронирования
@router.get("/by_reservation/{reservation_id}", response_model=list[ReservationItemResponse])
def get_items_by_reservation(reservation_id: int, db: Session = Depends(get_db)):
    return db.query(models.ReservationItem).filter(models.ReservationItem.reservation_id == reservation_id).all()