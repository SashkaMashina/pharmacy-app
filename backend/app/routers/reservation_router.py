from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from app.models import models
from app.schemas.reservation import ReservationCreate, ReservationResponse, ReservationUpdate
from app.core.database import get_db
from sqlalchemy.exc import SQLAlchemyError
from app.services.email_service import send_email

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
            
            # Отправляем email пользователю о бронировании
            email_body = (
                f"Здравствуйте, {reservation.user_name}!\n\n"
                f"Вы успешно забронировали товары на сумму {reservation.total_sum:.2f} ₽.\n\n"
                f"Мы сообщим, когда их можно будет забрать.\n"
                f"Спасибо за бронирование!"
            )
            await send_email(
                to_email=reservation.user_email,
                subject="Ваше бронирование в аптеке",
                body=email_body,
            )

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
        .options(
            selectinload(models.Reservation.items).selectinload(models.ReservationItem.product)
        )
        .where(models.Reservation.id == id)
    )
    reservation = result.scalar_one_or_none()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    if update.status:
        reservation.status = update.status
        await db.commit()
        await db.refresh(reservation)
        
        # Если бронирование подтверждено — отправляем письмо
        if update.status == "confirmed":
            items_list = "\n".join(
                [
                    f"- {item.product.name}: {item.quantity} шт. по {item.price:.2f} ₽"
                    for item in reservation.items
                ]
            )
            email_body = (
                f"Здравствуйте, {reservation.user_name}!\n"
                f"Товары можно забирать из пункта выдачи.\n\n"
                f"Товары:\n{items_list}\n\n"
                f"Спасибо, что выбрали нас!"
            )
            await send_email(
                to_email=reservation.user_email,
                subject="Товары поступили в пункт выдачи",
                body=email_body,
            )

    return reservation