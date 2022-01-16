import email
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
from sqlalchemy import orm

class UserWrittenRoute(BaseModel):
    trek_id: int
    title: str
    class Config: 
        orm_mode = True

class UserName(BaseModel):
    full_name: str

    class Config: 
        orm_mode = True


class UserNameEmail(UserName):
    email: EmailStr

    class Config: 
        orm_mode = True

    

class UserCreate(UserNameEmail):
    password: str
    address : Optional[str] = None
    phone_no: Optional[str] = None
    
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name : str

    class Config:
        orm_mode = True


class UserDetailResponse(UserResponse):
    phone_no: Optional[str] = None
    address : Optional[str] = None
    routes_written: List[UserWrittenRoute] = []
    class Config: 
        orm_mode = True
