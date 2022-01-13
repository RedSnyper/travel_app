from pydantic import BaseModel
from . import user_schema, travel_destination_schema
from datetime import datetime


class UserComment(BaseModel):
    comment_by_user: int #user_schema.UserCreate.full_name
    created_at : datetime


class CommentsResponse(BaseModel):
    comment : str

    class Config:
        orm_mode = True

