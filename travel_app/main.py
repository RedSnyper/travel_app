from fastapi import FastAPI
from travel_app.database.db import engine
from travel_app.models import user
from travel_app.database.db_model_init import add_models_to_database

app = FastAPI()

add_models_to_database()


@app.get("/")
def main():
    return {"message": "hello world"}

if __name__ == '__main__':
    main()