# app/routes/auth_routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user_schema import UserCreate, Token
from app.services import auth_service

router = APIRouter(tags=["Auth"])

@router.post("/register")
def register(user: UserCreate):
    existing = auth_service.authenticate_user(user.username, user.password)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = auth_service.register_user(user)
    return {"message": "User registered successfully"}
    
    

@router.post("/login", response_model=Token)
def login(form_data: UserCreate):
    user = auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = auth_service.generate_token(user)
    return {"access_token": token, "token_type": "bearer"}
