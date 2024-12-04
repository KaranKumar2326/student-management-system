from typing import Optional
from pydantic import BaseModel
from app.models import Address

class StudentOut(BaseModel):
    name: str
    age: int
    address: Address

class StudentUpdate(BaseModel):
    name: Optional[str]  # Optional name
    age: Optional[int]   # Optional age
    address: Optional[Address]    # Make address optional


    class Config:
        orm_mode = True



    class Config:
        from_attributes = True  # Update this for Pydantic V2 compatibility
