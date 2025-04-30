# JWT Auth RBAC API with FastAPI 

This is a RESTful API built with FastAPI, SQLModel, and PostgreSQL that implements JWT Authentication and Role-Based Access Control (RBAC). It supports two user roles: `admin` and `user`. Admins can create, update, and delete projects, while users can only view them.

---

## Features

- JWT-based authentication
- Role-based access control (`admin`, `user`)
- CRUD operations on `Project`
- Swagger UI support
- PostgreSQL and SQLModel integration

---

## Tech Stack

- **FastAPI**
- **SQLModel**
- **PostgreSQL**
- **JWT (via `python-jose`)**
- **Swagger UI** (auto-generated)


Installation Steps
Clone the repository

git clone https://github.com/your-username/jwt-auth-rbac-api.git


Create and activate virtual environment

python -m venv env
env\Scripts\activate 

Install dependencies

pip install -r requirements.txt

Create .env file

DATABASE_URL
SECRET_KEY
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES

Run Alembic migrations
alembic upgrade head

Start the server
uvicorn main:app --reload


Visit the docs at:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

 Demo (Video Recording)
 https://www.loom.com/share/cfe59ca4e421475f96749f2f6bca48f9?sid=a22d9823-a699-4eaf-9542-d0ed215eb6cc

Testing
You can test the API using:

Swagger UI

Postman (import the collection from /docs)



