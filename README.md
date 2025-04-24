# Старт проекта  
## Запуск контейнеров
Если не существуют: docker-compose up --build -d  
Если уже существуют и их заново нужно запустить: docker-compose start  


## Проверка работы
http://127.0.0.1:8000/docs

## Остановка контейнеров  
docker-compose stop  
docker-compose down  

## Запуск миграции для создания таблиц  
docker exec -it pharmacy-backend alembic revision --autogenerate -m "initial migration"  
Применение миграции к базе  
docker exec -it pharmacy-backend alembic upgrade head  