from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from db import database
from datetime import timedelta,datetime
from jose import jwt

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = '9e28d49e86c9ae965e0ccfd34ce18e85580100ed6bfb48553a03a17a7a3e2d98'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict,expires_delta: Optional[timedelta]= None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.Utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


