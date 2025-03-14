# Wishlist Service

Сервис для создания списков желаемых товаров. Пользователи могут создавать списки, добавлять товары с описанием, ценами и ссылками, делиться списками с друзьями или оставлять их приватными. Поддерживаются статусы ("Хочу", "Куплено", "Подарено").

## Структура проекта

Проект разделён на:
- **Бэкенд**: Flask-приложение с использованием Blueprints, SQLAlchemy, Flask-Login и Flask-Migrate.
- **Фронтенд**: чистые HTML-шаблоны, CSS и JavaScript.

## Установка и запуск

1. Создайте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate   # для Linux/Mac
   venv\Scripts\activate      # для Windows
