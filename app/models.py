from pydantic import BaseModel, Field
from typing import Optional

class Address(BaseModel):
    city: str
    country: str

class StudentCreate(BaseModel):
    name: str
    age: int
    address: Address

class StudentUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    address: Optional[Address]

      # Update this for Pydantic V2 compatibility
