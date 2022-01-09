from fastapi import FastAPI
from travel_app.database.db import engine
from travel_app.models import user
user.Base.metadata.create_all(bind=engine)


app = FastAPI()



@app.get("/")
def main():
    return {"message": "hello world"}

if __name__ == '__main__':
    main()