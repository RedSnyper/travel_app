from fastapi import FastAPI
from travel_app.database.db import engine
from travel_app.models import user
from travel_app.database.db_model_init import add_models_to_database
from travel_app.utils import fake_gen
app = FastAPI()

fake_gen.gen_fake_user(2)
@app.get("/")
async def main() -> dict:
    await add_models_to_database()
    await fake_gen.gen_fake_user(10)
    return {"message": "hello world"}

if __name__ == '__main__':
    main()