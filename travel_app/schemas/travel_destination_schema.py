from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from . import user_schema, itenary_schema, comment_schema


class TravelDestinationCreate(BaseModel):
    id: int
    title: str
    days : int
    difficulty: str
    total_cost: str
    # itenaries: itenary_schema.IternaryCreate


class TravelDestinationResponse(TravelDestinationCreate):
    class Config: 
        orm_mode = True


class TravelDestinationDetailResponse(TravelDestinationResponse):
    created_by: user_schema.User
    created_at : datetime
    itenaries : List[itenary_schema.IternaryResponse]
    comments : List[comment_schema.CommentsResponse]

    class Config:
        orm_mode = True
    

