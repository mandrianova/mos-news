from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class NewsItem(BaseModel):
    id: int
    title: str
    date: str


class RecommendationAndHistoryOut(BaseModel):
    recommendations: Optional[List[NewsItem]]
    history: Optional[List[NewsItem]]
