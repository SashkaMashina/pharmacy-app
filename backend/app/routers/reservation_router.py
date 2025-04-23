from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import models
from app.schemas.reservation import ReservationCreate, ReservationResponse, ReservationUpdate
from app.core.database import get_db

router = APIRouter(tags=["Reservations"])

# Создание бронирования
@router.post("/", response_model=ReservationResponse)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    db_reservation = models.Reservation(
        user_name=reservation.user_name,
        user_phone=reservation.user_phone,
        user_email=reservation.user_email,
        status=reservation.status,
        total_sum=reservation.sum,
    )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

# Получение всех бронирований с фильтрами
@router.get("/", response_model=list[ReservationResponse])
def get_reservations(
    user_name: str = None,
    user_phone: str = None,
    user_email: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Reservation)

    if user_name:
        query = query.filter(models.Reservation.user_name.ilike(f"%{user_name}%"))
    if user_phone:
        query = query.filter(models.Reservation.user_phone.ilike(f"%{user_phone}%"))
    if user_email:
        query = query.filter(models.Reservation.user_email.ilike(f"%{user_email}%"))

    return query.all()

# Получение по ID
@router.get("/{id}", response_model=ReservationResponse)
def get_reservation(id: int, db: Session = Depends(get_db)):
    reservation = db.query(models.Reservation).filter(models.Reservation.id == id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

# Обновление статуса
@router.patch("/{id}/status", response_model=ReservationResponse)
def update_reservation_status(id: int, update: ReservationUpdate, db: Session = Depends(get_db)):
    reservation = db.query(models.Reservation).filter(models.Reservation.id == id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    if update.status:
        reservation.status = update.status
        db.commit()
        db.refresh(reservation)

    return reservation