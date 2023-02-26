from fastapi import HTTPException
from db.models import User
from schema import UserBase
from sqlalchemy.orm import Session
from db.hash import Hash

def create_user(request:UserBase,db:Session):
    user = User(
        username=request.username,
        email = request.email,
        password = Hash.bcrypt(request.password) # Should be hash
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_username(username:str,db:Session):
    user  = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404,detail="user not found !")

    return user

