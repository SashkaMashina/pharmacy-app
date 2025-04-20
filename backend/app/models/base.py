from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# Импорты всех моделей, чтобы Alembic их увидел
from app.models import models  # пусть models.py содержит все классы