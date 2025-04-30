# app/schemas/user_schema.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from app.models.user import RoleEnum

class UserCreate(BaseModel):
    username: str
    # email: EmailStr
    password: str
    role: RoleEnum

class UserRead(BaseModel):
    id: int
    username: str
    # email: EmailStr
    role: RoleEnum

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
