from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    # Allow login via username OR email
    identifier: str  
    password: str

class Token(BaseModel):
    token: str
