from fastapi import FastAPI
from db.database import SessionLocal, engine
from db import models
from router import home, listsize
from db.database import Base

app = FastAPI()
app.include_router(listsize.router)
app.include_router(home.router)

@app.get("/")
def read_root():
    return {"message": "luong oi cuu back"}

#models.Base.metadata.create_all(bind=engine)