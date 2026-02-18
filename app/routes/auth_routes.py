from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from jose import jwt
import os
from app.database import db

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET = os.getenv("JWT_SECRET")

@router.post("/signup")
def signup(user: dict):
    hashed = pwd_context.hash(user["password"])
    db.users.insert_one({
        "name": user["name"],
        "email": user["email"],
        "password": hashed
    })
    token = jwt.encode({"email": user["email"]}, SECRET)
    return {"token": token}

@router.post("/login")
def login(user: dict):
    existing = db.users.find_one({"email": user["email"]})
    if not existing:
        raise HTTPException(status_code=400, detail="User not found")
    
    if not pwd_context.verify(user["password"], existing["password"]):
        raise HTTPException(status_code=400, detail="Wrong password")

    token = jwt.encode({"email": user["email"]}, SECRET)
    return {"token": token}
