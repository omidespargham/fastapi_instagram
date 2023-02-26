from pydantic import BaseModel
from datetime import datetime



# user schema 
class UserBase(BaseModel):
    username:str
    email:str
    password:str

class UserShow(BaseModel):
    id:int
    username:str
    email:str

    class Config:
        orm_mode = True


class UserAuth(BaseModel):
    user_id:int
    username:str
    email:str
    
# post schema 

class PostBase(BaseModel):
    image_url:str
    image_url_type:str
    caption:str
    user_id:int

class PostUserShow(BaseModel):
    id:int
    username:str

    class Config:
        orm_mode = True

class PostShow(BaseModel):
    id:int
    image_url:str
    image_url_type:str
    caption:str
    timestamp:datetime
    user:PostUserShow

    class Config:
        orm_mode = True

# comment schema

class CommentUserShow(BaseModel):
    id:int
    username:str
    email:str

    class Config:
        orm_mode = True

class CommentPostShow(BaseModel):
    id:int
    caption:str

class CommentBase(BaseModel):
    text:str
    timestamp:datetime
    user_id:int
    post_id:int

class CommentShow(BaseModel):
    id:int
    text:str
    timestamp:datetime
    user:CommentUserShow
    post:CommentPostShow

