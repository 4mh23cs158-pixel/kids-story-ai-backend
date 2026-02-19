from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import bcrypt
from jose import jwt
import os
from app.database import get_db
from app.models.user_models import User
from app.schemas.auth_schemas import UserCreate, UserLogin, Token

router = APIRouter()

SECRET = os.getenv("JWT_SECRET")

@router.post("/signup", response_model=Token)
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    hashed = bcrypt.hashpw(user_data.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    
    existing_email = db.query(User).filter(User.email == user_data.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    new_user = User(
        username=user_data.username,
        name=user_data.name,
        email=user_data.email,
        password=hashed
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = jwt.encode({"email": new_user.email, "username": new_user.username}, SECRET)
    return {"token": token}

@router.post("/login", response_model=Token)
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    # Try to find by email first, then username
    user = db.query(User).filter(
        (User.email == login_data.identifier) | (User.username == login_data.identifier)
    ).first()

    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    
    if not bcrypt.checkpw(login_data.password.encode("utf-8"), user.password.encode("utf-8")):
        raise HTTPException(status_code=400, detail="Wrong password")

    token = jwt.encode({"email": user.email, "username": user.username}, SECRET)
    return {"token": token}
