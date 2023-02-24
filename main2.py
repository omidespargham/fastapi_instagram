from pydantic import BaseModel
from fastapi import FastAPI,Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str = None
    full_name: str = None
    disabled: bool = None


def fake_decode_token(token,user):
    return User(
        username=user.username, email=user.email, full_name=user.full_name
    )


async def get_current_user(request:User,token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token,request)
    return user


@app.get("/users")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user