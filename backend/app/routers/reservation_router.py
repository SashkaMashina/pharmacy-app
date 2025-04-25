from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from app.models import models
from app.schemas.reservation import ReservationCreate, ReservationResponse, ReservationUpdate
from app.core.database import get_db
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter(prefix="/reservations", tags=["Reservations"])

# Создание бронирования
@router.post("/", response_model=ReservationResponse)
async def create_reservation(reservation: ReservationCreate, db: AsyncSession = Depends(get_db)):
    try:
        async with db.begin():  # начинаем транзакцию
            # Создание бронирования
            db_reservation = models.Reservation(
                user_name=reservation.user_name,
                user_phone=reservation.user_phone,
                user_email=reservation.user_email,
                status=reservation.status or "pending",
                total_sum=reservation.total_sum,
            )
            db.add(db_reservation)
            await db.flush()  # получаем ID новой записи

            # Добавляем позиции бронирования
            db_items = [
                models.ReservationItem(
                    reservation_id=db_reservation.id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    price=item.price,
                )
                for item in reservation.items
            ]
            db.add_all(db_items)

        # Обновляем и загружаем связанные items
        await db.refresh(db_reservation)

        result = await db.execute(
            select(models.Reservation)
            .options(selectinload(models.Reservation.items))
            .where(models.Reservation.id == db_reservation.id)
        )
        db_reservation = result.scalar_one()

        return db_reservation

    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating reservation: {str(e)}")

# Получение всех бронирований с фильтрами
@router.get("/", response_model=list[ReservationResponse])
async def get_reservations(
    user_name: str = None,
    user_phone: str = None,
    user_email: str = None,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(models.Reservation).options(selectinload(models.Reservation.items))

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
    result = await db.execute(
        select(models.Reservation)
        .options(selectinload(models.Reservation.items))
        .where(models.Reservation.id == id)
    )
    reservation = result.scalar_one_or_none()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

# Обновление статуса
@router.patch("/{id}/status", response_model=ReservationResponse)
async def update_reservation_status(id: int, update: ReservationUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(models.Reservation)
        .options(selectinload(models.Reservation.items))
        .where(models.Reservation.id == id)
    )
    reservation = result.scalar_one_or_none()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    if update.status:
        reservation.status = update.status
        await db.commit()
        await db.refresh(reservation)

    return reservation