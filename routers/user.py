from fastapi import APIRouter,Depends
from typing import List
import schema
from db import models
from sqlalchemy.orm import Session
from db.database import get_db
from db import user_db
router = APIRouter(prefix="/user",tags=["user"])

@router.post("/create_user",response_model=schema.UserShow)
def create_user(request:schema.UserBase,db:Session=Depends(get_db)):
    return user_db.create_user(request,db)

@router.get("/get_all_users",response_model=List[schema.UserShow])
def get_all_users(db:Session=Depends(get_db)):
    users = db.query(models.User).all()
    return users

