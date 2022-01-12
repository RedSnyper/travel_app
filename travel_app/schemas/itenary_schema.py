from pydantic import BaseModel

class IternaryCreate(BaseModel):
    day: int
    title: str
    description: str
    day_cost : int


class IternaryResponse(IternaryCreate):
    class Config: 
        orm_mode = True