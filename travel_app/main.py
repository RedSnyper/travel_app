from fastapi import FastAPI
from .database import *
from . import models
from .database.db import engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()



@app.get("/")
def main():
    return {"message": "hello world"}

if __name__ == '__main__':
    main()