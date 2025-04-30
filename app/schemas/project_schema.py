# app/schemas/project_schema.py
from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    description: str

class ProjectRead(ProjectCreate):
    id: int

    class Config:
        orm_mode = True
