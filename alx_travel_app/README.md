# ALX Travel App

A Django REST API for managing travel listings, built with PostgreSQL, Django REST Framework, and Swagger API documentation.

---

## 🚀 Project Features

- ✅ Django & DRF for API development
- ✅ PostgreSQL database (secure via `.env`)
- ✅ Swagger API docs available at `/swagger/`
- ✅ CORS configured for API access
- ✅ Flexible dependency management: `requirements.txt`
- ✅ Git version control setup

---

## 📁 Project Structure

```
alx_travel_app/
├── alx_travel_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├──listings/
│   ├──management/
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── seed.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── README.md
├── manage.py
├── requirements.txt
├── .env
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1 Clone the Repository

```bash
git clone https://github.com/your-username/alx_travel_app_0x00.git
cd alx_travel_app
```

---

### 2 Environment Setup (Two Options)

\*\*Option A: Traditional \*\*`** + **`

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

\*\*Option B: Using \*\*\`\`

```bash
pip install pipenv
pipenv install -r requirements.txt
pipenv lock
pipenv shell
```

> ⚠ If switching between methods, ensure dependencies stay in sync:
>
> ```bash
> pip freeze > requirement.txt
> or
> pipenv lock -r > requirements.txt
> ```

---

### 3 Configure Environment Variables

Create a `.env` file:

```ini
DEBUG=True # don't run with debug turned on in production!
SECRET_KEY=your_secret_key

DB_NAME=alx_travel_app_db
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

---

### 4 Run Migrations & Server

```bash
python manage.py migrate
python manage.py runserver
```

---

## 📖 API Documentation

Swagger UI available at:

```bash
http://127.0.0.1:8000/swagger/
```

---

## 💈 Database

- PostgreSQL configured via `.env`
- Uses `django-environ` for secure environment variable handling

---

## 📂 .gitignore Highlights

```
# Ignore virtual environment
venv/
.env
*.pyc
__pycache__/
*.log
*.sqlite3

# Optional: If not using Pipenv
# Pipfile
# Pipfile.lock
```

---

## Notes

- Use either venv or pipenv, but avoid mixing them in the same workflow.

- Keep requirements.txt and Pipfile consistent by regenerating after changes.