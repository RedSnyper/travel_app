from pydantic import BaseModel

class UserCreate(BaseModel):
    full_name : str
    address : str
    email: str
    phone_no: str