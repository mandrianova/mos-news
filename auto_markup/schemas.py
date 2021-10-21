from typing import Optional, List
from pydantic import BaseModel


class TheNews(BaseModel):
    title: str
    preview_text: str
    full_text: str


class MarkUp(BaseModel):
    tags: Optional[List[str]]
    spheres: Optional[List[str]]

    class Config:
        orm_mode = True
