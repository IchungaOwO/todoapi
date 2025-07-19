from pydantic import BaseModel
from schemas.tag import TagResponse
from typing import List, Optional

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    tag_ids: list[int] = []

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    tags: List[TagResponse] = []
    class Config:
        orm_mode = True