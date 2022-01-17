from optparse import Option
from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional, List

from travel_app.models.trekdestination import TrekDestination
from . import user_schema, itenary_schema, comment_schema, vote_schema



class TravelDestinationCreate(BaseModel):
    title: str
    days : int
    difficulty: str
    total_cost: str

    class Config:
        orm_mode = True


class TravelDestinationResponse(BaseModel):
    trek_id: int
    title: str
    days : int
    difficulty: str
    total_cost: str
    created_by : user_schema.UserName
    comment_count : int
    vote_count : int 
    class Config: 
        orm_mode = True


class TravelDestinationDetailResponse(TravelDestinationCreate):
    created_by: user_schema.UserNameEmail
    created_at : datetime
    itenaries : List[itenary_schema.IternaryResponse]
    comments : List[comment_schema.CommentsResponse]
    votes: List[vote_schema.VotedBy]
    class Config:
        orm_mode = True
    

