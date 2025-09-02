from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class User(BaseModel):
    id: Optional[int] = Field(default=None, ge=1, description="Auto-generated positive integer ID")
    name: str = Field(min_length=1, max_length=100, description="User's full name")
    age: int = Field(ge=0, le=120, description="User's age between 0 and 120")
    city: str = Field(min_length=1, max_length=100, description="City name")
    email: Optional[EmailStr] = Field(default=None, description="Valid email address if provided")

    # Example data for documentation on swagger UI
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Alice",
                "age": 30,
                "city": "New York",
                "email": "eee",
            }
        }
    }
