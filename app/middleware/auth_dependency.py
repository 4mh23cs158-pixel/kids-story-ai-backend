from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt
import os

security = HTTPBearer()
SECRET = os.getenv("JWT_SECRET")

def verify_token(credentials = Depends(security)):

    try:
        payload = jwt.decode(
            credentials.credentials,
            SECRET,
            algorithms=["HS256"]
        )
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
