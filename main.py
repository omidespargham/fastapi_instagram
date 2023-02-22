from fastapi import FastAPI
from db.database import engine
from db.models import Base # we import it from model because some tables extends from the Base

app = FastAPI()

Base.metadata.create_all(engine)

@app.get("/")
def home():
    return "this is home page"
