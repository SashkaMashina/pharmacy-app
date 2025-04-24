import datetime
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.database import async_session
from app.models import models
from sqlalchemy import text
import asyncio

async def seed():
    async with async_session() as db:

        # Очистка БД
        await db.execute(text('DELETE FROM reservation_items'))
        await db.execute(text('DELETE FROM reservations'))
        await db.execute(text('DELETE FROM products'))
        await db.execute(text('DELETE FROM categories'))
        await db.execute(text('DELETE FROM admins'))
        await db.commit()

        # 1. Категории
        category_names = ["Антибиотики", "Обезболивающие", "Витамины", "Антисептики", "Противоаллергические"]
        categories = [models.Category(name=name) for name in category_names]
        db.add_all(categories)
        await db.commit()

        # 2. Продукты
        products_data = [
            {
                "name": "Амоксициллин",
                "category": categories[0],
                "price": 200.0,
                "stock": 50,
                "description": "Антибиотик широкого спектра",
                "image_url": "https://images.apteka.ru/medium_1d07e626-bb3e-4c23-818f-71b3907b1b4b.webp",
                "manufacturer": "PharmaCorp",
                "release_form": "таблетки",
                "prescription_required": True,
            },
            {
                "name": "Ципрофлоксацин",
                "category": categories[0],
                "price": 300.0,
                "stock": 30,
                "description": "Противомикробное средство",
                "image_url": "https://images.apteka.ru/medium_91416b52-b716-4622-90de-0cfe4ee31980.webp",
                "manufacturer": "BioMed",
                "release_form": "таблетки",
                "prescription_required": True,
            },
            {
                "name": "Парацетамол",
                "category": categories[1],
                "price": 50.0,
                "stock": 100,
                "description": "Обезболивающее и жаропонижающее",
                "image_url": "https://images.apteka.ru/medium_3d5536b9-49b4-455a-8320-545ce45c4c85.webp",
                "manufacturer": "MediPharm",
                "release_form": "таблетки",
                "prescription_required": False,
            },
            {
                "name": "Ибупрофен",
                "category": categories[1],
                "price": 80.0,
                "stock": 80,
                "description": "Обезболивающее, противовоспалительное",
                "image_url": "https://images.apteka.ru/medium_e8e5d419-8a58-4d1d-b212-66535a2ac74d.webp",
                "manufacturer": "HealthLine",
                "release_form": "гель",
                "prescription_required": False,
            },
            {
                "name": "Витамин C",
                "category": categories[2],
                "price": 60.0,
                "stock": 200,
                "description": "Иммуностимулирующее средство",
                "image_url": "https://images.apteka.ru/medium_cb0cbd50-bdcc-4eba-8d3f-c1991b732bfe.webp",
                "manufacturer": "NutriLife",
                "release_form": "таблетки жевательные",
                "prescription_required": False,
            },
            {
                "name": "Витамин D",
                "category": categories[2],
                "price": 280.0,
                "stock": 150,
                "description": "Поддержка костей и иммунитета",
                "image_url": "https://images.apteka.ru/medium_3a737e44-1fde-43dd-84be-3065e230ab33.webp",
                "manufacturer": "ЭВАЛАР",
                "release_form": "таблетки",
                "prescription_required": False,
            },
            {
                "name": "Хлоргексидин",
                "category": categories[3],
                "price": 110.0,
                "stock": 300,
                "description": "Антисептическое средство",
                "image_url": "https://images.apteka.ru/medium_634583a7-2a1c-40d9-aa3d-bc66eba3915f.webp",
                "manufacturer": "RENEWAL",
                "release_form": "раствор",
                "prescription_required": False,
            },
            {
                "name": "Мирамистин",
                "category": categories[3],
                "price": 346.0,
                "stock": 120,
                "description": "Антисептик широкого спектра",
                "image_url": "https://images.apteka.ru/medium_af3a5e4b-b98a-4004-8f41-9a47a4a21410.webp",
                "manufacturer": "SafePharm",
                "release_form": "спрей",
                "prescription_required": False,
            },
            {
                "name": "Супрастин",
                "category": categories[4],
                "price": 90.0,
                "stock": 70,
                "description": "Антигистаминный препарат",
                "image_url": "https://images.apteka.ru/medium_0496ccfa-d597-41d0-8720-84bc5976e666.webp",
                "manufacturer": "AllerStop",
                "release_form": "таблетки",
                "prescription_required": False,
            },
            {
                "name": "Цетиризин",
                "category": categories[4],
                "price": 100.0,
                "stock": 60,
                "description": "Снимает симптомы аллергии",
                "image_url": "https://images.apteka.ru/medium_2b75b057-076a-4e77-9f9c-6f6de0c1134a.webp",
                "manufacturer": "Antiallerg",
                "release_form": "капли",
                "prescription_required": False,
            },
        ]

        now = datetime.datetime.utcnow()
        products = []
        for prod in products_data:
            products.append(models.Product(
                name=prod["name"],
                category_id=prod["category"].id,
                price=prod["price"],
                stock=prod["stock"],
                description=prod["description"],
                image_url=prod["image_url"],
                manufacturer=prod["manufacturer"],
                release_form=prod["release_form"],
                prescription_required=prod["prescription_required"],
                created_at=now,
                updated_at=now,
            ))
        db.add_all(products)
        await db.commit()

        # 3. Бронирования
        reservations = [
            models.Reservation(
                user_name="Анна Петрова",
                user_phone="+79995556677",
                user_email="anna@example.com",
                status="pending",
                total_sum=410.0,
                created_at=now
            ),
            models.Reservation(
                user_name="Дмитрий Сидоров",
                user_phone="+79993332211",
                user_email="dmitry@example.com",
                status="confirmed",
                total_sum=250.0,
                created_at=now
            ),
        ]
        db.add_all(reservations)
        await db.commit()

        # 4. Товары в заказе
        items = [
            models.ReservationItem(reservation_id=reservations[0].id, product_id=products[0].id, quantity=1, price=200.0),
            models.ReservationItem(reservation_id=reservations[0].id, product_id=products[4].id, quantity=1, price=60.0),
            models.ReservationItem(reservation_id=reservations[0].id, product_id=products[2].id, quantity=3, price=50.0),
            models.ReservationItem(reservation_id=reservations[1].id, product_id=products[9].id, quantity=2, price=100.0),
            models.ReservationItem(reservation_id=reservations[1].id, product_id=products[5].id, quantity=1, price=120.0),
        ]
        db.add_all(items)
        await db.commit()

        # 5. Администратор
        admin_username = "admin_pharmacy"
        admin_password_hash = "$2b$12$8JX6uWWK6.s4CCIMqSuYYeDfWWwGpl8tIas87GuBmczrNauuJ37Nm" 

        existing_admin = await db.execute(
            text("SELECT * FROM admins WHERE username = :username"),
            {"username": admin_username}
        )
        if not existing_admin.first():
            admin = models.Admin(
                username=admin_username,
                password_hash=admin_password_hash
            )
            db.add(admin)
            await db.commit()
            print(f"👤 Администратор '{admin_username}' добавлен.")
        else:
            print(f"ℹ️ Администратор '{admin_username}' уже существует.")

    print("✅ Seed-данные успешно добавлены.")

if __name__ == "__main__":
    asyncio.run(seed())