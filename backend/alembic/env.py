import asyncio
from logging.config import fileConfig

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import pool
from alembic import context
from app.core.database import DATABASE_URL  # Импортируем URL базы данных
from app.models.base import Base  # Импортируем Base, чтобы Alembic видел модели

# Настройка логирования из alembic.ini
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Указываем, где искать модели
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Запуск миграций в offline-режиме (без подключения к БД)."""
    url = DATABASE_URL.replace("asyncpg", "psycopg2")  # Alembic не работает с asyncpg
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Запуск миграций в online-режиме (с подключением к БД)."""
    connectable = create_async_engine(DATABASE_URL, poolclass=pool.NullPool)

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


def do_run_migrations(connection):
    """Функция, выполняющая миграции в синхронном режиме."""
    context.configure(
        connection=connection, target_metadata=target_metadata
    )
    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())  # Асинхронный запуск
