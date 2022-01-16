from pydantic import BaseModel
from pydantic.types import conint

from . import user_schema

class VotedBy(BaseModel):
    voted_by: user_schema.UserName

    class Config:
        orm_mode = True

class Vote(BaseModel):
    post_id : int
    dir : conint(le=1 , ge=0)