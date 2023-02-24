from fastapi import FastAPI
from db.database import engine
# we import it from model because some tables extends from the Base
from db.models import Base
from routers import user
app = FastAPI()

Base.metadata.create_all(engine)
app.include_router(user.router)


@app.get("/")
def home():
    return "this is home page"
