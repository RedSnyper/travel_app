from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
from sqlalchemy import orm

class UserWrittenRoute(BaseModel):
    id: int
    title: str
    class Config: 
        orm_mode = True

class User(BaseModel):
    full_name : str
    email: EmailStr

    class Config: 
        orm_mode = True

class UserCreate(User):
    password: str
    address : Optional[str] = None
    phone_no: Optional[str] = None
    
class UserResponse(User):
    id: int
    phone_no: Optional[str] = None
    address : Optional[str] = None
    routes_written: List[UserWrittenRoute] = []
    class Config: 
        orm_mode = True
