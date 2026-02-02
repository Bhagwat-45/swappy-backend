from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class ProfileBase(BaseModel):
    email: EmailStr = Field(description="Official university or personal email")
    full_name: str = Field(min_length=2, max_length=50)
    usn_id: str = Field(min_length=5, description="University Serial Number")
    semester: int = Field(gt=0, lt=9)

class ProfileCreate(ProfileBase):
    password: str = Field(min_length=8, max_length=15)

class ProfileOut(ProfileBase):
    id: int 
    is_verified: bool = False
    tech_stack: Optional[str] = Field(None, min_length=2)
    bio: Optional[str] = Field(None, max_length=500)

    class Config:
        from_attributes = True