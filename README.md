# Старт проекта  
## Запуск контейнеров
Если не существуют: docker-compose up --build -d  
Если уже существуют и их заново нужно запустить: docker-compose start  

## Проверка работы
http://127.0.0.1:8000/docs

## Остановка контейнеров  
docker-compose stop  
docker-compose down  

## Первая инициализация проекта  
1. Сначала запускаем контейнеры  
**docker-compose up --build -d**  

2. Запускаем миграции  
**docker exec -it pharmacy-backend alembic revision --autogenerate -m "initial migration"**  
Применение миграции к базе  
**docker exec -it pharmacy-backend alembic upgrade head**  

3. Заносим данные в созданные таблицы (для начала нужно проверить их существование)  
Заходим внутрь контейнера  
**docker exec -it pharmacy-backend bash**  
Внутри пишем следующую команду  
**PYTHONPATH=/app python app/utils/seed_db.py**  
Дожидаемся ответа:  
👤 Администратор 'admin_pharmacy' добавлен.  
✅ Seed-данные успешно добавлены.  
Выходим из контейнера: **exit**  

Таблички созданы и вних уже загружены все нужные данные!