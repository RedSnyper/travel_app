from fastapi import APIRouter

from travel_app.api.api_vi.endpoints import users,travel_destinations,iternaries,comments,votes


api_router = APIRouter()

api_router.include_router(users.router)
api_router.include_router(travel_destinations.router)
api_router.include_router(iternaries.router)
api_router.include_router(comments.router)
api_router.include_router(votes.router)
