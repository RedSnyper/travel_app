from pydantic import BaseModel
from . import user_schema

class VotedBy(BaseModel):
    voted_by: user_schema.UserNameEmail

    class Config:
        orm_mode = True
