from fastapi import FastAPI
from travel_app.database.db import engine
from travel_app.models import user
from travel_app.database.db_model_init import add_models_to_database
from fastapi.middleware.cors import CORSMiddleware
from travel_app.api.api_vi.api import api_router
from travel_app.api.api_vi.endpoints import login

app = FastAPI(title="Elective_Travel_App")
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"], 
    allow_headers = ["*"]
)

app.include_router(api_router, prefix='/api/api_v1')
app.include_router(login.router)

@app.get("/")
async def main() -> dict:
    await add_models_to_database() 
    return {"message": "hello world"}

if __name__ == '__main__':
    main()