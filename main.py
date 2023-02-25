from fastapi import FastAPI
from db.database import engine
# we import it from model because some tables extends from the Base
from db.models import Base
from routers import user, post
from auth import authentication
# this should be mount in main file not routers
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/files", StaticFiles(directory="uploaded_files"),
          name="files")
# app.mount()
Base.metadata.create_all(engine)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(authentication.router)


@app.get("/")
def home():
    return "this is home page"
