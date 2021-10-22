from typing import Optional, List
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class TheNews(BaseModel):
    title: str
    preview_text: str
    full_text: str


class MarkUp(BaseModel):
    tags: Optional[List[str]]
    spheres: Optional[List[str]]

    class Config:
        orm_mode = True


class Job(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    status: str = "in_progress"
    exception: str = None
