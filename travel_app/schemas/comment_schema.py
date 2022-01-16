from pydantic import BaseModel
from . import user_schema, travel_destination_schema
from datetime import datetime


class UserComment(BaseModel):
    commented_by: user_schema.UserName

class CommentCreate(BaseModel):
    comment: str

class CommentsResponse(UserComment):
    comment_id: int
    comment : str
    created_at : datetime

    class Config:
        orm_mode = True

