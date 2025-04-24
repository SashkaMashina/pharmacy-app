from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import or_
from app.models import models
from app.schemas.reservation import ReservationCreate, ReservationResponse, ReservationUpdate
from app.core.database import get_db

router = APIRouter(prefix="/reservations", tags=["Reservations"])

# Создание бронирования
@router.post("/", response_model=ReservationResponse)
async def create_reservation(reservation: ReservationCreate, db: AsyncSession = Depends(get_db)):
    db_reservation = models.Reservation(
        user_name=reservation.user_name,
        user_phone=reservation.user_phone,
        user_email=reservation.user_email,
        status=reservation.status,
        total_sum=reservation.sum,
    )
    db.add(db_reservation)
    await db.commit()
    await db.refresh(db_reservation)
    return db_reservation

# Получение всех бронирований с фильтрами
@router.get("/", response_model=list[ReservationResponse])
async def get_reservations(
    user_name: str = None,
    user_phone: str = None,
    user_email: str = None,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(models.Reservation)

    if user_name:
        stmt = stmt.where(models.Reservation.user_name.ilike(f"%{user_name}%"))
    if user_phone:
        stmt = stmt.where(models.Reservation.user_phone.ilike(f"%{user_phone}%"))
    if user_email:
        stmt = stmt.where(models.Reservation.user_email.ilike(f"%{user_email}%"))

    result = await db.execute(stmt)
    reservations = result.scalars().all()
    return reservations

# Получение по ID
@router.get("/{id}", response_model=ReservationResponse)
async def get_reservation(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Reservation).where(models.Reservation.id == id))
    reservation = result.scalar_one_or_none()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

# Обновление статуса
@router.patch("/{id}/status", response_model=ReservationResponse)
async def update_reservation_status(id: int, update: ReservationUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Reservation).where(models.Reservation.id == id))
    reservation = result.scalar_one_or_none()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    if update.status:
        reservation.status = update.status
        await db.commit()
        await db.refresh(reservation)

    return reservation