from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class AssignmentBase(BaseModel):
    title: str = Field(min_length=5, max_length=100)
    description: str = Field(min_length=10, max_length=500)
    subject_name: str = Field(min_length=2, max_length=50)
    semester: int = Field(gt=0, lt=9)
    tags: str = Field(min_length=2, max_length=100)

class AssignmentCreate(AssignmentBase):
    file_url: str = Field(min_length=10)

class AssignmentOut(AssignmentBase):
    id: int
    created_at: datetime
    author_id: int
    
    class Config:
        from_attributes = True