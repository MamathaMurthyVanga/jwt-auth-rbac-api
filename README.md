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

---

## Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/your-username/jwt-auth-rbac-api.git
```


2. Create and activate virtual environment
```bash
python -m venv env
env\Scripts\activate 
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create .env file                                                                                    
Add the following variables to the .env file:                                                          
DATABASE_URL=your_database_url                                                                        
SECRET_KEY=your_secret_key                                                                            
ALGORITHM=HS256                                                                                       
ACCESS_TOKEN_EXPIRE_MINUTES=30                                                                        

5. Run Alembic migrations
alembic upgrade head

6. Start the server
```bash
uvicorn main:app --reload
```


Visit the docs at:
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

Demo (Video Recording)
https://www.loom.com/share/cfe59ca4e421475f96749f2f6bca48f9?sid=a22d9823-a699-4eaf-9542-d0ed215eb6cc

https://drive.google.com/file/d/1rBNC0ASUTslCEnWOZvReB0FcBsb7pUGz/view?usp=sharing

