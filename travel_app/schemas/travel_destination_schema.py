from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from . import user_schema, itenary_schema, comment_schema

class Trek(BaseModel):
    title: str

class TravelDestinationCreate(Trek):
    title: str
    days : int
    difficulty: str
    total_cost: str
    # itenaries: itenary_schema.IternaryCreate
    created_at : datetime

class TravelDestinationResponse(TravelDestinationCreate):
    created_by: user_schema.User
    
    # itenaries : itenary_schema.IternaryResponse
    # comments : comment_schema.CommentsResponse
    class Config: 
        orm_mode = True



