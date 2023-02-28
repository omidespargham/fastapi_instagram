from fastapi import APIRouter,Depends,HTTPException,status,UploadFile,File
from typing import List
import schema
from db import models
from sqlalchemy.orm import Session
from db.database import get_db
from db import comment_db
from auth.oauth2 import oauth_scheme,get_current_user
import shutil

router = APIRouter(prefix="/comment",tags=["comment"])


@router.post("/create_comment",response_model=schema.CommentShow)
def create_comment(request:schema.CommentBase,db:Session = Depends(get_db),
                   current_user:schema.UserAuth = Depends(get_current_user)):
    comment = comment_db.create_comment(user_id=current_user.id,request=request,db=db)
    return comment

