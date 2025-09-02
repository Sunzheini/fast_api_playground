from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    city: str
    email: Optional[str] = None
