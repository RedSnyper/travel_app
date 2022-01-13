from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from sqlalchemy import orm


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
    class Config: 
        orm_mode = True
