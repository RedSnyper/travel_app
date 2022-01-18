from pydantic import BaseModel
from . import user_schema
from datetime import datetime


class UserComment(BaseModel):
    commented_by: user_schema.UserNameEmail

class CommentCreate(BaseModel):
    comment: str

class CommentRes(BaseModel):
    comment_id : int
    comment : str
    commented_by: user_schema.UserName

    class Config: 
        orm_mode = True

class CommentsResponse(UserComment):
    comment_id: int
    comment : str
    created_at : datetime

    class Config:
        orm_mode = True

