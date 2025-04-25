from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.database import get_db
from app.models import models
from app.schemas.reservation_item import ReservationItemResponse

router = APIRouter(prefix="/reservation_items", tags=["Reservation Items"])

# Получить все зарезервированные товары
@router.get("/", response_model=list[ReservationItemResponse])
async def get_all_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.ReservationItem))
    items = result.scalars().all()
    return items

# Получить товар по ID
@router.get("/{id}", response_model=ReservationItemResponse)
async def get_item_by_id(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.ReservationItem).where(models.ReservationItem.id == id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Reservation item not found")
    return item

# Получить все товары по ID бронирования
@router.get("/by_reservation/{reservation_id}", response_model=list[ReservationItemResponse])
async def get_items_by_reservation(reservation_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(models.ReservationItem).where(models.ReservationItem.reservation_id == reservation_id)
    )
    items = result.scalars().all()
    return items