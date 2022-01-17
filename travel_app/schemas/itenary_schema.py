from pydantic import BaseModel

class IternaryCreate(BaseModel):
    day: int
    title: str
    description: str
    day_cost : int

class IternaryUpdate(BaseModel):
    title: str
    description: str
    day_cost : int
    class Config:
        orm_mode = True

class IternaryResponse(IternaryCreate):
    class Config: 
        orm_mode = True