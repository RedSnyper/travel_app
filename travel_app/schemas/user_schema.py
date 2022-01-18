from pydantic import BaseModel, EmailStr
from typing import Optional, List


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
    phone_no: Optional[str] = None
    address : Optional[str] = None
    class Config:
        orm_mode = True

class UserDetailResponse(UserResponse):
    routes_written: List[UserWrittenRoute] = []
    class Config: 
        orm_mode = True
