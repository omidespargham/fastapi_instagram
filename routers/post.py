from fastapi import APIRouter,Depends,HTTPException,status,UploadFile,File
from typing import List
import schema
from db import models
from sqlalchemy.orm import Session
from db.database import get_db
from db import post_db
from auth.oauth2 import oauth_scheme,get_current_user
import shutil


router = APIRouter(prefix="/post",tags=["post"])



IMGAE_URL_TYPES = [
    "url",
    "uploaded"
]
# ,token:str=Depends(oauth_scheme),
@router.post("/create_post",response_model=schema.PostShow)
def create_post(request:schema.PostBase,db:Session= Depends(get_db),
                current_user:schema.UserAuth = Depends(get_current_user)):
    if request.image_url_type not in IMGAE_URL_TYPES:
        raise HTTPException(status_code=404,detail="this url type is not correct !")
    return post_db.create_post(request,db)
     


@router.get("/get_all_posts",response_model=List[schema.PostShow])
def get_all_posts(db:Session = Depends(get_db)):
    return post_db.get_all_posts(db)




@router.post("/upload_file")
def upload_file(file:UploadFile=File(...)):
    path_file = f"uploaded_files/{file.filename}"
    with open(path_file,"w+b") as buffer:
        shutil.copyfileobj(file.file,buffer)
    
    return {"path_file":path_file}


@router.post("delete_post/{post_id}")
def delete_post(post_id:int,db:Session= Depends(get_db),current_user:schema.UserAuth = Depends(get_current_user)):
    post = db.query(models.Post).filter(models.Post.id==post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="the post dosent exist !")
    if post.user_id == current_user.id:
        db.delete(post)
        db.commit()
        return {"ok"}
    else:
        return {"this post is not for you to delete it !"}
