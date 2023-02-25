from fastapi import APIRouter, Depends, HTTPException, Query,Body,status
from sqlalchemy.orm import Session
import schema
import db.models as models
from db.database import get_db
from typing import List
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from db.hash import Hash
from auth import oauth2


router = APIRouter(tags=["authentication"])

@router.post("/token")
def get_token(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user with this username dosent exist")
    
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="pass is not correct")
    
    access_token = oauth2.create_access_token(data={"sub":request.username})

    return {
        "access_token":access_token,
        "type_token":"bearer",
    }

