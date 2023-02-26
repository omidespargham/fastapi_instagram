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

