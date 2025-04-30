# app/services/auth_service.py
from sqlmodel import Session, select
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.core.security import get_password_hash, verify_password, create_access_token
from app.core.config import settings
from app.db.database import engine
from datetime import timedelta

def register_user(user_data: UserCreate):
    with Session(engine) as session:
        user = User(
            username=user_data.username,
            # email=user_data.email,
            hashed_password=get_password_hash(user_data.password),
            role=user_data.role
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

def authenticate_user(username: str, password: str):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.username == username)).first()
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user

def generate_token(user: User):
    token_data = {"sub": user.username}
    return create_access_token(
        data=token_data,
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
