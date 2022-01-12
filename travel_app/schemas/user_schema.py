from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from sqlalchemy import orm


class User(BaseModel):
    full_name : str
    email: EmailStr

    class Config: 
        orm_mode = True

class UserWrittenDestinations(BaseModel):
    id: Optional[int] = 0
    title: Optional[str] = ''


class UserResponse(User):
    id: int
    # routes_written: UserWrittenDestinations
    phone_no: Optional[str] = None
    address : Optional[str] = None

    class Config: 
        orm_mode = True
