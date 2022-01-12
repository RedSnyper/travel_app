from pydantic import BaseModel
from . import user_schema, travel_destination_schema
from datetime import datetime


class CommentCreate(BaseModel):
    user_name : str #user_schema.UserCreate.full_name
    created_at : datetime

class CommentsResponse(CommentCreate):
    comments : str

    class Config:
        orm_mode = True

