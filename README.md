# HW12 - FastAPI REST API з авторизацією, ролями та email-підтвердженням

## 📌 Опис

Це REST API застосунок, побудований з використанням **FastAPI**, який підтримує:

- Реєстрацію та логін користувачів
- Авторизацію з JWT токенами
- Ролі користувачів (наприклад, admin / user)
- Підтвердження email-адреси
- CRUD-операції з базою даних
- Контейнеризацію через Docker
- Міграції бази даних через Alembic

---

## ⚙️ Технології

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Docker](https://www.docker.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [JWT](https://jwt.io/)
- [Uvicorn](https://www.uvicorn.org/)
- Email-сервіс (`smtplib`)

---

## 📁 Структура проєкту

├── main.py # Точка входу
├── auth.py # Авторизація користувача
├── auth_services.py # JWT та логіка токенів
├── users.py # Обробка користувачів
├── crud.py # CRUD-операції
├── models.py # SQLAlchemy моделі
├── schemas.py # Pydantic-схеми
├── config.py # Налаштування застосунку
├── db.py # Підключення до БД
├── send_email.py # Відправка email
├── roles.py # Система ролей
├── docker-compose.yml # Docker-конфігурація
├── alembic.ini # Налаштування міграцій
├── .env.example # Приклад налаштувань середовища




---

## 🚀 Як запустити

### 1. Клонуй репозиторій

```bash
git clone https://github.com/your-username/HW12.git
cd HW12
2. Створи .env файл
На основі .env.example, додай свій:
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
SECRET_KEY=your_secret_key
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_email_password
3. Запуск через Docker
docker-compose up --build
4. Міграції бази даних (через Alembic)
alembic upgrade head
🧪 Тестування API
Після запуску:
Відкрий Swagger-документацію за адресою:
http://localhost:8000/docs
Там можна протестувати:

/auth/signup

/auth/login

/users/

/confirm-email

інші ендпоінти
