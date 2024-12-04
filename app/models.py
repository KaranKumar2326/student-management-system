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
    name: Optional[str] = Field(default=None)
    age: Optional[int] = Field(default=None)
    address: Optional[Address] = Field(default=None)

      # Update this for Pydantic V2 compatibility
