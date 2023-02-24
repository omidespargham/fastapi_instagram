from pydantic import BaseModel

class UserBase(BaseModel):
    username:str
    email:str
    password:str

class UserShow(BaseModel):
    username:str
    email:str



